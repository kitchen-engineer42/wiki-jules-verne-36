---
round: 162
date: 2026-07-16
type_round: 133
phase: "2.1"
current_type: place
gene: NEW1
pages: [kachgar]
result: success
---

# GROW 2.1-B · R162 · NEW1 · place — 建 kachgar（ASC 单源，Chinese Turkestan 首府/Grand Transasiatic 俄华枢纽，13PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 133 轮（type_round 133）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、streak=0<3、since_discover=0<10、queue(place)>0、stub%=0 → §3(7)）。
承 R161 SCN28 补种建序（**Kachgar**→Tachkend→Douchak→Brindisi→Concepcion），建首项 **Kachgar**——
R161 判 24 distinctPN、ASC 单源、Chinese Turkestan 首府。

**消歧裁定**：Kachgar（alias Kashgar）= 中亚 Chinese Turkestan 首府，Vernean 归属**全在《The Adventures of a Special Correspondent》**——
Grand Transasiatic 华属段门（ASC-008-032）、4:30 抵「capital of Chinese Turkestan」（ASC-015-075）、
华境险地（ASC-013-108）、double town 新旧城 Yangi-Chahr vs Kachgar（ASC-016-007/016-009/016-011）、
昔首府今降俄华线枢纽（ASC-016-008）、俄手商贸中心（ASC-016-012）、Turkoman 民杂华人（ASC-016-014）、
华兵于 Kachgar 接管车厢（ASC-018-007）、1873–74 英使团 Chapman/Gordon（ASC-016-013）、Russians lord it（ASC-016-002）。
剔 ASC-005-018 站名并列。净 solid = 13（全 ASC 单源，城主体确指）。

place 计数 370→371，registry total 1438→1439，unknown 恒 0。
alias Kashgar 建前查重确认无既有页（NEW）。散文首版 max para ≤400；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10、queue 补种>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| kachgar | WedhEW | The Adventures of a Special Correspondent | real | Chinese Turkestan | 13 | Chinese Turkestan 首府；俄华线枢纽；double town；alias Kashgar |

- **kachgar**：13 distinct solid PN — ASC-008-032/015-075/013-108/017-007/016-007/016-009/016-011/016-008/016-012/016-014/018-007/016-013/016-002。ASC 单源。剔 005-018 站名列举。alias Kashgar。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：kachgar 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：13（ASC 单源，全 solid，已剔列举）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1439 place 371 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R163 起始计数）

| 字段 | R162 起始 | R163 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 162 | 163 |
| type_round | 133 | 134 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 97 | 98 |
| last_updated_round | 162 | 163 |

## 遗留问题

1. **place 页数 371**：本轮 +1。registry 全库 1439，unknown 0。
2. **下轮 R163 = NEW1**：since_evv5=2<10、since_discover=1<10、queue>0 → §3(7) NEW1。建 **Tachkend**（R161 补种序第 2，ASC 俄属突厥斯坦城，15 distinctPN，alias Tashkend）。
3. **R161 补种建序进度**：✔Kachgar → **Tachkend**(下轮) → Douchak → Brindisi → Concepcion。
4. **净 buildable**：R161 补 5 项，消 1（Kachgar），余 4（Tachkend/Douchak/Brindisi/Concepcion）+ 既有 DEFER/hold。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=1→2，约 R171 触发。
7. **corpus-discover 顺延临界**：since_corpus=97（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
