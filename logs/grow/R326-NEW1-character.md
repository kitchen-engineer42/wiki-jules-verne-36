---
round: 326
date: 2026-07-19
type_round: 19
phase: "2.1"
current_type: character
gene: NEW1
pages: [thalcave]
result: success
---

# GROW 2.1-B · R326 · NEW1 · character — 建 Thalcave（Patagonia 印第安向导）

## 执行摘要

Phase 2.1-B character 第 16 建（type_round 19），消费 R322 第三批 discover 队列**建序 66**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Thalcave**（*In Search of the Castaways*）——领 Glenarvan 一行越 pampas 之 Patagonia 向导，「a practised guide, and one of the most intelligent of his class」（SC-015-059），身量伟岸，同侪须「make great strides to keep up with the giant Thalcave」（SC-015-060），且为「a consummate horseman」（SC-016-003）。其领路穿无水之乡，先行「to beat the bushes and frighten away the cholinas」毒蛇（SC-017-002），掷 bolas 擒 nandou 以给养队伍（SC-018-078）。其识定全搜之向——Glenarvan 曰「Thalcave has set us on the track... I have great confidence in him」（SC-018-042），且「would not leave his companions behind, alone in the midst of a desert」（SC-018-056）。其人以缄默为标记：既悟身为向导反被导，「with true Indian reserve, he maintained absolute silence」（SC-016-017）；临难无惧，思「to despair if the Guamini should be dried up--if, indeed, the heart of an Indian can ever despair」（SC-018-054）；甚其渴亦克之，「drinking very quietly, without hurrying himself, taking small gulps」（SC-018-067）。待 [[Paganel]] 为其传译（SC-016-061），勉幼者 Robert Grant 之勇（SC-018-027），与爱马 Thaouka 相语相得（SC-018-057）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-015、affiliation 空、aliases 空。

**13 distinct solid PN**（SC-015-059/060、016-003/017/061、017-002、018-027/042/054/056/057/067/078）：均 solid，逾门。

**查重**：exact-slug thalcave filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Lord Glenarvan]]（R320）、[[Paganel]]（R313）、[[In Search of the Castaways]]（work）——三链均存在无悬挂。Robert Grant、Thaouka 纯文本。SC 簇达七页（glenarvan/paganel/ayrton/mary-grant/john-mangles/mcnabbs/thalcave 互链）。

prose-gate：add_page 初稿 0 超段。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未剥离）。

character 计数 30→**31**，registry total 1554→**1555**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3>0、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费建序 66。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| thalcave | NsbLUN | In Search of the Castaways | supporting | SC-015 | 13 distinct | 向导-伟岸-缄默-给养单指；SC 2-char 无 Note；strict 首过 ✓；[[Lord Glenarvan]]/[[Paganel]]/work 互链 |

- **thalcave**：13 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev NsbLUN。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Thalcave 向导-缄默-给养因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1555 character 31 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Lord Glenarvan/Paganel/In Search of the Castaways 三链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R327 起始计数）

| 字段 | R326 起始 | R327 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 326 | 327 |
| type_round | 18 | 19 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 262 | 263 |
| last_updated_round | 326 | 327 |

## 遗留问题

1. **character 页数 31**：本轮 +1（thalcave）。queue(character) 3→**2**（建序 66 消费；余 67-68：nadia/ivan-ogareff）。registry 全库 **1555**，unknown 0。
2. **下轮 R327 = NEW1（§3(7)）**：since_evv5=8<10；queue(character)=2>0 → §3(7) NEW1，消费建序 67（nadia）。Nadia（book Michael Strogoff，pn_anchor MS-008，role supporting，MS 2-char 无 Note）——流放者之女、伴 Strogoff 越西伯利亚（伪作其妹）；与既建 michel-strogoff（MS-029-005 已引 Nadia）/michael-strogoff 可互链。
3. **SC 簇达七页**：glenarvan/paganel/ayrton/mary-grant/john-mangles/mcnabbs/thalcave 互链成最大群。
4. **EVV5 下次约 R329**（since_evv5 于 R318 复位，+10）：R327 起 since_evv5=8，R328→9，R329 达 10——**EVV5 反射轮预计落 R329**（消费建序 68 后）。届时 §3(1b) EVV5 优先。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=262→263（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
