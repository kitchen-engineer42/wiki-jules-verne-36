---
round: 370
date: 2026-07-19
type_round: 62
phase: "2.1"
current_type: character
gene: NEW1
pages: [phil-evans]
result: success
---

# GROW 2.1-B · R370 · NEW1 · character — 建 Phil Evans（Robur the Conqueror 冷静的 Weldon Institute 秘书、Uncle Prudent 之竞敌兼同囚；RC 簇补 uncle-prudent/robur；第八批建序 101）

## 执行摘要

Phase 2.1-B character 第 51 建（type_round 62），消费 R367 第八批 discover 队列**建序 101**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Phil Evans**（*Robur the Conqueror*）——Weldon Institute 秘书、Wheelton Watch Company 巨富经理、Uncle Prudent 恒常的气球派竞敌，被 Robur 掠上 Albatross 后不辍谋逃。富有——「This was Phil Evans, who was also very rich, being the manager of the Wheelton Watch Company... equal in every respect to the best Swiss workmanship」（RC-002-021）；位居竞敌之次「that is why Phil Evans was only secretary of the Weldon Institute, whereas Uncle Prudent was president」（RC-002-032）；气球派死忠「the bird has no helix; that we know!」（RC-004-041）。夜遭掳「a bandage over the eyes, a gag in the mouth, a cord round the wrists, a cord round the ankles」（RC-006-002），脱狱「Uncle Prudent and Phil Evans rushed out of their prison」（RC-006-113），逃志坚定「had quite made up their minds to escape」（RC-011-002），洞悉 Robur「will only give us our liberty when it suits him, and perhaps not at all」（RC-013-035）。冷静为其本色——「regaining his coolness, managed to slacken the cord which bound his wrists」（RC-006-005），且慷慨「did not hesitate to at once set free his rival」（RC-006-008），屡抑 Prudent 之暴「drew away his colleague, who was about to commit some act of violence」（RC-013-015）；愤极时携其入舱「led him off to his cabin」（RC-013-086），并为 Frycollin 求情「to be taken on board again」（RC-013-092）。

**role=supporting**。book='Robur the Conqueror'、first_appearance=RC-002、affiliation='Weldon Institute'、**label=Phil Evans，aliases=[]**。

**12 distinct solid PN**（RC-002-021/032、004-041、006-002/005/008/113、011-002、013-015/035/086/092）：均 solid，逾门。

**查重**：exact-slug phil-evans filesystem test -f ABSENT + registry entity ABSENT（R367 discover 已验，本轮建前复验一致）。

**RC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（RC 簇补 uncle-prudent/robur）**：[[Uncle Prudent]]（character，R364 建）/ [[Robur]]（character，存）/ [[Robur the Conqueror]]（work，存）——三链互链无悬挂。Frycollin（未建，无候选）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 65→**66**，registry total 1589→**1590**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2、queue=2>0 → NEW1 消费建序 101。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| phil-evans | bsNRMw | Robur the Conqueror | supporting | RC-002 | 12 distinct | Weldon Institute 秘书-Wheelton Watch 经理-气球派竞敌-Albatross 同囚-恒谋逃-冷静抑 Prudent-为 Frycollin 求情；label Phil Evans + aliases 空；RC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Uncle Prudent]]/[[Robur]]/[[Robur the Conqueror]] |

- **phil-evans**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev bsNRMw（size 2708）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Phil Evans 秘书身份-气球派-同囚-谋逃-冷静抑友因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；RC 2-char 无 Note。✔
- **registry 一致**：total 1590 character 66 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Phil Evans 唯一）。✔
- **wikilink 完整性**：Uncle Prudent / Robur / Robur the Conqueror 三链存在无悬挂；Frycollin 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R371 起始计数）

| 字段 | R370 起始 | R371 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 370 | 371 |
| type_round | 62 | 63 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 306 | 307 |
| last_updated_round | 370 | 371 |

## 遗留问题

1. **character 页数 66**：本轮 +1（phil-evans）。queue(character) 2→**1**（建序 101 消费）。registry 全库 **1590**，unknown 0。
2. **EVV5 排期校正（off-by-one）**：R367/R368/R369 日志前瞻误记「R371 起始 since_evv5=10 → EVV5」。以 grow_state 活计数为准（权威）：last EVV5=R361，R362 起始归 0，逐轮 +1 → R371 起始 since_evv5=**9**（<10），**R371 仍为 NEW1**；R372 起始 since_evv5=**10** → §3(1b) EVV5 首触。决策每轮以活计数重算，自动纠偏。
3. **下轮 R371 = NEW1（§3(7)）**：since_evv5=9<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 **102**（simon-hart，book Facing the Flag，pn_anchor FF-001，role narrator；建前复验 exact-slug simon-hart + 变体 warder-gaydon 均 ABSENT）。消费后 queue=0。
4. **R372 = EVV5（§3(1b)）**：since_evv5=10 首达 → schema-reflection 轮（pages:[]，仅 G4，role 读 frontmatter）。R373 起始 queue=0 → §3(4) SCN28-zombie 补第九批 discover。
5. **回链回填债**（DEFERRED，非阻塞）：既有 + major-noltitz→Faruskiar、uncle-prudent→Phil Evans（本轮建，可回填）、claudius-bombarnac→Faruskiar、ker-karraje→Engineer Serko/Simon Hart、thomas-roch→Simon Hart/Ker Karraje、engineer-serko→Captain Spade/Simon Hart。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=306→307（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
