---
round: 384
date: 2026-07-19
type_round: 76
phase: "2.1"
current_type: character
gene: NEW1
pages: [sir-francis-trevellyan]
result: success
---

# GROW 2.1-B · R384 · NEW1 · character — 建 Sir Francis Trevellyan（The Adventures of a Special Correspondent 沉默倨傲之英国绅士、以缄默与不屑贯穿全程的冷面旅客、终以掷弃雪茄谢幕；第十一批建序 110）

## 执行摘要

Phase 2.1-B character 第 60 建（type_round 76），消费 R381 第十一批 discover 队列**建序 110**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。下轮 R385 = NEW1 消费建序 111（tom-turner），消费后 queue 归 0 → R386 SCN28-zombie。**

**Sir Francis Trevellyan**（*The Adventures of a Special Correspondent*）——沉默倨傲之英国绅士、以缄默与不屑贯穿全程的冷面旅客。初仅以行李知其名「bore the address in full: Sir Francis Trevellyan, Trevellyan Hall, Trevellyanshire」（ASC-006-071），全程不发一言「the silent personage, who has not said a word all through the piece--I mean all through the journey」（ASC-026-021）。对俄国铁道唯以无言之蔑视「has nothing but looks of contempt and shrugs of the shoulder for all we have done」（ASC-007-028），俄国事业之谈使其不悦「this conversation on the Russian enterprise is not very pleasing to Sir Francis Trevellyan」（ASC-011-039），不肯为异邦举杯「Sir Francis Trevellyan abruptly left the」席（ASC-011-056）。临危仍保英式镇定「matters very coolly」（ASC-020-033），耸肩为其惯常辞令「he merely shrugged his shoulders, as much as to say: 'What management!'」（ASC-015-069），警报中超然「calm and impassive in his car, utterly regardless of our efforts」（ASC-021-030），无事可动「Sir Francis Trevellyan was calmly seated in his place, utterly indifferent to all that happened」（ASC-025-043）。终至冷面谢幕，掷叙事者之雪茄于站台「Sir Francis Trevellyan takes a few puffs at his own cigar, and then nonchalantly throws mine on to the platform」（ASC-026-028），对 Caterna 之喝彩无动于衷「the bravos lavished on Caterna had no effect on Sir Francis Trevellyan」（ASC-014-059），终作「欠我一句道歉与一支雪茄」之第八号旅客，再无消息「who owes me an apology and a cigar」（ASC-027-058）。

**role=supporting**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-006、affiliation 空、**label=Sir Francis Trevellyan，aliases=[]**。

**12 distinct solid PN**（ASC-006-071、007-028、011-039/056、014-059、015-069、020-033、021-030、025-043、026-021/028、027-058）：均 solid，逾门。

**查重**：exact-slug sir-francis-trevellyan filesystem test -f ABSENT + registry entity/label（Sir Francis Trevellyan）ABSENT（R381 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Claudius Bombarnac]]（character，存，ASC-026-028）/ [[Caterna]]（character，R378 建，ASC-014-059）/ [[The Adventures of a Special Correspondent]]（work，存，ASC-027-058）——三链互链无悬挂。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 74→**75**，registry total 1598→**1599**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2<10、queue=2>0 → NEW1 消费建序 110。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| sir-francis-trevellyan | Qi7ZrS | The Adventures of a Special Correspondent | supporting | ASC-006 | 12 distinct | 沉默倨傲英国绅士-Trevellyan Hall-全程不语-无言之蔑视-不肯举杯-英式镇定-耸肩辞令-掷弃雪茄谢幕；label Sir Francis Trevellyan + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Claudius Bombarnac]]/[[Caterna]]/[[The Adventures of a Special Correspondent]] |

- **sir-francis-trevellyan**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev Qi7ZrS（size 2499）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Sir Francis Trevellyan 沉默-蔑视-镇定-谢幕因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=supporting ∈ enum；ASC 3-char 无 Note。✔
- **registry 一致**：total 1599 character 75 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Sir Francis Trevellyan 唯一）。✔
- **wikilink 完整性**：Claudius Bombarnac / Caterna / The Adventures of a Special Correspondent 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R385 起始计数）

| 字段 | R384 起始 | R385 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 384 | 385 |
| type_round | 76 | 77 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 320 | 321 |
| last_updated_round | 384 | 385 |

## 遗留问题

1. **character 页数 75**：本轮 +1（sir-francis-trevellyan）。queue(character) 2→**1**（建序 110 消费）。registry 全库 **1599**，unknown 0。
2. **下轮 R385 = NEW1（§3(7)）**：since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 111（tom-turner，book Robur the Conqueror，pn_anchor RC-007，role supporting）。**消费后 queue 归 0 → R386 SCN28-zombie 补第十二批。下次 EVV5 于 R393 起始达 since_evv5=10。**
3. **第十一批剩 1 候选（建序 111）**：tom-turner。R385 NEW1 消费；消费后（R385 末）queue 归 0 → R386 SCN28-zombie 补第十二批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + claudius-bombarnac→Sir Francis Trevellyan、claudius-bombarnac/caterna→Ephrinell、claudius-bombarnac/major-noltitz→Pan Chao、claudius-bombarnac/faruskiar→Popof。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=320→321（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
