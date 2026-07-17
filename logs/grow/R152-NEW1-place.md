---
round: 152
date: 2026-07-15
type_round: 123
phase: "2.1"
current_type: place
gene: NEW1
pages: [tunis]
result: success
---

# GROW 2.1-B · R152 · NEW1 · place — 建 tunis（OC 主源，Gallia 卷走 Bay of Tunis，7PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 123 轮（type_round 123）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、streak=0<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
承 R150 SCN28 补种建序（Nantucket✔→**Tunis**→Tripoli→Timbuktu→Maryland），建第 2 项 **Tunis**——
R150 判 ~7 solid，*Off on a Comet* 主源（多源 OC/FWB/RC）。

**消歧裁定**：Tunis = 北非海岸城/区域（历史突尼斯），Vernean 核心为 **《Off on a Comet》彗星 Gallia 卷走 Bay of Tunis**——
灾变后 Cape Matafuz→Tunis 尽毁（OC-012-003）、schooner Dobryna 测绘旧 Bay of Tunis 水域（OC-012-005）、
越覆盖旧 Bay of Tunis 半岛浅滩（OC-013-001）、no trace of Tunis except one rock/法王墓（OC-015-033）、
沿新岸经 what had been Tunis→Constantine 省→Ziban 绿洲（OC-018-027）；Robur Albatross 一日掠 Tunis（Cape Bon→Cape Carthage，RC-015-004）；
FWB 探险家 Richardson/Barth/Overweg 抵 Tunis and Tripoli（FWB-004-007）。净 solid = 7（OC×5+FWB×1+RC×1）。

place 计数 363→364，registry total 1431→1432，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、queue>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tunis | twcBLv | Off on a Comet | real | North Africa | 7 | 北非海岸城/区域；OC 彗星 Gallia 卷走 Bay of Tunis/Dobryna 测绘；FWB 探险抵城；RC Albatross 掠 |

- **tunis**：7 distinct PN — OC-012-003（Cape Matafuz→Tunis 尽毁）/012-005（Dobryna 测旧 Bay of Tunis）/013-001（越旧 Bay of Tunis 半岛浅滩）/015-033（no trace except 法王墓岩）/018-027（新岸经 what had been Tunis→Constantine→Ziban）、FWB-004-007（探险家抵 Tunis/Tripoli）、RC-015-004（Albatross 掠 Cape Bon→Cape Carthage）。多源 OC(5)/FWB(1)/RC(1)。链 off-on-a-comet/five-weeks-in-a-balloon。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tunis 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：7（三源；剔无）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1432 place 364 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R153 起始计数）

| 字段 | R152 起始 | R153 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 152 | 153 |
| type_round | 123 | 124 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 88 | 89 |
| last_updated_round | 152 | 153 |

## 遗留问题

1. **place 页数 364**：本轮 +1。registry 全库 1432，unknown 0。
2. **下轮 R153 = NEW1**：since_evv5=3<10、since_discover=2<10、queue>0 → §3(7) NEW1。建 **Tripoli**（R150 补种序第 3，~7 solid，Five Weeks in a Balloon 主源）。
3. **R150 补种建序进度**：✔Nantucket ✔Tunis → **Tripoli**(下轮) → Timbuktu → Maryland。
4. **净 buildable**：R150 补 5 项，消 2（Nantucket/Tunis），余 3（Tripoli/Timbuktu/Maryland）+ 既有 DEFER/hold 项。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=2→约 R160 触发。
7. **corpus-discover 顺延临界**：since_corpus=88（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
