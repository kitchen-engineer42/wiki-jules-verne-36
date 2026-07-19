---
round: 293
date: 2026-07-18
type_round: 59
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R293 · SCN28-zombie · event — 续掘单事件作品第二事件，采 TT/ASC/WC 三部终末高潮，掘建序 43-45

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 59）。R289 discover 队列建序 40-42 已于 R290/291/292 全消费，**queue(event)==0**。决策机 §3 首匹配 **SCN28-zombie**
（since_evv5=4<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=3<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**）。

**续「单事件作品掘第二事件」策略**：语料零事件作品池 R275 已竭；本策略从单事件作品掘其终末（terminal）第二事件。已建十二部第二 event（RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/RM/EHLA/AM）。
本轮 re-scan 余单事件作品，按章数（长篇优先）与终章 pn_anchor 反查，采 **TT/ASC/WC** 三部长篇之终末高潮，掘 3 候选建序 43-45。

**逐句核实（framing 视为线索、逐章复核终局）**：
- **建序 43 maston-calculation-error（TT-020）**：核 TT-020 终局揭晓章——Barbicane/Nicholl 追问失败之因，Alcide Pierdeux 于 Times 揭 Maston 取地球周长时漏三零（40,000 代 40,000,000），十二零之差致炮击近乎无效、北极仅移三千分之一毫米（TT-020-034/036/038）；溯因 Maston 遭雷击+Scorbitt 电话两度打断漏写末三零（TT-020-045）；世人先讥后贺其误免全球倾覆之灾（TT-020-041/042）。与既有 kilimanjaro-cannon-shot（TT-017..019 巨炮发射）PN 区段不重叠、分工明确（发射 vs 失败之因）。
- **建序 44 tjon-viaduct-sacrifice（ASC-025）**：核 ASC-025 终末灾变章——Faruskiar 暗设扳道岔将列车引上未竣 Nanking 支线趋 Tjon 断桥深渊欲夺帝国十五百万金宝（ASC-025-003/009），藏箱之 Kinko 令锅炉顶爆使车骤停免坠、以身殉全车百命（ASC-025-004/006/015），众悟英雄乃 Kinko 非 Faruskiar（ASC-025-007），Noltitz/Bombarnac 当众揭 Faruskiar 即匪首（ASC-025-033/044/048）。与既有 ki-tsang-train-attack（ASC-020..021 中途匪劫）PN 区段不重叠、分工明确（匪劫 vs 终局叛卖救难）。
- **建序 45 recognition-of-erik（WC-021）**：核 WC-020/021 认亲终局——冰原 O'Donoghan 携秘而死、恶人 Tudor Brown 亦毙（WC-020-002/003），Alaska 鸣炮救 Erik 父子、完成首次环极航行归 Stockholm（WC-020-007/024），Erik 向记者坦陈航行真意寻身世未果、传记译遍欧洲传至巴黎（WC-020-032/035/039），Durrien 读报识出外孙、去信「My dear child」相认（WC-021-004/005/008）。与既有 waif-cynthia-rescue（WC-002/006 开篇拾婴）PN 区段不重叠、分工明确（拾婴 vs 认亲）。

**VVV 宽度**：TT/WC 2-char、ASC 3-char——均为正常宽度，无需 RFC-0003 Note（Note 仅限 4-char 且 PN 断行者）。

**dup-check（filesystem + registry sweep）**：三 exact-slug + 全变体 filesystem ABSENT；work 页 aliases sweep（topsy-turvy / adventures-of-a-special-correspondent / the-waif-of-the-cynthia）无 label/alias 冲突。链目标 work 页均存在（[[Topsy-Turvy]]、[[The Adventures of a Special Correspondent]]、[[The Waif of the Cynthia]]），建序 43 另链 [[Gun Club]]。

new_candidates=3 ≥ type_close_new_candidate_min(3) → **productive**，discover_streak_low 保持 0。queue(event) 0→3。本轮不建页，registry 不变（total 1531，event 56，unknown 0）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)==0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

（discover 轮，不建页；掘 3 候选入 queue）

| 建序 | slug | pn_anchor | 作品(VVV) | 事件焦点 | 与首事件分工 |
|------|------|-----------|-----------|----------|-------------|
| 43 | maston-calculation-error | TT-020 | Topsy-Turvy(TT,2c) | Maston 漏三零致北极运河巨炮惨败、误反免灾 | vs kilimanjaro-cannon-shot(发射) |
| 44 | tjon-viaduct-sacrifice | ASC-025 | The Adventures of a Special Correspondent(ASC,3c) | Tjon 断桥前 Kinko 殉难止车、Faruskiar 叛卖被揭 | vs ki-tsang-train-attack(中途匪劫) |
| 45 | recognition-of-erik | WC-021 | The Waif of the Cynthia(WC,2c) | Erik 环极归来、Durrien 读传记认外孙 | vs waif-cynthia-rescue(开篇拾婴) |

## EXIT-GATE 检查

- **G4 脚本建页**：本轮 discover 不建页，无 pages/** 写入。✔
- **registry 一致**：不建页，total 1531 event 56 unknown 0 不变。✔
- **查重充分**：三 exact-slug + 全变体 filesystem ABSENT；work 页 aliases sweep 无冲突。✔
- **framing 核实**：三候选终章逐句核（TT-020 揭误 / ASC-025 揭叛 / WC-020/021 认亲），均与首事件 PN 区段不重叠。✔
- **new_candidates≥min**：3≥3，productive，streak 保持 0。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie，grow_state 存 R294 起始计数）

| 字段 | R293 起始 | R294 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 293 | 294 |
| type_round | 59 | 60 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 229 | 230 |
| last_updated_round | 293 | 294 |

## 遗留问题

1. **queue(event) 0→3**：本轮掘建序 43-45。registry 全库 **1531**，unknown 0（不建页）。
2. **下轮 R294 = NEW1（§3(7)）**：since_evv5=5<10；streak=0<3；since_discover=0<10 且全局 queue≥10 → §3(3) 否；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 43 maston-calculation-error（TT，anchor TT-020）**。TT 2-char 无需 Note；逐句核 TT-020 追问-揭误-溯因-免灾序列、剔 kilimanjaro-cannon-shot 发射别线。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。三候选建时须逐句复核（尤 TT-020 揭误、ASC-025 揭叛、WC-020/021 认亲）。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略·余矿**：单事件作品第二事件矿脉，已采十二部 + 本批 TT/ASC/WC 三部（建后共十五部）。余单事件作品 BR(10c)/TN(20c)/PL(9c)/MZ(5c)/WAI(16c)/DOSE(17c)/GM(22c) 留后续 zombie 批次；**DA 单章短篇不可掘第二事件**（排除）；**GM 首事件 wreck-of-the-dream 已引 GM-022-022 终章，掘 GM 第二事件时须慎防重叠**。MW（Master of the World / The Master of the World）实为同作双 label（HK 待批归一），非单事件作品。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=229→230（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
