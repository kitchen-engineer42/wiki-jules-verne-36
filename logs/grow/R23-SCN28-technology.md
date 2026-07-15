---
round: 23
date: 2026-07-15
type_round: 2
phase: "2.1"
current_type: technology
gene: SCN28
new_candidates: 3
pages: []
result: accept
---

# GROW 2.1-B · R23 · SCN28 · technology — 广类扫描修正 R21 盲区（+3 候选）

## 本轮公告

**R23 — Phase 2.1 — SCN28 — technology — 0 页（discover 轮）**

R22 后 queue(technology)=0，zombie-guard 触 SCN28。R21 首轮 discover 仅扫**命名船只/飞行器**，
本轮扩展到**武器/气体/装置/仪器**类发明复扫，命中 3 个 R21 漏判的真发明。**technology 未穷尽。**

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=13, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =21 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(technology)=0 | **触发 SCN28** |

## SCN28 — technology 广类复扫（武器/气体/装置/仪器）

R21 首轮 discover 聚焦命名船只/飞行器（Go-Ahead 命中，普通船只弃），**未扫武器/气体/装置类**——
此即 HK-corpus-discover-orgname-blindspot 的 technology 变体（窄模式漏判）。本轮扩展候选词表复扫：

| distinctPN | 专名 | 判定 | 处置 |
|-----|------|------|------|
| **44** | **Fulgurator** | **真发明**（Thomas Roch 的毁灭性爆炸武器，FF 核心 McGuffin；FF-011-016 "composition of his fulgurator"）| **新候选 → queue P1** |
| **37** | **the Sword** | **真发明**（潜水艇/潜水器，Davon 中尉驾驶潜入 Ker Karraje 巢穴；FF-015-039 "lines around the hull of the Sword"；Nautilus 类特制潜艇）| **新候选 → queue P1** |
| **6** | **oxyhydric gas** | **真发明**（Doctor Ox 制氧氢气，管道输城致居民亢奋；DOSE-003-041 "Oxyhydric gas."）| **新候选 → queue P1** |
| 101 | aeronef | 既有页别名（= Albatross，albatross.aliases 含 aeronef）| 弃 |
| 120/116/47/22 | sledge / telegraph / electric light / telephone | 泛用真实技术/普通名词，非凡尔纳特制发明| 弃 |
| 19/19/16 | submarine boat / torpedo / accumulators | 泛用描述/通用器件，非单一命名实体 | 弃 |
| 5/5 | helices / Bunsen | Albatross 螺旋桨（既有页）/ 真实器件 | 弃 |
| 1–2 | Frankville / Herr Schultze / phonograph | distinctPN 不达门（≥3）| 弃 |

| 结果 | 数值 |
|------|------|
| 广类命中真发明（distinctPN≥3，非既有）| 3 |
| 泛用/既有/低频弃 | 多 |
| **technology new_candidates** | **3（Fulgurator / the Sword / oxyhydric gas）** |
| discover_streak_low | **保持 0（new_candidates 3 ≥ 3；候选池未枯竭）** |

> **盲区修正**：R21 曾 project「technology 或仅 Go-Ahead 一页后穷尽」，本轮证伪——扫描模式偏窄
> （仅船只/飞行器）导致漏判 FF/DOSE 的武器·潜艇·气体发明。教训同 organization 的 org-name
> blindspot：discover 须覆盖类型全部子范畴（technology = 载具+武器+气体+仪器+装置）。已扩词表复扫。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md P1 +3 technology 候选；grow_state step-six→R24（type_round 1→2，since_evv5 1→2，since_discover→0，streak 保持 0，since_corpus 21→22）|

## state 更新

`current_round 23→24`，`type_round 1→2`，`rounds_since_last_evv5 1→2`，
`rounds_since_last_discover→0`，`discover_streak_low` 保持 0（new_candidates=3），
`rounds_since_last_corpus_discover 21→22`。`current_type` 仍 technology，`last_updated_round→24`。

## 遗留问题

1. **R24 = technology NEW1 建 3 候选**（Fulgurator / the Sword / oxyhydric gas，≤5 页 standard 批）：
   Fulgurator + the Sword 同源 FF（Facing the Flag），oxyhydric gas 源 DOSE（Doctor Ox's Experiment）。
   slug 建议：fulgurator / the-sword（或 sword-submarine）/ oxyhydric-gas。
2. **R25 = technology SCN28**：三候选建后再复扫确认是否还有漏判（如 Steam House/Standard Island 若
   在语料——R21 探扫 0 命中，疑不在 36 部合集）。
3. **HK 记录**：technology discover 窄扫盲区已在本轮修正；可考虑将「discover 须覆盖类型全子范畴」
   补入 HK-corpus-discover-orgname-blindspot 条目（technology 变体佐证），待批量复审。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
