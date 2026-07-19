---
round: 394
date: 2026-07-19
type_round: 86
phase: "2.1"
current_type: character
gene: NEW1
pages: [william-kolderup]
result: success
---

# GROW 2.1-B · R394 · NEW1 · character — 建 William W. Kolderup（Godfrey Morgan 旧金山巨贾叔父兼监护人、幕后策划侄儿荒岛骗局之纳博布；GM 簇补 tartlet/carefinotu，第十三批建序 117 末候选，消费后 queue 归 0）

## 执行摘要

Phase 2.1-B character 第 67 建（type_round 86），消费 R390 第十三批 discover 队列**建序 117（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → 下轮 R395 = §3(4) SCN28-zombie 补第十四批。**

**William W. Kolderup**（*Godfrey Morgan*）——旧金山巨贾、Godfrey 之叔父兼监护人、幕后策划整场荒岛骗局之纳博布。初现「It was William W. Kolderup, of San Francisco」（GM-001-053），富可敌国「a man extraordinarily rich, who counted dollars by the million as other men do by the thousand」（GM-002-002），商网遍球「2000 branch offices scattered」（GM-002-006）。拍卖场意志必胜——「Spencer Island fell for four millions of dollars to William W. Kolderup」（GM-002-081）。幕后导演侄儿全部磨难——「the Dream was quietly sunk by means of her water ballast, according to the instructions I had given」（GM-022-022），伪野人「stuffed with straw, and landed before you saw them with Jup Brass and his companions」（GM-022-032），然真险几败其局「without the arrival of William W. Kolderup」castaways 几为寒冬猛兽所毁（GM-022-064）。挚爱关系：侄儿 Godfrey「his uncle was thinking of binding」于婚约（GM-003-030），教女 Phina「Phina Hollaney was the goddaughter of William W. Kolderup」（GM-003-014）、成其所愿「William W. Kolderup desired」之婚（GM-003-025），雇伶 Jup Brass/Carefinotu「Yes, Mr. Kolderup」（GM-022-049）。宿敌 Taskinar「J. R. Taskinar particularly detested William W. Kolderup」（GM-002-040），终以侄儿婚礼收束「the wedding of the nephew and pupil of William W. Kolderup」（GM-022-096）。

**role=supporting**。book='Godfrey Morgan'、first_appearance=GM-001、affiliation 空、**label=William W. Kolderup，aliases=[]**（Uncle Will/Kolderup 系正文简称，未入 alias 避冲突；亦规避 HK(e) Godfrey Morgan 同名 label 风险）。

**13 distinct solid PN**（GM-001-053、002-002/006/040/081、003-014/025/030、022-022/032/049/064/096）：均 solid，逾门。

**查重**：exact-slug william-kolderup filesystem test -f ABSENT（bucket wi）+ registry entity/label（William W. Kolderup）ABSENT（R390 discover 已验，本轮建前复验一致）。

**GM 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Carefinotu]]（character，R391 建，GM-022-049）/ [[Godfrey Morgan]]（work，存，GM-022-096）——二链互链无悬挂。Godfrey（角色页未建）、Phina、J. R. Taskinar、Tartlet 均以正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 81→**82**，registry total 1605→**1606**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 1）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=3<10、queue=1>0 → NEW1 消费建序 117。消费后 queue=0 → 下轮 SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| william-kolderup | GQRAVE | Godfrey Morgan | supporting | GM-001 | 13 distinct | 旧金山巨贾-叔父监护人-富可敌国-商网遍球-拍卖必胜-幕后导演荒岛骗局-伪野人-真险几败其局-侄 Godfrey 婚约-教女 Phina-雇伶 Jup Brass-宿敌 Taskinar-侄儿婚礼收束；label William W. Kolderup + aliases 空；GM 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Carefinotu]]/[[Godfrey Morgan]] |

- **william-kolderup**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev GQRAVE（size 2306）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Kolderup 巨贾-监护-导演骗局-亲缘-宿敌因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；GM 2-char 无 Note。✔
- **registry 一致**：total 1606 character 82 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label William W. Kolderup 唯一；未与 work「Godfrey Morgan」撞名）。✔
- **wikilink 完整性**：Carefinotu / Godfrey Morgan 二链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R395 起始计数）

| 字段 | R394 起始 | R395 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 394 | 395 |
| type_round | 86 | 87 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 330 | 331 |
| last_updated_round | 394 | 395 |

## 遗留问题

1. **character 页数 82**：本轮 +1（william-kolderup）。queue(character) 1→**0**（建序 117 消费，第十三批全数消费完毕）。registry 全库 **1606**，unknown 0。
2. **下轮 R395 = SCN28-zombie（§3(4)）**：since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**。补第十四批候选（pages:[]，仅 G4，since_discover 归零）。**下次 EVV5 于 R403 起始达 since_evv5=10。**
3. **第十四批 discover（R395）**：queue 归 0，需补 ≥3 grounded+dup-checked 候选。GM 簇近饱和（tartlet/carefinotu/william-kolderup 已建，Godfrey/Phina/Taskinar 为候选但 Godfrey 触 HK(e) 同名风险）；FC 簇（sergeant-long/lieutenant-hobson/paulina-barnett 已建，Marbre/Sabine/Mac-Nab/Thomas Black 可挖）；或跨作品拓展。filesystem+registry alias 并查。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=330→331（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
