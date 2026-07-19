---
round: 356
date: 2026-07-19
type_round: 48
phase: "2.1"
current_type: character
gene: NEW1
pages: [j-t-maston]
result: success
---

# GROW 2.1-B · R356 · NEW1 · character — 建 J. T. Maston（Gun Club 独臂铁钩之火炮狂热秘书；FEM 补配对 barbicane；第七批建序 89 首位）

## 执行摘要

Phase 2.1-B character 第 39 建（type_round 48），消费 R355 第七批 discover 队列**建序 89（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；discover_streak_low=0<3；queue(character)=10>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=9。**

**J. T. Maston**（*From the Earth to the Moon*）——Gun Club 之永久秘书、独臂钢钩之火炮狂热者。「a distinguished member and perpetual secretary of the Gun Club」（FEM-001-012），残于本业「the famous J.T. Maston, scratching his gutta-percha cranium with his steel hook」（FEM-001-023）。委员会成立即任秘书「the inevitable J.T. Maston, to whom were confided the functions of secretary」（FEM-007-003），首会「J.T. Maston immediately screwed his pen on to his steel hook and the business began」（FEM-007-004）。会中威望自赢——「interrupted the president, and was heard with the attention which his magnificent past career deserved」（FEM-007-011），Barbicane 敬其算术「our clever calculator, Mr. Maston」（FEM-007-069）。随事业各阶段——离 Baltimore「accompanied by J.T. Maston, Major Elphinstone」（FEM-013-003），铸厂自任向导「constituted himself their cicerone... forced them to visit the 1,200 furnaces one after the other」（FEM-015-015）。狂热无度——珍藏其炮残片「a precious fragment of J.T. Maston's cannon」（FEM-002-006），求战不得则辞会隐居 Arkansas「I shall send in my resignation as member of the Gun Club, and I shall go and bury myself in the backwoods of Arkansas」（FEM-001-047），月弹之议令其大悦「delighted with the idea of sending an aluminium bullet to the Selenites」（FEM-007-097）。爱 Barbicane 至深——Ardan 解其「his wanting to be killed for the man he loves」（FEM-021-065），Barbicane 直抑其锐「Maston," said Barbicane... "I agree with you」（FEM-011-015）。

**role=supporting**。book=From the Earth to the Moon、first_appearance=FEM-001、affiliation=Gun Club、**label=J. T. Maston，aliases=[]**。

**13 distinct solid PN**（FEM-001-012/023/047、002-006、007-003/004/011/069/097、011-015、013-003、015-015、021-065）：均 solid，逾门。

**查重**：exact-slug j-t-maston filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**FEM 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FEM 补配对）**：[[Impey Barbicane]]（character，存）/ [[Michel Ardan]]（character，存）/ [[From the Earth to the Moon]]（work，存）——三链互链无悬挂。Captain Nicholl（未建，建序 90 待建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 53→**54**，registry total 1577→**1578**，unknown 恒 0。

**新增 alias warn（pre-existing 潜伏，非本轮引入）**：build_registry 现 3 warn——Hector Servadac(HK(e)) + Robur the Conqueror + **Claudius Bombarnac**（work 页 adventures-of-a-special-correspondent aliases 含 'Claudius Bombarnac'，即小说法文原题，与 R353 建 character claudius-bombarnac 之 label 撞名）。属 character-vs-work 同名 label 张力（HK(e) 同类），**parked 非阻塞 warn**，不自主 fix。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=10、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =10>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=10>0，按既有实践走 NEW1 消费建序 89。消费后 queue=9。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| j-t-maston | Q4ST79 | From the Earth to the Moon | supporting | FEM-001 | 13 distinct | Gun Club 永久秘书-独臂钢钩-火炮狂热者；label J. T. Maston + aliases 空；affiliation Gun Club；FEM 2-char 无 Note；初稿 0 超段直接建；strict 首验通过；互链 [[Impey Barbicane]]/[[Michel Ardan]]/[[From the Earth to the Moon]] |

- **j-t-maston**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev Q4ST79。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Maston 秘书身份-会中威望-事业随行-狂热-爱 Barbicane 因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；FEM 2-char 无 Note。✔
- **registry 一致**：total 1578 character 54 unknown 0；3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label J. T. Maston 唯一）。✔
- **wikilink 完整性**：Impey Barbicane / Michel Ardan / From the Earth to the Moon 三链存在无悬挂；Captain Nicholl 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R357 起始计数）

| 字段 | R356 起始 | R357 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 356 | 357 |
| type_round | 48 | 49 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 292 | 293 |
| last_updated_round | 356 | 357 |

## 遗留问题

1. **character 页数 54**：本轮 +1（j-t-maston）。queue(character) 10→**9**（建序 89 首位消费）。registry 全库 **1578**，unknown 0。
2. **下轮 R357 = NEW1（§3(7)）**：since_evv5=6<10；discover_streak_low=0<3；queue(character)=9>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 90（captain-nicholl，book From the Earth to the Moon，pn_anchor FEM-010，role antagonist）——Barbicane 之装甲专家宿敌。**下次 EVV5 于 R360 起始达 since_evv5=10。**
3. **FEM 簇扩充**：barbicane（既有）+ j-t-maston（本轮）+ michel-ardan（既有），配 captain-nicholl（建序 90 待建）。
4. **Claudius Bombarnac alias warn（新增第 3 warn）**：character-vs-work 同名 label 张力，与 HK(e)（hector-servadac vs off-on-a-comet）同类，parked 非阻塞，Phase 2.1 EVV6 统一处理。
5. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、captain-grant→Robert。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=292→293（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
