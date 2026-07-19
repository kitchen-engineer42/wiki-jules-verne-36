---
round: 374
date: 2026-07-19
type_round: 66
phase: "2.1"
current_type: character
gene: NEW1
pages: [captain-spade]
result: success
---

# GROW 2.1-B · R374 · NEW1 · character — 建 Captain Spade（Facing the Flag 纵帆船 Ebba 船长、Ker Karraje 打手、劫持 Roch 的冷酷帮凶；FF 簇补 ker-karraje/engineer-serko/simon-hart；第九批建序 103）

## 执行摘要

Phase 2.1-B character 第 53 建（type_round 66），消费 R373 第九批 discover 队列**建序 103**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。**

**Captain Spade**（*Facing the Flag*）——纵帆船 Ebba 船长、Ker Karraje（伪 Count d'Artigas）之打手、亲率劫持 Thomas Roch 与看守 Gaydon 之冷酷帮凶。初现「accompanied by Captain Spade, commander of the schooner Ebba」（FF-001-007），其职显然「the name of the captain of the Ebba, he would have replied, Spade」（FF-002-002），随主赴 Healthful House「the Count d'Artigas presented himself... accompanied by Captain Spade, the commander of the Ebba」（FF-002-012）。主谈时其侦「minutely examining the immediate surroundings of the pavilion」（FF-002-040），冷谋劫案「five men will do... even if the keeper is aroused and it becomes necessary to put him out of the way」（FF-003-027），夜下小艇「the boat was lowered, and Captain Spade and five sailors took their places in it」（FF-003-046），启锁无声「drew the key from his pocket, inserted it in the lock and turned it noiselessly」（FF-003-058），入宅掠人「two of the men then kept guard over him, while Captain Spade and the others entered the house」（FF-003-082）。缄默恭顺「Captain Spade was not in the habit of addressing him without being first spoken to」（FF-003-003），狠辣即决「Spade decided that the best thing to be done was to spring upon him as he passed and stifle his cries」（FF-003-080）；船上号令「strolling quietly about giving orders」（FF-004-003）；Serko 遣之「Good luck, Spade」（FF-003-047）。

**role=antagonist**。book='Facing the Flag'、first_appearance=FF-001、affiliation 空、**label=Captain Spade，aliases=[]**。

**12 distinct solid PN**（FF-001-007、002-002/012/040、003-003/027/046/058/080/082、003-047、004-003）：均 solid，逾门。

**查重**：exact-slug captain-spade filesystem test -f ABSENT + registry entity ABSENT（R373 discover 已验，本轮建前复验一致）。

**FF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FF 簇补 ker-karraje/engineer-serko/simon-hart）**：[[Ker Karraje]]（character，R365 建）/ [[Engineer Serko]]（character，R368 建）/ [[Simon Hart]]（character，R371 建）/ [[Facing the Flag]]（work，存）——四链互链无悬挂。Count d'Artigas 已为 ker-karraje 之 alias，正文纯文本提及无需再链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 67→**68**，registry total 1591→**1592**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0（R373 刚 discover）、queue=3>0 → NEW1 消费建序 103。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| captain-spade | wz4rNI | Facing the Flag | antagonist | FF-001 | 12 distinct | Ebba 船长-Ker Karraje 打手-亲率劫 Roch/Gaydon-冷谋启锁掠人-缄默恭顺-狠辣即决；label Captain Spade + aliases 空；FF 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Ker Karraje]]/[[Engineer Serko]]/[[Simon Hart]]/[[Facing the Flag]] |

- **captain-spade**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev wz4rNI（size 2644）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Captain Spade 船长身份-打手-劫案-恭顺狠辣因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=antagonist ∈ enum；FF 2-char 无 Note。✔
- **registry 一致**：total 1592 character 68 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Captain Spade 唯一）。✔
- **wikilink 完整性**：Ker Karraje / Engineer Serko / Simon Hart / Facing the Flag 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R375 起始计数）

| 字段 | R374 起始 | R375 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 374 | 375 |
| type_round | 66 | 67 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 310 | 311 |
| last_updated_round | 374 | 375 |

## 遗留问题

1. **character 页数 68**：本轮 +1（captain-spade）。queue(character) 3→**2**（建序 103 消费）。registry 全库 **1592**，unknown 0。
2. **下轮 R375 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 104（frycollin，book Robur the Conqueror，pn_anchor RC-002，role supporting）。**下次 EVV5 于 R382 起始达 since_evv5=10（§3(1b)）。**
3. **第九批剩 2 候选（建序 104-105）**：frycollin/kinko。R375-R376 NEW1 续消费；建序 105 消费后（R376 末）queue 归 0 → R377 SCN28-zombie 补第十批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + ker-karraje/engineer-serko/simon-hart→Captain Spade（本轮建，可回填）、uncle-prudent/phil-evans→Frycollin、faruskiar/claudius-bombarnac→Kinko。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=310→311（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
