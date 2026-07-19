---
round: 298
date: 2026-07-19
type_round: 64
phase: "2.1"
current_type: event
gene: NEW1
pages: [return-of-the-jeune-hardie]
result: success
---

# GROW 2.1-B · R298 · NEW1 · event — 建 The Return of the Jeune-Hardie（越冬之末叛平-父殁-春归-返航 Dunkirk 成婚，WAI 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 60 建（type_round 64），消费 R297 discover 队列**建序 46**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**The Return of the Jeune-Hardie**（WAI 第二 event，作品原仅 finding-of-louis-cornbutte 寻获）——*A Winter Amid the Ice* 之终局返航。
Vasling 叛变已平（Herming 重伤被舁 WAI-016-002），然更大不幸降临 Louis Cornbutte——其父 Jean Cornbutte 忧劳成疾、终不复生（WAI-016-003）。
Louis 与 Marie 悲跪床畔为 Jean 之魂祈祷，Vasling/Aupic/Jocki 之尸掷入冰岸掘穴、Herming 夜殁无悔随葬（WAI-016-004）。
Jean Cornbutte 葬于冰岸高地、水手立木十字为记（WAI-016-006）；此后众人历诸苦，赖所觅柠檬愈坏血病（WAI-016-007）。
寒冱至日归乃解（WAI-016-005），二月狂飙暴雪后暖至（WAI-016-010），船之护板/舱壁/桥板皆已焚作燃料、越冬当止（WAI-016-011）。
春分后日恒悬空、八月长昼作用于冰（WAI-016-012），四月初船复自然吃水线（WAI-016-013），四月雨催冰解（WAI-016-014）。
4 月 25 日整船待发、帆具完好如初（WAI-016-017），五月融雪（WAI-016-018），二十里外冰群漂向大西洋、水道启（WAI-016-019）。
5 月 21 日 Louis 别父墓启程、历月险途冰山以火药炸开（WAI-016-020），Jeune-Hardie 号于 Jan Mayen 岛外破冰、月余出极海（WAI-016-021）。
8 月 16 日望见 Dunkirk，举城涌至码头、水手拥于亲友之怀，老神父迎 Louis 与 Marie、翌日诵二弥撒——一为 Jean Cornbutte 之魂、一为 Louis 与 Marie 之婚（WAI-016-022）。

**锚核（逐句复核，锚无误、framing 准确）**：R297 队列记 pn_anchor=**WAI-016**（终局章「越冬之末」），framing 为「叛平-父殁-春归-返航-成婚」。
逐句核 WAI-016（76 sid）：Herming 舁（002）、Jean 殁（003）、叛党葬（004）、Jean 立十字（006）、柠檬愈坏血（007）、寒待日归（005）、二月暴雪后暖（010）、焚船越冬当止（011）、八月长昼（012）、四月复吃水线（013）、四月雨解冰（014）、4 月 25 整船（017）、五月融雪（018）、冰群漂大西洋水道启（019）、5 月 21 别父墓启程炸冰山（020）、Jan Mayen 破冰月余出极海（021）、8 月 16 望 Dunkirk 众迎二弥撒（022）——全在 **WAI-016** 单章终局连贯。锚保留 **WAI-016**，framing 相符，无需改锚/改 slug。

**单指核**：全 17 distinct PN 单指越冬之末 Jean Cornbutte 之死与 Jeune-Hardie 返航成婚这一连续因果（叛平善后→父殁→立十字→柠檬愈病→待春→冰解→整船→别墓启程→破冰→返 Dunkirk→二弥撒）。
**排除**：finding-of-louis-cornbutte（WAI-012 Shannon Island 寻获 Louis，首 event 已建独立页——分工：寻获 vs 终局返航）；WAI-016 早段冬猎/融冰技术细节（009 水鸟、015/016 冰裂海豹，背景仅取结论不逐句展开）。
exact-slug return-of-the-jeune-hardie ABSENT（变体 jeune-hardie-return/return-to-dunkirk/deliverance-of-louis-cornbutte/death-of-jean-cornbutte/spring-deliverance/jeune-hardie-homecoming 亦 ABSENT）。aliases [The Deliverance of Louis Cornbutte, The Death of Jean Cornbutte, Homecoming to Dunkirk]（避 work 页 aliases 及首 event alias「The Rescue at Shannon Island」「The Finding of the Jeune-Hardie Castaways」，无 label 冲突）。

**VVV 3-char 核**：WAI 为 3-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：WAI 有 work 页 **[[A Winter Amid the Ice]]**；链回之。Louis/Marie/Jean Cornbutte/Penellan/Vasling 无对应页，纯文本叙述（不造死链）。
book='A Winter Amid the Ice'、location='The Polar Sea and Dunkirk, France'（与首 event location='Shannon Island' 区分）。

**逾达门 17 distinct solid PN**（WAI-016）：002/003/004/005/006/007/010/011/012/013/014/017/018/019/020/021/022。

prose-gate：add_page 前 /tmp 初稿 Overview 段 419 超门，edit 前删「old」冗字缩至 <400 后 0 超段；add_page 一次成型（rev vbsfdm，size 4055）；全段 ≤400。pn_validator --mode strict ✓。

event 计数 59→60，registry total 1534→**1535**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| return-of-the-jeune-hardie | vbsfdm | A Winter Amid the Ice | The Polar Sea and Dunkirk, France | WAI-016 | 17 distinct | 叛平-父殁-春归-返航-成婚单指（WAI-016 终局单章）；锚 WAI-016 逐句核实、framing 准确；剔 finding-of-louis-cornbutte(寻获 已覆盖)；WAI 3-char 无需 Note；避 work 页 aliases + 首 event aliases；链 [[A Winter Amid the Ice]] |

- **return-of-the-jeune-hardie**：17 distinct solid PN（WAI-016，越冬之末与返航成婚）；aliases [The Deliverance of Louis Cornbutte, The Death of Jean Cornbutte, Homecoming to Dunkirk]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指越冬之末-返航成婚；finding-of-louis-cornbutte 寻获别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 Overview 419 超门，删冗字后 0 超段。✔
- **G3 ≥5 distinct PN**：17 solid（WAI-016），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；WAI 3-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1535 event 60 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug return-of-the-jeune-hardie ABSENT；变体 ABSENT；aliases 避 work 页 aliases 及首 event aliases 无 label 冲突。✔
- **单指核**：WAI-016 叛平-父殁-春归-返航-成婚因果逐句确认；终局单章核实；与 finding-of-louis-cornbutte 分工不重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R299 起始计数）

| 字段 | R298 起始 | R299 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 298 | 299 |
| type_round | 64 | 65 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 234 | 235 |
| last_updated_round | 298 | 299 |

## 遗留问题

1. **event 页数 60**：本轮 +1（WAI 第二 event）。queue(event) 3→**2**（建序 46 消费，余建序 47/48）。registry 全库 **1535**，unknown 0。
2. **下轮 R299 = EVV5（§3(1b)）**：since_evv5 R299 起 **=10≥10 → §3(1b) EVV5 触发**（since_discover=1<10 → §3(1a) EVV5+SCN28 不触发，走纯 §3(1b) EVV5）。R299 须执行 event 类型全库抽检 + 模板校准 + PN 回填债评审（13/53 早期页 <5 PN），**不建页**；EVV5 后 since_evv5 归 0。建序 47/48 顺延至 R300 起 NEW1 消费。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 WAI-016 锚 + framing 逐句核实均准确，无需改。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略**：单事件作品第二事件矿脉，已建 …/TT/ASC/WC/**WAI** 十六部第二 event，R297 批 WAI/TN/PL 三候选（WAI 本轮消费，TN/PL 留 R300+）。余单事件作品 TN(20c)/PL(9c) queue 待建；MZ(5c)/GM(22c overlap-watch) 薄矿留察；BR/DOSE 判饱和（剔）；DA 单章不可掘；SI/MI 非单事件。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解；R299 EVV5 须评审。本轮页 17 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 Overview 已缩）。
8. **corpus-discover 顺延**：since_corpus=234→235（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
