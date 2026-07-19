---
round: 371
date: 2026-07-19
type_round: 63
phase: "2.1"
current_type: character
gene: NEW1
pages: [simon-hart]
result: success
---

# GROW 2.1-B · R371 · NEW1 · character — 建 Simon Hart（Facing the Flag 第一人称叙事者、伪装看守 Warder Gaydon 之法国工程师；FF 簇补 ker-karraje/engineer-serko/thomas-roch；第八批建序 102，末位，queue 归 0）

## 执行摘要

Phase 2.1-B character 第 52 建（type_round 63），消费 R367 第八批 discover 队列**建序 102（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0；第八批（建序 99-102）全数消费完毕。**

**Simon Hart**（*Facing the Flag*）——伪装看守 Warder Gaydon 之法国工程师、全书第一人称叙事者、Ker Karraje 巢穴内的暗探。伪装之下「the alleged Gaydon was a French engineer named Simon Hart, who for several years past had been connected with a manufactory of chemical products in New Jersey」（FF-001-041），「Simon Hart, alias Gaydon, had been an attendant at Healthful House for fifteen months」（FF-001-042），其务为国「this the mission to which he had wholly devoted himself in the interest of his native country」（FF-001-044）。全书主体为其手记「(Notes by Simon Hart, the Engineer.)」（FF-005-002）；与所守之人同遭掳「Thomas Roch and his keeper Gaydon, or rather Simon Hart... were kidnapped」（FF-013-022）；独藏一秘「he must at any rate never know that I am aware of the position of Back Cup Island」（FF-011-010）；获救时手记验其身「it was learned from the note-book that he was Simon Hart」（FF-018-026）。其貌显其智「a large head, high, wide forehead... eyes generally haggard, but which became piercing and imperious when illuminated by his dominant idea」（FF-001-045）；伪装无懈「None suspected that I was Simon Hart, the engineer, nor could they have suspected my nationality」（FF-005-006），「No one could have had any idea that I was Simon Hart, the engineer」（FF-006-027）。Ker Karraje 揭其真身「Warder Gaydon is Engineer Simon Hart... who knows his secrets」（FF-010-093）；Serko 早识破之，Hart 诘其「how you came to find out that Gaydon, the warder, was Simon Hart, the engineer」（FF-012-024）。

**role=narrator**。book='Facing the Flag'、first_appearance=FF-001、affiliation 空、**label=Simon Hart，aliases=[Warder Gaydon, Gaydon]**。

**12 distinct solid PN**（FF-001-041/042/044/045、005-002/006、006-027、010-093、011-010、012-024、013-022、018-026）：均 solid，逾门。

**查重**：exact-slug simon-hart + 变体 warder-gaydon filesystem test -f 均 ABSENT + registry entity ABSENT（R367 discover 已验，本轮建前复验一致）。

**alias 新增校验**：aliases=[Warder Gaydon, Gaydon] 建后 build_registry **未引入新 alias 冲突**（仍仅 Hector Servadac + Robur + Claudius Bombarnac 三 parked 冲突），故保留（与 R365 ker-karraje 加 Count d'Artigas 同法）。

**FF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FF 簇补 ker-karraje/engineer-serko/thomas-roch）**：[[Ker Karraje]]（character，R365 建）/ [[Engineer Serko]]（character，R368 建）/ [[Thomas Roch]]（character，存）/ [[Facing the Flag]]（work，存）——四链互链无悬挂。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 66→**67**，registry total 1590→**1591**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_evv5=9<10（EVV5 未达门）、queue=1>0 → NEW1 消费建序 102。消费后 queue=0。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| simon-hart | FmaeJs | Facing the Flag | narrator | FF-001 | 12 distinct | 伪装 Warder Gaydon 之法国工程师-第一人称叙事者-巢内暗探-守 Roch-独知 Back Cup 之位-Ker Karraje 揭身-Serko 识破；label Simon Hart + aliases [Warder Gaydon, Gaydon]（无新冲突）；FF 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Ker Karraje]]/[[Engineer Serko]]/[[Thomas Roch]]/[[Facing the Flag]] |

- **simon-hart**：12 distinct solid PN；aliases [Warder Gaydon, Gaydon]；character-schema 五 H2。add_page rev FmaeJs（size 2818）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Simon Hart 伪装身份-叙事者-暗探-守 Roch-藏秘-被揭因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=narrator ∈ enum；FF 2-char 无 Note。✔
- **registry 一致**：total 1591 character 67 unknown 0；3 alias warn（均 parked HK，新增 aliases 无冲突）。✔
- **查重充分**：exact-slug simon-hart + 变体 warder-gaydon + entity 全 ABSENT；registry 无 character 冲突（label Simon Hart 唯一）。✔
- **wikilink 完整性**：Ker Karraje / Engineer Serko / Thomas Roch / Facing the Flag 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R372 起始计数）

| 字段 | R371 起始 | R372 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 371 | 372 |
| type_round | 63 | 64 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 307 | 308 |
| last_updated_round | 371 | 372 |

## 遗留问题

1. **character 页数 67**：本轮 +1（simon-hart）。queue(character) 1→**0**（建序 102 消费，第八批全数消费完毕）。registry 全库 **1591**，unknown 0。
2. **下轮 R372 = EVV5（§3(1b)）**：since_evv5=10 首达门 → schema-reflection 轮（pages:[]，仅 G4，role 读 frontmatter，勿依 pages.json 顶层——R350 假阴教训）。§3(1a) 需 since_evv5≥10 **且** since_discover≥10；since_discover=4<10 → §3(1a) 否，落 §3(1b) 纯 EVV5。stage 集仅 `local/state/grow_state.json logs/grow/R372-EVV5-character.md`。
3. **R373 = SCN28-zombie discover（§3(4)）**：R372 EVV5 后 since_discover +=1=5，queue(character)=0 → §3(4) 触发，补第九批候选（≥3 grounded + filesystem/registry dup-check ABSENT）。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + major-noltitz→Faruskiar、uncle-prudent→Phil Evans、claudius-bombarnac→Faruskiar、ker-karraje→Engineer Serko/Simon Hart（本轮建，可回填）、engineer-serko→Simon Hart/Captain Spade、thomas-roch→Simon Hart/Ker Karraje。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=307→308（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
