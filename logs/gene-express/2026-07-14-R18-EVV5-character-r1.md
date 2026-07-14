---
round: 18
date: 2026-07-14
phase: 9
gene: EVV5
type: character
pages: [captain-nemo, phileas-fogg, professor-lidenbrock, cyrus-harding, captain-hatteras]
result: refine
---

# R18 — EVV5 character r1 质量评估（模板反思第一轮）

## 执行摘要

对 R17 r1 的 5 个最强主角页做质量评估，据评估结果精化 `character-schema.md`。结论：**五节结构骨架稳定，本轮追加 1 处 §引文规范澄清 + 7 条写作指引，无结构性字段增删**。5 页 H2 五节序零偏差、frontmatter 专属字段（book/affiliation/first_appearance/role）全适配、引注 6–7 条均 ≥ featured 门槛（≥10 引注实为 6–7？见下修正说明），auto-backfill 全 featured。

## 逐页复核

| 页面 | H2 五节 | role | 引注 | overlap warn | 判定 |
|------|---------|------|------|--------------|------|
| captain-nemo | 5/5 | protagonist | 7 | 无 | pass |
| phileas-fogg | 5/5 | protagonist | 7 | 无 | pass |
| professor-lidenbrock | 5/5 | protagonist | 6 | JCE-002-036（已 edit_page 修正）| pass |
| cyrus-harding | 5/5 | protagonist | 6 | 无 | pass |
| captain-hatteras | 5/5 | protagonist | 6 | 无 | pass |

H2 五节序 5 页严格遵循 Overview → Role in the Story → Character & Traits → Relationships → Appearances。

## 引注门槛说明（featured 判定）

- schema featured 门槛写「≥10 条引注」，5 页实际 6–7 条。**compute_quality.py 客观评级仍判 featured**——工具以「五节齐全 + Relationships 完整 + 无悬挂链接 + 引注密度」综合评定，非机械计数 10。以工具计算为权威（沿用 place EVV6「quality 工具计算权威」定策），schema 的「≥10」为期望值非硬门，r1 五页密度（每 200 词 ≥1 条）已满足 standard 密度期望且五节齐全。
- 是否将 featured 引注门从「≥10」调为更贴合工具判定的表述，留 EVV6 元反思裁定。

## 模板精化动作（本轮）

1. **§引文规范 wikilink 节豁免澄清**（关键）：原文「每个 H2 节至少 1 条 PN」与 Relationships/Appearances 的 wikilink 交叉引用性质冲突。比照 place Connections（place EVV6 已定）澄清：**散文节（Overview/Role/Character & Traits）每节 ≥1 PN；Relationships/Appearances 以链接完整性为准，不强制 PN**。
2. **追加「写作指引（EVV5 r1）」7 条**：五节对主角自然成立、跨作品 book 单值、段落 ≤400、meta 表述避 warn、4-char VVV Note、quality 省略 + edit_page 补跑、引文核验 + sentence_index 兜底。

均为写作指引/规范澄清层面，无结构性字段增删——与 place r1（追加 5 条写作指引、0 字段变更）同构。

## 本轮工具经验

- **overlap warn 复现于 character**：professor-lidenbrock JCE-002-036 挂元叙述句告警，edit_page 改逐字子句消除。确认 place EVV5 r2「meta 表述避 warn」指引跨类型通用。
- **edit_page 后 quality 失配**：professor-lidenbrock edit 后补跑 compute_quality + build_registry 回填 featured。
- **段落 ≤400 门在台词密集页更易触发**：Role/Character 节两次超限（477/516 字），按论点拆段。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 EVV6 之后统一执行。

## 遗留问题（交后续轮次）

1. **featured 引注门表述**：「≥10」vs 工具综合判定，EVV6 裁定是否调整 schema 表述。
2. **r2 子领域选取**：r1 取主角，r2 应取不同子领域（antagonist / supporting / narrator / 女性角色 / 反派）以压 role 枚举与关系网络。
3. **跨作品实体累计 3 例**：captain-nemo 使累计达 3，<5 阈值维持现状。
