---
round: 169
date: 2026-07-16
type_round: 140
phase: "2.1"
current_type: place
gene: NEW1
pages: [tai-youan]
result: success
---

# GROW 2.1-B · R169 · NEW1 · place — Baikal 建前查重 DUPLICATE（既有 lake-baikal）→ 改建 tai-youan（ASC 单源 5PN，relief engine 站）

## 执行摘要

Phase 2.1-B place 广度扩张第 140 轮（type_round 140）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、streak=0<3、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
承 R166 SCN28 discover 建序，第 3 项预定 **Baikal**——建前查重 DUPLICATE，改建序末 Tai-Youan。

**Baikal DUPLICATE 裁定（关键，HK-discover-existing-type-blindspot 第 3 例）**：
建前 label/alias 查重命中既有 **lake-baikal.md**（label「Lake Baikal」、alias [The Baikal]、MS featured place），
覆盖同湖同源、引注重叠（028-094/029-011/029-013 等）。**R166 SCN28 查重仅测「baikal」小写变体
（baikal/baikal/baikal），漏检「lake-」前缀 id**——与 R154 timbuctoo/Timbuktu 同型漏检。
裁定：DUPLICATE 不建。同时对 Baikal 语料严 re-vet（剔 003-044/013-014/018-004/031-011 省列举与「Baikal
provinces」区域泛指，净 11 湖体确指 solid）——既有页素材充足，Phase 3 富化机会但本轮 breadth 不做。
**纪律强化**：lake/mount/cape/bay 类 toponym 查重须双测「{name}」与「{feature}-{name}」两式。

**改建 Tai-Youan（建前复核达门）**：ASC Grand Transasiatic 华北站，6 distinctPN，剔 023-069 乘客目的地列举
（Si-Ngan/Ho Nan/Lou-Ngan/Tai-Youan enumeration），净 solid = 5（恰达门）——024-009（10pm 停站）、
025-061（telegraph 求 relief engine）、025-064（3pm 前到）、025-071（stationmaster 电请 engine 赴 Nanking 线）、
025-076（无须返 Tai-Youan 省 1.5h）。relief-engine 事件为 Tai-Youan 站叙事角色，非 enumeration，合规建。

place 计数 376→377，registry total 1444→1445，unknown 恒 0。
首版全段 ≤400（388/229/347/295/331），add_page 一次成型。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10、R166 补种 queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tai-youan | RT4Pp4 | The Adventures of a Special Correspondent | real | China | 5 | Grand Transasiatic 华北站；relief engine depot；恰达 5 门 |
| ~~baikal~~ | — | — | — | — | — | **DUPLICATE**：既有 lake-baikal.md（label Lake Baikal）；R166 查重漏检 lake- 前缀 |

- **tai-youan**：5 distinct solid PN — ASC-024-009（230km 后 10pm 停站）/025-061（telegraph Tai-Youan 求 relief engine）/025-064（3pm 前 engine 到）/025-071（stationmaster 电请 engine 赴 Nanking 线）/025-076（无须返 Tai-Youan 省 1.5h）。剔 023-069 乘客目的地列举。ASC 单源。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tai-youan 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（388/229/347/295/331）。✔
- **G3 ≥5 distinct PN**：5（ASC 单源，剔列举后恰达门；relief-engine 事件为站叙事角色，非 enumeration）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1445 place 377 unknown 0。✔
- **查重充分**：Baikal 建前捕获 lake-baikal DUPLICATE；Tai-Youan 查重 NEW。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R170 起始计数）

| 字段 | R169 起始 | R170 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 169 | 170 |
| type_round | 140 | 141 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 105 | 106 |
| last_updated_round | 169 | 170 |

## 遗留问题

1. **place 页数 377**：本轮 +1（Tai-Youan）。Baikal DUPLICATE 未建。registry 全库 1445，unknown 0。
2. **下轮 R170 = NEW1**：since_evv5=9<10、since_discover=3<10、queue>0 → §3(7) NEW1。
   建 R166 discover 余项 **Yeniseisk/Tioumen**（**建前严剔**：Yeniseisk 8 hits 多省列举疑 <5 solid、Tioumen 临界 5）；
   若两者建前净 <5 clean solid 则 DEFER，转 SCN28 深层补种或洲际其他富矿。
3. **R166 discover 建序结果**：✔Sou-Tcheou → ✔Lan-Tcheou → ✘Baikal(DUPLICATE) → ✔Tai-Youan；余 Yeniseisk/Tioumen 待建前定。
   6 候选 → 3 建 + 1 DUPLICATE + 2 待定。
4. **⚠ R171 = EVV5**：since_evv5=9→10 达门，R171 触发 §3(1b) EVV5（周期质量/模板反思，无建页）。
5. **查重纪律强化（HK-discover-existing-type-blindspot 第 3 例）**：SCN28 discover 阶段查重须对 geographic-feature
   toponym（lake/mount/cape/bay/gulf/sea）双测「{name}」与「{feature}-{name}」id 两式；单测 name 变体会漏检既有页。
   本轮 Baikal 若非建前二次查重，将建重复页。
6. **建前压缩纪律见效**：R169 首版即全段 ≤400，无建后 edit。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=105→106（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE(既有 lake-baikal)；待定 Yeniseisk/Tioumen。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
