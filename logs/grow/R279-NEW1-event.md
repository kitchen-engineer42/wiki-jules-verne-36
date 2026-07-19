---
round: 279
date: 2026-07-18
type_round: 45
phase: "2.1"
current_type: event
gene: NEW1
pages: [assault-on-irkutsk]
result: success
---

# GROW 2.1-B · R279 · NEW1 · event — 建 The Assault on Irkutsk（Ogareff 内应叛谋·Angara 火河·鞑靼夜袭，MS 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 33 建（type_round 45），消费 R275 discover 队列**建序 33**（队列末项）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Assault on Irkutsk**（MS 第二 event，作品原仅 strogoff-blinding MS-024）。叛徒 Ivan Ogareff 假冒沙皇信使潜入宫中，
与鞑靼 Emir 定内应之谋：佯攻 Angara 上下游、诱大公集兵于河岸、空置 Bolchaia 门；凌晨二时自宫台掷燃引信入 Angara——
河面早已依其令泼满 naphtha 石油，顷刻全河成蓝焰火河、上下游皆燃；同时南北炮击、数千鞑靼扑击土垒、岸屋尽焚；
守军困于鞑靼攻势与烈火之间、警钟大作，而 Bolchaia 门仅余小队几近空置。**叛卖-火河-夜袭三线合一之首府陷落序幕**。

**锚核（本轮逐句复核，改采动作序列句）**：R275 队列记 pn_anchor=**MS-033**，且明标「须逐句复核 MS-033 主线(叛谋夜袭)与火河 PN 归属，锚为线索非定论」。
逐句核 MS-033（215 sents/71 paras）：queue 原候选（001/003/005/016/017/019）多为叛谋铺垫与 Ogareff 潜伏静态句，
实建时**改采叛谋-火河-夜袭动作序列**：叛谋 001（空置 Bolchaia 门）/002（佯攻 Angara）/006（蓄意制恐怖灾祸）+
火河 021（掷燃引信入河）/022（依令泼 naphtha）/023（决堤石油库泄流）/024（全河蓝焰）+ 夜袭 025（南北炮击、数千鞑靼扑垒、岸屋焚）/
027（守军困于攻势与火之间、警钟）/028（Bolchaia 门几空）。锚 **MS-033** 确认无误、保持。

**单指核**：全 10 distinct PN 单指 Irkutsk 之陷落这一连续事件（叛谋→佯攻→点火→火河→夜袭→守军困→门开）。
**排除**：MS-024 strogoff-blinding（Tomsk 灼目，已建独立页）；**MS-033-032~049 Michael/Nadia 抵岸 + Michael-Ogareff 宫中私斗**（属人物对决支线，非首府攻防，整体剔除）；Emir/Feofar 别线剔除。
exact-slug assault-on-irkutsk ABSENT（变体 defense-of-irkutsk/siege-of-irkutsk/battle-of-irkutsk/irkutsk-assault/the-river-of-fire 亦 ABSENT）。**MS 2-char → 无需 page-top Note**。

**工作页处置**：MS 有 work 页 **[[Michael Strogoff]]**；链回之 + [[Irkutsk]]（place）。Ogareff/Nadia/Angara 无对应页，纯文本叙述（不造死链）。
book=Michael Strogoff、location=Irkutsk, on the Angara, Eastern Siberia。

**逾达门 10 distinct solid PN**（皆 MS-033，叛谋-火河-夜袭全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | MS-033-006 | 叛徒蓄意制骇人灾祸、以恐怖压倒守城者之心（动机）|
| What Happens | MS-033-001 | 谋使 Bolchaia 门无守或仅弱守、诱守方注意力它移（叛谋）|
| What Happens | MS-033-002 | 与 Emir 定佯攻上下游 + 左岸佯渡 Angara（佯攻）|
| What Happens | MS-033-021 | 凌晨二时自宫台掷燃引信药捻入 Angara（点火）|
| What Happens | MS-033-022 | 依其令 naphtha 石油早已泼满 Angara 河面（火源）|
| What Happens | MS-033-024 | 顷刻全河成蓝焰、上下游皆燃、蒸汽腾空（火河）|
| Significance | MS-033-025 | 南北炮击、数千鞑靼扑击土垒、岸木屋尽焚（夜袭）|
| Significance | MS-033-027 | 守军困于鞑靼攻势与烈火之间、警钟大作民奔走（困境）|
| Significance | MS-033-028 | Bolchaia 门几近自由、仅余极小守队（门开）|
| Setting | MS-033-023 | 决堤石油库泄 naphtha 成流、漫布 Angara（背景）|

**VVV 处置**：MS 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 243/208/221 字，均 <400）。pn_validator --mode strict ✓。

event 计数 46→47，registry total 1521→**1522**，unknown 恒 0。add_page 一次成型（rev 59vhoi，size 3044，
quality 自动 featured）。
location=Irkutsk, on the Angara, Eastern Siberia、pn_anchor=MS-033、book=Michael Strogoff、aliases=[The Burning of the Angara, The River of Fire]。
链 [[Michael Strogoff]]+[[Irkutsk]]。build_registry 仅 Robur PARK（既有债）。

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
| assault-on-irkutsk | 59vhoi | Michael Strogoff | Irkutsk, on the Angara, Eastern Siberia | MS-033 | 10 distinct | 叛谋-火河-夜袭单指（空置 Bolchaia 门 → 佯攻 Angara → 掷火 → naphtha 火河 → 鞑靼扑垒 → 守军困）；锚 MS-033 逐句核实无误保持；queue 候选多铺垫句、改采动作序列；剔 MS-024 灼目/MS-033 Michael-Ogareff 私斗支线/Emir 别线；MS 2-char 无 Note；链 [[Michael Strogoff]]+[[Irkutsk]] |

- **assault-on-irkutsk**：10 distinct solid PN（皆 MS-033，首府陷落全程）；aliases [The Burning of the Angara, The River of Fire]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Irkutsk 陷落；strogoff-blinding/Michael-Ogareff 私斗/Emir 别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（243/208/221，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：10 solid（皆 MS-033），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；MS 2-char 无需 Note。✔
- **registry 一致**：total 1522 event 47 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug assault-on-irkutsk ABSENT；变体 5 式 ABSENT；registry sweep 'irkutsk' 仅 irkutsk(place)+MS-ch31(chapter)，无 event 覆盖；无 alias 冲突。✔
- **单指核**：MS-033 首府陷落逐句确认；锚核实无误无需改锚；queue 候选铺垫句、改采动作序列句。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R280 起始计数）

| 字段 | R279 起始 | R280 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 279 | 280 |
| type_round | 45 | 46 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 215 | 216 |
| last_updated_round | 279 | 280 |

## 遗留问题

1. **event 页数 47**：本轮 +1（MS 第二 event）。queue(event) 1→**0**（建序 33 消费，队列清空）。registry 全库 **1522**，unknown 0。
2. **下轮 R280 = SCN28-zombie（§3(4)）**：since_evv5=2<10；streak=0<3；since_discover=3<10、全局 queue≥10 → §3(3) 否；
   **queue(event)==0 → §3(4) SCN28-zombie 触发**。须掘 event 新候选：继续「单事件作品掘第二事件」策略，
   扫尚未开采第二事件之单 event 作品（候选：DSCF/FWB/FC 等，或 MW/MS/RC 之第三事件）。discover 若 new_candidates<3 则 discover_streak_low+1。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。四例修正（R256/R260/R261/R264）+ R272 nemo-death dup（查重失误）
   + 十例核实无误（R265/R268/R269/R270/R273/R274/R276/R278/**R279**）。R278/R279 均遇 queue 候选 PN 偏铺垫、改采动作序列句，锚本身无误。
4. **event 覆盖策略**：R275 discover 队列（建序 31/32/33）**已全部消费**。R280 SCN28-zombie 须补种子。零 event 作品穷尽（SI≈MI/VB=DA），续掘单事件作品第二/第三事件。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可借机补 PN 至 ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债**：13/47 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解；R278/R279 新建页各 10 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=215→216（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
