---
round: 242
date: 2026-07-18
type_round: 8
phase: "2.1"
current_type: event
gene: NEW1
pages: [missionary-rescue]
result: success
---

# GROW 2.1-B · R242 · NEW1 · event — 建 The Missionary's Rescue（Victoria 气球掠救火刑柱下法国传教士，FWB）

## 执行摘要

Phase 2.1-B event 类型第 8 建（type_round 8），消费 R238 discover 队列**建序 8（末项）**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub=0 → §3(7)）。

**The Missionary's Rescue**（FWB 主）。事件锚定 pn_anchor=**FWB-022**（气球降临火刑柱、掠救之章）。
gather("missionary" FWB 16 + "stake/savages/balloon/rescue" FWB-021/022)。逐句核**单指该事件**：
FWB-021 发现 Frenchman 落入土著手中、议定拂晓营救；FWB-022 Victoria 降临、Kennedy 揽起传教士抛压舱物、
气球骤升 300 尺脱险、Ferguson 告知身份、伤重濒死。**排除**：FWB-004-023（Dr. Krapf 史述，别一 missionary）、
FWB-023/033 死亡下葬与后文类比（属后续，非本救援动作）。exact-slug missionary-rescue ABSENT。FWB 3-char，无需 RFC-0003 Note。

**恰达门 8 distinct solid PN**（FWB×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | FWB-021-060 | 察觉 Frenchman 落入 savages 手中 |
| Overview | FWB-022-004 | 火刑柱下半裸血污的青年 |
| What Happens | FWB-022-013 | 气流推 Victoria 至囚徒正上方、渐降 |
| What Happens | FWB-022-015 | Kennedy 揽传教士入车、Joe 抛 200 磅压舱 |
| What Happens | FWB-022-021 | 气球骤升 300 尺、囚徒脱土著之手 |
| Significance | FWB-022-045 | Ferguson 告知「good fortune to rescue you」|
| Significance | FWB-022-054 | 传教士虚弱如死人般僵卧 Ferguson 眼前 |
| Significance | FWB-024-032 | 「save that unfortunate missionary from a horrible death」道德证成 |

**VVV 处置**：FWB 3-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓（重叠度门全过，无回炉）。

event 计数 22→23，registry total 1497→1498，unknown 恒 0。add_page 一次成型（rev n24yJJ，size 2928，
quality 自动 featured）。prose-gate awk 首过 0 超段（无需拆分、无 edit_page 回炉、quality 未被剥离）。
location=Africa、pn_anchor=FWB-022、book=Five Weeks in a Balloon、aliases=[The Rescue of the French Missionary]。
链 [[africa]]/[[victoria-balloon]]/*[[five-weeks-in-a-balloon]]*（Ferguson/Kennedy/Joe 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| missionary-rescue | n24yJJ | Five Weeks in a Balloon | Africa | FWB-022 | 8 | Victoria 掠救传教士单指；剔 FWB-004 Krapf 史述与 FWB-023/033 后续；FWB 3-char 无需 Note；add_page 一次成型 |

- **missionary-rescue**：8 distinct solid PN（FWB 全用，四节分配）；aliases [The Rescue of the French Missionary]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指本救援；FWB-004 别 missionary 与 FWB-023/033 后续剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（FWB），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（含撇号）。✔
- **registry 一致**：total 1498 event 23 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug missionary-rescue ABSENT；非既有 22 event；无 alias 冲突。✔
- **单指核**：FWB-021/022 救援动作逐句确认指同一事件；史述与死亡下葬剔除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R243 起始计数）

| 字段 | R242 起始 | R243 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 242 | 243 |
| type_round | 8 | 9 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 178 | 179 |
| last_updated_round | 242 | 243 |

## 遗留问题

1. **event 页数 23**：本轮 +1（The Missionary's Rescue）。R238 discover 队列（建序 5-8）全数消费，queue(event)==0。registry 全库 1498，unknown 0。
2. **下轮 R243 = SCN28-zombie（event discover 第 2 轮）**：queue(event)==0 → §3(4) 触发。
   （since_evv5=9<10 不触 EVV5；streak=0<3 不触 CLOSE；§3(3) since_discover=4<10 且全局 queue≥10 不触。）
   须扫既有 23 event **未覆盖之作品**，播种新一批 net-new 事件候选（≥3 保 productive、streak 归零）。
   候选方向：Robur 空战、Steam House、80 Days 各段、20KL 更多情节、JCE 地心历险、Mysterious Island、Hector Servadac 等。
3. **R244 EVV5 逼近**：since_evv5=9，R243 SCN28 不动 evv5 时钟（SCN28 只 reset since_discover），
   故 R244 since_evv5=10 → §3(1b) EVV5 全库评审轮（非建页）。R243 discover 后须留意 R244 转 EVV5。
4. **edit_page.py quality 剥离债**（R240 教训）：本轮 add_page 一次成型规避之；event 建页宜 add_page 一次成型。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=178→179（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
