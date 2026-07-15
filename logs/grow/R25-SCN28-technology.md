---
round: 25
date: 2026-07-15
type_round: 3
phase: "2.1"
current_type: technology
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R25 · SCN28 · technology — 复扫确认穷尽（+0 候选，streak 0→1）

## 本轮公告

**R25 — Phase 2.1 — SCN28 — technology — 0 页（discover 轮）**

R24 建完 3 页后 queue(technology)=0，zombie-guard 触 SCN28。本轮全语料复扫确认 technology 是否穷尽。
R23 已 broadened（武器/气体/装置）复扫一轮，本轮**跨全 36 部合集**再确认三类之外的漏判——
命中 **0 个新命名发明**。**technology 收尾倒计时启动（streak 0→1）。**

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=13, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =23 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(technology)=0 | **触发 SCN28** |

## SCN28 — technology 全语料复扫（确认穷尽）

既有 20 页（Pilot 16 + Go-Ahead + R24 三页）覆盖：核心机器（Nautilus/Albatross/Terror/Forward/
Columbiad/…）+ 载具（Go-Ahead/the Sword）+ 武器（Fulgurator）+ 化学概念（oxyhydric gas）。
本轮跨全集探扫剩余候选：

| 候选 | 探测 | 判定 | 处置 |
|-----|------|------|------|
| Standard Island / Propeller Island | SI 工作码实为《神秘岛》第三部（Ayrton/Duncan/Lincoln 岛），**非** Propeller Island | 语料不含此作 | 弃（不在 36 部） |
| Steam House（机械象）| 全集 `steam house` 命中 0 | 语料不含此作 | 弃（不在 36 部） |
| Begum 巨炮 / Stahlstadt / Frankville | Begum=1，Stahlstadt=0，Frankville=2 | 《Begum's Fortune》实质不在合集 | 弃（distinctPN 不达门） |
| Great Eastern | TTLU 中 2 处提及，真实汽船非凡尔纳发明 | 真实船只 | 弃 |
| aluminium | 19（FEM/AM 炮弹材料）| 既有页 lunar-projectile 材料，非独立实体 | 弃 |
| sledge | 144（Hatteras 等冰橇）| 泛用载具非命名发明（同 R23）| 弃 |
| Dobryna / Hansa | 1 / 5（Hector Servadac 船只）| 叙事载具非发明 | 弃 |
| **the tug（FF 海盗潜水拖船）** | **distinctPN=8**；"a submersible boat, a submarine tug, worked by a screw set in motion by electricity"（FF-008），带 periscope | **真机器但无专名**（仅"the tug"），同 R23 弃"submarine boat"惯例 | **borderline 弃**（见判例） |

| 结果 | 数值 |
|------|------|
| 全集复扫命中新命名发明 | 0 |
| 泛用/既有/不在合集/无专名弃 | 多 |
| **technology new_candidates** | **0** |
| discover_streak_low | **0→1（new_candidates 0 < 3）** |

> **GROW-JUDGMENT-R25（the tug borderline）**：FF 海盗潜水拖船 distinctPN=8、机械描述具体（电力螺旋桨 +
> periscope + 三段式），是全书核心载具，*够格*成 technology；但全书仅以通名"the tug / submarine tug"
> 指称，**无专名**（不同于 the Sword / Go-Ahead / Nautilus 等命名实体）。依 R23 弃"submarine boat /
> torpedo"的「须单一命名实体」惯例，本轮**弃**，记为最强 borderline。若后续 place/event 轮出现关联专名
> （如其伪装母船 schooner *Ebba*），可复议是否补建 technology 或归 place。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 记 the-tug borderline；grow_state step-six→R26（streak 0→1，since_discover→0，since_evv5→4，since_corpus→24）|

## state 更新

`current_round 25→26`，`type_round 3→4`，`rounds_since_last_evv5 3→4`，
`rounds_since_last_discover→0`，`discover_streak_low 0→1`（new_candidates=0），
`rounds_since_last_corpus_discover 23→24`。`current_type` 仍 technology，`last_updated_round→26`。

## 遗留问题

1. **R26 = technology SCN28 或收尾**：streak=1，尚需连续 3 轮低命中才触 CLOSE。R26 zombie-guard 仍会触
   SCN28（queue(technology)=0），预期再 +0 → streak 1→2。technology 周期临近结束。
2. **CLOSE 倒计时**：streak 需达 type_close_streak=3。当前 1，预计 R26→2、R27→3 触 CLOSE+SCN28，
   关闭 technology（final_count≈20）转 place。注意 since_evv5 R26=4/R27=5，未达 10，EVV5 不抢先。
3. **the tug borderline（GROW-JUDGMENT-R25）**：已记 queue，待 character/place 轮 Ebba 关联复议。
4. **Thomas Roch / Ker Karraje / Doctor Ox / Davon 红链**：R24 埋入的人物红链待 character 轮消费。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
