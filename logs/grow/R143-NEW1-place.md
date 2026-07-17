---
round: 143
date: 2026-07-15
type_round: 114
phase: "2.1"
current_type: place
gene: NEW1
pages: [kentucky]
result: success
---

# GROW 2.1-B · R143 · NEW1 · place — 建 kentucky（Mammoth Cave 地下奇观基准，6PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 114 轮（type_round 114）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、streak=0<3、queue≈11≥10、since_discover=3<10、queue(place)>0、stub%=0 → §3(7)）。
消费 R139 SCN28 新种 **Kentucky**（6 solid distinctPN，Facing the Flag 主源）。

**消歧裁定**：Vernean 核心为**猛犸洞（Mammoth Cave）所在州**——Verne 反复以之为地下宏大之基准。
FF 三处（Back Cup 对照 Mammoth Caves、"I know these Kentucky grottoes, having visited"、grottoes of Kentucky）
+ JCE（mammoth cave 500ft/40mi）+ MI（Mammoth caverns in Kentucky）+ MW（Terror near Frankfort）。
**剔异指/泛指**：MI-056-018/SI-014-019「Kentucky oxen」（牛种喻，非地名）、FEM-026-007/RM-020-019（人籍列举）、
MW-008-044/RM-023-013（州列举）、UC-007-029（假匹配，实为苏格兰郡）。净 solid = 6（FF×3+JCE×1+MI×1+MW×1）。

place 计数 356→357，registry total 1424→1425，unknown 恒 0。
散文首版 FF 段 456 过门，edit_page 分拆至 max 366 ≤400（纪律续守，就地复拆）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈11≥10、since_discover=3 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| kentucky | vnIyn9 | Facing the Flag | real | United States | 6 | 州/Mammoth Cave；FF Back Cup 对照 + 亲访；JCE/MI 猛犸洞尺度基准；MW Terror near Frankfort |

- **kentucky**：6 distinct PN — FF-009-019（Mammoth Caves in Kentucky 更广于 Back Cup）/009-020（亲访 Kentucky grottoes）/009-047（grottoes of Kentucky 之奇）、JCE-030-013（mammoth cave in Kentucky 500 呎/40 哩）、MI-057-108（Mammoth caverns in Kentucky 列世界名洞）、MW-004-013（Terror 现 Kentucky near Frankfort）。四源 FF(3)/JCE(1)/MI(1)/MW(1)。剔 Kentucky oxen 牛种喻 + 人籍/州列举 6 项。链 facing-the-flag/journey-to-the-centre-of-the-earth/the-mysterious-island/the-master-of-the-world。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：kentucky 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 FF 段 456 过门，edit_page 分拆至 max 366。✔
- **G3 ≥5 distinct PN**：6（FF×3+JCE×1+MI×1+MW×1；剔 6 项异指/泛指）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 复拆，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1425 place 357 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R144 起始计数）

| 字段 | R143 起始 | R144 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 143 | 144 |
| type_round | 114 | 115 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 79 | 80 |
| last_updated_round | 143 | 144 |

## 遗留问题

1. **place 页数 357**：本轮 +1。registry 全库 1425，unknown 0。
2. **下轮 R144 = NEW1**：since_evv5=5<10、streak=0、queue≈10≥10、since_discover=4<10 → §3(7) NEW1。
   建议序（承 R139 discover 末项）：Massachusetts（BR Fort Sumter「Massachusetts granite」+ DSCF Salem 棉布 + MW×3）。
   R139 五 buildable 消费至此仅余 Massachusetts；其后转既有 queue 待筛项（须消歧）。
3. **待筛/DEFER 项**：Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Soudan/Guinea/Abyssinia/Indiana（既有 queue）。
4. **散文门债**：37 页 >400（既有 DEFERRED）；本轮首版过门即就地复拆，over-400=0。
5. **EVV5 节奏**：since_evv5=5，下次约 R149（half-way）。
6. **corpus-discover 顺延临界**：since_corpus=80（HK-corpus-discover-not-in-statemachine PARK）。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**。
