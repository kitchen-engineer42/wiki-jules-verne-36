---
round: 368
date: 2026-07-19
type_round: 60
phase: "2.1"
current_type: character
gene: NEW1
pages: [engineer-serko]
result: success
---

# GROW 2.1-B · R368 · NEW1 · character — 建 Engineer Serko（Facing the Flag 首席帮凶、潜艇设计者、逼取 Roch 之秘的狡黠工程师；FF 簇补 ker-karraje/thomas-roch；第八批建序 99）

## 执行摘要

Phase 2.1-B character 第 49 建（type_round 60），消费 R367 第八批 discover 队列**建序 99**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=3。**

**Engineer Serko**（*Facing the Flag*）——Ker Karraje 首席帮凶、潜艇设计者。初现于纵帆船，戏遣 Spade 掠人「Good luck, Spade... and don't make more noise about it than if you were a gallant carrying off his lady-love」（FF-003-047）；其史系于海盗首领——澳洲金矿间「were Captain Spade and Engineer Serko, two outcasts, whom a certain community of ideas and character soon bound together in close friendship」（FF-010-048）。使 Ker Karraje 无敌之潜艇乃其构想——「well versed in his profession, and... a clever mechanic to boot, and who had made a special study of submarine craft, [he] proposed to Ker Karraje that they should construct one」（FF-010-061），艇「constructed from a model and under the personal supervision of Engineer Serko」（FF-010-064）；其为全谋之脑「the most formidable and resolute of his accomplices」（FF-010-065），营 Back Cup「installed an electric power house」（FF-010-081）。其恒务在破发明家——Roch「is daily sounded in regard to his discoveries, especially by Engineer Serko」（FF-011-016），叙事者望「Engineer Serko's efforts to acquire it will remain futile」（FF-013-006）。威而含笑——「'Of business, Mr. Hart, of business,'... with a smile. 'Our engines are now completed, and when the fine weather returns we shall resume offensive operations'」（FF-014-027）；矜其巧「very proud of his handiwork,--and also very positive that the prisoner of Back Cup will never be able to disclose the secret」（FF-010-077）；守秘甚严，叙事者听「in the hope that Engineer Serko will give away a part of the secret, but in vain」（FF-012-049）。

**role=antagonist**。book='Facing the Flag'（YAML 单引号，LAW §8）、first_appearance=FF-003、affiliation 空、**label=Engineer Serko，aliases=[]**。

**11 distinct solid PN**（FF-003-047、010-048/061/064/065/077/081、011-016、012-049、013-006、014-027）：均 solid，逾门。

**查重**：exact-slug engineer-serko filesystem + registry entity ABSENT（R367 discover 已验，本轮建前复验一致）。

**FF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FF 簇补 ker-karraje/thomas-roch）**：[[Ker Karraje]]（character，R365 建）/ [[Thomas Roch]]（character，存）/ [[Facing the Flag]]（work，存）——三链互链无悬挂。Captain Spade / Simon Hart（未建；simon-hart 为第八批建序 102 待建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 63→**64**，registry total 1587→**1588**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0（R367 刚 discover）、queue=4>0 → NEW1 消费建序 99。消费后 queue=3。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| engineer-serko | bdionw | Facing the Flag | antagonist | FF-003 | 11 distinct | 首席帮凶-潜艇设计者-全谋之脑-营 Back Cup-逼取 Roch 之秘-威而含笑-矜巧守秘；label Engineer Serko + aliases 空；FF 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Ker Karraje]]/[[Thomas Roch]]/[[Facing the Flag]] |

- **engineer-serko**：11 distinct solid PN；aliases []；character-schema 五 H2。add_page rev bdionw。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Serko 帮凶身份-设计潜艇-营巢-逼秘-含笑守秘因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；FF 2-char 无 Note。✔
- **registry 一致**：total 1588 character 64 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Engineer Serko 唯一）。✔
- **wikilink 完整性**：Ker Karraje / Thomas Roch / Facing the Flag 三链存在无悬挂；Captain Spade/Simon Hart 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R369 起始计数）

| 字段 | R368 起始 | R369 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 368 | 369 |
| type_round | 60 | 61 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 304 | 305 |
| last_updated_round | 368 | 369 |

## 遗留问题

1. **character 页数 64**：本轮 +1（engineer-serko）。queue(character) 4→**3**（建序 99 消费）。registry 全库 **1588**，unknown 0。
2. **下轮 R369 = NEW1（§3(7)）**：since_evv5=7<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 100（faruskiar，book The Adventures of a Special Correspondent，pn_anchor ASC-008，role antagonist）。**下次 EVV5 于 R371 起始达 since_evv5=10（§3(1b) 先于 NEW1）。**
3. **第八批剩 3 候选（建序 100-102）**：faruskiar/phil-evans/simon-hart。R369-R370 NEW1 消费 faruskiar/phil-evans；R371 起始 since_evv5=10 → §3(1b) EVV5 先行，simon-hart（建序 102）顺延至 EVV5 后 R372 NEW1。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + major-noltitz→Faruskiar、uncle-prudent→Phil Evans、ker-karraje→Engineer Serko（本轮建，可回填）/Simon Hart、thomas-roch→Simon Hart/Ker Karraje、engineer-serko→Captain Spade/Simon Hart。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=304→305（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
