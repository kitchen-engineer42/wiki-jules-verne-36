---
round: 145
date: 2026-07-15
type_round: 116
phase: "2.1"
current_type: place
gene: NEW1
pages: [soudan]
result: success
---

# GROW 2.1-B · R145 · NEW1 · place — 建 soudan（FWB Victoria 越 Soudan 边界，9PN；R139 五 buildable 后首个既有 queue 项）

## 执行摘要

Phase 2.1-B place 广度扩张第 116 轮（type_round 116）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、streak=0<3、queue≈15≥10、since_discover=5<10、queue(place)>0、stub%=0 → §3(7)）。
R139 五 buildable 已于 R144 收官，本轮转消费既有 queue 待筛项，选**非河/湖歧义**的 **Soudan**
（中非历史大区，FWB 气球航路核心，9 solid distinctPN，Five Weeks in a Balloon 主源）。

**消歧裁定**：Vernean 核心为**《Five Weeks in a Balloon》气球 Victoria 穿越之非洲内陆带**——
Ferguson 博士历数入 Soudan 的探险家（Barth 受命/Brun-Rollet 东 Soudan 领事/Vogel 1853 入 Soudan），
其图册按 Barth 记 Soudan，Clapperton/Oudney 穿 Soudan country 抵 Sackatoo，Victoria 越 Belad el Djerid 达 Soudan 边界。
OC Servadac 二役之一在 Soudan（Ben Zoof 在此报救命之恩）；WC 地理学家 Durrien 游历 Soudan。
**剔 demonym/列举**：FWB-020-008「A Soudan negro」（族称）、GM-018-004「negro from Soudan or Abyssinia」（族称/出身）、
FWB-002-004（Barth/Livingstone/Burton/Speke 探险家列举）、OC-003-006（「_Campaigns:_ Soudan and Japan」履历裸列）。
净 solid = 9（FWB×6+OC×2+WC×1，三源）。

place 计数 358→359，registry total 1426→1427，unknown 恒 0。
散文 max para 341 ≤400（首版即守门，无需复拆）；pn_validator strict 首版即全通过（Connections 词面对齐，无 warn）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈15≥10、since_discover=5 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| soudan | dnzqYj | Five Weeks in a Balloon | real | Africa | 9 | 中非大区；FWB Ferguson 探险史 + Victoria 越边界；OC Servadac 二役之一；WC Durrien 游历 |

- **soudan**：9 distinct PN — FWB-004-005（Barth 受命 mission in the Soudan）/004-017（Brun-Rollet 东 Soudan 领事）/005-063（Vogel 1853 入 Soudan）/012-067（图册按 Barth 记 Soudan）/030-015（Clapperton/Oudney 穿 Soudan country 抵 Sackatoo）/034-022（Victoria 越 border of the Soudan）、OC-003-014（Servadac 二役 Soudan/Japan）/003-018（Ben Zoof 在 Soudan 报恩）、WC-013-004（Durrien 游历 Asia Minor and the Soudan）。三源 FWB(6)/OC(2)/WC(1)。剔族称 2 项 + 列举 2 项。链 five-weeks-in-a-balloon/off-on-a-comet/the-waif-of-the-cynthia。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：soudan 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过（首版即无 warn，Connections 词面已对齐）。✔
- **G2 段落 ≤400 字**：max para 341（首版即守门）。✔
- **G3 ≥5 distinct PN**：9（三源；剔 4 项族称/列举）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1427 place 359 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R146 起始计数）

| 字段 | R145 起始 | R146 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 145 | 146 |
| type_round | 116 | 117 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 81 | 82 |
| last_updated_round | 145 | 146 |

## 遗留问题

1. **place 页数 359**：本轮 +1。registry 全库 1427，unknown 0。
2. **R139 五 buildable 收官后首个既有 queue 项**：Soudan 为非河/湖歧义之干净候选（FWB 气球航路核心）。
3. **下轮 R146 = NEW1**：since_evv5=7<10、streak=0、queue≈14≥10、since_discover=6<10 → §3(7) NEW1。
   建议序：既有 queue 待筛项。Guinea（16 distinctPN，Gulf of Guinea vs region 须消歧）或 Virginia（BR 烟草/FF Norfolk 城，凑 solid ≥5）。
   **注意**：净 buildable 渐减，since_discover 累积；若 queue_size 跌破 10 或 since_discover≥10，将触发 §3(3) SCN28 复扫补种。
4. **待筛/DEFER 项**：Guinea（Gulf vs region）、Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Abyssinia/Indiana（既有 queue，borderline）。
5. **引注对齐教训（已内化）**：R145 Connections 首版即词面对齐（每引子句复用源句特征词，不挤多引于一句），strict 首版通过，无 warn→修正循环。R142/R144 教训已成稳定实践。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（首版即守门）。
7. **EVV5 节奏**：since_evv5=7，下次约 R149。
8. **corpus-discover 顺延临界**：since_corpus=82（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
