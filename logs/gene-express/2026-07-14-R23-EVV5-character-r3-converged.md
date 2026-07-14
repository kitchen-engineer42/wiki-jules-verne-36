---
round: 23
date: 2026-07-14
phase: 9
gene: EVV5
type: character
pages: [top, robur, aouda, conseil, barbicane]
result: converge
---

# R23 — EVV5 character r3 质量评估（模板反思第三轮 · 收敛检查）

## 执行摘要

对 R21 r3 的 5 个边缘/复杂角色页做质量评估，重点：**检查模板是否趋于收敛**。结论：**character 模板结构确认收敛**——连续三轮（15 页）H2 五节序、frontmatter 专属字段、引文规范零偏差；r3 的五类边缘压力（动物角色、跨作品反派、女性角色、痴迷型仆从、科学领袖）schema 全部无摩擦吸收，**零模板追加**。追加量轨迹 8→5→0，与 place（5→3→0）、technology（3→2→0）同构。

## r3 边缘案例适配复核

| 边缘类型 | 页面 | schema 承压点 | 结果 |
|----------|------|---------------|------|
| 动物角色 | top（犬）| 非人实体作 character | 无摩擦——role=supporting，五节以叙事职能填满 |
| 跨作品反派 | robur（RC+MW）| 单值 book + 反派跨两作 | 无摩擦——book=RC，MW 正文引 PN |
| 女性角色 | aouda | 着墨少能否 featured | 成立——3 引注工具判 featured |
| 痴迷型仆从 | conseil | vs ned-land 塌缩 | 不塌缩——分类癖 vs 逃亡欲 |
| 科学领袖 | barbicane | vs michel-ardan 重叠 | 不重叠——冷静方法 vs 鲁莽热情 |

## 逐页复核

| 页面 | H2 五节 | role | 引注 | overlap warn | 判定 |
|------|---------|------|------|--------------|------|
| top | 5/5 | supporting | 4 | 无 | pass |
| robur | 5/5 | antagonist | 5 | 无 | pass |
| aouda | 5/5 | supporting | 3 | 无 | pass |
| conseil | 5/5 | supporting | 3 | 无 | pass |
| barbicane | 5/5 | protagonist | 4 | 无 | pass |

H2 五节序 5 页严格遵循 Overview → Role in the Story → Character & Traits → Relationships → Appearances。

## 收敛判断（三轮汇总）

- **结构收敛确认**：r1（最强主角）、r2（新子领域：narrator/antagonist/supporting）、r3（边缘案例）三个差异化批次，H2 五节序 / frontmatter 字段 / 引文规范三项 15 页零偏差。
- **模板迭代轨迹**：EVV5 r1 追加 1 澄清 + 7 写作指引（wikilink 节 PN 豁免、五节自然成立、跨作品 book、段落≤400、meta 避 warn、4-char Note、quality 省略+edit_page 补跑、引文核验）；EVV5 r2 追加 4 写作指引 + 1 质量表述调整（role 四档、affiliation 取值、label 消歧、featured 引注门工具判定）；**r3 追加 0 条**。均为写作指引/表述层面，无一次触及结构性字段增删。
- **r3 无新增模板变更**：最难的边缘批次也不再产生模板压力，**收敛的直接证据**。

## 本轮工具经验（交 EVV6）

- **RC corpus_search 排序陷阱**：搜 "Robur" 前 40 命中全 MW，RC 命中被淹没。改用 `grep data/sentence_index/RC-*.jsonl`（sid 内嵌 PPP）+ 精确短语回验。建议固化为「同名角色跨作品定位时直读 sentence_index」提示，交 EVV6。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 EVV6 之后统一执行。

## 遗留问题（交 EVV6）

1. **收敛定稿**：character 模板追加量 8→5→0，与 place/technology 同构，EVV6 判 converged 并在 character-schema.md 追加定稿节。
2. **跨作品实体累计 4 例**：robur 使累计达 4（逼近 5 阈值），EVV6 评估 butler 观察计数机制。
3. **RC/sentence_index 定位提示**：是否固化为模板级工具提示。
