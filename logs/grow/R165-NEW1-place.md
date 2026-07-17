---
round: 165
date: 2026-07-16
type_round: 136
phase: "2.1"
current_type: place
gene: NEW1
pages: [concepcion]
result: success
---

# GROW 2.1-B · R165 · NEW1 · place — 建 concepcion（SC 单源，智利古城/Duncan 南美登陆点，6PN）；Brindisi 建前复核净 4 → DEFER

## 执行摘要

Phase 2.1-B place 广度扩张第 136 轮（type_round 136）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、streak=0<3、since_discover=3<10、queue(place)>0、stub%=0 → §3(7)）。
承 R161 SCN28 补种建序末段（Kachgar→Tachkend→Douchak→**Brindisi**→**Concepcion**）。

**建前复核裁定（关键）**：R161 vet 标 Brindisi/Concepcion 均「~5 临界，建前复核」。本轮逐条复核：
- **Brindisi 净 clean solid = 4**（AWED-006-003 Mongolia 往返 Brindisi-Bombay/006-007 直自 Brindisi/006-008 载印度邮/009-002 客赴印）。
  剔 003-012 港名并列 + 003-029/007-031/007-032 行程表列举（enumeration）。距 5 门 1，**与 Virginia 同款 DEFER，本轮不建**。
- **Concepcion 净 solid = 6**（达门）→ 建。

**Concepcion 消歧裁定**：智利 Concepcion 城（Talcahuano 湾内陆侧），Vernean 归属**全在《In Search of the Castaways》**——
Duncan 航向 Concepcion 如向 Calcutta（SC-007-046）、Paganel 抵城前习语（SC-009-006）、英领事居城外一时程（SC-010-004）、
「ancient city of brave men」震后成妇孺村（SC-010-005）、目的地对白确指「To Concepcion」（SC-007-038）/「At Concepcion」（SC-008-066）。
**区分既有 bay-of-talcahuano**（城 vs 港：Concepcion 为内陆城，Talcahuano 为其港湾）——HK-blindspot 建前查重确认 concepcion/concepción 均 NEW。
净 solid = 6（SC 单源，城主体确指）。

place 计数 373→374，registry total 1441→1442，unknown 恒 0。
散文首版 max para ≤400；**Connections 首版有 ungrounded embroidery（37 平行线/Andes/pampas 非 Concepcion 句所载），建前自查即改写为纯 grounded**；pn_validator strict 全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10、queue 补种>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| concepcion | oYShag | In Search of the Castaways | real | Chile | 6 | 智利古城/Duncan 南美登陆点；区分 bay-of-talcahuano（城 vs 港）|
| ~~brindisi~~ | — | — | — | — | 4 | **DEFER**：净 clean solid=4（剔港名/行程表列举）；距门 1，同 Virginia |

- **concepcion**：6 distinct solid PN — SC-007-046（Duncan 航向）/009-006（抵城前习语）/010-004（英领事居城外一时程）/010-005（古勇士城成妇孺村）/007-038（To Concepcion 对白）/008-066（At Concepcion 对白）。SC 单源。区分既有 bay-of-talcahuano。链 in-search-of-the-castaways。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：concepcion 全句源自 sentence_index；首版 Connections 有 ungrounded 叙述，建前自查改写为纯 grounded；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400。✔
- **G3 ≥5 distinct PN**：6（SC 单源，全 solid）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1442 place 374 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R166 起始计数）

| 字段 | R165 起始 | R166 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 165 | 166 |
| type_round | 136 | 137 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 100 | 101 |
| last_updated_round | 165 | 166 |

## 遗留问题

1. **place 页数 374**：本轮 +1（Concepcion）。Brindisi DEFER 未建。registry 全库 1442，unknown 0。
2. **下轮 R166 = SCN28**：**R161 补种批已尽**（Kachgar/Tachkend/Douchak/Concepcion 4 建 + Brindisi DEFER），净 buildable 罄 → §3(3) 实务 SCN28 深层补种。宽扫未测区（东欧/近东/远东/北美中层 toponym）。
3. **R161 补种建序结果**：✔Kachgar → ✔Tachkend → ✔Douchak → ✘Brindisi(DEFER 净4) → ✔Concepcion。5 补 4 建 1 DEFER。
4. **DEFER 累积**：Brindisi 净4（距门1，AWED 港，待凑第5 solid 或 Phase3 富化）、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、Colorado/Michigan 河湖歧义。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **EVV5 节奏**：since_evv5=4→5，约 R171 触发。
7. **corpus-discover 顺延临界**：since_corpus=100（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **建前复核纪律强化**：本轮 Brindisi 复核揭示 R161 SCN28 vet 的「~5 临界」标注对 enumeration-heavy 候选偏乐观——港名并列/行程表列举须严剔。DEFER 而非勉强建页，守 5-solid 门。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
