---
round: 380
date: 2026-07-19
type_round: 72
phase: "2.1"
current_type: character
gene: NEW1
pages: [ephrinell]
result: success
---

# GROW 2.1-B · R380 · NEW1 · character — 建 Ephrinell（The Adventures of a Special Correspondent 兜售义齿之美国行商、与 Miss Horatia Bluett 途中联姻的实利主义旅客；ASC 簇补 claudius-bombarnac/caterna；第十批建序 108，队列归零）

## 执行摘要

Phase 2.1-B character 第 58 建（type_round 72），消费 R377 第十批 discover 队列**建序 108（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R381 触发 SCN28-zombie 补第十一批。**

**Ephrinell**（*The Adventures of a Special Correspondent*）——兜售义齿之美国行商、Strong, Bulbul & Co. 纽约商号旅行推销员、与英国发商 Miss Horatia Bluett 途中冷静联姻之实利主义旅客。自报家门「Fulk Ephrinell, of the firm of Strong, Bulbul & Co., of New York City, New York, U.S.A.」（ASC-002-027），阅历遍世「Ephrinell, as may be supposed, has been everywhere--and even farther」（ASC-002-030）。货箱充车「gathering up the odontological treasures of the forty-second case」（ASC-003-060），行李塞满前车「the front van is already full of Ephrinell's baggage」（ASC-005-028），过关无碍「Ephrinell and Miss Bluett went through like a posted letter」（ASC-016-033）。叙事者嫌其乏味「Ephrinell would not be quite the traveling companion I had dreamed of」（ASC-002-041），与 Bluett 同气「an understanding between these two perfectly Anglo-Saxon natures」（ASC-004-034），闲谈皆商「talk of brokerages and prices current」（ASC-004-053），婚约如并购「Miss Bluett will become Mrs. Ephrinell」（ASC-006-054）。Bombarnac 纳其入册「I have already secured Ephrinell, and perhaps that charming Englishwoman」（ASC-004-005），与 Caterna 同席「gather all the passengers whom the sea has not affected: ...Ephrinell, Miss Bluett, Monsieur Caterna」（ASC-004-087），全程商谈「all the time absorbed in their commercial tête-à-tête」（ASC-017-003）。

**role=supporting**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-002、affiliation 空、**label=Ephrinell，aliases=[]**。

**12 distinct solid PN**（ASC-002-027/030/041、003-060、004-005/034/053/087、005-028、006-054、016-033、017-003）：均 solid，逾门。

**查重**：exact-slug ephrinell filesystem test -f ABSENT + registry entity ABSENT（R377 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note。

**wikilink（ASC 簇补 claudius-bombarnac/caterna）**：[[Claudius Bombarnac]]（character，R363 建）/ [[Caterna]]（character，R378 建）/ [[The Adventures of a Special Correspondent]]（work，存）——三链互链无悬挂。妻 Miss Horatia Bluett 无页，正文纯文本提及无需再链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 72→**73**，registry total 1596→**1597**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2、queue=1>0 → NEW1 消费建序 108。消费后 queue=0 → R381 SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| ephrinell | o080Op | The Adventures of a Special Correspondent | supporting | ASC-002 | 12 distinct | 美国义齿行商-Strong Bulbul & Co.-货箱充车-过关无碍-乏味实利-与 Bluett 同气-闲谈皆商-婚约如并购；label Ephrinell + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Claudius Bombarnac]]/[[Caterna]]/[[The Adventures of a Special Correspondent]] |

- **ephrinell**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev o080Op（size 2388）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ephrinell 义齿行商身份-货箱-实利本色-联姻因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=supporting ∈ enum；ASC 3-char 无 Note。✔
- **registry 一致**：total 1597 character 73 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Ephrinell 唯一）。✔
- **wikilink 完整性**：Claudius Bombarnac / Caterna / The Adventures of a Special Correspondent 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R381 起始计数）

| 字段 | R380 起始 | R381 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 380 | 381 |
| type_round | 72 | 73 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 316 | 317 |
| last_updated_round | 380 | 381 |

## 遗留问题

1. **character 页数 73**：本轮 +1（ephrinell）。queue(character) 1→**0**（建序 108 消费，第十批全数用尽）。registry 全库 **1597**，unknown 0。
2. **下轮 R381 = SCN28-zombie（§3(4)）**：since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第十一批候选（≥3 grounded + dup-check），since_discover 归零。**R382 起始 since_evv5=10 → §3(1b) EVV5（先于 §3(4)，因 R381 discover 后 R382 queue>0）。**
3. **第十批 3 候选（建序 106-108）全数消费**：caterna（R378）/popof（R379）/ephrinell（R380）。R381 SCN28-zombie 补第十一批。候选方向（R372/R373 备注 + 新扫）：pan-chao（ASC 46）、ghangir（ASC 26 低）、tom-turner（RC 30）、及其他作品新扫（如 miss-horatia-bluett、doctor-tio-king 等 ASC 配角，或转其他 Verne 作品）。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + claudius-bombarnac/caterna→Ephrinell（本轮建，可回填）、claudius-bombarnac/faruskiar→Popof、claudius-bombarnac/major-noltitz→Caterna、faruskiar/claudius-bombarnac→Kinko。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=316→317（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
