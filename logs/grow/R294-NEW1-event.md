---
round: 294
date: 2026-07-18
type_round: 60
phase: "2.1"
current_type: event
gene: NEW1
pages: [maston-calculation-error]
result: success
---

# GROW 2.1-B · R294 · NEW1 · event — 建 Maston's Calculation Error（J.T. Maston 漏三零致北极运河巨炮惨败、误反免灾，TT 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 57 建（type_round 60），消费 R293 discover 队列**建序 43**（最小建序）。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Maston's Calculation Error**（TT 第二 event，作品原仅 kilimanjaro-cannon-shot 乞力马扎罗巨炮发射）——*Topsy-Turvy* 之终局揭晓。
Gun Club 欲以巨炮之反冲改地球自转轴、令北极冰域可垦，然一击之后地轴纹丝未动。Barbicane 与 Nicholl 归国追问秘书 J.T. Maston 何以失败；Maston 铁钩按额，唯断炮弹未得预定初速（TT-020-007/017），三度自验之数如石击顶（TT-020-014）。
数日后工程师 Alcide Pierdeux 于 *Times* 撰文揭真相：Maston 取地球周长为算基时，将 40,000,000 米误写作 40,000 米——漏三个零（TT-020-034）。此三零之漏致算式末端生十二个零之变（TT-020-036），故炮击仅移北极三千分之一毫米、抛射体自身成一小行星入太阳系（TT-020-038）。
此疏忽毁此宏图、使 Barbicane & Co. 成举世笑柄（TT-020-031/040），然同一错误反免全球于倾覆之灾，贺电如潮涌至（TT-020-041/042）。
Maston 终忆起疏漏缘由：闭居 Ballistic Cottage、于黑板写 40,000,000 时遭雷击穿电话击倒（TT-020-045），起身重写半抹之数、再度被扰、仅写 40,000 而漏末三零（TT-020-046）。

**锚核（逐句复核，锚无误、framing 准确）**：R293 队列记 pn_anchor=**TT-020**（终局揭晓章「IN WHICH THIS STORY ... IS FINISHED」），framing 为「追问-揭误-溯因-免灾」。
逐句核 TT-020：追问失败（020-007/014/017）、Pierdeux 揭漏三零（020-034）、十二零之变（020-036）、北极仅移三千分之一毫米+抛射体成小行星（020-038）、举世笑柄（020-031/040）、误反免灾贺电如潮（020-041/042）、溯因雷击+电话两度打断（020-045/046）全在 **TT-020**（单章终局）。锚保留 **TT-020**，framing 相符，无需改锚/改 slug。

**单指核**：全 16 distinct PN 单指北极运河巨炮惨败之因揭晓这一连续因果（追问失败→铁钩按额断初速不足→三验如石→Pierdeux 揭漏三零→十二零之变→北极仅移三千分之一毫米→抛射体成小行星→举世笑柄→误反免灾→贺电如潮→Maston 忆起→雷击+电话两度打断漏末三零）。
**排除**：kilimanjaro-cannon-shot（TT-017..019 乞力马扎罗巨炮发射，首 event 已建独立页——分工：发射 vs 失败之因）；磁石物理/弹道长论不逐句展开；TT-020 之前追问前情（背景，仅取结论 007/017）。
exact-slug maston-calculation-error ABSENT（变体 maston-error/the-three-zeros/north-pole-fiasco/topsy-turvy-fiasco 亦 ABSENT）。aliases [The Three Forgotten Zeros, Maston's Miscalculation, The North Pole Fiasco]（避 work 页 aliases「Sans dessus dessous」「The Purchase of the North Pole」，无 label 冲突）。

**VVV 2-char 核**：TT 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：TT 有 work 页 **[[Topsy-Turvy]]**；另链 **[[Gun Club]]**（organization 页，Barbicane/Maston/Nicholl 皆 Gun Club 员）。Alcide Pierdeux/J.T. Maston/Barbicane/Nicholl 无对应页，纯文本叙述（不造死链）。
book='Topsy-Turvy'、location='Baltimore, United States'。

**逾达门 16 distinct solid PN**（TT-020）：TT-020-007/014/017（追问-铁钩-三验）+ TT-020-027/031/034（乏经验-笑柄-漏三零）+ TT-020-036/038/039/040（十二零变-北极三千分之一毫米-Pierdeux 撰文-举世笑柄）+ TT-020-041/042/044（免灾-贺电-Pierdeux 未误）+ TT-020-045/046/047（雷击溯因-再扰漏零-Maston 蒙羞）。

prose-gate：add_page 前 /tmp 初稿 2 段超门（565「Pierdeux 揭漏三零」段 + 439「Maston 忆起溯因」段），edit 前各拆一次（TT-020-034 后、TT-020-045 后断行）后 0 超段；add_page 一次成型（rev M34enS，size 3103）；全段 ≤400。pn_validator --mode strict ✓。

event 计数 56→57，registry total 1531→**1532**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| maston-calculation-error | M34enS | Topsy-Turvy | Baltimore, United States | TT-020 | 16 distinct | 追问-揭误-溯因-免灾单指（TT-020 单章终局）；锚 TT-020 逐句核实、framing 准确；剔 kilimanjaro-cannon-shot(发射 已覆盖)；TT 2-char 无需 Note；避 work 页 aliases「Sans dessus dessous」；链 [[Topsy-Turvy]]+[[Gun Club]] |

- **maston-calculation-error**：16 distinct solid PN（TT-020，惨败之因揭晓）；aliases [The Three Forgotten Zeros, Maston's Miscalculation, The North Pole Fiasco]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指惨败之因揭晓；kilimanjaro-cannon-shot 发射别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 2 段超门（565+439），各拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：16 solid（TT-020），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；TT 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1532 event 57 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug maston-calculation-error ABSENT；变体 ABSENT；aliases 避 work 页 aliases 无 label 冲突。✔
- **单指核**：TT-020 追问-揭误-溯因-免灾因果逐句确认；climax 单章 TT-020 核实；与 kilimanjaro-cannon-shot 分工不重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R295 起始计数）

| 字段 | R294 起始 | R295 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 294 | 295 |
| type_round | 60 | 61 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 230 | 231 |
| last_updated_round | 294 | 295 |

## 遗留问题

1. **event 页数 57**：本轮 +1（TT 第二 event）。queue(event) 3→**2**（建序 43 消费）。registry 全库 **1532**，unknown 0。
2. **下轮 R295 = NEW1（§3(7)）**：since_evv5=6<10；streak=0<3；since_discover=1<10 且全局 queue≥10 → §3(3) 否；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 44 tjon-viaduct-sacrifice（ASC，anchor ASC-025）**。ASC 3-char 正常宽度无需 Note；逐句核 ASC-025 Faruskiar 扳道岔引车趋 Tjon 断桥、Kinko 顶爆锅炉殉难止车、揭 Faruskiar 匪首序列、剔 ki-tsang-train-attack 中途匪劫别线。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 TT-020 锚 + framing 逐句核实均准确，无需改。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略**：单事件作品第二事件矿脉，已建 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/RM/EHLA/AM/**TT** 十三部第二 event；queue 余建序 44(ASC)/45(WC)。余单事件作品 BR(10c)/TN(20c)/PL(9c)/MZ(5c)/WAI(16c)/DOSE(17c)/GM(22c，overlap-watch) 留后续 zombie 批次；DA 单章短篇不可掘第二事件（排除）；MW 实为双 label（HK 待批归一），非单一。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解；本轮页 16 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 2 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=230→231（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
