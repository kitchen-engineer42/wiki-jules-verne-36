#!/usr/bin/env python3
"""reconstruct_corpus.py — 从 Calibre pandoc 输出重建凡尔纳全集章节结构。

Calibre epub 转出的 book.md 没有 Markdown 标题：作品名/章节名以居中大写
段落（styled div）呈现。本脚本：
  1. 依 ToC 的 36 部作品，定位每部在正文中的起始行（标题匹配）；
  2. 在每部范围内识别章节行（CHAPTER/PART/罗马数字）→ 二级标题；
  3. 清洗 Calibre 噪声（::: 围栏、[]{#anchor}、{.class} span）；
  4. 段落间保留空行，输出 doc_final.md。

用法:
    python3 wiki/scripts/reconstruct_corpus.py --detect      # 只报告作品边界
    python3 wiki/scripts/reconstruct_corpus.py --emit OUT.md # 生成终稿
"""
import argparse
import re
import sys
from pathlib import Path

SRC = Path("corpus/raw/book.md")

# 36 部作品：ToC 顺序编号 + 规范展示名（含正文中可能出现的别名/大写变体）
# aliases 用于匹配正文标题行（规范化后比较）。
WORKS = [
    ("Twenty Thousand Leagues Under the Sea", ["20,000 LEAGUES UNDER THE SEA", "TWENTY THOUSAND LEAGUES UNDER THE SEA", "TWENTY THOUSAND LEAGUES UNDER THE SEAS"]),
    ("A Journey to the Center of the Earth", ["A JOURNEY TO THE CENTER OF THE EARTH", "JOURNEY TO THE CENTER OF THE EARTH", "JOURNEY TO THE CENTRE OF THE EARTH"]),
    ("Around the World in Eighty Days", ["AROUND THE WORLD IN EIGHTY DAYS", "AROUND THE WORLD IN 80 DAYS"]),
    ("The Mysterious Island", ["THE MYSTERIOUS ISLAND"]),
    ("From the Earth to the Moon", ["FROM THE EARTH TO THE MOON"]),
    ("Round the Moon", ["ROUND THE MOON", "AROUND THE MOON"]),
    ("A Voyage in a Balloon", ["A VOYAGE IN A BALLOON", "A VOYAGE IN A BALOON"]),
    ("Doctor Ox's Experiment", ["DOCTOR OX'S EXPERIMENT", "DR OX'S EXPERIMENT", "DR. OX'S EXPERIMENT"]),
    ("Master Zacharius", ["MASTER ZACHARIUS", "MASTER ZACHARIUS; OR, THE CLOCKMAKER WHO LOST HIS SOUL"]),
    ("A Drama in the Air", ["A DRAMA IN THE AIR"]),
    ("A Winter Amid the Ice", ["A WINTER AMID THE ICE", "A WINTER AMONG THE ICE FIELDS"]),
    ("Ascent of Mont Blanc", ["ASCENT OF MONT BLANC", "THE FORTIETH FRENCH ASCENT OF MONT BLANC"]),
    ("An Antarctic Mystery", ["AN ANTARCTIC MYSTERY", "THE SPHINX OF THE ICE FIELDS"]),
    ("Dick Sand: A Captain at Fifteen", ["DICK SAND; OR, A CAPTAIN AT FIFTEEN", "DICK SAND", "A CAPTAIN AT FIFTEEN"]),
    ("Eight Hundred Leagues on the Amazon", ["EIGHT HUNDRED LEAGUES ON THE AMAZON", "800 LEAGUES ON THE AMAZON"]),
    ("Facing the Flag", ["FACING THE FLAG"]),
    ("Five Weeks in a Balloon", ["FIVE WEEKS IN A BALLOON", "FIVE WEEKS IN A BALOON"]),
    ("Godfrey Morgan", ["GODFREY MORGAN", "GODFREY MORGAN: A CALIFORNIAN MYSTERY", "THE SCHOOL FOR CRUSOES"]),
    ("The Adventures of Captain Hatteras", ["THE ADVENTURES OF CAPTAIN HATTERAS", "THE ENGLISH AT THE NORTH POLE"]),
    ("In Search of the Castaways", ["IN SEARCH OF THE CASTAWAYS", "THE CHILDREN OF CAPTAIN GRANT"]),
    ("Michael Strogoff", ["MICHAEL STROGOFF", "MICHAEL STROGOFF; OR, THE COURIER OF THE CZAR"]),
    ("Off on a Comet", ["OFF ON A COMET", "OFF ON A COMET!", "HECTOR SERVADAC", "OFF ON A COMET OR HECTOR SERVADAC"]),
    ("Robur the Conqueror", ["ROBUR THE CONQUEROR", "THE CLIPPER OF THE CLOUDS"]),
    ("The Adventures of a Special Correspondent", ["THE ADVENTURES OF A SPECIAL CORRESPONDENT", "CLAUDIUS BOMBARNAC"]),
    ("The Blockade Runners", ["THE BLOCKADE RUNNERS"]),
    ("The Fur Country", ["THE FUR COUNTRY", "THE FUR COUNTRY; OR, SEVENTY DEGREES NORTH LATITUDE"]),
    ("The Master of the World", ["THE MASTER OF THE WORLD", "MASTER OF THE WORLD"]),
    ("The Pearl of Lima", ["THE PEARL OF LIMA", "THE PEARL OF LIMA: A STORY OF TRUE LOVE"]),
    ("The Secret of the Island", ["THE SECRET OF THE ISLAND"]),
    ("The Survivors of the Chancellor", ["THE SURVIVORS OF THE CHANCELLOR", "THE SURVIVORS OF THE CHANCELLOR: DIARY OF J.R. KAZALLON, PASSENGER"]),
    ("The Underground City", ["THE UNDERGROUND CITY", "THE BLACK INDIES", "THE CHILD OF THE CAVERN"]),
    ("The Waif of the Cynthia", ["THE WAIF OF THE CYNTHIA", "SALVAGE FROM THE CYNTHIA"]),
    ("Ticket No. 9672", ["TICKET NO. 9262", "TICKET NO. 9672", "THE LOTTERY TICKET"]),
    ("Topsy Turvy", ["TOPSY TURVY", "THE PURCHASE OF THE NORTH POLE"]),
    ("In the Year 2889", ["IN THE YEAR 2889"]),
]

CHAPTER_KW_RE = re.compile(r"^(CHAPTER|LETTER|SECTION|BOOK)\b\.?\s*(.*)$", re.I)
PART_RE = re.compile(r"^((FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH)\s+PART|PART\s+(THE\s+)?([A-Z0-9]+))\b\.?\s*(.*)$", re.I)

ANCHOR_RE = re.compile(r"\[\]\{#[^}]*\}")
FENCE_RE = re.compile(r"^:::")
ATTR_ONLY_RE = re.compile(r"^\{[^}]*\}$")


def _upper_ratio(t: str) -> float:
    letters = [c for c in t if c.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for c in letters if c.isupper()) / len(letters)


def is_title_line(s: str) -> bool:
    """判断某行是否像章节小标题（短、无句末标点、非正文段落）。"""
    t = s.strip()
    if not t or len(t) > 90:
        return False
    if t.endswith((".", "?", "!", ",", ";", ":", '"')):
        return False
    return _upper_ratio(t) > 0.6  # 多为大写 → 标题


def chapter_head(t: str):
    """若该行是章节标题（CHAPTER/LETTER/SECTION/BOOK + 大写短行），
    返回 (head, inline_rest)，否则 None。兼容罗马/阿拉伯/序数词编号。"""
    m = CHAPTER_KW_RE.match(t)
    if not m:
        return None
    # 短行 + 关键字开头即视为章节标题（兼容 "Chapter I" 标题式大小写）。
    # 仅用 upper_ratio 排除较长的正文行（如 "Chapter one was the happiest..."）。
    if len(t) > 75:
        return None
    if len(t) > 40 and _upper_ratio(t) < 0.6:
        return None
    kw = m.group(1).upper()
    rest = m.group(2).strip().rstrip(".")
    # rest 里可能同时含编号与小标题（"XIX. GALLIA'S GOVERNOR"）；整体保留
    return kw, rest


def norm(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\\", "", s)               # 去反斜杠转义
    s = re.sub(r"[^A-Za-z0-9 ]", " ", s)   # 去标点
    s = re.sub(r"\s+", " ", s)
    return s.strip().upper()


def load_body_start(lines):
    """跳过封面/版权/ToC，返回正文首行索引（ToC 结束的 ::: 之后）。"""
    # ToC 以 "CONTENTS" 起，正文标题 "1. IN THE YEAR 2889" 之后有一行 ":::"
    for i, ln in enumerate(lines):
        if norm(ln) == "IN THE YEAR 2889" and i > 60 and "]" in lines[i]:
            # 这是 ToC 最后一项（带链接）；其后的 ::: 收尾
            for j in range(i, min(i + 6, len(lines))):
                if lines[j].strip() == ":::":
                    return j + 1
    return 0


def detect(lines):
    start = load_body_start(lines)
    # 别名 → work index
    alias_map = {}
    for idx, (_, aliases) in enumerate(WORKS):
        for a in aliases:
            alias_map.setdefault(norm(a), idx)
    # 收集每部作品的所有候选行（标题在正文中可能多次出现，如三部曲的
    # 分卷标题也叫某独立作品名）。
    cands = {}  # work idx -> [line no, ...]
    for i in range(start, len(lines)):
        key = norm(lines[i])
        if not key or len(key) < 5:
            continue
        idx = alias_map.get(key)
        if idx is not None:
            cands.setdefault(idx, []).append(i)
    # 按 ToC 顺序单调赋值：每部选取「晚于上一部已赋行」的最早候选，
    # 从而排除嵌在前一部作品体内的分卷标题（如 Mysterious Island 内的
    # "THE SECRET OF THE ISLAND" 分卷头）。
    found = {}
    last = -1
    for idx in range(len(WORKS)):
        cs = cands.get(idx)
        if not cs:
            continue
        pick = next((c for c in cs if c > last), None)
        if pick is None:
            pick = cs[0]  # 无单调候选，回退首个（并保持 last 不倒退）
        found[idx] = pick
        last = max(last, pick)
    return start, found


def clean_line(s: str) -> str:
    s = ANCHOR_RE.sub("", s)
    s = s.replace("\\", "")  # 去 pandoc 反斜杠转义
    return s


def emit(lines, start, found, out_path):
    # 按正文物理位置排序作品边界
    order = sorted(found.items(), key=lambda kv: kv[1])  # (idx, line)
    bounds = [(ln, idx) for idx, ln in order]
    bounds.append((len(lines), None))

    out = []
    stats = {"works": 0, "chapters": 0}
    for b in range(len(bounds) - 1):
        line_no, idx = bounds[b]
        end = bounds[b + 1][0]
        title = WORKS[idx][0]
        stats["works"] += 1
        out.append(f"# {title}\n")
        i = line_no + 1  # 跳过标题行本身
        # 跳过紧随的 byline
        while i < end and (not lines[i].strip() or re.match(r"(?i)^by\s+jules verne", lines[i].strip())):
            i += 1
        while i < end:
            raw = lines[i]
            t = raw.strip()
            if FENCE_RE.match(t) or ATTR_ONLY_RE.match(t) or t.startswith("<svg") or t.startswith("</svg") or t.startswith("`<image") or t == "\\":
                i += 1
                continue
            ch = chapter_head(t)
            # PART 分卷头须为短的大写行（如 "FIRST PART"），排除正文
            # "Part of the ..."（PART_RE 在 re.I 下会误配 "of"）。
            mpt = None
            if not ch and PART_RE.match(t) and len(t) <= 40 and _upper_ratio(t) > 0.6:
                mpt = PART_RE.match(t)
            if ch or mpt:
                if ch:
                    kw, rest = ch
                    head = kw if not rest else f"{kw} {rest}".rstrip()
                    rest_inline = rest
                else:
                    head = t.rstrip(".")
                    rest_inline = mpt.group(5).strip() if mpt.lastindex and mpt.group(mpt.lastindex) else ""
                    head = head[: len(head) - len(rest_inline)].rstrip() if rest_inline else head
                # 若无内联小标题，尝试折入下一非空标题行
                if not rest_inline:
                    j = i + 1
                    while j < end and not lines[j].strip():
                        j += 1
                    nxt = lines[j].strip() if j < end else ""
                    if (j < end and is_title_line(lines[j])
                            and not chapter_head(nxt) and not PART_RE.match(nxt)):
                        rest_inline = clean_line(nxt)
                        head = f"{head} — {rest_inline}"
                        i = j
                out.append("")
                out.append(f"## {head}")
                out.append("")
                stats["chapters"] += 1
                i += 1
                continue
            out.append(clean_line(raw.rstrip()))
            i += 1
        out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)  # 折叠多余空行
    Path(out_path).write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"✓ 写入 {out_path}")
    print(f"  作品 {stats['works']} 部，章节标题 {stats['chapters']} 个")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detect", action="store_true")
    ap.add_argument("--emit")
    args = ap.parse_args()

    lines = SRC.read_text(encoding="utf-8").splitlines()
    start, found = detect(lines)

    if args.detect or not args.emit:
        print(f"正文起始行: {start+1}")
        print(f"检测到作品数: {len(found)}/36")
        for idx, (title, _) in enumerate(WORKS):
            ln = found.get(idx)
            mark = f"L{ln+1}" if ln is not None else "✗ MISSING"
            print(f"  {idx+1:2d}. {title:45s} {mark}")
        missing = [i + 1 for i in range(len(WORKS)) if i not in found]
        if missing:
            print(f"未匹配编号: {missing}")
        return

    if args.emit:
        if len(found) < len(WORKS):
            print(f"⚠ 仅检测到 {len(found)}/{len(WORKS)} 部作品，先补全再生成", file=sys.stderr)
            sys.exit(1)
        emit(lines, start, found, args.emit)


if __name__ == "__main__":
    main()
