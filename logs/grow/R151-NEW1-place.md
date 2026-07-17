---
round: 151
date: 2026-07-15
type_round: 122
phase: "2.1"
current_type: place
gene: NEW1
pages: [nantucket]
result: success
---

# GROW 2.1-B · R151 · NEW1 · place — 建 nantucket（AM 单源，Pym 出生地/Bedford School，7PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 122 轮（type_round 122）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、streak=0<3、queue 补种后 since_discover=0<10、queue(place)>0、stub%=0 → §3(7)）。
承 R150 SCN28 补种建序（Nantucket→Tunis→Tripoli→Timbuktu→Maryland），建首项 **Nantucket**——
R150 判 ~8 solid、最强候选，*An Antarctic Mystery* 单源。

**消歧裁定**：Nantucket = 马萨诸塞外海岛，Vernean 核心为 **《An Antarctic Mystery》Arthur Gordon Pym 出生地**——
Captain Len Guy 审问 Jeorling 时反复锚定：Nantucket 为 Pym 出生地（AM-003-054）、Poe romance 起点（AM-003-055）、
Jeorling 曾访岛（AM-004-023）、Pym 家族居岛（AM-004-030）、Pym born at Nantucket + Bedford School（AM-005-004）、
Penguin 幸存者送回 Nantucket（AM-005-005）、哗变捕鲸航 thirty days out from Nantucket（AM-005-035）。
**剔** AM-005-076 footnote「Nantucket youth」（demonym 泛指）。净 solid = 7（AM 单源，全为岛主体确指）。

place 计数 362→363，registry total 1430→1431，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10、queue 补种后>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| nantucket | 5SFDJS | An Antarctic Mystery | real | United States | 7 | 马萨诸塞外海岛；Pym 出生地/Bedford School；Len Guy 审 Jeorling 锚定 Poe romance 起点；AM 单源 |

- **nantucket**：7 distinct PN — AM-003-054（Nantucket 为 Pym 出生地）/003-055（Poe romance 起点）/004-023（Jeorling belongs to Connecticut + 访 Nantucket）/004-030（Pym family lived in Nantucket Island）/005-004（born at Nantucket + Bedford School）/005-005（Penguin 送回 Nantucket）/005-035（thirty days out from Nantucket 哗变启航）。单源 AM(7)。剔 005-076 footnote demonym。链 an-antarctic-mystery/connecticut。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：nantucket 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：7（单源 AM；剔 footnote demonym 1 项）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1431 place 363 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R152 起始计数）

| 字段 | R151 起始 | R152 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 151 | 152 |
| type_round | 122 | 123 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 87 | 88 |
| last_updated_round | 151 | 152 |

## 遗留问题

1. **place 页数 363**：本轮 +1。registry 全库 1431，unknown 0。
2. **下轮 R152 = NEW1**：since_evv5=2<10、since_discover=1<10、queue>0 → §3(7) NEW1。建 **Tunis**（R150 补种序第 2，~7 solid，Off on a Comet 主源）。
3. **R150 补种建序进度**：✔Nantucket → **Tunis**(下轮) → Tripoli → Timbuktu → Maryland。
4. **单源页说明**：nantucket 7 PN 全 AM，单源但均岛主体确指、无异指混入，达 ≥5 solid distinctPN 门。
5. **净 buildable**：R150 补 5 项，消 1（Nantucket），余 4（Tunis/Tripoli/Timbuktu/Maryland）+ 既有 DEFER/hold 项。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **EVV5 节奏**：since_evv5=1→约 R160 触发。
8. **corpus-discover 顺延临界**：since_corpus=87（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
