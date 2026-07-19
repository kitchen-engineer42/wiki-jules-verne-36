---
round: 302
date: 2026-07-19
type_round: 68
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R302 · SCN28-zombie · event — 单事件作品第二事件 re-scan，掘 2 候选（GM 救番 / MZ 钟停），new_candidates=2 低产、discover_streak_low 0→1

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 68）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；since_discover=4<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**）。

R297 批建序 46-48（return-of-the-jeune-hardie / return-of-ole-kamp / lima-indian-uprising）已于 R298/R300/R301 全消费，queue(event) 归 0，触发 zombie re-scan。

**re-scan 结论（exhaustive，遵「claiming saturation 前须扫全语料」memory 规则）**：单事件作品掘第二事件矿脉已建十八部。本轮全量复扫余单事件作品，仅得 **2** 离散第二事件候选（< type_close_new_candidate_min=3，判**低产**）：

| 建序 | slug | VVV | anchor | 第二事件 | 与首事件分工（PN 区段零重叠）|
|------|------|-----|--------|---------|------------------------------|
| 49 | rescue-of-carefinotu | GM | GM-017 | Godfrey 救番高潮（食人生番登岛缚俘将炙、Godfrey 效 Crusoe 枪毙其酋 + Tartlet 乱射毙第二番、余番驾 proa 溃遁、俘即 Carefinotu 获救）| 首 wreck-of-the-dream(GM-007/008/022 沉船漂岛)｜救番 GM-017 零重叠 |
| 50 | failing-of-the-zacharius-clocks | MZ | MZ-002 | 钟表尽停开篇奇变（Zacharius 所制众钟一夜无端尽停、Aubert 诫「科学之骄」、Faust 式殒灭之始）| 首 death-of-master-zacharius(MZ-005 Andernatt 堡殒魂)｜钟停 MZ-001/002 零重叠 |

**排除记录（re-scan 覆盖）**：
- **GM 余段「Phina 岛群兽之谜」**（GM-018/019/020 熊-虎-栅栏）：判为**弥散谜团弧**（非单一离散事件），且与 GM-021/022 火灾-揭秘及首事件已引 GM-022-022 纠缠 → **不采**（不为凑数强建弱候选，遵「honest saturation」原则）。
- **BR（charleston-blockade-run）**：饱和（首事件已引 BR-001/006/007/009 全连续情节含逃逸高潮）。
- **DOSE（quiquendone-frenzy）**：饱和（首事件已引 DOSE-013-017 含爆炸-揭秘双 climax）。
- **DA**：单章短篇，不可掘第二离散事件。
- **SI**：=MI 第四事件，MI 另有三事件，排除。

**逐句核实（R286 anchor-as-clue 教训）**：
- **GM-017**（158 句）：核实 051 沙滩篝火十番环之 / 055 第十二番缚桩 / 056 备炙食（Tartlet 早断食人族）/ 059 Godfrey 效 Crusoe 决意救 / 067 一枪毙酋 / 071 Tartlet 闭目乱射 / 072 第二番仆 / 073 余番驾 proa 溃遁 / 074 俘获救——救番 climax 逐句确认。GM-016 为登岛设置段（生番驾 proa 潜聚）。
- **MZ-002**（107 句）：核实 003 众表无端尽停 / 004 翌晨复工强作信心 / 005 头痛已为日光驱散 / 008 Aubert 诫「科学之骄已附汝身」。MZ-001（148 句）为冬夜设置段（036 祈神赋表以生命 / 046-047 Zacharius 夜半立室呼「是死！」）。二章合凑 ≥5 distinct PN 可达。

**dup-check**：exact-slug + 变体全 filesystem ABSENT（详 queue 块）。work 页 aliases（GM/MZ）+ 首事件 aliases（wreck: The Foundering of the Dream；death: The Damnation of Master Zacharius / The Bursting of the Last Clock）sweep 无冲突。

**VVV 宽度**：GM/MZ 均 2-char，正常宽度，无需 RFC-0003 Note。

**低产判定**：new_candidates=2 < type_close_new_candidate_min(3) → **discover_streak_low 0→1**。event 二次矿近竭，续二轮 discover 仍 <3（连续三轮低产）则 streak 达 3 → R30x CLOSE+SCN28 切 character（type_queue 末类型）。

本轮 discover 轮，不建页（pages: []）。registry 不变（event 62、total 1537、unknown 0）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| — | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 discover 轮，无建页/编辑。仅 seed queue（建序 49-50）+ 更新 grow_state + 写日志。

## EXIT-GATE 检查

- **G1–G3、schema**：discover 轮不建页，N/A。✔
- **G4 脚本建页**：本轮不建页，无 Write/Edit 于 pages/**。✔
- **registry 一致**：不变（total 1537 event 62 unknown 0）；build_registry 未跑（无页变动）。✔
- **查重充分**：建序 49-50 exact-slug + 变体全 ABSENT；work 页 + 首事件 aliases 无冲突。✔
- **re-scan 充分性**：全量复扫余单事件作品（GM/MZ/BR/DOSE/DA/SI），排除记录完整；GM 群兽谜团弧判弥散不采（不凑数）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie，grow_state 存 R303 起始计数）

| 字段 | R302 起始 | R303 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 302 | 303 |
| type_round | 68 | 69 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 4 | **0**（SCN28 重置）|
| discover_streak_low | 0 | **1**（new_candidates=2<3）|
| rounds_since_last_corpus_discover | 238 | 239 |
| last_updated_round | 302 | 303 |

## 遗留问题

1. **queue(event) 0→2**：本轮 seed 建序 49-50（rescue-of-carefinotu / failing-of-the-zacharius-clocks）。registry 不变（event 62、total 1537、unknown 0）。
2. **下轮 R303 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=1<3；since_discover=0<10 且全局 queue≥10 → §3(3) 否；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 49 rescue-of-carefinotu（GM，anchor GM-017）**。GM 2-char 无需 Note；逐句核 GM-017 救番 climax（+GM-016 登岛设置段）；剔 wreck-of-the-dream（GM-007/008/022 沉船别线）。
3. **event 二次矿近竭·type_close 逼近**：单事件作品第二事件已建十八部，本轮 re-scan 仅余 GM/MZ 二候选（<3 低产），discover_streak_low 0→1。GM 群兽谜团弧判弥散不采。**续策**：R303/R304 建 GM/MZ 二候选耗尽 queue(event) → R305 再 zombie re-scan；若 new_candidates 续 <3（连续三轮低产 streak 达 3）→ CLOSE+SCN28 切 character（末类型）。
4. **消歧方法论·honest saturation**：本轮严守「不为凑 3 强建弱候选」——GM 群兽弧虽可勉强成页，但属弥散谜团且与终章纠缠，判不采，如实记 new_candidates=2。遵 memory 规则「exhaustively re-scan before claiming saturation」+「不凑数」。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/62 早期页 <5 PN，DEFERRED，R299 EVV5 记录、零消解。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=238→239（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时并处理 13 页 PN 回填债 + 散文门债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
