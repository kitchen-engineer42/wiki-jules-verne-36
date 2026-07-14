---
round: 2
date: 2026-07-13
phase: 9
gene: EVV5
type: technology
pages: [columbiad, lunar-projectile, the-terror, ruhmkorff-apparatus, diving-apparatus]
result: converge
---

# R2 — EVV5 technology r1 质量评估（模板反思首轮）

## 执行摘要

对 r1-SCN27 建的 5 个 technology 页做质量评估，对照 `local/template/technology-schema.md`，识别模板偏差、判断是否需要更新模板。结论：**模板结构无需改动，schema 已收敛**；仅追加一段「写作指引」固化本轮自发形成的良性写作模式（Science & Speculation 常态化 + 段落上限 + 引文核验），供 r2/r3 继承。

## 逐页评估

| 页面 | H2 顺序 | 4 节齐全 | 类型 frontmatter | 引注数 | quality | 判定 |
|------|---------|----------|------------------|--------|---------|------|
| columbiad | ✓ Overview/Design/Role/Science | 4/4 | book+inventor+category(weapon) | 11 | standard | pass |
| lunar-projectile | ✓ | 4/4 | book+inventor+category(vehicle) | 9 | standard | pass |
| the-terror | ✓ | 4/4 | book+inventor+category(vehicle) | 10 | standard | pass |
| ruhmkorff-apparatus | ✓ | 4/4 | book+inventor+category(instrument) | 6 | standard | pass |
| diving-apparatus | ✓ | 4/4 | book+inventor+category(instrument) | 8 | standard | pass |

- **H2 顺序**：5 页全部严格遵循 schema 规定顺序（Overview → Design & Operation → Role in the Story → Science & Speculation），无乱序、无缺节。
- **frontmatter 专属字段**：`book` / `inventor` / `category` 全部填全；`category` 取值均落在枚举内（weapon / vehicle / instrument），无 concept 类本轮（合理，r1 选的是具象机器/器械）。
- **引注密度**：平均 ~8.8 条，最低 6（ruhmkorff），全部 ≥ standard 门槛 5，且远超；无凑数引注（每条对应正文具体断言）。
- **wikilink 形式**：均用 label 形式（`[[Gun Club]]`、`[[Robur]]`、`[[Nautilus]]`、`[[Professor Lidenbrock]]`、`[[Ruhmkorff Apparatus]]`），符合 LAW §九。

## 模板偏差与处置

| 观察 | 是否偏差 | 处置 |
|------|----------|------|
| 5 页全部写了「选填」的 Science & Speculation 节 | 非缺陷，是良性超额 | 追加写作指引：standard 档建议纳入此节（凡尔纳技术类天然适配「真实器械 vs 外推」框架），仍标 ○ 不强制 |
| tags 比 schema 示例 `[technology, invention]` 更丰富（加时代/子领域标签） | 符合 LAW §十二 | 保留，不改 schema |
| aliases 多页非空（Épouvante、Ruhmkorff lamp 等） | 符合原文别名 | 保留 |
| 段落一度超 400 字触发 edit_page.py 退出码 8 | 工作流约束非模板缺陷 | 写作指引记录段落 ≤400 字规则 |
| corpus_search 快照与页面 PN 个别错位（spindle→MW-015-026） | 数据层缺陷（RFC-0002 同源） | 写作指引记录「以页面正文 grep 核验为准」；不改 schema |

**模板变更**：`technology-schema.md` 新增「写作指引（EVV5 r1）」一节（3 条），无结构性字段增删。r2 将继承此版模板。

## 收敛判断

- **结构收敛**：H2 节序、frontmatter 字段、引文规范三项 5 页零偏差 → schema 结构已稳定。
- **待观察**：r1 选的是具象大型机器 + 便携仪器；r2 拟选不同子领域（如载具航线类、通信/信号类、或 `category=concept` 的科学概念），验证 schema 对更抽象 technology 实体是否仍适用。若 concept 类暴露「Design & Operation 无实体参数可引」的张力，r2 EVV5 再议。

## EXIT-GATE 检查

本轮为评估轮，不新建页面；完整 E1–E5 出口门在 technology 三轮结束后（EVV6 之后）统一执行。

## 遗留问题

- Science & Speculation 是否应从 ○ 升为 standard 必填，待 r3 收集更多样本后由 EVV6 元反思定夺（当前证据倾向「建议但不强制」）。
- want-link（[[Gun Club]]、[[Robur]]、[[Professor Lidenbrock]] 等）待 character/organization 轮次建页后由 9-C wikify 回填。
