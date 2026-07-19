---
round: 427
date: 2026-07-19
type_round: 119
phase: "2.1"
current_type: character
gene: NEW1
pages: [johnson]
result: success
---

# GROW 2.1-B · R427 · NEW1 · character — 建 Johnson（The Adventures of Captain Hatteras 之 Forward 号老水手长、历北极风霜之忠仆水手；补 ACH 簇，消费第二十一批建序 139，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 89 建（type_round 119），消费 R425 第二十一批 discover 队列**建序 139（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 140-141 altamont/olbinett）。补 ACH 簇。**

**Johnson**（*The Adventures of Captain Hatteras*）——Forward 号之老水手长、历北极风霜之忠仆水手、Hatteras 远征之定海砥柱。受 Shandon 招为水手长「Shandon told him and Johnson (whom he engaged as boatswain) all he knew about the business」（ACH-003-006），价值可贵而谙高纬航行「a valuable acquisition; he understood the navigation of these high latitudes」（ACH-003-014），启航前即为船况进言（ACH-001-049）。启程之际进谏指挥官「if you will allow me to advise you, you will prepare everything to start」（ACH-004-026），北冰洋老手「an old stager in the Arctic Ocean, and had nothing to learn either in audacity or sang-froid」（ACH-005-041）。哗变则助复秩序「Johnson and Bell disarmed Pen, who no longer made any resistance, and placed him in the hold」（ACH-022-021），治军严明「a very strict observer of discipline」（ACH-009-064），本性唯以听命「a sailor who only cares to obey」（ACH-018-028）。耐寒取薪生火「Johnson went to fetch some lumps of the new fuel... and soon obtained enough heat」（ACH-027-002），揉雪救冻「by dint of shaking and rubbing him with snow, he succeeded」（ACH-033-051），冰天护犬入舍（ACH-036-002）。

**role=supporting**。book='The Adventures of Captain Hatteras'、first_appearance=ACH-001、affiliation 空、**label=Johnson，aliases=[]**。

**15 distinct solid PN**（ACH-001-049、003-006/014、004-026、005-041、007-004、009-064、018-028、022-021、027-002、028-006、033-051/073、034-023、036-002）：均 solid，逾门。「Johnson」ACH 内单指本人（水手长 Johnson）；无消歧冲突。

**查重**：exact-slug johnson filesystem test -f ABSENT（bucket jo）+ registry entity/label/alias 复验（Python 精确）——「Johnson / johnson」无既建人物页，无冲突。

**ACH 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Captain Hatteras]]（captain-hatteras，既建，ACH-028-006）、[[Dr Clawbonny]]（clawbonny，R422 既建，ACH-007-004）、[[Richard Shandon]]（shandon，R423 既建，ACH-003-006）、[[The Adventures of Captain Hatteras]]（work，存，ACH-034-023）——四链均无悬挂。**Bell/Simpson/Pen 页未建**：正文以 PN-grounded 行内文字呈现（Bell ACH-022-021、Pen ACH-022-021），未设悬挂链。**ACH 簇再拓**（johnson 补 captain-hatteras/clawbonny/shandon，Forward 北极远征簇共 4 页）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 103→**104**，registry total 1627→**1628**，unknown 恒 0。build_registry 2 known parked HK(e) alias warn（Hector Servadac、Robur the Conqueror，均既存全局非本轮引入）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 139。消费后 queue=2 → R428 继续 NEW1（建序 140 altamont）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| johnson | 6kLP4h | The Adventures of Captain Hatteras | supporting | ACH-001 | 15 distinct | 受招水手长-谙高纬航行-进谏指挥官-北冰洋老手-助平哗变-治军严明-唯以听命-耐寒取薪-揉雪救冻-护犬入舍；label Johnson / alias []；ACH 3-char 无 Note；0 超段直建；strict 首验通过；四链 [[Captain Hatteras]]/[[Dr Clawbonny]]/[[Richard Shandon]]/[[The Adventures of Captain Hatteras]]；Bell/Pen 行内文字 |

- **johnson**：15 distinct solid PN；aliases []；character-schema 五 H2。add_page rev 6kLP4h（size 2715）。quality featured 回填。pn_validator --mode strict ✓。**ACH 簇再拓；Johnson 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Johnson 水手长-招募-进谏-平乱-耐寒因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：15 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号）；role=supporting ∈ enum；ACH 3-char 无 Note。✔
- **registry 一致**：total 1628 character 104 unknown 0（2 known parked HK(e) alias warn，非本轮引入）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Captain Hatteras + Dr Clawbonny + Richard Shandon + The Adventures of Captain Hatteras 四链存在无悬挂；Bell/Pen 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R428 起始计数）

| 字段 | R427 起始 | R428 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 427 | 428 |
| type_round | 119 | 120 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 363 | 364 |
| last_updated_round | 427 | 428 |

## 遗留问题

1. **character 页数 104**：本轮 +1（johnson）。queue(character) 3→**2**（建序 139 消费）。registry 全库 **1628**，unknown 0。
2. **下轮 R428 = NEW1（§3(7)）**：since_evv5=1<10；queue=2>0 且 since_discover=2<10 → NEW1，消费建序 140 **altamont**（ACH Porpoise 号美国船长、冰原获救而与 Hatteras 争北极优先权，224 mentions，首现 ACH-032；配对 [[Captain Hatteras]]/[[Dr Clawbonny]]/[[Johnson]]）。
3. **第二十一批消费进度**：R427 NEW1（139 johnson ✓）→ R428 NEW1（140 altamont 待）→ R429 NEW1（141 olbinett 待）→ queue 归 0 → R430 SCN28-zombie 补第二十二批。**EVV5 时点**：since_evv5 R428 起始=1，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 簇再拓**（johnson→captain-hatteras/clawbonny/shandon 反向、altamont 待建、Bell/Simpson/Pen/Wilson 待建）、SC 簇（olbinett 待建、lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=363→364（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
