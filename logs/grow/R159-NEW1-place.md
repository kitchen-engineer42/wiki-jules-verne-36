---
round: 159
date: 2026-07-16
type_round: 130
phase: "2.1"
current_type: place
gene: NEW1
pages: [callao]
result: success
---

# GROW 2.1-B · R159 · NEW1 · place — 建 callao（PL+SC 双源，Lima 之太平洋港/Britannia 末港，9PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 130 轮（type_round 130）。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10、streak=0<3、since_discover=3<10、queue(place)>0、stub%=0 → §3(7)）。
承 R155 SCN28 补种建序末项（Formentera→Ceuta→Samarkand→**Callao**），建 **Callao**——
R155 判 14 distinctPN、PL+SC 双源（PL×5+SC×9）、Lima 之港/Britannia 末港。

**消歧裁定**：Callao = 秘鲁 Lima 之太平洋港（distinct from 既有 lima 城页——港 vs 城）。双源——
《The Pearl of Lima》：Lima 之 Port of Callao 建 1779（PL-002-006）、Annonciation 现于 Callao（PL-002-036）、
Sarah 骑向 Callao（PL-003-062）、夺 Callao 舰之谋（PL-003-063）；
《In Search of the Castaways》：Britannia 5/30 离 Callao（SC-002-075）、自 Callao 后无音讯（SC-004-005）、
Callao 补给后启航返欧（SC-033-042）、离 Callao 后侦 New Zealand（SC-063-067）。
净 solid = 9（PL×4 + SC×4~5，港主体确指，非列举）。

place 计数 369→370，registry total 1437→1438，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10、queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| callao | qUuRv9 | The Pearl of Lima | real | South America | 9 | Lima 太平洋港（区分 lima 城）；PL 港/SC Britannia 末港双源 |

- **callao**：9 distinct solid PN — PL-002-006（Port of Callao 建 1779）/002-036（Annonciation）/003-062（Sarah 骑向）/003-063（夺 Callao 舰）；SC-002-075（Britannia 离港）/004-005（自 Callao 后无音）/033-042（补给启航）/063-067（离港后侦 NZ）。PL+SC 双源。区分既有 lima（港 vs 城）。链 the-pearl-of-lima。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：callao 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：9（PL+SC 双源，全 solid）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1438 place 370 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R160 起始计数）

| 字段 | R159 起始 | R160 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 159 | 160 |
| type_round | 130 | 131 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 95 | 96 |
| last_updated_round | 159 | 160 |

## 遗留问题

1. **place 页数 370**：本轮 +1。registry 全库 1438，unknown 0。
2. **下轮 R160 = EVV5**：since_evv5 达 **10**≥10 → §3(1b) EVV5（周期质量反思，非建页）。**R155 补种批已全消（Formentera/Ceuta/Samarkand/Callao 四项尽建）**，净 buildable 归零恰逢 EVV5 触发——节奏契合。
3. **R155 补种建序完成**：✔Formentera → ✔Ceuta → ✔Samarkand → ✔Callao（4/4 全消）。
4. **净 buildable 罄**：R155 补 4 项全消，余既有 DEFER/hold（Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、Colorado/Michigan 河湖歧义）。**R160 EVV5 后（R161）须再 SCN28 深层补种**（宽扫南美/东欧/近东/远东中层 toponym，未测区尚多）。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：R160 触发（since_evv5=10）。EVV5 后 reset 0。
7. **corpus-discover 顺延临界**：since_corpus=95（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
