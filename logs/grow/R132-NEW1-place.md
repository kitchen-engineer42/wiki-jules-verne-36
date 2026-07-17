---
round: 132
date: 2026-07-15
type_round: 103
phase: "2.1"
current_type: place
gene: NEW1
pages: [senegal]
result: success
---

# GROW 2.1-B · R132 · NEW1 · place — 建 senegal（FWB 气球航路西非终点，11PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 103 轮（type_round 103）。承 R131 证伪饱和误判、queue 补种 17 候选后，
本轮回归常规 NEW1，消费 R131 补种强候选 **Senegal**（25 distinctPN，FWB 主源）。
决策机 §3 首匹配 **NEW1**（since_evv5=4<10、streak=1<3、queue 充盈≥10、since_discover=3<10、
queue(place)>0、stub%=0 → §3(7)）。

**消歧裁定**：Senegal 25 PN 分河义（Senegal River，FWB 气球坠落终点/Gouina 瀑布）与区域义（法属殖民地/西非地区）。
鉴于 senegal 与 senegal-river 页均不存在，定**主体为西非区域/法属殖民地**（更高层级，含河为核心特征），
统合区域引（colony/governor/coast/Fonta-Jallon）+ 河作为其地理特征引（basin/cataracts/Medina），凑 11 干净引。

place 计数 347→348，registry total 1415→1416，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≥10、since_discover=3 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| R131 补种后≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| senegal | jgvSUe | Five Weeks in a Balloon | real | West Africa | 11 | Ferguson 气球航路西非终点/法属殖民地；Senegal River 为核心特征（Gouina 瀑布 breadth 2000ft/落差 150ft）；Medina 哨站；Fonta-Jallon/Foullah/Mandingo；Niger↔Senegal 分水岭 |

- **senegal**：11 distinct PN — 区域义 FWB-008-022（Zanzibar 至 Senegal 海岸距离）/041-003（Senegal 前此段非洲危险）/041-022（法国殖民者占 Senegal 殖民地）/042-002（离 Senegal 25 里）/044-002（Senegal 总督遣队）/038-037（抵 Senegal 入 Fonta-Jallon）、SC-008-031（Senegal 有同胞）；河义（作区域核心特征）FWB-041-002（Niger↔Senegal 流域分水岭）/043-067（Senegal 瀑布 breadth 2000ft 落差 150ft）/044-010（河上 Medina 哨站）、TTLU-032-002（Senegal 列世界大河）。三源 FWB(9)/SC(1)/TTLU(1)。链 five-weeks-in-a-balloon/africa/cape-verde/timbuctoo。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：senegal 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：11（FWB×9 + SC×1 + TTLU×1）。✔
- **G4 脚本建页**：add_page.py 建立（quality 自动回填 featured），未用 Write/Edit 触碰页面。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1416 place 348 unknown 0。✔
- **排除检查**：commit 前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R133 起始计数）

| 字段 | R132 起始 | R133 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 132 | 133 |
| type_round | 103 | 104 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 1 | 1（NEW1 不动 streak）|
| rounds_since_last_corpus_discover | 68 | 69 |
| last_updated_round | 132 | 133 |

## 遗留问题

1. **place 页数 348**：本轮 +1。registry 全库 1416，unknown 0。
2. **place 候选充盈**：queue 尚余 Utah/Nebraska/Nevada/Illinois/Michigan/Missouri/Ohio/Colorado/Wisconsin/Iowa/Oregon/
   Soudan/Guinea/Abyssinia/Indiana 等 15 候选（部分待河/湖/泛指筛选）。CLOSE 时机远未至。
3. **待筛河/湖重叠候选**：Missouri/Ohio/Colorado（疑河）、Michigan（须与 lake-michigan 区分州/湖）——建前须逐一查主体。
4. **下轮 R133 预测**：NEW1（since_evv5=5<10、streak=1、queue 充盈、stub%=0）。建议序 Utah→Nebraska→Nevada（AWED 横美铁路段，干净度高）。
5. **EVV5 节奏**：since_evv5=5，下次约 R137。
6. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
7. **散文门债**：32 页 >400（DEFERRED）；本轮页 over-400=0，无新增。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（32 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**：泛指风险；州级/区域级页更干净，优先消化。
