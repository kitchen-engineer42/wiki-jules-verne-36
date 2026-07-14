---
round: 20
date: 2026-07-14
phase: 9
gene: EVV5
type: character
pages: [axel, passepartout, fix, ned-land, michel-ardan]
result: refine
---

# R20 — EVV5 character r2 质量评估（模板反思第二轮）

## 执行摘要

对 R19 r2 的 5 个非主角角色页做质量评估，据结果精化 `character-schema.md`。结论：**结构骨架继续稳定，本轮追加 4 条写作指引 + 1 处质量阈值表述调整，无结构性字段增删**。追加量 r1（1 澄清 + 7 指引）→ r2（4 指引 + 1 表述）呈递减，与 place（r1 5 条 → r2 3 条）同构趋势。5 页零 overlap warn，role 枚举四档经 r2 补齐全覆盖。

## 逐页复核

| 页面 | H2 五节 | role | affiliation | 引注 | 判定 |
|------|---------|------|-------------|------|------|
| axel | 5/5 | narrator | （空）| 5 | pass |
| passepartout | 5/5 | supporting | （空）| 5 | pass |
| fix | 5/5 | antagonist | Scotland Yard | 6 | pass |
| ned-land | 5/5 | supporting | （空）| 4 | pass |
| michel-ardan | 5/5 | supporting | （空）| 4 | pass |

H2 五节序 5 页零偏差。

## r2 承压点适配复核

| 承压点 | 页面 | 结果 |
|--------|------|------|
| narrator 枚举首用 | axel（第一人称叙述者）| 无摩擦——Role 述其被动卷入 + 恐惧视角 |
| antagonist 枚举首用 | fix（误判追捕）| 无摩擦——「误判型反派」归 antagonist，非恶意亦可 |
| affiliation 非空首用 | fix=Scotland Yard | 无摩擦——有组织身份即填 |
| 裸名 label 碰撞 | fix（"Fix" 常用词）| label="Detective Fix" + aliases=[Fix] 消歧 |
| 低引注数 featured | ned-land/ardan（4 引注）| 工具综合判定 featured，非机械计 10 |

## 模板精化动作（本轮）

追加「写作指引（EVV5 r2）」4 条：
1. role 枚举四档全覆盖（antagonist 不限恶意）。
2. affiliation 非空档取值规则。
3. 裸名/常用词角色 label 消歧。
4. featured 引注门以工具判定为准。

并将质量阈值表 featured 行「≥10 条引注」调为「引注充分（工具综合判定，期望 ≥8）」，消解 schema 表述与 compute_quality 实判的张力（r1 遗留问题 1）。均为写作指引/表述层面，无结构性字段增删。

## 本轮工具经验

- **r2 零 warn**：吸取 r1 professor-lidenbrock 的 meta 表述教训，r2 所有引注均挂逐字子句，无一 overlap warn，无需 edit_page 返工。
- **auto-backfill 稳定**：5 页省略 quality 字段，add_page 全回填 featured，无失配。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 EVV6 之后统一执行。

## 遗留问题（交 r3/QUO23/EVV6）

1. **r3 边缘案例**：跨作品角色深化、群像/集体、动物角色（Top 犬）、极短出场，压 schema 最后盲点。
2. **模板追加量趋势**：r1→r2 递减（8→5），若 r3 趋 0 即可判 converged（比照 place 5→3→0、technology 3→2→0）。
3. **跨作品实体累计 3 例**：维持单值 book，<5 阈值不提 RFC。
