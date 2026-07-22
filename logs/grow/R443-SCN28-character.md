---
round: 443
date: 2026-07-21
type_round: 135
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R443 · SCN28-zombie · character — 第二十五批 discover：续深耕 EHLA/SC2/DOSE 三簇各补第三员（benito-garral/andre-letourneur/niklausse），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 135）。决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=5<10；discover_streak_low=0；since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十四批（建序 148-150）R440-R442 全数消费（3 建：torres/doctor-ox/miss-herbey），queue 归 0，本轮触发 zombie discover。

**第二十五批 3 候选**（=3 → discover_streak_low 保持 0）——**续深耕**：第二十三批新开、第二十四批扩为 2 页之 EHLA/SC2/DOSE 三簇，各补第三员以完足簇内核心关系网：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 151 | benito-garral | Eight Hundred Leagues on the Amazon | EHLA | EHLA-002 | supporting | 370 | ABSENT | EHLA 接 joam-garral/torres |
| 152 | andre-letourneur | The Survivors of the Chancellor | SC2 | SC2-002 | supporting | 85 | ABSENT | SC2 接 robert-curtis/miss-herbey |
| 153 | niklausse | Doctor Ox's Experiment | DOSE | DOSE-002 | supporting | 59 | ABSENT | DOSE 接 van-tricasse/doctor-ox |

**候选说明**：
- **benito-garral**（EHLA）——Joam Garral 之热血少年子，力辩父之声誉、终手刃奸人 Torres（torres 页已引 EHLA-026-122「killed by my hand!」）；370 mentions，首现 EHLA-002。接 joam-garral↔torres，成 EHLA 三角。
- **andre-letourneur**（SC2）——Chancellor 号跛足青年乘客，父 M. Letourneur 至爱之子，与 Miss Herbey 情谊笃（miss-herbey 页已引 SC2-057-016「in Andre a brother」）；85 名指（Andre），首现 SC2-002。接 robert-curtis/miss-herbey。**注**：姓「Letourneur」与父共用，建页须以名「Andre」锚定、区分父子。
- **niklausse**（DOSE）——Quiquendone 参事、Van Tricasse 同僚，以数十年不决之「非对话」共体现全镇昏沉（van-tricasse 页已引 DOSE-013-077 二人氧下几成决斗）；59 mentions，首现 DOSE-002。接 van-tricasse/doctor-ox。

**dup-check 汇总**：3 候选 exact-slug test -f 全 ABSENT + registry entity/label/alias 精确复验 ABSENT，无冲突。全 mentions ≥59（370/85/59），足支撑 ≥12 distinct solid PN。**排除（registry-catch）**：joam-garral/torres/robert-curtis/miss-herbey/van-tricasse/doctor-ox（各既建，label EXISTS）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 151-153）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：discover 轮，无建页无编辑；仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、registry 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥59（370/85/59），足支撑 ≥12 distinct solid PN。✔
- **registry-catch 排除**：6 既建簇员 label EXISTS 命中，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R444 起始计数）

| 字段 | R443 起始 | R444 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 443 | 444 |
| type_round | 135 | 136 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 379 | 380 |
| last_updated_round | 443 | 444 |

## 遗留问题

1. **character 页数 115**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十五批建序 151-153）。registry 全库 **1639**，featured 34（5.1%）。
2. **下轮 R444 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 151 **benito-garral**（EHLA Joam 之子/手刃 Torres，supporting，370 mentions，首现 EHLA-002；成 EHLA joam-garral↔torres↔benito 三角）。
3. **深耕闭环里程碑**：第二十五批将 EHLA/SC2/DOSE 三簇各推至 **3 页**，簇内核心关系与反向链完足；广度转新作留待第二十六批（候选未覆盖作品：WAI/TN/MZ/BR/PL/SI/TT 等）。
4. **PN 渲染 bug**（已处理）：本地影子修 localhost；引擎 RFC-0003 → baojie/memex#562。
5. **回链回填债 / HK / Pilot 债 / event PN 债**：承前，DEFERRED EVV6。**下次 EVV5 = R447**（since_evv5 R444 起始=6，逐轮 +1 → R448 起始=10；即 R448 EVV5，期间 151-153 建于 R444-R446）。
6. **corpus-discover 顺延**：since_corpus=379→380。
