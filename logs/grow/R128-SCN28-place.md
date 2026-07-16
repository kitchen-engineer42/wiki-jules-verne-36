---
round: 128
date: 2026-07-15
type_round: 99
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 2
pages: []
result: discover
---

# GROW 2.1-B · R128 · SCN28 · place — 表层 discover 补种（Mont Blanc 强候选 + Bay of Bengal 升格，new=2<门，streak→1）

## 本轮公告

**R128 — Phase 2.1 — SCN28 — place — 表层 toponym 复扫，2 新候选（Mont Blanc / Bay of Bengal），discover_streak_low 0→1**

R127（EVV5）后：since_evv5=0、since_discover=5、discover_streak_low=0、queue(place)≈6、since_corpus=64。
决策矩阵 §3 首匹配：since_evv5=0<10（非 1a/1b）、streak=0<3（非 2）、**queue≈6<10 → 优先级 3 SCN28 触发**。
本轮不新建/编辑任何页面，纯表层 discover：对 `data/sentence_index/` 全库 968 章 jsonl 作 toponym 词边界扫描，
凑 ≥5 distinctPN 且未建的地名候选，补入 queue。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5≥10）| =0（R127 刚 RESET）| 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **queue≈6<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus≥30，项目扩展）| =64 | 否（非 §3 分支，记 HK-corpus-discover-not-in-statemachine PARK）|
| 7 | NEW1（默认）| — | 否 |

> since_corpus=64≥30 本会触发项目扩展 corpus-discover，但该分支**不在 §3 状态机**内（PARK）；
> §3 首匹配为表层 SCN28（queue<10）。本轮先做表层复扫；若表层续罄，后续再议 corpus 深扫。

## 扫描方法与结果

对 `data/sentence_index/**/*.jsonl` 全库 968 章作 toponym 词边界（`\bTerm\b`）聚合扫描，
过滤已建页（registry label + aliases 2506 名），保留 distinctPN≥5 的未建候选。原始命中 12：

| distinctPN | 候选 | 判定 |
|-----------|------|------|
| **41** | **Mont Blanc** | ✅ **新增**——AMB 专篇 33 + FEM/MI/OC/RM/SC 跨源；欧洲最高峰；与既有 alps 山链页判然不同（本页具体峰体）|
| 31 | Bay Company | ✗ 噪声——"Hudson's Bay Company" 截断，属 organization 非 place（且 hudsons-bay-company 类既有）|
| 31 | Cape of Good | ✗ 变体——cape-of-good-hope 截断，既有页 |
| 10 | Isle of Paques | ✗ 变体——easter-island 法语名（Île de Pâques），既有页 |
| 6 | The Torres Strait | ✗ 变体——torres-strait 既有页（冠词/定冠差异）|
| 6 | Long Island | ⏸ 续 hold——真 NY 岛 TTLU:3+AWED:1=4 干净，ASC:2 为里海 Uzun Ada 异地同名（"means Long Island" 译注）；混指，clean<5 |
| **5** | **Bay of Bengal** | ✅ **升格**——由 R89 之 4<门 hold 升可建（详见下）|
| 5 | Lake City | ✗ 变体——"Salt Lake City" 截断，salt-lake-city 既有页（R126 建）|
| 5 | Sea of Kara | ✗ 噪声——Kara Sea 词边界仅单源，agg 5 系子串污染，R84/R89 已剔 |
| 5 | Cape Mandible | ✗ 变体——mandible-cape 既有页（词序差异）|
| 5 | Lancaster Sound | ✗ 变体——lancaster-strait 既有页（Sound/Strait 同一水道）|
| 5 | Isle Tabor | ✗ 变体——tabor-island 既有页（词序差异）|

**净新候选 = 2**（Mont Blanc 新增 + Bay of Bengal 升格），10 项为噪声/既有页变体/续 hold。

### Mont Blanc 专核（41 distinctPN，强候选）

`python3 /tmp/gather.py "Mont Blanc"` → distinctPN=41 totalHits=44，
`by VVV: {AMB:33, FEM:1, MI:1, OC:1, RM:3, SC:2}`。AMB=《The Ascent of Mont Blanc》专篇，
Chamonix 出发登顶叙事贯穿全篇（AMB-001-002 起「fully decided to make the ascent of Mont Blanc」）；
跨源引：FEM-024-021「Mont Blanc is 14,439 [ft]」高度对照、RM-007-005/013-041/016-030 月篇高度基准、
SC-008-025/013-014 高度类比、MI-021-039 地质、OC-003-020 Montmartre 反讽。
**与既有 alps 判然不同**：alps（rev vR6O4P，label Alps，alias the Alps，山链）为「阿尔卑斯山脉」；
Mont Blanc 为链中**具体最高峰**（AMB-001-104「the highest mountain in Europe」），独立叙事主体，
registry 复核 mont-blanc/chamonix/mont-maudit 均 ABSENT。**下轮 NEW1 优先建**（rof=real，region Europe/France，book Ascent of Mont Blanc）。

### Bay of Bengal 升格核（5 distinctPN，恰达门）

`python3 /tmp/gather.py "Bay of Bengal"` → distinctPN=5 totalHits=5，`by VVV: {AWED:1, RM:1, TTLU:3}`：
- AWED-016-005：Andaman「principal of the islands in the Bay of Bengal」——真湾群岛 ✓
- TTLU-014-028：黑潮「leaves the Bay of Bengal」；TTLU-025-040：湾口浮尸；TTLU-026-011：Nemo 珍珠场 ✓×3
- RM-010-016：从月看地「the Indian Peninsula, the Bay of Bengal, and Cochin-China」——**复核为真湾地理命名**（Earth 倒影中辨识真湾），非 R89 所疑「月面白斑隐喻」。

4 叙事确指 + 1 地理命名恰 **5**，达门。较 R89 之「4<门续 hold」升格（RM 一引改判为真湾）。
⚠ RM 为「从月远指」偏 oblique，建页时以 AWED/TTLU 4 确指为主干、RM 为辅证。孟加拉湾（real，region Indian Ocean）。

### Long Island 续 hold（6 agg，clean 4）

真 NY 长岛 TTLU:3+AWED:1=4 干净确指；ASC:2 为「Uzun Ada, the name of which means Long Island」
——里海岛屿 Uzun Ada 的译名注解，异地同名污染。clean distinctPN=4<门，续 hold（同 R89 裁定）。

## SCN28 结论

表层 discover 显 place 类**接近饱和但未罄**：本轮凑得 **2 净新候选**（Mont Blanc 强 / Bay of Bengal 恰门），
余 10 命中皆噪声或既有页变体。new_candidates=2 < type_close_new_candidate_min=3 →
**discover_streak_low 0→1**（离 CLOSE 门槛 3 尚 2 步）。queue(place) 开放候选补至约 8
（Panama 待消歧 + Mont Blanc + Bay of Bengal + 洲级 Asia/Europe/America HOLD + Long Island/Bengal 原 hold 项）。
下轮 R129：queue≈8<10 仍会触发 §3(3) SCN28，但连续两低产 discover 恐使 streak→2；
或先落 NEW1 消费 Mont Blanc/Bay of Bengal（queue 消费后是否 <10 决定）。执行前读状态机重判。

## EXIT-GATE 检查（SCN28 轮：G4 + 不变式；G1/G2/G3 不适用——不建页）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；queue.md 补 2 候选 + Bengal 升格注；grow_state SCN28 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3（PN grounding/散文门/≥5PN）不适用——本轮不新增/编辑页面。

## state 更新（SCN28 six-step）

`current_round 128→129`；`type_round 99→100`；`rounds_since_last_evv5 0→1`（SCN28 非 EVV5，+1）；
`rounds_since_last_discover 5→0`（**discover RESET**）；`discover_streak_low 0→1`（new=2<3）；
`rounds_since_last_corpus_discover 64→65`（表层 discover 非 corpus，+1）；`last_updated_round→129`。

## 遗留问题

1. **place 页数保持 343**：本轮非建页，registry 全库 1411，unknown 0。
2. **discover_streak_low=1**：连续两低产 discover 将逼近 CLOSE 门（streak≥3 触发 CLOSE+SCN28 关闭 place 转 event）。
   本轮尚有 2 新候选，未至。下轮若再 <3 新则 streak→2。
3. **下轮 R129 预测**：queue 消费前约 8<10 → §3(3) SCN28；或若判定应消费新候选则走 NEW1（建 Mont Blanc/Bay of Bengal）。
   倾向下轮 NEW1 消费 Mont Blanc（强候选，41 PN，勿使强候选滞留）+ Bay of Bengal，再看 streak 走向。
4. **corpus-discover 顺延临界**：since_corpus=65，远过阈但非 §3 分支（PARK）；待表层复扫 0 新时议 corpus 深扫补单作残余。
5. **EVV5 节奏**：since_evv5=1，下次约 R138。
6. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
7. **散文门债**：32 页 >400（既有债 DEFERRED，RFC 后 edit_page 复拆）；R124 起建页 over-400=0，无新增。
8. **PHQ 待决**：Panama 消歧（isthmus/gulf/city/route）；Rome/Petersburg/Athens/Amsterdam 荷城（称号/缩写系 <门 hold）；
   Long Island（clean 4<门）；amsterdam-island R45 页不合规（H1+bullet Connections+aliases list）。
9. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass（32 页）、HK-corpus-discover-not-in-statemachine、
   HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。建成后统一处理。
10. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧；国级页价值待评。
