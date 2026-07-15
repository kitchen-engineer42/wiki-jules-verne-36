---
round: 21
date: 2026-07-15
type_round: 11
phase: "2.1"
current_type: organization
gene: CLOSE+SCN28
new_candidates: 1
pages: []
result: accept
---

# GROW 2.1-B · R21 · CLOSE+SCN28 · organization → technology — 关闭 organization，补种 technology

## 本轮公告

**R21 — Phase 2.1 — CLOSE+SCN28 — organization 关闭 → technology 启动 — 0 页**

R20 EVV5 后 `since_evv5` 归零，`discover_streak_low=3 ≥ type_close_streak(3)`，决策矩阵优先级 2
触发 **CLOSE+SCN28**：关闭 organization（final_count=15），切换 current_type→technology，
并原子性执行 technology 首轮 discover 补种候选队列。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =0（R20 刚重置）| 否 |
| **2** | **CLOSE+SCN28（discover_streak_low ≥ 3）** | =3 | **触发** |

## 类型切换（organization ACTIVE → CLOSED）

依 grow-state-machine.md §5.1 原子执行：

| 动作 | 值 |
|------|-----|
| closed_type | organization |
| final_count（pages.json 计 type==organization）| **15** |
| closed_types += | `{type: organization, closed_at_round: 21, final_count: 15, evv6_score: null}` |
| type_queue 弹出首位 | `[technology, place, event, character]` → `[place, event, character]` |
| current_type | organization → **technology** |
| 类型级计数器重置 | type_round=0，discover_streak_low=0，rounds_since_last_evv5=0 |

> evv6_score 留 null，待 Phase 2.1-Z-0 阶段关闭评审 EVV6 回填（grow-state-machine.md L220、L1251）。
> organization final_count=15 = GROW 建 13（R11 建 5 + R13 建 5 + R16 建 2 + R18 建 1）+ Pilot 既有
> gun-club / weldon-institute 2。

### organization 类型总结（work 之后第 2 个关闭类型）

- 起始：R10（work 关闭后切入），历 R10–R21 共 12 轮。
- 建页：13 页（GROW），全 standard/deep 档，PN grounding 达标（pn_count 4–28）。
- discover：SCN28 红链（R12/R14）+ org-suffix 标准复扫（R15/R19）+ broadened 复扫（R17）交叉覆盖。
- EVV5（R20）：模板稳定，无结构变动。
- judgment-hold（R15/R17）：合计多建 3 个达门 org（north-west / cgtc / inquiry-committee），已兑现为 grounded 页面，留用户批量复审。

## SCN28 — technology 首轮 discover（补种新类型队列）

technology 既有 16 页（Pilot 建），本轮 discover 找 Pilot 未覆盖的新发明/机器候选。

**红链扫描**（label-aware 未解析 wikilink）：命中全为 character/place（已在 queue P2）+ 20KL "Seas"
复数 alias 错配（既有 HK），**无 technology 红链**（尚无页链向新 tech）。

**语料专名探扫**（命名船只/机器/发明，distinctPN≥3，排除既有 16 页）：

| distinctPN | 专名 | 判定 | 处置 |
|-----|------|------|------|
| **≈39** | **Go-Ahead** | **真发明**（Weldon Institute 建造的巨型飞艇 aerostat，对抗 Robur 的 Albatross；RC-022-008 "most perfect type of what had...been invented in aerostatic art"）| **新候选 → queue P1（technology）** |
| 602 | Weldon | 误报（Mrs. Weldon 人物 + Weldon Institute 组织，非 tech）| 弃 |
| 46 | Doctor Ox | 误报（Dr. Ox 人物）| 弃 |
| 213/82/54/49… | Pilgrim / Chancellor / Abraham Lincoln / Duncan / Mongolia / Rangoon / Carnatic / Henrietta / Tankadere / Susquehanna / Scotia / Halbrane / General Grant | 普通船只（叙事载具/场景，非发明）| 弃（同 Pilot 惯例，仅特制/中心机器入 technology；borderline 留 place/2.1-Z）|
| 1 | Fulgurator | 真发明但 distinctPN=1 不达门（FF Roch 的炸药）| 弃（低于 ≥3 门）|

| 结果 | 数值 |
|------|------|
| technology new_candidates | **1（Go-Ahead）** |
| discover_streak_low | **0（新类型 §5.1 重置基线；首轮 discover 即得 grounded 候选）** |

> **streak 说明**：CLOSE §5.1 将 discover_streak_low 重置为 0（新类型从零起）。technology 首轮
> discover 即命中 Go-Ahead（distinctPN≈39 真发明），streak 保持 0，无 judgment-hold（与 R15/R17
> 不同——此为 §5.1 规定的新类型基线重置，非机械增量的判断性覆盖）。

## EXIT-GATE 检查（CLOSE+SCN28 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；closed_types +organization；type_queue 弹出 technology；queue.md +Go-Ahead(P1 technology)；grow_state 切换 current_type→technology + 计数器重置 + step-six→R22 |

### 不变式核验（grow-state-machine.md §6）

| # | 不变式 | 结果 |
|---|--------|------|
| I1 | type_queue ∩ closed_types = ∅ | PASS（[place,event,character] ∩ {work,organization} = ∅）|
| I2 | current_type 不在 closed_types | PASS（technology ∉ {work,organization}）|
| I3 | 所有 counter ≥ 0 | PASS |
| I4 | grow_phase 格式 "2.N" | PASS（"2.1"）|
| I5 | phase2_closed==True ⟺ grow_phase=="3" | PASS（False / "2.1"）|

## state 更新

`current_type` organization → **technology**；`type_queue` → [place, event, character]；
`closed_types` += organization(final_count 15)；`current_round 21→22`，`type_round` **重置 0**，
`rounds_since_last_evv5` **重置 0**，`rounds_since_last_discover→0`，`discover_streak_low` **重置 0**，
`rounds_since_last_corpus_discover 19→20`。`last_updated_round→22`。

## 遗留问题

1. **R22 = technology NEW1 建 Go-Ahead**（1 页 standard，RC/MW）：Weldon Institute 飞艇，姊妹页
   [[Albatross]] / [[Weldon Institute]]；grounding RC-003-012/013、RC-022-002/006/008/009/011、
   RC-023-019 等（distinctPN≈39 充足）。建后 queue(technology)=0。
2. **R23 = technology SCN28**：确认 technology 是否穷尽（Pilot 已建 16 页 + R22 Go-Ahead = 17）。
   预期候选稀少 → 可能快速 streak 累积 → 短 technology 周期后转 place。
3. **technology Mini-Pilot 豁免**：technology 非全新类型（既有 16 Pilot 页 + 模板 technology-schema），
   无需 2.1-A Mini-Pilot（2–3 页 + EVV5），直接沿用既有模板 NEW1 建 Go-Ahead。
4. **普通船只归类**：Duncan/Pilgrim/Chancellor 等叙事载具留 place/2.1-Z 裁定（同 Pacific Railroad）。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
