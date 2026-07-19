---
round: 331
date: 2026-07-19
type_round: 24
phase: "2.1"
current_type: character
gene: NEW1
pages: [marfa-strogoff]
result: success
---

# GROW 2.1-B · R331 · NEW1 · character — 建 Marfa Strogoff（认子而佯不识之母）

## 执行摘要

Phase 2.1-B character 第 19 建（type_round 24），消费 R330 第四批 discover 队列**建序 69**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Marfa Strogoff**（*Michael Strogoff*）——Czar 密使之老母，居 Omsk，「old Peter Strogoff, dead ten years since」（MS-004-035）后独守 Strogoff 家宅，「could never be induced to leave the house of the Strogoffs」（MS-004-038）。Michael 化名过 Omsk 时「his mother, the old woman Marfa, was before him!」（MS-015-057）；察其密使身份之险，出声试之「'Thou art not the son of Peter and Marfa Strogoff?'」（MS-015-064），继而公然弃认，然内白「'Do you think that for anything in the world I would deny a son whom God has given me?'」（MS-015-094）。被鞑靼掳去，「Marfa Strogoff, with firm step, followed the Tartar」（MS-015-074）。后于俘中见 Michael，自制如铁「'It is my son... and you see that I do not make a step towards him!'」（MS-022-022），Michael 睹其克制，「Marfa, then, had understood all, and kept his secret」（MS-022-024）。其勇乃母性不折：受鞭「the guards brutally pushed her. She fell」（MS-023-031），而最深之痛为自责，「longed to ask her son's pardon for the harm she had unintentionally done him」（MS-023-017）；至其子受刑之极，立而「her eyes open wide, her arms extended towards where he stood」（MS-024-051），终「his aged mother fell senseless to the ground」（MS-024-052）。落入 Ogareff 之俘，泄「beyond doubt that Marfa Strogoff's son, the Czar's courier」在侧（MS-022-028）。

**role=supporting**。book=Michael Strogoff、first_appearance=MS-004、affiliation 空、aliases 空。

**13 distinct solid PN**（MS-004-035/038、015-057/064/074/094、022-022/024/028、023-017/031、024-051/052）：均 solid，逾门。

**查重**：exact-slug marfa-strogoff filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Michel Strogoff]]（R321）、[[Nadia]]（R327）、[[Ivan Ogareff]]（R328）、[[Michael Strogoff]]（work）——四链均存在无悬挂。MS 簇达五实体互链。

prose-gate：add_page 初稿 1 超段（514），拆段后 0 超门。**引注修正**：strict 首验 MS-023-017 重叠 1.82%<2%（Ogareff bullet 关系散文与源句字面重叠低），改引 MS-022-028（源句含 Marfa Strogoff's son/Czar's courier/Ogareff's prisoners，重叠达标），edit_page rev DLBFyU 后 strict ✓；MS-023-017 仍存于 Character & Traits 节（自责句），distinct PN 净 13。quality featured 未剥离。

character 计数 33→**34**，registry total 1557→**1558**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6>0、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=6>0，按既有实践走 NEW1 消费建序 69。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| marfa-strogoff | DLBFyU | Michael Strogoff | supporting | MS-004 | 13 distinct | 老母-认子佯不识-守密-受刑单指；MS 2-char 无 Note；拆 1 超段；引注 MS-023-017→MS-022-028 修正后 strict ✓；[[Michel Strogoff]]/[[Nadia]]/[[Ivan Ogareff]]/work 互链 |

- **marfa-strogoff**：13 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev x9PFGf→edit_page rev DLBFyU。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Marfa 守密-受刑-自责因果；引注修正后 strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建页改页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1558 character 34 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Michel Strogoff/Nadia/Ivan Ogareff/Michael Strogoff 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R332 起始计数）

| 字段 | R331 起始 | R332 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 331 | 332 |
| type_round | 23 | 24 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 267 | 268 |
| last_updated_round | 331 | 332 |

## 遗留问题

1. **character 页数 34**：本轮 +1（marfa-strogoff）。queue(character) 6→**5**（建序 69 消费；余 70-74：alcide-jolivet/harry-blount/feofar-khan/captain-grant/robert-grant）。registry 全库 **1558**，unknown 0。
2. **下轮 R332 = NEW1（§3(7)）**：since_evv5=2<10；queue(character)=5>0 → §3(7) NEW1，消费建序 70（alcide-jolivet）。Alcide Jolivet（book Michael Strogoff，pn_anchor MS-002，role supporting，MS 2-char 无 Note）——法国记者、诙谐、以「表妹」暗语发报；与 harry-blount/michel-strogoff 可互链。
3. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。
4. **MS 簇达五实体**：michel-strogoff/michael-strogoff/nadia/ivan-ogareff/marfa-strogoff 互链成群；建序 70-72（jolivet/blount/feofar）建成后 MS 达八实体。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=267→268（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
