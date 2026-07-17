---
round: 187
date: 2026-07-17
type_round: 158
phase: "2.1"
current_type: place
gene: SCN28
pages: []
new_candidates: 4
result: discover
---

# GROW 2.1-B · R187 · SCN28 · place — discover 补种（R181 队列建罄；转掘 MI/20KL/Hatteras 矿脉，净新 4）

## 执行摘要

Phase 2.1-B place 广度扩张第 158 轮（type_round 158）。R186 建 Stapi 后 R181 discover 队列（5 buildable，Tsalal 除）建罄，
queue(place)=0。决策机 §3 首匹配 **SCN28**：§3(3)（queue_size=0<10）与 §3(4)（queue(place)==0 zombie）同触，走 discover 补种。**非建页轮**。

**矿脉转向**：前批（R181）掘 AM/JCE/FEM/OC 表层 toponym 已建齐（Tristan/Bennet/Long's Peak/Stapi）。
本轮转掘迄今**未系统采掘的三大强矿脉**：
- **Mysterious Island（MI）**：Lincoln Island 地名网密集（Granite House 440、Prospect Heights 96、Mount Franklin 93 等多已建），
  仍余高频未采：Reptile End(16)、Tadorn Marsh(12)。
- **Twenty Thousand Leagues（TTLU/20KL）**：Nautilus 航线地名，余 Vanikoro(14)。
- **Adventures of Captain Hatteras（ACH）**：极地探险地名，余 New America(7)。

**净新 4 buildable**（均 ≥5 solid 抽样确认，文件系统 + 后缀变体查重）：

| slug | 源 | distinctPN | 净 solid（抽样）| 要点 |
|------|-----|-----------|---------------|------|
| reptile-end | MI | 16 | ≥6（013-065/023-052/026-035/026-038/026-041/026-042）| Lincoln Island 西南岬 |
| vanikoro | TTLU(20KL) | 14 | ≥5（019-033/019-042/019-043/019-044 + 019-026/030 对白）| La Pérouse 沉没岛，Nautilus 访 |
| tadorn-marsh | MI | 12 | ≥6（033-074/042-075/053-022/054-004/061-060/061-062）| Lincoln Island 东南沼泽 |
| new-america | ACH | 7 | ≥6（039-053/039-058/039-077/046-069/049-003/051-014/057-016）| Altamont 命名极地大陆/岛 |

new_candidates=4 ≥ min 3 → discover_streak_low 保持 0。since_discover 归 0。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue_size<10 或 since_discover≥10）** | **queue=0<10** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| =0（亦触，同走 discover）| （并触）|
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

> §3(3) 与 §3(4) 同时成立（queue 既 <10 又 ==0），均导向 SCN28 discover。本轮补种 4，R188 起转 NEW1 消费。

## 查重与排除记录

- **入队 4 项均文件系统 + 后缀变体查重**（承 R183 Tsalal 教训）：
  reptile-end（reptile-point NEW）、vanikoro（-island/-islands NEW）、tadorn-marsh（tadorns-marsh NEW）、new-america NEW。
- **既有排除（已建）**：prospect-heights/mount-franklin/union-bay/shark-gulf/granite-house/claw-cape/port-balloon/
  serpentine-peninsula/flotsam-point/washington-bay/crespo-island/victoria-bay。
- **DEFER**：
  - **Cape Mandible**（MI×5）→ 既有 `mandible-cape`（"Mandible Capes" 复数，同一岬簇）overlap，DEFER（Tsalal 式同指规避）。
  - **Indian Peninsula**（6）→ 多为 "Great Indian Peninsula Railway" 铁路名 + RM 泛指对比，非确指地点，净 solid<5，DEFER。
  - **Balearic Isles**（OC×5）→ 薄，多对白/从属 Formentera（已建），DEFER。

## 六步状态机（SCN28，grow_state 存 R188 起始计数）

| 字段 | R187 起始 | R188 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 187 | 188 |
| type_round | 158 | 159 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 5 | 0（RESET）|
| discover_streak_low | 0 | 0（new_candidates=4≥3）|
| rounds_since_last_corpus_discover | 123 | 124 |
| last_updated_round | 187 | 188 |

## 遗留问题

1. **place 页数 390**（本轮未建页）。registry 全库 1458，unknown 0。
2. **下轮 R188 = NEW1**：since_evv5=5<10、since_discover=0<10、queue=4>0 → §3(7) NEW1。
   建 **Reptile End**（MI×16，Lincoln Island 西南岬），建前文件系统查重 + 抽样 ≥5 solid。
3. **R188+ 建序（本批 4）**：Reptile End → Vanikoro → Tadorn Marsh → New America（4 项后队列罄，再 SCN28）。
4. **矿脉盘点**：MI 为迄今最密地名网（Granite House 440 等），本轮仅采 2 高频未采项（Reptile End/Tadorn Marsh），
   MI 仍有中频未采层（后续 discover 续掘）；20KL Vanikoro、ACH New America 开采。未宣布任何类型饱和。
5. **discover 查重纪律**：入队即查 slug + 后缀变体，已执行。
6. **EVV5 临近**：since_evv5=5，距 10 尚 5 轮；R188–R192 NEW1 建 4 项后，约 R193 触 EVV5。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=123→124（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：+ Cape Mandible（overlap mandible-cape）/Indian Peninsula/Balearic Isles DEFER；
    既有 Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、
    Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
