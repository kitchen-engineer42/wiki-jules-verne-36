---
round: 31
date: 2026-07-15
type_round: 3
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - crespo-island
  - stony-hill
  - pacific-railroad
result: accept
---

# GROW 2.1-B · R31 · NEW1 · place — 第三批 place NEW1（+3 页，standard 档）

## 本轮公告

**R31 — Phase 2.1 — NEW1 — place — 3 建页 / standard 档**

queue_size=14（≥ discover_queue_threshold 10），queue(place)≠0，无门抢先，落入 NEW1 默认门。
建第三批 3 页 place，消费 P1 余量 + P2 place 候选：**TTLU**（Crespo Island）+ **FEM**（Stony Hill）+
**AWED**（Pacific Railroad，borderline place/org，按线路定 place）。P1 place 至此清空。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=14, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =29 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=3 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | citations | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------|---------------------------|------|
| crespo-island | TTLU(Twenty Thousand Leagues)| 8YgtOo | 2821 | 8 | fictional / North Pacific Ocean | accept |
| stony-hill | FEM(From the Earth to the Moon)| qnxGqg | 3234 | 12 | fictional / Florida, US | accept |
| pacific-railroad | AWED(Around the World in Eighty Days)| yVmD3f | 2764 | 8 | real / United States | accept |

> **候选勘误（建页前实测校准，承 R30 教训）**：
> - queue 记「Stone's Hill」→ 语料实名 **Stony Hill**（FEM，25 命中/9 distinctPN），slug 定为 `stony-hill`。
> - queue 记「Crespo Island」属 **TTLU**（非 queue 早期误写「20KL」）；13 命中/7 distinctPN，达 standard。
> - Pacific Railroad **borderline place/org**：语料命名碎裂（Pacific Railroad 4 / Pacific Railway 6 /
>   Union Pacific / Central Pacific），但 AWED 段内 6 distinctPN 连贯（分线定义、1867 通车、Omaha 终点），
>   足支 standard 档 place 页；aliases 收 Union Pacific / Central Pacific 以聚合红链。

> **互链**：Crespo Island → Nautilus（既有 technology）/ Captain Nemo；Stony Hill → columbiad / gun-club /
> tampa-town（三既有页，FEM 铸炮基地链）；Pacific Railroad → Phileas Fogg（AWED 主角，红链留 character 轮）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{TTLU,FEM,AWED}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
crespo-island（初稿 2 段 417/453）、stony-hill（初稿 2 段 539/482）、pacific-railroad（初稿 2 段 453/504）
均拆分后过门。Connections 节为 wikilink/纯文本，不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | 三页各 2 长段拆分后 add 前核验通过 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 3 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 31→32`；`type_round 2→3`；`rounds_since_last_evv5 2→3`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 29→30`；`last_updated_round→32`。

## 遗留问题

1. **R32 = place discover 临界**：P1 place 已清空；queue(place) 仅余 P2 红链候选（无独立 place 候选）。
   R32 起 `since_corpus=30`（达 corpus_discover_interval 30）→ **SCN28-corpus 深扫**将抢先触发，
   全集 36 部扫描新地名补种（真实地理门槛：Iceland/Baltimore/Tampa Town 均既有 Pilot，须排除）。
2. **Pacific Railroad alias 聚合**：收 Union Pacific / Central Pacific 为 aliases；若后续 character 轮
   建 Phileas Fogg，其红链应解析至本页。build_registry 已纳入 alias_index。
3. **queue distinctPN 估值持续校准**：Stone's Hill→Stony Hill（拼写）、20KL→TTLU（VVV 码）两处再勘误，
   延续 R30「建页前实测」惯例。queue 中 P2 红链候选（10 character + James Starr）估值待各类型轮实测。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传** 七项债务照旧 PARK/记录。
