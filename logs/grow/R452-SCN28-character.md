---
round: 452
date: 2026-07-22
type_round: 144
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R452 · SCN28-zombie · character — 第二十七批 discover：深耕 TN/WAI/BR 三新簇各补第二员（ole-kamp/penellan/jenny-halliburtt），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 144）。决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=3<10；since_discover=4<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十六批（建序 154-156）R449-R451 全数消费（3 建：hulda/jean-cornbutte/james-playfair，三新簇各首建），queue 归 0，本轮触发 zombie discover。

**第二十七批 3 候选**（=3 → discover_streak_low 保持 0）——**深耕**上批新开之 TN/WAI/BR 三簇，各补第二员（各簇 protagonist 之核心伴侣/主仆），起反向链：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 157 | ole-kamp | Ticket No. 9672 | TN | TN-001 | supporting | 155 | ABSENT | TN 接 hulda |
| 158 | penellan | A Winter Amid the Ice | WAI | WAI-001 | supporting | 152 | ABSENT | WAI 接 jean-cornbutte |
| 159 | jenny-halliburtt | The Blockade Runners | BR | BR-003 | supporting | 49 | ABSENT | BR 接 james-playfair |

**候选说明**：
- **ole-kamp**（TN）——Hulda 之航海未婚夫，Viking 号沉没前遗瓶书与彩票 9672、终生还归者；155 mentions，首现 TN-001。接 hulda（hulda 页已多引 Ole）。
- **penellan**（WAI）——Jean Cornbutte 之忠仆 Breton 舵手、北冰洋搜寻之砥柱；152 mentions，首现 WAI-001。接 jean-cornbutte（jean 页已引 Penellan the Breton）。
- **jenny-halliburtt**（BR）——乔装登 Dolphin 号入 Charleston 救囚父之 Boston 少女、James Playfair 所爱者；49 名指（Jenny，亦称 Miss Halliburtt），首现 BR-003。接 james-playfair（james 页已多引 Jenny）。**注**：姓「Halliburtt」与父 Mr. Halliburtt 共用，建页以名「Jenny」锚定、区分父女。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT，无冲突。全 mentions ≥49（155/152/49），足支撑 ≥12 distinct solid PN。**排除（registry-catch）**：hulda/jean-cornbutte/james-playfair（上批既建，label EXISTS）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =3 | 否 |
| 3 | SCN28（since_discover≥10）| =4 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 157-159）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：discover 轮，无建页无编辑；仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、registry 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥49（155/152/49），足支撑 ≥12 distinct solid PN。✔
- **registry-catch 排除**：hulda/jean-cornbutte/james-playfair label EXISTS 命中，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R453 起始计数）

| 字段 | R452 起始 | R453 起始 |
|------|----------|----------|
| current_round | 452 | 453 |
| type_round | 144 | 145 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 4 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 388 | 389 |
| last_updated_round | 452 | 453 |

## 遗留问题

1. **character 121**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十七批建序 157-159）。registry **1645**，featured 34（5.1%），覆盖 26 部。
2. **下轮 R453 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 157 **ole-kamp**（TN Hulda 未婚夫/遗彩票者，supporting，155 mentions，首现 TN-001；深耕 TN 簇 + 接 hulda）。
3. **深耕计划**：R453（157 ole-kamp）→ R454（158 penellan）→ R455（159 jenny-halliburtt）→ queue 归 0 → R456 SCN28-zombie 补第二十八批。**R458 = EVV5**。
4. **目标**：grow 至 Phase 10（GROW 终局）。Phase 2 广度扩张持续中，R452/~500。
5. **PN 渲染 bug**（已定案）：本地影子（RFC #562 closed）。
6. **HK / Pilot 债 / event PN 债**：DEFERRED。
7. **corpus-discover 顺延**：since_corpus=388→389。
