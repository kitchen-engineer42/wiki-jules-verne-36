---
round: 163
date: 2026-07-16
type_round: 134
phase: "2.1"
current_type: place
gene: NEW1
pages: [tachkend]
result: success
---

# GROW 2.1-B · R163 · NEW1 · place — 建 tachkend（ASC 单源，俄属突厥斯坦城/Grand Transasiatic 停站，11PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 134 轮（type_round 134）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、streak=0<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
承 R161 SCN28 补种建序（Kachgar→**Tachkend**→Douchak→Brindisi→Concepcion），建第 2 项 **Tachkend**——
R161 判 15 distinctPN、ASC 单源、俄属突厥斯坦城。

**消歧裁定**：Tachkend（alias Tashkend）= 中亚俄属突厥斯坦城（Samarkand 东北 300km），
Vernean 归属**全在《The Adventures of a Special Correspondent》**——睡至 Tachkend（ASC-013-005）、
Sarthe pedlars 群赴（ASC-006-011）、停 2.5h（ASC-014-003）、11am 离（ASC-014-014）、南弯赴 Khodjend（ASC-014-029）、
Samarkand→300km（ASC-013-006）、旧城女子（ASC-014-010）、突厥斯坦民（ASC-014-007）、犹太人聚居（ASC-014-008）、
1887 震迹（ASC-015-031）、1870 俄设集市敌 Nijni-Novgorod（ASC-014-001）、Khotan 丝出口 Tachkend-Koulja（ASC-016-012）。
剔 005-018/005-023/018-035 站名/路线并列。净 solid = 11（全 ASC 单源，城主体确指）。

place 计数 371→372，registry total 1439→1440，unknown 恒 0。
alias Tashkend 建前查重确认无既有页。散文首版 max para ≤400；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、queue 补种>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tachkend | 8mDpfG | The Adventures of a Special Correspondent | real | Central Asia | 11 | 俄属突厥斯坦城；Grand Transasiatic 停站；alias Tashkend |

- **tachkend**：11 distinct solid PN — ASC-013-005/006-011/014-003/014-014/014-029/013-006/014-010/014-007/014-008/015-031/014-001/016-012。ASC 单源。剔 005-018/005-023/018-035 列举。alias Tashkend。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tachkend 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：11（ASC 单源，全 solid，已剔列举）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1440 place 372 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R164 起始计数）

| 字段 | R163 起始 | R164 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 163 | 164 |
| type_round | 134 | 135 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 98 | 99 |
| last_updated_round | 163 | 164 |

## 遗留问题

1. **place 页数 372**：本轮 +1。registry 全库 1440，unknown 0。
2. **下轮 R164 = NEW1**：since_evv5=3<10、since_discover=2<10、queue>0 → §3(7) NEW1。建 **Douchak**（R161 补种序第 3，ASC Transcaspian 660th verst 站，11 distinctPN）。
3. **R161 补种建序进度**：✔Kachgar → ✔Tachkend → **Douchak**(下轮) → Brindisi → Concepcion。
4. **净 buildable**：R161 补 5 项，消 2（Kachgar/Tachkend），余 3（Douchak/Brindisi/Concepcion）+ 既有 DEFER/hold。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=2→3，约 R171 触发。
7. **corpus-discover 顺延临界**：since_corpus=98（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
