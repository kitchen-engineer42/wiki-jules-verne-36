---
round: 363
date: 2026-07-19
type_round: 55
phase: "2.1"
current_type: character
gene: NEW1
pages: [tudor-brown]
result: success
---

# GROW 2.1-B · R363 · NEW1 · character — 建 Tudor Brown（The Waif of the Cynthia 神秘反派、阻挠 Erik 寻源之伪证者、冰原殒命；WC 配对 erik；第七批建序 95）

## 执行摘要

Phase 2.1-B character 第 45 建（type_round 55），消费 R355 第七批 discover 队列**建序 95**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=3。**

**Tudor Brown**（*The Waif of the Cynthia*）——神秘反派，以名片自现「Mr. Tudor Brown, on board the 'Albatross'」（WC-010-002），其名之乖违即被点出「the singular person who answered to the feudal name of Tudor, and the plebeian name of Brown」（WC-010-008），其形亦伪——「a man about fifty years of age」，鬈发「carroty color... made of curled silk」、钩鼻加「an enormous pair of gold spectacles」（WC-010-009）。以伪证入局——出示「a paper stamped with a notarial seal」（WC-010-044），伪称 O'Donoghan 之死「a certified account of the death of Patrick O'Donoghan」而人实存（WC-012-003）。以捐资附条件登船「on condition that he is received as a passenger」（WC-011-064），使 Erik 一行被迫携疑敌同行，盖其「a factor quite as important as Patrick O'Donoghan himself」（WC-012-038）。终局于冰原——「shot Patrick O'Donoghan through the heart」灭口（WC-019-076），旋「received a bullet in his forehead, and fell forward on his face」自毙（WC-019-077）。性冷戾拒人——「with his hat on his head」「not the least inclination to enter into any relations with his neighbors」（WC-012-044）；恶意速而残——犬啮其腿即拔枪，「white with rage and terror, insisted that the dog's brains should be blown out」（WC-012-053）；行踪拒查——爱丁堡查之「nobody knew Mr. Tudor Brown, which he thought looked suspicious」（WC-010-077）。

**role=antagonist**。book='The Waif of the Cynthia'（YAML 单引号，LAW §8）、first_appearance=WC-010、affiliation 空、**label=Tudor Brown，aliases=[]**。

**13 distinct solid PN**（WC-010-002/008/009/044/077、011-064、012-003/038/044/053、018-015、019-076/077）：均 solid，逾门。

**查重**：exact-slug tudor-brown filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**WC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（WC 配对 erik）**：[[Erik]]（character，存）/ [[The Waif of the Cynthia]]（work，存）——二链互链无悬挂。Patrick O'Donoghan（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 59→**60**，registry total 1583→**1584**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4、since_discover=7 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费建序 95。消费后 queue=3。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| tudor-brown | iBGGtU | The Waif of the Cynthia | antagonist | WC-010 | 13 distinct | 神秘反派-名形皆伪-伪证入局-捐资附条件登船-冰原灭口自毙-冷戾拒人-恶意速残；label Tudor Brown + aliases 空；WC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Erik]]/[[The Waif of the Cynthia]] |

- **tudor-brown**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev iBGGtU。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Tudor Brown 名形-伪证-登船-灭口-自毙-冷戾因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；WC 2-char 无 Note。✔
- **registry 一致**：total 1584 character 60 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Tudor Brown 唯一）。✔
- **wikilink 完整性**：Erik / The Waif of the Cynthia 二链存在无悬挂；Patrick O'Donoghan 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R364 起始计数）

| 字段 | R363 起始 | R364 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 363 | 364 |
| type_round | 55 | 56 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 7 | 8 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 299 | 300 |
| last_updated_round | 363 | 364 |

## 遗留问题

1. **character 页数 60**：本轮 +1（tudor-brown）。queue(character) 4→**3**（建序 95 消费）。registry 全库 **1584**，unknown 0。
2. **下轮 R364 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 96（uncle-prudent，book Robur the Conqueror，pn_anchor RC-002，role supporting）。**下次 EVV5 于 R371 起始达 since_evv5=10。**
3. **第七批剩 3 候选（建序 96-98）**：uncle-prudent/ker-karraje/major-noltitz。R364 起 NEW1 续消费。queue 归 0 后 R367 起 SCN28-zombie 第八批 discover。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien/Tudor Brown、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert、doctor-clawbonny→Johnson/Bell/Simpson、tudor-brown→Patrick O'Donoghan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=299→300（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
