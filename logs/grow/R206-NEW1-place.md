---
round: 206
date: 2026-07-17
type_round: 177
phase: "2.1"
current_type: place
gene: NEW1
pages: [carmen]
result: success
---

# GROW 2.1-B · R206 · NEW1 · place — 建 Carmen（SC 巴塔哥尼亚 Rio Negro 口殖民镇，净 solid 7 单指；Carmen–Mendoza 商道东端）

## 执行摘要

Phase 2.1-B place 广度扩张第 177 轮（type_round 177）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、since_discover=4<10、queue(place)=2>0、stub%=0 → §3(7)）。

取 R201 discover 队列**建序 4** **Carmen**（SC）。建前 pages.json 子串（carmen）+
`the-` 前缀双查皆 NEW。**同名异指审查通过**：警惕 Carmen 恐为人名/异地同名，但全库
7 distinctPN 全指 SC 巴塔哥尼亚 Rio Negro 口殖民镇（无人名 referent），**单指无混淆**。
**净 7 distinct solid SC PN**：
- **SC-009-019**：Carmen 殖民者称原住民为 Tehuelches（Magellan 称 Patagonians）。
- **SC-016-018**：Thalcave 谓 "the Carmen route"。
- **SC-016-019**：Paganel 西语答 "from Carmen to Mendoza" 之道。
- **SC-016-027**：Thalcave 问是否赴 Carmen。
- **SC-016-032**：问赴 Carmen 抑 Mendoza，闻双否而讶。
- **SC-016-041**：Paganel 沙上绘图，示 Carmen 道跨经纬贯两洋。
- **SC-021-062**：Tandil–Carmen（Rio Negro 口）间印第安商贩往来。

place 计数 403→404，registry total 1471→1472，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Argentina、book In Search of the Castaways、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；queue=2 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Rio Colorado（1 项）。R207 建毕队列罄 → SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| carmen | 2GtTAr | In Search of the Castaways | real | Argentina | 7 | 巴塔哥尼亚 Rio Negro 口殖民镇；Carmen–Mendoza 商道东端；单指无混淆（非人名）|

- **carmen**：7 distinct solid SC PN（单指）；aliases []。链 Rio Negro/Mendoza/Tandil 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 SC Carmen 镇；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：7 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1472 place 404 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（carmen）+ `the-` 前缀双查。✔
- **同名异指审查**：Carmen 排查人名/异地同名——7 PN 全指 Rio Negro 口镇，无人名，单指采全。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R207 起始计数）

| 字段 | R206 起始 | R207 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 206 | 207 |
| type_round | 177 | 178 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 142 | 143 |
| last_updated_round | 206 | 207 |

## 遗留问题

1. **place 页数 404**：本轮 +1（Carmen）。registry 全库 1472，unknown 0。
2. **下轮 R207 = NEW1**：since_evv5=2<10、since_discover=5<10、queue(place)=1>0 → §3(7)。
   建 **Rio Colorado**（rio-colorado，SC×6 主，巴塔哥尼亚河越 37th parallel），**须剔 1 DSCF
   同名异指**，仅采 SC referent，抽样 ≥5 solid。建前 pages.json 子串 + `the-` 双查。
3. **R207 建毕队列罄 → R208 = SCN28**：since_discover 达 5〔<10〕但 queue(place)==0 → §3(4)
   zombie 触发。届时全库掘 place toponym 补种（承 premature-saturation 纪律，全库重扫）。
4. **同名异指剔除**：本轮 Carmen 排查通过（单指，非人名）；下轮 Rio Colorado 剔 1 DSCF。
   承 Rio Negro/New Georgia/Far West 纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=142→143（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
