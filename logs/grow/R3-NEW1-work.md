---
round: 3
date: 2026-07-14
type_round: 2
phase: "2.1"
current_type: work
gene: NEW1
pages: [in-search-of-the-castaways, survivors-of-the-chancellor, the-fur-country, five-weeks-in-a-balloon, off-on-a-comet]
result: accept
---

# GROW 2.1-B · R3 · NEW1 · work — 5 页

## 本轮公告

**R3 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

`current_type=work` 第二轮扩张，串行建 5 页。决策矩阵：evv5/discover 间隔（10）均未触发，corpus-discover（30）未触发 → 默认 NEW1。

## 选页依据

改用**全库 `book:` 字段引用频次**（比 R2 的实体页局部计数更权威），取尚未建页的 Top 5 作品：

| slug | 作品 | book 引用数 | VVV | 章数 |
|------|------|-----------|-----|------|
| in-search-of-the-castaways | In Search of the Castaways | 66 | SC | 66 |
| survivors-of-the-chancellor | The Survivors of the Chancellor | 57 | SC2 | 57 |
| the-fur-country | The Fur Country | 47 | FC | 48 |
| five-weeks-in-a-balloon | Five Weeks in a Balloon | 45 | FWB | 44 |
| off-on-a-comet | Off on a Comet | 45 | OC | 45 |

> The Mysterious Island（72）、Twenty Thousand Leagues（49）、Around the World（46）、
> Journey to the Center（45）、Captain Hatteras（62）已在 Showcase / R2 建页，本轮跳过。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| in-search-of-the-castaways | 新建 | standard | g56j87 | 352 |
| survivors-of-the-chancellor | 新建 | standard | hRJ3Jy | 381 |
| the-fur-country | 新建 | standard | 3oeanv | 327 |
| five-weeks-in-a-balloon | 新建 | standard | le7Auc | 329 |
| off-on-a-comet | 新建 | standard | 25ISuw | 325 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 sentence_index 命中句并标注 PN。散文段预控 ≤400 字（规避 add_page.py 散文门旁路缺陷）。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（SC/SC2/FC/FWB/OC 各章 jsonl）
- [x] G4 记录完整性：本日志 + state 更新
- [x] G5 散文段全部 ≤400 字（预控，非事后修补；最长 381）

## state 更新

`current_round 3→4`，`type_round 1→2`，`rounds_since_last_evv5/discover/corpus_discover 1→2`。
`current_type` 仍为 `work`（候选未耗尽，剩余约 23 部作品）。

## 遗留问题

1. work 候选仍充足（35 − 已建 12 = 23 待建），无需 discover。下一轮延续 work NEW1
   （次高引用：Eight Hundred Leagues on the Amazon(41)、Dick Sand(39)、Michael Strogoff(34)、
   The Adventures of a Special Correspondent(27)、An Antarctic Mystery(26) 等）。
2. R6 将触及 EVV5（每 10 轮，当前 rounds_since_last_evv5=2）——届时抽检既有页散文门与链接。
3. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
