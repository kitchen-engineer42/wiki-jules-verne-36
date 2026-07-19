---
round: 352
date: 2026-07-19
type_round: 44
phase: "2.1"
current_type: character
gene: NEW1
pages: [nell]
result: success
---

# GROW 2.1-B · R352 · NEW1 · character — 建 Nell（New Aberfoyle 地下城之孤女、Silfax 之孙女；UC 簇配对；第六批建序 86）

## 执行摘要

Phase 2.1-B character 第 36 建（type_round 44），消费 R345 第六批 discover 队列**建序 86**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。**

**Nell**（*The Underground City*）——New Aberfoyle 深处诞生之神秘少女、老 Silfax 之孙女、Harry Ford 之妻。初见不谙言语——「uttered these few words like one unused to speak much」（UC-012-010）；身世乃全书之秘，终自陈「I am the granddaughter of old Silfax」「I never knew a mother till the day I came here」（UC-017-027）。入 Ford 家「had become a most intelligent and zealous assistant to old Madge」（UC-012-034），得救后「became a fashionable wonder without knowing it」（UC-012-022），然「some secret existed in connection with the place, which she could have explained」（UC-012-028）。其实乃暗中守护困于矿中之探险者——Harry 揭「those men were James Starr, my father, and myself, Nell!」（UC-012-076），彼时众「at the point of death... but for a kind and charitable being--an angel perhaps」（UC-012-074）。终指认施害之祖：「as soon as my grandfather saw that you were fairly inside the gallery leading to New Aberfoyle, he stopped up the」隘（UC-017-033），警「my grandfather is everywhere and nowhere」（UC-017-038）；故事结于婚坛，牧师问「Harry, will you take Nell to be your wife」（UC-018-015）。生于暗，目不耐昼——「this imperfect light suited Nell, to whose eyes a glare was very unpleasant」（UC-012-049），言「darkness is beautiful as well as light」（UC-012-057）；怯中含重然诺，「for me indeed it is well, whatever may happen」「for others--who can tell?」（UC-012-069）。婚事关乎其安——「malevolence would be disarmed」惟「she was his wife」（UC-016-052）。

**role=supporting**。book=The Underground City、first_appearance=UC-012、affiliation 空、**label=Nell，aliases=[]**。

**14 distinct solid PN**（UC-012-010/022/028/034/049/057/069/074/076、016-052、017-027/033/038、018-015）：均 solid，逾门。

**查重**：exact-slug nell filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**UC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（UC 簇配对）**：[[James Starr]]（character，存，R351 建）+ [[The Underground City]]（work，存）——互链无悬挂，UC 簇 james-starr/nell 配对成型。Harry Ford / Silfax（未建）暂纯文本（DEFERRED）。可回填 james-starr 页 Nell 纯文本为 [[Nell]]。

prose-gate：add_page 初稿 2 超段（415、423），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 50→**51**，registry total 1574→**1575**，unknown 恒 0。build_registry 仅 Robur the Conqueror 一 alias warn（本轮 Hector Servadac warn 未列出，实仍 parked）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=6 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费建序 86。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| nell | wfApsV | The Underground City | supporting | UC-012 | 14 distinct | 地下城孤女-Silfax 孙女-暗中守护者-Harry 之妻；label Nell + aliases 空；UC 2-char 无 Note；拆 2 超段；strict 首验通过；互链 [[James Starr]]/[[The Underground City]] |

- **nell**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev wfApsV。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Nell 身世-守护-指认-婚事-目盲-然诺因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；UC 2-char 无 Note。✔
- **registry 一致**：total 1575 character 51 unknown 0；Robur alias warn（Hector Servadac 仍 parked）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Nell 唯一）。✔
- **wikilink 完整性**：James Starr/The Underground City 链存在无悬挂；Harry Ford/Silfax 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R353 起始计数）

| 字段 | R352 起始 | R353 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 352 | 353 |
| type_round | 44 | 45 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 288 | 289 |
| last_updated_round | 352 | 353 |

## 遗留问题

1. **character 页数 51**：本轮 +1（nell）。queue(character) 3→**2**（建序 86 消费）。registry 全库 **1575**，unknown 0。
2. **下轮 R353 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 87（claudius-bombarnac）。Claudius Bombarnac（book The Adventures of a Special Correspondent，pn_anchor ASC-001，role narrator，ASC 2-char 无 Note）——跨里海铁道之记者叙者；建后启 ASC 簇。
3. **UC 簇配对成型**：james-starr + nell + the-underground-city(work)。Simon Ford / Harry Ford / Silfax / Jack Ryan 可续为 UC 候选。
4. **AM 簇三主角齐**：len-guy + dirk-peters + william-guy + an-antarctic-mystery(work)。Arthur Pym 深池候选。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
6. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、captain-grant→Robert。
7. **第六批消费预判**：R353-R354 建 claudius-bombarnac/erik（建序 87-88），R355 queue 归 0 → 第七批 discover。下次 EVV5 于 R360 起始达门。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=288→289（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
