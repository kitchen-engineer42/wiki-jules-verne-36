---
round: 237
date: 2026-07-18
type_round: 3
phase: "2.1"
current_type: event
gene: NEW1
pages: [forward-mutiny]
result: success
---

# GROW 2.1-B · R237 · NEW1 · event — 建 The Forward Mutiny（Forward 号船员哗变焚船，ACH；R233 队列末项）

## 执行摘要

Phase 2.1-B event 类型第 4 建（type_round 3），**消费 R233 播种队列末项**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub=0 → §3(7)）。

取 R233 event 队列**建序 4** **The Forward Mutiny**（ACH 主）。事件锚定 pn_anchor=**ACH-034**
（Johnson 追述哗变始末之章）。gather 事件核心（"the Forward" distinctPN=10 全 ACH；"revolt"/"mutiny" ACH 语境）。
逐句核**单指该事件**（Hatteras 离船北进期间 Shandon 率众夺权哗变、弃船焚毁 Forward 号），
剔他作泛指叛乱（AM/MS/PL 等）。exact-slug forward-mutiny ABSENT。

**恰达门 8 distinct solid PN**（ACH×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | ACH-034-016 | Johnson 述：Hatteras 离船后 Shandon 率众夺船权 |
| What Happens | ACH-021-027 | 忠奸分野（Doctor/Johnson/Bell/Simpson 忠 vs 未决派）|
| What Happens | ACH-024-002 | Frozen Pole 困境，crew nearly in revolt |
| What Happens | ACH-034-017 | Shandon 纵众、诓其苦役将终 |
| What Happens | ACH-034-021 | Forward 号焚烧两日 |
| What Happens | ACH-033-007 | Forward 号荡然无存（not a vestige remained）|
| Significance | ACH-054-029 | Hatteras 梦见焚船叛徒（创伤延续）|
| Significance | ACH-034-005 | 雪覆爆炸现场、抹尽 Forward 痕迹 |

**4-char VVV 处置**：ACH 4 字符码，PN 渲染纯文本（RFC-0003 未决）→ 页顶加 RFC-0003 Note。pn_validator strict ✓。

event 计数 18→19，registry total 1493→1494，unknown 恒 0。add_page 一次成型（rev 4HfYgZ，size 2672，
quality 自动 featured）。prose-gate awk 初 1 段超（Overview 425），拆分后 0 超段。
location=The Forward、pn_anchor=ACH-034、book=The Adventures of Captain Hatteras、aliases=[The Burning of the Forward]。
链 [[Captain Hatteras]]/[[The Forward]]/[[The Adventures of Captain Hatteras]]（Shandon/Johnson/Clawbonny 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| forward-mutiny | 4HfYgZ | The Adventures of Captain Hatteras | The Forward | ACH-034 | 8 | Forward 号哗变焚船；单事件核；4-char VVV → RFC-0003 Note |

- **forward-mutiny**：8 distinct solid PN（ACH 全用，四节分配）；aliases [The Burning of the Forward]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（Forward 号哗变）；泛指叛乱已剔；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：初 1 段超（425），拆分后 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（ACH），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；4-char VVV 加 RFC-0003 Note。✔
- **registry 一致**：total 1494 event 19 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug forward-mutiny ABSENT；非既有 18 event。✔
- **单指核**：ACH ch21-54 逐句确认指同一 Forward 号哗变焚船事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R238 起始计数）

| 字段 | R237 起始 | R238 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 237 | 238 |
| type_round | 3 | 4 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 173 | 174 |
| last_updated_round | 237 | 238 |

## 遗留问题

1. **event 页数 19**：本轮 +1（The Forward Mutiny）。R233 播种 4 候选（build序 1-4）全消费。registry 全库 1494，unknown 0。
2. **下轮 R238 = SCN28-zombie（首轮 event discover）**：queue(event)==0（§3(4)）；since_evv5=4<10、streak=0、since_discover=4<10。
   这是 event 类型**首次 discover 复评**：以事件锚点法扫未覆盖作品（36 部仅 9 部有 event），
   掘 net-new 事件候选（如 MS 环西伯利亚急信、SC 三大洲寻父、JCE 地心下降返程、80DA 各段冒险、FWB 气球横非洲等）。
   - 若 ≥3 净新 → productive discover，streak 保持 0，续 NEW1。
   - 若 <3 → discover_streak_low 0→1 起累积。
3. **event 建页方法论稳定**：pn_anchor 锚定 + 单事件单指核 + 四节侧面分配 + 4-char VVV（TTLU/ACH/AWED）加 RFC-0003 Note。
4. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
5. **corpus-discover 顺延**：since_corpus=173→174（dead 变量）。
6. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
7. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
