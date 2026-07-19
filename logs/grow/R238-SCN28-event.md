---
round: 238
date: 2026-07-18
type_round: 5
phase: "2.1"
current_type: event
gene: SCN28
pages: []
new_candidates: 4
result: discover
---

# GROW 2.1-B · R238 · SCN28-zombie · event — 首轮 event discover（播种 4 net-new 事件候选）

## 执行摘要

Phase 2.1-B event 类型**首轮 discover 复评**（type_round 5）。R237 消费 R233 播种队列末项后
queue(event)==0 → 决策机 §3(4) **SCN28-zombie**（since_evv5=4<10、streak=0<3、since_discover=4<10；
但 queue(current_type)==0 触发）。

**event discover 方法论**（异于 place toponym 扫描）：以「事件锚点 pn_anchor」定位——扫既有 19 event
**未覆盖之作品**（36 部作品仅 9 部有 event），择戏剧张力强、PN 丰度足（≥5）的情节节点。

**播种 4 net-new 事件候选**（皆 exact-slug ABSENT，非既有 19 event）：

| 建序 | event | slug | 作品 | 锚点 | 锚点线索 | PN 丰度 |
|------|-------|------|------|------|---------|---------|
| 5 | The Blinding of Michael Strogoff | strogoff-blinding | Michael Strogoff | MS-024 | Tartar 以炽刃掠目致盲 | "blinded" MS 4 + MS-024-041/049 |
| 6 | The Andes Earthquake | andes-earthquake | In Search of the Castaways | SC-012 | 安第斯地震毁道、region overturned | "earthquake" SC 多 PN |
| 7 | The Condor Abduction | condor-abduction | In Search of the Castaways | SC-014 | 秃鹰掠走 Robert Grant | "condor" SC 12 PN |
| 8 | The Missionary's Rescue | missionary-rescue | Five Weeks in a Balloon | FWB-022 | 气球队救濒死法国传教士 | "missionary" FWB 16 PN |

new_candidates=4 ≥ type_close_new_candidate_min(3) → **productive discover**，discover_streak_low 保持 0。
event 空间仍广（MS/SC/FWB/Robur/Steam House 等多部长篇无 event），远未饱和。

无建页：pages: []，registry total 恒 1494，event 恒 19，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| 全局 queue≥10；since_discover=4<10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | R237 后 event 队列罄 | **触发** |
| 5/6/7 | RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 discover，无建页。event 队列播种 4 候选（见上表，建序 5–8）。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：无建页；候选锚点线索经 gather 初核，建时逐句 strict。✔（建页时）
- **G2 段落 ≤400 字**：无建页，N/A。
- **G3 ≥5 distinct PN**：4 候选 PN 丰度经 gather 确认充足（blinded/earthquake/condor/missionary 皆 ≥5 可达）。✔
- **G4 脚本建页**：本轮无建页。✔（N/A）
- **schema 一致**：无建页；建时用 event-schema（四 H2 + book/location/pn_anchor）。N/A。
- **registry 一致**：total 1494 event 19 unknown 0 恒定（无写页）。✔
- **查重充分**：4 候选 exact-slug 皆 ABSENT，非既有 19 event。✔

## 六步状态机（SCN28，grow_state 存 R239 起始计数）

| 字段 | R238 起始 | R239 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 238 | 239 |
| type_round | 4 | 5 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 4 | 0（SCN28 reset）|
| discover_streak_low | 0 | 0（productive discover）|
| rounds_since_last_corpus_discover | 174 | 175 |
| last_updated_round | 238 | 239 |

## 遗留问题

1. **event 页数 19**（不变，discover 轮无建页）。队列现 4 候选（建序 5–8）。registry 全库 1494，unknown 0。
2. **下轮 R239 = NEW1（event）**：建 queue 建序 5 **The Blinding of Michael Strogoff**（MS，MS-024）。
   since_evv5=5<10、streak=0、queue(event)=4>0 → §3(7) NEW1。MS 2-char，无需 RFC-0003 Note。
3. **event discover 首轮 productive**：4 净新证 event 空间未饱和；后续可续掘（Robur 空战、Steam House、
   80 Days 各段、20KL 更多情节、JCE 地心历险等）。streak 归零，CLOSE 时钟未启。
4. **event 建页方法论稳定**：pn_anchor 锚定 + 单事件单指核 + 四节侧面分配 + 4-char VVV 加 RFC-0003 Note。
   condor-abduction 建时须核「秃鹰掠 Robert Grant」单指（SC condor 亦有泛指飞掠句，剔除）。
5. **散文门债**：37 页 >400（既有 DEFERRED）。
6. **corpus-discover 顺延**：since_corpus=174→175（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
