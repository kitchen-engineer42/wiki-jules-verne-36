---
round: 8
date: 2026-07-14
type_round: 7
phase: "2.1"
current_type: work
gene: NEW1
pages: [in-the-year-2889]
result: accept
---

# GROW 2.1-B · R8 · NEW1 · work — 1 页（收官）

## 本轮公告

**R8 — Phase 2.1 — NEW1 — work — 1 页（standard 档）**

`current_type=work` 第七轮，建 work 全集最后一部作品 `in-the-year-2889`，work 语料自此耗尽。

## 决策矩阵与原则性偏离（同 R7 逻辑）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| rounds_since=6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| streak=0 | 否 |
| 3 | SCN28（可建候选 < 10 **或** rounds_since_discover ≥ 10）| 候选=1 < 10 | **严格触发** |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| rounds_since=6 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| 6 | 默认 NEW1 | — | — |

**严格判定为 priority-3 SCN28**，同 R7 作原则性偏离改走 NEW1：`work` 是 `ref/chapter-order.md`
固定枚举的 35 部合集，red-link/LLM 勘探无法"发现"第 36 部作品。仅剩 1 部**已知可建**作品
（YEAR），故本轮建之，把 work 语料铺满，勘探语义留给无限开放的类型。

> 本轮为**退化 1 页 NEW1**（NEW1 常规 5 页，但 work 候选仅剩 1 部）。建完即触发 2.1-E
> 类型完成 Wikify + 关闭流程（见遗留问题，R9 执行 BLK3）。

## 选页依据

延续全库 `book:` 字段引用频次排序，取最后一部尚未建页的作品：

| slug | 作品 | VVV | 章数 | 备注 |
|------|------|-----|------|------|
| in-the-year-2889 | In the Year 2889 | YEAR | 1 | 未来主义短篇；`data/sentence_index/YEAR-001.jsonl`（347 句 / 109 段）可用 |

> **全集收官核对**：`ref/chapter-order.md` 列 35 部。已建 33 部（R6 前各轮 + R7 5 部 + 本轮 YEAR），
> 语义重复弃建 2 部（**SI**=Mysterious Island 第三部随 MI 建；**VB**=A Voyage in a Balloon 与
> DA/A Drama in the Air 同一故事）。33 + 2 = 35，**work 全集边界闭合**。

## 页面处理记录

| 页面 | 结果 | quality | rev | max 段长 |
|------|------|---------|-----|---------|
| in-the-year-2889 | 新建 | standard | RU9esk | 396 |

> work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes）。
> 每句断言均来自 YEAR sentence_index 命中句并标注 PN；PN 用真实三段段号
> （`'-'.join(sid.split('-')[:3])`，沿用 R7 修正）。散文段预控 ≤400，最长 396。
> add_page.py PN 自检全绿（无 ⚠ 低重叠 / ✗ 不存在段号告警）。

## EXIT-GATE 检查

- [x] G1 1 页成功新建（standard 档，work 收官页）
- [x] G2 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验（add_page.py 自检全绿）
- [x] G4 记录完整性：本日志 + state 更新；页面经 add_page.py（无 Write/Edit 旁路）
- [x] G5 散文段全部 ≤400 字（预控；最长 396）

## state 更新（NEW1 per-round）

`current_round 8→9`，`type_round 6→7`，`rounds_since_last_evv5/discover/corpus_discover 6→7`。
`current_type` 仍为 `work`（类型关闭在 R9 BLK3 执行）。

## 遗留问题

1. **work 候选彻底耗尽**（可建候选=0）。触发 §2.1-E：R9 执行 **BLK3 work-type wikify pass**
   （`bulk_wikilink.py --type work` + 补录 record_revision + scan_wanted_pages + build_backlinks），
   随后执行**类型关闭 bookkeeping**（work 入 `closed_types`，`current_type→organization`，
   重置 type_round/discover_streak_low/rounds_since_last_evv5），转入 type_queue 队首 `organization`。
2. **BLK3 命中率注记**：当前实体类型（character/place/technology/event/organization）尚几乎为空，
   work 页 wikify 主要命中 work↔work 互链与既有页；命中率偏低属预期，spec §2.1-E 仍要求即时执行
   （"不积压到最后"），故 R9 照常执行，后续类型建成后由 2.1-X 前的全库 backlink 重建补齐。
3. **段号提取规则**沿用 R7 固化：dump sentence_index 供 PN 引用时段号取 `sid` 前三段。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度三项债务照旧 PARK（housekeeping_queue.md）。
