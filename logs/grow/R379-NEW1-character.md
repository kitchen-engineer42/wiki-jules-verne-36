---
round: 379
date: 2026-07-19
type_round: 71
phase: "2.1"
current_type: character
gene: NEW1
pages: [popof]
result: success
---

# GROW 2.1-B · R379 · NEW1 · character — 建 Popof（The Adventures of a Special Correspondent Grand Transasiatic 列车长、军人风度之俄国人、Bombarnac 最可信之消息源；ASC 簇补 claudius-bombarnac/faruskiar；第十批建序 107）

## 执行摘要

Phase 2.1-B character 第 57 建（type_round 71），消费 R377 第十批 discover 队列**建序 107**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Popof**（*The Adventures of a Special Correspondent*）——Grand Transasiatic 列车长、军人风度之俄国人、其岗位紧邻行李车而成 Bombarnac 全车最可信之消息源。初现「Popof, our head guard, a true Russian of soldierly bearing」（ASC-005-020），岗位定位「Popof's little cabin is on the platform of the first car, in the left-hand corner」（ASC-005-028）。为叙事者通报旅客「asked if he knew anything of our fellow travelers」（ASC-006-037），奉命探名「asked Popof to discover the name of the defunct」（ASC-008-078），谙熟站点「Popof pointed out the stations for the guards on the parapet of the bridge」（ASC-010-068），告知过境者「would cross the Russo-Chinese frontier, so that they interested me little」（ASC-013-002）。叙事者倚为心腹「he is the only one I can really trust besides Popof」（ASC-006-032），烟中相契「Popof smiles and soon his perfumed puffs are mingling voluptuously with mine」（ASC-006-034），有请必应「Popof did not want asking twice」（ASC-008-016）。Bombarnac 探讯「as soon as Popof reappeared I said to him: 'Anything fresh?'」（ASC-008-011），揭 Faruskiar 名「this leading star, I soon learned from Popof, bore the name of Faruskiar」（ASC-008-082），全程随车「goes through with us」（ASC-008-036）。

**role=supporting**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-005、affiliation 空、**label=Popof，aliases=[]**。

**12 distinct solid PN**（ASC-005-020/028、006-032/034/037、008-011/016/036/078/082、010-068、013-002）：均 solid，逾门。

**查重**：exact-slug popof filesystem test -f ABSENT + registry entity ABSENT（R377 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note。

**wikilink（ASC 簇补 claudius-bombarnac/faruskiar）**：[[Claudius Bombarnac]]（character，R363 建）/ [[Faruskiar]]（character，R369 建）/ [[The Adventures of a Special Correspondent]]（work，存）——三链互链无悬挂。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 71→**72**，registry total 1595→**1596**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1、queue=2>0 → NEW1 消费建序 107。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| popof | vj4cIH | The Adventures of a Special Correspondent | supporting | ASC-005 | 12 distinct | 列车长-军人风度俄国人-岗邻行李车-通报旅客-奉命探名-谙熟站点-叙事者心腹-烟中相契-揭 Faruskiar 名；label Popof + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Claudius Bombarnac]]/[[Faruskiar]]/[[The Adventures of a Special Correspondent]] |

- **popof**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev vj4cIH（size 2367）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Popof 列车长身份-岗位-消息源-心腹因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=supporting ∈ enum；ASC 3-char 无 Note。✔
- **registry 一致**：total 1596 character 72 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Popof 唯一）。✔
- **wikilink 完整性**：Claudius Bombarnac / Faruskiar / The Adventures of a Special Correspondent 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R380 起始计数）

| 字段 | R379 起始 | R380 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 379 | 380 |
| type_round | 71 | 72 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 315 | 316 |
| last_updated_round | 379 | 380 |

## 遗留问题

1. **character 页数 72**：本轮 +1（popof）。queue(character) 2→**1**（建序 107 消费）。registry 全库 **1596**，unknown 0。
2. **下轮 R380 = NEW1（§3(7)）**：since_evv5=7<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 108（ephrinell，book The Adventures of a Special Correspondent，pn_anchor ASC-002，role supporting）。消费后 queue=0。**下次 EVV5 于 R382 起始达 since_evv5=10（§3(1b)）。**
3. **第十批剩 1 候选（建序 108）**：ephrinell。R380 NEW1 消费后 queue 归 0 → **R381 SCN28-zombie 补第十一批**（R382 EVV5 逼近但 R381 since_evv5=9<10，§3(4) 先于 §3(1) 触发 discover；R382 起始 since_evv5=10 → §3(1b) EVV5）。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + claudius-bombarnac/faruskiar→Popof（本轮建，可回填）、claudius-bombarnac/major-noltitz→Caterna、claudius-bombarnac→Ephrinell、faruskiar/claudius-bombarnac→Kinko。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=315→316（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
