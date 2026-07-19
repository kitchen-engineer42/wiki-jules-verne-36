---
round: 305
date: 2026-07-19
type_round: 71
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R305 · SCN28-zombie · event — exhaustive re-scan 零新候选，event 二次矿竭，discover_streak_low 1→2

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 71）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=1<3 → §3(2) 否；since_discover=2<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**）。

R302 批建序 49-50（rescue-of-carefinotu / failing-of-the-zacharius-clocks）已于 R303/R304 全消费，queue(event) 归 0，触发 zombie re-scan。

**re-scan 结论（exhaustive，遵「claiming saturation 前须扫全语料」memory 规则）：new_candidates=0**。

本轮从 pages.json 重建 event→work map（64 event 页 / 33 book），逐 book 判定「单事件」作品仅余 6 项，无一可掘干净离散第二事件：

| # | book | 单事件页 | 判定 |
|---|------|---------|------|
| 1 | A Drama in the Air | the-madman-in-the-balloon | 单章短篇，不可掘第二离散事件 |
| 2 | Doctor Ox's Experiment | quiquendone-frenzy | **饱和**：首事件已引 DOSE-001/002/003/004（设置）+ 013/014/015/016/017（狂乱-爆炸-揭秘双极）；中段 005-012 为弥散渐 escalation（巨植/兽/急奏/议会激辩）非离散事件 |
| 3 | The Blockade Runners | charleston-blockade-run | **饱和**：首事件已引 BR-001/002/003/004/006/007/008/009/010（十章之九，闯关-救囚 Halliburtt-逃逸全弧） |
| 4 | Master of the World | terror-destruction | 与 #5 **实为同一小说 MW**（book label 未归一，HK 债）；MW 已有二事件、非单事件 |
| 5 | The Master of the World | great-eyrie-investigation | 同 #4 |
| 6 | The Secret of the Island | destruction-of-lincoln-island | 属 Mysterious Island(MI) 三部曲第四事件；MI 另有三事件，非单事件 |

**双事件矿累计已建二十部**（…/WAI/TN/PL/GM/MZ），GM 群兽弧（GM-018/019/020）判弥散谜团弧、且与 GM-021/022 火灾-揭秘纠缠，R302 已定不采。**结论：单事件作品第二事件矿竭。**

**充分性**（memory 规则遵守）：本轮非仅据 queue.md bare lines 推断，而是重建 event→work map + 逐 book PN 覆盖复核（BR 十章之九、DOSE 双极已覆盖），如实记 new_candidates=0。

**低产判定**：new_candidates=0 < type_close_new_candidate_min(3) → **discover_streak_low 1→2**。续一轮 zombie 仍低产（streak 达 3）→ CLOSE+SCN28 收 event 切 character。

本轮 discover 轮，不建页（pages: []）。registry 不变（event 64、total 1539、unknown 0）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| — | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 discover 轮，无建页/编辑。仅记 re-scan 负结果 + 更新 grow_state + 写日志。

## EXIT-GATE 检查

- **G1–G3、schema**：discover 轮不建页，N/A。✔
- **G4 脚本建页**：本轮不建页，无 Write/Edit 于 pages/**。✔
- **registry 一致**：不变（total 1539 event 64 unknown 0）；build_registry 未跑（无页变动）。✔
- **re-scan 充分性**：重建 event→work map + 逐 book 判定（6 单事件 book 全覆盖）；非据 queue.md 推断。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie，grow_state 存 R306 起始计数）

| 字段 | R305 起始 | R306 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 305 | 306 |
| type_round | 71 | 72 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 2 | **0**（SCN28 重置）|
| discover_streak_low | 1 | **2**（new_candidates=0<3）|
| rounds_since_last_corpus_discover | 241 | 242 |
| last_updated_round | 305 | 306 |

## 遗留问题

1. **queue(event) 恒 0**：本轮零新候选。registry 不变（event 64、total 1539、unknown 0）。
2. **下轮 R306 = SCN28-zombie（§3(4)）**：since_evv5=6<10；discover_streak_low=2<3；since_discover=0<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4)**。event 二次矿已竭，R306 re-scan 预判续 new_candidates<3、**discover_streak_low 2→3**；R307 则 discover_streak_low=3≥3 → §3(2) **CLOSE+SCN28 触发**，收 event（final_count 64）、切 character（type_queue 末类型）。
3. **event 二次矿竭·type_close 进行中**：单事件作品第二事件矿脉正式判竭（本轮 exhaustive re-scan 零候选）。streak 1→2，再一轮低产即达 type_close_streak=3。**Phase 2.1 迭代末临近**：character 为 type_queue 末类型，其后 type_queue 空 → Phase 2.1 迭代收尾（EVV6 全库评审 + closed_types evv6_score 回填）。
4. **消歧方法论·honest saturation**：本轮严守「非据 queue 推断、须扫全 map」——重建 event→work map、逐 book 复核 PN 覆盖，如实记 new_candidates=0，不强建弱候选。遵 memory 规则「exhaustively re-scan before claiming saturation」。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一（本轮 re-scan 亦确认此债致 SI 误判为独立单事件 book）；（c）「Master of the World」book label 归一（本轮确认 terror-destruction/great-eyrie-investigation 因 label 未归一被误列为二 book）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED，R299 EVV5 记录、零消解。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=241→242（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event type_close 后即须 event EVV6，并处理 13 页 PN 回填债 + 散文门债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
