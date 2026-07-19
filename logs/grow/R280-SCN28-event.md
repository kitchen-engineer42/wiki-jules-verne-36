---
round: 280
date: 2026-07-18
type_round: 46
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R280 · SCN28-zombie · event — 队列耗尽再勘探，掘 3 单事件作品之第二事件（建序 34-36）

## 执行摘要

Phase 2.1-B event 类型**第五次 discover**（type_round 46）。R279 NEW1 消费建序 33 后 queue(event)=0，
R280-start 决策机 §3 首匹配 **SCN28-zombie**（§3(4)：since_evv5=2<10 → 非 §3(1)；streak=0<3 → 非 §3(2)；
since_discover=2<10 且全局 queue≥10 → 非 §3(3)；**queue(event)==0 → §3(4) 触发**）。

SCN28 为**勘探轮，非建页**：扫描语料寻 event 新候选，写入 queue.md，更新计数（since_discover reset）。**pages: []，registry 恒 1522，event 恒 47，unknown 0。**

## 勘探策略（续 R275）

零 event 作品池已穷尽（R275 确认：SI≈MI 同作别译已覆盖、VB=DA 同故事、AMB/YEAR 非叙事散文）。
续行「**单事件作品掘第二事件**」策略——R276/R278/R279 已从 RC/MW/MS 各掘第二 event 成功建页（wreck-of-the-albatross/great-eyrie-investigation/assault-on-irkutsk）。
本轮脚本化统计全 47 event 页 pn_anchor VVV 分布：**21 部作品现仅 1 event**（AM/ASC/BR/DA/DOSE/DSCF/EHLA/FC/FF/FWB/GM/MZ/OC/PL/RM/SC2/SI/TN/TT/WAI/WC），
为第二事件矿脉。本轮择其三富矿（FF/SC2/DSCF）逐章勘探，各掘一离散第二事件。

## 勘探结果（建序 34-36，queue(event) 0→3）

| 建序 | slug | 作品(VVV) | pn_anchor | 事件 | 预估 PN |
|------|------|-----------|-----------|------|---------|
| 34 | destruction-of-back-cup | Facing the Flag (FF) | FF-018 | 五国舰队炮击 Back Cup、fulgurator 击沉首舰、Tonnant 升三色旗、Roch 面旗不忍施射、全岛爆炸夷焦礁、唯 Simon Hart 生还 | ≥9（FF-018-008/009/011/016/018/019/020/024/025/026）|
| 35 | drawing-lots-on-the-raft | The Survivors of the Chancellor (SC2) | SC2-053 | Chancellor 沉后幸存者困竹筏漂大西洋、饥渴仅余十一人、抽签食人、签落 Letourneur、临刑获救于 Amazon 河口 | ≥8（SC2-050~057 序列）|
| 36 | wreck-of-the-pilgrim | Dick Sand: A Captain at Fifteen (DSCF) | DSCF-014 | Dick Sand 误信 Negoro 篡改罗盘、飓风后将 Pilgrim 搁浅安哥拉海岸、众登岸落入 Harris/Negoro 奴贩之谋 | ≥5（DSCF-012/013/014/015/016，建时须核搁浅动作序列）|

**各候选查重**（filesystem exact-slug + 变体，全 ABSENT）：
- destruction-of-back-cup（+ fall-of-back-cup/back-cup-destruction）ABSENT；**facing-the-flag 为 work 页非 event**，勿用「Facing the Flag」作 alias（与 work label 冲突）。
- drawing-lots-on-the-raft（+ raft-of-the-chancellor/chancellor-raft/cannibalism-on-the-chancellor）ABSENT。
- wreck-of-the-pilgrim（+ grounding-of-the-pilgrim/pilgrim-shipwreck/dick-sand-shipwreck）ABSENT。

**建时注意**：
- FF 2-char / SC2 3-char 无需 RFC-0003 Note；**DSCF 4-char → 建时须核 PN 渲染，如断行加 Note**。
- 三锚均为线索非定论，建时逐句复核（尤 DSCF-014 搁浅、SC2-053 抽签、FF-017 结尾「面旗」高潮 PN 归属）。
- 单指核：各剔已覆盖首事件别线（FF abduction-of-thomas-roch、SC2 chancellor-fire、DSCF whale-hunt-disaster）及后续别事件（DSCF Harris 内陆奴队）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)=0** | **触发** |
| 5–7 | RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 SCN28 勘探，无建页、无改页。产出 3 候选写入 queue.md（建序 34-36）。

## EXIT-GATE 检查（SCN28 轮）

- **G1–G4**：无建页/改页，N/A（勘探轮）。
- **registry 一致**：total 1522 event 47 unknown 0 恒定（无写页）。✔
- **勘探充分**：全 47 页 VVV 分布脚本化统计；21 单事件作品识别；三候选逐章勘探、查重、预估 PN。✔
- **new_candidates=3 ≥ type_close_new_candidate_min(3)** → productive，discover_streak_low 保持 0（非 low-yield）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean（本轮仅 state+log+queue）。✔

## 六步状态机（SCN28，grow_state 存 R281 起始计数）

| 字段 | R280 起始 | R281 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 280 | 281 |
| type_round | 46 | 47 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 2 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 216 | 217 |
| last_updated_round | 280 | 281 |

## 遗留问题

1. **event 页数 47**（勘探轮无建页）。queue(event)=**3**（建序 34/35/36 seeded）。registry 全库 1522，unknown 0。
2. **下轮 R281 = NEW1（event）**：since_evv5=3<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(7) NEW1。
   建建序 34 **destruction-of-back-cup**（FF，FF-018）。FF 2-char 无需 Note；建时核炮击-火焚-认旗-爆岛单指、剔 abduction 别线、复核 FF-017「面旗」高潮 PN；链 [[Facing the Flag]]（勿用同名 alias）。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。R278/R279 均遇 queue 候选偏铺垫、改采动作序列句，锚本身无误。本轮三锚同须建时逐句核。
4. **event 覆盖策略**：21 单事件作品为第二事件矿脉；本轮采 FF/SC2/DSCF 三部。余 18 部（AM/ASC/BR/DA/DOSE/EHLA/FC/FWB/GM/MZ/OC/PL/RM/TN/TT/WAI/WC 等）留后续 zombie 轮续掘。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可补 PN 至 ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债**：13/47 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=216→217（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
