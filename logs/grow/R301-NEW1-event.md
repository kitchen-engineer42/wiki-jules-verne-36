---
round: 301
date: 2026-07-19
type_round: 67
phase: "2.1"
current_type: event
gene: NEW1
pages: [lima-indian-uprising]
result: success
---

# GROW 2.1-B · R301 · NEW1 · event — 建 The Lima Indian Uprising（Sambo 领 Lima 印第安五时警钟怒起、攻总统府中炮溃败，PL 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 62 建（type_round 67），消费 R297 discover 队列**建序 48**（末候选）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=3<10、全局 queue≥10 → §3(3) 否；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**The Lima Indian Uprising**（PL 第二 event，作品原仅 death-of-martin-paz 终局殉死）——*The Pearl of Lima* 之大起义。
印第安/zambo/chiño 潜聚 Lima 富人区（PL-008-003），Sambo 现身斥「西班牙人乃压迫我族者，当诛」（PL-008-008/009），定「五时钟鸣、山间警钟为复仇之号」（PL-008-011），赴 chingana 会起义首领（PL-008-012）。
大教堂钟响五下、警钟雷动（PL-008-014），全城印第安持械怒目而出（PL-008-015），呼「诛西班牙人！诛压迫者！」为号（PL-008-016）；退路尽绝、山巅亦布敌（PL-008-017），Martin Paz 举独立黑旗领一纵队（PL-008-018）。
然政府军早备、列阵总统府前以猛烈排枪迎起义者（PL-008-019），Manangani 跃上首级石阶时敌阵忽启、露双炮待发（PL-008-021）；炮发葡萄弹扫石阶上印第安人（PL-008-028），溃逃如叛、印第安人以为首领弃之，官军追杀无算（PL-008-030）。

**锚核（逐句复核，锚无误、framing 准确）**：R297 队列记 pn_anchor=**PL-008**（章「CONQUERORS AND CONQUERED」），framing 为「潜聚-号令-钟响-怒起-攻府-溃败」。
逐句核 PL-008（58 段）：潜聚富人区（003）、Sambo 现身（008）、斥压迫者当诛（009）、五时警钟号令（011）、赴 chingana 会首领（012）、钟响五下警钟雷动（014）、全城怒起（015）、诛压迫者为号（016）、退路绝（017）、Martin Paz 举黑旗（018）、政府军排枪迎击（019）、双炮露出（021）、葡萄弹扫石阶（028）、溃逃官军追杀（030）——全在 **PL-008** 单章起义弧。锚保留 **PL-008**，framing 相符，无需改锚/改 slug。

**单指核**：全 15 distinct PN 单指 Lima 印第安起义之潜聚-号令-怒起-攻府-溃败这一连续因果。
**排除**：death-of-martin-paz（首 event，**PL-009** Madeira 瀑布 Martin Paz 殉死，PN 区段 PL-009 与本页 PL-008 **零重叠**——分工：起义 vs 终局殉死）；PL-008 后段 Martin Paz 弃战救 Don Vegal（031-038）、杀 André Certa（045-047）、Samuel 收据揭 Sarah 身世（051-053）、Sarah 被劫向 Madeira（056-057）——此为 Martin Paz 个人线与向 PL-009 殉死之过渡，**本页不采**（止于起义溃败 PL-008-030，留 death 别线接续），确保与 death-of-martin-paz 无语义重叠。
exact-slug lima-indian-uprising ABSENT（变体 lima-uprising/indian-uprising-lima/sambo-revolt/lima-indian-revolt/uprising-of-lima 亦 ABSENT）。aliases [The Sambo's Revolt, Death to the Oppressors, The Rising of the Limanian Indians]（避首 event aliases「Martin Paz's Sacrifice」「The Rescue at the Madeira Cataract」及 work 页 aliases「Martin Paz」「Un drame au Mexique」「The Pearl of Lima: A Story of True Love」，无 label 冲突）。

**VVV 2-char 核**：PL 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：PL 有 work 页 **[[The Pearl of Lima]]**；链回之。Sambo/Martin Paz/Manangani/Don Vegal 无对应页，纯文本叙述（不造死链）。
book='The Pearl of Lima'（对齐首 event death-of-martin-paz）、location='Lima, Peru'（与首 event location='Cataracts of the Madeira' 区分）。

**逾达门 15 distinct solid PN**（PL-008）：003/008/009/011/012/013/014/015/016/017/018/019/021/028/030。

prose-gate：add_page 前 /tmp 初稿 1 段超门（钟响-怒起 PL-008-014/015/016 段 402），edit 前拆一次（PL-008-014 后断行）后 0 超段；add_page 一次成型（rev Lae7se，size 3301）；全段 ≤400。pn_validator --mode strict ✓。

event 计数 61→62，registry total 1536→**1537**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| lima-indian-uprising | Lae7se | The Pearl of Lima | Lima, Peru | PL-008 | 15 distinct | 潜聚-号令-怒起-攻府-溃败单指（PL-008 起义弧）；锚 PL-008 逐句核实、framing 准确；剔 death-of-martin-paz(PL-009 殉死 PN 区段零重叠)；止于溃败 PL-008-030 不入 Martin Paz 个人线；PL 2-char 无需 Note；避首 event + work aliases；链 [[The Pearl of Lima]] |

- **lima-indian-uprising**：15 distinct solid PN（PL-008，Sambo 领印第安起义与溃败）；aliases [The Sambo's Revolt, Death to the Oppressors, The Rising of the Limanian Indians]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指起义潜聚-号令-怒起-攻府-溃败；death-of-martin-paz 殉死别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 1 段超门（402），拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：15 solid（PL-008），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；PL 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1537 event 62 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug lima-indian-uprising ABSENT；变体 ABSENT；aliases 避首 event + work 页 aliases 无 label 冲突。✔
- **单指核**：PL-008 起义因果逐句确认；止于 PL-008-030 溃败；与 death-of-martin-paz（PL-009）PN 区段零重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R302 起始计数）

| 字段 | R301 起始 | R302 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 301 | 302 |
| type_round | 67 | 68 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 237 | 238 |
| last_updated_round | 301 | 302 |

## 遗留问题

1. **event 页数 62**：本轮 +1（PL 第二 event）。queue(event) 1→**0**（建序 48 消费，R297 discover 队列全清）。registry 全库 **1537**，unknown 0。
2. **下轮 R302 = SCN28-zombie（§3(4)）**：since_evv5=2<10；streak=0<3；since_discover=4<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**。续「单事件作品掘第二事件」策略：re-scan 余单事件作品薄矿——**MZ（Master Zacharius，5c）早段「钟停」候补**、**GM（Mistress Branican，22c）overlap-watch**（首 event wreck-of-the-dream 已引 GM-022-022 终章，掘第二须慎防重叠）。BR/DOSE 判饱和（剔）；DA 单章不可掘；SI/MI 非单事件。**若 re-scan 得 new_candidates<3 → discover_streak_low +1**，连续三轮低产则 R30x = CLOSE+SCN28 切 character。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 PL-008 锚 + framing 逐句核实均准确，无需改。**PN 区段防重叠教训**：同作双 event（起义 PL-008 vs 殉死 PL-009）须核 PN 区段零重叠、语义分工清晰（本轮止于 PL-008-030、不入 Martin Paz 个人过渡线）。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略·余矿近竭**：单事件作品第二事件矿脉已建十八部（…/TT/ASC/WC/WAI/TN/PL），R297 批 WAI/TN/PL 三候选全消费。余可掘极薄：MZ 早段/GM(overlap-watch) 留 R302 zombie re-scan；BR/DOSE 饱和；DA/SI/MI 排除。**event 二次矿将近竭，type_close 判据渐近**（连续 discover new_candidates<3 三轮则 CLOSE+SCN28 切 character，type_queue=[character] 为末类型）。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/62 早期页 <5 PN，DEFERRED，R299 EVV5 记录、零消解；本轮页 15 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 1 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=237→238（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债 + 散文门债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
