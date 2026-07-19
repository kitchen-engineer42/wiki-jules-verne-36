---
round: 389
date: 2026-07-19
type_round: 81
phase: "2.1"
current_type: character
gene: NEW1
pages: [zinca-klork]
result: success
---

# GROW 2.1-B · R389 · NEW1 · character — 建 Zinca Klork（The Adventures of a Special Correspondent 藏身货箱偷渡英雄 Kinko 之罗马尼亚未婚妻、于北京翘首以待终成眷属；ASC 补 kinko/claudius-bombarnac，第十二批建序 114，末候选，消费后 queue 归 0）

## 执行摘要

Phase 2.1-B character 第 64 建（type_round 81），消费 R386 第十二批 discover 队列**建序 114（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → 下轮 R390 = §3(4) SCN28-zombie 补第十三批。**

**Zinca Klork**（*The Adventures of a Special Correspondent*）——藏身货箱偷渡英雄 Kinko 之罗马尼亚未婚妻、于北京翘首以待终成眷属。名示其籍「this Zinca Klork--her name showed it--ought to be a Roumanian」（ASC-004-017），美而候人「the most lovely of Roumanians, is expecting you at Pekin」（ASC-010-057）。为 Kinko 奇旅之目的地，货箱标其址「Mademoiselle Zinca Klork, Avenue Cha-Coua, Pekin, Petchili, China」（ASC-004-016），长途待中忧煎「pretty Zinca Klork, devoured by anxiety in her house in the Avenue Cha-Coua」（ASC-022-060），闻噩耗恸绝「the unhappy Zinca falls on to a chair... her tears roll down like rain on an autumn night」（ASC-026-085），闻爱人声即起「Zinca jumps up, springs to the window, opens it, and we look out」（ASC-026-090）。见生客而惊「evidently much surprised at seeing a stranger in her doorway」（ASC-026-044），为救 Kinko 挺身恳请「Gentlemen... do save him before he is sentenced」（ASC-027-018），得天眷佑「divine intervention in favor of Kinko and Zinca Klork was manifested in all its plenitude」（ASC-013-104）。终嫁 Kinko「No. 11 was married to Zinca Klork with great ceremony」（ASC-027-059），Bombarnac 寻至其门「the name of Madame Zinca Klork on a door」（ASC-026-041），为 Kinko 伪装货运之收件人「glass goods exported to Miss Zinca Klork, Avenue Cha-Coua, Pekin, China」（ASC-007-057）。

**role=supporting**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-004、affiliation 空、**label=Zinca Klork，aliases=[]**。

**12 distinct solid PN**（ASC-004-016/017、007-057、010-057、013-104、022-060、026-041/044/085/090、027-018/059）：均 solid，逾门。

**查重**：exact-slug zinca-klork filesystem test -f ABSENT（bucket zi）+ registry entity/label（Zinca Klork）ABSENT（R386 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Kinko]]（character，R376 建，ASC-027-059）/ [[Claudius Bombarnac]]（character，存，ASC-026-041）/ [[The Adventures of a Special Correspondent]]（work，存，ASC-007-057）——三链互链无悬挂。Madame Caterna（ASC-027-009 拥抱 Zinca）于正文未提及，不涉链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 78→**79**，registry total 1602→**1603**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 2）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2<10、queue=1>0 → NEW1 消费建序 114。消费后 queue=0。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| zinca-klork | 60453T | The Adventures of a Special Correspondent | supporting | ASC-004 | 12 distinct | Kinko 之罗马尼亚未婚妻-北京翘首以待-货箱目的地-忧煎-闻噩恸绝-闻声即起-见客而惊-挺身恳请-得天眷佑-终成眷属；label Zinca Klork + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Kinko]]/[[Claudius Bombarnac]]/[[The Adventures of a Special Correspondent]] |

- **zinca-klork**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev 60453T（size 2321）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Zinca Klork 未婚妻-待人-忧煎-恸绝-恳请-成眷因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；ASC 3-char 无 Note。✔
- **registry 一致**：total 1603 character 79 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Zinca Klork 唯一）。✔
- **wikilink 完整性**：Kinko / Claudius Bombarnac / The Adventures of a Special Correspondent 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R390 起始计数）

| 字段 | R389 起始 | R390 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 389 | 390 |
| type_round | 81 | 82 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 325 | 326 |
| last_updated_round | 389 | 390 |

## 遗留问题

1. **character 页数 79**：本轮 +1（zinca-klork）。queue(character) 1→**0**（建序 114 消费，第十二批全数消费完毕）。registry 全库 **1603**，unknown 0。
2. **下轮 R390 = SCN28-zombie（§3(4)）**：since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**。补第十三批候选（pages:[]，仅 G4，since_discover 归零）。**下次 EVV5 于 R393 起始达 since_evv5=10。**
3. **第十三批 discover（R390）**：queue 归 0，需补 ≥3 grounded+dup-checked 候选。GM 新簇续挖（godfrey/kolderup/carefinotu）或跨作品拓展。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=325→326（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
