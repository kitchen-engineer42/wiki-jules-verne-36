---
round: 146
date: 2026-07-15
type_round: 117
phase: "2.1"
current_type: place
gene: NEW1
pages: [guinea]
result: success
---

# GROW 2.1-B · R146 · NEW1 · place — 建 guinea（FWB Gulf of Guinea 航路参照，6PN；重消歧 New Guinea/动植物）

## 执行摘要

Phase 2.1-B place 广度扩张第 117 轮（type_round 117）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、streak=0<3、queue≈14≥10、since_discover=6<10、queue(place)>0、stub%=0 → §3(7)）。
续 R145 消费既有 queue 待筛项，选 **Guinea**（西非海岸大区 + Gulf of Guinea，FWB 气球航路参照，6 solid distinctPN，Five Weeks in a Balloon 主源）。

**消歧裁定**：Vernean 核心为**西非几内亚海岸/几内亚湾**——Ferguson 以「距 Gulf of Guinea 三百哩」定位气球，
内陆分水岭定水系归 Gulf of Guinea 或 Cape Verde 湾，几内亚海岸有蛮族出没；RC Albatross 越 northern Guinea（Sudan 与湾之间），
Trans-Saharan Railway 拟通 Gulf of Guinea；DSCF Lower Guinea 殖民地为落难者庇护。
**重消歧剔除**：**New Guinea/Papua**（SC-033-041、TTLU-020-021/020-060/025-024 — 大洋洲异指，非洲外）、
**动植物**（DSCF-021-076「Guinea fowls」珍珠鸡、DSCF-031-012「Goliaths of Guinea」甲虫）、
**列举**（ACH-012-051 发现地列表、TT-015-019/015-030 淹没区列举、MI-025-038 树种列举误匹配）。
净 solid = 6（FWB×3+RC×2+DSCF×1，三源）。

place 计数 359→360，registry total 1427→1428，unknown 恒 0。
散文首版 FWB 段 515 过门，edit_page 分拆首句独立段至 max 354 ≤400（纪律续守，就地复拆）；
pn_validator strict 两版均全通过（Connections 首版即词面对齐，无 warn）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈14≥10、since_discover=6 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| guinea | U6cFPe | Five Weeks in a Balloon | real | Africa | 6 | 西非海岸/几内亚湾；FWB 气球定位参照 + 海岸蛮族；RC Albatross 越 northern Guinea；DSCF Lower Guinea 殖民地 |

- **guinea**：6 distinct PN — FWB-024-049（距 Gulf of Guinea 三百哩定位）/041-002（分水岭归 Gulf of Guinea vs Cape Verde 湾）/040-004（coasts of Guinea 蛮族）、RC-015-050（Albatross 越 mountains of northern Guinea）/015-013（Trans-Saharan Railway 拟通 Gulf of Guinea）、DSCF-035-040（colonies of Lower Guinea 庇护）。三源 FWB(3)/RC(2)/DSCF(1)。剔 New Guinea/Papua 4 项 + 动植物 2 项 + 列举 3 项。链 five-weeks-in-a-balloon/robur-the-conqueror/dick-sand-a-captain-at-fifteen。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：guinea 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过（Connections 首版即词面对齐，无 warn）。✔
- **G2 段落 ≤400 字**：首版 FWB 段 515 过门，edit_page 分拆至 max 354。✔
- **G3 ≥5 distinct PN**：6（三源；剔 New Guinea/动植物/列举 9 项）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 复拆，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1428 place 360 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R147 起始计数）

| 字段 | R146 起始 | R147 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 146 | 147 |
| type_round | 117 | 118 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 82 | 83 |
| last_updated_round | 146 | 147 |

## 遗留问题

1. **place 页数 360**：本轮 +1。registry 全库 1428，unknown 0。
2. **重消歧样本**：Guinea 同名异指丰富（New Guinea/Papua 大洋洲、Guinea fowl 禽、Goliaths of Guinea 甲虫），保留于日志供后续同类消歧参考。
3. **下轮 R147 = NEW1**：since_evv5=8<10、streak=0、queue≈13≥10、since_discover=7<10 → §3(7) NEW1。
   建议序：Virginia（BR 烟草/FF Norfolk + MI/MW/RM/DSCF；8 distinctPN，须剔州/城列举，凑 solid ≥5）或 Louisiana（FEM 1803 购地×4 + Gulf；须剔泛指）。
   **注意**：since_evv5→8，EVV5 临近（≥10 于 R149 触发 §3(1b)）；净 buildable 渐减，since_discover 累积，若跌破阈值触发 SCN28。
4. **待筛/DEFER 项**：Virginia（州/城列举待筛）、Louisiana（FEM 购地 + Gulf 泛指）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Abyssinia/Indiana（borderline）。
5. **引注对齐教训（已内化）**：R146 Connections 首版即词面对齐，strict 首版通过。散文门首版 FWB 段仍超（515），已就地复拆——首版起句控 ≤400 仍需注意长引句拆分。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮首版过门即就地复拆，over-400=0。
7. **EVV5 节奏**：since_evv5=8，下次约 R149（§3(1b) 将优先于 NEW1）。
8. **corpus-discover 顺延临界**：since_corpus=83（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
