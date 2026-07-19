---
round: 354
date: 2026-07-19
type_round: 46
phase: "2.1"
current_type: character
gene: NEW1
pages: [erik]
result: success
---

# GROW 2.1-B · R354 · NEW1 · character — 建 Erik（Cynthia 救生圈上寻身世之弃儿主角；WC 开簇；第六批建序 88 末位，消费后 queue 归 0）

## 执行摘要

Phase 2.1-B character 第 38 建（type_round 46），消费 R345 第六批 discover 队列**建序 88（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R355 触 §3(4) SCN28-zombie 第七批 discover。**

**Erik**（*The Waif of the Cynthia*）——挪威 Noroe 渔家养子、天资之弃儿、Cynthia 沉船救生圈上拾得之婴、终认作 Durrien 之外孙。「Erik Hersebom!」（WC-001-026），Schwaryencrona 医生叹「your son, Erik, Master Hersebom, is a most remarkable child」（WC-002-059）。其实乃弃儿——「Erik believed himself to be your son, and that every one in Noroe had forgotten how he had become yours」（WC-002-071）；医生慕其才「Erik is twelve years old, nearly thirteen, and he appears to be highly gifted」（WC-003-036），携赴 Stockholm 就学寻源。谜难解——「Nothing had occurred to throw any light on the mystery which surrounded Erik's origin」（WC-006-030），遍访海港「none of them could give him any useful information about the last voyage of the 'Cynthia'」（WC-008-024）；然心系海而非书斋「I knew that the child would prefer the sea to all their books」（WC-006-017），寻源之志驱其乘 Alaska 北极远航。终以信释谜：「you were picked up at sea about twenty-two years ago by a Norwegian fisherman in the neighborhood of Bergen; that you were tied to a buoy, bearing the name of 'Cynthia'」（WC-021-008），「in that case you are my grandson, for whom I have mourned so many years」（WC-021-009），其归复令「the good, simple-hearted beings who had saved her son's life」深喜（WC-022-002）。谦挹其才——「I am at the command of the doctor," answered Erik, modestly」（WC-001-033），学识精敏「Erik answered without hesitation 'that it was one of the family of umbelliferous plants,' and described them in detail」（WC-001-039），忠而知感「I am too much obliged to you, dear doctor, for having brought me」（WC-004-027）。

**role=protagonist**。book=The Waif of the Cynthia、first_appearance=WC-001、affiliation 空、**label=Erik，aliases=['Erik Hersebom']**。

**13 distinct solid PN**（WC-001-026/033/039、002-059/071、003-036、004-027、006-017/030、008-024、021-008/009、022-002）：均 solid，逾门。

**查重**：exact-slug erik filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**WC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（WC 开簇）**：[[The Waif of the Cynthia]]（work，存）——互链无悬挂。Dr. Schwaryencrona / Mr. Durrien（未建）暂纯文本（DEFERRED）。WC 簇本轮开簇，erik + the-waif-of-the-cynthia(work) 两页起步。

prose-gate：add_page 初稿 2 超段（495、436），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 52→**53**，registry total 1576→**1577**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=8 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=1>0，按既有实践走 NEW1 消费建序 88。**消费后 queue=0 → R355 §3(4) SCN28-zombie discover 触发。**

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| erik | vPShKB | The Waif of the Cynthia | protagonist | WC-001 | 13 distinct | Noroe 渔家养子-Cynthia 救生圈弃儿-Stockholm 寻源-Durrien 外孙；label Erik + alias Erik Hersebom；WC 2-char 无 Note；拆 2 超段；strict 首验通过；互链 [[The Waif of the Cynthia]] |

- **erik**：13 distinct solid PN；alias ['Erik Hersebom']；character-schema 五 H2。add_page rev vPShKB。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Erik 弃儿身世-寻源-释谜-谦才-忠感因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；WC 2-char 无 Note。✔
- **registry 一致**：total 1577 character 53 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Erik 唯一；alias Erik Hersebom 唯一）。✔
- **wikilink 完整性**：The Waif of the Cynthia 链存在无悬挂；Dr. Schwaryencrona/Mr. Durrien 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R355 起始计数）

| 字段 | R354 起始 | R355 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 354 | 355 |
| type_round | 46 | 47 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 8 | 9 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 290 | 291 |
| last_updated_round | 354 | 355 |

## 遗留问题

1. **character 页数 53**：本轮 +1（erik）。queue(character) 1→**0**（建序 88 末位消费）。registry 全库 **1577**，unknown 0。
2. **下轮 R355 = SCN28-zombie discover（§3(4)）**：queue(character)==0 → §3(4) 触发第七批 discover。补 ≥3 grounded + dup-checked 候选（建序 89 起）入 queue.md，pages:[]，仅 G4，since_discover 归零；若新候选<3 则 discover_streak_low+=1。since_evv5=4（EVV5 于 R360 起始达 10）。
3. **WC 开簇**：erik + the-waif-of-the-cynthia(work) 两页起步。Dr. Schwaryencrona / Mr. Durrien / Vanda / Tudor Brown 可续为 WC 候选。
4. **第六批（建序 81-88）全消费完毕**：paulina-barnett/palmyrin-rosette/dirk-peters/william-guy/james-starr/nell/claudius-bombarnac/erik 八页全建。簇成果：FC（+paulina-barnett）、OC（+palmyrin-rosette）、AM 三主角齐（+dirk-peters/william-guy）、UC 开簇配对（james-starr/nell）、ASC 开簇（claudius-bombarnac）、WC 开簇（erik）。
5. **AM 簇三主角齐**：len-guy + dirk-peters + william-guy + an-antarctic-mystery(work)。Arthur Pym 深池候选。
6. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
7. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、captain-grant→Robert。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=290→291（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
