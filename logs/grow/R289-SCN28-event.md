---
round: 289
date: 2026-07-18
type_round: 55
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R289 · SCN28-zombie · event — 勘探轮，掘 RM/EHLA/AM 三部单事件作品之第二事件（建序 40/41/42）

## 执行摘要

Phase 2.1-B event 类型第 55 轮（type_round 55）。R288 EVV5 reset since_evv5=0；R289-start since_evv5=0、streak=0、since_discover=4<10 且全局 queue≥10（非 §3(3)）、**queue(event)==0 → 决策机 §3(4) SCN28-zombie 触发**。

SCN28-zombie 为**勘探轮，非建页**：续「单事件作品掘第二事件」策略（零 event 作品池 R275 已穷尽），
自 20 单事件作品中采 **RM（Round the Moon）/ EHLA（Eight Hundred Leagues on the Amazon）/ AM（An Antarctic Mystery）** 三部之终末高潮，
逐章核实、seed 3 net-new 候选入 queue 建序 40/41/42，reset since_discover=0。**pages: []，registry 恒 1528，event 恒 53，unknown 0。**

## 勘探方法（R286 framing 教训贯彻）

三候选均**逐句核 sentence_index 文本**确认事件离散、锚准确、与既有 event 无重叠、≥8 distinct PN 可达；exact-slug + 全变体 filesystem dup-check 全 ABSENT；registry label/alias sweep 无 event 覆盖。

### 建序 40 — recovery-of-the-projectile（RM，Round the Moon）

- **第二事件**（RM 现仅 lunar-orbit-miss RM-008 掠月未着）：Columbiad 炮弹返地溅落太平洋、Susquehanna 号打捞获救。
- **pn_anchor RM-022**（打捞高潮章：连日搜海底徒劳→忽见铝弹因比重轻浮于海面 022-061→开舱得 Barbicane/Nicholl/Ardan 三人安然弈骨牌 066/067）。RM-020 测深 + RM-021 电告 Gun Club 邻章可补。
- 逐句核实：RM-021-027 电文「炮弹十二日坠太平洋」；RM-022-046「浮标在下风舷」→ 052 美利坚国旗 → 061 Maston 顿悟「它浮着！」→ 064 开破损舷窗 → 066 Ardan 呼「double blank」→ 067 三人正弈骨牌。**framing 准确**，锚无误。
- aliases [The Susquehanna Rescue, Splashdown in the Pacific, Recovery from the Ocean Bed]（避「The Projectile」——technology 页 label）。链 [[Round the Moon]]+[[Gun Club]]。RM 2-char 无需 Note。
- 剔 lunar-orbit-miss（掠月，首 event 已覆盖）。

### 建序 41 — rescue-of-joam-dacosta（EHLA，Eight Hundred Leagues on the Amazon）

- **第二事件**（EHLA 现仅 amazon-cryptogram EHLA-027..034 密文解谜苦斗）：绞架前的临刑赦免。
- **分工核实（关键，避重叠）**：既有 amazon-cryptogram 覆盖**智力解谜/文档**（PN 止于 EHLA-034，「the analytical struggle to read it is the climax」），**未涉绞架场景**；本页覆盖**临刑赦免/人物营救**（EHLA-038/039），二者分工明确、非重复。
- **pn_anchor EHLA-039**（章题句「ON THE ARRIVAL of the judge the mournful procession halted」，Jarriquez 携破译密文赶至刑场宣读高潮）。EHLA-038 行刑令 + Fragoso 疾驰携 Ortega 之名邻章可补。
- 逐句核实：EHLA-038-002 行刑定 8 月 31 晨九时 → 009「是 Fragoso！」（携亡友 Ortega 之名）→ EHLA-039-001 判官至刑队止 → 004 宣读 → 011 真凶自白 → 015 Ortega 自愿招认 → 016「以 Ortega 之数破全文」。**framing 准确**。
- aliases [The Gallows Reprieve, Vindication of Joam Dacosta, The Ortega Confession]。链 [[Eight Hundred Leagues on the Amazon]]+[[The Amazon Cryptogram]]。
- **EHLA 4-char → 建时须核 PN 渲染，如断行加 RFC-0003 Note**。
- 剔 amazon-cryptogram（解谜苦斗，首 event 已覆盖）。

### 建序 42 — the-ice-sphinx（AM，An Antarctic Mystery）

- **第二事件**（AM 现仅 halbrane-wreck AM-018..020 冰崩毁 Halbrane 号）：冰之 Sphinx 揭晓为巨磁、觅得 Arthur Pym 尸。
- **pn_anchor AM-025**（磁 Sphinx 揭晓高潮章：舟上铁器悉被撕离 035/040→悟 Sphinx 乃巨型天然磁石 054/056→Dirk Peters 于其基觅 Pym 干尸 082/084→恸绝倒毙 086）。AM-024 Paracuta 逃生 + AM-026 北返邻章可补。
- 逐句核实：AM-025-035 铁器骤被撕离 → 054「一块磁石！」→ 056 Antarctic Sphinx 乃巨磁 → 072 Peters 身向 Sphinx 倾如被吸 → 082 跪对半裸尸 → 084 锈枪横缚尸身 → 085「Pym 我可怜的 Pym」→ 086 心碎倒毙 → 087 Pym 亦为磁流所擒。**framing 准确**，锚无误。
- aliases [The Magnetic Sphinx, Fate of Arthur Pym, Death of Dirk Peters]（避 work 页 alias「The Sphinx of the Ice Fields / Le Sphinx des glaces」）。链 [[An Antarctic Mystery]]。AM 2-char 无需 Note。
- 剔 halbrane-wreck（冰崩，首 event 已覆盖）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **=0** | **触发** |
| 5–7 | RCH2 系/NEW1 | — | — |

## 页面处理记录

本轮为 SCN28-zombie 勘探，无建页、无改页。产出 3 net-new 候选入 queue（建序 40/41/42），详见上「勘探方法」及 `logs/butler/queue.md` R289 discover 块。

## EXIT-GATE 检查（SCN28 轮）

- **G1–G4**：无建页/改页，N/A（勘探轮）。
- **registry 一致**：total 1528 event 53 unknown 0 恒定（无写页）。✔
- **勘探充分**：三候选逐句核 sentence_index 文本（framing 准确性 R286 教训贯彻）；exact-slug+全变体 filesystem dup-check 全 ABSENT；registry label/alias sweep 无 event 覆盖；三 work 页（round-the-moon/eight-hundred-leagues-on-the-amazon/an-antarctic-mystery）均存在可链。✔
- **new_candidates=3 ≥ type_close_new_candidate_min(3)**：productive discover，discover_streak_low 保持 0。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean（本轮仅触 state+log+queue）。✔

## 六步状态机（SCN28，grow_state 存 R290 起始计数）

| 字段 | R289 起始 | R290 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 289 | 290 |
| type_round | 55 | 56 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 4 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 225 | 226 |
| last_updated_round | 289 | 290 |

## 遗留问题

1. **event 页数 53**（勘探轮无建页）。queue(event) 0→**3**（建序 40/41/42 seed）。registry 全库 1528，unknown 0。
2. **下轮 R290 = NEW1（§3(7)）**：since_evv5=1<10；streak=0<3；since_discover=0<10 且全局 queue≥10（非 §3(3)）；queue(event)=3>0（非 §3(4)）；stub%=0（非 §3(5/6)）→ **§3(7) NEW1 默认触发**。建 queue 最小建序候选 = **建序 40 recovery-of-the-projectile（RM）**。**建时须警惕 framing 准确性（R286 教训）**：逐句核 RM-022 浮弹获救序列。
3. **EHLA 4-char 提示**：建序 41 rescue-of-joam-dacosta 建时须核 PN 渲染，如断行加 RFC-0003 Note（参 R283 DSCF 4-char 渲染正常无需 Note 之先例，建时实测为准）。
4. **event PN 回填债（R244/R255/R266/R277/R288 五度记录）**：13/53 早期 event 页 distinct PN <5，DEFERRED，零消解；留待 RCH2 enrich 或 Phase 2.1-Z EVV6 前统一补引。本轮 seed 三候选均逐章核 ≥8 distinct PN 可达（目标 16），不入债。
5. **单事件矿脉进度**：已掘/在掘 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC（九部，第二事件已建）+ 本轮 seed RM/EHLA/AM（三部，待 R290+ 建）。余 14 部单事件作品（A Winter Amid the Ice 已掘 finding-of-louis-cornbutte 属二事件... 复核：AWI/DA/DOSE/GM/MZ/PL/TN/ASC/BR/TT/WC 等，下轮 zombie 前重扫 pn_anchor 反查确认未覆盖）。
6. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」/「The Master of the World」book label 归一（terror-destruction/great-eyrie-investigation 同作 MW）。批量评审时处置。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=225→226（dead 变量，priority 3.5 从不触发）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
