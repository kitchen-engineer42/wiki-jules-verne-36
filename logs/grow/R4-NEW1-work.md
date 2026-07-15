---
round: 4
date: 2026-07-14
type_round: 3
phase: "2.1"
current_type: work
gene: NEW1
pages: [eight-hundred-leagues-on-the-amazon, dick-sand-a-captain-at-fifteen, michael-strogoff, adventures-of-a-special-correspondent, an-antarctic-mystery]
result: accept
---

# GROW 2.1-B · R4 · NEW1 · work — 5 页

## 本轮公告

**R4 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

`current_type=work` 第三轮扩张，串行建 5 页。决策矩阵：evv5/discover 间隔（10）均未触发（rounds_since=2），corpus-discover（30）未触发（rounds_since=2）→ 默认 NEW1。

## 选页依据

延续 R3 的**全库 `book:` 字段引用频次**排序，取尚未建页的次高引用 Top 5 作品：

| slug | 作品 | VVV | 章数 |
|------|------|-----|------|
| eight-hundred-leagues-on-the-amazon | Eight Hundred Leagues on the Amazon | EHLA | 42 |
| dick-sand-a-captain-at-fifteen | Dick Sand: A Captain at Fifteen | DSCF | 38 |
| michael-strogoff | Michael Strogoff | MS | 34 |
| adventures-of-a-special-correspondent | The Adventures of a Special Correspondent | ASC | 27 |
| an-antarctic-mystery | An Antarctic Mystery | AM | 26 |

> R3 遗留问题已点名此 5 部（EHLA 41、Dick Sand 39、Michael Strogoff 34、Special Correspondent 27、Antarctic Mystery 26），本轮兑现。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| eight-hundred-leagues-on-the-amazon | 新建 | standard | 2DLU4Y | 339 |
| dick-sand-a-captain-at-fifteen | 新建 | standard | K25HSk | 386 |
| michael-strogoff | 新建 | standard | c4PfcN | 366 |
| adventures-of-a-special-correspondent | 新建 | standard | j5LHS8 | 344 |
| an-antarctic-mystery | 新建 | standard | LIcdUJ | 352 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 sentence_index 命中句并标注 PN（EHLA/DSCF/MS/ASC/AM 各章 jsonl）。散文段预控 ≤400 字（规避 add_page.py 散文门旁路缺陷），最长 386。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（EHLA/DSCF/MS/ASC/AM 各章 jsonl）
- [x] G4 记录完整性：本日志 + state 更新；页面全部经 add_page.py（无 Write/Edit 旁路）
- [x] G5 散文段全部 ≤400 字（预控，非事后修补；最长 386）

## state 更新

`current_round 4→5`，`type_round 2→3`，`rounds_since_last_evv5/discover/corpus_discover 2→3`。
`current_type` 仍为 `work`（候选未耗尽，全库 17/35 已建，剩余约 18 部）。

## 遗留问题

1. work 候选仍充足（35 − 已建 17 = 18 待建）。下一轮 R5 延续 work NEW1
   （次高引用余部：The Blockade Runners、A Winter Amid the Ice、The Green Ray、
   Master of the World、The Master of the World / 短篇集等，届时按 `book:` 频次重排）。
2. R6 将触及 EVV5（每 10 轮，届时 rounds_since_last_evv5=4 起算，尚未到）——继续累计。
3. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
