---
round: 150
date: 2026-07-15
type_round: 121
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 5
pages: []
result: discover
---

# GROW 2.1-B · R150 · SCN28 · place — 表层候选补种（净新 5 buildable：Nantucket/Tunis/Timbuktu/Tripoli/Maryland；Georgia 裂页 hold）

## 本轮公告

**R150 — Phase 2.1 — SCN28 — place — 表层 toponym 复扫 / 非建页 / since_discover 归 0 / new_candidates=5**

R149 EVV5 后 since_evv5=0、since_discover=10、discover_streak_low=0、queue(place) 名义≈12 但净 buildable 近罄、since_corpus=86。
决策矩阵 §3 首匹配：since_evv5=0<10 故非 1a/1b；streak=0<3 故非 2；**since_discover=10≥discover_periodic_interval(10) → 优先级 3 SCN28 触发**。
承 R149 遗留 #2「R150 应宽扫补新候选并复议 held/hold 项」，本轮对 sentence_index 做州级/城级/非洲区域级 toponym 复扫，凑 ≥5 distinctPN 且未建者入队。
本轮不新建/编辑任何页面，不修改模板。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=0<10 | 否 |
| 1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **since_discover=10≥10** | **触发** |
| 7 | NEW1（默认）| — | 否（被 3 抢占）|

> SCN28（3）§3 首匹配。SCN28 重置 since_discover=0，since_evv5+1、since_corpus+1；
> new_candidates=5≥type_close_new_candidate_min(3) → discover_streak_low 保持 0（非低产轮）。

## 扫描方法与结果

对 `data/sentence_index/` 做 word-boundary toponym 复扫（gather.py），对每个候选 term 统计 distinctPN、
按源作品（VVV）拆分命中、抽样判 solid（州/城/区域主体确指）vs 泛指（州列举/demonym/异指同名/动植物/河湖异指）。
筛除已建页（比对 `docs/wiki/pages/**`）。凑净 solid ≥5 distinct FULL PN 者入队。

| 候选 | distinctPN | 净 solid | 主源作品 | 裁定 | 入队? |
|------|-----------|---------|---------|------|------|
| Nantucket | 10 | ~8 | An Antarctic Mystery | Pym 出生地（AM-003-054）/Bedford School（AM-005-004）；AM 主体 | ✅ 入队（最强）|
| Tunis | 10 | ~7 | Off on a Comet | Bay of Tunis/Cape Matafuz→Tunis/coast of Tunis（OC×5）+FWB-004-007+RC-015-004 | ✅ 入队 |
| Tripoli | 9 | ~7 | Five Weeks in a Balloon | 出发/复得 Tripoli（FWB-004-007/009/012/030-015/037-036）+OC×2+TT | ✅ 入队 |
| Timbuktu | 7 | ~7 | Robur the Conqueror | Albatross 掠 Timbuktu（RC-015-013/016/020/022/046/051+017-003）| ✅ 入队 |
| Maryland | 6 | 5 | From the Earth to the Moon | Baltimore Maryland/Gun Club 本部（FEM-001-002/003-005）+TT×3 Baltimore 拍卖 | ✅ 入队 |
| Georgia | 24 | 0（美州）| —（裂）| New/South Georgia 南极岛（AM×6）+ Caucasus/俄省 Georgia（ASC×3），无干净美州指 | ⏸ split-candidate hold |

**净新 buildable = 5**（Nantucket/Tunis/Tripoli/Timbuktu/Maryland），均未建、均 ≥5 solid distinctPN。
Georgia 虽 24 distinctPN 但作为单页不可建（南极岛 vs 高加索省两异指主体，无美州主体），标 split-candidate hold。

### 复议既有 held/hold 项

- **Missouri**（R148 DEFER）：州主体净 solid≈0（全 Missouri River 或列举），维持不可建。
- **Colorado/Michigan**（河/湖歧义）：本轮未逐条剥离，续 hold 待专项（大概率同 Missouri 命运）。
- **Virginia（净4）/Louisiana（净3）/Arkansas/Tennessee/Abyssinia（5 勉达）/Indiana（5 勉达）**：维持 DEFER/hold，本轮新增 5 项优先级更高（solid 更足）。

## SCN28 结论

**队列补种成功。** 净新 5 buildable 候选入队（R139 discover 后既有优质项已由 R140–R148 消耗殆尽，本轮复扫补充）。
候选质量：Nantucket（~8 solid，最强）> Tunis≈Tripoli≈Timbuktu（~7）> Maryland（5，勉达门但干净）。
下轮 R151 起转 NEW1，按 solid 强度序建：**Nantucket → Tunis → Tripoli → Timbuktu → Maryland**。
模板不修改，不触发 backfill，不新起 RFC（组件债依 RFC-parking 记 housekeeping）。

> **附**：净 buildable 收窄趋势持续（HK-queue-size-scope 再证）。本轮 5 项补入后，
> place 类型广度仍有 ~5 轮 NEW1 余量；耗尽后须再 SCN28 或转 corpus 深扫（since_corpus=86，HK-corpus-discover PARK）。

## EXIT-GATE 检查（SCN28 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；grow_state SCN28 six-step；queue.md R150 marker 追加；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 six-step）

`current_round 150→151`；`type_round 121→122`；`rounds_since_last_evv5 0→1`（SCN28 非 EVV5 轮，+1）；
`rounds_since_last_discover 10→0`（SCN28 RESET）；`discover_streak_low` 保持 0（new_candidates=5≥3）；
`rounds_since_last_corpus_discover 86→87`；`last_updated_round→151`。

## 遗留问题

1. **place 页数保持 362**：本轮非建页，registry 全库 1430，unknown 0。
2. **下轮 R151 = NEW1**：since_discover 归 0、queue 补 5 项 → §3 首匹配 §3(7) NEW1。建 **Nantucket** 首（AM Pym 出生地，~8 solid，最强）。
3. **本轮补种 5 项建序**：Nantucket → Tunis → Tripoli → Timbuktu → Maryland（solid 强度序）。
4. **Georgia split-candidate**：24 distinctPN 裂为南极 New/South Georgia 岛（AM×6）+ 高加索/俄省 Georgia（ASC×3），无美州主体，须分别专项凑句后各建，本轮 hold。
5. **净 buildable 收窄再证**（HK-queue-size-scope）：R139 discover 项 R140–R148 耗尽，本轮补 5；耗尽后须再 SCN28 或转 corpus 深扫。
6. **河/湖歧义州续 hold**：Colorado（疑 Colorado River）、Michigan（vs lake-michigan），大概率同 Missouri 不可建，建前须逐条查。
7. **corpus-discover 顺延临界**：since_corpus=86→87，已远过阈 30；待表层复扫近罄时转 corpus 深扫（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV5 节奏**：R149 归 0，下次约 R160。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **散文门债**：37 页 >400（既有 DEFERRED，本批零自致，行为纪律已内化）。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧。
