---
round: 73
date: 2026-07-15
type_round: 44
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 8
pages: []
result: discover
---

# GROW 2.1-B · R73 · SCN28 · place — 表层复扫补种（8 候选，非建页）

## 本轮公告

**R73 — Phase 2.1 — SCN28 — place — 0 建页 / 表层复扫 discover / 补种 8 候选 / queue 9→17**

R72（EVV5）后 since_evv5=0、since_discover=4、discover_streak_low=0、queue(place)=9、since_corpus=9。
决策矩阵：since_evv5=0<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
**queue=9<10 → 优先级 3 SCN28 触发**（抢占 NEW1），since_corpus=9<30 → 非 corpus 型。
本轮为表层复扫 discover：补种 place 候选入 queue，不建任何页；since_discover 归 0。
R68 补种 15 强候选已 R69–R71 全数消费，本轮续补 8 强候选（各精核词边界 distinctPN ≥5、
非既有页/人物），聚焦 Michael Strogoff 西伯利亚城镇群 + Eight Hundred Leagues 亚马逊河口镇 + AWED 横滨：
Semipolatinsk / Tobolsk / Kolyvan / Ichim / Baraba / Belem / Tabatinga / Yokohama。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =9 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=9 | 否 |
| RCH2（stub% ≥ 20%）| —（未评估，SCN28 先占）| 否 |
| NEW1（默认）| —（被优先级 3 抢占）| 否 |

## 复扫方法与候选核验

复扫 `data/sentence_index/*.jsonl`，逐候选精核**词边界**（`\bName\b`）distinctPN（段级 PN =
sid 前三段 `VVV-NNN-PPP`），比对 pages.json 的 label/alias/id 排除既有页，逐句抽样确认为地名非人物。
仅保留单作 distinctPN ≥5 的真地点。

| 候选 | 单作 distinctPN（top） | region / real | 排除污染核验 |
|------|----------------------|---------------|--------------|
| Semipolatinsk | MS:5（恰达门）| 西伯利亚/今哈萨克 Semey / real | 专名；MS-002-021 与 Omsk/Tobolsk 并列政府名 |
| Tobolsk | MS:14 / ASC:1 | 西西伯利亚 / real | 词边界；MS-002-060 Cossack 政府所在 |
| Kolyvan | MS:47 | 西西伯利亚 / real | 专名；MS-022-002 Michael 被俘地 |
| Ichim | MS:38 | 西西伯利亚（Ishim）/ real | 专名；MS-022-085 驿站「relay at Ichim」 |
| Baraba | MS:14 | 西西伯利亚巴拉巴草原 / real | 专名；MS-016-008 沼泽地带 region |
| Belem | EHLA:43 | 巴西帕拉州贝伦 / real | 专名；EHLA-014-034「at Manaos and Belem」河口城 |
| Tabatinga | EHLA:23 | 巴西亚马逊边境镇 / real | 专名；EHLA-016-003 巴西/秘鲁边境哨镇 |
| Yokohama | AWED:35 / WC:5 / ASC:4 | 日本横滨 / real | 专名；AWED-024-002 Fogg 日本登陆港 |

> **既有页去重**：8 候选逐一比对 pages.json label/alias/id，**均 new**（无 HK-discover-existing-type-blindspot 命中）。
> **MS 城镇群溯源**：Semipolatinsk/Tobolsk/Kolyvan/Ichim/Baraba 均为 Michael Strogoff 西伯利亚驿路沿线
> real 城镇/region，Verne 依 real 地理设定；与既建 Irkutsk/Omsk/Tomsk（R69–R70）同源，region 归 Siberia。
> **noise/碎片剔除**（不入 queue）：Nijni-Udinsk（MS:2<门）、Ratmanoff/Coron/Kamishlov/Poutorana（0 命中）、
> 孤词/人名假匹配。

## PN 接地核验

本轮不建页，无正文 PN 落地。候选 distinctPN 仅为 queue 强度参考，来自 `data/sentence_index/`
词边界精核；建页轮（R74+）消费时须再逐句复核页内引注 ≥5。

## EXIT-GATE 检查（discover 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 补种 8 候选（9→17）；grow_state SCN28 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 discover six-step）

`current_round 73→74`；`type_round 44→45`；`rounds_since_last_evv5 0→1`；
`rounds_since_last_discover 4→0`（discover 轮，RESET）；
`discover_streak_low` 保持 0（new_candidates=8≥3，不自增）；
`rounds_since_last_corpus_discover 9→10`；`last_updated_round→74`。

## 遗留问题

1. **queue(place) 9→17**：补种 8 强候选后 discover 门解除；R74 起 since_discover=0，
   优先级 3 不再触发，回落 NEW1 建页。
2. **下轮 R74：queue=17≥10、since_evv5=1<10、since_discover=0<10、since_corpus=10<30 → NEW1**。
   建 5 新页（standard 档），消费 queue 头部候选（优先 MS 西伯利亚城镇群 Semipolatinsk/Tobolsk/
   Kolyvan/Ichim/Baraba 或 EHLA Belem/Tabatinga、AWED Yokohama）。
3. **region 待定（建页时确认）**：MS 五镇归 Siberia（Semipolatinsk 今属哈萨克，label 从 Verne 原文，
   region 记 Siberia/Kazakh Steppe）；Belem→Pará (Brazil)、Tabatinga→Amazonas (Brazil)、Yokohama→Japan。
4. **单作强候选渐稀预警**：R73 已扫至 MS/EHLA/AWED 次级城镇；后续 discover 或转向跨源候选精核
   （既有 6 跨源 North Sea/Firth of Clyde/Long Island/Goat Island/Bay of Bengal/Cape Bon）与剩余零散镇名。
5. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）；Kara Sea 建前须精扫。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
