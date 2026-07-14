---
round: 1
date: 2026-07-14
phase: GROW Phase 2.1-Showcase
gene: NEW36-seed-showcase-build
pages: [twenty-thousand-leagues, the-mysterious-island, gun-club, weldon-institute]
result: pass
---

# GROW 2.1-Showcase 首批精品样板奠基 — R1

## 执行摘要

Phase 2 大规模扩张前的强制样板轮。基线（`grow_baseline.md`）确认六个核心实体类型中，
BIRTH 61 页已覆盖 `character`/`place`/`technology`/`event`（各 15–16 页，均已有 featured），
仅 `work` 与 `organization` 为**零 featured 覆盖类型**。依选页规则 line 651「同类型已有 featured 页则跳过」，
本轮只对这两个零覆盖类型各建 2 页，共 4 页，全部达到 featured 并互引成网。

## 选页表

| 类型 | 候选实体 | corpus 命中段数 | 入选 | 主要 PN 源 |
|------|---------|----------------|------|-----------|
| work | Twenty Thousand Leagues Under the Sea | 高（TTLU 全卷）| ✅ | TTLU-001/002/006/047 |
| work | The Mysterious Island | 高（MI 全卷）| ✅ | MI-001/020/062 |
| organization | Gun Club | 188 | ✅ | FEM-001/002/003/004 |
| organization | Weldon Institute | 67 | ✅ | RC-002/003 |
| organization | Reform Club | 25 | ❌ 已存在为 `place` 型 featured 页 | — |
| organization | Royal Geographical Society | 14 | ❌ 频次低于入选двух | — |

> Reform Club 在 BIRTH 阶段已建为 `place` 类型 featured 页（俱乐部兼具地点属性），
> 不重复打磨；organization 第 2 页取频次次高的 Weldon Institute（*Robur the Conqueror*）。

## 八要素自检表

| 页面 | frontmatter+featured | 导语≥3 wikilink | H2 3–6 | 引文带 PN≥2 | 结构化元素 | seealso 互引 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| twenty-thousand-leagues | ✓ | ✓ (3) | ✓ (5) | ✓ | ✓ 列表 | ✓ |
| the-mysterious-island | ✓ | ✓ (3) | ✓ (5) | ✓ | ✓ 列表 | ✓ |
| gun-club | ✓ | ✓ | ✓ (4) | ✓ blockquote | ✓ blockquote | ✓ |
| weldon-institute | ✓ | ✓ (3) | ✓ (4) | ✓ | ✓ 列表 | ✓ |

## 互引图（无孤岛，每页被引 ≥2）

| 页面 | 入链数 |
|------|-------|
| twenty-thousand-leagues | 7 |
| the-mysterious-island | 9 |
| gun-club | 10 |
| weldon-institute | 2（新增 robur、albatross 两处入链）|

初建时 weldon-institute 为孤岛（0 入链），已在 `robur`、`albatross` 两页 linkify
`[[Weldon Institute]]` 补足至 ≥2。

## EVV5 类型样板反思（≥1 次）

**系统性发现（重要）**：`add_page.py` **不执行** `edit_page.py` 所强制的散文质量门
（`ref/散文质量强制规范.md`，单段 ≤400 字）。本轮 4 页经 `add_page.py` 建立时均含
超 400 字长段（TTLU 603、MI 527、Gun Club 474、Weldon 604），却仍被写入并自动标 featured；
只有事后用 `edit_page.py` 触碰才会被拦截（退出码 8）。

- **影响**：样板作为 Phase 2 全期质量基线，若自身违反散文规范则基线失真；
  且新建页与编辑页走**两套不一致的门禁**。
- **本轮处置**：对 4 页逐段拆分（在句界/引文界断段），全部复检 max_block ≤400 后重新 featured。
- **待记录**：`add_page.py` 应与 `edit_page.py` 对齐散文门（或至少给出 warning）。属共享 memex
  组件（`add_page.py`），依 RFC 停靠决策 **PARK**，记入 housekeeping，不自动提交。

**次要发现**：organization 型 Members 连续 bullet 块被散文门当作单段合并计字（Weldon 初版 525 字），
需控制成员列表总长或精简单条 bullet。已将 Phil Evans 条从双引文精简为单引文，页面仍保有 8 处 PN 引注（远超 ≥6 门槛）。

## EVV6 类型模板元反思（1 次）

固化两个零覆盖类型的模板骨架，写回 `local/template/{type}-schema.md`（已存在，本轮确认可用）：

- **work-schema**：5 个 H2（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes）。
  样板证实：开篇导语宜含 3 链（作品内主角/载具/关键地点），Plot Summary 可多段但每段 ≤400 字，
  章节区间用 `[[VVV-ch01]]`…`[[VVV-chNN]]` 收束。
- **organization-schema**：4 个 H2（Overview / Role in the Story / Members / Activities），≥6 引注。
  样板证实：Members 用 bullet 但**须控制总长**（散文门合并计字）；Activities 收束于该组织的
  「defining enterprise/activity」一句。

> N=6 核心类型，EXIT-GATE 要求固化 ≥N-1=5 个模板。character/place/technology/event 四模板
> 于 BIRTH Phase 7–9 已固化，加本轮 work/organization 复核，6/6 齐备。

## EXIT-GATE 检查

- [x] 4 页全部 `quality: featured`，八要素自检行行 ✓
- [x] 互引图无孤岛（每页被引 ≥2：7/9/10/2）
- [x] EVV5 ≥1 次（本轮 1 次，含 add_page.py 散文门旁路发现）
- [x] EVV6 1 次（work/organization 模板复核固化）
- [x] 已固化 ≥5 类型模板（实为 6/6）
- [x] 全部页面散文段 ≤400 字，复检通过

## 遗留问题

1. **add_page.py 散文门旁路**（EVV5 主发现）→ 记入 `housekeeping_queue.md`，PARK，待 featured-inflation RFC 一并评审。
2. **featured 虚高**（既有 DEFERRED-REGRADE）→ 本轮 4 页同样自动 featured；接受为无意义信号，待全库批量重评。
3. showcase 完成，`showcase_done: true`；下一步进入 2.1-B 类型串行扩张，队列首类型 `work`。
