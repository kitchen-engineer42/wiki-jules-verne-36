---
round: 41
date: 2026-07-15
type_round: 13
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 30
pages: []
result: discover
---

# GROW 2.1-B · R41 · SCN28 · place — 表层复扫补种（+30 候选）

## 本轮公告

**R41 — Phase 2.1 — SCN28 — place — 0 建页 / 表层地理标记复扫 / 补种 30 候选**

R40 末 queue(place)=9 < 10，轮首决策矩阵优先级 3（`queue_size < 10`）先于 NEW1 触发 →
本轮为 **SCN28 表层复扫**（discover 轮）：不建页、不消费队列，全 sentence_index 地理标记
正则扫描，析出 ≥5 distinctPN 且未成页/未在队的新 place 候选，补种候选池。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=1 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9 < 10** | **触发** |

## 扫描方法

全 968 个 `data/sentence_index/*.jsonl` 逐句正则：
- PRE 型 `(Cape|Lake|Mount|Fort|Port|Loch|Gulf|Isle|River|Point|Peninsula|Harbour|Falls|Creek|Strait|Bay|Cove|Sound|Island)\s+[A-Z]\w+`
- POST 型 `[A-Z]\w+\s+(Island|Bay|River|Sea|Point|Strait|Gulf|Cove|Sound|Mountains|Lake|Cape|Rock|Reef|Channel|Land|...)`

按候选名 × 源作（VVV）聚 distinctPN（sid 前三段去重），取**主源** distinctPN（非跨源聚合，
承「深扫聚合跨源误报」教训）。阈值 ≥5 得 60 原始候选，剔假阳后curate 30 入队。

## 假阳性剔除

| 剔除项 | 原因 |
|--------|------|
| Ned Land（TTLU:265）| 人物（POST「Land」误捕），非地点 |
| Bay Company（FC:27）| 「Hudson's Bay Company」组织，非地点 |
| Greek Islands / Caribbean Sea / Antarctic Sea | 泛称，叙事角色薄，暂缓 |
| Sandwich Islands / Chatham Islands 等 | 历史泛称，低叙事权重，暂缓入 tail |

## 勘误：Flag Point 恢复入队

**Flag Point（GM）** R34/R36/R38 三度以「GM 仅 4 distinctPN」误弃。R41 严扫 `Flag Point` GM 专扫，
实测 **14 distinctPN**（GM-015-038/050/051/056、016-008/018/027/069/071、017-002/020/024/073、021-098）。
系 Godfrey 于荒岛所命之岬（竖信号旗处），真实 fictional 地点，达 standard 门。**勘误恢复入队**。
根因归入「深扫聚合 distinctPN 跨源误报」债务的**对偶**：早期严扫计数亦曾偏低，建前逐候选严扫为准。

## 补种候选（30，主源 distinctPN 严扫）

| 簇 | 候选（主源:distinctPN）|
|----|----------------------|
| FC 漂流 | Behring Sea(13) / Fort Confidence(16) / Slave Lake(12) / Aleutian Islands(12) |
| ACH 北极 | Melville Bay(12) / Wellington Channel(10) / Lancaster Strait(7) / Bellot Strait(7) / Barrow Strait(6) / Cape Farewell(8) / Victoria Bay(6) / Cape Washington(5) |
| MW 大湖 | Niagara River(12) / Black Rock Creek(17) / Lake Superior(6) / Lake Michigan(6) |
| 各作真实 | Ural Mountains MS(21) / Salt Lake AWED(10) / Fort Kearney AWED(9) / Amsterdam Island SC(9) / Lake Taupo SC(8) / Cape Corrientes SC(5) / Port Egmont AM(9) / Lake Tanganyika DSCF(6) / Pamlico Sound FF(21) |
| AM/MI/GM 虚构 | Halbrane Land AM(14) / Creek Glycerine MI(13) / Mandible Cape MI(9) / Washington Bay MI(7) / Flag Point GM(14, 勘误) |

## EXIT-GATE 检查

| 门 | 结果 | 说明 |
|----|------|------|
| G4 记录完整性 | PASS | 本日志；queue.md 补种 30 候选（不消费）；grow_state six-step |

> SCN28 discover 轮不建页，故 G1 PN / G2 散文门 / G3 schema 不适用，仅核 G4。

## state 更新（SCN28 six-step）

`current_round 41→42`；`type_round 12→13`；`rounds_since_last_evv5 1→2`；
`rounds_since_last_discover 4→0`（discover 轮重置）；`discover_streak_low` 保持 0（高产 30 ≥ 3）；
`rounds_since_last_corpus_discover 8→9`（表层 SCN28 不重置 corpus 计数，仅 SCN28-corpus 深扫重置）；
`last_updated_round→42`。

## 遗留问题

1. **queue(place)=39**（9 + 30 补种）→ R42 恢复 NEW1（queue ≥10，since_discover=0）。
   下批优选高分：Ural Mountains(MS:21) / Pamlico Sound(FF:21) / Black Rock Creek(MW:17) /
   Fort Confidence(FC:16) / Halbrane Land(AM:14) / Flag Point(GM:14) / Behring Sea(FC:13) /
   Creek Glycerine(MI:13) / Niagara River(MW:12)。建前逐页复核 distinctPN、查同实体合并。
2. **Flag Point 三度误弃勘误已记**：早期严扫计数偏低（4 vs 实 14），非仅聚合高估。
   建前严扫为唯一裁定口径，double-check 上下限。
3. **tail 候选（暂缓，低权重/待核）**：Sandwich Islands / Chatham Islands / Fort Sumter / Morris Island /
   Sullivan Island（BR 内战地理）/ Cape Tchelynskin(WC) / Lake Tinn(TN) / Platte River(AWED) /
   Detroit River(MW) / Fort Independence(SC) / Mount Mendif(FWB) / Lake Ukereoue(FWB) /
   Icy Cape(FC) / Coronation Gulf(FC) / Washburn Bay(FC) / Lake Barnett(FC) / Isle Tabor(SC，或即 tabor-island 别名，建前查合并) / Gueboroa Island(TTLU) / Cape Saknussemm(JCE) / Mandible 已入。若 R42+ 消费见底再 curate。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
