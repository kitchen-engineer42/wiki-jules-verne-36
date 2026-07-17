---
round: 155
date: 2026-07-15
type_round: 126
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 4
pages: []
result: discover
---

# GROW 2.1-B · R155 · SCN28 · place — 深层候选补种（实务触发：净 buildable 罄）；净新 4 buildable：Samarkand/Ceuta/Formentera/Callao

## 本轮公告

**R155 — Phase 2.1 — SCN28 — place — 中亚/俄/合集城岛级 toponym 宽扫 / 非建页 / since_discover 归 0 / new_candidates=4**

R154 后 since_evv5=5、since_discover=4、streak=0、queue(place) 名义>10 但净 buildable=0、since_corpus=91。
决策矩阵 §3 严格首匹配为 §3(7) NEW1（since_discover=4<10、queue_size 名义>10），**但 R150 补种批已全部处理完毕**
（✔Nantucket ✔Tunis ✔Tripoli ✘Timbuktu[重复] ✔Maryland），且既有 queue 仅剩 sub-gate DEFER/hold 项
（Virginia 净4、Indiana 净0、Louisiana 净3、Arkansas/Tennessee <5、Colorado/Michigan 河湖歧义）。
本轮先**复议 DEFER 项**：Virginia 复算净 solid=4（距门 1）、Indiana 复算净 solid=0（全州列举）——均不可建。

**净 buildable 实务归零，触发深层 SCN28 补种。** 依 memory feedback「Exhaustively re-scan before claiming saturation」，
非从 queue 推断枯竭，而是对语料宽扫新 toponym。属 HK-queue-size-scope 情形（名义 queue_size 高估净可建，
致 §3 discover 触发滞后至 since_discover=10）；本轮以实务判断提前补种，不建页。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| 名义不满足；**净 buildable=0 实务触发** | **触发（实务）** |
| 7 | NEW1（默认）| — | 否（无净可建，被实务 SCN28 抢占）|

> **实务裁定说明**：严格 §3 本应 NEW1，但净可建=0 使 NEW1 无对象。依 R154 遗留 #3 与 memory feedback，
> 提前行 SCN28 补种（等价于 queue_size 按净 buildable 计则 <10 触发 §3(3)）。counter 按 SCN28 更新。

## 扫描方法与结果

对 `data/sentence_index/` 宽扫中亚（Bombarnac/ASC）、俄西伯利亚（Michael Strogoff/MS）、80 天环游路线城、
合集港/岛级 toponym，每候选统计 distinctPN、**双向查重既有页（label+aliases+id，含拼写/音译变体）**、抽样判 solid。

| 候选 | distinctPN | 主源 | 查重 | 抽样判定 | 入队? |
|------|-----------|------|------|---------|------|
| Samarkand | 31 | ASC | new | 大中亚铁路要站（ASC-004-004 63 站/005-002 Uzun Ada→Samarkand）；剔站名列举后 ≥5 solid | ✅ |
| Ceuta | 20 | OC(19)+TTLU(1) | new | 对 Gibraltar 摩洛哥岸（OC-019-052）/彗后残岛（OC-020-002）/Ceuta→Tripoli 巡航（OC-020-024） | ✅ |
| Formentera | 18 | OC | new | 巴利阿里最小岛（OC-025-001）/Servadac 折返（OC-025-011）；Rosette 汇合关键地 | ✅ |
| Callao | 14 | PL(5)+SC(9) | new | Lima 之港 Port of Callao（PL-002-006）/Sarah 骑向 Callao（PL-003-062） | ✅ |
| Baikal | 17 | MS | **✘ 重复** | 既有 lake-baikal（MS×17 全 Lake Baikal 湖/provinces 同指） | ✘ |
| Bokhara/Merv/Aden/... | 高 | — | ✘ 已建 | 既有页 | ✘ |

**净新 buildable = 4**（Samarkand/Ceuta/Formentera/Callao），均未建、均远超 5 solid distinctPN 门。
Baikal 判重（既有 lake-baikal）——**HK-discover-existing-type-blindspot 主动规避**（本轮双向查重含变体，建前捕获）。

## SCN28 结论

**队列深层补种成功。** 净新 4 buildable 入队，均高 distinctPN（14–31）优质候选，覆盖新作品源（ASC Bombarnac、
PL、SC）与既有薄弱区域（中亚、Balearic、Peru）。下轮 R156 起转 NEW1，按 solid 强度/源多样性序建：
**Formentera（OC 关键地）→ Ceuta（OC 多源）→ Samarkand（ASC 要站）→ Callao（PL+SC 双源）**。
复议 DEFER：Virginia 净4 距门 1（待凑第 5 solid）、Indiana 净0 不可建，均维持 DEFER。
模板不修改，不触发 backfill，不新起 RFC。

> **附**：本轮证 place 类型**远未饱和**——宽扫即得 4 优质净新候选（且仅测部分中亚/俄/港岛项，
> 未测南美/东欧/近东/远东大量中层 toponym）。HK-premature-saturation-claim 再次证伪。

## EXIT-GATE 检查（SCN28 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；grow_state SCN28 six-step；queue.md R155 marker 追加；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 six-step）

`current_round 155→156`；`type_round 126→127`；`rounds_since_last_evv5 5→6`（SCN28 非 EVV5 轮，+1）；
`rounds_since_last_discover 4→0`（SCN28 RESET）；`discover_streak_low` 保持 0（new_candidates=4≥3）；
`rounds_since_last_corpus_discover 91→92`；`last_updated_round→156`。

## 遗留问题

1. **place 页数保持 366**：本轮非建页，registry 全库 1434，unknown 0。
2. **下轮 R156 = NEW1**：since_discover 归 0、queue 补 4 项 → §3(7) NEW1。建 **Formentera** 首（OC Off on a Comet 关键地，18 distinctPN 单源）。
3. **R155 补种建序**：Formentera → Ceuta → Samarkand → Callao（solid/源多样性序）。
4. **DEFER 复议结论**：Virginia 净4（距门 1，待凑）、Indiana 净0（不可建）；Louisiana/Arkansas/Tennessee 维持 hold；Colorado/Michigan 河湖歧义待逐条剥离。
5. **HK-discover-existing-type-blindspot 主动规避**：本轮对每候选双向查重（label+aliases+id 含变体），建前捕获 Baikal 重复（既有 lake-baikal）。SCN28 查重纪律已内化。
6. **HK-queue-size-scope 再证**：名义 queue_size>10 但净 buildable=0，致严格 §3 discover 触发滞后；本轮实务提前补种。RFC-parking 记 housekeeping。
7. **place 远未饱和**：宽扫即得 4 优质净新候选，未测大量中层 toponym；HK-premature-saturation-claim 证伪。
8. **corpus-discover 顺延临界**：since_corpus=92（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV5 节奏**：since_evv5=5→6，约 R160 触发。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **散文门债**：37 页 >400（既有 DEFERRED，本批零自致）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
