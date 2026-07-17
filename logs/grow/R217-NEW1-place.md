---
round: 217
date: 2026-07-17
type_round: 188
phase: "2.1"
current_type: place
gene: NEW1
pages: [coal-town]
result: success
---

# GROW 2.1-B · R217 · NEW1 · place — 建 Coal Town（UC 地下电力矿村，净 solid 13 单指；Loch Katrine 底 New Aberfoyle 聚落，The Underground City 核心居所）

## 执行摘要

Phase 2.1-B place 广度扩张第 188 轮（type_round 188）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、since_discover=4<10、queue(place)=1>0、stub%=0 → §3(7)）。

取 R212 discover 队列**建序 4（末项）** **Coal Town**（UC 主）。建前 pages.json 子串（coal）+
`the-` 前缀双查皆 NEW。**单指无混淆**：全库 19 distinctPN 全指 UC 地下矿村，无同名异指。
**净 13 distinct solid UC PN**（远超门）：
- **UC-010-004**：液压双轨通往埋于县地下之村，名曰 Coal Town。
- **UC-010-005**：电力为热与光之主角。
- **UC-010-011**：居民以其地自豪。
- **UC-011-003**：劳作毕，Coal Town 静息，无风无雨。
- **UC-013-062**：New Aberfoyle 矿工于 Coal Town 婚宴狂欢。
- **UC-016-006**：突发内涝，四处呼号。
- **UC-016-011**：洪水泄入未及深处，Coal Town 无损。
- **UC-010-009**：建于 Loch Katrine 东岬下，Stirling 县北。
- **UC-014-053**：其上悬 vaulted rocky roof，出之方见苍穹如渊。
- **UC-016-002**：全城 electric lamps 满功率通明。
- **UC-018-014**：大日 electric discs 亮如列日。
- **UC-018-009**：矿师与要人聚，即 New Aberfoyle 全民。
- **UC-018-002**：居民无叛虞，险讯遍告。

place 计数 411→412，registry total 1479→1480，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=fictional、region Scotland、book The Underground City、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；queue=1 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 建毕队列罄（R212 discover 4 项全消费）→ **R218 = SCN28**（§3(4) zombie）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| coal-town | 1pE7VU | The Underground City | fictional | Scotland | 13 | Loch Katrine 底地下电力矿村；New Aberfoyle 聚落；单指无混淆 |

- **coal-town**：13 distinct solid UC PN（单指）；aliases []。链 New Aberfoyle/Loch Katrine/James Starr/subterranean colony 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 UC Coal Town；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：13 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（附 wikilink [[New Aberfoyle]]）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1480 place 412 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（coal）+ `the-` 前缀双查。✔
- **地底 Geography 替代维度**：承 EVV5 r2，以 vaulted roof/无天气/电力照明/Loch Katrine 位定义地下城，无空节。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R218 起始计数）

| 字段 | R217 起始 | R218 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 217 | 218 |
| type_round | 188 | 189 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 153 | 154 |
| last_updated_round | 217 | 218 |

## 遗留问题

1. **place 页数 412**：本轮 +1（Coal Town）。registry 全库 1480，unknown 0。
2. **下轮 R218 = SCN28**：queue(place)==0（R212 队列 4 项全消费）→ §3(4) zombie。
   届时可优先核 **R212 备选** 4 项 solid 后入队（Montgomery Street〔GM×10〕/ Kamtchatka Current〔FC×7〕/ Pleasant Garden〔MW×7〕/ North Carolina〔MW×7+FF×6，双书需逐句核同指〕），或再运行 discover3.py 全库重扫补池。
3. **R218 后**：若 SCN28 得 ≥3 净新 → 续 NEW1 消费；若 <3 连续 → discover_streak_low 累加，逼近 CLOSE 评估（type_close_streak=3）。
4. **同名异指剔除**：本轮无（Coal Town 单指）；承纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=153→154（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
