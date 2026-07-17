---
round: 139
date: 2026-07-15
type_round: 110
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 5
pages: []
result: discover
---

# GROW 2.1-B · R139 · SCN28 · place — 表层 discover 补种（5 强候选，discover_streak_low 1→0，place 远未饱和再证）

## 本轮公告

**R139 — Phase 2.1 — SCN28 — place — 州/城级 toponym 复扫，5 新 buildable 候选，discover_streak_low 1→0**

R138（EVV5）后：since_evv5=0、since_discover=10、discover_streak_low=1、queue(place)=9、since_corpus=75。
决策矩阵 §3 首匹配：since_evv5=0<10（非 1a/1b）、streak=1<3（非 2）、**since_discover=10≥10 且 queue=9<10 → 优先级 3 SCN28 触发**。
本轮不新建/编辑任何页面，纯表层 discover：对 `data/sentence_index/` toponym 词边界扫描，凑 ≥5 distinctPN
且未建的地名候选，补入 queue。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5≥10）| =0（R138 刚 RESET）| 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =1 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **since_discover=10≥10 且 queue=9<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus≥30，项目扩展）| =75 | 否（非 §3 分支，记 HK-corpus-discover-not-in-statemachine PARK）|
| 7 | NEW1（默认）| — | 否 |

## 扫描方法与结果

对既有 queue 9 项（Illinois/Michigan/Missouri/Ohio/Colorado/Soudan/Guinea/Abyssinia/Indiana）之外，
批测 23 个未建州/城级 toponym 的 gather distinctPN + 逐样本 solid vs 泛指/异指判定。原始命中与裁定：

| distinctPN | 候选 | 判定 |
|-----------|------|------|
| 21 | Illinois | （既在 queue，待筛泛指）|
| **18** | **Pennsylvania** | ✅ **新增**——solid ≥5：DSCF×3（Tom 等自由黑人所属州）+ MW×2（Master of the World 剧场州）|
| **15** | **Connecticut** | ✅ **新增 强**——AM×9（Sphinx of Ice：Jeorling 故乡）+ MW×3；跨源确指 |
| 15 | Michigan | （既在 queue，须 vs lake-michigan）|
| **14** | **Kentucky** | ✅ **新增**——solid 5：FF×3 Mammoth Cave 洞窟对照 + JCE×1 猛犸洞 + MW×1（Frankfort）|
| 14 | Missouri/Ohio | （既在 queue，疑河）|
| **13** | **Massachusetts** | ✅ **新增**——solid ≥5：BR Fort Sumter「Massachusetts granite」+ DSCF Salem 棉布 + MW×3；待细筛城名列举 |
| **11** | **Sacramento** | ✅ **新增**——AWED×4（太平洋铁路西端/SF↔Sacramento/Sacramento River 汽船）+ GM×5（加州淘金）+ EHLA×2 |
| 13 | Colorado | （既在 queue，疑河）|
| 8 | Virginia | ⏸ 待筛——BR 烟草/FF Norfolk 城确指 solid + 多州列举/DSCF 废奴枚举；solid 边界 4–5，入队待凑 |
| 7 | Arkansas | ⏸ DEFER——多指 Arkansas River（AWED-028-030/030-014）+ 州列举；仅 MW-008-040 Little Rock 确指州，<5 clean |
| 7 | Louisiana | ⏸ 待筛——FEM 1803 拿破仑售路易斯安那史 + 离岸 solid + Gulf 海岸弧枚举；solid 边界，入队待凑 |
| 5 | Tennessee | ⏸ hold——FEM-010-008 系铁甲舰 ram Tennessee（异指）+ 州列举；仅 MW-004-013 Nashville 确指，<5 clean |
| 5 | Indiana | （既在 queue，勉达门）|
| 4 | Kansas | ✗ <门 hold |
| 3 | Ogden | ✗ <门 |
| 2 | Cincinnati | ✗ <门 |
| 0 | Cheyenne | ✗ 无命中 |

**净新 buildable 候选 = 5**（Connecticut / Pennsylvania / Kentucky / Massachusetts / Sacramento），
另 3 项（Virginia / Louisiana / Arkansas）入队 待筛/DEFER，Tennessee/Kansas hold（<5 clean）。

## SCN28 结论

表层 discover 显 place **远未饱和**：单轮凑得 **5 净新 buildable 候选**，另 3 待筛项。
承 R131 premature-saturation 教训——**扫描广度足够时候选充盈**，此前「归零」判断系采样不足所致。
new_candidates=5 ≥ type_close_new_candidate_min=3 → **discover_streak_low 1→0**（远离 CLOSE 门）。
queue(place) 开放 buildable 候选补至约 14（原 9 待筛/干净 + 5 新 buildable）。

下轮 R140：since_discover 归 0、queue≈14≥10、since_evv5=1 → §3 无 discover/EVV5/CLOSE 触发 → **§3(7) NEW1**（建页）。
建议序：Connecticut（AM 强）→ Sacramento（AWED/GM）→ Pennsylvania（DSCF/MW），干净度高优先。

## EXIT-GATE 检查（SCN28 轮：G4 + 不变式；G1/G2/G3 不适用——不建页）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；queue.md 补 5 buildable + 3 待筛 + Texas 补记 consumed；grow_state SCN28 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3（PN grounding/散文门/≥5PN）不适用——本轮不新增/编辑页面。
> 排除检查：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。

## state 更新（SCN28 six-step）

`current_round 139→140`；`type_round 110→111`；`rounds_since_last_evv5 0→1`（SCN28 非 EVV5，+1）；
`rounds_since_last_discover 10→0`（**discover RESET**）；`discover_streak_low 1→0`（new=5≥3，RESET）；
`rounds_since_last_corpus_discover 75→76`（表层 discover 非 corpus，+1）；`last_updated_round→140`。

## 遗留问题

1. **place 页数保持 353**：本轮非建页，registry 全库 1421，unknown 0。
2. **discover_streak_low 归 0**：5 新 buildable 候选远超门，CLOSE 风险清零。place 广度扩张续行。
3. **下轮 R140 = NEW1**：since_discover 归 0、queue≈14≥10、streak=0、since_evv5=1 → §3(7) NEW1 建页。
   建议序 Connecticut→Sacramento→Pennsylvania→Kentucky→Massachusetts（5 新 buildable），再消费既有 9 待筛项（河/湖/泛指须建前消歧）。
4. **待筛/DEFER 项**：Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）。
5. **corpus-discover 顺延临界**：since_corpus=75，远过阈 30 但非 §3 分支（PARK）；待表层近罄时议 corpus 深扫。
6. **EVV5 节奏**：since_evv5=1，下次约 R149。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **散文门债**：37 页 >400（既有 DEFERRED；本批 5 页 R131–R136 自致，R137 起收紧，R140 续守）。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧。
