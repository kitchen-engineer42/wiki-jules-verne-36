---
round: 322
date: 2026-07-19
type_round: 15
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R322 · SCN28 · character — 第三批 discover（queue 归 0，补 6 候选深化 SC/MS 簇）

## 执行摘要

Phase 2.1-B character 第三批候选发现（type_round 15）。上轮 R321 消费队列末条建序 62（michel-strogoff），**queue(character) 归 0** → 决策机 §3(4) SCN28-zombie 触发（且 §3(3) queue<10、since_discover=7 亦成立）。本轮**不建页**，仅为 character 补给候选队列。

**新增 6 候选（建序 63–68）**，全部 exact-slug filesystem dup-check ABSENT，全部富 grounding：

| 建序 | slug | label | book | pn_anchor | role | grounding |
|------|------|-------|------|-----------|------|-----------|
| 63 | mary-grant | Mary Grant | In Search of the Castaways | SC-004 | supporting | 首现 SC-004，83 mentions |
| 64 | john-mangles | John Mangles | In Search of the Castaways | SC-001 | supporting | 首现 SC-001，272 mentions（富矿）|
| 65 | mcnabbs | Major McNabbs | In Search of the Castaways | SC-001 | supporting | 首现 SC-001，167 mentions |
| 66 | thalcave | Thalcave | In Search of the Castaways | SC-015 | supporting | 首现 SC-015，137 mentions |
| 67 | nadia | Nadia | Michael Strogoff | MS-008 | supporting | 首现 MS-008 |
| 68 | ivan-ogareff | Ivan Ogareff | Michael Strogoff | MS-002 | antagonist | 首现 MS-002 |

**批次策略**：深化 R320/R321 刚建之 SC 簇（glenarvan/paganel/ayrton）与 MS 簇（michel-strogoff + work + events），最大化建成后互链回报。SC 四角（Mary Grant/John Mangles/McNabbs/Thalcave）皆 Duncan 号核心随行者，与既建 glenarvan 直接关联（thalcave 已被 glenarvan SC-018-042 引注）；MS 二角（Nadia/Ogareff）为 michel-strogoff 页已文本提及者（MS-029-005 Nadia、MS-015-052 须避 Ogareff），建成即消悬钩。

**new_candidates=6 ≥ type_close_new_candidate_min(3)** → 非低产，`discover_streak_low` 保持 0（不进逼类型关闭）。

**未触及 registry / 页面**：本轮无 add_page/edit_page，registry 维持 total 1551 character 27 unknown 0。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=0<10、since_discover=7 | **成立** |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

> §3(3) 与 §3(4) 同时成立；queue==0 归 §3(4) zombie discover（强制补给，解僵尸轮）。

## 页面处理记录

（本轮为 discover，无页面新建/编辑。）

## EXIT-GATE 检查

- **G4 脚本建页**：本轮无建页，仅编辑 queue.md（butler 候选，非 pages/**）。✔
- **discover 充分性**：6 候选均 dup-check ABSENT + grounding 已核（SC/MS sentence_index mentions ≥83）。✔
- **registry 一致**：未触及，total 1551 character 27 unknown 0。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

> discover 轮 EXIT-GATE 仅 G4 与 discover 充分性适用（无 G1/G2/G3/G5，无建页/编辑实体页）。

## 六步状态机（SCN28，grow_state 存 R323 起始计数）

| 字段 | R322 起始 | R323 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 322 | 323 |
| type_round | 14 | 15 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 7 | **0**（SCN28 复位）|
| discover_streak_low | 0 | 0（new_candidates=6≥3）|
| rounds_since_last_corpus_discover | 258 | 259 |
| last_updated_round | 322 | 323 |

## 遗留问题

1. **queue(character) 0→6**（建序 63–68 补给）。registry 全库 1551，character 27，unknown 0。
2. **下轮 R323 = NEW1（§3(7)）**：since_evv5=4<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费**建序 63（mary-grant）**。Mary Grant（book In Search of the Castaways，pn_anchor SC-004，role supporting）——Captain Grant 之女、随 Duncan 号寻父；与既建 glenarvan/paganel/ayrton 同书可互链。
3. **后续 R323–R328 预排**：NEW1 依次消费 63–68（mary-grant/john-mangles/mcnabbs/thalcave/nadia/ivan-ogareff），至 **R328 前后 EVV5 复位到期**（since_evv5 于 R318 复位，R328 达 10）——届时 §3(1b) EVV5 反射轮先行。若 EVV5 与消费错位，按决策机首匹配为准。
4. **深池尚存**（第四批储备）：SC（Robert Grant/Captain Grant）、MS（Marfa Strogoff/Feofar-Khan/Harry Blount/Alcide Jolivet）、DSCF（Mrs. Weldon/Cousin Benedict/Tom）、单作品主角（Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz/Nicholl/Hans）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）；（e）character-vs-work 同名 label 张力（R321 michel/michael 就源裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=258→259（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
