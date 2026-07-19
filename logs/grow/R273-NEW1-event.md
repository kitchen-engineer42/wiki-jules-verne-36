---
round: 273
date: 2026-07-18
type_round: 40
phase: "2.1"
current_type: event
gene: NEW1
pages: [destruction-of-lincoln-island]
result: success
---

# GROW 2.1-B · R273 · NEW1 · event — 建 Destruction of Lincoln Island（Franklin 火山复苏、熔岩毁地、气爆没岛仅余孤岩，SI）

## 执行摘要

Phase 2.1-B event 类型第 29 建（type_round 40），消费 R271 discover 队列**建序 29**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7)）。

**Destruction of Lincoln Island**（SI 第二 event）。Mount Franklin 火山复苏、喷发在即；熔岩自火山口喷薄、
毁磨坊屋舍等殖民地建设；殖民者退守未竟之船；3 月 8 夜 Dakkar Grotto 壁溃、海水涌入火山竖井、
气爆百里可闻、山块崩入太平洋、Lincoln 岛没于洋下，仅余一孤岩为六殖民者最后栖身之所。

**锚核（本轮无精修）**：R271 队列记 pn_anchor=**SI-019**，逐句核 SI-018/019/020 三章确为火山复苏-熔岩毁地-气爆没岛全程所在
（喷发在即 018-023 → 火山口喷焰连爆 018-044 → 熔岩毁殖民地 019-077 → 退守末船 019-078 → Grotto 溃气爆没岛 019-080 → 孤岩三十尺 020-002 → 四周皆没仅存窄岩 020-003 → 孤岩九日必死 020-007），锚 **SI-019** 确认无误、保持。

**单指核**：全 8 PN 单指 Lincoln 岛火山毁灭这一连续事件（预警→喷发→熔岩毁地→退守→气爆没岛→孤岩→尽没→绝境）。
**排除**：后续 Duncan 救援（另一事件）、Nemo 之死（建序 28）、殖民地日常重建等别线剔除，仅取火山毁岛本身之句。
exact-slug destruction-of-lincoln-island ABSENT（变体 lincoln-island-explosion/end-of-lincoln-island 亦 ABSENT）。**SI 2-char → 无需 page-top Note**。

**工作页处置**：SI 无独立 work 页；链既有 work 页 **[[The Mysterious Island]]**（Overview 段）。book=The Secret of the Island。

**恰达门 8 distinct solid PN**（跨 SI-018/019/020，火山毁岛全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SI-018-023 | 火山物质已燃、喷发在即、岛受威胁（预警）|
| What Happens | SI-018-044 | 火山口喷焰束、光片四射、连爆如排炮（喷发）|
| What Happens | SI-019-077 | 熔岩越花岗岩壁、毁磨坊屋舍畜栏——最后一击（毁地）|
| What Happens | SI-019-078 | 殖民者退守未竟之船、上缝未捻仍决避难（退守）|
| Significance | SI-019-080 | Grotto 壁溃海涌、气爆百里、山块崩入太平洋、洋覆全岛（没岛）|
| Significance | SI-020-002 | 唯余孤岩三十尺、大岛所在仅此固点浮出水面（孤岩）|
| Significance | SI-020-003 | 四周皆没深渊、Franklin 山崩裂、仅存窄岩为 Lincoln 岛所余（尽没）|
| Significance | SI-020-007 | 孤岩九日、船碎无火无路、势必尽亡（绝境）|

**VVV 处置**：SI 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 166/177/141 字，均 <400）。pn_validator --mode strict ✓。

event 计数 43→44，registry total 1518→**1519**，unknown 恒 0。add_page 一次成型（rev TglwoF，size 2846，
quality 自动 featured）。
location=Lincoln Island、pn_anchor=SI-019、book=The Secret of the Island、aliases=[The Explosion of Lincoln Island, The End of Lincoln Island]。
链 [[The Mysterious Island]]（Cyrus Harding 等散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| destruction-of-lincoln-island | TglwoF | The Secret of the Island | Lincoln Island | SI-019 | 8 distinct | 火山复苏-熔岩毁地-气爆没岛单指（Dakkar Grotto 溃 → 洋覆全岛 → 仅余孤岩）；锚 SI-019 核实无误保持；剔 Duncan 救援/Nemo 之死别线；SI 2-char 无 Note；无 work 页链 [[The Mysterious Island]] |

- **destruction-of-lincoln-island**：8 distinct solid PN（跨 SI-018/019/020，火山毁岛全程）；aliases [The Explosion of Lincoln Island, The End of Lincoln Island]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指火山毁岛；Duncan 救援/Nemo 之死/日常重建别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（166/177/141，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（跨 SI-018/019/020），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；SI 2-char 无需 Note。✔
- **registry 一致**：total 1519 event 44 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug destruction-of-lincoln-island ABSENT；变体 ABSENT；非既有 43 event；无 alias 冲突。✔
- **单指核**：SI-018/019/020 火山毁岛全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R274 起始计数）

| 字段 | R273 起始 | R274 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 273 | 274 |
| type_round | 39 | 40 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 209 | 210 |
| last_updated_round | 273 | 274 |

## 遗留问题

1. **event 页数 44**：本轮 +1（SI 第二 event）。queue(event) 2→**1**（建序 29 消费，余 30）。registry 全库 **1519**，unknown 0。
2. **下轮 R274 = NEW1（event）**：建 queue 建序 30 **the-madman-in-the-balloon**（DA，DA-001）。
   since_evv5=7<10、streak=0、queue(event)=1>0 → §3(7) NEW1。**DA 2-char 无需 Note**。
   建时核气球升空-疯客掀祸-脱险单指、剔球升技术/历代飞行家掌故别线；DA 有 work 页链 [[A Drama in the Air]]。
   **注**：R274 后 queue(event)=0 → R275 = SCN28-zombie discover（§3(4)）。
3. **消歧方法论四例沉淀（R256/R260/R261/R264）**：queue 锚点视为线索非定论，建时逐句复核。已积四例修正 + 六例核实无误（R265/R268/R269/R270/R272/R273）。
4. **event 覆盖 31/36**：建序 30（DA）建毕后达 32/36。
5. **event PN 回填债（R244/R255/R266 EVV5）**：13/44 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=209→210（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **零 event 剩余**：VB（备选）、AMB/YEAR（判非事件）。R275 zombie 可掘 VB 或跨作品低覆盖作品。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
