---
round: 344
date: 2026-07-19
type_round: 36
phase: "2.1"
current_type: character
gene: NEW1
pages: [len-guy]
result: success
---

# GROW 2.1-B · R344 · NEW1 · character — 建 Len Guy（Halbrane 号船长、寻兄 William Guy 之南极远征领队；AM 新簇种子；第五批建序 80，收官）

## 执行摘要

Phase 2.1-B character 第 30 建（type_round 36），消费 R337 第五批 discover 队列**建序 80（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0，R345 触发第六批 SCN28-zombie discover。**

**Len Guy**（*An Antarctic Mystery*）——纵帆船 _Halbrane_ 之船长。「Captain Len Guy, of Liverpool」，「was three-fifths owner of the vessel, which he had commanded for nearly six years」（AM-002-002）；其名与其船相系，客栈主 Atkins 断言若 _Halbrane_ 不至「it is because there is no longer a Captain Len Guy」（AM-001-037）。其人难以接近——叙者 Jeorling 求搭船，决意「to address myself personally to Len Guy, hard to get at though he might be」（AM-002-053），席间见其缄默寡言（AM-007-007）。启其沉默者乃 Poe 传奇中一名——「the _Jane_ ... and Captain Len Guy had now uttered it for the first time」（AM-004-072）。

谜底系于血亲：「her captain, Len Guy, is William Guy's own brother」（AM-007-074），_Halbrane_ 南航以救沉船 _Jane_ 之幸存者。冻尸之前他崩溃——「Captain Len Guy lifted up the hair ... and finally said with a sort of sob」（AM-006-038）——终得兄弟重逢，告 William 其寻踪之由时「William Guy hid his face in his hands and wept」（AM-024-035）。其人肃穆孤峭、为悲所刻，Jeorling「struck by the sadness of his eyes, which were as black as ink」（AM-003-008），一句探问「Captain Len Guy?」（AM-001-035）亦守其意甚密。然缄默之下有不摧之决心，Jeorling「convinced that the hour would come when Len Guy would again speak to me of his brother, and of the efforts which he intended to make to save him」（AM-007-007）——南冰之险无阻其誓，兄弟终「succeeded with great difficulty in taking an approximate observation」（AM-025-021）。

**role=protagonist**。book=An Antarctic Mystery、first_appearance=AM-001、affiliation 空、**label=Len Guy，aliases=['Captain Len Guy']**。

**13 distinct solid PN**（AM-001-035/037、002-002/053、003-008、004-019/072、006-038/053、007-007/074、024-035、025-021）：均 solid，逾门。

**查重**：exact-slug len-guy + captain-len-guy filesystem + registry entity 全 ABSENT。

**AM 2-char VVV**：无需 RFC-0003 Note。

**wikilink（AM 新簇种子）**：[[An Antarctic Mystery]]（work，存）——互链无悬挂。William Guy（未建，深池候选）、Jeorling（叙者，未建）暂纯文本，待建后回填（DEFERRED）。

prose-gate：add_page 初稿 1 超段（579）+ 1 临界（402），各插空行拆一刀后 0 超门；edit_page（修 Jeorling 引注）再触 William Guy bullet 403 → 删「whole」减一字降至门内。**引注**：add_page 初验 Jeorling bullet AM-002-053 重叠 0%（该 PN 属 Role 段「address myself personally to Len Guy」正引，bullet 语义为「grudgingly takes aboard」不匹配）；改引 **AM-004-019**「decided in the end to offer you a passage on the _Halbrane_」后 strict 通过。distinct 12→**13**（AM-004-019 新增，AM-002-053 仍存于 Role 段）。quality featured 未剥离。

character 计数 44→**45**，registry total 1568→**1569**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=6 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=1>0，按既有实践走 NEW1 消费建序 80（末位）。消费后 queue=0 → R345 第六批 discover。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| len-guy | QEb4bz | An Antarctic Mystery | protagonist | AM-001 | 13 distinct | Halbrane 船长-寻兄 William Guy-Poe/Jane 之谜-南极远征领队；label Len Guy + alias Captain Len Guy；AM 2-char 无 Note；拆 2 超段 + 修 bullet；Jeorling 引注 AM-002-053→AM-004-019 后 strict 通过；[[An Antarctic Mystery]] 互链 |

- **len-guy**：13 distinct solid PN；alias ['Captain Len Guy']；character-schema 五 H2。add_page rev rHbxXl → edit_page rev QEb4bz。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Len Guy 缄默-血亲-决心-重逢因果；strict ✓（Jeorling bullet 改 AM-004-019 消 0% 重叠）。✔
- **G2 段落 ≤400 字**：拆段 + 修 bullet 后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建改页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；AM 2-char 无 Note。✔
- **registry 一致**：total 1569 character 45 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug（含 captain-len-guy 变体）+ entity ABSENT；registry 无 character 冲突（label Len Guy 唯一）。✔
- **wikilink 完整性**：An Antarctic Mystery 链存在无悬挂；William Guy/Jeorling 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R345 起始计数）

| 字段 | R344 起始 | R345 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 344 | 345 |
| type_round | 36 | 37 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 280 | 281 |
| last_updated_round | 344 | 345 |

## 遗留问题

1. **character 页数 45**：本轮 +1（len-guy）。queue(character) 1→**0**（建序 80 末位消费，第五批收官）。registry 全库 **1569**，unknown 0。
2. **下轮 R345 = SCN28-zombie 第六批 discover（§3(4)）**：queue(character)==0 触发。补充 ≥3 grounded + dup-checked 候选。深池余续（R337/R343 记，均本 36 部合集内，建前须 filesystem dup-check 复验）：claudius-bombarnac(ASC)/erik(WC)/james-starr(UC)/nell(UC)/paulina-barnett(FC)/palmyrin-rosette(OC)/dirk-peters(AM)/William Guy(AM)。pages:[]，仅 G4，since_discover 归 0。
3. **AM 簇种子**：len-guy + an-antarctic-mystery(work)。深池 dirk-peters(AM)/William Guy(AM) 可续为 AM 簇配对。
4. **William Guy / Jeorling 回链回填**：本页二者纯文本，待建后 edit_page 回填（DEFERRED，非阻塞）。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。EVV6/HK 批处理裁决。
6. **下次 EVV5 预判**：since_evv5 上次归零于 R340，R350 起始达 10 → EVV5 约 R350 触发。
7. **hector-servadac→Ben Zoof / lieutenant-hobson→Barnett/Long / thomas-roch→Simon Hart/Ker Karraje / captain-grant→Robert 回链回填**：DEFERRED。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（R321 裁例，R339 具化）。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=280→281（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
