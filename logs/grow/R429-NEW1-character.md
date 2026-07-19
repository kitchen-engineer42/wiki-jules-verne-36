---
round: 429
date: 2026-07-19
type_round: 121
phase: "2.1"
current_type: character
gene: NEW1
pages: [olbinett]
result: success
---

# GROW 2.1-B · R429 · NEW1 · character — 建 Olbinett（In Search of the Castaways 之 Duncan 号司膳管事、随陆行搜救队之膳役；补 SC 簇，消费第二十一批建序 141，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 91 建（type_round 121），消费 R425 第二十一批 discover 队列**建序 141（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=3<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R430 SCN28-zombie 补第二十二批。补 SC 簇。**

**Olbinett**（*In Search of the Castaways*）——Duncan 号之司膳管事、随 Glenarvan 陆行搜救队之膳役。游艇司膳「M. Olbinett, the steward, who could only acknowledge so polite an attention by announcing that breakfast was ready」（SC-027-007），携行军炊具「M. Olbinett's portable kitchen」（SC-034-024）。以膳为职，研图碍其铺席「to the great annoyance of M. Olbinett, who could never get the cloth laid for meals」（SC-009-006），扎营即备晚膳「the tent was pitched, and Olbinett got the supper ready」（SC-038-033），一度技惊四座（SC-036-024），让舱以待宾客（SC-028-003）。不喜乘骑而挤身行李间（SC-034-025），荒野持重如在城堡「with as much dignity as if he was in Malcolm Castle」（SC-058-094），遇袭亦赴共御「Olbinett rushed to the common defense」（SC-043-005），炭火巧炊野鸨之卵（SC-045-034）。

**role=supporting**。book='In Search of the Castaways'、first_appearance=SC-006、affiliation 空、**label=Olbinett，aliases=[]**。

**14 distinct solid PN**（SC-006-026/060、009-006、027-007、028-003、034-024/025、036-024、038-033、042-033、043-005、045-034、050-004、058-094）：均 solid，逾门。「Olbinett」SC 内单指本人（Duncan 司膳）；无消歧冲突。

**查重**：exact-slug olbinett filesystem test -f ABSENT（bucket ol）+ registry entity/label/alias 复验（Python 精确）——「Olbinett / olbinett」无既建人物页，无冲突。

**SC 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Lord Glenarvan]]（glenarvan，既建，SC-006-026）、[[Lady Helena Glenarvan]]（lady-helena，R424 既建，SC-042-033）、[[John Mangles]]（john-mangles，既建，SC-006-060）、[[In Search of the Castaways]]（work，存，SC-050-004）——四链均无悬挂（labels 经 registry 复核：Lord Glenarvan / Lady Helena Glenarvan / John Mangles）。**SC 簇再拓**（olbinett 补 glenarvan/lady-helena/john-mangles，Duncan 搜救簇）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 105→**106**，registry total 1629→**1630**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 141。消费后 queue=0 → R430 SCN28-zombie 补第二十二批。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| olbinett | KvPBAJ | In Search of the Castaways | supporting | SC-006 | 14 distinct | 游艇司膳-携行军炊具-研图碍铺席-扎营备膳-技惊四座-让舱待宾-不喜乘骑-荒野持重-遇袭共御-炭火巧炊；label Olbinett / alias []；SC 3-char 无 Note；0 超段直建；strict 首验通过；四链 [[Lord Glenarvan]]/[[Lady Helena Glenarvan]]/[[John Mangles]]/[[In Search of the Castaways]] |

- **olbinett**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev KvPBAJ（size 2422）。quality featured 回填。pn_validator --mode strict ✓。**SC 簇再拓；Olbinett 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Olbinett 司膳-备膳-御敌因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；SC 3-char 无 Note。✔
- **registry 一致**：total 1630 character 106 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Lord Glenarvan + Lady Helena Glenarvan + John Mangles + In Search of the Castaways 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R430 起始计数）

| 字段 | R429 起始 | R430 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 429 | 430 |
| type_round | 121 | 122 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 365 | 366 |
| last_updated_round | 429 | 430 |

## 遗留问题

1. **character 页数 106**：本轮 +1（olbinett）。queue(character) 1→**0**（建序 141 消费，第二十一批全数消费完毕）。registry 全库 **1630**，unknown 0。
2. **下轮 R430 = SCN28-zombie（§3(4)）**：queue(character)==0 → SCN28-zombie 补第二十二批 discover 候选（≥3 grounded+dup-checked），since_discover 归零。since_evv5=3<10。
3. **第二十一批消费完结**：R427 NEW1（139 johnson ✓）→ R428 NEW1（140 altamont ✓）→ R429 NEW1（141 olbinett ✓）→ queue 归 0 → R430 SCN28-zombie 补第二十二批。**EVV5 时点**：since_evv5 R430 起始=3，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**SC 簇再拓**（olbinett→glenarvan/lady-helena/john-mangles 反向、lady-helena→glenarvan/mary-grant/mcnabbs 反向、robert-grant/thalcave/paganel 反向）、**ACH 簇**（altamont→captain-hatteras/clawbonny/johnson 反向、johnson→captain-hatteras/clawbonny/shandon 反向、Bell/Simpson/Pen/Wilson 待建）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=365→366（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
