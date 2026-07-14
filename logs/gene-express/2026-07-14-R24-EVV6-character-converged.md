---
round: 24
date: 2026-07-14
phase: 9
gene: EVV6
type: character
pages: []
result: converged
---

# R24 — EVV6 character 元反思（横向分析三轮 EVV5，模板定稿）

## 执行摘要

读取三份 character EVV5 日志（R18 r1、R20 r2、R23 r3）横向分析，对 `character-schema.md` 做最终定稿判断。结论：**模板 converged**。三个差异化批次（最强主角 → 新子领域 → 边缘复杂案例）15 页零结构偏差，两次模板追加均属写作指引/表述层面、无结构性字段增删，且 r3 最难批次零追加。本轮完成遗留决议：**跨作品实体累计 4 例留 butler 观察**、**edit_page 后补跑 compute_quality 固化**、**同名角色 sentence_index 定位提示固化**。

## 三轮 EVV5 横向分析

| 维度 | r1（R18）| r2（R20）| r3（R23）| 趋势 |
|------|---------|---------|---------|------|
| 结构偏差 | 0 | 0 | 0 | 稳定零偏差 |
| 模板变更 | 1 澄清 + 7 指引 | 4 指引 + 1 表述 | 0 | 追加量 8→5→0 |
| 变更性质 | 规范澄清 + 写作指引 | 写作指引 + 表述 | — | 从不触及结构 |
| 压力来源 | 五节适配/wikilink 节 PN | role 枚举/affiliation/label | 边缘案例全吸收 | 压力递减 |
| 子领域 | 五主角 | narrator/antagonist/supporting | 动物/跨作反派/女性/仆从/领袖 | 覆盖渐广 |

**关键判据**：模板追加量 8→5→0，且 r3（专挑边缘/复杂案例）**零追加**——最能暴露 schema 盲点的批次也未产生新指引需求，是收敛的决定性证据。五节结构（Overview / Role in the Story / Character & Traits / Relationships / Appearances）与专属 frontmatter（book / affiliation / first_appearance / role）经 15 页四档 role 全覆盖验证，骨架自 r1 即稳定。与 place（5→3→0）、technology（3→2→0）收敛轨迹同构。

## 收敛判断：converged

- **结构收敛**：H2 五节序 / frontmatter / 引文规范三项 15 页零偏差。
- **写作指引收敛**：EVV5 r1/r2 追加的指引在后续批次全部生效且无副作用，r3 无新增。
- **role 枚举验证**：四档均有实例（protagonist 6 / supporting 6 / antagonist 2 / narrator 1），经边缘案例（动物 top、跨作反派 robur、误判反派 fix）确认适配。
- **判定 converged**，不追加第 4 轮。character 模板定稿，五节结构 + `book`/`affiliation`/`first_appearance`/`role` 专属字段定稿，不再变更。

## 遗留决议

### 决议 1：跨作品实体累计 4 例——留 butler 观察计数

**背景**：technology gun-cotton（FEM+MI）+ place the-moon（FEM+RM）+ character captain-nemo（TTLU+MI）+ character robur（RC+MW）= 累计 4 个跨作品实体，逼近 5 经验阈值。

**决议**：**暂不提 RFC**。维持单值 `book`（主作品）+ 正文点名其余作品并引 PN。多值 book 字段会破坏 `build_registry.py` 既有单值语义。作为 butler 长期观察项，**累积到 ≥5 例再评估**。「出场跨作品」（michel-ardan/barbicane FEM+RM，仅 Appearances 列他作）不计入。

### 决议 2：edit_page 后补跑 compute_quality（已固化）

**背景**：R17 professor-lidenbrock 用 edit_page 修 overlap warn 后 quality 未回填。

**决议**：在 character-schema.md 定稿节记流程提示（沿用 place EVV6），通用操作提示适用所有类型。

### 决议 3：同名角色跨作品 sentence_index 定位（已固化）

**背景**：R21 搜 "Robur" 前 40 全 MW，RC 命中被淹。

**决议**：定稿节记提示——跨作品同名角色改用 `grep data/sentence_index/{VVV}-*.jsonl` + 精确短语回验。

## 模板定稿动作

`character-schema.md` 追加「EVV6 定稿（converged）」一节，固化：(a) 收敛结论；(b) role 枚举定稿（含非人角色）；(c) quality 工具计算权威 + edit_page 补跑；(d) 跨作品单值 book + butler 观察；(e) 同名角色 sentence_index 定位提示。无结构性字段变更。

## EXIT-GATE 预告

character 三轮 + EVV6 完成，下一步执行完整 E1–E5 出口质量门（作用域=15 页 character），通过后 character 类型结束，进入 event 类型。
