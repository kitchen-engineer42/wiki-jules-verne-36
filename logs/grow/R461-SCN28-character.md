---
round: 461
date: 2026-07-22
type_round: 153
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R461 · SCN28-zombie · character — 第二十九批 discover：开 MW/YEAR 两零覆盖新作（john-strock/mr-ward/fritz-napoleon-smith），queue 0→3

## 执行摘要

Phase 2.1-B character discover 轮（type_round 153）。决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=1<10；SCN28 周期 since_discover=4<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十八批（建序 160-162）R456-R460 全数消费（martin-paz/gerande/evangelina-scorbitt，PL/MZ/TT 三簇各开），queue 归 0，本轮触发 zombie discover。

**第二十九批 3 候选**（=3 → discover_streak_low 保持 0）——**广度续开二零覆盖新作**（The Master of the World、In the Year 2889），MW 一簇建 2 页起互链：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 163 | john-strock | The Master of the World | MW | MW-002 | protagonist | 63（11 章）| ABSENT | MW 开新簇 |
| 164 | mr-ward | The Master of the World | MW | MW-002 | supporting | 82（12 章）| ABSENT | MW 深耕 接 john-strock |
| 165 | fritz-napoleon-smith | In the Year 2889 | YEAR | YEAR-001 | protagonist | 68（distinct-PN 50）| ABSENT | YEAR 开新簇 |

**候选说明**：
- **john-strock**（MW）——Washington 联邦警探、第一人称叙事者，奉命查 Great Eyrie 之谜、追踪 Robur 化身「Master of the World」所驾之全能机器「Terror」；63 mentions／11 章，首现 MW-002。开 The Master of the World 新簇。
- **mr-ward**（MW）——联邦警察总长、Strock 之上司，遣其赴 Great Eyrie；82 mentions／12 章，首现 MW-002。深耕 MW，接 john-strock（互链）。
- **fritz-napoleon-smith**（YEAR）——公元 2889 年 Earth Herald 报业巨头，承祖业统御全球新闻之富豪；68 mentions／**distinct-PN 50**（单章短篇 YEAR-001，名指 Smith/Fritz），足支撑 ≥16 distinct solid PN。开 In the Year 2889 新簇。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT，无冲突。grounded（63/82/68，distinct-PN 均 ≥16 可支撑）。work 页 The Master of the World / In the Year 2889 均存，Appearances 可挂链。**排除（registry-catch）**：MW 之 Robur=「Master of the World」既建于 RC（robur）；RC 簇 uncle-prudent/phil-evans/robur 三员既建（Robur 簇不再取）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| since_evv5=1 | 否 |
| 2 | CLOSE（streak_low≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =4 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 163-165）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：discover 轮，无建页无编辑；仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、registry 精确复验无冲突。✔
- **grounding**：mentions 63/82/68，distinct-PN 均可支撑 ≥16 solid PN（YEAR 单章但 distinct-PN 50）。✔
- **registry-catch 排除**：robur（MW 中即 Master of the World）/uncle-prudent/phil-evans label EXISTS 命中，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R462 起始计数）

| 字段 | R461 起始 | R462 起始 |
|------|----------|----------|
| current_round | 461 | 462 |
| type_round | 153 | 154 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 397 | 398 |
| last_updated_round | 461 | 462 |

## 遗留问题

1. **character 127**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十九批建序 163-165）。registry **1651**，featured 35（5.1%），覆盖 29 部。
2. **下轮 R462 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 163 **john-strock**（MW 联邦警探/叙事者，protagonist，63 mentions/11 章；开 The Master of the World 新簇）。
3. **深耕计划**：R462（163 john-strock）→ R463（164 mr-ward）→ R464（165 fritz-napoleon-smith）→ queue 归 0 → R465 SCN28-zombie 补第三十批。**EVV5 顺延**：since_evv5=1，R470 前后触发（每 10 轮）。
4. **目标**：grow 至 Phase 10（GROW 终局）。Phase 2.1-B 广度扩张持续中，R461/~500。
5. **PN 渲染 bug**（已定案）：本地影子插件（RFC #562 closed / RFC-0003 多卷 deferred）。
6. **新 alias 冲突（parked）**：`Martin Paz`（character martin-paz vs work the-pearl-of-lima alias）——character-vs-work 同名 HK 债，DEFERRED。
7. **HK / Pilot 债（7 页 PN<5）/ event PN 债**：DEFERRED。
8. **corpus-discover 顺延**：since_corpus=397→398。
