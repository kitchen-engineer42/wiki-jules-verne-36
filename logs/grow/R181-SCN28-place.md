---
round: 181
date: 2026-07-17
type_round: 152
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 5
pages: []
result: discover
---

# GROW 2.1-B · R181 · SCN28 · place — 表层 toponym 复扫（净新 5 buildable：Tsalal/Tristan d'Acunha/Bennet Islet/Long's Peak/Stapi）

## 本轮公告

**R181 — Phase 2.1 — SCN28 — place — 表层 toponym 复扫 / 非建页 / since_discover 归 0 / new_candidates=5**

R180 NEW1（Irtish）后 R181 起始：since_evv5=9、since_discover=10、discover_streak_low=0、queue(place) 名义>0 但净 buildable 近罄、since_corpus=117。
决策矩阵 §3 首匹配：since_evv5=9<10 故非 1a/1b；streak=0<3 故非 2；**since_discover=10≥discover_periodic_interval(10) → 优先级 3 SCN28 触发**。
承 R180 遗留 #2「R181 走 discover：宽扫 AM/JCE/FEM/OC 未采 toponym，补 queue」，本轮对 sentence_index 做未采层 toponym 复扫。
本轮不新建/编辑任何页面，不修改模板。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=9<10 | 否 |
| 1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **since_discover=10≥10** | **触发** |
| 7 | NEW1（默认）| — | 否（被 3 抢占）|

> SCN28（3）§3 首匹配。SCN28 重置 since_discover=0，since_evv5+1（→10）、since_corpus+1；
> new_candidates=5≥type_close_new_candidate_min(3) → discover_streak_low 保持 0（非低产轮）。

## 扫描方法与结果

对 `data/sentence_index/` 做 word-boundary toponym 复扫（gather.py），聚焦 R179–R180 记录的未采主脉：
AM（An Antarctic Mystery）/JCE（Journey to the Center of the Earth）/FEM（From the Earth to the Moon）/OC（Off on a Comet）。
对每候选统计 distinctPN、按源作品（VVV）拆分、抽样判 solid（主体确指）vs 泛指/异指。
筛除已建页（文件系统 `ls docs/wiki/pages/*/<slug>.md` + 拼写变体，承 R180 查重纪律）。凑净 solid ≥5 distinct FULL PN 者入队。

| 候选 | distinctPN | 主源 | 裁定 | 入队? |
|------|-----------|------|------|------|
| Tsalal | 90 | AM | Pym 叙事南极岛（土著/Grampus 幸存者被带至；Halbrane 目的地）主体确指，最强 | ✅ 入队（最强）|
| Tristan d'Acunha | 45 | AM×29+SC×14 | 大西洋岛，Halbrane 卸货地/南洋航线常提；多源主体 | ✅ 入队 |
| Bennet Islet | 19 | AM×13(+FWB×6 异指) | 以 Jane 船东合伙人 Bennet 命名之岛，赴 Tsalal 途中（005-054/011-013/012-017）；AM×13 净≥5 | ✅ 入队 |
| Long's Peak | 16 | FEM×8+RM×7(+TT×1) | Rocky Mtns 巨镜观测台，Gun Club 望远镜架设/月弹观测电报（024-022/027-008/013/016）| ✅ 入队 |
| Stapi | 10 | JCE | Snæfell 半岛南麓村，火山脚下牧师宅，下降前驻地（011-011/011-014/013-035/014-002/014-005/014-017）| ✅ 入队 |

**净新 buildable = 5**（Tsalal/Tristan d'Acunha/Bennet Islet/Long's Peak/Stapi），均未建、均 ≥5 solid distinctPN。

### 复扫既有排除（文件系统查重命中，未入队）

- **AM**：gourbi-island（OC，非 AM）/christmas-harbour/halbrane-land 均已建；Falklands=falkland-islands 已建。
- **JCE Iceland**：snaefellsjokull（=Sneffels，R180 已确认）已建；Cape Portland（JCE×3 净<5）DEFER；Altona（JCE×6 多为 Kiel/Altona/Hamburg 过境列举 + Gräuben 寄居，净<5）DEFER；Reykjavik/Gardar（0 命中，Verne 拼写待考）暂搁。
- **FEM/OC 城市**：malta/gibraltar/ceuta/formentera/florida/texas/hamburg/copenhagen 皆已建。

## SCN28 结论

**队列补种成功。** 净新 5 buildable 候选入队（R150 discover 后既有优质项由 R151–R180 消耗殆尽，本轮转 AM/JCE/FEM/OC 未采主脉复扫补充，印证「主矿脉建齐后新矿转向 Verne 小众作品 toponym」的 R179–R180 判断）。
候选质量：Tsalal（AM×90，最强，Pym 叙事核心岛）> Tristan d'Acunha（45，多源）> Bennet Islet（AM×13）> Long's Peak（15）> Stapi（10）。
下轮 R182 = EVV5（since_evv5 SCN28 后=10≥10 → §3(1b)），reflection 非建页；R183 起转 NEW1，按序建 **Tsalal → Tristan d'Acunha → Bennet Islet → Long's Peak → Stapi**。
模板不修改，不触发 backfill，不新起 RFC（组件债依 RFC-parking 记 housekeeping）。

> **附**：HK-premature-saturation-claim 再否——「主矿脉近饱」不等于 place 类型饱和；AM/JCE/FEM/OC 未采层本轮即补 5 项，续 exhaustive re-scan，未宣布饱和。

## EXIT-GATE 检查（SCN28 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；grow_state SCN28 six-step；queue.md R181 marker + 5 候选行追加；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 six-step）

`current_round 181→182`；`type_round 152→153`；`rounds_since_last_evv5 9→10`（SCN28 非 EVV5 轮，+1）；
`rounds_since_last_discover 10→0`（SCN28 RESET）；`discover_streak_low` 保持 0（new_candidates=5≥3）；
`rounds_since_last_corpus_discover 117→118`；`last_updated_round→182`。

## 遗留问题

1. **place 页数保持 386**：本轮非建页，registry 全库 1454，unknown 0。
2. **下轮 R182 = EVV5**：SCN28 后 since_evv5=10≥10 → §3(1b) EVV5 触发（reflection/schema 评审，非建页），since_discover=0 故非 1a。
3. **R183+ 建序（本轮补种 5 项，solid 强度序）**：Tsalal → Tristan d'Acunha → Bennet Islet → Long's Peak → Stapi。
4. **净 buildable 收窄再证（HK-queue-size-scope）**：R150 补 5 项经 R151–R180 耗尽，本轮再补 5；耗尽后须再 SCN28 或转 corpus 深扫（since_corpus=118，已远过阈 30，HK-corpus-discover-not-in-statemachine PARK）。
5. **DEFER/待考项**：Cape Portland（JCE×3 净<5）、Altona（JCE×6 混列举）、Reykjavik/Gardar（0 命中，Verne 拼写待考——JCE 冰岛首府/主教区应有别拼，下次 discover 专项查）、Tobol 河（MS×1）。
6. **主矿脉建齐盘点（承 R180）**：DSCF 安哥拉/ASC 中亚/MS 西伯利亚主站及河系（Irtish✔ Obi/Yenisei 既有）/FWB 非洲均建齐；新矿续 AM（Tsalal 等待）/JCE（Stapi 待）/FEM（Long's Peak 待）/OC 未采层。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮非建页。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积（承 R180）**：Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、Baikal/Timbuktu/Tampa/Sneffels/Ishim DUPLICATE、Cape Portland/Altona DEFER。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
