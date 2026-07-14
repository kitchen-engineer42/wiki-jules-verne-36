---
round: 16
date: 2026-07-13
phase: 9
gene: EVV6
type: place
pages: []
result: converged
---

# R16 — EVV6 place 元反思（横向分析三轮 EVV5，模板定稿）

## 执行摘要

读取三份 place EVV5 日志（R10 r1、R12 r2、R15 r3）横向分析，对 `place-schema.md` 做最终定稿判断。结论：**模板 converged**。三个差异化批次（最强实体 → 新子领域 → 边缘复杂案例）15 页零结构偏差，两次模板追加均属写作指引层面、无结构性字段增删，且 r3 最难批次零追加。本轮完成两项遗留决议：**edit_page 后补跑 compute_quality 固化为流程提示**、**跨作品实体累计 2 例暂不提 RFC**。

## 三轮 EVV5 横向分析

| 维度 | r1（R10）| r2（R12）| r3（R15）| 趋势 |
|------|---------|---------|---------|------|
| 结构偏差 | 0 | 0 | 0 | 稳定零偏差 |
| 模板变更 | +写作指引5条 | +写作指引3条 | 0（无变更）| 追加量递减→0 |
| 变更性质 | 写作指引 | 写作指引 | — | 从不触及结构 |
| 压力来源 | 双档适配/引文核验 | 无地形地点 Geography | 边缘案例全吸收 | 压力递减 |
| 子领域 | 岛/火山/城镇/俱乐部/地底海 | 都市/海域/极地/真实国家 | 天体/神秘/出口/居所/航点 | 覆盖渐广 |

**关键判据**：模板追加量 5→3→0，且 r3（专挑边缘/复杂案例）**零追加**——最能暴露 schema 盲点的批次也未产生新指引需求，是收敛的决定性证据。四节结构（Overview / In the Narrative / Geography & Features / Connections）与专属 frontmatter（book / real_or_fictional / region）经 15 页 real/fictional 双档全覆盖验证，骨架自 r1 即稳定。与 technology schema（追加量 3→2→0）收敛轨迹同构。

## 收敛判断：converged

- **结构收敛**：H2 节序 / frontmatter / 引文规范三项 15 页零偏差。
- **写作指引收敛**：EVV5 r1/r2 追加的 8 条指引在后续批次全部生效且无副作用，r3 无新增。
- **real_or_fictional 枚举验证**：real(9)/fictional(6) 两档均有实例，经边缘案例（天体 the-moon=real、神秘 great-eyrie=fictional）确认适配。
- **region 弹性验证**：常规（洲/国/城）+ 非常规（cislunar/subterranean/Arctic）层级均自然填出。
- **判定 converged**，不追加第 4 轮。place 模板定稿，四节结构 + `book`/`real_or_fictional`/`region` 专属字段定稿，不再变更。

## 遗留决议

### 决议 1：edit_page 后补跑 compute_quality（已固化为流程提示）

**背景**：R12 mount-franklin 用 `edit_page.py` 修引文保真度后，registry quality 变 None——`edit_page.py` 不触发 `_backfill_quality`（仅 `add_page.py` 回填）。QUO23（R14）已运行 compute_quality + build_registry 修正为 featured。

**决议**：在 place-schema.md 定稿节记流程提示——「**用 edit_page.py 修改页面内容后，需补跑 `compute_quality.py` + `build_registry.py`**，否则 registry quality 可能失配」。此为工具行为，非模板缺陷，作为通用操作提示适用所有类型。

### 决议 2：跨作品实体——暂不提 RFC

**背景**：technology gun-cotton（FEM+MI）+ place the-moon（FEM+RM）= 累计 2 个跨作品实体，单值 `book` 略局促。

**决议**：**暂不向 memex 提 RFC**。累计 2 例仍远低于经验阈值（≥5），正文点名其余作品并引 PN 已充分补偿；多值 book 字段会破坏 `build_registry.py` 既有单值语义。留 butler 长期观察项，累积到 ≥5 例再评估。

## 模板定稿动作

`place-schema.md` 追加「EVV6 定稿（converged）」一节，固化：(a) 收敛结论；(b) quality 工具计算权威 + edit_page 后补跑提示；(c) 跨作品单值 book 处置。无结构性字段变更。

## EXIT-GATE 预告

place 三轮 + EVV6 完成，下一步执行完整 E1–E5 出口质量门（作用域=15 页 place），通过后 place 类型结束，进入 character 类型。
