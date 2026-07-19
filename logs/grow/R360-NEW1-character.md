---
round: 360
date: 2026-07-19
type_round: 52
phase: "2.1"
current_type: character
gene: NEW1
pages: [captain-hull]
result: success
---

# GROW 2.1-B · R360 · NEW1 · character — 建 Captain Hull（Pilgrim 号仁勇捕鲸船长、捕鲸罹难引全书悲剧；DSCF 簇成三页；第七批建序 93）

## 执行摘要

Phase 2.1-B character 第 43 建（type_round 52），消费 R355 第七批 discover 队列**建序 93**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=5。R361 起始 since_evv5=10 → §3(1b) EVV5 触发。**

**Captain Hull**（*Dick Sand: A Captain at Fifteen*）——Pilgrim 号仁勇捕鲸船长，James Weldon 所托，救漂流者上船，终于捕鲸中罹难引全书悲剧。James W. Weldon「had for several years intrusted the command of it to Captain Hull」（DSCF-001-003），「a good seaman, and also one of the most skilful harpooners of the flotilla」（DSCF-001-005），善避冰山「knew how to disentangle himself... from among those icebergs」（DSCF-001-004）。捕鲸季败，「a request for a passage was made which he could not refuse」（DSCF-001-012）；少年学徒受其恩「it was, when he was a cabin-boy on board a merchant vessel, that Dick Sand was remarked by Captain Hull」（DSCF-002-029）。见沉船遂令救「"Howik," said Captain Hull... "heave to, and lower the small boat"」（DSCF-003-045），登船「discovered the bodies of five negroes」（DSCF-003-083），庇护之而慰「you have not compromised your liberty in coming on board of the American brig」（DSCF-004-024）。仁心自觉——知贩奴之酷「obliged to tell Mrs. Weldon that such facts, monstrous as they might be, were unhappily not rare」（DSCF-004-018）。海上自信近于致命之骄——「More than once it has been my lot to hunt the whale with a single boat, and I have always finished by taking possession of it」（DSCF-007-005），然审慎「was forced to put on Dick Sand the care of guarding the 'Pilgrim'」（DSCF-007-012）方出。捕鲸转灾——呼「the beast is going to take a spring and throw herself on us」（DSCF-008-076），末举英勇「he was seen for a moment hoisting the boatswain on a wreck」（DSCF-008-109），旋没于海。

**role=supporting**。book='Dick Sand: A Captain at Fifteen'（YAML 单引号，LAW §8）、first_appearance=DSCF-001、affiliation 空、**label=Captain Hull，aliases=[]**。

**13 distinct solid PN**（DSCF-001-003/004/005/012、002-029、003-045/083、004-018/024、007-005/012、008-076/109）：均 solid，逾门。

**查重**：exact-slug captain-hull filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**DSCF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（DSCF 簇成三页）**：[[Mrs. Weldon]]（character，R359 建）/ [[Dick Sand]]（character，存）/ [[Dick Sand: A Captain at Fifteen]]（work，存）——三链互链无悬挂。Negoro（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 57→**58**，registry total 1581→**1582**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6、since_discover=4 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=6>0，按既有实践走 NEW1 消费建序 93。消费后 queue=5。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| captain-hull | bJtQRQ | Dick Sand: A Captain at Fifteen | supporting | DSCF-001 | 13 distinct | Pilgrim 仁勇捕鲸船长-Weldon 所托-救漂流者-仁心自觉-致命自信-捕鲸罹难；label Captain Hull + aliases 空；book 冒号单引号；DSCF 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Mrs. Weldon]]/[[Dick Sand]]/[[Dick Sand: A Captain at Fifteen]] |

- **captain-hull**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev bJtQRQ。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Hull 船长身份-受托-救援-仁心-致命自信-罹难因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 冒号单引号）；DSCF 2-char 无 Note。✔
- **registry 一致**：total 1582 character 58 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Captain Hull 唯一）。✔
- **wikilink 完整性**：Mrs. Weldon / Dick Sand / Dick Sand: A Captain at Fifteen 三链存在无悬挂；Negoro 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R361 起始计数）

| 字段 | R360 起始 | R361 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 360 | 361 |
| type_round | 52 | 53 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 296 | 297 |
| last_updated_round | 360 | 361 |

## 遗留问题

1. **character 页数 58**：本轮 +1（captain-hull）。queue(character) 6→**5**（建序 93 消费）。registry 全库 **1582**，unknown 0。
2. **下轮 R361 = EVV5（§3(1b)）**：since_evv5=10≥10 → §3(1b) EVV5 触发（schema-reflection 全 character 页复评，pages:[]，仅 G4，since_evv5 归 0）。scan 3 结构指标（5 H2 精确匹配、role∈enum、book 非空）+ 追踪 2 内容债指标（≥5 distinct PN、prose ≤400）。**注意 role 位于 frontmatter，须读页文件扫描，勿从 pages.json 顶层误判（R350 假阴教训）。** stage 仅 grow_state + R361-EVV5 日志。
3. **DSCF 簇成三页**：cousin-benedict + mrs-weldon + captain-hull + dick-sand（既有）+ hercules（既有）+ dick-sand-a-captain-at-fifteen(work)。
4. **第七批剩 5 候选（建序 94-98）**：doctor-clawbonny/tudor-brown/uncle-prudent/ker-karraje/major-noltitz。R361 EVV5 后 R362 起 NEW1 续消费（建序 94 doctor-clawbonny）。
5. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=296→297（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
