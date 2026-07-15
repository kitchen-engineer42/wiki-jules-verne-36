---
round: 10
date: 2026-07-15
type_round: 0
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 11
pages: []
result: accept
---

# GROW 2.1-B · R10 · SCN28 · organization — 候选播种

## 本轮公告

**R10 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮）**

`organization` 类型首轮。work 于 R9 关闭后转入 organization，候选池为空
（queue_size=0 < discover_queue_threshold=10）→ priority-3 SCN28 触发。为新类型播种候选。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（可建候选 < 10 或 rounds_since_discover ≥ 10）| 候选=0 < 10 | **触发** |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =8 | 否 |
| 4/5 | RCH2 / NEW1+RCH2 | stub%=0 | 否 |

> organization 为**开放类型**，与 work（有限枚举）不同——discover 语义有效且必要，无原则性偏离。

## SCN28 — discover

**红链法（build_wanted_pages）**：待建页面 **0** 条——R9 全库 wikify 后所有 wikilink 目标均已解析，
红链盲区为空。故转 **corpus 关键词扫描**（LLM 候选发现半），扫 `data/sentence_index/*.jsonl`，
以组织指示词（Club/Institute/Society/Company/Committee/Association/Observatory/Railway…）匹配专名，
按 distinctPN 统计，过滤 ≥3，排除已建（gun-club、weldon-institute）与假阳（Twenty Thousand League、
Ice Bank、Grand Bank 等地理/通用词）。

**新候选（distinctPN ≥ 3，入 queue.md P1）**：

| 候选 | 源作 | distinctPN | 备注 |
|------|------|-----------|------|
| Reform Club | AWED | ~23 | Fogg 打赌的伦敦绅士俱乐部 |
| Hudson's Bay Company | FC | ~31 | 《毛皮国》皮货公司（"Bay Company"/"Hudson"）|
| Cambridge Observatory | FEM/RM | ~19 | Barbicane 咨询的天文台（borderline place/org）|
| Royal Geographical Society | FWB/ACH | ~14 | 资助气球/北极探险的地理学会 |
| North Polar Practical Association | TT | ~13 | 《颠倒》Gun Club 购北极的公司 |
| Grand Transasiatic Railway Company | ASC | 高（Transasiatic 76）| 横贯亚洲铁路公司 |
| St Louis Fur Company | FC | ~4 | 圣路易斯皮货公司 |
| Peninsular and Oriental Company | AWED | ~4 | P&O 轮船公司 |
| Royal Society | 多部 | ~7 | 伦敦皇家学会 |
| Royal Institution | 多部 | ~7 | 皇家研究院 |
| East India Company | 多部 | ~3 | 东印度公司 |

| 结果 | 数值 |
|------|------|
| 红链新候选 | 0 |
| corpus 新候选（distinctPN ≥ 3）| 11 |
| **new_candidates** | **11** |
| discover_streak_low | 0（11 ≥ type_close_new_candidate_min=3，不累加）|

> 候选池 11 条 > discover_queue_threshold=10，足够支撑约 2 轮 NEW1（5 页/轮）。R11 起转 NEW1 建页。
> Cambridge Observatory 归类存疑（天文台建筑 vs 机构）——建页时按其作为咨询机构的功能定 organization，
> 若最终更像 place 则改归 place 类型队列。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志产出；queue.md P1 入 11 候选；grow_state step-six→R11（type_round 0→1，discover reset，since_evv5 0→1，since_corpus 8→9）|

> discover 轮不建页，G1/G2/G3/G5 不适用。

## state 更新

`current_round 10→11`，`type_round 0→1`，`rounds_since_last_evv5 0→1`，`rounds_since_last_discover→0`，
`rounds_since_last_corpus_discover 8→9`，`discover_streak_low→0`。`current_type` 仍 organization。

## 遗留问题

1. **R11 = organization NEW1 首建**：从 queue.md P1 取 5 条（Reform Club / Hudson's Bay Company /
   Royal Geographical Society / North Polar Practical Association / Grand Transasiatic Railway Company），
   standard 档，每句 PN-grounded（源作 sentence_index）。
2. **organization 缺类型专属模板核对**：建页前确认 `local/template/organization-schema.md` 存在且字段
   （`book`/`org_type`/`founded`，见 CLAUDE.md Phase 7 表）；Pilot 已建 gun-club/weldon-institute 可作范式。
3. **Cambridge Observatory 归类**待建页时定夺（org vs place）。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias 撞名四项债务照旧 PARK/记录。
