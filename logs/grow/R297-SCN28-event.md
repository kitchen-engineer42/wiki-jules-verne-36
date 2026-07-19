---
round: 297
date: 2026-07-19
type_round: 63
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R297 · SCN28-zombie · event — 续掘单事件作品第二事件第三批，采 WAI/TN/PL 三部离散终局，掘建序 46-48

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 63）。R293 discover 队列建序 43-45 已于 R294/295/296 全消费，**queue(event)==0**。决策机 §3 首匹配 **SCN28-zombie**
（since_evv5=8<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=3<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**）。

**续「单事件作品掘第二事件」策略（第三批）**：语料零事件作品池 R275 已竭；本策略从单事件作品掘其离散第二事件。已建十五部第二 event（RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/RM/EHLA/AM/TT/ASC/WC）。
本轮 re-scan 余单事件作品，按首事件 pn_anchor 反查各作离散climax章，采 **WAI/TN/PL** 三部之终局或起义高潮，掘 3 候选建序 46-48。

**饱和排除（本批新增判定）**：
- **BR（Blockade Runners，10c）饱和**：首事件 charleston-blockade-run 已引 BR-001/006/007/**009**——BR 两大climax（BR-006 闯入 Charleston + BR-009「Between Two Fires」逃逸救 Halliburtt）皆入首事件，无余离散事件。**剔**。
- **DOSE（Doctor Ox's Experiment，17c）饱和**：首事件 quiquendone-frenzy 已引 DOSE-013/014/015/**016/017**——DOSE 终局（爆炸令城复常 + Doctor Ox 纯氧致狂之揭秘）皆入首事件。**剔**。
- **MZ（Master Zacharius，5c）**：首事件 death-of-master-zacharius 锚 MZ-005（终章），仅 5 章、全弧趋 Zacharius 之死；早段（钟停）候补，本批不采。
- **GM（Mistress Branican，22c）overlap-watch**：首事件 wreck-of-the-dream 引 GM-007/008 + **GM-022-022**（终章单句），掘 GM 终局第二事件恐与 022 重叠，留察。
- **DA（单章短篇）**：不可掘第二事件（永久排除）。
- **SI/MI**：destruction-of-lincoln-island（book SI，HK 待归一 MI）实为 MI 第四 event，MI 非单事件作品，剔。

**逐句核实（framing 视为线索、逐章复核）**：
- **建序 46 return-of-the-jeune-hardie（WAI-016）**：核 WAI-016 终局章——Vasling 叛变被平（Herming/Vasling/Aupic/Jocki 死，WAI-016-004），Louis 之父 Jean Cornbutte 忧劳而殁、葬冰岸立木十字（WAI-016-003/006），柠檬治愈坏血病（WAI-016-007），春归 Louis 别父墓启程（WAI-016-020），Jeune-Hardie 号破冰出极海（WAI-016-021），8 月 16 日返 Dunkirk 众迎、老神父为二亡魂与 Louis/Marie 婚礼诵弥撒（WAI-016-022）。与既有 finding-of-louis-cornbutte（WAI-012 寻获 Louis）PN 区段不重叠、分工明确（寻获 vs 终局返航）。
- **建序 47 return-of-ole-kamp（TN-020）**：核 TN-020 终局章「Yes; it was Ole Kamp!」——Viking 号沉船生还之 Ole Kamp 奇迹归 Christiania（TN-020-001），全城知其归来兼中头奖（TN-020-003），与未婚妻 Hulda 重逢（TN-020-005），Sylvius Hogg 揭其自 Christiansand 之丹麦双桅 Genius 号获救、并请守密（TN-020-007/008），定当晚赴 Dal 成婚（TN-020-006）。与既有 christiania-lottery-drawing（TN-019 彩票开奖）PN 区段不重叠、分工明确（开奖 vs 终局归来）。
- **建序 48 lima-indian-uprising（PL-008）**：核 PL-008「CONQUERORS AND CONQUERED」——Lima 印第安/zambo/chino 潜聚富人区（PL-008-003），首领 Sambo 现身斥西班牙压迫者当诛（PL-008-008/009），约定五时大教堂钟鸣、山间警钟为复仇号令（PL-008-011），赴 chingana 会起义首领（PL-008-012），五时钟响警钟雷动、全城印第安持械怒起（PL-008-014/015）。与既有 death-of-martin-paz（PL-009 Madeira 瀑布殉死）PN 区段不重叠、分工明确（起义 vs 终局殉死；起义结局 PL-008 后段/PL-009 前段建时慎防与 death 重叠）。

**VVV 宽度**：WAI 3-char、TN/PL 2-char——均为正常宽度，无需 RFC-0003 Note（Note 仅限 4-char 且 PN 断行者）。

**dup-check（filesystem + registry sweep）**：三 exact-slug + 全变体 filesystem ABSENT；work 页 aliases sweep（a-winter-amid-the-ice / ticket-no-9672 / the-pearl-of-lima）无 label/alias 冲突。链目标 work 页均存在（[[A Winter Amid the Ice]]、[[Ticket No. 9672]]、[[The Pearl of Lima]]）。

new_candidates=3 ≥ type_close_new_candidate_min(3) → **productive**，discover_streak_low 保持 0。queue(event) 0→3。本轮不建页，registry 不变（total 1534，event 59，unknown 0）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)==0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

（discover 轮，不建页；掘 3 候选入 queue）

| 建序 | slug | pn_anchor | 作品(VVV) | 事件焦点 | 与首事件分工 |
|------|------|-----------|-----------|----------|-------------|
| 46 | return-of-the-jeune-hardie | WAI-016 | A Winter Amid the Ice(WAI,3c) | 越冬之末 Jean Cornbutte 死、叛平、春归返 Dunkirk 成婚 | vs finding-of-louis-cornbutte(寻获) |
| 47 | return-of-ole-kamp | TN-020 | Ticket No. 9672(TN,2c) | Ole Kamp 生还归 Christiania 与 Hulda 重逢 | vs christiania-lottery-drawing(开奖) |
| 48 | lima-indian-uprising | PL-008 | The Pearl of Lima(PL,2c) | Sambo 领 Lima 印第安起义、钟响怒起 | vs death-of-martin-paz(终局殉死) |

## EXIT-GATE 检查

- **G4 脚本建页**：本轮 discover 不建页，无 pages/** 写入。✔
- **registry 一致**：不建页，total 1534 event 59 unknown 0 不变。✔
- **查重充分**：三 exact-slug + 全变体 filesystem ABSENT；work 页 aliases sweep 无冲突。✔
- **framing 核实**：三候选章逐句核（WAI-016 越冬之末 / TN-020 Ole 归来 / PL-008 起义），均与首事件 PN 区段不重叠；BR/DOSE 饱和判定引用首事件 PN 已核。✔
- **new_candidates≥min**：3≥3，productive，streak 保持 0。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie，grow_state 存 R298 起始计数）

| 字段 | R297 起始 | R298 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 297 | 298 |
| type_round | 63 | 64 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 233 | 234 |
| last_updated_round | 297 | 298 |

## 遗留问题

1. **queue(event) 0→3**：本轮掘建序 46-48。registry 全库 **1534**，unknown 0（不建页）。
2. **下轮 R298 = NEW1（§3(7)）**：since_evv5=9<10 → §3(1) 否；streak=0<3；since_discover=0<10 且全局 queue≥10 → §3(3) 否；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 46 return-of-the-jeune-hardie（WAI，anchor WAI-016）**。WAI 3-char 无需 Note；逐句核 WAI-016 叛平-父殁-春归-返航-成婚序列、剔 finding-of-louis-cornbutte 寻获别线。
3. **EVV5 逼近**：since_evv5 R298 起 9，R299 达 10 → R299 触发 §3(1b) EVV5（event 类型全库抽检 + 模板校准 + PN 回填债评审）。
4. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。三候选建时须逐句复核。教训延续（R283 改锚 / R286 改锚+改 slug）。
5. **event 覆盖策略·余矿**：单事件作品第二事件矿脉，已采十五部 + 本批 WAI/TN/PL 三部（建后共十八部）。**BR/DOSE 已判饱和**（两climax 皆入首事件，剔）。余可掘薄：MZ 早段（钟停）候补、GM(overlap-watch) 留察；DA 排除、SI/MI 非单事件。event 二次矿将近竭，type_close 判据渐近（连续 discover new_candidates<3 三轮则 CLOSE+SCN28 切 character）。
6. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
7. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解。
8. **散文门债**：37 页 >400（既有 DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=233→234（dead 变量）。
10. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
11. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
