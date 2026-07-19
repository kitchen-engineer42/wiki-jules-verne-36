---
round: 282
date: 2026-07-18
type_round: 48
phase: "2.1"
current_type: event
gene: NEW1
pages: [drawing-lots-on-the-raft]
result: success
---

# GROW 2.1-B · R282 · NEW1 · event — 建 The Drawing of Lots on the Raft（Chancellor 竹筏抽签食人·Letourneur 父代子死·Amazon 淡水获救，SC2 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 35 建（type_round 48），消费 R280 discover 队列**建序 35**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Drawing of Lots on the Raft**（SC2 第二 event，作品原仅 chancellor-fire=SC2-009）——*The Survivors of the Chancellor* 之高潮。
Chancellor 焚沉后幸存者困竹筏漂大西洋、饥渴仅余十一人；议决抽签食人、约定「末签者为 victim」；M. Letourneur 自愿执抽，
签落其子 Andre（第九签），老父暗撕真末签、以己名顶替；Miss Herbey 恳求延一日；翌晨（1 月 27）临刑之际，
Kazallon 被掷入海反尝出海水为淡——近 Amazon 河口，全筏获救于 Marajo 岛 Cape Magoari，三十二人唯十一生还。

**锚核（逐句复核）**：R280 队列记 pn_anchor=**SC2-053**（抽签章）。逐句核 SC2-050~057（Kazallon 手记日期体，
JANUARY 23rd→27th）：抽签主线在 **SC2-053**（名入帽→Letourneur 执抽→逐名唱→Andre 第九→父代子），
父代子牺牲在 **SC2-054-001**，延刑在 **SC2-054-003/007**，淡水获救在 **SC2-055-020/056-003/056-010**，鲜活分明。
pn_anchor 保持 **SC2-053**。

**单指核**：全 16 distinct PN 单指抽签食人这一连续高潮（十一人→定抽签→执抽→Andre 中签→父顶替→Herbey 延刑→临刑→淡水→获救）。
**排除**：chancellor-fire（SC2-009，已建独立页首事件）；Kazallon 早期漂流铺垫（SC2-051 天热/052 望绝）仅作背景不取为动作 PN；Herbey/Curtis 归宿尾声别线剔除。
exact-slug drawing-lots-on-the-raft ABSENT（变体 raft-of-the-chancellor/chancellor-raft/cannibalism-on-the-chancellor 亦 ABSENT）。aliases [The Raft of the Chancellor, The Chancellor Castaways]（与任何现有 label 无冲突）。**SC2 3-char → 无需 page-top Note**。

**工作页处置**：SC2 有 work 页 **[[The Survivors of the Chancellor]]**；链回之 + [[Amazon]]（place，唯一现存实体链）。Curtis/Herbey/Letourneur/Chancellor/Para/Marajo 无对应页，纯文本叙述（不造死链）。
book=The Survivors of the Chancellor、location=A raft on the Atlantic, off the mouth of the Amazon。

**逾达门 16 distinct solid PN**（跨 SC2-050~057，抽签食人高潮）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SC2-050-001 | 1 月 23 仅余十一人、悲剧将尽（缘起）|
| Overview | SC2-053-001 | 议抽签、各分 victim 之身（定抽签）|
| What Happens | SC2-053-003 | 十一名入帽、末签者为 victim（规则）|
| What Happens | SC2-053-004 | M. Letourneur 自愿执抽（父之牺牲）|
| What Happens | SC2-053-008 | 逐名唱至第九落 Letourneur（唱名）|
| What Happens | SC2-053-010 | 答曰「Andre」（子中签）|
| What Happens | SC2-053-011 | Andre 昏厥、余 Dowlas 与老父二签（顶替伏笔）|
| Significance | SC2-054-001 | 父无余物、以命予子（顶替揭晓）|
| Significance | SC2-054-003 | 屠刀将举、Herbey 上前恳求（延刑）|
| Significance | SC2-054-007 | 「待明晨」boatswain 掷刀（缓刑）|
| Significance | SC2-055-002 | 27 晨海空无帆、临刑绝望（危机）|
| Significance | SC2-055-020 | 掷海反尝海水为淡（转机）|
| Significance | SC2-056-003 | 血未溅、victim 未倒（获救）|
| Significance | SC2-056-010 | 南美近 Amazon、河口淡化二十里海（定位）|
| Participants | SC2-057-007 | 筏泊 Marajo Cape Magoari、渔人送 Para（脱险）|
| Participants | SC2-057-009 | 三十二人唯十一生还（结局）|

**VVV 处置**：SC2 3-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate：add_page 一次成型后，edit_page 首过报 Overview 514/Significance 534 双段 over-400 + Participants bullet 块合并 771 误报；拆两长段 + bullet 间加空行分隔后二过 clean。pn_validator --mode strict ✓。

event 计数 48→49，registry total 1523→**1524**，unknown 恒 0。add_page 建（rev VWtM5c）后 edit_page 拆段（rev jE0hqV，size 3489，
quality 自动 featured）。
location=A raft on the Atlantic, off the mouth of the Amazon、pn_anchor=SC2-053、book=The Survivors of the Chancellor、aliases=[The Raft of the Chancellor, The Chancellor Castaways]。
链 [[The Survivors of the Chancellor]]+[[Amazon]]。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| drawing-lots-on-the-raft | jE0hqV | The Survivors of the Chancellor | A raft on the Atlantic, off the mouth of the Amazon | SC2-053 | 16 distinct | 抽签-父代子-延刑-淡水获救单指（跨 SC2-050~057）；抽签主线 SC2-053 逐句核；剔 chancellor-fire(SC2-009 已覆盖)/漂流铺垫/尾声归宿别线；aliases 无冲突；SC2 3-char 无 Note；链 [[The Survivors of the Chancellor]]+[[Amazon]] |

- **drawing-lots-on-the-raft**：16 distinct solid PN（跨 SC2-050~057，抽签食人高潮）；aliases [The Raft of the Chancellor, The Chancellor Castaways]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指抽签食人；chancellor-fire/漂流铺垫/尾声别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：edit_page 首过 Overview 514/Significance 534 双超 + bullet 合并 771 误报；拆段 + bullet 空行分隔后 0 超段。✔
- **G3 ≥5 distinct PN**：16 solid（跨 SC2-050~057），逾门。✔
- **G4 脚本建页**：add_page.py 建、edit_page.py 改，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；SC2 3-char 无需 Note。✔
- **registry 一致**：total 1524 event 49 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug drawing-lots-on-the-raft ABSENT；变体 ABSENT；aliases 无 label 冲突。✔
- **单指核**：SC2-050~057 抽签食人高潮逐句确认；抽签主线 SC2-053 核实；pn_anchor SC2-053 保持。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R283 起始计数）

| 字段 | R282 起始 | R283 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 282 | 283 |
| type_round | 48 | 49 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 218 | 219 |
| last_updated_round | 282 | 283 |

## 遗留问题

1. **event 页数 49**：本轮 +1（SC2 第二 event）。queue(event) 2→**1**（建序 35 消费，余 36）。registry 全库 **1524**，unknown 0。
2. **下轮 R283 = NEW1（§3(7)）**：since_evv5=5<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=1>0 → NEW1。
   建建序 36 **wreck-of-the-pilgrim**（DSCF，DSCF-014）。**DSCF 4-char → 建时须核 PN 渲染，如断行加 RFC-0003 Note**；建时核搁浅动作序列（DSCF-012/013/014/015/016）单指、剔 whale-hunt-disaster(已覆盖)及 Harris 内陆奴队后续别线；须逐句复核搁浅 PN；链 [[Dick Sand: A Captain at Fifteen]]。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。R278/R279/R281/R282 均逐句核实锚本身无误、择动作/高潮序列句。十二例核实无误（R265/R268-274/R276/R278/R279/R281/**R282**）+ R272 dup 教训。
4. **event 覆盖策略**：R280 discover 队列（建序 34/35/36）余 36。18 单事件作品续为矿脉，后续 zombie 轮续掘。
5. **建序 36 后 queue(event)=0**：R284 = SCN28-zombie discover，须自 18 部单事件作品（AM/ASC/BR/DA/DOSE/EHLA/FC/FWB/GM/MZ/OC/PL/RM/TN/TT/WAI/WC）续掘第二事件。
6. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可补 PN 至 ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一。
7. **event PN 回填债**：13/49 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解；R278/R279/R281/R282 新建页各 ≥10 PN 不入债。
8. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
9. **corpus-discover 顺延**：since_corpus=218→219（dead 变量）。
10. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
11. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
