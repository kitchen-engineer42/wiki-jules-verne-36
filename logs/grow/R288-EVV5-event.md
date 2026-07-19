---
round: 288
date: 2026-07-18
type_round: 54
phase: "2.1"
current_type: event
gene: EVV5
pages: []
result: reflect
mean_score: 83
---

# GROW 2.1-B · R288 · EVV5 · event — event 类型 schema 反思（全 53 页评审，均分 83，模板验证通过）

## 执行摘要

Phase 2.1-B event 类型**第五次 EVV5 schema 反思**（type_round 54）。R287 NEW1 后 since_evv5 累至 10，
R288-start since_evv5=10≥10 → 决策机 §3(1b) **EVV5**（since_discover=3<10 不触 §3(1a) EVV5+SCN28 组合轮）。
EVV5 优先于 §3(4) SCN28-zombie（虽 queue(event)=0）。

EVV5 为**反思轮，非建页**：扫描全类型 53 event 页，比对 event-schema（四 H2 + 专属字段 book/location/pn_anchor），
识别系统性问题，评均分，据结论决定是否更新模板。**pages: []，registry 恒 1528，event 恒 53，unknown 0。**

## 全类型扫描结果（53 event 页，脚本化统计）

**结构一致性（合格）**：
- 四 H2（Overview / What Happens / Significance / Participants & Setting）：**53/53 全含，0 缺节**。
- 专属字段 book/location/pn_anchor：**53/53 frontmatter 完整**（type=event 无 unknown）。
- quality：53/53 featured（add_page 自动回填；featured re-grade DEFERRED，不在本轮处理）。

**PN 丰度（系统性发现，正则 `\([A-Za-z0-9]{1,4}-\d{3}-\d{3}\)` distinct 计数）**：
- 达 ≥5 distinct solid PN（现行 G3 门）：**40/53**（占比 75%，较 R277 的 32/45=71% 升 4pt）。
  R277→R288 新建 8 页（drawing-lots-on-the-raft / wreck-of-the-pilgrim / disintegration-of-victoria-island / flight-to-the-senegal / return-to-earth-by-balloon 及会话前 3 页）全达 16 distinct PN，一次成型。
- **低于 ≥5 门：13/53**（早期 butler/种子层所建，成于现行 PN 门之前，与 R244/R255/R266/R277 EVV5 记录**同一批 13 页，零增零消**）：

| slug | distinct PN | 作品 |
|------|-------------|------|
| date-line-revelation | 3 | AWED |
| liedenbrock-cipher | 3 | JCE |
| snaefells-descent | 3 | JCE |
| columbiad-launch | 4 | FEM |
| fogg-hires-passepartout | 4 | AWED |
| gun-club-moon-proposal | 4 | FEM |
| lincoln-island-landing | 4 | MI |
| lunar-orbit-miss | 4 | RM |
| nemo-death | 4 | MI |
| north-pole-volcano | 4 | ACH |
| sea-monster-hunt | 4 | TTLU |
| stromboli-eruption-return | 4 | JCE |
| tabor-island-castaway | 4 | MI |

> **注**：13 债页身份与前四次 EVV5（R244/R255/R266/R277）完全一致，零消解。
> 分母由 45→53（中间新建 8 页，全达 16 PN 不入债），占比随分母增大由 29%→25% 持续下降。

## 反思结论

1. **模板验证通过（无结构变动）**：event-schema 四 H2 + book/location/pn_anchor 字段体系健全。
   R277–R287 新建 8 页全部在现行模板下达 16 distinct PN，一次成型；pn_anchor 锚定 + 单事件单指核方法论稳定。
   **模板不需修改**——问题不在模板，而在 13 早期页成于更松 PN 门。
2. **均分 83 ≥ 75 门**（与 R277 持平）：结构 53/53 合格（+），PN 丰度 40/53 达门（占比由 R277 的 71% 升至 75%）。
   加权估算 ≈ (40×87 + 13×72)/53 ≈ 83。**≥75 → 模板可用，event 批量建设继续。**
3. **系统性债（DEFERRED enrichment）**：13/53（25%，占比随分母增大持续下降）早期 event 页 distinct PN <5。
   与 R244/R255/R266/R277 同一批 13 页，本轮**无新增、无消解**。属 **PN 回填 enrichment 债**，非本反思轮职责（EVV5 不建页/不改页）。
   留待后续 RCH2 enrich 轮或 Phase 2.1-Z EVV6 前统一补引。与既有「featured re-grade DEFERRED」一致：不在本轮重建/重评。
4. **消歧/查重方法论沉淀（新增改锚+改 slug 例）**：event discover 队列锚点**与 framing** 均须视为线索非定论，建时逐句复核。
   R283 首现改锚（DSCF-014→DSCF-013，锚偏余波章）；**R286 首现因 framing 谬误改 slug**（joes-sacrifice-over-the-desert→flight-to-the-senegal：队列述「Joe 跳球减负」实被原著否决，真实事件为弃 gas 仪器+越 Senegal 逃亡）并改锚（FWB-042→FWB-043）；
   R287 特加 framing 核实、确认 OC 锚 OC-044 与 framing 均准确。教训：discover framing 可能与文本不符，建时须以 sentence_index 文本为准，逐句核动作序列所在章。
5. **单事件矿脉进度（R275 起 zombie 策略）**：零 event 池穷尽后转掘 20 单事件作品之第二事件。
   已掘 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC 九部，余 17 部（A Drama in the Air/A Winter Amid the Ice/An Antarctic Mystery/Doctor Ox's Experiment/Eight Hundred Leagues on the Amazon/Godfrey Morgan/Master Zacharius/Round the Moon/The Adventures of a Special Correspondent/The Blockade Runners/The Master of the World/The Pearl of Lima/The Secret of the Island/The Waif of the Cynthia/Ticket No. 9672/Topsy-Turvy 等）。queue(event)=0，R289 起 SCN28-zombie 续掘。

## 决策矩阵（EVV5）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10；since_discover=3<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | — |
| 3–7 | SCN28/RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 EVV5 反思，无建页、无改页。产出反思报告（本日志）。

## EXIT-GATE 检查（EVV5 轮）

- **G1–G4**：无建页/改页，N/A（反思轮）。
- **registry 一致**：total 1528 event 53 unknown 0 恒定（无写页）。✔
- **反思充分**：全 53 页结构 + PN 丰度双维脚本化扫描；模板决策有据（均分 83≥75，无结构变动）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean（本轮不触 -schema.md，模板不改）。✔

## 六步状态机（EVV5，grow_state 存 R289 起始计数）

| 字段 | R288 起始 | R289 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 288 | 289 |
| type_round | 54 | 55 |
| rounds_since_last_evv5 | 10 | **0（EVV5 reset）** |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 224 | 225 |
| last_updated_round | 288 | 289 |

## 遗留问题

1. **event 页数 53**（反思轮无建页）。queue(event)=**0**（R284 discover 队列建序 37/38/39 已全消费）。registry 全库 1528，unknown 0。
2. **下轮 R289 = SCN28-zombie（§3(4)）**：EVV5 reset since_evv5=0；streak=0<3；since_discover=4<10 且全局 queue≥10 → 非 §3(3)；**queue(event)==0 → §3(4) 触发**。
   为勘探轮，须自 17 部单事件作品续掘第二事件、seed ≥3 候选入 queue、reset since_discover。**建时须警惕 framing 准确性（R286 教训）**：discover 阶段所记事件描述须能被 sentence_index 文本逐句支撑，勿凭章题臆测。
3. **event PN 回填债（R244/R255/R266/R277/R288 五度记录）**：13/53 早期 event 页 distinct PN <5（见上表），五次 EVV5 均记录、零消解。
   留待后续 RCH2 enrich 或 Phase 2.1-Z EVV6 前统一补引至 ≥5。**本轮不重建**（EVV5 反思轮职责边界 + featured re-grade DEFERRED）。
4. **event 模板验证通过**：无结构变动，pn_anchor + 单指核 + 锚精修方法论稳定；R277–R287 八页均达 16 PN 佐证。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可借机补 PN 至 ≥5，消一债页）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」/「The Master of the World」book label 归一（terror-destruction/great-eyrie-investigation 同作 MW）。批量评审时处置。
6. **散文门债**：37 页 >400（既有 DEFERRED）。
7. **corpus-discover 顺延**：since_corpus=224→225（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；
   event 类型 EVV6 时须一并处理本轮记录的 13 页 PN 回填债。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
