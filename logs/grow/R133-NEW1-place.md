---
round: 133
date: 2026-07-15
type_round: 104
phase: "2.1"
current_type: place
gene: NEW1
pages: [utah]
result: success
---

# GROW 2.1-B · R133 · NEW1 · place — 建 utah（AWED 摩门领地/Great Salt Lake，8PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 104 轮（type_round 104）。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10、streak=1<3、queue 充盈、since_discover=4<10、queue(place)>0、stub%=0 → §3(7)）。
消费 R131 补种候选 **Utah**（9 distinctPN，AWED 主源）。

**消歧裁定**：定主体为**摩门领地/州**（更高层级，含既有 salt-lake-city 城页与 great-salt-lake 湖页）。
Fogg 火车横越章 + 摩门长老布道/Brigham Young 与 Union 冲突为叙事核心。剔 GM-006-040（Far West 州列举泛指）。

place 计数 348→349，registry total 1416→1417，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≥10、since_discover=4 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| utah | FsdqIf | Around the World in Eighty Days | real | United States | 8 | 摩门领地/州；Fogg 太平洋铁路横越/长老车厢布道/Brigham Young 被囚/Union 平叛；Great Salt Lake 之乡；Humboldt Range 隘口入境；Albatross 斜掠 |

- **utah**：8 distinct PN — AWED-026-026（入 Utah，Great Salt Lake 之乡，摩门殖民地，Humboldt Range 隘口）/027-009（Union 制服 Utah 领地，囚 Brigham Young）/027-015（Union 军入 Utah 之土）/027-021（Utah 女citizens 急欲婚，摩门多妻）、GM-001-004（Utah/Oregon/California 诸州之民）、RC-010-024（Albatross 沉降 Oregon 或 Utah）/010-026（斜掠 Utah）。三源 AWED(4)/GM(1)/RC(2)。剔 GM-006-040 泛指。链 phileas-fogg/great-salt-lake/salt-lake-city/around-the-world-in-eighty-days/albatross/robur-the-conqueror。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：utah 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：8（AWED×4 + GM×1 + RC×2；剔 1 泛指）。✔
- **G4 脚本建页**：add_page.py（quality 自动回填 featured），未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1417 place 349 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R134 起始计数）

| 字段 | R133 起始 | R134 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 133 | 134 |
| type_round | 104 | 105 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 69 | 70 |
| last_updated_round | 133 | 134 |

## 遗留问题

1. **place 页数 349**：本轮 +1。registry 全库 1417，unknown 0。
2. **place 候选仍充盈**：queue 尚余 Nebraska/Nevada/Illinois/Michigan/Missouri/Ohio/Colorado/Wisconsin/Iowa/Oregon/
   Soudan/Guinea/Abyssinia/Indiana 等 14 候选（部分待河/湖/泛指筛选）。
3. **待筛河/湖重叠候选**：Missouri/Ohio/Colorado（疑河）、Michigan（须与 lake-michigan 区分）。
4. **下轮 R134 预测**：NEW1（since_evv5=6<10、streak=1、queue 充盈、stub%=0）。建议序 Nebraska→Nevada→Oregon（AWED/RC 铁路/Albatross 段，干净度高）。
5. **EVV5 节奏**：since_evv5=6，下次约 R137。
6. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
7. **散文门债**：32 页 >400（DEFERRED）；本轮页 over-400=0。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（32 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**。
