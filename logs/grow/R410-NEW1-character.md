---
round: 410
date: 2026-07-19
type_round: 102
phase: "2.1"
current_type: character
gene: NEW1
pages: [sabine]
result: success
---

# GROW 2.1-B · R410 · NEW1 · character — 建 Sabine（The Fur Country 之加拿大猎人、Fort Hope 觅食队主力射手，善辞令之神射手；FC 簇第八页，第十七批建序 128，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 78 建（type_round 102），消费 R408 第十七批 discover 队列**建序 128**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1**（建序 129 待 R411 消费）。

**Sabine**（*The Fur Country*）——探险队之加拿大猎人、Fort Hope 觅食队主力射手、善辞令之神射手。首席猎手「the chief hunters of the expedition were the soldiers Marbre and Sabine, both very expert at their business」（FC-006-024），技艺娴熟「two--Marbre and Sabine--were skilful hunters」（FC-013-004），善用诡术「skilled in all the artifices which sportsmen employ in stalking their prey」（FC-014-014），剥皮而归「Marbre and Sabine taking immediate possession, carried off their skins」（FC-006-057），四季供给「Sabine and Marbre killed a good many Polar hares」（FC-020-002），长官所倚「consulted...Marbre, and Sabine, in whom he had great confidence」（FC-043-030）。自矜辞令「in his usual sententious manner...delighted with the elegant way in which he had rounded his sentence」（FC-014-026），言辞生动「to let them 'ripen,' or...to wait for the cold to bleach them」（FC-016-017），苦中作乐「bears' steaks are as good as reindeers', and we get the fur in!」（FC-019-012），较真于猎「beside himself with rage...subterfuge was unworthy of a respectable fox」（FC-019-015），自信不疑「no, no, sir; Marbre and I are not mistaken」（FC-006-032）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-006、affiliation 空、**label=Sabine，aliases=[]**。

**14 distinct solid PN**（FC-006-024/032/057、011-019、013-004、014-014/026、016-017/020、019-012/015、020-002、043-011/030）：均 solid，逾门。「Sabine」FC 内单指本人（探险队猎人）；「Marbre and Sabine」并称句取其明指 Sabine 属性/言行者。

**查重**：exact-slug sabine filesystem test -f ABSENT（bucket sa）+ registry entity/label/alias 复验——「Sabine」无既建人物页，无冲突。

**FC 2-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Jaspar Hobson]]（lieutenant-hobson，既建）、[[The Fur Country]]（work，存）——均无悬挂。**Marbre 页未建**：Relationships bullet 以正文明指之 plain-text（PN grounded FC-016-020，不设悬挂链）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 92→**93**，registry total 1616→**1617**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 128。消费后 queue=1，R411 消费 129。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| sabine | qWO9Be | The Fur Country | supporting | FC-006 | 14 distinct | 首席猎手-技艺娴熟-善用诡术-剥皮而归-四季供给-长官所倚-自矜辞令-言辞生动-苦中作乐-较真于猎-自信不疑；label Sabine；FC 2-char 无 Note；0 超段直建；strict 首验通过；双链 [[Jaspar Hobson]]/[[The Fur Country]]（Marbre 未建作 plain-text）|

- **sabine**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev qWO9Be（size 2652）。quality featured 回填。pn_validator --mode strict ✓。**FC 簇第八页；Marbre 并称句消歧取明指 Sabine 者。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Sabine 猎手-辞令-较真因果；「Marbre and Sabine」并称句取明指 Sabine 属性/言行者；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1617 character 93 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Jaspar Hobson + The Fur Country 双链存在无悬挂；Marbre 未建作 plain-text 不悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R411 起始计数）

| 字段 | R410 起始 | R411 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 410 | 411 |
| type_round | 102 | 103 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 346 | 347 |
| last_updated_round | 410 | 411 |

## 遗留问题

1. **character 页数 93**：本轮 +1（sabine）。queue(character) 2→**1**（建序 128 消费）。registry 全库 **1617**，unknown 0。
2. **下轮 R411 = NEW1（§3(7)）**：since_evv5=6<10；queue=1>0 且 since_discover=2<10 → NEW1，消费建序 129 **fridrikssen**（JCE，JCE-009，supporting，20 mentions；Reykjavik 博物学教授、荐 Hans 予 Lidenbrock 之雷城学者；可回链 [[Professor Lidenbrock]]/[[Axel]]/[[Hans Bjelke]]）。**消费后 queue=0 → R412 SCN28-zombie 补第十八批。**
3. **第十七批消费**：R409 NEW1（127 joe ✓）→ R410 NEW1（128 sabine ✓）→ R411 NEW1（129 fridrikssen）→ queue 归 0 → R412 SCN28-zombie。**EVV5 时点**：since_evv5 R411 起始=6 → R415 起始=10 → **R415 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：Marbre 待建、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R415 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=346→347（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
