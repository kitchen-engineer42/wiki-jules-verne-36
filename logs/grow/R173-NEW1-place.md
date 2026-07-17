---
round: 173
date: 2026-07-16
type_round: 144
phase: "2.1"
current_type: place
gene: NEW1
pages: [gondokoro]
result: success
---

# GROW 2.1-B · R173 · NEW1 · place — 建 Gondokoro（FWB 尼罗河探险北限点，8 distinctPN→净 solid 7，R170 discover 建序第 2 项）

## 执行摘要

Phase 2.1-B place 广度扩张第 144 轮（type_round 144）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、streak=0<3、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
承 R170 SCN28 discover 建序，第 2 项 **Gondokoro**（FWB 白尼罗河源探险史北限地标）。

**Gondokoro 建页（FWB 单源，净 solid 7 超门）**：8 distinctPN 全 FWB。剔 005-055（Speke/Grant
升湖任务段，本句不确指 Gondokoro）；净 clean solid = 7，取 5 段 7 引注建页：
004-016（1840 Mehemet Ali 探险止于 Gondokoro，北纬 4–5 度间）、004-018（Penney 越 1 度后返 Khartoum 力竭而亡）、
004-019（1859 Lejean 不得过 Gondokoro）、018-057（气球距 90mi、离北向探险家极点 <5mi）、
018-097（盼北风赴 Gondokoro 会同胞）、019-005（虑抵达之难）、005-028（doctor 定线「Stop at Gondokoro」）。

place 计数 378→379，registry total 1446→1447，unknown 恒 0。
首版全段 ≤400（308/309/352/368/284），add_page 一次成型。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10、queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| gondokoro | yJVORW | Five Weeks in a Balloon | real | East Africa | 7 | 尼罗河北纬 4–5 度间；北向探险极点；剔 005-055 非确指 |

- **gondokoro**：7 distinct solid PN（全 FWB）— 004-016（1840 探险止于 Gondokoro，北纬 4–5 度间）/004-018（Penney 越 1 度返 Khartoum 亡）/004-019（1859 Lejean 不得过）/018-057（距 90mi、离北向极点 <5mi）/018-097（盼北风赴会同胞）/019-005（虑抵达难）/005-028（定线 Stop at Gondokoro）。剔 005-055（Speke/Grant 升湖段，本句不确指）。FWB 单源。链 five-weeks-in-a-balloon。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：gondokoro 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（308/309/352/368/284）。✔
- **G3 ≥5 distinct PN**：7（FWB 单源，剔 005-055 非确指后净 solid 7）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1447 place 379 unknown 0。✔
- **查重充分**：gondokoro 建前查重 NEW（非 lake/mount/cape 地物，单式 name 查重充分，无既有页）。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R174 起始计数）

| 字段 | R173 起始 | R174 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 173 | 174 |
| type_round | 144 | 145 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 109 | 110 |
| last_updated_round | 173 | 174 |

## 遗留问题

1. **place 页数 379**：本轮 +1（Gondokoro）。registry 全库 1447，unknown 0。
2. **下轮 R174 = NEW1**：since_evv5=2<10、since_discover=3<10、queue>0 → §3(7) NEW1。
   建 R170 discover 建序第 3 项 **Carmen**（SC Carmen de Patagones，7 distinctPN，**建前复核**：
   剔 009-019 命名 Tehuelches 段，确认净 ≥5 solid town，否则 DEFER）。
3. **R170 discover 建序进度**：✔Kazeh → ✔Gondokoro；余 Carmen(re-vet) → Tandil(disambig) → Mozambique(严剔，大概率 DEFER)。
4. **FWB 非洲富矿续采**：Kazeh(12)+Gondokoro(7) 两页净 solid 均超门，FWB 尼罗河源探险史 toponym 层持续产出。
   R174 起转 SC 巴塔哥尼亚段（Carmen/Tandil），验证南美富矿。
5. **建前压缩纪律见效**：R173 首版即全段 ≤400，无建后 edit。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=109→110（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3；待定 Mozambique。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
