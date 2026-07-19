---
round: 292
date: 2026-07-18
type_round: 58
phase: "2.1"
current_type: event
gene: NEW1
pages: [the-ice-sphinx]
result: success
---

# GROW 2.1-B · R292 · NEW1 · event — 建 The Ice Sphinx（Paracuta 驶入磁石怪域、悟 Antarctic Sphinx 乃巨型天然磁石、Dirk Peters 于其基觅得 Arthur Pym 干尸恸绝而亡，AM 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 56 建（type_round 58），消费 R289 discover 队列**建序 42**（末候选）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；streak=0<3；since_discover=2<10、全局 queue≥10 → §3(3) 否；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Ice Sphinx**（AM 第二 event，作品原仅 halbrane-wreck 冰崩毁 Halbrane 号）——*An Antarctic Mystery* 之终局。
Paracuta 小艇北返途中驶入怪域，舟速无风自增；Halbrane 号抓钩忽自舷孔飞出如被不可抗之力牵曳、缆绳崩断，抓钩激射向一 sphinx 状巨丘；
舟上一切铁器（炊具、兵刃、被夺出袋之刀）悉数同向飞去、小艇撞滩；岸上见 Hearne 所窃之艇尽毁、铁件连舵铰皆失，旁陈三尸（Hearne、Martin Holt、一 Falklands 水手）；
近丘 narrator 顿悟——「一块磁石！」Antarctic Sphinx 实为巨型天然磁石，撕铁如弹、任何铁造船只近之必毁；
Dirk Peters（自离觅 Pym 处即缄默）身向 sphinx 倾如被吸，于怪物右爪后觅得一半裸干尸、锈枪缚其身；呼「Pym——我可怜的 Pym！」，欲起吻尸而膝软、faithful heart 碎、倒毙；真相自明：Pym 分离后亦漂入怪域、为磁流所擒掷于石壁。

**锚核（逐句复核，锚无误、framing 准确）**：R289 队列记 pn_anchor=**AM-025**（磁 Sphinx 揭晓高潮章），framing 为「撕铁-悟磁-觅尸-恸亡」。
逐句核 AM-025：舟入怪域铁器被撕（025-032/034/035）、艇毁铁失三尸（025-038~043）、悟磁石（025-054/056/075）、Peters 觅尸恸亡（025-072/082/084/085/086）、Pym 之命（025-087/088）全在 **AM-025**（单章高潮）。锚保留 **AM-025**，framing 相符，无需改锚/改 slug。

**单指核**：全 16 distinct PN 单指冰之 Sphinx 揭晓这一连续因果（抓钩飞脱→铁器尽撕→艇毁铁失→三尸→悟磁石→撕铁毁船→物附石壁→Peters 身倾如吸→觅半裸尸+锈枪→「我可怜的 Pym」→心碎倒毙→Pym 为磁流所擒→葬 Peters 于 Pym 侧）。
**排除**：halbrane-wreck（AM-018..020 冰崩毁 Halbrane 号，首 event 已建独立页）；AM-024 Paracuta 逃生/William Guy 十一年流亡回溯（背景支线，剔）；磁石物理成因长论（025-057~065 电流成磁之科学推演，仅取结论 056/075 不逐句展开）；AM-026 离 Sphinx 之地北返后续（结局别线，剔）。
exact-slug the-ice-sphinx ABSENT（变体 ice-sphinx/magnetic-sphinx/antarctic-sphinx/fate-of-arthur-pym/death-of-dirk-peters/sphinx-of-the-ice 亦 ABSENT）。aliases [The Magnetic Sphinx, Fate of Arthur Pym, Death of Dirk Peters]（**避 work 页 alias「The Sphinx of the Ice Fields」「Le Sphinx des glaces」**，无 label 冲突）。

**VVV 2-char 核**：AM 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：AM 有 work 页 **[[An Antarctic Mystery]]**（label 'An Antarctic Mystery'）；链回之。Dirk Peters/Arthur Pym/Jeorling/Hearne/Martin Holt/William Guy/Len Guy 无对应页，纯文本叙述（不造死链）；Halbrane Land/Land of the Sphinx 无页纯文本。
book='An Antarctic Mystery'、location='The Land of the Sphinx, Antarctica'。

**逾达门 16 distinct solid PN**（AM-025）：AM-025-032/034/035/040/043（撕铁-艇毁-三尸）+ AM-025-054/056/075（悟磁-撕船-物附）+ AM-025-072/082/083/084/085/086（Peters 身倾-觅尸-锈枪-呼 Pym-心碎）+ AM-025-087/088（Pym 之命-葬 Peters）。

prose-gate：add_page 前 /tmp 初稿 2 段超门（438「铁器同向飞去」段 + 486「近丘悟磁」段），edit 前各拆一次（025-035 后、025-056 后断行）后 0 超段；add_page 一次成型（rev 3Oda49，size 3458）；Participants bullet 预置空行分隔无合并误报；全段 ≤400。pn_validator --mode strict ✓。

event 计数 55→56，registry total 1530→**1531**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| the-ice-sphinx | 3Oda49 | An Antarctic Mystery | The Land of the Sphinx, Antarctica | AM-025 | 16 distinct | 撕铁-悟磁-觅尸-恸亡单指（AM-025 单章高潮）；锚 AM-025 逐句核实、framing 准确；剔 halbrane-wreck(冰崩 已覆盖)/William Guy 流亡回溯/磁石物理成因长论/AM-026 北返别线；AM 2-char 无需 Note；避 work 页 alias「Sphinx of the Ice Fields」；链 [[An Antarctic Mystery]] |

- **the-ice-sphinx**：16 distinct solid PN（AM-025，冰之 Sphinx 揭晓）；aliases [The Magnetic Sphinx, Fate of Arthur Pym, Death of Dirk Peters]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指冰之 Sphinx 揭晓；halbrane-wreck/流亡回溯/磁石成因长论/AM-026 北返剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 2 段超门（438+486），各拆一次后 0 超段；bullet 预置空行无合并误报。✔
- **G3 ≥5 distinct PN**：16 solid（AM-025），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；AM 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1531 event 56 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug the-ice-sphinx ABSENT；变体 ABSENT；aliases 避 work 页 alias 无 label 冲突。✔
- **单指核**：AM-025 撕铁-悟磁-觅尸-恸亡因果逐句确认；climax 单章 AM-025 核实；与 halbrane-wreck 分工不重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R293 起始计数）

| 字段 | R292 起始 | R293 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 292 | 293 |
| type_round | 58 | 59 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 228 | 229 |
| last_updated_round | 292 | 293 |

## 遗留问题

1. **event 页数 56**：本轮 +1（AM 第二 event）。queue(event) 1→**0**（建序 42 消费，R289 discover 队列全清）。registry 全库 **1531**，unknown 0。
2. **下轮 R293 = SCN28-zombie（§3(4)）**：since_evv5=4<10；streak=0<3；since_discover=3<10 且全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**。续「单事件作品掘第二事件」策略：re-scan 余未采单事件作品（pn_anchor 反查终末高潮章），掘 ≥3 候选。目标 new_candidates≥3 保 discover_streak_low=0。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 AM-025 锚 + framing 逐句核实均准确，无需改。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略**：20 单事件作品为第二事件矿脉；已建 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/RM/EHLA/**AM** 十二部第二 event。R293 zombie 须 re-scan 余单事件作品定第三批候选。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解；本轮页 16 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 2 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=228→229（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
