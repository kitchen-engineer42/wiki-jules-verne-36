#!/usr/bin/env python3
"""build_chapter_pages.py — 从 doc_final.md 导入 35 部凡尔纳作品的章节页。

本 wiki 为多作品合集（anthology），非单书。设计（详见 BIRTH.md Phase 4）：
  - `#`  行 = 一部作品（VVV 卷号见 ref/chapter-order.md）
  - `##` 行 = 章节；PART 分卷头（"FIRST PART" 等）仅作分组，不生成页面
  - 有章节的作品：每章一页，slug=`{VVV}-ch{NN:02d}`（NN 为作品内顺序号）
  - 无章节的短篇：整篇单页，slug=`{VVV}`
  - pn_prefix=`{VVV}-{NN:03d}`（LAW.md 三段式 PN 的卷内前缀）
  - book_seq/chapter = 全合集连续序号（1..N，满足 chapter_integrity C03）
  - label 保留原书章节编号文字（分卷内 "CHAPTER 1" 可重复，slug/pn 用 NN 去重）

写入路径经 page_bucket 分桶；生成 chapter_map.json（键=pn_prefix）。
不插入 PN（留 Phase 5）；段落间空行保留。
"""
import json
import os
import re
import sys
from pathlib import Path

MEMEX = os.environ.get("MEMEX_ROOT", str(Path.home() / "memex"))
sys.path.insert(0, os.path.join(MEMEX, "wiki/scripts"))
from page_bucket import page_bucket  # noqa: E402

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.getcwd()))
CORPUS = WIKI_ROOT / "corpus/raw/doc_final.md"
PAGES_DIR = WIKI_ROOT / "docs/wiki/pages"
DATA_DIR = WIKI_ROOT / "docs/wiki/data"

# 作品显示名 → VVV 卷号（与 ref/chapter-order.md 一致）
VVV = {
    "Twenty Thousand Leagues Under the Sea": "TTLU",
    "A Journey to the Center of the Earth": "JCE",
    "Around the World in Eighty Days": "AWED",
    "The Mysterious Island": "MI",
    "The Secret of the Island": "SI",
    "From the Earth to the Moon": "FEM",
    "Round the Moon": "RM",
    "A Voyage in a Balloon": "VB",
    "Doctor Ox's Experiment": "DOSE",
    "Master Zacharius": "MZ",
    "A Drama in the Air": "DA",
    "A Winter Amid the Ice": "WAI",
    "Ascent of Mont Blanc": "AMB",
    "An Antarctic Mystery": "AM",
    "Dick Sand: A Captain at Fifteen": "DSCF",
    "Eight Hundred Leagues on the Amazon": "EHLA",
    "Facing the Flag": "FF",
    "Five Weeks in a Balloon": "FWB",
    "Godfrey Morgan": "GM",
    "The Adventures of Captain Hatteras": "ACH",
    "In Search of the Castaways": "SC",
    "Michael Strogoff": "MS",
    "Off on a Comet": "OC",
    "Robur the Conqueror": "RC",
    "The Adventures of a Special Correspondent": "ASC",
    "The Blockade Runners": "BR",
    "The Fur Country": "FC",
    "The Master of the World": "MW",
    "The Pearl of Lima": "PL",
    "The Survivors of the Chancellor": "SC2",
    "The Underground City": "UC",
    "The Waif of the Cynthia": "WC",
    "Ticket No. 9672": "TN",
    "Topsy Turvy": "TT",
    "In the Year 2889": "YEAR",
}

PART_RE = re.compile(
    r"^((FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH)\s+PART|PART\s+(THE\s+)?[A-Z0-9]+)\b",
    re.I,
)


def is_part(head: str) -> bool:
    return bool(PART_RE.match(head.strip()))


def parse_corpus():
    """→ [ {work, vvv, parts:[(part_label, [ (heading, [lines]) ])] ,
             chapters:[(heading, part_label|None, [content_lines])],
             body:[lines] } ]"""
    lines = CORPUS.read_text(encoding="utf-8").splitlines()
    works = []
    cur = None
    cur_part = None
    cur_chapter = None  # (heading, part, content list)

    def flush_chapter():
        nonlocal cur_chapter
        if cur is not None and cur_chapter is not None:
            cur["chapters"].append(cur_chapter)
        cur_chapter = None

    for ln in lines:
        if ln.startswith("# "):
            flush_chapter()
            if cur is not None:
                works.append(cur)
            title = ln[2:].strip()
            cur = {"work": title, "vvv": VVV.get(title, title[:4].upper()),
                   "chapters": [], "body": []}
            cur_part = None
            continue
        if cur is None:
            continue
        if ln.startswith("## "):
            head = ln[3:].strip()
            if is_part(head):
                flush_chapter()
                cur_part = head
                continue
            flush_chapter()
            cur_chapter = (head, cur_part, [])
            continue
        # content line
        if cur_chapter is not None:
            cur_chapter[2].append(ln)
        else:
            cur["body"].append(ln)
    flush_chapter()
    if cur is not None:
        works.append(cur)
    return works


_BYLINE_RE = re.compile(r"(?i)^(by(\s+jules\s+verne)?|jules\s+verne)\.?$")
_TRIVIAL_RE = re.compile(r"^[IVXLC0-9]+\.?$", re.I)


def strip_leading_byline(lines):
    out = list(lines)
    while out and (not out[0].strip() or _BYLINE_RE.match(out[0].strip())):
        out.pop(0)
    return out


_CALIBRE_SPAN_RE = re.compile(r"\[([^\]]*)\]\{\.calibre[0-9]*\}")


def clean_body(lines):
    lines = strip_leading_byline(lines)
    text = "\n".join(lines).strip("\n")
    # 去 Calibre 展示性 span（`[文本]{.calibreN}` → 文本）；
    # .bold/.italic 等语义 span 留给 normalize_pandoc_spans 处理。
    text = _CALIBRE_SPAN_RE.sub(r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def first_sentence(text, work):
    for para in text.split("\n\n"):
        p = para.strip()
        if not p or _TRIVIAL_RE.match(p) or _BYLINE_RE.match(p):
            continue
        s = re.split(r"(?<=[.!?])\s", p)[0]
        return (s[:150]).strip()
    return f"A chapter from {work}."


def clean_label(s: str) -> str:
    # 去 pandoc 反斜杠转义，并将成对直引号转为弯引号。label 在构造时即归一，
    # 使 frontmatter、pages.json、EXPECTED_CHAPTERS 三处一致（C04/C07）。
    # 弯引号规避 chapter_integrity 朴素解析器 `.strip('"').strip("'")` 误截尾部引号
    # （如 `THE 'MONK'` 被截成 `THE 'MONK`，与正规 YAML 解析器结果不一致）。
    s = s.replace("\\", "")
    s = re.sub(r'"([^"]*)"', "\u201c\\1\u201d", s)
    s = re.sub(r"'([^']*)'", "\u2018\\1\u2019", s)
    return s


def yaml_q(s: str) -> str:
    # 双引号包裹已归一的值；内部残留直引号（如所有格 CAPTAIN'S）降级避免转义冲突。
    return '"' + clean_label(s).replace('"', "\u201d") + '"'


def build():
    works = parse_corpus()
    chapter_map = {}
    expected = []  # (global_seq, slug, label)
    seq = 0

    for w in works:
        vvv = w["vvv"]
        work = w["work"]
        if w["chapters"]:
            for i, (head, part, content) in enumerate(w["chapters"], 1):
                slug = f"{vvv}-ch{i:02d}"
                pn_prefix = f"{vvv}-{i:03d}"
                body = clean_body(content)
                label = clean_label(f"{work} — {head}")
                seq += 1
                _write_page(slug, pn_prefix, label, work, seq, part, body, head)
                chapter_map[pn_prefix] = slug
                expected.append((seq, slug, label))
        else:
            slug = vvv
            pn_prefix = f"{vvv}-001"
            body = clean_body(w["body"])
            label = clean_label(work)
            seq += 1
            _write_page(slug, pn_prefix, label, work, seq, None, body, None)
            chapter_map[pn_prefix] = slug
            expected.append((seq, slug, label))
    written = seq

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "chapter_map.json").write_text(
        json.dumps(chapter_map, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_chapter_list(expected)
    print(f"✓ 写入 {written} 个章节页（{len(works)} 部作品）")
    print(f"  chapter_map.json: {len(chapter_map)} 条")


def _write_page(slug, pn_prefix, label, work, seq, part, body, head):
    fm = ["---",
          f"id: {slug}",
          "type: chapter",
          f"label: {yaml_q(label)}",
          f"description: {yaml_q(first_sentence(body, work))}",
          f"book: {yaml_q(work)}",
          f"chapter: {seq}",
          f"book_seq: {seq}",
          f'pn_prefix: "{pn_prefix}"']
    if part:
        fm.append(f"part: {yaml_q(part)}")
    fm += ["tags: [chapter]", "---", ""]
    heading = f"# {label}"
    text = "\n".join(fm) + heading + "\n\n" + body + "\n"
    bucket = page_bucket(slug)
    out = PAGES_DIR / bucket / f"{slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


def _write_chapter_list(expected):
    lines = ['"""local/chapter_list.py — CHK12 章节完整性预期表（自动生成）。"""',
             "EXPECTED_CHAPTERS = ["]
    for seq, slug, label in expected:
        lines.append(f"    ({seq}, {slug!r}, {label!r}),")
    lines += ["]", "", "NON_CHAPTER_PAGES = {'About', 'TOC'}", ""]
    (WIKI_ROOT / "local").mkdir(exist_ok=True)
    (WIKI_ROOT / "local/chapter_list.py").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    build()
