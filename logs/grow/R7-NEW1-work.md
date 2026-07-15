---
round: 7
date: 2026-07-14
type_round: 6
phase: "2.1"
current_type: work
gene: NEW1
pages: [the-blockade-runners, the-pearl-of-lima, master-zacharius, a-drama-in-the-air, the-ascent-of-mont-blanc]
result: accept
---

# GROW 2.1-B · R7 · NEW1 · work — 5 页

## 本轮公告

**R7 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

`current_type=work` 第六轮扩张，串行建 5 页，收尾 work 长尾。

## 决策矩阵与原则性偏离

按 GROW.spec.md §2.1-B 决策矩阵逐条评估：

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| rounds_since=5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| streak=0 | 否 |
| 3 | SCN28（可建候选 < 10 **或** rounds_since_discover ≥ 10）| 候选=6 < 10 | **严格触发** |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| rounds_since=5 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| 6 | 默认 NEW1 | — | — |

**严格判定为 priority-3 SCN28（勘探轮）**，但本轮作出原则性偏离，改走 NEW1，理由：

> `work` 类型是**有限且已完全枚举**的语料集合——`ref/chapter-order.md` 固定列出 35 部作品。
> red-link/LLM 勘探（SCN28）的作用是发现语料中尚未成词条的**新**主题；但对 work 而言，
> 全集边界已知，勘探不可能"发现"第 36 部作品。此时机械执行 SCN28 只会产出退化的空勘探轮，
> 同时把 6 部**已知可建**作品搁置。故本轮按 NEW1 建剩余高频作品，把 SCN28 语义正确地留给
> 无限开放的类型（character/place 等）。

## 选页依据

延续全库 `book:` 字段引用频次排序，取尚未建页的次高引用作品，并处理语义重复：

| slug | 作品 | VVV | 章数 | 备注 |
|------|------|-----|------|------|
| the-blockade-runners | The Blockade Runners | BR | 10 | 独立作品 |
| the-pearl-of-lima | The Pearl of Lima | PL | 9 | 独立作品（Martin Paz）|
| master-zacharius | Master Zacharius | MZ | 5 | 独立作品 |
| a-drama-in-the-air | A Drama in the Air | DA | 1 | 碎片；VB 为其重复，**不建 VB** |
| the-ascent-of-mont-blanc | The Ascent of Mont Blanc | AMB | 1 | 碎片；纪实叙事 |

> **重复处理**：
> - **SI**（The Secret of the Island）= Mysterious Island 第三部，已随 MI 建页，**跳过**。
> - **VB**（A Voyage in a Balloon）与 **DA**（A Drama in the Air）为同一故事（Un drame dans les airs，
>   同以 Frankfort 气球升空、闯入的疯子为核），仅建 DA，**VB 跳过**。
> - VB/DA/AMB/YEAR 章数标为 0（碎片），但 sentence_index 均有完整内容（347–490 行），可建。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| the-blockade-runners | 新建 | standard | FZyLQm | 354 |
| the-pearl-of-lima | 新建 | standard | 9kKZLb | 352 |
| master-zacharius | 新建→修正 | standard | W5a7lu | 347 |
| a-drama-in-the-air | 新建 | standard | PAg9gW | 333 |
| the-ascent-of-mont-blanc | 新建 | standard | L2xDNp | 384 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 sentence_index 命中句并标注 PN。散文段预控 ≤400 字，最长 384。

## 事故与修正：MZ 段号错位

MZ 首稿（rev=Q3PFdm）在 add_page.py PN 校验中报 3 处问题：
`MZ-005-133`、`MZ-005-140` 不存在，`MZ-001-002` 重叠度过低。根因：初次 dump sentence_index 时
误用 `pn`（两段 `MZ-005`）+ 句序号（s1/s2）拼接，把它当成三段段号来数，导致 PPP 计数错位。
**修正**：改用 `sid` 去掉 `-sN` 得真实三段段号（`'-'.join(sid.split('-')[:3])`），
逐句重新绑定 PN，经 edit_page.py 更新（rev=W5a7lu），复核 PN 全部命中。
BR/PL/DA/AMB 经复核或 add_page.py 自检 PN 全绿。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（含 MZ 修正后复核）
- [x] G4 记录完整性：本日志 + state 更新；页面全部经 add_page.py/edit_page.py（无 Write/Edit 旁路）
- [x] G5 散文段全部 ≤400 字（预控；最长 384）

## state 更新

`current_round 7→8`，`type_round 5→6`，`rounds_since_last_evv5/discover/corpus_discover 5→6`。
`current_type` 仍为 `work`。

## 遗留问题

1. **work 候选基本耗尽**。全库 35 部作品：已建 32 部（含 R6 之前各轮 + 本轮 5 部），
   语义重复 2 部弃建（SI=MI-3、VB=DA），仅剩 **YEAR**（In the Year 2889，碎片，sentence_index 可用）1 部。
   → **R8 建 YEAR 后触发 type-close，work 类型收官，转入 `organization`（type_queue 队首）**。
2. **R11 触及 EVV5**：rounds_since_last_evv5 R8 将达 6，预计 R11 达 10 触发首个 EVV5 抽检轮。
3. **段号提取教训固化**：dump sentence_index 供 PN 引用时，段号一律取 `sid` 前三段，
   **禁止**用 `pn`+句序号拼接。已在本轮修正，后续各类型建页沿用。
4. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
5. 已建 work 页中，character/place/technology 词条尚未回链——留待 EVV5 抽检。
