---
round: 243
date: 2026-07-18
type_round: 9
phase: "2.1"
current_type: event
gene: SCN28
pages: []
new_candidates: 3
result: discover
---

# GROW 2.1-B · R243 · SCN28-zombie · event — 第 2 轮 event discover（播种 3 net-new 事件候选，取未覆盖作品）

## 执行摘要

Phase 2.1-B event 类型**第 2 轮 discover 复评**（type_round 9）。R242 消费 R238 播种队列末项（建序 8）后
queue(event)==0 → 决策机 §3(4) **SCN28-zombie**（since_evv5=9<10、streak=0<3、since_discover=4<10；
§3(3) 全局 queue≥10 且 since_discover<10 不触；但 queue(current_type)==0 触发）。

**event discover 方法论**（承 R238）：以「事件锚点 pn_anchor」定位——扫既有 23 event **覆盖分布**
（36 部作品仅 12 部有 event），择**未覆盖作品**中戏剧张力强、PN 丰度足（≥5）的情节节点。

**既有 23 event 作品覆盖**（book 计）：AWED 3、TTLU 3、JCE 3、MI 3、SC 2、FEM 2、ACH 2、OC 1、FC 1、RM 1、FWB 1、MS 1。
**未覆盖强戏剧作品**：SC2 Chancellor、DSCF Dick Sand、RC Robur、MW Master of the World、AM Antarctic Mystery、
EHLA Amazon、GM Godfrey Morgan、UC Underground City、WC Cynthia 等。

**播种 3 net-new 事件候选**（皆 exact-slug ABSENT，非既有 23 event，均取未覆盖作品）：

| 建序 | event | slug | 作品 | 锚点 | 锚点线索 | PN 丰度 |
|------|-------|------|------|------|---------|---------|
| 9 | The Burning of the Chancellor | chancellor-fire | The Survivors of the Chancellor | SC2-009 | 棉货舱起火、无法扑救，海上苦难开端 | "fire" SC2 47 + SC2-008-012/009-005 |
| 10 | The Whale Hunt Disaster | whale-hunt-disaster | Dick Sand: A Captain at Fifteen | DSCF-008 | 捕鲸艇倾覆、Hull 与全员葬身、Dick 少年掌舵 | "whale" DSCF 73 + DSCF-008-084/009-035 |
| 11 | The Abduction by the Albatross | albatross-abduction | Robur the Conqueror | RC-005 | Uncle Prudent 与 Phil Evans 被堵嘴蒙眼掳上飞行器 | "Albatross" RC 众 + RC-005-031 |

new_candidates=3 ≥ type_close_new_candidate_min(3) → **productive discover**，discover_streak_low 保持 0。
event 空间仍广（MW/AM/EHLA/GM/UC 等多部未掘），远未饱和。

无建页：pages: []，registry total 恒 1498，event 恒 23，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| 全局 queue≥10；since_discover=4<10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | R242 后 event 队列罄 | **触发** |
| 5/6/7 | RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 discover，无建页。event 队列播种 3 候选（见上表，建序 9–11）。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：无建页；候选锚点线索经 gather 初核，建时逐句 strict。✔（建页时）
- **G2 段落 ≤400 字**：无建页，N/A。
- **G3 ≥5 distinct PN**：3 候选 PN 丰度经 gather 确认充足（fire/whale/Albatross 皆 ≥5 可达）。✔
- **G4 脚本建页**：本轮无建页。✔（N/A）
- **schema 一致**：无建页；建时用 event-schema（四 H2 + book/location/pn_anchor）。N/A。
- **registry 一致**：total 1498 event 23 unknown 0 恒定（无写页）。✔
- **查重充分**：3 候选 exact-slug 皆 ABSENT（含 burning-of-the-chancellor/chancellor-shipwreck 变体），非既有 23 event。✔

## 六步状态机（SCN28，grow_state 存 R244 起始计数）

| 字段 | R243 起始 | R244 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 243 | 244 |
| type_round | 9 | 10 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 4 | 0（SCN28 reset）|
| discover_streak_low | 0 | 0（productive discover）|
| rounds_since_last_corpus_discover | 179 | 180 |
| last_updated_round | 243 | 244 |

## 遗留问题

1. **event 页数 23**（不变，discover 轮无建页）。队列现 3 候选（建序 9–11）。registry 全库 1498，unknown 0。
2. **下轮 R244 = EVV5（全库评审轮，非建页）**：SCN28 未动 evv5 时钟（只 reset since_discover），
   R244-start since_evv5=10≥10 → §3(1b) **EVV5** 触发（since_discover=0<10 不触 §3(1a) 组合轮）。
   按 grow-state-machine §3 执行 EVV5 全库评审（抽样评分、不建页），评审后 since_evv5 reset=0。
3. **R245 起恢复 NEW1**：EVV5 后 queue(event)=3>0，R245 建 queue 建序 9 **The Burning of the Chancellor**（SC2，SC2-009）。
4. **event discover 第 2 轮 productive**：3 净新证 event 空间未饱和；后续可续掘（MW Terror、AM Antarctic、EHLA、GM、UC 等）。
   streak 归零，CLOSE 时钟未启。
5. **建时消歧提醒**：chancellor-fire 核船货起火单指（SC2 fire 47 PN 有炉火/枪火泛指，剔除）；
   whale-hunt-disaster 核 Hull 覆没单指（DSCF whale 73 有捕鲸泛述，剔除）；albatross-abduction 核 Weldon 二人被掳单指。
6. **散文门债**：37 页 >400（既有 DEFERRED）。
7. **corpus-discover 顺延**：since_corpus=179→180（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
