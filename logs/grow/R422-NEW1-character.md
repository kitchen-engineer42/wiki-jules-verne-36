---
round: 422
date: 2026-07-19
type_round: 114
phase: "2.1"
current_type: character
gene: NEW1
pages: [clawbonny]
result: success
---

# GROW 2.1-B · R422 · NEW1 · character — 建 Dr Clawbonny（The Adventures of Captain Hatteras 之 Forward 号博学随船医生、Hatteras 北极远征之百科式伙伴；开 ACH 新簇，消费第二十批建序 136，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 86 建（type_round 114），消费 R421 第二十批 discover 队列**建序 136（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 137-138 shandon/lady-helena）。开 ACH 新簇。**

**Dr Clawbonny**（*The Adventures of Captain Hatteras*）——Forward 号之博学好脾气随船医生、Hatteras 北极远征之百科全书式伙伴。良医而少诊「Dr. Clawbonny was a doctor, and a good one, though practising little」（ACH-003-054），得其所哉据舱「taken possession of his cabin on the 6th of February, the day after the Forward was launched」（ACH-004-004），舱居船尾（ACH-004-003）。应命自荐于指挥官「if Dr. Clawbonny wishes to embark on board the Forward for a long cruise, he may introduce himself to the commander, Richard Shandon」（ACH-003-042），去函求随于素昧之 John Hatteras「entered into correspondence with John Hatteras, whom he did not know, requesting to join the expedition」（ACH-012-058）。急盼启航「up and down in agitation, looking through his telescope, gesticulating, impatient for the sea」（ACH-004-031）。陆行北极四人组「Hatteras, Clawbonny, Bell, and Simpson, and seven dogs」（ACH-028-013），冻鼻几失赖 Johnson 揉救（ACH-030-015）。博识释奇「scientific men, and Dr. Clawbonny amongst them, explain the fact」（ACH-024-002），水手叩问天象（ACH-008-083），恒以乐观自持「In the long run depicts Dr. Clawbonny in a single phrase」（ACH-010-007），仁心可驯虎「whose kindness and caresses would have tamed a tiger」（ACH-004-007），好学采知于老海员（ACH-007-003）。

**role=supporting**。book='The Adventures of Captain Hatteras'、first_appearance=ACH-002、affiliation 空、**label=Dr Clawbonny，aliases=['Clawbonny']**。

**14 distinct solid PN**（ACH-003-042/054、004-003/004/007/031、007-003、008-083、010-007、012-058、013-021、024-002、028-013、030-015）：均 solid，逾门。「Clawbonny」ACH 内单指本人（随船医生）；无消歧冲突。

**查重**：exact-slug clawbonny filesystem test -f ABSENT（bucket cl）+ registry entity/label/alias 复验——「Dr Clawbonny / clawbonny」无既建人物页，无冲突。

**ACH 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Captain Hatteras]]（captain-hatteras，既建，ACH-013-021）、[[The Adventures of Captain Hatteras]]（work，存，ACH-028-013）——二链均无悬挂。**Shandon/Johnson 页未建**：正文以 PN-grounded 行内文字呈现（Richard Shandon ACH-003-042、Johnson ACH-030-015），未设悬挂链（shandon 建序 137 待建 R423）。**ACH 新簇启**（clawbonny 开 captain-hatteras，Forward 北极远征簇）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 100→**101**，registry total 1624→**1625**，unknown 恒 0。build_registry 0 alias warn（3 known parked HK 本次未复现，均既存全局非本轮引入）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 136。消费后 queue=2 → R423 继续 NEW1（建序 137 shandon）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| clawbonny | IlB6b4 | The Adventures of Captain Hatteras | supporting | ACH-002 | 14 distinct | 良医少诊-据舱船尾-应命自荐-去函求随-急盼启航-陆行四人组-冻鼻揉救-博识释奇-乐观自持-仁心驯虎-采知老海员；label Dr Clawbonny / alias Clawbonny；ACH 3-char 无 Note；0 超段直建；strict 首验通过；二链 [[Captain Hatteras]]/[[The Adventures of Captain Hatteras]]；Shandon/Johnson 行内文字 |

- **clawbonny**：14 distinct solid PN；aliases ['Clawbonny']；character-schema 五 H2。add_page rev IlB6b4（size 3044）。quality featured 回填。pn_validator --mode strict ✓。**ACH 新簇启；Clawbonny 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Clawbonny 医生-求随-博识-仁心因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（Relationships bullet 分段；awk 复核）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；ACH 3-char 无 Note。✔
- **registry 一致**：total 1625 character 101 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Captain Hatteras + The Adventures of Captain Hatteras 二链存在无悬挂；Shandon/Johnson 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R423 起始计数）

| 字段 | R422 起始 | R423 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 422 | 423 |
| type_round | 114 | 115 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 358 | 359 |
| last_updated_round | 422 | 423 |

## 遗留问题

1. **character 页数 101**：本轮 +1（clawbonny）。queue(character) 3→**2**（建序 136 消费）。registry 全库 **1625**，unknown 0。
2. **下轮 R423 = NEW1（§3(7)）**：since_evv5=7<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 137 **shandon**（ACH Forward 号大副兼受命指挥官，261 mentions，首现 ACH-001；配对 [[Captain Hatteras]]/[[Dr Clawbonny]]）。
3. **第二十批消费进度**：R422 NEW1（136 clawbonny ✓）→ R423 NEW1（137 shandon 待）→ R424 NEW1（138 lady-helena 待）→ queue 归 0 → R425 SCN28-zombie 补第二十一批。**EVV5 时点**：since_evv5 R423 起始=7 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 新簇启**（clawbonny→captain-hatteras 反向、clawbonny↔shandon 待 shandon 建后互链）；lady-helena 待建、shandon 待建、SC 簇（lady-helena→glenarvan/john-mangles/mary-grant/robert-grant/mcnabbs/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=358→359（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
