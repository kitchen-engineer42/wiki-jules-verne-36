---
round: 391
date: 2026-07-19
type_round: 83
phase: "2.1"
current_type: character
gene: NEW1
pages: [carefinotu]
result: success
---

# GROW 2.1-B · R391 · NEW1 · character — 建 Carefinotu（Godfrey Morgan 荒岛忠仆、Godfrey 之「星期五」、以火脱险的黑人，终揭为忠仆 Jup Brass 扮演；GM 簇补 tartlet，第十三批建序 115，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 65 建（type_round 83），消费 R390 第十三批 discover 队列**建序 115（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 116-117 待 R392/R394）。**

**Carefinotu**（*Godfrey Morgan*）——荒岛救起之黑人忠仆、Godfrey 之「星期五」，初现如未开化野人「fire itself seemed to be unknown to him」（GM-018-036），其名之正当性亦见疑「Is he to be allowed to call himself Carefinotu?」（GM-018-007）。依附 Godfrey 为伴、屡随狩猎「Carefinotu many times accompanied Godfrey on his shooting excursions」（GM-018-051），夜守自任 Will Tree 卫士、为救命恩人「of service to his liberators」（GM-019-012）。慕白人之械「the weapons carried by Godfrey and Tartlet」（GM-018-025），唯不习英语「refractoriness」（GM-018-052），然勇武绝伦——搏虎扼喉、一刃穿心「holding him by the throat, and at last stabbing him to the heart」（GM-019-059），护 Godfrey 避蛇「threw himself between Godfrey and the reptile」（GM-020-081），Godfrey 病愈「mainly owed his return to health」赖之（GM-021-008），扶 Tartlet 脱险「rushed towards Tartlet and lifted him up」（GM-020-094）。高潮反转：忽操英语「in that English language which up to then he had seemed unable to speak」（GM-021-106），Uncle Will 揭其真身「Carefinotu was my faithful Jup Brass, who played his part of Friday marvellously well」（GM-022-030）；末围之战守交叉火力位「whence he could deliver a cross fire」（GM-021-085）。

**role=supporting**。book='Godfrey Morgan'、first_appearance=GM-018、affiliation 空、**label=Carefinotu，aliases=[]**（Jup Brass 系其真名，正文交代，未入 alias 避冲突）。

**13 distinct solid PN**（GM-018-007/025/036/051/052、019-012/059、020-081/094、021-008/085/106、022-030）：均 solid，逾门。

**查重**：exact-slug carefinotu filesystem test -f ABSENT（bucket ca）+ registry entity/label（Carefinotu）ABSENT（R390 discover 已验，本轮建前复验一致）。

**GM 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Tartlet]]（character，R387 建，GM-020-094）/ [[Godfrey Morgan]]（work，存，GM-021-106）——二链互链无悬挂。Godfrey（角色页未建）、Uncle Will/Kolderup（william-kolderup 待 R394）均以正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 79→**80**，registry total 1603→**1604**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0<10、queue=3>0 → NEW1 消费建序 115。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| carefinotu | w5Ehqs | Godfrey Morgan | supporting | GM-018 | 13 distinct | 荒岛忠仆-星期五-初现野人-依附 Godfrey-Will Tree 卫士-慕械-不习英语-搏虎穿心-护主避蛇-助其病愈-扶 Tartlet-高潮忽操英语-揭为 Jup Brass-末围交叉火力；label Carefinotu + aliases 空；GM 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Tartlet]]/[[Godfrey Morgan]] |

- **carefinotu**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev w5Ehqs（size 2642）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Carefinotu 野人-忠仆-卫士-勇武-护主-反转因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；GM 2-char 无 Note。✔
- **registry 一致**：total 1604 character 80 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Carefinotu 唯一）。✔
- **wikilink 完整性**：Tartlet / Godfrey Morgan 二链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R392 起始计数）

| 字段 | R391 起始 | R392 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 391 | 392 |
| type_round | 83 | 84 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 327 | 328 |
| last_updated_round | 391 | 392 |

## 遗留问题

1. **character 页数 80**：本轮 +1（carefinotu）。queue(character) 3→**2**（建序 115 消费）。registry 全库 **1604**，unknown 0。
2. **下轮 R392 = NEW1（§3(7)）**：since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 116（sergeant-long，book The Fur Country，pn_anchor FC-001，role supporting）。**下次 EVV5 于 R393 起始达 since_evv5=10（§3(1b)）——即 R392 NEW1（sergeant-long）→ R393 EVV5（不消费）→ R394 NEW1（william-kolderup）→ queue 归 0 → R395 SCN28-zombie。**
3. **第十三批余 2 候选（建序 116-117）**：sergeant-long（R392）/william-kolderup（R394），R393 EVV5 间隔。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。tartlet 可回链 Carefinotu。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=327→328（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
