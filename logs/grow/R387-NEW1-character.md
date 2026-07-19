---
round: 387
date: 2026-07-19
type_round: 79
phase: "2.1"
current_type: character
gene: NEW1
pages: [tartlet]
result: success
---

# GROW 2.1-B · R387 · NEW1 · character — 建 Tartlet（Godfrey Morgan 之滑稽舞蹈兼体操教师、荒岛遇难的怯懦搭档、陆上端方海上失态；GM 新簇首页，第十二批建序 112）

## 执行摘要

Phase 2.1-B character 第 62 建（type_round 79），消费 R386 第十二批 discover 队列**建序 112**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。下轮 R388 = NEW1 消费建序 113（horatia-bluett）。**

**Tartlet**（*Godfrey Morgan*）——Godfrey 之滑稽舞蹈兼体操教师、荒岛遇难的怯懦搭档、陆上端方海上失态。**GM 新簇首个 character 页**（godfrey-morgan work 页已存，label Godfrey Morgan；本作暂无兄弟 character 页）。为舞蹈仪态教师「professor of dancing and deportment in the capital of their state」（GM-004-004），中年独身「a bachelor, and aged about forty-five at the time we introduce him to our readers」（GM-004-005）。为 Kolderup 择为侄之旅伴「this Professor Tartlet, whom William W. Kolderup had chosen as his nephew's companion during the projected voyage」（GM-004-026），遂成行「thus was Professor Tartlet selected as the travelling-companion of Godfrey Morgan」（GM-004-052），一路夸大险情「still less to Tartlet, whose troubled spirit exaggerated from day to day the dangers」（GM-005-032）。陆上仪态不可撼「the professor preserved an absolute per[fect]」平衡（GM-004-027），海上尽失「Professor Tartlet, generally so firm on his limbs, had lost all his dancing equilibrium」（GM-005-005），晕船兼恐惧「not only did Professor Tartlet suffer from sea-sickness, but also that fear had seized him」（GM-007-014），登岸复其端方「Professor Tartlet recovered the aplomb which he had lost since his departure; his feet placed themselves naturally, with their toes turned ou[t]」（GM-008-076）。为 Godfrey 所救「down by Tartlet; he unloosed the life-belt and rubbed him vigorously」（GM-008-066），受 Kolderup 召「'Mr. Tartlet,' said William W. Kolderup, 'I have sent for you'」（GM-004-028），乱中犹护琴弓「himself that his precious kit and bow」（GM-008-070）。

**role=supporting**。book='Godfrey Morgan'、first_appearance=GM-004、affiliation 空、**label=Tartlet，aliases=[]**。

**12 distinct solid PN**（GM-004-004/005/026/027/028/052、005-005/032、007-014、008-066/070/076）：均 solid，逾门。

**查重**：exact-slug tartlet filesystem test -f ABSENT（bucket ta）+ registry entity/label（Tartlet）ABSENT（R386 discover 已验，本轮建前复验一致）。

**GM 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Godfrey Morgan]]（work，存，GM-008-070）——Appearances 单链无悬挂。Godfrey（pupil）/ William W. Kolderup（patron）暂无 character 页，Relationships 以纯文本 PN-grounded bullet 呈现（非悬挂链）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 76→**77**，registry total 1600→**1601**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 2）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0（R386 刚 discover）、queue=3>0 → NEW1 消费建序 112。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| tartlet | cmnQvV | Godfrey Morgan | supporting | GM-004 | 12 distinct | 舞蹈仪态教师-中年独身-Kolderup 择为旅伴-一路夸大险情-陆上端方-海上失态-晕船兼恐惧-登岸复端方-护琴弓；label Tartlet + aliases 空；GM 2-char 无 Note；0 超段直建；strict 首验通过；GM 新簇首页；Appearances 链 [[Godfrey Morgan]]，Relationships 纯文本 Godfrey/Kolderup |

- **tartlet**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev cmnQvV（size 2559）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Tartlet 舞蹈教师-择伴-夸大险情-陆端海失-受救护琴因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；GM 2-char 无 Note。✔
- **registry 一致**：total 1601 character 77 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Tartlet 唯一）。✔
- **wikilink 完整性**：Godfrey Morgan（work）单链存在无悬挂；Relationships 纯文本无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R388 起始计数）

| 字段 | R387 起始 | R388 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 387 | 388 |
| type_round | 79 | 80 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 323 | 324 |
| last_updated_round | 387 | 388 |

## 遗留问题

1. **character 页数 77**：本轮 +1（tartlet）。queue(character) 3→**2**（建序 112 消费）。registry 全库 **1601**，unknown 0。
2. **下轮 R388 = NEW1（§3(7)）**：since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 113（horatia-bluett，book The Adventures of a Special Correspondent，pn_anchor ASC-004，role supporting）。**下次 EVV5 于 R393 起始达 since_evv5=10。**
3. **第十二批剩 2 候选（建序 113-114）**：horatia-bluett/zinca-klork。R388-R389 NEW1 消费；建序 114 消费后（R389 末）queue 归 0 → R390 SCN28-zombie 补第十三批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。GM 新簇 tartlet 暂无兄弟页可回链（godfrey/kolderup 未建）。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=323→324（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
