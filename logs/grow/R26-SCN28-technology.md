---
round: 26
date: 2026-07-15
type_round: 4
phase: "2.1"
current_type: technology
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R26 · SCN28 · technology — 换角度复扫（+0，streak 1→2）

## 本轮公告

**R26 — Phase 2.1 — SCN28 — technology — 0 页（discover 轮）**

queue(technology)=0，zombie-guard 再触 SCN28。R25 已跨全集确认穷尽；本轮**换角度**——聚焦
「命名 apparatus/engine」与「专名载具」二次核验，仍 **+0**。**streak 1→2，CLOSE 倒计时推进。**

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =1 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=13, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =24 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(technology)=0 | **触发 SCN28** |

## SCN28 — technology 换角度复扫（apparatus + 专名载具）

| 候选 | 探测 | 判定 | 处置 |
|-----|------|------|------|
| Ruhmkorff / Bunsen | 18 / 6 | 既有页 ruhmkorff-apparatus / 真实器件 | 弃（既有/通用） |
| aeronef | 110 | = Albatross 别名（albatross.aliases 含 aeronef）| 弃（既有页别名） |
| the Ebba | 100 | FF 海盗伪装 schooner（潜水拖船母船），叙事载具/专名帆船 | 弃 technology → place/2.1-Z 候选 |
| the Susquehanna | 21 | FEM/AM 美军巡洋舰，叙事载具 | 弃 technology → place/2.1-Z |
| the Duncan | 187 | ISC 游艇，叙事载具 | 弃 technology → place/2.1-Z |
| the Great Eastern | 3 | TTLU 提及的真实汽船 | 弃（真实船只）|
| apparatus（泛）| 176 | 多为既有页（diving/ruhmkorff）或通用描述 | 弃 |

| 结果 | 数值 |
|------|------|
| 换角度复扫命中新命名发明 | 0 |
| 既有别名/真实器件/叙事载具弃 | 多 |
| **technology new_candidates** | **0** |
| discover_streak_low | **1→2（new_candidates 0 < 3）** |

> **专名载具归属重申**：the Ebba（FF）新入普通船只清单——与 Duncan/Pilgrim/Chancellor/Susquehanna
> 同属「叙事载具/专名帆船」，非凡尔纳特制中心机器，依 Pilot 惯例不入 technology，留 place/2.1-Z 裁定。
> 注意：Ebba 是 R25 borderline「the tug」的伪装母船——若 place 轮建 Ebba，可回链 the tug 的复议。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 记 Ebba 入普通船只清单；grow_state step-six→R27（streak 1→2，since_discover→0，since_evv5→5，since_corpus→25）|

## state 更新

`current_round 26→27`，`type_round 4→5`，`rounds_since_last_evv5 4→5`，
`rounds_since_last_discover→0`，`discover_streak_low 1→2`（new_candidates=0），
`rounds_since_last_corpus_discover 24→25`。`current_type` 仍 technology，`last_updated_round→27`。

## 遗留问题

1. **R27 = technology SCN28（zombie-guard）**：streak=2，再 +0 → streak 2→3。R27 为 technology 末轮
   discover。
2. **R28 = CLOSE+SCN28**：streak 达 3 触 CLOSE，关闭 technology（final_count≈20）→ current_type
   转 place，type_queue 弹出 place（余 [event, character]）。since_evv5 R28=6 未达 10，EVV5 不抢先。
   CLOSE 同轮 SCN28 为 place 首轮 discover（补种 place 候选）。
3. **place 首轮预备**：queue P2 已有 place 候选 Stone's Hill / Pacific Railroad；红链 place 及 36 部
   合集地名（Lincoln Island / Back Cup / Quiquendone / Iceland / Stahlstadt 等）待 place discover 收集。
4. **the tug / Ebba borderline**：待 place 轮 Ebba 建页时复议 the tug 是否补建 technology。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
