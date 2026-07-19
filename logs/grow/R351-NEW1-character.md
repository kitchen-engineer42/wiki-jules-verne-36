---
round: 351
date: 2026-07-19
type_round: 43
phase: "2.1"
current_type: character
gene: NEW1
pages: [james-starr]
result: success
---

# GROW 2.1-B · R351 · NEW1 · character — 建 James Starr（Aberfoyle 退休工程师、New Aberfoyle 地下城之领；UC 开簇；第六批建序 85）

## 执行摘要

Phase 2.1-B character 第 35 建（type_round 43），消费 R345 第六批 discover 队列**建序 85**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=3。** R350 EVV5 复位后首建。

**James Starr**（*The Underground City*）——Aberfoyle 煤矿退休工程师、New Aberfoyle 地下城之发现者与首领。「had for twenty years, been the manager」（UC-001-006）。全书启于召还之信：「IF Mr. James Starr will come to-morrow to the Aberfoyle coal-mines, Dochart pit, Yarrow shaft, a communication of an interesting nature will be made to him」（UC-001-002），信「by the first post, on the 3rd December」达（UC-001-005）。其曾主持闭矿——「had collected the hundreds of workmen which composed the active and courageous population of the mine」（UC-001-011），举末煤宣「is like the last drop of blood which has flowed through the veins of the mine!」（UC-001-015）。得 Simon Ford 召信与匿名警告相抵，「thought it wiser to give more credence to the first letter than to the second」（UC-002-004）遂赴矿。工程师本能系于气：「What troubled James Starr was, not lest too much gas mingled with the air, but lest there should be little or none」（UC-006-042）；然遭隐敌封路，「James Starr and his companions were prisoners in New Aberfoyle」（UC-008-064）。新矿开则居其中——「a second habitation was erected in the neighborhood of Simon Ford's cottage: this was for James Starr」（UC-010-007），警治其城「any stranger entering the mine was brought before James Starr, that he might give an account of himself」（UC-018-002）。其人硕健博学：退休时「with the absolute conviction」矿已无脉（UC-002-017），重逢旧监「glad to find the old man just as he used to be」（UC-004-018），好奇不息「could not rest till he had penetrated this mystery」（UC-012-043）。

**role=protagonist**。book=The Underground City、first_appearance=UC-001、affiliation 空、**label=James Starr，aliases=['Mr Starr']**。

**15 distinct solid PN**（UC-001-002/005/006/011/015/019、002-004/017、004-018、006-042、008-064、010-007、012-043、015-009、018-002）：均 solid，逾门（超目标 13，留余）。

**查重**：exact-slug james-starr filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**UC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（UC 开簇）**：[[The Underground City]]（work，存）——互链无悬挂。Simon Ford / Nell（建序 86，未建）暂纯文本，待 nell 建后回填（DEFERRED）。UC 簇本轮开簇，james-starr + the-underground-city(work) 两页起步。

prose-gate：add_page 初稿 0 超段（起草即控段 ≤400），无需拆段。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 49→**50**，registry total 1573→**1574**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R350 复位）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4、since_discover=5 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费建序 85。消费后 queue=3。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| james-starr | MVyF4s | The Underground City | protagonist | UC-001 | 15 distinct | Aberfoyle 退休工程师-召还之信-New Aberfoyle 发现者-地下城之首；label James Starr + alias Mr Starr；UC 2-char 无 Note；0 超段；strict 首验通过；互链 [[The Underground City]] |

- **james-starr**：15 distinct solid PN；alias ['Mr Starr']；character-schema 五 H2。add_page rev MVyF4s。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Starr 工程师-召还-发现-被困-领城-性格因果；strict ✓。✔
- **G2 段落 ≤400 字**：起草即 0 超门，无需拆段。✔
- **G3 ≥5 distinct PN**：15 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；UC 2-char 无 Note。✔
- **registry 一致**：total 1574 character 50 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label James Starr 唯一；alias Mr Starr 唯一）。✔
- **wikilink 完整性**：The Underground City 链存在无悬挂；Simon Ford/Nell 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R352 起始计数）

| 字段 | R351 起始 | R352 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 351 | 352 |
| type_round | 43 | 44 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 287 | 288 |
| last_updated_round | 351 | 352 |

## 遗留问题

1. **character 页数 50**：本轮 +1（james-starr）。queue(character) 4→**3**（建序 85 消费）。registry 全库 **1574**，unknown 0。
2. **下轮 R352 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 86（nell）。Nell（book The Underground City，pn_anchor UC-012，role supporting，UC 2-char 无 Note）——地下城之孤女；建后 UC 簇配对成型，可回填 james-starr 页 Nell 纯文本为 [[Nell]]。
3. **UC 开簇**：james-starr + the-underground-city(work) 两页起步；R352 补 nell 后配对成型。Simon Ford / Harry Ford / Jack Ryan 可续为 UC 候选。
4. **AM 簇三主角齐**：len-guy + dirk-peters + william-guy + an-antarctic-mystery(work)。Arthur Pym 深池候选。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
6. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Simon Ford/Nell、captain-grant→Robert。
7. **第六批消费预判**：R352-R354 建 nell/claudius-bombarnac/erik（建序 86-88），R355 queue 归 0 → 第七批 discover。下次 EVV5 于 R360 起始达门。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=287→288（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
