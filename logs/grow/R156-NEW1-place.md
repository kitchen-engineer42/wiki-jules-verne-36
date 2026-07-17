---
round: 156
date: 2026-07-15
type_round: 127
phase: "2.1"
current_type: place
gene: NEW1
pages: [formentera]
result: success
---

# GROW 2.1-B · R156 · NEW1 · place — 建 formentera（OC 单源，Palmyrin Rosette 观测岛/Gallia 残岛，7PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 127 轮（type_round 127）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、streak=0<3、since_discover=0<10、queue(place)>0、stub%=0 → §3(7)）。
承 R155 SCN28 补种建序（**Formentera**→Ceuta→Samarkand→Callao），建首项 **Formentera**——
R155 判 18 distinctPN、OC 单源、Off on a Comet 关键地。

**消歧裁定**：Formentera = 巴利阿里最小岛（西地中海），Vernean 归属**全在《Off on a Comet》**——
Servadac/Timascheff 认出「one of the smallest of the Balearic Islands」（OC-025-001）、三日航抵（OC-025-011）、
彗后仅存四分之一英里残岛「sole surviving remnant of Formentera」（OC-025-042）、救隐士 Rosette 使 Gallia 人口至 36（OC-027-001）、
Rosette 离 Paris 于 Formentera 最高点设观测台（OC-029-019）、恋 solitude of Formentera（OC-029-039）、后悔 quitted quarters at Formentera（OC-038-017）。
净 solid = 7（OC 单源，全岛主体确指）+ OC-042-003 幸存岛列举（bonus，未计入 7）。

place 计数 366→367，registry total 1434→1435，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10、queue 补种>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| formentera | XITl4H | Off on a Comet | real | Balearic Islands | 7 | 巴利阿里最小岛；OC Palmyrin Rosette 观测岛；Gallia 残岛；救隐士天文学家 |

- **formentera**：7 distinct PN — OC-025-001（最小巴利阿里岛）/025-011（三日抵）/025-042（Gallia 残岛 sole surviving remnant）/027-001（救 Rosette 人口至 36）/029-019（Rosette 最高点观测台）/029-039（solitude of Formentera）/038-017（quitted quarters）。OC 单源。bonus OC-042-003 幸存岛列举。链 off-on-a-comet。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：formentera 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：7（OC 单源，全 solid）+ 1 bonus 列举。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1435 place 367 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R157 起始计数）

| 字段 | R156 起始 | R157 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 156 | 157 |
| type_round | 127 | 128 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 92 | 93 |
| last_updated_round | 156 | 157 |

## 遗留问题

1. **place 页数 367**：本轮 +1。registry 全库 1435，unknown 0。
2. **下轮 R157 = NEW1**：since_evv5=7<10、since_discover=1<10、queue>0 → §3(7) NEW1。建 **Ceuta**（R155 补种序第 2，OC 多源 OC×19+TTLU×1）。
3. **R155 补种建序进度**：✔Formentera → **Ceuta**(下轮) → Samarkand → Callao。
4. **净 buildable**：R155 补 4 项，消 1（Formentera），余 3（Ceuta/Samarkand/Callao）+ 既有 DEFER/hold。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=6→约 R160 触发（R160 时 since_evv5 将达 10）。
7. **corpus-discover 顺延临界**：since_corpus=92（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
