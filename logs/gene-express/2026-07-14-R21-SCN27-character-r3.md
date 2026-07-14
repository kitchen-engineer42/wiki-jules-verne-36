---
round: 21
date: 2026-07-14
phase: 9
gene: SCN27
type: character
pages: [top, robur, aouda, conseil, barbicane]
result: pass
---

# R21 — SCN27 character r3（边缘/复杂案例批次）

## 执行摘要

character 类型 pilot 第三轮（r3），专挑**边缘/复杂角色**压 `character-schema` 盲点：动物角色（top 犬）、跨作品反派（robur RC+MW）、女性角色（aouda）、痴迷型仆从（conseil）、科学领袖（barbicane）。5 页用 r2 精化后的 schema 建成，全部 auto-backfill featured，零 overlap warn，五节结构无摩擦吸收全部边缘压力。

## 页面处理记录

| 页面 | book | role | affiliation | 引注数 | 引注 PN | quality |
|------|------|------|-------------|--------|---------|---------|
| top | The Mysterious Island | supporting | （空）| 4 | MI-001-028, MI-002-046, MI-003-011, MI-006-032 | featured |
| robur | Robur the Conqueror | antagonist | （空）| 5 | RC-003-027, RC-004-015, RC-007-032, MW-015-053, MW-016-002 | featured |
| aouda | Around the World in Eighty Days | supporting | （空）| 3 | AWED-013-011, AWED-014-008, AWED-014-011 | featured |
| conseil | Twenty Thousand Leagues Under the Seas | supporting | （空）| 3 | TTLU-003-007/009/011 | featured |
| barbicane | From the Earth to the Moon | protagonist | Gun Club | 4 | FEM-002-002/009, FEM-007-003 | featured |

## r3 边缘案例适配复核

| 边缘类型 | 页面 | schema 承压点 | 结果 |
|----------|------|---------------|------|
| 动物角色 | top（犬）| 非人实体能否作 character | 成立——role=supporting，五节以「忠诚 + 本能预警」自然填满，无空节 |
| 跨作品反派 | robur（RC+MW）| 单值 book + 反派跨两作 | 无摩擦——book=RC（首现且最详），MW 正文引 PN；cross-work 实体第 4 例 |
| 女性角色 | aouda | 语料着墨较少能否 featured | 成立——3 引注经工具综合判定 featured |
| 痴迷型仆从 | conseil | vs ned-land 塌缩 | 不塌缩——分类癖 vs 逃亡欲，职责清晰互补 |
| 科学领袖 | barbicane | vs michel-ardan 重叠 | 不重叠——冷静方法 vs 鲁莽热情，Gun Club 领袖 vs 志愿乘客 |

## 本轮要点

- **动物角色作 character 验证**：top 是首个非人 character 实体。schema 无「人类」硬约束，role=supporting 适配，五节以叙事职能（本能预警、忠诚）填写，证明 character 类型可容纳叙事中承担角色职能的动物。
- **跨作品实体累计升至 4**：robur（RC+MW）为第 4 个跨作品实体（+technology gun-cotton、place the-moon、character captain-nemo）。仍 <5 阈值，维持单值 book + 正文引其余作品 PN。**逼近阈值，EVV6 需评估是否 R24 后启动 butler 观察计数**。
- **barbicane/michel-ardan 跨作品出场辨析**：二者均 FEM+RM，但按 R19 既定——「出场跨作品」（主作品 FEM 建实体，RM 列 Appearances）不计入「跨作品实体」（同一实体在两作均实质展开）。故 barbicane 不增 cross-work 计数，仅 robur 计入。
- **4-char VVV Note**：aouda（AWED）、conseil（TTLU）加渲染 Note；top（MI）、robur（RC/MW）、barbicane（FEM）无需。
- **RC 语料 corpus_search 排序陷阱**：搜 "Robur" 前 40 命中全 MW（排序更高），RC 命中被淹没。改用 `grep data/sentence_index/RC-*.jsonl` 直接定位（sid 格式 `RC-NNN-PPP-sN` 内嵌 PPP），再以精确短语 corpus_search 回验 PN。

## EXIT-GATE 检查

r3 建页轮，不做完整 E1–E5（留 QUO23/EVV6）。即时核查：
- QUO7 `pn_format_lint.py --fix`：5 页无问题。
- `lint_bucket_structure.py --fix`：分桶正常。
- H2 五节序 5 页遵循 Overview → Role in the Story → Character & Traits → Relationships → Appearances。

## 遗留问题（交 QUO23/EVV6）

1. **收敛判断**：r3 边缘批次零模板追加？（本轮建页未触发 schema 变更，EVV5 r3 复核确认）。若确认零追加，EVV6 判 converged。
2. **跨作品实体累计 4 例**：逼近 5 阈值，EVV6 评估 butler 观察计数或提前预警。
3. **QUO23 配额核查**：15 页 character 三轮累计的 role 分布、作品分布、real 无关（character 无 real_or_fictional）、quality 达标待 QUO23 核。
