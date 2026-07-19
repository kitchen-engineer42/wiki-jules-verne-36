---
round: 303
date: 2026-07-19
type_round: 69
phase: "2.1"
current_type: event
gene: NEW1
pages: [rescue-of-carefinotu]
result: success
---

# GROW 2.1-B · R303 · NEW1 · event — 建 The Rescue of Carefinotu（Godfrey 效 Crusoe 救食人生番之俘、枪毙其酋 Tartlet 乱射毙第二番，GM 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 63 建（type_round 69），消费 R302 discover 队列**建序 49**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=1<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**The Rescue of Carefinotu**（GM 第二 event，作品原仅 wreck-of-the-dream 沉船）——*Godfrey Morgan / L'École des Robinsons* 之岛上救番高潮。
食人生番驾 proa 登 Phina 岛（GM-016-031），Godfrey 以望远镜追其转 promontory 过河口（GM-016-036），闭门匿于 Will Tree 度惧夜（GM-016-042）。
黎明侦察，见沙滩篝火（GM-017-051），十番环火驱桩备炙、第十二番缚于桩（GM-017-053/055），备炙食之（Tartlet 早断食人族，GM-017-056）。
Godfrey 效 Defoe 之英雄决意救之（GM-017-059）；酋令三番解俘迫近火，Godfrey 呼喝一枪、酋中弹仆地（GM-017-064/067），执俘之番惊释之（GM-017-068）；Tartlet 闭目乱射竟毙第二番（GM-017-071/072），余番溃逃携伤驾 proa 遁（GM-017-073），Godfrey 不追、俘既获救（GM-017-074）。获救之俘即后名 Carefinotu，成 Godfrey 之伴。

**锚核（逐句复核，锚无误、framing 准确）**：R302 队列记 pn_anchor=**GM-017**（章「IN WHICH PROFESSOR TARTLET'S GUN REALLY DOES MARVELS」），framing 为「登岛-缚俘-备炙-开枪-溃遁-获救」。
逐句核 GM-017（158 段）+ GM-016 设置段（71+ 段）：登岛（GM-016-031/036）、匿 Will Tree（GM-016-042）、沙滩篝火（GM-017-051）、十番驱桩备炙（053）、第十二番缚桩（055）、备炙食（056）、效 Crusoe 决意救（059）、酋令解俘（064）、一枪毙酋（067）、执俘者释之（068）、Tartlet 闭目乱射（071）、第二番仆（072）、余番驾 proa 溃（073）、俘获救（074）——救番 climax 全在 **GM-017** 单章、设置段 GM-016。锚保留 **GM-017**，framing 相符，无需改锚/改 slug。

**单指核**：全 15 distinct PN 单指 Carefinotu 之获救这一登岛-缚俘-开枪-溃遁-获救连续因果。
**排除**：wreck-of-the-dream（首 event，**GM-007/008/022** Dream 号触礁沉没漂岛，PN 区段与本页 GM-016/017 **零重叠**——分工：沉船漂岛 vs 岛上救番）；GM 余段「Phina 岛群兽之谜」（GM-018/019/020 熊-虎-栅栏）判弥散谜团弧、且与 GM-021/022 火灾-揭秘纠缠，**本页不采**，止于救番 GM-017-074、不入群兽线。

exact-slug rescue-of-carefinotu ABSENT（变体 carefinotu-rescue/the-rescue-of-carefinotu 亦 ABSENT）。aliases [Godfrey's Rescue of the Native, Deliverance from the Cannibals, Tartlet's Gun Does Marvels]（避首 event alias「The Foundering of the Dream」及 work 页 aliases「L'École des Robinsons」「The School for Crusoes」「Godfrey Morgan: A Californian Mystery」，无 label 冲突）。

**VVV 2-char 核**：GM 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：GM 有 work 页 **[[Godfrey Morgan]]**；链回之。Godfrey/Tartlet/Carefinotu 无对应页，纯文本叙述（不造死链）。
book='Godfrey Morgan'（对齐首 event wreck-of-the-dream）、location='Phina Island'（与首 event location='Pacific Ocean' 区分）。

**逾达门 15 distinct solid PN**（GM-016/017）：016-031/016-036/016-042/017-051/017-053/017-055/017-056/017-059/017-064/017-067/017-068/017-071/017-072/017-073/017-074。

prose-gate：add_page 前 /tmp 初稿 Overview 段超门（424），删「timorous」「castaway」「faithful」缩至 <400 后 0 超段；add_page 一次成型（rev DKn5jP，size 3214）；全段 ≤400。pn_validator --mode strict ✓。

event 计数 62→63，registry total 1537→**1538**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| rescue-of-carefinotu | DKn5jP | Godfrey Morgan | Phina Island | GM-017 | 15 distinct | 登岛-缚俘-备炙-开枪-溃遁-获救单指（GM-016/017 救番弧）；锚 GM-017 逐句核实、framing 准确；剔 wreck-of-the-dream(GM-007/008/022 沉船 PN 区段零重叠)；止于 GM-017-074 不入群兽谜团线；GM 2-char 无需 Note；避首 event + work aliases；链 [[Godfrey Morgan]] |

- **rescue-of-carefinotu**：15 distinct solid PN（GM-016/017，食人生番之俘获救）；aliases [Godfrey's Rescue of the Native, Deliverance from the Cannibals, Tartlet's Gun Does Marvels]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指登岛-救番因果；wreck-of-the-dream 沉船别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 Overview 超门（424），缩字后 0 超段。✔
- **G3 ≥5 distinct PN**：15 solid（GM-016/017），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；GM 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1538 event 63 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug rescue-of-carefinotu ABSENT；变体 ABSENT；aliases 避首 event（The Foundering of the Dream）+ work 页 aliases 无 label 冲突。✔
- **单指核**：GM-016/017 救番因果逐句确认；止于 GM-017-074；与 wreck-of-the-dream（GM-007/008/022）PN 区段零重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R304 起始计数）

| 字段 | R303 起始 | R304 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 303 | 304 |
| type_round | 69 | 70 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 239 | 240 |
| last_updated_round | 303 | 304 |

## 遗留问题

1. **event 页数 63**：本轮 +1（GM 第二 event）。queue(event) 2→**1**（建序 49 消费，余建序 50 failing-of-the-zacharius-clocks）。registry 全库 **1538**，unknown 0。
2. **下轮 R304 = NEW1（§3(7)）**：since_evv5=4<10；discover_streak_low=1<3；since_discover=1<10 且全局 queue≥10 → §3(3) 否；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 50 failing-of-the-zacharius-clocks（MZ，anchor MZ-002）**。MZ 2-char 无需 Note；逐句核 MZ-002「THE PRIDE OF SCIENCE」众钟尽停 + MZ-001「A WINTER NIGHT」设置段；剔 death-of-master-zacharius（MZ-005 终局殒魂别线，PN 区段零重叠）。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 GM-017 锚 + framing 逐句核实均准确，无需改。**PN 区段防重叠**：同作双 event（救番 GM-016/017 vs 沉船 GM-007/008/022）核 PN 区段零重叠、语义分工清晰。教训延续（R283 改锚 / R286 改锚+改 slug / R301 止段防重叠）。
4. **event 二次矿近竭·type_close 逼近**：单事件作品第二事件已建十九部（…/WAI/TN/PL/GM）。queue 余 MZ 一候选（建序 50）；R304 建后 queue(event)→0，R305=SCN28-zombie re-scan。**event 二次矿将竭**：discover_streak_low 现 1，若 R305/后续 re-scan 续 new_candidates<3（连续三轮低产 streak 达 3）→ CLOSE+SCN28 切 character（type_queue 末类型）。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/63 早期页 <5 PN，DEFERRED，R299 EVV5 记录、零消解；本轮页 15 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 Overview 超门已缩）。
8. **corpus-discover 顺延**：since_corpus=239→240（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时并处理 13 页 PN 回填债 + 散文门债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
