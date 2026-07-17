---
round: 161
date: 2026-07-16
type_round: 132
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 5
pages: []
result: discover
---

# GROW 2.1-B · R161 · SCN28 · place — 深层候选补种（实务触发：R155 批全消、净 buildable 罄）；净新 5 buildable：Kachgar/Tachkend/Douchak/Brindisi/Concepcion

## 本轮公告

**R161 — Phase 2.1 — SCN28 — place — 中亚/远东铁路站·地中海港·南美城 toponym 宽扫 / 非建页 / since_discover 归 0 / new_candidates=5**

R160 EVV5 后 since_evv5=0、since_discover=5、streak=0、queue(place) 名义>0 但净 buildable=0、since_corpus=96。
R155 补种批（Formentera/Ceuta/Samarkand/Callao）四项 R156–R159 全消，既有 queue 仅剩 sub-gate DEFER/hold 项
（Louisiana 净3、Arkansas/Tennessee <5 clean state、Virginia 净4、Indiana 净0、Colorado/Michigan 河湖歧义）。

**净 buildable 实务归零，触发深层 SCN28 补种。** 依 memory feedback「Exhaustively re-scan before claiming saturation」，
非从 queue 推断枯竭，而是对语料宽扫新 toponym。属 HK-queue-size-scope 情形（名义 queue_size 高估净可建）；
本轮以实务判断提前补种，不建页。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R160 刚 reset）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| 名义 since_discover=5<10；**净 buildable=0 实务触发** | **触发（实务）** |
| 7 | NEW1（默认）| — | 否（无净可建，被实务 SCN28 抢占）|

> **实务裁定说明**：严格 §3 本应 NEW1，但净可建=0 使 NEW1 无对象。依 R155 同款裁定与 memory feedback，
> 提前行 SCN28 补种（等价于 queue_size 按净 buildable 计则 <10 触发 §3(3)）。counter 按 SCN28 更新。

## 扫描方法与结果

对 `data/sentence_index/` 宽扫中亚/远东铁路站（Claudius Bombarnac/ASC）、80 天环游沿线港（AWED）、
南美太平洋岸城（In Search of the Castaways/SC、The Pearl of Lima/PL），每候选统计 distinctPN、
**双向查重既有页（label+aliases+id，含拼写/音译变体）**、抽样判 solid（剔铁路站名并列与行程表列举）。

| 候选 | distinctPN | 主源 | 查重 | 抽样判定 | 入队? |
|------|-----------|------|------|---------|------|
| Kachgar | 24 | ASC | new | Chinese Turkestan 首府/Grand Transasiatic 华属段（008-032/013-108/015-045/015-075/016-002）；剔 Merv/Bokhara 列举后 ≥5 solid | ✅ |
| Tachkend | 15 | ASC | new（alias Tashkend）| 俄属突厥斯坦城（013-006 Samarkand→300km/014-001 1870 集市/014-003 停 2.5h/014-007 人口/006-011 pedlars）；剔 005-018/023 列举 | ✅ |
| Douchak | 11 | ASC | new | Transcaspian 660th verst 站（008-022/023/025/028/060/010-041）；≥5 solid | ✅ |
| Brindisi | 8 | AWED | new | 地中海邮轮港（006-003/006-007/006-008/009-002/003-012）；⚠ 剔 003-029/007-031/007-032 行程表列举后 ~5 solid，建前复核 | ✅ |
| Concepcion | 6 | SC | new | 智利古城（007-038/008-066/009-006/010-004/010-005 震后妇孺村）；⚠ ~5 临界，建前复核 | ✅ |
| Valparaiso/Auckland/Yokohama/Suez/Omaha/Tiflis/Shanghai/Allahabad/Benares/Teheran/Talcahuano | 高 | — | **✘ 已建** | 既有页（Talcahuano=bay-of-talcahuano）| ✘ |

**净新 buildable = 5**（Kachgar/Tachkend/Douchak/Brindisi/Concepcion），均未建、均 ≥5 solid distinctPN 门
（Brindisi/Concepcion 临界，建前复核）。11 候选判重既有页——**HK-discover-existing-type-blindspot 主动规避**
（本轮双向查重含变体，建前捕获 Talcahuano=bay-of-talcahuano 等）。

## SCN28 结论

**队列深层补种成功。** 净新 5 buildable 入队，覆盖新源（ASC Chinese Turkestan/Transcaspian、AWED 地中海港、SC 智利）
与既有薄弱区域（中亚东段、意大利、智利）。下轮 R162 起转 NEW1，按 solid 强度/源多样性序建：
**Kachgar（ASC 24，Chinese Turkestan 首府）→ Tachkend（ASC 15）→ Douchak（ASC 11）→ Brindisi（AWED 8，地中海港）→ Concepcion（SC 6，智利）**。
模板不修改，不触发 backfill，不新起 RFC。

> **附**：本轮再证 place 类型**远未饱和**——宽扫即得 5 优质净新候选（仅测部分中亚东段/环游港/智利城，
> 未测大量东欧/近东/远东/北美中层 toponym）。HK-premature-saturation-claim 三度证伪。

## EXIT-GATE 检查（SCN28 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；grow_state SCN28 six-step；queue.md R161 marker 追加；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 six-step）

`current_round 161→162`；`type_round 132→133`；`rounds_since_last_evv5 0→1`（SCN28 非 EVV5 轮，+1）；
`rounds_since_last_discover 5→0`（SCN28 RESET）；`discover_streak_low` 保持 0（new_candidates=5≥3）；
`rounds_since_last_corpus_discover 96→97`；`last_updated_round→162`。

## 遗留问题

1. **place 页数保持 370**：本轮非建页，registry 全库 1438，unknown 0。
2. **下轮 R162 = NEW1**：since_discover 归 0、queue 补 5 项 → §3(7) NEW1。建 **Kachgar** 首（ASC Chinese Turkestan 首府，24 distinctPN）。
3. **R161 补种建序**：Kachgar → Tachkend → Douchak → Brindisi → Concepcion（solid/源多样性序）。
4. **DEFER 复议维持**：Virginia 净4（距门 1，待凑第 5 solid）、Indiana 净0（不可建）；Louisiana/Arkansas/Tennessee hold；Colorado/Michigan 河湖歧义待逐条剥离。
5. **HK-discover-existing-type-blindspot 主动规避**：本轮对每候选双向查重（label+aliases+id 含变体），建前捕获 11 既有页（含 Talcahuano=bay-of-talcahuano 音译变体）。查重纪律已内化。
6. **HK-queue-size-scope 再证**：名义 queue 有项但净 buildable=0，致严格 §3 discover 触发滞后；本轮实务提前补种。
7. **place 远未饱和**：宽扫即得 5 优质净新候选，未测大量中层 toponym；HK-premature-saturation-claim 三度证伪。
8. **corpus-discover 顺延临界**：since_corpus=96→97（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV5 节奏**：R160 刚 reset，since_evv5=0→1，下次约 R171。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **散文门债**：37 页 >400（既有 DEFERRED，本批零自致）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
