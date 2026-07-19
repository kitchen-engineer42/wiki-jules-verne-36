---
round: 407
date: 2026-07-19
type_round: 99
phase: "2.1"
current_type: character
gene: NEW1
pages: [hans-bjelke]
result: success
---

# GROW 2.1-B · R407 · NEW1 · character — 建 Hans Bjelke（A Journey to the Center of the Earth 之冰岛绒鸭猎人、Lidenbrock 地心探险之沉默忠仆向导；JCE 簇新页，第十六批建序 126 末候选，queue 1→0，R408 起 SCN28-zombie）

## 执行摘要

Phase 2.1-B character 第 76 建（type_round 99），消费 R403 第十六批 discover 队列**建序 126（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=3<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R408 = §3(4) SCN28-zombie 补第十七批。**

**Hans Bjelke**（*A Journey to the Center of the Earth*）——冰岛绒鸭猎人、Lidenbrock 地心探险之沉默忠仆向导。沉毅寡言「this grave, phlegmatic, and silent individual was called Hans Bjelke; and he came recommended by M. Fridrikssen」（JCE-011-009），约成即退「the treaty concluded, Hans silently withdrew」（JCE-011-018），受雇导引「to conduct us to the village of Stapi...at the very foot of the volcano」（JCE-011-011），步履不辍「Hans moved steadily on, keeping ahead of us at an even, smooth, and rapid pace」（JCE-012-006），荷担在肩「Hans will take charge of the tools and a portion of the provisions」（JCE-017-009），率先坠渊「the descent commenced in the following order; Hans, my uncle, and myself」（JCE-017-018）。手巧俭省「without moving a limb; and yet he did his work cleverly」（JCE-011-041），谨思备患「as a cautious man, had added to our luggage a leathern bottle full of water」（JCE-014-042），临渊无惧「with such calmness, such indifference, such perfect disregard of any possible danger」（JCE-017-003），暗中冷引「with perfect coolness resumed the lead...followed him without a word」（JCE-016-016），猎人之眼「examined attentively with the eye of a huntsman」（JCE-018-016），顺受苦厄「with the resignation of his passive nature」（JCE-021-003）。

**role=supporting**。book='A Journey to the Center of the Earth'、first_appearance=JCE-011、affiliation 空、**label=Hans Bjelke，aliases=['Hans']**。

**12 distinct solid PN**（JCE-011-009/011/018/041、012-006、014-042、016-016、017-003/009/018、018-016、021-003）：均 solid，逾门。「Hans」/「Hans Bjelke」JCE 内单指本人（探险队唯一冰岛向导），无消歧歧义。

**查重**：exact-slug hans-bjelke filesystem test -f ABSENT（bucket ha）+ registry entity/label 复验——「Hans」无既建人物页；Hans Bjelke 作 character label ABSENT，无冲突。

**JCE 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Professor Lidenbrock]]（既建，JCE 簇）、[[Axel]]（既建，JCE 叙事者）、[[A Journey to the Center of the Earth]]（work→journey-to-the-center-of-the-earth，存，label「A Journey to the Center of the Earth」）——三链均无悬挂。**JCE 簇回链充分**：本页可回链既建二人物，破 FWB/FC 簇 plain-text 待建之限。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 90→**91**，registry total 1614→**1615**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 126。消费后 queue=0 → R408 SCN28-zombie 补第十七批。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| hans-bjelke | uA2CHR | A Journey to the Center of the Earth | supporting | JCE-011 | 12 distinct | 沉毅寡言-约成即退-受雇导引-步履不辍-荷担在肩-率先坠渊-手巧俭省-谨思备患-临渊无惧-暗中冷引-猎人之眼-顺受苦厄；label Hans Bjelke + aliases [Hans]；JCE 3-char 无 Note；0 超段直建；strict 首验通过；三链 [[Professor Lidenbrock]]/[[Axel]]/[[A Journey to the Center of the Earth]]（JCE 簇回链充分）|

- **hans-bjelke**：12 distinct solid PN；aliases [Hans]；character-schema 五 H2。add_page rev uA2CHR（size 2745）。quality featured 回填。pn_validator --mode strict ✓。**JCE 簇新页，可回链既建 professor-lidenbrock/axel 二人物。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Hans 向导-沉默-荷担-无惧-猎人因果；「Hans」为探险队唯一冰岛向导，无消歧歧义；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；JCE 3-char 无 Note。✔
- **registry 一致**：total 1615 character 91 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Professor Lidenbrock + Axel + A Journey to the Center of the Earth 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R408 起始计数）

| 字段 | R407 起始 | R408 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 407 | 408 |
| type_round | 99 | 100 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 343 | 344 |
| last_updated_round | 407 | 408 |

## 遗留问题

1. **character 页数 91**：本轮 +1（hans-bjelke）。queue(character) 1→**0**（建序 126 消费，第十六批全数消费完毕）。registry 全库 **1615**，unknown 0。
2. **下轮 R408 = SCN28-zombie（§3(4)）**：since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第十七批候选（≥3），since_discover 归零。
3. **第十六批全数消费**（建序 124-126：samuel-fergusson/mac-nab/hans-bjelke）R405-R407 NEW1 消费完毕，queue 归 0。R408 SCN28-zombie 补第十七批。**候选池提示**：FWB 余 joe（Ferguson 仆从、远征「右手」）；FC 余 corporal-joliffe/marbre/sabine/rae（blacksmith）；JCE 余 fridrikssen（推荐 Hans 之教授）；nicholl（FEM/RM/TT 多值 book HK(d) 暂缓）；建前须 filesystem+registry 复验，避单作品集中。
4. **回链回填债**（DEFERRED，非阻塞）：dick-kennedy→samuel-fergusson 反向、Mrs Mac-Nab 待建、Joe 待建、**hans-bjelke↔professor-lidenbrock/axel 本轮单向已链**（hans→二人物），反向待回填；william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs——slug/label 分立，无冲突，仅记录）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R414 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=343→344（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
