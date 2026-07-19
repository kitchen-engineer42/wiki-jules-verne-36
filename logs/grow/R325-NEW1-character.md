---
round: 325
date: 2026-07-19
type_round: 18
phase: "2.1"
current_type: character
gene: NEW1
pages: [mcnabbs]
result: success
---

# GROW 2.1-B · R325 · NEW1 · character — 建 Major McNabbs（Glenarvan 之表兄、沉稳少校）

## 执行摘要

Phase 2.1-B character 第 15 建（type_round 18），消费 R322 第三批 discover 队列**建序 65**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Major McNabbs**（*In Search of the Castaways*）——[[Lord Glenarvan]] 之表兄、随 *Duncan* 号自始至终之少校（SC-001-002/005-011）。其静定为其标记：陌客之激动与「the Major's placidity」成强对照（SC-006-034），他人必哂之景，「McNabbs never moved a muscle of his face」（SC-006-036）；观洪泛「with the utmost indifference」（SC-008-036）；进言干燥若其性——「'I should wait,' said the Major, just as if he had said, 'I should not wait'」（SC-008-063）；言隙常「absorbed in his cigar」（SC-006-030）。然其眼锐利务实：他人百过而不觉之小屋，独 McNabbs 识为庇所（SC-013-001）；沉稳猎手，答问仅「By this」而举其所猎（SC-013-040）。Paganel 数其为天然首领之一「who would not yield his place to anybody」（SC-010-049）。待 [[Paganel]] 虽表冷而实亲（SC-014-006）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-001、affiliation 空、aliases 空。

**12 distinct solid PN**（SC-001-002/004-015/005-011/006-030/006-034/006-036/008-036/008-063/010-049/013-001/013-040/014-006）：均 solid，逾门。

**查重**：exact-slug mcnabbs filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Lord Glenarvan]]（R320）、[[Paganel]]（R313）、[[Mary Grant]]（R323）、[[In Search of the Castaways]]（work）——四链均存在无悬挂。SC 簇成大群（glenarvan/paganel/ayrton/mary-grant/john-mangles/mcnabbs 六页互链）。

prose-gate：add_page 初稿 0 超段。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未剥离）。

character 计数 29→**30**，registry total 1553→**1554**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4>0、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费建序 65。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| mcnabbs | cYQikr | In Search of the Castaways | supporting | SC-001 | 12 distinct | 表兄少校-静定-锐眼-猎手单指；SC 2-char 无 Note；strict 首过 ✓；[[Lord Glenarvan]]/[[Paganel]]/[[Mary Grant]]/work 互链 |

- **mcnabbs**：12 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev cYQikr。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 McNabbs 静定-锐眼-猎手因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1554 character 30 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Lord Glenarvan/Paganel/Mary Grant/In Search of the Castaways 四链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R326 起始计数）

| 字段 | R325 起始 | R326 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 325 | 326 |
| type_round | 17 | 18 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 261 | 262 |
| last_updated_round | 325 | 326 |

## 遗留问题

1. **character 页数 30**：本轮 +1（mcnabbs）。queue(character) 4→**3**（建序 65 消费；余 66-68：thalcave/nadia/ivan-ogareff）。registry 全库 **1554**，unknown 0。
2. **下轮 R326 = NEW1（§3(7)）**：since_evv5=7<10；queue(character)=3>0 → §3(7) NEW1，消费建序 66（thalcave）。Thalcave（book In Search of the Castaways，pn_anchor SC-015，role supporting，SC 2-char 无 Note）——Patagonia 印第安向导、pampas 领路，137 mentions；与既建 glenarvan（SC-018-042 已引 Thalcave）等同书可互链。
3. **SC 簇成大群**：六页互链；建序 66（Thalcave）建成后 SC 达七页。
4. **EVV5 下次约 R328**（since_evv5 于 R318 复位，+10）：R326 起 since_evv5=7，R327→8，R328→9，R329 达 10——**EVV5 反射轮预计落 R329**（消费建序 68 后）。届时 §3(1b) EVV5 优先。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=261→262（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
