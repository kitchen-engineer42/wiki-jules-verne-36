---
round: 451
date: 2026-07-22
type_round: 143
phase: "2.1"
current_type: character
gene: NEW1
pages: [james-playfair]
result: success
---

# GROW 2.1-B · R451 · NEW1 · character — 建 James Playfair（The Blockade Runners 之 Dolphin 号苏格兰船长/闯 Charleston 封锁线）；开 BR 新簇，消费第二十六批建序 156（末位），queue 1→0

## 执行摘要

Phase 2.1-B character 第 106 建（type_round 143），消费建序 156（末位）。决策机 §3 首匹配 **NEW1**（since_evv5=2<10；since_discover=3<10 且 queue=1>0；stub%=0 → §3(7)）。**消费后 queue(character)=0（第二十六批 hulda/jean-cornbutte/james-playfair 三建告罄）→ R452 = §3(4) SCN28-zombie 补第二十七批。开 BR 新簇。character 覆盖作品 26 部。**

**James Playfair**（*The Blockade Runners*）——Glasgow Dolphin 号年轻苏格兰船长（叔 Vincent Playfair 之船，BR-001-016）。美国南北战争棉荒之际（BR-001-033），谋以商船闯 Charleston 联邦封锁线售械购棉牟利（BR-001-042/052）——初为唯利是图之商人（BR-004-036 / 001-035 / 005-056），厉治偷渡者（BR-003-045），然精熟 Charleston 湾水道（BR-009-050）。发觉船上乔装女子 Jenny Halliburtt、让舱于她（BR-003-074），继堕情网（BR-006-004），遂为救其被囚之父再冒封锁「in two hours your father will be in safety」（BR-008-069 / 008-084），终与 Jenny 完婚（BR-010-006）——利欲之商为爱所化之英雄弧。关系：Jenny Halliburtt（BR-006-004）、水手 Crockston（BR-002-045）、叔 Vincent Playfair（BR-002-052）。

**role=protagonist**。book=The Blockade Runners、first_appearance=BR-001、affiliation 空、**label=James Playfair，aliases=[]**。

**16 distinct solid PN**（BR-001-016/033/035/042/052、002-045/052、003-045/074、004-036、005-056、006-004、008-069/084、009-050、010-006）：逾门。全 16 引文程序化逐字子串复核 + strict 双通过（明嘱区分侄 James 与叔 Vincent Playfair，同姓）。

**质量档（cap 持守）**：regrade → **standard**。featured 恒 34/675=5.1%。

**方法（workflow + 转录恢复）**：mine→verify（5+5 子代理）扫 BR 10 章。自 verify 转录恢复 52 valid / 51 distinct PN（后 workflow 完成复验一致）；择 16。建页前 1 处（BR-002-052）跨对话标签失配，改续引后 strict 通过。

**查重**：exact-slug + registry label/alias ABSENT，无冲突。

**wikilink**：BR 首建页，关系人（Jenny/Crockston/Vincent）未建，PN-grounded 纯文本无悬链；Appearances 挂 [[The Blockade Runners]]（work，存，BR-008-084）。

prose-gate：0 超段。character 120→**121**，registry 1644→**1645**，覆盖作品 25→**26** 部。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =2 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

- **james-playfair**：rev Gf0ouV（size 3214）；16 distinct solid PN；aliases []；五 H2；role=protagonist；quality standard（cap）。pn_validator --mode strict ✓。[[The Blockade Runners]] 挂链；侄/叔消歧。**BR 簇开纵深。**

## EXIT-GATE 检查

- **G1**：全句 sentence_index 单指 James（非叔 Vincent）；52 validated + Python 逐字校；strict ✓。✔
- **G2**：0 超段。✔　**G3**：16 distinct ≥5。✔　**G4**：add_page，未用 Write/Edit 于 pages/**。✔
- **schema**：五 H2；frontmatter 全字段（description 单引号）；role ∈ enum。✔
- **quality cap**：regrade 持守 5%；james standard。✔　**registry**：total 1645 character 121 unknown 0 featured 34。✔
- **查重**：exact-slug + entity/label/alias ABSENT。✔　**wikilink**：[[The Blockade Runners]] 无悬挂；关系人纯文本。✔
- **排除**：提交前 grep clean。✔

## 六步状态机（NEW1，grow_state 存 R452 起始计数）

| 字段 | R451 起始 | R452 起始 |
|------|----------|----------|
| current_round | 451 | 452 |
| type_round | 143 | 144 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 387 | 388 |
| last_updated_round | 451 | 452 |

## 遗留问题

1. **character 121**：queue(character) 1→**0**（第二十六批 154-156 三建告罄）。registry **1645**，featured 34（5.1%），**覆盖 26 部**。
2. **下轮 R452 = SCN28-zombie（§3(4)）**：queue==0 → zombie discover 补第二十七批（since_discover 归零）。
3. **广度里程碑**：第二十六批开 TN/WAI/BR 三新作，各成单页新簇（hulda/jean-cornbutte/james-playfair）。后批可深耕新簇或续开新作（未覆盖：MZ/PL/SI/TT 等）。
4. **目标**：grow 至 Phase 10（GROW 终局）。Phase 2 广度扩张（R~50-500）持续中，R451/~500。
5. **PN 渲染 bug**（已定案）：本地影子（RFC #562 closed）。
6. **HK / Pilot 债 / event PN 债**：DEFERRED（下次 EVV5 R458）。
7. **corpus-discover 顺延**：since_corpus=387→388。
