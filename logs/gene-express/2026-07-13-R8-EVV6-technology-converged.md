---
round: 8
date: 2026-07-13
phase: 9
gene: EVV6
type: technology
pages: []
result: converged
---

# R8 — EVV6 technology 元反思（横向分析三轮 EVV5，模板定稿）

## 执行摘要

读取三份 EVV5 日志（R2 r1、R4 r2、R7 r3）横向分析，对 `technology-schema.md` 做最终定稿判断。结论：**模板 converged**。三个差异化批次（具象机器/仪器 → 航空航海载具+concept → 边缘复杂案例）15 页零结构偏差，两次模板追加均属写作指引层面、无结构性字段增删，且 r3 最难批次不再产生任何模板压力。本轮完成三项遗留决议：**quality 口径统一为工具计算权威**（已执行，16 页全部对齐 featured）、**跨作品 book 字段暂不提 RFC**、**weapon 样本偏少列 butler 观察项**。

## 三轮 EVV5 横向分析

| 维度 | r1（R2）| r2（R4）| r3（R7）| 趋势 |
|------|---------|---------|---------|------|
| 结构偏差 | 0 | 0 | 0 | 稳定零偏差 |
| 模板变更 | +写作指引3条 | +跨作品实体指引2条 | 0（无变更）| 追加量递减→0 |
| 变更性质 | 写作指引 | 写作指引 | — | 从不触及结构 |
| 压力来源 | 段落长度/引文错位 | concept 适配/单值book | 边缘案例全吸收 | 压力递减 |
| 子领域 | 火炮/弹舱/便携仪器 | 载具/气球/破冰船/concept/仪器 | 望远镜/炸药/升降机/电力/木筏 | 覆盖渐广 |

**关键判据**：模板追加量 3→2→0，且 r3（专挑边缘/复杂案例）**零追加**——最能暴露 schema 盲点的批次也未产生新指引需求，是收敛的决定性证据。四节结构（Overview / Design & Operation / Role in the Story / Science & Speculation）与专属 frontmatter（book / inventor / category）经 15 页四类 category 全覆盖验证，骨架自 r1 即稳定。

## 收敛判断：converged

- **结构收敛**：H2 节序 / frontmatter / 引文规范三项 15 页零偏差。
- **写作指引收敛**：EVV5 r1/r2 追加的 5 条指引在后续批次全部生效且无副作用，r3 无新增。
- **category 枚举验证**：vehicle(7)/weapon(1)/instrument(5)/concept(3) 四类均有实例，concept 经两页（gun-cotton、nitroglycerine/nemo-electricity）确认适配。
- **判定 converged**，不追加第 4 轮。technology 模板定稿，可作为 place/character/event 三类型 schema 设计的方法论范本（三轮差异化批次 + 每句有据 + 工具判档）。

## 遗留决议

### 决议 1：quality 口径统一为工具计算权威（已执行）

**背景**：r1/r2 页 frontmatter 显式写 `quality: standard`（人工floor），add_page 的 `_backfill_quality` 尊重显式声明故不覆盖；r3 页省略 quality 字段，工具自动回填 `featured`。导致同等质量页档位不一致。

**核查**：`compute_quality.py --dry-run --report` 显示全部 16 页客观评分 43–59，**均达 featured**（全 4 节 + 引注≥8 + Science & Speculation 含现实对照）。r1/r2 的 standard 是人工 floor 下压，非真实质量。

**决议**：
1. **工具计算为权威**——`compute_quality.py` 的评级是全库一致的客观标准，优先于人工 floor。
2. **已执行对齐**：运行 `compute_quality.py`（仅升级模式）+ `build_registry.py` 重建，16 页 technology 全部 `quality: featured`，registry 已刷新（`{'featured': 16}`）。
3. **后续批次策略**：place/character/event 建页时**省略 frontmatter 的 quality 字段**，交 add_page 自动回填；日志不再手记档位，以工具计算为准。BIRTH「quality: standard」目标理解为**最低floor**而非固定值，超出即如实记为 featured。

### 决议 2：跨作品 book 字段——暂不提 RFC

**背景**：EVV5 r2 记 gun-cotton 跨 FEM+MI，单值 `book` 略局促。r3 未再现（nitroglycerine/nemo-electricity 均单作品）。

**决议**：**暂不向 memex 提 RFC**。理由：跨作品 concept 目前仅 gun-cotton 一例，正文点名其余作品并引 PN 已充分补偿；多值 book 字段会破坏 `build_registry.py` 既有单值语义。留 butler 循环，若跨作品实体累积到一定数量（经验阈值 ≥5 例）再评估提 RFC。记为 butler 长期观察项。

### 决议 3：weapon category 样本偏少——butler 观察项

QUO23 已记：weapon 仅 columbiad 一例，非选页偏差（凡尔纳纯武器类实体稀少）。非模板问题，butler 循环补页时留意（如 the-terror 舰载武器、MI 火炮等）。

## 模板定稿动作

`technology-schema.md` 追加「EVV6 定稿（converged）」一节，固化：(a) 收敛结论；(b) quality 工具计算权威策略；(c) 三决议指针。无结构性字段变更。

## EXIT-GATE 预告

technology 三轮 + EVV6 完成，下一步执行完整 E1–E5 出口质量门（作用域=16 页 technology），通过后 technology 类型结束，进入 place 类型。
