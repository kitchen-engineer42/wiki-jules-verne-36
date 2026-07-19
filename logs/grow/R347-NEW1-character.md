---
round: 347
date: 2026-07-19
type_round: 39
phase: "2.1"
current_type: character
gene: NEW1
pages: [palmyrin-rosette]
result: success
---

# GROW 2.1-B · R347 · NEW1 · character — 建 Palmyrin Rosette（Gallia 上古怪天文学家；OC 簇扩；第六批建序 82）

## 执行摘要

Phase 2.1-B character 第 32 建（type_round 39），消费 R345 第六批 discover 队列**建序 82**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=7>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=6。**

**Palmyrin Rosette**（*Off on a Comet*）——随彗星 Gallia 遨游太空之天文学家、Servadac 之旧日塾师。重逢时被认作「my old tutor, Mr. Rosette, in very flesh and blood」（OC-027-014）；Servadac 告众「although the professor was always eccentric, and at times very irascible, yet he was real[ly]」有真才（OC-027-020），其孤僻更见于履历——名曾被逐出官方委员会「apparently for no other reason than his personal unpopularity」（OC-029-018）。全船唯其解此漫游之星：不满「with three positions」而「made ten, twenty, thirty observations」（OC-029-029），由此「able to calculate the date at which the comet would reach its perihelion」，喜不自胜（OC-029-037）。视 Gallia 为己有——「the diameter, the surface, the volume of my comet are settled」（OC-030-076），其学皆出自冰中一穴，「projected the case of an astronomer's telescope; it was the opening of Palmyrin Rosette's observatory」（OC-031-036）。其性乃专注学究之漫画像：疾怒而好训人，呼喊「with all the petulant impatience of the old pedagogue」（OC-030-033），受挫则「scratched his head in perplexity, glaring round upon his companions as if they were personally responsible」（OC-032-045）。痴迷使其成天穹隐者——「irremovable from his observatory」（OC-034-025），静夜「cared so little to quit his observatory」（OC-034-003）；Servadac 念其「dislike to visitors」（OC-037-018）遂由其独处，然其狂喜真切，「rejoicing in an approach nearer to Jupiter than any other mortal」（OC-036-008）。

**role=supporting**。book=Off on a Comet、first_appearance=OC-027、affiliation 空、**label=Palmyrin Rosette，aliases=['Professor Rosette']**。

**13 distinct solid PN**（OC-027-014/020、029-018/029/037、030-033/076、031-036、032-045、034-003/025、036-008、037-018）：均 solid，逾门。

**查重**：exact-slug palmyrin-rosette filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**OC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（OC 簇扩）**：[[Hector Servadac]]（character，存）+ [[Off on a Comet]]（work，存）——互链无悬挂，OC 簇 hector-servadac/ben-zoof/palmyrin-rosette 三页成型。⚠ 与 ben-zoof 同：[[Hector Servadac]] label 与 off-on-a-comet work alias 'Hector Servadac' 冲突（HK(e) parked，warn-only，character 页优先解析，页内链无歧义）。

prose-gate：add_page 初稿 2 超段（557、458），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 46→**47**，registry total 1570→**1571**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=7、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =7>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=7>0，按既有实践走 NEW1 消费建序 82。消费后 queue=6。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| palmyrin-rosette | uSFUe3 | Off on a Comet | supporting | OC-027 | 13 distinct | Gallia 天文学家-Servadac 旧塾师-彗星轨道推算者-观测台隐者；label Palmyrin Rosette + alias Professor Rosette；OC 2-char 无 Note；拆 2 超段；strict 首验通过；互链 [[Hector Servadac]]/[[Off on a Comet]] |

- **palmyrin-rosette**：13 distinct solid PN；alias ['Professor Rosette']；character-schema 五 H2。add_page rev uSFUe3。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Rosette 塾师-孤僻-推算-隐者因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；OC 2-char 无 Note。✔
- **registry 一致**：total 1571 character 47 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Palmyrin Rosette 唯一）。✔
- **wikilink 完整性**：Hector Servadac/Off on a Comet 链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R348 起始计数）

| 字段 | R347 起始 | R348 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 347 | 348 |
| type_round | 39 | 40 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 283 | 284 |
| last_updated_round | 347 | 348 |

## 遗留问题

1. **character 页数 47**：本轮 +1（palmyrin-rosette）。queue(character) 7→**6**（建序 82 消费）。registry 全库 **1571**，unknown 0。
2. **下轮 R348 = NEW1（§3(7)）**：since_evv5=7<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 83（dirk-peters）。Dirk Peters（book An Antarctic Mystery，pn_anchor AM-004，role supporting，AM 2-char 无 Note）——Poe Pym 传奇混血水手；AM 簇配对 len-guy。
3. **OC 簇成型**：hector-servadac + ben-zoof + palmyrin-rosette + off-on-a-comet(work)，四页齐。
4. **下次 EVV5 预判**：since_evv5 上次归零 R340，R350 起始达 10 → EVV5 约 R350 触发（届时 queue 尚余候选，1b 优先于 NEW1，暂停一轮 NEW1）。R348-R349 续 NEW1（dirk-peters/william-guy），R350 EVV5。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked（本轮 palmyrin-rosette 亦触 warn-only，无阻塞）。
6. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、captain-grant→Robert。
7. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
8. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
9. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
10. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
11. **corpus-discover 顺延**：since_corpus=283→284（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
