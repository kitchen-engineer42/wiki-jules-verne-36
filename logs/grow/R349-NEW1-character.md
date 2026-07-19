---
round: 349
date: 2026-07-19
type_round: 41
phase: "2.1"
current_type: character
gene: NEW1
pages: [william-guy]
result: success
---

# GROW 2.1-B · R349 · NEW1 · character — 建 William Guy（失踪 _Jane_ 船长、Len Guy 之兄、全远征救援目标；AM 三主角齐；第六批建序 84）

## 执行摘要

Phase 2.1-B character 第 34 建（type_round 41），消费 R345 第六批 discover 队列**建序 84**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=4。**

**William Guy**（*An Antarctic Mystery*）——纵帆船 _Jane_ 之船长、Len Guy 之兄，Tsalal 岛以南失踪十一载，_Halbrane_ 全程南航之救援目标。_Jane_「picked up」漂流之 Arthur Pym 与 Dirk Peters（AM-005-046）。全书情节系于其血缘：「her captain, Len Guy, is William Guy's own brother」（AM-007-074），救兄乃 _Halbrane_ 启航之由。Poe 前传中其率 _Jane_ 抵 Tsalal，于 Klock-Klock「found a population」估「ten thousand souls」（AM-005-061），善以谈判治众，「immediately endeavour[ing] to come to an understanding with Too-Wit」（AM-005-062）。叛变毁船，「Arthur Pym and William Guy escaped the doom of the _Jane_」（AM-007-070）。其生死乃 Verne 续作之谜：浮冰信息报「Captain William Guy and five of the men of the _Jane_」尚存 Tsalal 之北（AM-006-049），Len Guy 坚信「my brother William Guy and five of his companions are living」（AM-008-020），设若在世「would have recognized」英旗「and come down to the shore」（AM-022-018）。终为耐忍稳健之长者：重逢时众知「not an incident occurred to break the monotony of that existence of eleven years」（AM-024-029），困境仍探，「it occurred to William Guy to explore the fissure on the right」惜「found it blocked」（AM-024-026）；清点其众「counting William Guy, the captain, Arthur Pym, and Dirk Peters, formed a body of thirty-two men」（AM-024-004），Len Guy 终告其寻踪之线索（AM-024-035），_Halbrane_ 舟「bringing Captain William Guy and his three companions together」而归（AM-026-007）。

**role=supporting**。book=An Antarctic Mystery、first_appearance=AM-005、affiliation 空、**label=William Guy，aliases=['Captain William Guy']**。

**13 distinct solid PN**（AM-005-046/061/062、006-049、007-070/074、008-020、022-018、024-004/026/029/035、026-007）：均 solid，逾门。

**查重**：exact-slug william-guy filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**AM 2-char VVV**：无需 RFC-0003 Note。

**wikilink（AM 簇三主角齐）**：[[Len Guy]]（character，存）+ [[Dirk Peters]]（character，存）+ [[An Antarctic Mystery]]（work，存）——互链无悬挂，AM 簇 len-guy/dirk-peters/william-guy 三主角成型。Arthur Pym（Poe 主角，未建）暂纯文本，待建后回填（DEFERRED）。

prose-gate：add_page 初稿 4 超段（404、492、433、550），各插空行拆一刀后 0 超门再建（末段 Character & Traits 404 二次拆解）。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 48→**49**，registry total 1572→**1573**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=5、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=5>0，按既有实践走 NEW1 消费建序 84。消费后 queue=4。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| william-guy | iOiPad | An Antarctic Mystery | supporting | AM-005 | 13 distinct | 失踪 _Jane_ 船长-Len Guy 之兄-Tsalal 以南十一载-救援目标；label William Guy + alias Captain William Guy；AM 2-char 无 Note；拆 4 超段；strict 首验通过；互链 [[Len Guy]]/[[Dirk Peters]]/[[An Antarctic Mystery]] |

- **william-guy**：13 distinct solid PN；alias ['Captain William Guy']；character-schema 五 H2。add_page rev iOiPad。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 William Guy 船长-血缘-失踪-救援-耐忍因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；AM 2-char 无 Note。✔
- **registry 一致**：total 1573 character 49 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label William Guy 唯一；alias Captain William Guy 唯一）。✔
- **wikilink 完整性**：Len Guy/Dirk Peters/An Antarctic Mystery 链存在无悬挂；Arthur Pym 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R350 起始计数）

| 字段 | R349 起始 | R350 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 349 | 350 |
| type_round | 41 | 42 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 285 | 286 |
| last_updated_round | 349 | 350 |

## 遗留问题

1. **character 页数 49**：本轮 +1（william-guy）。queue(character) 5→**4**（建序 84 消费）。registry 全库 **1573**，unknown 0。
2. **下轮 R350 = EVV5（§3(1b)）**：since_evv5=9→R350 起始达 **10** → EVV5 触发（优先于 NEW1），character schema 全库反思评估；pages:[]，仅 G4；since_evv5 归零。queue(character)=4 仍余，EVV5 后 R351 续 NEW1（建序 85 james-starr）。
3. **AM 簇三主角齐**：len-guy + dirk-peters + william-guy + an-antarctic-mystery(work)。Arthur Pym 可续为 AM/深池候选。
4. **下次 EVV5**：R350 触发后归零，R360 起始再达 10。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
6. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、captain-grant→Robert。
7. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
8. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
9. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
10. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
11. **corpus-discover 顺延**：since_corpus=285→286（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
