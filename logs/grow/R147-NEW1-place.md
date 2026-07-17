---
round: 147
date: 2026-07-15
type_round: 118
phase: "2.1"
current_type: place
gene: NEW1
pages: [illinois]
result: success
---

# GROW 2.1-B · R147 · NEW1 · place — 建 illinois（AM Dirk Peters 居 Vandalia，7PN；三候选试筛后择富锚点州）

## 执行摘要

Phase 2.1-B place 广度扩张第 118 轮（type_round 118）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、streak=0<3、queue≈13≥10、since_discover=7<10、queue(place)>0、stub%=0 → §3(7)）。
本轮先试筛三个待筛项均**未达 gate**：Virginia（净 4：BR 烟草/FF Norfolk/FF Chesapeake/MI Richmond；剔 West Virginia + 州列举）、
Louisiana（净 3：FEM 购地 1803/FEM 岸/MW 岸；剔州/人籍列举）、Abyssinia（净 3：FWB Bruce×2/习俗；剔 GM demonym）。
转向富锚点州 **Illinois**（21 distinctPN，7 solid，An Antarctic Mystery 主源 Dirk Peters@Vandalia）。

**消歧裁定**：Vernean 核心为 **Dirk Peters（Pym 远征幸存混血）晚年隐居地 Vandalia, State of Illinois**——
AM 三处（居 Illinois/Len Guy 赴寻/「At Vandalia, State of Illinois」）；
+ AWED Mormon 史（Smith 1839 建 Nauvoo on Mississippi、1845 被逐）；MI Cyrus Smith「volunteer at Illinois under Grant」从军起点；RC Albatross 越 State of Illinois 北界过 Mississippi。
**剔州/人籍列举**：MW-004-013（Kentucky/Ohio/Tennessee/Missouri/Illinois 州列举，含 Chicago）、MW-004-023（邻州列举）、
MW-008-044（州道列举）、MW-008-038（John Hart of Illinois 人籍）、AWED-027-015（被逐州列举）、RM-023-013（巡游州列举）。
净 solid = 7（AM×3+AWED×2+MI×1+RC×1，四源）。**queue 注记的 Chicago 泛指顾虑仅涉被剔的 MW 列举**，主锚点 AM 与之无关。

place 计数 360→361，registry total 1428→1429，unknown 恒 0。
散文首版 max para 319 ≤400（首版即守门，无需复拆）；pn_validator strict 首版即全通过（Connections 词面对齐，无 warn）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈13≥10、since_discover=7 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| illinois | E2egcC | An Antarctic Mystery | real | United States | 7 | 中西部州；AM Dirk Peters 居 Vandalia + Len Guy 赴寻；AWED Mormon Nauvoo；MI Cyrus Smith 从军；RC Albatross 越州 |

- **illinois**：7 distinct PN — AM-004-046（Dirk Peters lived at Illinois）/005-026（Len Guy 赴 Illinois 寻）/017-062（At Vandalia, State of Illinois）、AWED-027-013（Smith 1839 建 Nauvoo on Mississippi）/026-003（Mormons 1845 driven from Illinois）、MI-002-004（volunteer at Illinois under Grant）、RC-009-014（State of Illinois 北界，Albatross 越 Mississippi）。四源 AM(3)/AWED(2)/MI(1)/RC(1)。剔州/人籍列举 6 项。链 an-antarctic-mystery/around-the-world-in-eighty-days/the-mysterious-island/robur-the-conqueror。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：illinois 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过（Connections 首版即词面对齐，无 warn）。✔
- **G2 段落 ≤400 字**：首版 max para 319（首版即守门）。✔
- **G3 ≥5 distinct PN**：7（四源；剔州/人籍列举 6 项）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1429 place 361 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R148 起始计数）

| 字段 | R147 起始 | R148 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 147 | 148 |
| type_round | 118 | 119 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 7 | 8 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 83 | 84 |
| last_updated_round | 147 | 148 |

## 遗留问题

1. **place 页数 361**：本轮 +1。registry 全库 1429，unknown 0。
2. **三候选试筛未达 gate（记录备后）**：Virginia 净 4、Louisiana 净 3、Abyssinia 净 3——均 <5，DEFER。
   净 buildable 明显收窄：R145 起既有 queue 待筛项多为**河/湖歧义州**（Missouri/Ohio/Colorado/Michigan 疑河湖）或**列举泛指主导**低净值项。
   Illinois 例外（AM Dirk Peters 富锚点），本轮消费。
3. **下轮 R148 = NEW1（或临 EVV5）**：since_evv5=9<10（**R149 将 ≥10 触发 §3(1b) EVV5**）、streak=0、queue≈12、since_discover=8<10 → §3(7) NEW1。
   建议序：**优先试河/湖歧义州剥离** Ohio（14PN，MW×7，剔 Ohio River）或 Missouri（14PN，AWED×4，剔 Missouri River）——
   择净 solid ≥5 者建；若均 <5 则考虑 §3(3) 早触发 SCN28 补种（HK-queue-size-scope：nominal queue_size 高估净 buildable）。
4. **待筛/DEFER 项**：Virginia（净 4，DEFER）、Louisiana（净 3，DEFER）、Abyssinia（净 3，DEFER）、Ohio/Missouri/Colorado（疑河，待剥离）、Michigan（vs lake-michigan，MW×9 疑湖）、Indiana（5，散引待筛）、Arkansas（Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）。
5. **引注对齐教训（已内化）**：R147 Connections 首版即词面对齐，strict 首版通过；散文首版即 ≤400，无复拆。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **EVV5 节奏**：since_evv5=9，**R149 触发**（§3(1b) 优先于 NEW1，届时执行质量反思，不建页，重置 since_evv5=0）。
8. **corpus-discover 顺延临界**：since_corpus=84（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope（本轮凸显：净 buildable≪nominal）、HK-premature-saturation-claim、
    HK-compute-quality-fullrun-regrade、HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、
    HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
