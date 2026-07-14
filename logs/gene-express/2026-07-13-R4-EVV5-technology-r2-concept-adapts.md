---
round: 4
date: 2026-07-13
phase: 9
gene: EVV5
type: technology
pages: [albatross, victoria-balloon, the-forward, gun-cotton, ships-compass]
result: converge
---

# R4 — EVV5 technology r2 质量评估（模板反思第二轮）

## 执行摘要

对 r2-SCN27 的 5 页做质量评估，重点：**验证 EVV5 r1 模板变更是否有效**、**评估 `category=concept` 与异质子领域对 schema 的压力**。结论：r1 变更全部生效且无副作用；schema 结构继续保持零偏差，已趋收敛。本轮仅追加一条跨作品实体处置指引（单值 `book` 字段），无结构性改动。

## r1 → r2 模板变更有效性

| EVV5 r1 变更 | r2 应用情况 | 判定 |
|--------------|-------------|------|
| Science & Speculation 建议纳入 standard | r2 全部 5 页均写此节，且在飞行器/气球/破冰船/炸药/罗盘 5 个异质子领域都自然成立（真实器械/物理 vs 外推框架） | 有效，跨子领域稳健 |
| 段落 ≤400 字 | gun-cotton Role 节主动拆三段，无退出码 8 | 有效 |
| 引文逐字核验 | 5 页引文全部 grep 核验；未再现 r1 的 spindle 类 PN 错位 | 有效 |

## 本轮压力测试结果

- **`category=concept`（gun-cotton）**：四节结构对抽象物质完全适用——Design & Operation 承载「MI-030 合成步骤 + 燃点/威力理化参数」，Role in the Story 承载「FEM 火炮装药 + MI 岛民补给」两作品用途，无空节、无生硬。**schema 无需为 concept 另开变体**。
- **高引注密度**：albatross/victoria-balloon/the-forward 引注 12–13，已达 featured 引注量级（≥8）且 Science & Speculation 含现实对照，实质满足 featured 三条件。当前档位仍记 standard 以与批次一致；**是否设「达标即提 featured」策略留 EVV6 定夺**。
- **单值 book 字段 vs 跨作品实体**：gun-cotton 横跨 FEM+MI，单值 `book` 略局促。处置：`book` 填主作品，正文点名其余作品并引 PN；已写入 schema「跨作品实体」指引。不新增多值字段（避免破坏 build_registry 既有语义）。

## 逐页复核

| 页面 | H2 顺序 | 4 节 | frontmatter | 引注 | 判定 |
|------|---------|------|-------------|------|------|
| albatross | ✓ | 4/4 | vehicle, inventor=Robur | 12 | pass |
| victoria-balloon | ✓ | 4/4 | vehicle, inventor=Dr. Ferguson | 13 | pass |
| the-forward | ✓ | 4/4 | vehicle, inventor=Captain Hatteras | 13 | pass |
| gun-cotton | ✓ | 4/4 | concept, inventor='' (真实物质，留空) | 8 | pass |
| ships-compass | ✓ | 4/4 | instrument, inventor='' | 9 | pass |

`inventor` 留空（gun-cotton/ships-compass 为真实器械/物质，无 in-story 发明者）符合 schema「可空」约定，未触发任何校验失败。

## 收敛判断

- **结构收敛**：连续两轮（10 页）H2 节序、frontmatter、引文规范零偏差 → schema 结构确认稳定。
- **待 r3 观察**：r3 拟选「边缘/复杂案例」（schema 流程要求），如：多组件系统、纯理论概念、或与已建页强耦合的实体，做最后一轮压力测试。若 r3 仍零偏差，EVV6 可判 converged。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 technology 三轮结束后（EVV6 之后）统一执行。

## 遗留问题

- 「达标即提 featured」策略未定，EVV6 决议。
- 跨作品 concept 的 book 字段为框架层面小张力（非本 wiki 可独修），已用正文补偿；若后续 concept 页增多可考虑向 memex 提 RFC，暂不处理。
