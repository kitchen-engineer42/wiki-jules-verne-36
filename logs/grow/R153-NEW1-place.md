---
round: 153
date: 2026-07-15
type_round: 124
phase: "2.1"
current_type: place
gene: NEW1
pages: [tripoli]
result: success
---

# GROW 2.1-B · R153 · NEW1 · place — 建 tripoli（FWB 主源，撒哈拉北门户，7PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 124 轮（type_round 124）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、streak=0<3、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
承 R150 SCN28 补种建序（Nantucket✔Tunis✔→**Tripoli**→Timbuktu→Maryland），建第 3 项 **Tripoli**——
R150 判 ~7 solid，*Five Weeks in a Balloon* 主源（多源 FWB/OC/TT）。

**消歧裁定**：Tripoli = 北非海岸城（利比亚），撒哈拉北门户，Vernean 核心为 **《Five Weeks in a Balloon》探险家出发/复得城**——
Richardson/Barth/Overweg 抵 Tunis and Tripoli 赴 Mourzouk（FWB-004-007）、quitted Tripoli 12 月后抵 Ngornou（FWB-004-009）、
1855 年 8 月复得 Tripoli 唯一生还（FWB-004-012）、3 月 set out from Tripoli 赴 Mourzouk（FWB-030-015）、
line leads to Tripoli over Great Desert（FWB-037-036）；OC coast of Tripoli 灾后新岸（OC-013-002/015-039）；隐 TT-015-015 子午线过 coast of Tripoli。
净 solid = 7（FWB×5+OC×2；TT 子午线隐引未计入 7）。

place 计数 364→365，registry total 1432→1433，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10、queue>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tripoli | eRrpRd | Five Weeks in a Balloon | real | North Africa | 7 | 北非海岸城；撒哈拉北门户；FWB 探险出发/复得城；OC coast of Tripoli 灾后新岸 |

- **tripoli**：7 distinct PN — FWB-004-007（抵 Tunis/Tripoli）/004-009（quitted Tripoli 12 月）/004-012（1855-08 复得）/030-015（set out from Tripoli）/037-036（line leads to Tripoli over Great Desert）、OC-013-002（coast of Tripoli 辨伪）/015-039（新岸 upheaved 前 coast of Tripoli）。多源 FWB(5)/OC(2)。隐 TT-015-015 子午线未计。链 five-weeks-in-a-balloon/tunis/off-on-a-comet。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tripoli 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：7（两源；剔无）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1433 place 365 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R154 起始计数）

| 字段 | R153 起始 | R154 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 153 | 154 |
| type_round | 124 | 125 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 89 | 90 |
| last_updated_round | 153 | 154 |

## 遗留问题

1. **place 页数 365**：本轮 +1。registry 全库 1433，unknown 0。
2. **下轮 R154 = NEW1**：since_evv5=4<10、since_discover=3<10、queue>0 → §3(7) NEW1。建 **Timbuktu**（R150 补种序第 4，~7 solid，Robur the Conqueror 主源）。
3. **R150 补种建序进度**：✔Nantucket ✔Tunis ✔Tripoli → **Timbuktu**(下轮) → Maryland。
4. **净 buildable**：R150 补 5 项，消 3（Nantucket/Tunis/Tripoli），余 2（Timbuktu/Maryland）+ 既有 DEFER/hold 项。耗尽后须再 SCN28 或转 corpus。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=3→约 R160 触发。
7. **corpus-discover 顺延临界**：since_corpus=89（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
