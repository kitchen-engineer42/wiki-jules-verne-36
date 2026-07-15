---
round: 27
date: 2026-07-15
type_round: 5
phase: "2.1"
current_type: technology
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R27 · SCN28 · technology — 末轮 discover 确认穷尽（+0，streak 2→3）

## 本轮公告

**R27 — Phase 2.1 — SCN28 — technology — 0 页（discover 轮）**

queue(technology)=0，zombie-guard 触 SCN28。本轮为 technology **末轮 discover**（武器/照明/电气角度
终扫），仍 **+0**。**streak 2→3 达 type_close_streak 门——R28 触 CLOSE 关闭 technology。**

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=13, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =25 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(technology)=0 | **触发 SCN28** |

## SCN28 — technology 末轮复扫（武器/照明/电气）

| 候选 | 探测 | 判定 | 处置 |
|-----|------|------|------|
| Columbiad / the projectile / gun-cotton | 74 / 365 / 13 | 既有页（columbiad / lunar-projectile / gun-cotton）| 弃（既有）|
| the Albatross / Go-Ahead / Fulgurator | 8 / 1 / 9 | 既有页（albatross / go-ahead / fulgurator）| 弃（既有）|
| electric light / telegraph / phonograph / the cannon / the shell | 47 / 118 / 1 / 70 / 20 | 泛用真实技术/通用名词 | 弃（非特制命名发明，同 R23）|
| melinite | 3 | FF 中对照用真实炸药 | 弃（真实物质）|
| the Pilot | 76 | 多为「领航员/舵手」人称，非命名机器 | 弃（非机器）|
| Maston | 352 | 人物（character 候选，已在 P2 队列）| 弃 technology |

| 结果 | 数值 |
|------|------|
| 末轮复扫命中新命名发明 | 0 |
| 既有页/真实技术/通用词弃 | 多 |
| **technology new_candidates** | **0** |
| discover_streak_low | **2→3（达门 type_close_streak=3）** |

> **technology 穷尽定论**：四轮 discover（R23 broadened +3 → R25 全集 +0 → R26 apparatus/载具 +0 →
> R27 武器/照明 +0）。final 覆盖 20 页：核心机器 + 载具（Go-Ahead/the Sword）+ 武器（Fulgurator）+
> 化学概念（oxyhydric gas）。borderline 债务：the tug（无专名）/ Ebba·Susquehanna·Duncan（叙事载具→
> place）留 place/2.1-Z 复议。**R28 CLOSE。**

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；grow_state step-six→R28（streak 2→3，since_discover→0，since_evv5→6，since_corpus→26）|

## state 更新

`current_round 27→28`，`type_round 5→6`，`rounds_since_last_evv5 5→6`，
`rounds_since_last_discover→0`，`discover_streak_low 2→3`（new_candidates=0），
`rounds_since_last_corpus_discover 25→26`。`current_type` 仍 technology，`last_updated_round→28`。

## 遗留问题

1. **R28 = CLOSE+SCN28（streak=3 触门）**：关闭 technology（final_count 由 pages.json type==technology
   计数确认，预计 20），append closed_types，current_type 弹出 place（type_queue 余 [event, character]），
   重置 type_round=0 / discover_streak_low=0 / rounds_since_last_evv5=0；同轮 SCN28 为 place 首轮 discover。
2. **place 首轮预备**：queue P2 已有 Stone's Hill / Pacific Railroad；36 部合集地名候选丰富
   （Lincoln Island / Back Cup / Quiquendone / Iceland / 各航线/城市），place 权重高（type-survey 第 2）。
3. **the tug / Ebba borderline**：待 place 轮复议。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
