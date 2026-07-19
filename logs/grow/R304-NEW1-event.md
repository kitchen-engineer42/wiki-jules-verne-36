---
round: 304
date: 2026-07-19
type_round: 70
phase: "2.1"
current_type: event
gene: NEW1
pages: [failing-of-the-zacharius-clocks]
result: success
---

# GROW 2.1-B · R304 · NEW1 · event — 建 The Failing of the Zacharius Clocks（Geneva 钟表匠 Zacharius 众钟无端尽停、科学之骄拒信其艺可败，MZ 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 64 建（type_round 70），消费 R302 discover 队列**建序 50**（末候选）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=1<3 → §3(2) 否；since_discover=1<10、全局 queue≥10 → §3(3) 否；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**The Failing of the Zacharius Clocks**（MZ 第二 event，作品原仅 death-of-master-zacharius 终局殒魂）——*Master Zacharius / Maître Zacharius* 之开篇奇变。
Geneva 第一钟表匠 Zacharius 数日忧郁失常、怀不明之秘（MZ-001-005/014），徒 Aubert 诉「有绝不可解之事发生」（MZ-001-029）；冬夜老人立于室中、以空洞之声呼「是死！」（MZ-001-046/047）。
众表无端尽停确凿（MZ-002-003）；翌晨 Zacharius 强作信心复工、自称头痛已为日光驱散（MZ-002-004/005）。
Aubert 诫「科学之骄已附汝身」，Zacharius 闻言暴怒（MZ-002-008/009）；老人（曾以发明擒纵机构 escapement 拔钟表艺于草昧）自称已注己之魂于每一机械、问 Aubert 可曾视之为狂人（MZ-002-025/020）；傲然自恃、信已得存在之秘（MZ-002-022）。女 Gerande 之惧旋验：老仆 Scholastique 又送回一停之「妖表」（MZ-002-040），Aubert 谨为之上弦而表终不行（MZ-002-043）。

**锚核（逐句复核，锚无误、framing 准确）**：R302 队列记 pn_anchor=**MZ-002**（章「THE PRIDE OF SCIENCE」），framing 为「钟停-复工-傲称-祈祷」。
逐句核 MZ-002（107 段）+ MZ-001 设置段（148 段）：忧郁失常（MZ-001-005/014）、Aubert 诉异（029）、夜半立室呼「是死」（046/047）、众表尽停（MZ-002-003）、复工强作信心（004/005）、诫科学之骄（008/009）、发明擒纵机构（025）、问可曾视为狂人（020）、傲然信得存在之秘（022）、Scholastique 又送妖表（040）、上弦而表不行（043）——钟停开篇奇变全在 **MZ-002** 主章 + MZ-001 设置。锚保留 **MZ-002**，framing 相符，无需改锚/改 slug。

**单指核**：全 16 distinct PN 单指众钟尽停之开篇奇变与科学之骄这一连续因果。
**排除**：death-of-master-zacharius（首 event，**MZ-005** Andernatt 堡 Zacharius 殒命、魔鬼 Pittonaccio 收魂，PN 区段 MZ-005 与本页 MZ-001/002 **零重叠**——分工：开篇钟停 vs 终局殒魂）；MZ-002 后段 Zacharius 昏厥（033-037）、逐向 Andernatt 追魂之过渡（本页止于钟停 MZ-002-043、不入向 MZ-005 殒魂之追魂线）。

exact-slug failing-of-the-zacharius-clocks ABSENT（变体 stopping-of-the-zacharius-clocks/zacharius-clocks-fail/pride-of-science 亦 ABSENT）。aliases [The Stopping of the Clocks, The Pride of Science, Zacharius's Failing Watches]（避首 event aliases「The Damnation of Master Zacharius」「The Bursting of the Last Clock」及 work 页 aliases「Maître Zacharius」「Master Zacharius, or the Clockmaker Who Lost His Soul」「The Clockmaker Who Lost His Soul」，无 label 冲突）。

**VVV 2-char 核**：MZ 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：MZ 有 work 页 **[[Master Zacharius]]**；链回之。Zacharius/Aubert/Gerande/Scholastique 无对应页，纯文本叙述（不造死链）。
book='Master Zacharius'（对齐首 event death-of-master-zacharius）、location='Geneva'（与首 event location='Château of Andernatt' 区分）。

**逾达门 16 distinct solid PN**（MZ-001/002）：001-005/001-014/001-029/001-036/001-046/001-047/002-003/002-004/002-005/002-008/002-009/002-020/002-022/002-025/002-040/002-043。

prose-gate：add_page 前 /tmp 初稿 What Happens 首段超门（420），MZ-001-029 后断行拆一次后 0 超段；add_page 一次成型（rev Fj9m9S，size 2788）。**pn_validator 警**：Participants 首 bullet MZ-002-003 引文用「timepiece mysteriously stops」与原文「watches...suddenly stopped...apparent reason」关键词重叠 0%，strict 报问题 → edit_page 改引文为「whose watches have suddenly stopped without any apparent reason」对齐原文关键词（rev 3STsVy，size 2793），strict ✓。全段 ≤400。

event 计数 63→64，registry total 1538→**1539**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| failing-of-the-zacharius-clocks | 3STsVy | Master Zacharius | Geneva | MZ-002 | 16 distinct | 钟停-复工-傲称-祈祷单指（MZ-001/002 开篇奇变）；锚 MZ-002 逐句核实、framing 准确；剔 death-of-master-zacharius(MZ-005 殒魂 PN 区段零重叠)；止于 MZ-002-043 不入追魂线；MZ 2-char 无需 Note；避首 event + work aliases；MZ-002-003 引文 edit 对齐关键词；链 [[Master Zacharius]] |

- **failing-of-the-zacharius-clocks**：16 distinct solid PN（MZ-001/002，众钟尽停之开篇奇变）；aliases [The Stopping of the Clocks, The Pride of Science, Zacharius's Failing Watches]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指众钟尽停-科学之骄因果；death-of-master-zacharius 殒魂别线剔除；MZ-002-003 引文 edit 对齐后 strict ✓。✔
- **G2 段落 ≤400 字**：初稿 1 段超门（420），拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：16 solid（MZ-001/002），逾门。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 改引文，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；MZ 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1539 event 64 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug failing-of-the-zacharius-clocks ABSENT；变体 ABSENT；aliases 避首 event + work 页 aliases 无 label 冲突。✔
- **单指核**：MZ-001/002 钟停因果逐句确认；止于 MZ-002-043；与 death-of-master-zacharius（MZ-005）PN 区段零重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R305 起始计数）

| 字段 | R304 起始 | R305 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 304 | 305 |
| type_round | 70 | 71 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 240 | 241 |
| last_updated_round | 304 | 305 |

## 遗留问题

1. **event 页数 64**：本轮 +1（MZ 第二 event）。queue(event) 1→**0**（建序 50 消费，R302 discover 队列全清）。registry 全库 **1539**，unknown 0。
2. **下轮 R305 = SCN28-zombie（§3(4)）**：since_evv5=5<10；discover_streak_low=1<3；since_discover=2<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**。event 二次矿 R302 re-scan 已仅余 GM/MZ 二候选（均本批 R303/R304 建），**R305 re-scan 预计 new_candidates<3**（余单事件作品 BR/DOSE 饱和、DA/SI 排除、GM 群兽弧弥散不采、MZ 已双 event）→ discover_streak_low 1→2。若 R305 及后续续低产（streak 达 3）→ CLOSE+SCN28 切 character（type_queue 末类型）。
3. **消歧方法论·framing 核实 + 引文关键词**：queue 锚点与 framing 均视为线索非定论。本轮 MZ-002 锚 + framing 逐句核实均准确。**引文关键词教训**：Participants bullet 若过度改写原文（timepiece vs watches）致 strict 关键词重叠 0%，须 edit 对齐原文用词——建页后必跑 pn_validator --mode strict，warn 亦须消解。
4. **event 二次矿竭·type_close 临近**：单事件作品第二事件已建二十部（…/PL/GM/MZ）。**余无干净离散第二事件可掘**：BR/DOSE 饱和、DA 单章、SI=MI 第四事件、GM 群兽弧弥散、WAI/TN/PL/GM/MZ 皆已双 event。R305 zombie re-scan 预判 new_candidates<3、streak 1→2；再一轮低产则 streak 达 3 → CLOSE+SCN28 收 event 切 character（末类型、type_queue 空后 Phase 2.1 迭代末）。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED，R299 EVV5 记录、零消解；本轮页 16 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 1 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=240→241（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时并处理 13 页 PN 回填债 + 散文门债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
