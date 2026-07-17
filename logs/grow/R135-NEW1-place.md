---
round: 135
date: 2026-07-15
type_round: 106
phase: "2.1"
current_type: place
gene: NEW1
pages: [nevada]
result: success
---

# GROW 2.1-B · R135 · NEW1 · place — 建 nevada（AWED 银州/Humboldt/Sierra 西壁，5PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 106 轮（type_round 106）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、streak=1<3、queue 充盈、since_discover=6<10、queue(place)>0、stub%=0 → §3(7)）。
消费 place 候选 **Nevada**（5 distinctPN，AWED 主源）。

**消歧裁定**：定主体为**州（银州/大盆地）**。gather 得 10 distinctPN，但 5 项系「Sierra Nevada 山脉」
（ASC-015-037、AWED-026-006、AWED-026-015、GM-001-006、RC-010-036 部分）与 GM-006-040（Far West 泛指）。
剔山脉泛指后取 4 项纯州级 PN（AWED-026-017/018、GM-002-003、RC-010-033）+ RC-010-036（作州西壁 Sierra 隘口，
接 RC-010-033「Sierra separates Nevada from California」框架，作 Geography 西壁地物合法引）= 5 distinctPN。

place 计数 350→351，registry total 1418→1419，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≥10、since_discover=6 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| nevada | SQvvj3 | Around the World in Eighty Days | real | United States | 5 | 银州/大盆地；Fogg 火车经 Carson Valley 入州、Reno 早餐；沿 Humboldt River 至 Humboldt Range 东界；Sierra 西壁隔加州；Godfrey Morgan 银财谚 |

- **nevada**：5 distinct PN — AWED-026-017（入 State of Nevada 经 Carson Valley/Reno）/026-018（沿 Humboldt River 至 Humboldt Range 东界）、GM-002-003（Senator Jones of Nevada 银财）、RC-010-033（Albatross 掠 Nevada 银区，Sierra 隔加州金土）/010-036（Sierra Nevada 隘口同铁路）。三源 AWED(2)/GM(1)/RC(2)。剔 Sierra Nevada 山脉泛指 5 项 + GM-006-040 泛指。链 phileas-fogg/around-the-world-in-eighty-days/robur-the-conqueror/albatross/california/great-salt-lake/godfrey-morgan。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：nevada 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：5（AWED×2 + GM×1 + RC×2；剔山脉/泛指 6 项）。✔
- **G4 脚本建页**：add_page.py（quality 自动回填 featured），未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1419 place 351 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R136 起始计数）

| 字段 | R135 起始 | R136 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 135 | 136 |
| type_round | 106 | 107 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 71 | 72 |
| last_updated_round | 135 | 136 |

## 遗留问题

1. **place 页数 351**：本轮 +1。registry 全库 1419，unknown 0。
2. **place 候选仍充盈**：queue 尚余 Illinois/Michigan/Missouri/Ohio/Colorado/Wisconsin/Iowa/Oregon/
   Soudan/Guinea/Abyssinia/Indiana 等 12 候选（部分待河/湖/泛指筛选）。
3. **待筛河/湖重叠候选**：Missouri/Ohio/Colorado（疑河）、Michigan（须与 lake-michigan 区分）。
4. **下轮 R136 预测**：NEW1（since_evv5=8<10、streak=1、queue 充盈、stub%=0）。建议序 Oregon→Iowa（AWED/RC 铁路/平原段，干净度高）。
5. **EVV5 节奏**：since_evv5=8，下次约 R138（届时 §3(1b) EVV5 触发）。
6. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
7. **散文门债**：32 页 >400（DEFERRED）；本轮页 over-400=0。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（32 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**。
