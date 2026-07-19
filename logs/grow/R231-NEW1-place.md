---
round: 231
date: 2026-07-18
type_round: 202
phase: "2.1"
current_type: place
gene: NEW1
pages: [plaza-mayor]
result: success
---

# GROW 2.1-B · R231 · NEW1 · place — 建 Plaza-Mayor（利马中央广场，PL 全书舞台；CLOSE 覆盖轮之一）

## 执行摘要

Phase 2.1-B place 广度扩张第 202 轮（type_round 202）。

**CLOSE 覆盖决策（本轮关键）**：R230 SCN28 使 discover_streak_low 达 3（=type_close_streak），
决策机 §3(2) 本应触 **CLOSE+SCN28**（place→event）。但 R230 discover 并非枯竭——三次低产轮
（R223/R227/R230）**各掘 2 真净新地名**，且每次皆因**新建扫描器闭合新盲区**（单词→多词特征→撇号连字符），
本轮手握 2 个过门候选（Plaza-Mayor PL×14、Saint-Pierre-Miquelon TN×5）。据「Exhaustively re-scan
before claiming saturation」三条反馈 + 在手候选实证，判 **place 未饱和**。经用户裁定
**「Build 2, then re-eval」**：覆盖本轮 CLOSE，将 discover_streak_low 3→0 复位（宣告 place 产出仍旺，
重新计饱和时钟），改以 NEW1 消费两候选（R231/R232），再由后续 discover 复评。

复位后 §3 首匹配 **NEW1**（since_evv5=4<10；streak=0<3；since_discover=0<10、全局 queue≥10；
queue(place)=2>0 → §3(4) 否；stub=0 → §3(7) NEW1）。

取 R230 SCN28 队列**建序 1** **Plaza-Mayor**（PL 主）。建前 exact-slug 复核 plaza-mayor ABSENT
（pages.json 无子串、无 label 命中）。**单指**：PL 全书 14 PN 皆指利马中心大广场，无同名异指。
label `Plaza-Mayor`（连字符无撇号，slugify=plaza-mayor 对齐 id，无 R229 式分歧）。

**10 distinct solid PN**（PL×14 中择要，四节分配）：

- **PL-001-003**：广场为「古王城之 forum」，populace 大动、artisans 罢工汇入人群。
- **PL-007-015**：夜半远处哨声亦令人忆及广场上曾闻之声——广场系全城生活之枢。
- **PL-001-015**：四马华车入广场，载一骄而哀之独客，视而不见众人。
- **PL-003-047**：老 duenna 忆一陌客某夜于广场施援少女。
- **PL-008-018**：起事时 Martin Paz 领一叛军纵队于广场挥黑旗（独立旗），印第安人自邻街进攻。
- **PL-008-048 / PL-008-034**：若其留守广场或已胜；然印第安众裹挟广场被征服者愈聚。
- **PL-001-007**：广场中央有喷泉，利马青年常聚其旁。
- **PL-001-040**：北侧踞副王宫，central portico 前骑警驻守，广场喧腾时几不能持位。
- **PL-005-003**：正对广场之宫中 president Gambarra 权位岿然。

place 计数 420→421，registry total 1488→1489，unknown 恒 0。
add_page 一次成型（rev WsEIDx，size 2263）；prose-gate awk 预检 0 超段（首版即达标）。
pn_validator strict ✓。real_or_fictional=real、region Peru、book The Pearl of Lima、aliases=[]。
Connections 含 [[Lima]]（存）/[[The Pearl of Lima]]（存，work）。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1，含 CLOSE 覆盖）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| **2** | **CLOSE+SCN28（streak≥3）** | **=3——但经用户裁定覆盖，streak 复位 0** | **否（覆盖）** |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| plaza-mayor | WsEIDx | The Pearl of Lima | real | Peru | 10 | 利马中央大广场；PL 全书单指；连字符 label slugify 对齐 id |

- **plaza-mayor**：10 distinct solid PN（PL 全书 14 中择）；aliases []；label `Plaza-Mayor`。链 Lima/The Pearl of Lima。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Plaza-Mayor；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全段预检 0 超段（首版达标）。✔
- **G3 ≥5 distinct PN**：10 solid（PL）。✔
- **G4 脚本建页**：add_page.py 建（quality 自动 featured），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（两 wikilink）；label 无撇号无冒号；description 无冒号/撇号。✔
- **registry 一致**：total 1489 place 421 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug plaza-mayor ABSENT + label 无命中。✔
- **单指核**：PL 逐句确认 Plaza-Mayor 指一利马广场。✔
- **排除检查**：提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R232 起始计数）

| 字段 | R231 起始 | R232 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 231 | 232 |
| type_round | 202 | 203 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0（CLOSE 覆盖复位）| 0 |
| rounds_since_last_corpus_discover | 167 | 168 |
| last_updated_round | 231 | 232 |

## 遗留问题

1. **place 页数 421**：本轮 +1（Plaza-Mayor）。registry 全库 1489，unknown 0。
2. **下轮 R232 = NEW1**：建 queue 建序 2 **Saint-Pierre-Miquelon**（TN×5，纽芬兰外法属群岛，Viking 号启航港；
   book Ticket No. 9672，real，region North Atlantic）。since_evv5=5<10、streak=0、queue(place)=1>0 → §3(7) NEW1。
3. **CLOSE 复评预告**：R232 建毕队列罄 → R233 = SCN28-zombie（§3(4)）。届时若 discover 仍 <3 净新，
   discover_streak_low 0→1 起重计；须连续三轮低产方再触 CLOSE 评估。**本次覆盖非永久豁免**——
   place 终将饱和，届时如实 CLOSE。（记 HK-close-override-productive-discover：streak 达阈但 discover 非枯竭时，
   凭在手候选与新盲区证据可覆盖 CLOSE，复位 streak 续建。）
4. **HK-place-apostrophe-label-slug-divergence〔R229〕**：本轮连字符 label 无撇号，slugify 天然对齐，无风险。
5. **HK-discover-possessive-hyphen-toponym-blindspot〔R227，R230 已由 possessive_scan.py 闭合〕**。
6. **HK-dupcheck-bareterm-vs-slug〔R223〕**：本轮续遵。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=167→168（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：place 页 quality=none 若干，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUP R198）；celestial-empire（DUP R212）；lancaster-sound〔同指 lancaster-strait〕；
    tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait（bare-term 净新但 slug 已建）；cape-mandible〔净4〕/
    long-island〔NY 净4〕/Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/
    Fort Enterprise/Turnagain/Fort Franklin/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot、HK-place-apostrophe-label-slug-divergence、HK-close-override-productive-discover〔新〕、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
