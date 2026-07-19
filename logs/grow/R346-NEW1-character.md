---
round: 346
date: 2026-07-19
type_round: 38
phase: "2.1"
current_type: character
gene: NEW1
pages: [paulina-barnett]
result: success
---

# GROW 2.1-B · R346 · NEW1 · character — 建 Paulina Barnett（随 Hobson 极地远征之女旅行家；FC 簇配对；第六批建序 81）

## 执行摘要

Phase 2.1-B character 第 31 建（type_round 38），消费 R345 第六批 discover 队列**建序 81**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；discover_streak_low=0<3；queue(character)=8>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=7。**

**Paulina Barnett**（*The Fur Country*）——皇家学会桂冠女旅行家。「no ordinary woman ... Paulina Barnett, a laureate of the Royal Society」，名列「the rival of the Pfeiffers, Tinnis, and Haimaires of Hull」，足迹上溯 Brahmaputra「as far as the mountains of Thibet」、横越「an unknown corner of New Holland」（FC-001-027）；阅历之广，寒地中忆「the tropical heat of India」、叹「the difference between these Polar regions and the green prairies of Australia」（FC-005-023）。她为远征荣誉之宾——「the lady traveller was to join the expedition of Jaspar Hobson for the exploration of the north」（FC-001-029），好奇主动，欲「now see the Lieutenant at work」（FC-002-011），且「well informed as to the ulterior projects of the celebrated Company」（FC-002-048）。Fort Hope 半岛断裂化冰岛漂流，其坚毅撑起殖民地——「Mrs Barnett was invaluable in setting an example of constant activity: always brave, she kept herself awake, and encouraged others」（FC-020-019），元旦 Hobson「complimented her on the courage and good temper with which she endured」（FC-020-020），危愈深而「courage was unabated」（FC-021-060）。其勇兼民主之温——「shared everything with her companions, never holding herself aloof ... working zealously amongst the others」（FC-018-010），为不伤土著少女之心而「showed superhuman courage」（FC-019-048）；识人亦锐，告中尉知其「on occasion you would be ready to devote body and soul to science」（FC-007-024）。

**role=supporting**。book=The Fur Country、first_appearance=FC-001、affiliation 空、**label=Paulina Barnett，aliases=['Mrs Paulina Barnett']**。

**13 distinct solid PN**（FC-001-027/029、002-011/048、004-064、005-023、006-018、007-024、018-010、019-048、020-019/020、021-060）：均 solid，逾门。

**查重**：exact-slug paulina-barnett filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FC 簇配对）**：[[Jaspar Hobson]]（character，存，slug lieutenant-hobson label Jaspar Hobson）+ [[The Fur Country]]（work，存）——互链无悬挂，FC 簇 lieutenant-hobson↔paulina-barnett 配对成型。Madge（忠仆，未建）暂纯文本，待建后回填（DEFERRED）。

prose-gate：add_page 初稿 4 超段（659、467、542、+ Role drift 段），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过（无 0% 重叠 warn）。quality featured 未剥离。

character 计数 45→**46**，registry total 1569→**1570**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=8、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =8>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=8>0，按既有实践走 NEW1 消费建序 81。消费后 queue=7。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| paulina-barnett | 1ZgcXB | The Fur Country | supporting | FC-001 | 13 distinct | 皇家学会桂冠女旅行家-随 Hobson 极地远征-冰岛漂流中之坚毅主心骨；label Paulina Barnett + alias Mrs Paulina Barnett；FC 2-char 无 Note；拆 4 超段；strict 首验通过；互链 [[Jaspar Hobson]]/[[The Fur Country]] |

- **paulina-barnett**：13 distinct solid PN；alias ['Mrs Paulina Barnett']；character-schema 五 H2。add_page rev 1ZgcXB。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Barnett 声望-好奇-坚毅-民主之温因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；FC 2-char 无 Note。✔
- **registry 一致**：total 1570 character 46 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Paulina Barnett 唯一）。✔
- **wikilink 完整性**：Jaspar Hobson/The Fur Country 链存在无悬挂；Madge 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R347 起始计数）

| 字段 | R346 起始 | R347 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 346 | 347 |
| type_round | 38 | 39 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 282 | 283 |
| last_updated_round | 346 | 347 |

## 遗留问题

1. **character 页数 46**：本轮 +1（paulina-barnett）。queue(character) 8→**7**（建序 81 消费）。registry 全库 **1570**，unknown 0。
2. **下轮 R347 = NEW1（§3(7)）**：since_evv5=6<10；discover_streak_low=0<3；queue(character)=7>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 82（palmyrin-rosette）。Palmyrin Rosette（book Off on a Comet，pn_anchor OC-027，role supporting，OC 2-char 无 Note）——Gallia 上古怪天文学家；OC 簇扩（hector-servadac/ben-zoof 已建）。
3. **FC 簇成型**：lieutenant-hobson + paulina-barnett + the-fur-country(work)。Madge 可续为 FC 簇第三配对。
4. **lieutenant-hobson→Barnett 回链回填**：lieutenant-hobson 页 Mrs Barnett 纯文本，可 edit_page 改 [[Paulina Barnett]]（DEFERRED，非阻塞）。
5. **下次 EVV5 预判**：since_evv5 上次归零 R340，R350 起始达 10 → EVV5 约 R350 触发（届时 queue 尚余候选，1b 优先于 NEW1，暂停一轮 NEW1）。
6. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
7. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、captain-grant→Robert。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=282→283（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
