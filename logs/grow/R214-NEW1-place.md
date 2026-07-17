---
round: 214
date: 2026-07-17
type_round: 185
phase: "2.1"
current_type: place
gene: NEW1
pages: [saville-row]
result: success
---

# GROW 2.1-B · R214 · NEW1 · place — 建 Saville Row（AWED 伦敦 Fogg 宅街，净 solid 12 单指；Burlington Gardens No.7，环球赌约启程地）

## 执行摘要

Phase 2.1-B place 广度扩张第 185 轮（type_round 185）。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10、since_discover=1<10、queue(place)=3>0、stub%=0 → §3(7)）。

取 R212 discover 队列**建序 2** **Saville Row**（AWED 主）。建前 pages.json 子串（saville/savile）+
`the-` 前缀双查皆 NEW。**单指无混淆**：全库 16 distinctPN 全指 AWED Fogg 伦敦宅街，无同名异指。
**净 12 distinct solid AWED PN**（远超门）：
- **AWED-001-002**：No.7 Saville Row，Burlington Gardens，Sheridan 1814 卒于此宅。
- **AWED-001-010**：Fogg 独居，无人得入。
- **AWED-001-012**：宅不奢而极舒适。
- **AWED-002-011**：昔 Sheridan 治下乱居，今 method idealised。
- **AWED-001-013**：午后十一时半 Fogg 离宅赴 Reform。
- **AWED-001-027**：Passepartout 独处宅中。
- **AWED-004-029**：街尾雇车驰 Charing Cross（启程）。
- **AWED-037-005**：终程三分钟复返 Saville Row。
- **AWED-017-014**：远行仍念宅中 gas 耗其资。
- **AWED-035-020**：周日宅如无人，首次不赴俱乐部。
- **AWED-035-002**：邻人若闻 Fogg 归当惊。
- **AWED-035-006**：宅设一室予 Aouda。

place 计数 409→410，registry total 1477→1478，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region England、book Around the World in Eighty Days、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；queue=3 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Villa Rica / Coal Town（2 项）。**R215 起 since_evv5→10 → §3(1b) EVV5 先插**（非建页），再续建。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| saville-row | Cyub57 | Around the World in Eighty Days | real | England | 12 | 伦敦 Burlington Gardens 街；Fogg 宅 No.7；单指无混淆 |

- **saville-row**：12 distinct solid AWED PN（单指）；aliases []。链 Phileas Fogg/Reform Club/Passepartout/Aouda/Charing Cross 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 AWED Saville Row；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：12 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1478 place 410 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（saville/savile）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R215 起始计数）

| 字段 | R214 起始 | R215 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 214 | 215 |
| type_round | 185 | 186 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 150 | 151 |
| last_updated_round | 214 | 215 |

## 遗留问题

1. **place 页数 410**：本轮 +1（Saville Row）。registry 全库 1478，unknown 0。
2. **下轮 R215 = EVV5**：since_evv5=10≥10 → §3(1b) 触发 EVV5（place schema 反思，非建页），执行后 reset since_evv5=0。
3. **R216+ 建序**：Villa Rica → Coal Town（2 项），建毕队列罄 → SCN28。
4. **同名异指剔除**：本轮无（Saville Row 单指）；承纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=150→151（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
