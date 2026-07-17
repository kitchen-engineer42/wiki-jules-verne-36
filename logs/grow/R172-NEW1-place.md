---
round: 172
date: 2026-07-16
type_round: 143
phase: "2.1"
current_type: place
gene: NEW1
pages: [kazeh]
result: success
---

# GROW 2.1-B · R172 · NEW1 · place — 建 Kazeh（FWB 中非商旅 rendezvous，16 distinctPN→净 solid 12，R170 discover 建序首项）

## 执行摘要

Phase 2.1-B place 广度扩张第 143 轮（type_round 143）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10、streak=0<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
承 R170 SCN28 discover 建序，首项 **Kazeh**（FWB《Five Weeks in a Balloon》中非探险富矿开采首页）。

**Kazeh 建页（FWB 单源，净 solid 远超门）**：16 distinctPN 全 FWB。建前严剔 chapter-title 列举
（FWB-014-001/015-001 章题 enumeration「Arrival at Kazeh」/「Kazeh.--The Noisy Market-place...」）
与松散 enum（019-025「as far as Kazeh, or the great lakes」）；净 clean solid = 12，
取 6 段 12 引注建页：004-027（trader/caravan 中央 rendezvous）、004-028/004-029（Burton/Speke 史行程点）、
014-091（内陆 100 英里要地）、014-092（气球飘临，距海岸 350 英里）、015-002（非城，内陆无城）、
015-005（excavation/native dwelling/market/cannabis 田物理描述）、015-016（Arab 商人）、015-078（population howling）、
015-092（sorcerer 逃向 Kazeh）、016-003（Sultan of Kazeh）、017-008（Speke 东向经 Kazeh 赴 Ukereoue）。

place 计数 377→378，registry total 1445→1446，unknown 恒 0。
首版全段 ≤400（315/341/368/326/331/368），add_page 一次成型。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R171 刚 RESET）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、R170 补种 queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| kazeh | T1DAf6 | Five Weeks in a Balloon | real | Central Africa | 12 | 中非商旅 rendezvous；非城；Sultan/Arab 商人；剔章题列举 |

- **kazeh**：12 distinct solid PN（全 FWB）— 004-027（central rendezvous for traders/caravans）/004-028（reentered 20 June）/004-029（return 25 Aug → route to Zanzibar）/014-091（100mi 内陆要地）/014-092（气球飘临，距海岸 350mi）/015-002（非城，内陆无城）/015-005（物理描述）/015-016（Arab 商人）/015-078（population howling）/015-092（sorcerer 逃向）/016-003（Sultan of Kazeh）/017-008（Speke 东向经 Kazeh）。剔 014-001/015-001 章题列举、019-025 松散 enum。FWB 单源。链 five-weeks-in-a-balloon。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：kazeh 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（315/341/368/326/331/368）。✔
- **G3 ≥5 distinct PN**：12（FWB 单源，剔章题列举后净 solid 12，远超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1446 place 378 unknown 0。✔
- **查重充分**：kazeh 建前查重 NEW（feature-aware：非 lake/mount/cape，单式 name 查重充分，无既有页）。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R173 起始计数）

| 字段 | R172 起始 | R173 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 172 | 173 |
| type_round | 143 | 144 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 108 | 109 |
| last_updated_round | 172 | 173 |

## 遗留问题

1. **place 页数 378**：本轮 +1（Kazeh）。registry 全库 1446，unknown 0。
2. **下轮 R173 = NEW1**：since_evv5=1<10、since_discover=2<10、queue>0 → §3(7) NEW1。
   建 R170 discover 建序第 2 项 **Gondokoro**（8 distinctPN，FWB 白尼罗河探险北限点），建前抽样 ≥5 solid。
3. **R170 discover 建序进度**：✔Kazeh；余 Gondokoro → Carmen(re-vet) → Tandil(disambig) → Mozambique(严剔，大概率 DEFER)。
4. **FWB 非洲富矿开采启动**：Kazeh 为 FWB《Five Weeks in a Balloon》中非·尼罗河源探险史 toponym 层首页，
   净 solid 12 远超门——证实该层为新富矿（承 R170 未饱和第 5 次证实）。
5. **建前压缩纪律见效**：R172 首版即全段 ≤400，无建后 edit。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=108→109（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3；待定 Mozambique。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
