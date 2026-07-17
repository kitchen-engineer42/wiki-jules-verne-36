---
round: 158
date: 2026-07-16
type_round: 129
phase: "2.1"
current_type: place
gene: NEW1
pages: [samarkand]
result: success
---

# GROW 2.1-B · R158 · NEW1 · place — 建 samarkand（ASC 单源，大中亚铁路要站/Sogd 谷古城，10PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 129 轮（type_round 129）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、streak=0<3、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
承 R155 SCN28 补种建序（Formentera→Ceuta→**Samarkand**→Callao），建第 3 项 **Samarkand**——
R155 判 31 distinctPN、ASC 单源、Grand Transasiatic 铁路关键停站。

**消歧裁定**：Samarkand = 中亚 Sogd 谷古城，Vernean 归属**全在《The Adventures of a Special Correspondent》**——
Claudius Bombarnac 沿 Grand Transasiatic 五小时停（ASC-012-003）、incomparable city（ASC-012-049）、long run（ASC-013-004）、
位 Zarafchane/Sogd 谷（ASC-012-001）、Amou-Daria 支流所抵城（ASC-010-072）、俄铺 quadrilateral 广场（ASC-012-019）、
bazaar（ASC-012-031）、至 Tachkend 300km（ASC-013-006）、Cyrus BC329 焚/Genghis 1219 毁（ASC-012-002）、
Irdjar-Zera-Buleh 战后归属（ASC-007-018）。
**剔站名列举**：ASC-005-018/005-023/006-008 等 Merv/Bokhara/Samarkand/... 并列不单计。净 solid ≥10（全 ASC 单源，城主体确指）。

place 计数 368→369，registry total 1436→1437，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10、queue 补种>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| samarkand | L7zz7h | The Adventures of a Special Correspondent | real | Central Asia | 10 | Sogd 谷古城；Grand Transasiatic 要站；Cyrus/Genghis 史 |

- **samarkand**：10 distinct solid PN — ASC-012-001（Zarafchane/Sogd 谷）/010-072（Amou-Daria 支流所抵城）/012-003（五小时停）/012-019（quadrilateral 广场）/012-031（bazaar）/013-006（至 Tachkend 300km）/012-002（Cyrus-Genghis 史）/007-018（Irdjar 战后归属）/012-049（incomparable city）/013-004（long run）。ASC 单源。剔 Merv/Bokhara 并列列举（005-018/005-023/006-008）。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：samarkand 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：10（ASC 单源，全 solid，已剔列举）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1437 place 369 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R159 起始计数）

| 字段 | R158 起始 | R159 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 158 | 159 |
| type_round | 129 | 130 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 94 | 95 |
| last_updated_round | 158 | 159 |

## 遗留问题

1. **place 页数 369**：本轮 +1。registry 全库 1437，unknown 0。
2. **下轮 R159 = NEW1**：since_evv5=9<10、since_discover=3<10、queue>0 → §3(7) NEW1。建 **Callao**（R155 补种序第 4，PL+SC 双源 Lima 之港，14 distinctPN）。
3. **R155 补种建序进度**：✔Formentera → ✔Ceuta → ✔Samarkand → **Callao**(下轮)。
4. **净 buildable**：R155 补 4 项，消 3（Formentera/Ceuta/Samarkand），余 1（Callao）+ 既有 DEFER/hold。**R160 起净罄，须 SCN28 或触 EVV5。**
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=8→9，**R160 触发**（R160 时 since_evv5 达 10 → §3(1b) EVV5）。R159 建 Callao 后即撞 EVV5，非 NEW1。
7. **corpus-discover 顺延临界**：since_corpus=94（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
