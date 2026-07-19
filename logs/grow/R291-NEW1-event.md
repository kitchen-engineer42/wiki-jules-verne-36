---
round: 291
date: 2026-07-18
type_round: 57
phase: "2.1"
current_type: event
gene: NEW1
pages: [rescue-of-joam-dacosta]
result: success
---

# GROW 2.1-B · R291 · NEW1 · event — 建 The Rescue of Joam Dacosta（绞架前 Jarriquez 破译密文宣读 Ortega 自白救 Joam，EHLA 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 55 建（type_round 57），消费 R289 discover 队列**建序 41**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；streak=0<3；since_discover=1<10、全局 queue≥10 → §3(3) 否；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Rescue of Joam Dacosta**（EHLA 第二 event，作品原仅 amazon-cryptogram 密文解谜）——*Eight Hundred Leagues on the Amazon* 之终局。
行刑令下、定 8 月 31 晨九时绞 Joam Dacosta；同晨 Fragoso 策马精疲力竭赶回 Manaos，带回其查得亡者 Torres 之旧友名——Ortega；
送葬般刑队正行，Judge Jarriquez 携破译之密文赶至、刑队立止；判官坐石座，当 Joam 拥妻之际高声宣读——以 Ortega 之名所derive 之数破解全篇密文，文中真凶自白乃 Ortega 非 Joam，Joam 昭雪，万众欢呼。

**分工核实（关键，避与 amazon-cryptogram 重叠）**：既有 amazon-cryptogram 覆盖**智力解谜/文档本身**（PN 跨 EHLA-027~034，止于「解读苦斗」）；
本页覆盖**临刑赦免/人物营救**（EHLA-038 行刑令+Fragoso 疾驰、EHLA-039 刑场宣读昭雪），二者 PN 区段不重叠、叙事焦点分明（谜题 vs 营救），非重复。逐句核 EHLA-038/039 确证。

**锚核（逐句复核，锚无误、framing 准确）**：R289 队列记 pn_anchor=**EHLA-039**（刑场宣读高潮章题句「ON THE ARRIVAL of the judge the mournful procession halted」）。
逐句核：行刑令+Fragoso 疾驰（EHLA-038-002/006/009/013/015/021）在前章；刑队止+宣读+真凶自白+昭雪+欢呼（EHLA-039-001/004/011/012/014/015/016/023/026）确在 **EHLA-039**。framing 与文本相符，无需改锚、无需改 slug。跨 EHLA-038/039 取 PN。

**单指核**：全 16 distinct PN 单指临刑赦免这一连续因果（行刑令下→无可救→Fragoso 疾驰→是 Fragoso！→识 Torres 为林中队长→寻得队长→问亡友之名（Ortega）→刑队止→判官宣读→以数破全文→真凶乃 Ortega→自愿招认→欢呼→阖家环立→Ortega 悔而书之→其名解密）。
**排除**：amazon-cryptogram（密文解谜苦斗，首 event 已建独立页）；密文原文乱码行（EHLA-039-005~010 法文+数字密码，不逐字引）；Ortega 犯罪始末回溯（EHLA-039-017~024 前情，仅取 023 悔书一句）剔除；jangada 竹筏溯 Amazon 之旅（前半部背景）剔除。
exact-slug rescue-of-joam-dacosta ABSENT（变体 joam-dacosta-reprieve/gallows-reprieve/vindication-of-joam-dacosta 亦 ABSENT）。aliases [The Gallows Reprieve, Vindication of Joam Dacosta, The Ortega Confession]（无 label 冲突）。

**VVV 4-char 核（RFC-0003）**：EHLA 为 4-char VVV，pn_validator --mode strict ✓；**建后核 PN 渲染为标准 (EHLA-038-002) 无断行**（与 R283 DSCF 4-char 先例一致），**无需 RFC-0003 Note**。

**工作页处置**：EHLA 有 work 页 **[[Eight Hundred Leagues on the Amazon]]**；链回之 + [[The Amazon Cryptogram]]（event 页交叉链，分工互补）。Joam/Jarriquez/Fragoso/Torres/Ortega/Yaquita 无对应页，纯文本叙述（不造死链）；Manaos/Tijuco 无页纯文本。
book='Eight Hundred Leagues on the Amazon'、location='Manaos, on the Amazon, Brazil'。

**逾达门 16 distinct solid PN**（跨 EHLA-038/039）：EHLA-038-002/005/006/009/013/015/021（行刑令+Fragoso 疾驰+问名）+ EHLA-039-001/004/011/012/014/015/016/023/026（刑队止+宣读+真凶自白+昭雪+欢呼+解密之由）。

prose-gate：add_page 一次成型（rev hYyixz，size 3301）；初稿 Significance 末段 427 字超门，edit 前于 /tmp 拆为两段（EHLA-039-014 后断行）后一次通过；Participants bullet 预置空行分隔无合并误报；全段 ≤400。pn_validator --mode strict ✓。

event 计数 54→55，registry total 1529→**1530**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| rescue-of-joam-dacosta | hYyixz | Eight Hundred Leagues on the Amazon | Manaos, on the Amazon, Brazil | EHLA-039 | 16 distinct | 行刑令-疾驰-破译-临刑宣读-昭雪单指（跨 EHLA-038/039）；锚 EHLA-039 逐句核实、framing 准确；与 amazon-cryptogram 分工（解谜 vs 营救）非重复；剔密文乱码行/Ortega 始末回溯/jangada 之旅别线；EHLA 4-char 渲染正常无需 Note；链 [[Eight Hundred Leagues on the Amazon]]+[[The Amazon Cryptogram]] |

- **rescue-of-joam-dacosta**：16 distinct solid PN（跨 EHLA-038/039，临刑赦免）；aliases [The Gallows Reprieve, Vindication of Joam Dacosta, The Ortega Confession]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指临刑赦免；amazon-cryptogram 解谜/密文乱码行/Ortega 回溯/jangada 之旅剔除；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 1 段 427 超门，拆段后 0 超段；bullet 预置空行无合并误报。✔
- **G3 ≥5 distinct PN**：16 solid（跨 EHLA-038/039），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；EHLA 4-char PN 渲染标准无断行、无需 Note。✔
- **registry 一致**：total 1530 event 55 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug rescue-of-joam-dacosta ABSENT；变体 ABSENT；aliases 无 label 冲突。✔
- **单指核**：EHLA-038/039 临刑赦免因果逐句确认；宣读 climax EHLA-039 核实；与 amazon-cryptogram 分工不重叠。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R292 起始计数）

| 字段 | R291 起始 | R292 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 291 | 292 |
| type_round | 57 | 58 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 227 | 228 |
| last_updated_round | 291 | 292 |

## 遗留问题

1. **event 页数 55**：本轮 +1（EHLA 第二 event）。queue(event) 2→**1**（建序 41 消费；余建序 42 the-ice-sphinx）。registry 全库 **1530**，unknown 0。
2. **下轮 R292 = NEW1（§3(7)）**：since_evv5=3<10；streak=0<3；since_discover=2<10 且全局 queue≥10；queue(event)=1>0；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 42 the-ice-sphinx（AM）**。AM 2-char 无需 Note；逐句核 AM-025 磁石觅尸序列。**建序 42 消费后 queue(event)=0 → R293 起 SCN28-zombie 续掘**（since_evv5 届时=4，非 EVV5）。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 EHLA-039 锚 + framing 逐句核实均准确；且与 amazon-cryptogram 之分工经逐句核 PN 区段确认不重叠。教训延续（R283 改锚 / R286 改锚+改 slug）。
4. **event 覆盖策略**：20 单事件作品为第二事件矿脉；已建 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/RM/**EHLA** 十一部。余 AM（queue 建序 42 待建）+ 其他单事件作品留后续 zombie 续掘。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解；本轮页 16 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 1 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=227→228（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
