---
round: 428
date: 2026-07-19
type_round: 120
phase: "2.1"
current_type: character
gene: NEW1
pages: [altamont]
result: success
---

# GROW 2.1-B · R428 · NEW1 · character — 建 Altamont（The Adventures of Captain Hatteras 之 Porpoise 号美国船长、冰原获救而与 Hatteras 争北极优先权的探险家；补 ACH 簇，消费第二十一批建序 140，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 90 建（type_round 120），消费 R425 第二十一批 discover 队列**建序 140**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=2<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 141 olbinett）。补 ACH 簇。**

**Altamont**（*The Adventures of Captain Hatteras*）——Porpoise 号之美国船长、冰原获救而与 Hatteras 争北极优先权之探险家。失船之长「Hatteras had the men, but Altamont had the ship, and it was hard to say whose was the better right」（ACH-039-006），自矜船远「yes, my ship went further than any other has ever ventured」（ACH-037-063），其众先弃船携长艇雪橇而行（ACH-035-004）。冰上濒死获救「Altamont still lived, but he was in a state of complete insensibility」（ACH-032-040），医者以橇载之裹以帐幕而归（ACH-033-063），苏醒示其失船之数「when he got to fifteen, Altamont made a sign to stop」（ACH-034-094），继而渐复其力（ACH-039-002）。傲执其国之权「this continent belongs to me」（ACH-039-051），诘问英人可曾先美人踏此（ACH-039-055），复持救命之债相责「without me and my ship, where would you all be at this moment?」（ACH-039-049），猎中勇捷以斧毙海象（ACH-040-059）。

**role=supporting**。book='The Adventures of Captain Hatteras'、first_appearance=ACH-032、affiliation 空、**label=Altamont，aliases=[]**。

**15 distinct solid PN**（ACH-032-040、033-063、034-094、035-004、037-063/081、039-002/004/006/023/049/051/055/056、040-059）：均 solid，逾门。「Altamont」ACH 内单指本人（Porpoise 船长）；无消歧冲突。

**查重**：exact-slug altamont filesystem test -f ABSENT（bucket al）+ registry entity/label/alias 复验（Python 精确）——「Altamont / altamont」无既建人物页，无冲突（R425 discover 排除误报的 grep 子串已辨明）。

**ACH 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Captain Hatteras]]（captain-hatteras，既建，ACH-039-004）、[[Dr Clawbonny]]（clawbonny，R422 既建，ACH-039-023）、[[Johnson]]（johnson，R427 既建，ACH-039-056）、[[The Adventures of Captain Hatteras]]（work，存，ACH-037-081）——四链均无悬挂。**ACH 簇再拓**（altamont 补 captain-hatteras/clawbonny/johnson，Forward 北极远征簇共 5 页）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 104→**105**，registry total 1628→**1629**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 140。消费后 queue=1 → R429 继续 NEW1（建序 141 olbinett）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| altamont | eCLJXk | The Adventures of Captain Hatteras | supporting | ACH-032 | 15 distinct | 失船之长-自矜船远-冰上获救-橇载而归-示失船之数-渐复其力-傲执国权-诘问优先-救命相责-勇捷毙海象；label Altamont / alias []；ACH 3-char 无 Note；0 超段直建；strict 首验通过；四链 [[Captain Hatteras]]/[[Dr Clawbonny]]/[[Johnson]]/[[The Adventures of Captain Hatteras]] |

- **altamont**：15 distinct solid PN；aliases []；character-schema 五 H2。add_page rev eCLJXk（size 2463）。quality featured 回填。pn_validator --mode strict ✓。**ACH 簇再拓；Altamont 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Altamont 获救-复力-争权因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：15 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号）；role=supporting ∈ enum；ACH 3-char 无 Note。✔
- **registry 一致**：total 1629 character 105 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Captain Hatteras + Dr Clawbonny + Johnson + The Adventures of Captain Hatteras 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R429 起始计数）

| 字段 | R428 起始 | R429 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 428 | 429 |
| type_round | 120 | 121 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 364 | 365 |
| last_updated_round | 428 | 429 |

## 遗留问题

1. **character 页数 105**：本轮 +1（altamont）。queue(character) 2→**1**（建序 140 消费）。registry 全库 **1629**，unknown 0。
2. **下轮 R429 = NEW1（§3(7)）**：since_evv5=2<10；queue=1>0 且 since_discover=3<10 → NEW1，消费建序 141 **olbinett**（SC Duncan 号司膳管事、随陆行搜救队之膳役，43 mentions，首现 SC-006；配对 [[Lord Glenarvan]]/[[Lady Helena Glenarvan]]/[[Mary Grant]]）。**消费后 queue=0 → R430 SCN28-zombie 补第二十二批。**
3. **第二十一批消费进度**：R427 NEW1（139 johnson ✓）→ R428 NEW1（140 altamont ✓）→ R429 NEW1（141 olbinett 待）→ queue 归 0 → R430 SCN28-zombie 补第二十二批。**EVV5 时点**：since_evv5 R429 起始=2，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 簇再拓**（altamont→captain-hatteras/clawbonny/johnson 反向、johnson→captain-hatteras/clawbonny/shandon 反向、Bell/Simpson/Pen/Wilson 待建）、SC 簇（olbinett 待建、lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=364→365（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
