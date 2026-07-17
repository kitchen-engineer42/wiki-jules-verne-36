---
round: 141
date: 2026-07-15
type_round: 112
phase: "2.1"
current_type: place
gene: NEW1
pages: [sacramento]
result: success
---

# GROW 2.1-B · R141 · NEW1 · place — 建 sacramento（Pacific Railroad 西端 / Godfrey Morgan 北矿都，6PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 112 轮（type_round 112）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、streak=0<3、queue≈13≥10、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
消费 R139 SCN28 新种 **Sacramento**（6 solid distinctPN，Around the World in Eighty Days 主源）。

**消歧裁定**：定主体为**加州首府城 / Sacramento River**。Vernean 核心为《AWED》太平洋铁路西端
（离 Sacramento 经 Roclin/Auburn/Colfax 入 Sierra Nevada、SF↔Sacramento 乡野、Sacramento River 多层汽船）
+《Godfrey Morgan》北加矿都（vs Stockton 南矿）与立法首府（Legislative Council of Sacramento）。
**剔异指**：EHLA×2「pampas/plain of Sacramento」系亚马逊流域异地（南美，非加州）；
GM-001-003/006-042「Sacramento Street」系 San Francisco 街名（非城）；GM-006-017 系感叹语（弱）。
净 solid = 6（AWED×4 + GM×2）。

place 计数 354→355，registry total 1422→1423，unknown 恒 0。散文 max para 320 ≤400（首版即守门）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈13≥10、since_discover=1 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| sacramento | XHlwJJ | Around the World in Eighty Days | real | California | 6 | 加州首府/Sacramento River；AWED 铁路西端；GM 北矿都 vs Stockton + 立法首府 |

- **sacramento**：6 distinct PN — AWED-026-006（Pacific Railroad Omaha→加州岸，西端近 Sacramento）/026-015（离 Sacramento 经 Roclin/Auburn/Colfax 入 Sierra Nevada）/026-014（SF↔Sacramento 乡野不甚丘陵）/025-002（Sacramento River 多层汽船 + 各国 clippers）、GM-002-037（Sacramento 北加矿都，vs Stockton 南矿）、GM-002-041（Legislative Council of Sacramento 立法首府）。两源 AWED(4)/GM(2)。**剔异指**：EHLA-005-025/010-006 亚马逊 pampas of Sacramento、GM-001-003/006-042 SF Sacramento Street、GM-006-017 感叹语。链 around-the-world-in-eighty-days/godfrey-morgan/san-francisco。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：sacramento 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：max para 320（首版即守门，无需复拆）。✔
- **G3 ≥5 distinct PN**：6（AWED×4 + GM×2；剔异指 5 项）。✔
- **G4 脚本建页**：add_page.py，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1423 place 355 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R142 起始计数）

| 字段 | R141 起始 | R142 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 141 | 142 |
| type_round | 112 | 113 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 77 | 78 |
| last_updated_round | 141 | 142 |

## 遗留问题

1. **place 页数 355**：本轮 +1。registry 全库 1423，unknown 0。
2. **下轮 R142 = NEW1**：since_evv5=3<10、streak=0、queue≈12≥10、since_discover=2<10 → §3(7) NEW1。
   建议序（承 R139 discover）：Pennsylvania（DSCF/MW）→ Kentucky（Mammoth Cave）→ Massachusetts（Salem/granite/MW）。
3. **待筛/DEFER 项**：Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Soudan/Guinea/Abyssinia/Indiana（既有 queue）。
4. **散文门债**：37 页 >400（既有 DEFERRED）；**本轮页 over-400=0**（首版即守门，纪律续守）。
5. **EVV5 节奏**：since_evv5=3，下次约 R149。
6. **corpus-discover 顺延临界**：since_corpus=77（HK-corpus-discover-not-in-statemachine PARK）。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**。
