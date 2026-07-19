---
round: 431
date: 2026-07-19
type_round: 123
phase: "2.1"
current_type: character
gene: NEW1
pages: [bell]
result: success
---

# GROW 2.1-B · R431 · NEW1 · character — 建 Bell（The Adventures of Captain Hatteras 之 Forward 号木匠、Hatteras 陆行北极小队之匠人与斥候；补 ACH 簇，消费第二十二批建序 142，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 92 建（type_round 123），消费 R430 第二十二批 discover 队列**建序 142（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 143-144 harris/isaac-hakkabut）。补 ACH 簇。**

**Bell**（*The Adventures of Captain Hatteras*）——Forward 号之木匠、Hatteras 陆行北极小队之匠人与斥候。忠信可靠之匠「the harpooner, Simpson, and the carpenter, Bell, were sure men, faithful to duty and discipline」（ACH-005-041），获选陆行「Bell the carpenter and Simpson」（ACH-028-013）。哗变则助制乱首「Johnson and Bell disarmed Pen, who no longer made any resistance, and placed him in the hold」（ACH-022-021），陆行为斥候探冰「sounding the ice with his iron-tipped stick」（ACH-029-002），复筑雪屋以固之（ACH-032-008）。医者冻面之救者，掬雪力揉其面「a handful of snow, and began to rub his companion's face with all his might」（ACH-030-009），戏言「if you've got a nose left, you owe it to me」（ACH-030-013）。历冰原之苦，春时罹雪盲（ACH-010-012），料理病犬啮嚼皮具（ACH-031-013），久苦而心硬「the poor fellow's heart was hardened by his own suffering」（ACH-031-018）。

**role=supporting**。book='The Adventures of Captain Hatteras'、first_appearance=ACH-003、affiliation 空、**label=Bell，aliases=[]**。

**14 distinct solid PN**（ACH-005-041、010-012、022-021、027-010、028-013/014、029-002/025、030-009/013/016、031-013/018、032-008）：均 solid，逾门。「Bell」ACH 内 183 提及单指 Forward 木匠 Bell；SC/TTLU 各 1 处一次性同名（HK(f) 留意，非本轮阻塞），本页锚定 ACH 单一实体。

**查重**：exact-slug bell filesystem test -f ABSENT（bucket be）+ registry entity/label/alias 复验（Python 精确）——「Bell / bell」无既建人物页，无冲突。

**ACH 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Captain Hatteras]]（captain-hatteras，既建，ACH-029-025）、[[Dr Clawbonny]]（clawbonny，R422 既建，ACH-030-016）、[[Johnson]]（johnson，R427 既建，ACH-027-010）、[[The Adventures of Captain Hatteras]]（work，存，ACH-028-014）——四链均无悬挂。**Simpson/Pen 页未建**：正文以 PN-grounded 行内文字呈现（Simpson ACH-005-041/028-013、Pen ACH-022-021），未设悬挂链。**ACH 簇收束**（bell 补 captain-hatteras/clawbonny/johnson，Forward 北极远征簇共 6 页）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 106→**107**，registry total 1630→**1631**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 142。消费后 queue=2 → R432 继续 NEW1（建序 143 harris）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| bell | xmS5hl | The Adventures of Captain Hatteras | supporting | ACH-003 | 14 distinct | 忠信之匠-获选陆行-助制乱首-斥候探冰-筑雪屋-救医冻面-戏言存鼻-罹雪盲-料理病犬-久苦心硬；label Bell / alias []；ACH 183 单指木匠，SC/TTLU 同名 HK(f) 留意；ACH 3-char 无 Note；0 超段直建；strict 首验通过；四链 [[Captain Hatteras]]/[[Dr Clawbonny]]/[[Johnson]]/[[The Adventures of Captain Hatteras]]；Simpson/Pen 行内文字 |

- **bell**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev xmS5hl（size 2375）。quality featured 回填。pn_validator --mode strict ✓。**ACH 簇收束；Bell 锚定 ACH 单一实体，SC/TTLU 同名 HK(f) 留意。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Bell 木匠-制乱-斥候-救医-苦役因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；ACH 3-char 无 Note。✔
- **registry 一致**：total 1631 character 107 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突（Bell 同名异实体 HK(f) 留意，非阻塞）。✔
- **wikilink 完整性**：Captain Hatteras + Dr Clawbonny + Johnson + The Adventures of Captain Hatteras 四链存在无悬挂；Simpson/Pen 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R432 起始计数）

| 字段 | R431 起始 | R432 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 431 | 432 |
| type_round | 123 | 124 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 367 | 368 |
| last_updated_round | 431 | 432 |

## 遗留问题

1. **character 页数 107**：本轮 +1（bell）。queue(character) 3→**2**（建序 142 消费）。registry 全库 **1631**，unknown 0。
2. **下轮 R432 = NEW1（§3(7)）**：since_evv5=5<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 143 **harris**（DSCF 诱骗 Dick Sand 一行深入非洲之美籍奸细、Negoro 同谋，248 mentions，首现 DSCF-015；配对 [[Dick Sand]]/[[Negoro]]）。
3. **第二十二批消费进度**：R431 NEW1（142 bell ✓）→ R432 NEW1（143 harris 待）→ R433 NEW1（144 isaac-hakkabut 待）→ queue 归 0 → R434 SCN28-zombie 补第二十三批。**EVV5 时点**：since_evv5 R432 起始=5，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 簇收束**（bell→captain-hatteras/clawbonny/johnson 反向、altamont/johnson 互链反向、Simpson/Pen/Wilson 待建）、DSCF 簇（harris 待建→dick-sand/negoro 反向）、OC 簇（isaac-hakkabut 待建→ben-zoof 反向）、SC 簇（olbinett/lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave/paganel 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs、Bell ACH vs SC/TTLU 一次性同名）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=367→368（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
