---
round: 284
date: 2026-07-18
type_round: 50
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R284 · SCN28-zombie · event — 队列耗尽再勘探，掘 3 单事件作品之终末第二事件（建序 37-39）

## 执行摘要

Phase 2.1-B event 类型**第六次 discover**（type_round 50）。R283 NEW1 消费建序 36 后 queue(event)=0，
R284-start 决策机 §3 首匹配 **SCN28-zombie**（§3(4)：since_evv5=6<10 → 非 §3(1)；streak=0<3 → 非 §3(2)；
since_discover=3<10 且全局 queue≥10 → 非 §3(3)；**queue(event)==0 → §3(4) 触发**）。

SCN28 为**勘探轮，非建页**：扫描语料寻 event 新候选，写入 queue.md，更新计数（since_discover reset）。**pages: []，registry 恒 1525，event 恒 50，unknown 0。**

## 勘探策略（续 R280）

零 event 作品池已穷尽（R275 确认）。续「**单事件作品掘第二事件**」策略——R278/R279/R281/R282/R283 已从 RC/MW/MS/FF/SC2/DSCF 各掘第二 event 成功建页。
本轮脚本化统计全 50 event 页 book 分布：**20 部作品现仅 1 event**（A Drama in the Air / A Winter Amid the Ice / An Antarctic Mystery / Doctor Ox's Experiment / Eight Hundred Leagues on the Amazon / Five Weeks in a Balloon / Godfrey Morgan / Master Zacharius / Master of the World / Off on a Comet / Round the Moon / The Adventures of a Special Correspondent / The Blockade Runners / The Fur Country / The Master of the World / The Pearl of Lima / The Secret of the Island / The Waif of the Cynthia / Ticket No. 9672 / Topsy-Turvy），
为第二事件矿脉。本轮择其三富矿（FC/FWB/OC）逐章勘探，各掘一离散**终末第二事件**（首事件均为「开端/中段」性质，第二事件取「终局高潮」，天然离散）。

> 注：「Master of the World」与「The Master of the World」在 book 字段呈两独立作品名（terror-destruction vs great-eyrie-investigation 均 MW），实为同作 book label 不一——HK 级归一债，非本轮范畴，记录待批。

## 勘探结果（建序 37-39，queue(event) 0→3）

| 建序 | slug | 作品(VVV) | pn_anchor | 事件 | 预估 PN |
|------|------|-----------|-----------|------|---------|
| 37 | disintegration-of-victoria-island | The Fur Country (FC) | FC-046 | Victoria Island 融缩成小岛再裂为浮冰、Hobson 率殖民者困三角浮冰漂散、终获救 | ≥8（FC-044/045/046/047 序列）|
| 38 | joes-sacrifice-over-the-desert | Five Weeks in a Balloon (FWB) | FWB-042 | 气球濒坠、Joe 自愿跃出减负孤身涉险、Talabas 骑队追逐、Ferguson 险中复救、终抵 Senegal | ≥8（FWB-041/042/043 序列）|
| 39 | return-to-earth-by-balloon | Off on a Comet (OC) | OC-044 | Gallia 彗星复近地时众制热气球升空脱 Gallia、越 Gallian Sea、返地球 | ≥8（OC-042/043/044/045 序列）|

**各候选查重**（filesystem exact-slug + 变体，全 ABSENT）：
- disintegration-of-victoria-island（+ breakup-of-victoria-island/victoria-island-breakup/melting-of-victoria-island）ABSENT。
- joes-sacrifice-over-the-desert（+ the-last-sacrifice/joes-leap/balloon-over-senegal）ABSENT。
- return-to-earth-by-balloon（+ gallia-balloon-ascent/escape-from-gallia）ABSENT。

**建时注意**：
- FC 2-char / OC 2-char / FWB 3-char 均无需 RFC-0003 Note。
- 三锚均为线索非定论，建时逐句复核（尤 FC-046 崩解序列、FWB-042 跳球牺牲、OC-044 升空返地）。**R283 已现改锚先例（DSCF-014→DSCF-013），本轮三锚同须建时逐句核实动作序列所在章。**
- 单指核：各剔已覆盖首事件别线（FC ice-island-drift 脱陆之始、FWB missionary-rescue、OC comet-collision 撞地之始）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)=0** | **触发** |
| 5–7 | RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 SCN28 勘探，无建页、无改页。产出 3 候选写入 queue.md（建序 37-39）。

## EXIT-GATE 检查（SCN28 轮）

- **G1–G4**：无建页/改页，N/A（勘探轮）。
- **registry 一致**：total 1525 event 50 unknown 0 恒定（无写页）。✔
- **勘探充分**：全 50 页 book 分布脚本化统计；20 单事件作品识别；三候选逐章勘探、查重、预估 PN。✔
- **new_candidates=3 ≥ type_close_new_candidate_min(3)** → productive，discover_streak_low 保持 0（非 low-yield）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean（本轮仅 state+log+queue）。✔

## 六步状态机（SCN28，grow_state 存 R285 起始计数）

| 字段 | R284 起始 | R285 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 284 | 285 |
| type_round | 50 | 51 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 3 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 220 | 221 |
| last_updated_round | 284 | 285 |

## 遗留问题

1. **event 页数 50**（勘探轮无建页）。queue(event)=**3**（建序 37/38/39 seeded）。registry 全库 1525，unknown 0。
2. **下轮 R285 = NEW1（event）**：since_evv5=7<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(7) NEW1。
   建建序 37 **disintegration-of-victoria-island**（FC，FC-046）。FC 2-char 无需 Note；建时核融缩-裂浮冰-困冰-获救单指、剔 ice-island-drift(脱陆之始 已覆盖)别线；须逐句复核崩解序列所在章（锚 FC-046 为线索）；链 [[The Fur Country]]。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。R283 首现改锚（DSCF-014→DSCF-013）。本轮三锚同须建时逐句核动作序列所在章。
4. **event 覆盖策略**：20 单事件作品为第二事件矿脉；已掘 RC/MW/MS/FF/SC2/DSCF 六部，本轮 seed FC/FWB/OC 三部。余 17 部（A Drama in the Air/A Winter Amid the Ice/An Antarctic Mystery/Doctor Ox's Experiment/Eight Hundred Leagues on the Amazon/Godfrey Morgan/Master Zacharius/Round the Moon/The Adventures of a Special Correspondent/The Blockade Runners/The Master of the World/The Pearl of Lima/The Secret of the Island/The Waif of the Cynthia/Ticket No. 9672/Topsy-Turvy 等）留后续 zombie 轮续掘。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并补 PN 至 ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）**新增**：「Master of the World」/「The Master of the World」book label 归一（terror-destruction/great-eyrie-investigation 同作 MW）。
6. **event PN 回填债**：13/50 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=220→221（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
