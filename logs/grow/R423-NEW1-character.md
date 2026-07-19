---
round: 423
date: 2026-07-19
type_round: 115
phase: "2.1"
current_type: character
gene: NEW1
pages: [shandon]
result: success
---

# GROW 2.1-B · R423 · NEW1 · character — 建 Richard Shandon（The Adventures of Captain Hatteras 之 Forward 号大副兼受命指挥官，招募船员而不知船长身份、徒盼得指挥权的利物浦航海家；补 ACH 簇，消费第二十批建序 137，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 87 建（type_round 115），消费 R421 第二十批 discover 队列**建序 137**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 138 lady-helena）。补 ACH 簇。**

**Richard Shandon**（*The Adventures of Captain Hatteras*）——Forward 号之大副兼受命指挥官、招募船员而不知船长身份、徒盼得指挥权的利物浦航海家。报载具名「the brig Forward, Captain K. Z----, Richard Shandon mate, will start from New Prince's Docks for an unknown destination」（ACH-001-002），久历北海之良手「Richard Shandon was a good sailor; he had been commander of whalers in the Arctic seas for many years, and had a wide reputation for skill」（ACH-003-002）。受神秘之函于八月前（ACH-002-002），依船长所定条件招募船员「Shandon set about recruiting his crew upon the conditions of family and health exacted by the captain」（ACH-003-006）。非彼则无人肯从「if it hadn't been for that, Richard Shandon wouldn't have found a soul to go with him」（ACH-001-018），暂摄船长之位「the captain is Richard Shandon till another comes」（ACH-003-021）。奉命纳医「may introduce himself to the commander, Richard Shandon, who has received orders concerning him」（ACH-003-042），然真船长之信物碎其望「vexed Shandon, and took away all chance of the chief command」（ACH-004-004），忧望人群欲窥命途（ACH-004-030）。壮年之勇「a bachelor of forty, robust, energetic, and brave... confidence, vigour, and sang-froid」（ACH-003-005），私心冀掌兵「Richard Shandon, in his secret heart, hoped that the command would remain with him」（ACH-003-022），复为智者所正「you are mistaken, Shandon... the captain will allow me to tell you」（ACH-013-021）。

**role=supporting**。book='The Adventures of Captain Hatteras'、first_appearance=ACH-001、affiliation 空、**label=Richard Shandon，aliases=['Shandon']**。

**12 distinct solid PN**（ACH-001-002/018、002-002、003-002/005/006/021/022/042、004-004/030、013-021）：均 solid，逾门。「Shandon」ACH 内单指本人（大副 Richard Shandon）；无消歧冲突。

**查重**：exact-slug shandon filesystem test -f ABSENT（bucket sh）+ registry entity/label/alias 复验——「Richard Shandon / shandon」无既建人物页，无冲突。

**ACH 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Captain Hatteras]]（captain-hatteras，既建，ACH-004-004）、[[Dr Clawbonny]]（clawbonny，R422 既建，ACH-013-021）、[[The Adventures of Captain Hatteras]]（work，存，ACH-003-021）——三链均无悬挂。**Johnson 页未建**：正文以 PN-grounded 行内文字呈现（ACH-003-006），未设悬挂链。**ACH 簇再拓**（shandon 补 clawbonny/captain-hatteras，Forward 北极远征簇共 3 页）。

prose-gate：add_page 初稿 1 超段（462，纳医-碎望-窥命途三引合段）→ 拆为两段（奉命纳医 / 信物碎望），复核 0 over-400。**引注**：strict 首验即通过。quality featured 回填。

character 计数 101→**102**，registry total 1625→**1626**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 137。消费后 queue=1 → R424 继续 NEW1（建序 138 lady-helena）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| shandon | peDsO0 | The Adventures of Captain Hatteras | supporting | ACH-001 | 12 distinct | 报载具名-北海良手-受神秘函-依令招募-非彼无从-暂摄船长-奉命纳医-信物碎望-壮年之勇-私冀掌兵-为智者正；label Richard Shandon / alias Shandon；ACH 3-char 无 Note；1 超段拆解后 0 over-400；strict 首验通过；三链 [[Captain Hatteras]]/[[Dr Clawbonny]]/[[The Adventures of Captain Hatteras]]；Johnson 行内文字 |

- **shandon**：12 distinct solid PN；aliases ['Shandon']；character-schema 五 H2。add_page rev peDsO0（size 2920）。quality featured 回填。pn_validator --mode strict ✓。**ACH 簇再拓；Shandon 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Shandon 大副-招募-暂摄-碎望因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 1 超门（462）→ 拆解后 0（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号）；role=supporting ∈ enum；ACH 3-char 无 Note。✔
- **registry 一致**：total 1626 character 102 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Captain Hatteras + Dr Clawbonny + The Adventures of Captain Hatteras 三链存在无悬挂；Johnson 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R424 起始计数）

| 字段 | R423 起始 | R424 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 423 | 424 |
| type_round | 115 | 116 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 359 | 360 |
| last_updated_round | 423 | 424 |

## 遗留问题

1. **character 页数 102**：本轮 +1（shandon）。queue(character) 2→**1**（建序 137 消费）。registry 全库 **1626**，unknown 0。
2. **下轮 R424 = NEW1（§3(7)）**：since_evv5=8<10；queue=1>0 且 since_discover=2<10 → NEW1，消费建序 138 **lady-helena**（SC Glenarvan 贤妻、力主搜救之 Duncan 女主人，274 mentions，首现 SC-001；配对 [[Lord Glenarvan]]/[[Mary Grant]]/[[John Mangles]]）。**消费后 queue=0 → R425 SCN28-zombie 补第二十一批。**
3. **第二十批消费进度**：R422 NEW1（136 clawbonny ✓）→ R423 NEW1（137 shandon ✓）→ R424 NEW1（138 lady-helena 待）→ queue 归 0 → R425 SCN28-zombie 补第二十一批。**EVV5 时点**：since_evv5 R424 起始=8 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 簇再拓**（shandon→captain-hatteras/clawbonny 反向、clawbonny→shandon 反向待回填、Johnson 待建）；lady-helena 待建、SC 簇（lady-helena→glenarvan/john-mangles/mary-grant/robert-grant/mcnabbs/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=359→360（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
