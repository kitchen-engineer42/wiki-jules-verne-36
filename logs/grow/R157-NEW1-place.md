---
round: 157
date: 2026-07-16
type_round: 128
phase: "2.1"
current_type: place
gene: NEW1
pages: [ceuta]
result: success
---

# GROW 2.1-B · R157 · NEW1 · place — 建 ceuta（OC 多源 OC×19+TTLU×1，Gibraltar 对岸摩洛哥岸点/Gallia 残岛，8PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 128 轮（type_round 128）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、streak=0<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
承 R155 SCN28 补种建序（Formentera→**Ceuta**→Samarkand→Callao），建第 2 项 **Ceuta**——
R155 判 20 distinctPN、OC 多源（OC×19+TTLU×1）、Off on a Comet 关键地。

**消歧裁定**：Ceuta = 摩洛哥海岸对 Gibraltar 的设防岬点（西地中海西门），Vernean 归属主在《Off on a Comet》——
Hansa 泊 Ceuta「exactly opposite Gibraltar」（OC-019-052）、Isaac Hakkabut 拟「cruise from Ceuta to Tripoli」（OC-020-024）、
Servadac 密谋「annexation of Ceuta to the French dominion」（OC-041-015）、英人「forestalled him in the occupation of Ceuta」（OC-041-045）、
守军「twelve miles distant from Gibraltar」（OC-041-046）、西班牙「made over Ceuta ... to the British government」（OC-041-057）、
Gallia 残片「included Ceuta and Gibraltar」（OC-042-078）；另链《20,000 Leagues》史前屏障「between Gibraltar and Ceuta」（TTLU-031-021）。
净 solid = 8（OC×7 主体确指 + TTLU×1 史前地峡）。

place 计数 367→368，registry total 1435→1436，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、queue 补种>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| ceuta | qfIk7Z | Off on a Comet | real | North Africa | 8 | Gibraltar 对岸摩洛哥岬；OC Gallia 残岛；法英争夺；TTLU 史前地峡 |

- **ceuta**：8 distinct PN — OC-019-052（Hansa 泊 Ceuta 对 Gibraltar）/020-024（Ceuta→Tripoli 巡航）/041-015（annexation to French）/041-045（English forestalled）/041-046（garrison 12mi from Gibraltar）/041-057（Spaniards made over to British）/042-078（fragment incl Ceuta+Gibraltar）；TTLU-031-021（Gibraltar-Ceuta 史前屏障闭合地中海）。OC 多源。链 off-on-a-comet。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：ceuta 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：8（OC×7 主体 + TTLU×1）全 solid。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1436 place 368 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R158 起始计数）

| 字段 | R157 起始 | R158 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 157 | 158 |
| type_round | 128 | 129 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 93 | 94 |
| last_updated_round | 157 | 158 |

## 遗留问题

1. **place 页数 368**：本轮 +1。registry 全库 1436，unknown 0。
2. **下轮 R158 = NEW1**：since_evv5=8<10、since_discover=2<10、queue>0 → §3(7) NEW1。建 **Samarkand**（R155 补种序第 3，ASC Claudius Bombarnac 大中亚铁路要站，31 distinctPN）。
3. **R155 补种建序进度**：✔Formentera → ✔Ceuta → **Samarkand**(下轮) → Callao。
4. **净 buildable**：R155 补 4 项，消 2（Formentera/Ceuta），余 2（Samarkand/Callao）+ 既有 DEFER/hold。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=7→约 R160 触发（R160 时 since_evv5 将达 10）。
7. **corpus-discover 顺延临界**：since_corpus=93（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
