---
round: 5
date: 2026-07-14
type_round: 4
phase: "2.1"
current_type: work
gene: NEW1
pages: [round-the-moon, godfrey-morgan, the-waif-of-the-cynthia, topsy-turvy, ticket-no-9672]
result: accept
---

# GROW 2.1-B · R5 · NEW1 · work — 5 页

## 本轮公告

**R5 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

`current_type=work` 第四轮扩张，串行建 5 页。决策矩阵：evv5/discover 间隔（10）均未触发（rounds_since=3），corpus-discover（30）未触发（rounds_since=3）→ 默认 NEW1。

## 选页依据

延续全库 `book:` 字段引用频次排序，取尚未建页的次高引用 Top 5 作品：

| slug | 作品 | book 引用数 | VVV | 章数 |
|------|------|-----------|-----|------|
| round-the-moon | Round the Moon | 26 | RM | 23 |
| godfrey-morgan | Godfrey Morgan | 22 | GM | 22 |
| the-waif-of-the-cynthia | The Waif of the Cynthia | 22 | WC | 22 |
| topsy-turvy | Topsy-Turvy | 21 | TT | 21 |
| ticket-no-9672 | Ticket No. 9672 | 20 | TN | 20 |

> **跳过 The Secret of the Island（SI, 20 引用）**：该 VVV 实为 The Mysterious Island 第三部
> （语料按物理结构拆分为独立卷），MI 已在 Showcase 建页，另建 SI 会产生语义重复词条。
> 故以同频次的 Ticket No. 9672（独立长篇）替补，避免重复。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| round-the-moon | 新建 | standard | Pt4jfj | 360 |
| godfrey-morgan | 新建 | standard | be3w32 | 389 |
| the-waif-of-the-cynthia | 新建 | standard | 36pFoU | 343 |
| topsy-turvy | 新建 | standard | Bt4epg | 383 |
| ticket-no-9672 | 新建 | standard | CNwRtz | 342 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 sentence_index 命中句并标注 PN（RM/GM/WC/TT/TN 各章 jsonl）。散文段预控 ≤400 字（规避 add_page.py 散文门旁路缺陷），最长 389。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（RM/GM/WC/TT/TN 各章 jsonl）
- [x] G4 记录完整性：本日志 + state 更新；页面全部经 add_page.py（无 Write/Edit 旁路）
- [x] G5 散文段全部 ≤400 字（预控，非事后修补；最长 389）

## state 更新

`current_round 5→6`，`type_round 3→4`，`rounds_since_last_evv5/discover/corpus_discover 3→4`。
`current_type` 仍为 `work`（候选未耗尽，全库 22/35 已建，剩余约 13 部）。

## 遗留问题

1. work 候选转入长尾（35 − 已建 22 = 13 待建，含 0 章的碎片/短篇需评估可建性）。
   下一轮 R6 触及 **EVV5**（每 10 轮，届时 rounds_since_last_evv5 将达 4→需继续累计至 10 才触发；
   注：当前计数 4，尚未到 10，R6 仍走 NEW1）。次高引用余部：
   The Secret of the Island(SI，MI 第三部，重复风险，暂缓)、The Underground City(UC,19)、
   Facing the Flag(FF,18)、The Master of the World(MW,18)、Doctor Ox's Experiment(DOSE,17)、
   A Winter Amid the Ice(WAI,16)、The Blockade Runners(BR,10)、The Pearl of Lima(PL,9)、
   Master Zacharius(MZ,5)。VB/DA/AMB/YEAR 章数为 0（碎片），建页前需核查 sentence_index 可用性。
2. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
3. 已建 work 页中，部分小说的 real-vs-fictional 地点、technology 词条尚未回链——留待 EVV5 抽检。
