---
round: 388
date: 2026-07-19
type_round: 80
phase: "2.1"
current_type: character
gene: NEW1
pages: [horatia-bluett]
result: success
---

# GROW 2.1-B · R388 · NEW1 · character — 建 Miss Horatia Bluett（The Adventures of a Special Correspondent 兜售束身衣之英国女行商、与 Ephrinell 途中如契约联姻旋即解除；ASC 补 ephrinell/claudius-bombarnac，第十二批建序 113）

## 执行摘要

Phase 2.1-B character 第 63 建（type_round 80），消费 R386 第十二批 discover 队列**建序 113**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。下轮 R389 = NEW1 消费建序 114（zinca-klork），消费后 queue 归 0 → R390 SCN28-zombie。**

**Miss Horatia Bluett**（*The Adventures of a Special Correspondent*）——兜售束身衣之英国女行商、与 Ephrinell 途中如契约联姻旋即解除。为伦敦商行代理「Miss Horatia Bluett represented an important firm in London」（ASC-004-035），形貌枯瘦朴素「as thin, as dry, as plain as ever... and in place of jewelry a noisy bunch of keys」（ASC-019-040）。与美国行商同气「there was an understanding between these two perfectly Anglo-Saxon natures」（ASC-004-034），早定婚约「as soon as they reach Pekin, Miss Bluett will become Mrs. Ephrinell」（ASC-006-054），婚誓简短如收据「a dry 'yes' from Horatia Bluett, a short 'yes' from Fulk Ephrinell, and the two are declared to be united in the bonds of matrimony」（ASC-022-030），终如作废契约「Miss Horatia Bluett remained Miss Horatia Bluett」（ASC-027-053）。言谈唯商「Ephrinell and Miss Bluett to talk of brokerages and prices current」（ASC-004-053），以行商眼观世「the women all have hair」（ASC-010-028），婚礼上犹讨价「well, let us say twenty per cent., Miss Bluett」（ASC-022-025）。与 Ephrinell 相契「a close intimacy, founded on a similarity in tastes and aptitudes」（ASC-014-032），为 Bombarnac 所关注问询「not see him at his post by the side of Miss Horatia Bluett」（ASC-009-011），劫袭中被 Popof 促入车厢「Popof hurried Madame Caterna, Miss Horatia Bluett, and the other women into the cars」（ASC-020-025）。

**role=supporting**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-004、affiliation 空、**label=Miss Horatia Bluett，aliases=[]**。

**12 distinct solid PN**（ASC-004-034/035/053、006-054、009-011、010-028、014-032、019-040、020-025、022-025/030、027-053）：均 solid，逾门。

**查重**：exact-slug horatia-bluett filesystem test -f ABSENT（bucket ho）+ registry entity/label（Miss Horatia Bluett）ABSENT（R386 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Ephrinell]]（character，R380 建，ASC-014-032）/ [[Claudius Bombarnac]]（character，存，ASC-009-011）/ [[The Adventures of a Special Correspondent]]（work，存，ASC-020-025）——三链互链无悬挂。Madame Caterna 于正文纯文本提及（无独立页，caterna 为其夫）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 77→**78**，registry total 1601→**1602**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 2）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1<10、queue=2>0 → NEW1 消费建序 113。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| horatia-bluett | bS0vza | The Adventures of a Special Correspondent | supporting | ASC-004 | 12 distinct | 伦敦束身衣女行商-枯瘦朴素-与 Ephrinell 同气-早定婚约-婚誓如收据-如作废契约-言谈唯商-婚礼讨价-被促入车厢；label Miss Horatia Bluett + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Ephrinell]]/[[Claudius Bombarnac]]/[[The Adventures of a Special Correspondent]] |

- **horatia-bluett**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev bS0vza（size 2396）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Horatia Bluett 女行商-联姻-解除-唯商-讨价因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；ASC 3-char 无 Note。✔
- **registry 一致**：total 1602 character 78 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Miss Horatia Bluett 唯一）。✔
- **wikilink 完整性**：Ephrinell / Claudius Bombarnac / The Adventures of a Special Correspondent 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R389 起始计数）

| 字段 | R388 起始 | R389 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 388 | 389 |
| type_round | 80 | 81 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 324 | 325 |
| last_updated_round | 388 | 389 |

## 遗留问题

1. **character 页数 78**：本轮 +1（horatia-bluett）。queue(character) 2→**1**（建序 113 消费）。registry 全库 **1602**，unknown 0。
2. **下轮 R389 = NEW1（§3(7)）**：since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 114（zinca-klork，book The Adventures of a Special Correspondent，pn_anchor ASC-004，role supporting）。**消费后 queue 归 0 → R390 SCN28-zombie 补第十三批。下次 EVV5 于 R393 起始达 since_evv5=10。**
3. **第十二批剩 1 候选（建序 114）**：zinca-klork。R389 NEW1 消费；消费后（R389 末）queue 归 0 → R390 SCN28-zombie 补第十三批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + ephrinell/claudius-bombarnac→Miss Horatia Bluett（本轮建，可回填）、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=324→325（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
