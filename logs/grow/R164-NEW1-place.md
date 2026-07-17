---
round: 164
date: 2026-07-16
type_round: 135
phase: "2.1"
current_type: place
gene: NEW1
pages: [douchak]
result: success
---

# GROW 2.1-B · R164 · NEW1 · place — 建 douchak（ASC 单源，Transcaspian 660th verst 站，11PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 135 轮（type_round 135）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、streak=0<3、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
承 R161 SCN28 补种建序（Kachgar→Tachkend→**Douchak**→Brindisi→Concepcion），建第 3 项 **Douchak**——
R161 判 11 distinctPN、ASC 单源、Transcaspian 660th verst 站。

**消歧裁定**：Douchak = Transcaspian 铁路 660th verst 站，Vernean 归属**全在《The Adventures of a Special Correspondent》**——
660th verst 6am 抵（ASC-008-022）、Noltitz 陪游（ASC-008-023）、"did" Douchak（ASC-008-028）、停半时（ASC-008-060）、
Askhabad+Douchak 补给（ASC-009-029）、线离路始（ASC-008-021）、或为英印线终点经 Kandahar（ASC-008-025）、
载 mandarin Yen Lou 尸自 Persia 赴 Pekin（ASC-010-041）、Faruskiar 于 Douchak 登车护宝（ASC-018-006）、
可疑 Mongols 于 Douchak 上车（ASC-011-017）、Faruskiar+Ghangir 于 Douchak（ASC-019-003）。
净 solid = 11（全 ASC 单源，站主体确指）。

place 计数 372→373，registry total 1440→1441，unknown 恒 0。
散文首版 max para ≤400；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10、queue 补种>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| douchak | p6t41a | The Adventures of a Special Correspondent | real | Transcaspia | 11 | Transcaspian 660th verst 站；Faruskiar 登车点；或英印线终点 |

- **douchak**：11 distinct solid PN — ASC-008-022/008-023/008-028/008-060/009-029/008-021/008-025/010-041/018-006/011-017/019-003。ASC 单源。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：douchak 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：11（ASC 单源，全 solid）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1441 place 373 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R165 起始计数）

| 字段 | R164 起始 | R165 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 164 | 165 |
| type_round | 135 | 136 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 99 | 100 |
| last_updated_round | 164 | 165 |

## 遗留问题

1. **place 页数 373**：本轮 +1。registry 全库 1441，unknown 0。
2. **下轮 R165 = NEW1**：since_evv5=4<10、since_discover=3<10、queue>0 → §3(7) NEW1。建 **Brindisi**（R161 补种序第 4，AWED 地中海邮轮港，8 distinctPN；⚠ 建前复核 ~5 solid 是否达门）。
3. **R161 补种建序进度**：✔Kachgar → ✔Tachkend → ✔Douchak → **Brindisi**(下轮) → Concepcion。
4. **净 buildable**：R161 补 5 项，消 3（Kachgar/Tachkend/Douchak），余 2（Brindisi/Concepcion）+ 既有 DEFER/hold。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=3→4，约 R171 触发。
7. **corpus-discover 顺延临界**：since_corpus=99（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
