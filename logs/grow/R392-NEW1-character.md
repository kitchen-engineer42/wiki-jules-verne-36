---
round: 392
date: 2026-07-19
type_round: 84
phase: "2.1"
current_type: character
gene: NEW1
pages: [sergeant-long]
result: success
---

# GROW 2.1-B · R392 · NEW1 · character — 建 Sergeant Long（The Fur Country Jaspar Hobson 之坚毅军士副手、绝对服从之模范士兵；FC 簇补 lieutenant-hobson/paulina-barnett，第十三批建序 116，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 66 建（type_round 84），消费 R390 第十三批 discover 队列**建序 116**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 117 待 R394；R393 EVV5 间隔）。**

**Sergeant Long**（*The Fur Country*）——Hudson's Bay Company 北极探险队之军士、Jaspar Hobson 最倚重之副手。列名出征之伍「Lieutenant Jaspar Hobson, Sergeant Long, Corporal and Mrs Joliffe」（FC-001-023），officer 与 soldier 相映「if the lieutenant was the type of a good officer, Sergeant Long was that of a good soldier」（FC-001-025）。为 Hobson 行军常询之参谋——「after consulting with Sergeant Long, gave the order to halt」（FC-007-033）、「after consulting with Sergeant Long, Lieutenant Hobson decided to give his party a day's rest here」（FC-011-003）。绝对服从——闻不可能之命唯答「I should come back」（FC-005-021）；静时善渔「Sergeant Long was a first-rate angler」（FC-014-019）；临险以他人有室、自请为先「the Sergeant reminded the other two that they were married, and insisted upon being the first」（FC-021-039），旋「rushed out without a moment's hesitation, dragging the cord behind him」（FC-021-045）。Hobson 珍之「Ah, Sergeant Long, I know if I gave you an impossible order---」（FC-005-016），遣其独领一队「none but Sergeant Long could be appointed to the command」惟「the faithful fellow would rather not have been separated from his Lieutenant」（FC-023-033），终「the Sergeant submitted with military obedience」（FC-023-034）。北行与 Paulina Barnett 同途「Jaspar Hobson and Sergeant Long went first; then Mrs Paulina Barnett and Madge」（FC-005-009），初由 Craventy 差遣「Sergeant Long, go and see what is the matter」（FC-002-054）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-001、affiliation 空、**label=Sergeant Long，aliases=[]**。

**13 distinct solid PN**（FC-001-023/025、002-054、005-009/016/021、007-033、011-003、014-019、021-039/045、023-033/034）：均 solid，逾门。

**查重**：exact-slug sergeant-long filesystem test -f ABSENT（bucket se）+ registry entity/label（Sergeant Long）ABSENT（R390 discover 已验，本轮建前复验一致）。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Jaspar Hobson]]（character→lieutenant-hobson，存，FC-005-016）/ [[Paulina Barnett]]（character→paulina-barnett，存，FC-005-009）/ [[The Fur Country]]（work，存，FC-002-054）——三链互链无悬挂（label→slug 经 alias_index 解析）。Madge/Craventy/Felton 正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 80→**81**，registry total 1604→**1605**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 1）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1<10、queue=2>0 → NEW1 消费建序 116。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| sergeant-long | DCwNvM | The Fur Country | supporting | FC-001 | 13 distinct | 军士副手-good soldier-Hobson 参谋-绝对服从-善渔-临险自请为先-无畏冲锋-Hobson 珍之-独领一队而不愿离-军令服从-与 Barnett 同途-Craventy 差遣；label Sergeant Long + aliases 空；FC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Jaspar Hobson]]/[[Paulina Barnett]]/[[The Fur Country]] |

- **sergeant-long**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev DCwNvM（size 2517）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Sergeant Long 军士-参谋-服从-勇武-忠 Hobson 因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1605 character 81 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Sergeant Long 唯一）。✔
- **wikilink 完整性**：Jaspar Hobson / Paulina Barnett / The Fur Country 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R393 起始计数）

| 字段 | R392 起始 | R393 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 392 | 393 |
| type_round | 84 | 85 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 328 | 329 |
| last_updated_round | 392 | 393 |

## 遗留问题

1. **character 页数 81**：本轮 +1（sergeant-long）。queue(character) 2→**1**（建序 116 消费）。registry 全库 **1605**，unknown 0。
2. **下轮 R393 = EVV5（§3(1b)）**：since_evv5=9→本轮末 R393 起始达 **10** → §3(1b) EVV5 触发（since_discover=2<10 → 非 §3(1a) 合并）。EVV5 为 schema-reflection 轮，pages:[]，仅 G4，**不消费 queue**，扫全 character 页 3 结构指标 + 2 内容债。EVV5 后 since_evv5 归 0。
3. **第十三批余 1 候选（建序 117）**：william-kolderup，R394 NEW1 消费（R393 EVV5 间隔）→ queue 归 0 → R395 SCN28-zombie 补第十四批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + lieutenant-hobson/paulina-barnett→Sergeant Long、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan、tartlet→Carefinotu。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill；R393 EVV5 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=328→329（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
