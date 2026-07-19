---
round: 241
date: 2026-07-18
type_round: 7
phase: "2.1"
current_type: event
gene: NEW1
pages: [condor-abduction]
result: success
---

# GROW 2.1-B · R241 · NEW1 · event — 建 The Condor Abduction（秃鹰掠走 Robert Grant、Thalcave 一枪救之，SC）

## 执行摘要

Phase 2.1-B event 类型第 7 建（type_round 7），消费 R238 discover 队列**建序 7**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

**The Condor Abduction**（SC 主）。事件锚定 pn_anchor=**SC-014**（秃鹰掠人之章，紧接安第斯地震）。
gather("condor" distinctPN=13：SC 12 + FC 1)。逐句核**单指该事件**：SC-014 秃鹰盘旋 inaccessible plateau、
掠起 apparently lifeless 的 Robert Grant、marksman 一枪射落、Glenarvan 夺回、SC-015 Patagonian 验伤救活。
**排除泛指**：FC-035-040（simile「as large as a condor」）、SC-027-036（Glenarvan 事后 recap）剔除。
exact-slug condor-abduction ABSENT（robert-grant-condor / condor-rescue 亦 ABSENT，无 alias 冲突）。SC 2-char，无需 RFC-0003 Note。

**恰达门 8 distinct solid PN**（SC×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SC-014-051 | 秃鹰盘旋 inaccessible plateau |
| Overview | SC-014-055 | 爪中人体 dangling，即 Robert Grant |
| What Happens | SC-014-053 | 「suppose Robert were still alive! That bird」|
| What Happens | SC-014-057 | seizing Wilson's carbine 瞄准秃鹰 |
| What Happens | SC-014-059 | 秃鹰头中弹、如 parachute 坠落 |
| What Happens | SC-014-061 | Glenarvan 从秃鹰爪中夺回尸身、探心跳 |
| Significance | SC-014-060 | providential shot 来路不明（Thalcave）|
| Significance | SC-015-058 | Patagonian 验伤、救活 Robert |

**VVV 处置**：SC 2-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓（重叠度门全过，无回炉）。

event 计数 21→22，registry total 1496→1497，unknown 恒 0。add_page 一次成型（rev TS2UyN，size 2785，
quality 自动 featured）。prose-gate awk 首过 0 超段（无需拆分、无 edit_page 回炉、quality 未被剥离）。
location=Andes、pn_anchor=SC-014、book=In Search of the Castaways、aliases=[The Rescue of Robert Grant]。
链 [[Andes]]/[[andes-earthquake]]/*[[in-search-of-the-castaways]]*（Glenarvan/Paganel/Thalcave/Robert Grant 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| condor-abduction | TS2UyN | In Search of the Castaways | Andes | SC-014 | 8 | 秃鹰掠 Robert Grant 单指；剔 FC-035 simile 与 SC-027 recap；Thalcave 救；SC 2-char 无需 Note；add_page 一次成型 |

- **condor-abduction**：8 distinct solid PN（SC 全用，四节分配）；aliases [The Rescue of Robert Grant]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（秃鹰掠 Robert Grant）；泛指 FC/SC-027 剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（SC），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（含撇号）。✔
- **registry 一致**：total 1497 event 22 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug condor-abduction ABSENT；非既有 21 event；无 alias 冲突。✔
- **单指核**：SC-014 秃鹰掠人 + SC-015 救活逐句确认指同一事件；FC simile 与 recap 剔除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R242 起始计数）

| 字段 | R241 起始 | R242 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 241 | 242 |
| type_round | 7 | 8 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 177 | 178 |
| last_updated_round | 241 | 242 |

## 遗留问题

1. **event 页数 22**：本轮 +1（The Condor Abduction）。队列余 1（建序 8）。registry 全库 1497，unknown 0。
2. **下轮 R242 = NEW1（event）**：建 queue 建序 8 **The Missionary's Rescue**（FWB，FWB-021/022）。
   since_evv5=8<10、streak=0、queue(event)=1>0 → §3(7) NEW1。FWB 3-char，无需 RFC-0003 Note。
3. **R242 后 queue(event) 将罄**：建序 8 消费后 queue(event)==0，R243 触发 §3(4) SCN28-zombie（event discover 第 2 轮）。
4. **R244 EVV5 逼近**：since_evv5=8，将于 R244（=10）触发 §3(1b) EVV5 全库评审轮（非建页）。惟 R243 若 SCN28 不影响 evv5 时钟。
5. **edit_page.py quality 剥离债**（R240 教训）：本轮 add_page 一次成型规避之；event 建页宜 add_page 一次成型、避免 edit 回炉。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=177→178（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
