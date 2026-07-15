---
round: 6
date: 2026-07-14
type_round: 5
phase: "2.1"
current_type: work
gene: NEW1
pages: [the-underground-city, facing-the-flag, the-master-of-the-world, doctor-oxs-experiment, a-winter-amid-the-ice]
result: accept
---

# GROW 2.1-B · R6 · NEW1 · work — 5 页

## 本轮公告

**R6 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

`current_type=work` 第五轮扩张，串行建 5 页。决策矩阵：evv5/discover 间隔（10）均未触发（rounds_since=4），corpus-discover（30）未触发（rounds_since=4）→ 默认 NEW1。

## 选页依据

延续全库 `book:` 字段引用频次排序，取尚未建页的次高引用 Top 5 作品：

| slug | 作品 | book 引用数 | VVV | 章数 |
|------|------|-----------|-----|------|
| the-underground-city | The Underground City | 19 | UC | 19 |
| facing-the-flag | Facing the Flag | 18 | FF | 18 |
| the-master-of-the-world | The Master of the World | 18 | MW | 18 |
| doctor-oxs-experiment | Doctor Ox's Experiment | 17 | DOSE | 17 |
| a-winter-amid-the-ice | A Winter Amid the Ice | 16 | WAI | 16 |

> **续接 R5 遗留**：R5 已跳过 The Secret of the Island（SI，MI 第三部，语义重复）。本轮次高引用余部
> 全部为独立作品，无重复风险，按引用频次顺次建页。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| the-underground-city | 新建 | standard | IUUYJE | 384 |
| facing-the-flag | 新建 | standard | Cw5NjF | 382 |
| the-master-of-the-world | 新建 | standard | iQ6ctk | 350 |
| doctor-oxs-experiment | 新建 | standard | kFDwYd | 380 |
| a-winter-amid-the-ice | 新建 | standard | P0aQph | 371 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 sentence_index 命中句并标注 PN（UC/FF/MW/DOSE/WAI 各章 jsonl）。散文段预控 ≤400 字
> （规避 add_page.py 散文门旁路缺陷），最长 384。DOSE 首稿两段超限（439/429），已断段后重控至 380。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（UC/FF/MW/DOSE/WAI 各章 jsonl）
- [x] G4 记录完整性：本日志 + state 更新；页面全部经 add_page.py（无 Write/Edit 旁路）
- [x] G5 散文段全部 ≤400 字（预控 + DOSE 事中断段；最长 384）

## state 更新

`current_round 6→7`，`type_round 4→5`，`rounds_since_last_evv5/discover/corpus_discover 4→5`。
`current_type` 仍为 `work`（候选未耗尽，全库 27/35 已建，剩余约 8 部）。

## 遗留问题

1. work 候选进入长尾（35 − 已建 27 = 8 待建）。次高引用余部：
   The Secret of the Island(SI，MI 第三部，重复风险，暂缓)、The Blockade Runners(BR,10)、
   The Pearl of Lima(PL,9)、Master Zacharius(MZ,5)。另 VB/DA/AMB/YEAR 章数为 0（碎片），
   建页前须核查 sentence_index 可用性——若无命中句则不可建（违反 G3）。
   预计 R7 建 BR/PL/MZ 后，可建 work 候选基本耗尽，需评估是否触发 type-close 转入 organization。
2. **R7 触及 EVV5 判定**：rounds_since_last_evv5 将达 5，仍未到 10，R7 仍走 NEW1；EVV5 预计 R11 触发。
3. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
4. 已建 work 页中，real-vs-fictional 地点、technology、character 词条尚未回链——留待 EVV5 抽检。
