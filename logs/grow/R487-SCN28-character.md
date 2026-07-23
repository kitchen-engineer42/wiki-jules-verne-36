---
round: 487
date: 2026-07-23
type_round: 179
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R487 · SCN28-zombie · character — 第三十五批 discover：转中低覆盖作高频缺员（dame-hansen/crockston/jack-ryan），queue 0→3

## 执行摘要

Phase 2.1-B character discover 轮（type_round 179）。§3 首匹配 **§3(4) SCN28-zombie**（since_evv5=5<10；SCN28 周期 since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第三十四批（建序 178-180）R484-R486 全数消费（fragoso/lina/jem-west，EHLA→9/AM→6），queue 归 0，本轮触发 zombie discover。

**簇策转向**：EHLA(9)/AM(6) 深耕暂足；据全库 proper-noun 频次扫描（去既建、去船/兽/族称），转其他中/低覆盖作之高频缺员，跨 TN/BR/UC 三作：

| 建序 | slug | book | VVV | pn_anchor | role | mentions/PN | dup-check | 簇 |
|------|------|------|-----|-----------|------|-------------|-----------|-----|
| 181 | dame-hansen | Ticket No. 9672 | TN | TN-001 | supporting | 135/130 | ABSENT | TN 接 hulda/joel-hansen/sylvius-hogg（→5）|
| 182 | crockston | The Blockade Runners | BR | BR-002 | supporting | 103/102 | ABSENT | BR 接 james-playfair/jenny-halliburtt（→3）|
| 183 | jack-ryan | The Underground City | UC | UC-003 | supporting | 93/89 | ABSENT | UC 深耕（→3）|

**候选说明**：
- **dame-hansen**（TN）——Dal 客栈之寡母、Hulda 与 Joel 之母；因秘密欠债将彩票典与 Sandgoist 而忧郁寡言；135 mentions/130 distinctPN，首现 TN-001-001。**前批 sylvius-hogg/joel-hansen 页已以纯文本引其→回链**，TN 簇 4→5。
- **crockston**（BR）——Jenny Halliburtt 之忠仆美国水手、乔装登 Dolphin 号助救其囚父者；103 mentions/102 distinctPN，首现 BR-002-023。BR 簇 2→3。
- **jack-ryan**（UC）——Aberfoyle 矿之乐天歌者、Harry Ford 之友、驱迷信之开朗矿工；93 mentions/89 distinctPN（Jack Ryan 76），首现 UC-003-043。UC 簇 2→3。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT。distinctPN 全 ≥89。**排除（registry-catch）**：TN 既建 hulda/ole-kamp/sylvius-hogg/joel-hansen；BR 既建 james-playfair/jenny-halliburtt；船/兽/族称（Dolphin/Dingo/Ebba/Chinese/Siberian 等）剔除。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| since_evv5=5 | 否 |
| 2 | CLOSE（streak_low≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 181-183）+ discover-note。

## EXIT-GATE 检查

- **G4**：discover 轮，仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、无冲突。✔
- **grounding**：distinctPN 130/102/89，足支撑 ≥16 solid PN。✔
- **广度回补**：转 TN/BR/UC 三中低覆盖作，避免过度集中 EHLA/AM。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R488 起始计数）

| 字段 | R487 起始 | R488 起始 |
|------|----------|----------|
| current_round | 487 | 488 |
| type_round | 179 | 180 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 423 | 424 |
| last_updated_round | 487 | 488 |

## 遗留问题

1. **character 145**：本轮无建页（discover 轮）。queue(character) 0→**3**（第三十五批建序 181-183）。registry **1669**，featured 35（5.0%），覆盖 32 部。
2. **下轮 R488 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 181 **dame-hansen**（TN Dal 客栈寡母，supporting，135 mentions；深耕 TN 至 5，回填 sylvius/joel 页 Dame Hansen）。
3. **深耕计划**：R488（181 dame-hansen）→ R489（182 crockston）→ R490（183 jack-ryan）→ queue 归 0 → **R491 = EVV5**（since_evv5 于 R491 起始达 10）。
4. **CLOSE 观察**：全库高频缺员仍充裕（多作 ≥69 mentions 角未建：Sandgoist/Martin Holt/Alvez/Craventy/Malarius/Patrick/Donellan/Mulrady 等），character 广度未尽，暂不触发 §3(2) CLOSE。
5. **目标**：grow 至 Phase 10。Phase 2.1-B 广度扩张持续，R487/~500。
6. **PN 渲染 / Martin Paz alias / HK / Pilot 债 / event PN 债 / 回链**：DEFERRED。
7. **corpus-discover 顺延**：since_corpus=423→424。
