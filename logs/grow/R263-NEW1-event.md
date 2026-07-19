---
round: 263
date: 2026-07-18
type_round: 30
phase: "2.1"
current_type: event
gene: NEW1
pages: [quiquendone-frenzy]
result: success
---

# GROW 2.1-B · R263 · NEW1 · event — 建 The Oxygen Frenzy of Quiquendone（Doctor Ox 氧气饱和全城致狂、气厂爆炸告终，DOSE）

## 执行摘要

Phase 2.1-B event 类型第 22 建（type_round 30），消费 R262 discover 队列**建序 22（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10 → §3(1) 否；streak=0<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；
queue(event)=3>0 → §3(4) 否；stub%=0 → §3(5/6) 否；**默认 §3(7) NEW1**）。

**The Oxygen Frenzy of Quiquendone**（DOSE 首 event）。Doctor Ox 借煤气管道以纯氧饱和平和的 Flemish 小镇 Quiquendone，
市民陷入狂热、艺术激情与对邻镇 Virgamen 的战争热；终以 Ox 气厂意外爆炸告终，小镇复归 phlegmatic 本性，Ox 与助手 Ygène 消失。

**单指核**：全 9 PN 单指 Doctor Ox 氧气实验这一事件（机理→效应→狂热顶点→战争决意→爆炸→揭底→复归）。
**排除**：醉舞会、议会争吵、Frantz/Suzel 恋情加速等属实验的**逐场景插曲**，剔除，仅取框定实验本身立意与转折的句。
**消歧**：DOSE 工作页 slug 为 `doctor-oxs-experiment`（type=work，小说本身），event 用 slug `quiquendone-frenzy` 避混淆，*[[doctor-oxs-experiment|Doctor Ox's Experiment]]* 链回。
exact-slug quiquendone-frenzy ABSENT（变体 doctor-ox-experiment/gasworks-explosion/oxygen-frenzy 亦 ABSENT）。**DOSE 4-char → 已加 page-top RFC-0003 Note**。

**恰达门 9 distinct solid PN**（四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | DOSE-017-002 | Ox 敷管后先饱和公共建筑、再私宅、终街道以纯氧，不掺一原子氢（机理）|
| What Happens | DOSE-017-003 | 无味无臭之氧大量弥散、呼吸致剧烈躁动、居氧饱和之气者兴奋狂燥而燃（效应）|
| What Happens | DOSE-014-002 | 全镇最老最温和的两友旧谊方复即刻反目动武，见狂热已至何等地步（顶点）|
| What Happens | DOSE-013-016 | 市长与议员本不能争、今誓四十八时内出兵伐邻镇 Virgamen（战争决意）|
| What Happens | DOSE-015-002 | 一声巨爆响起、笼罩全镇之气若燃、异常灿烈之焰如流星射天（爆炸）|
| Significance | DOSE-015-006 | 气厂径自炸毁、氧氢两库间通道成爆混气遇火（起因揭底）|
| Significance | DOSE-015-007 | 军队重整时 Ox 与助手 Ygène 已消失（实验者遁）|
| Significance | DOSE-016-002 | 爆炸后 Quiquendone 即刻复归其素来平和、phlegmatic 之 Flemish 小镇（复归）|
| Significance | DOSE-017-006 | 幸而天意一爆结此危险实验、废 Ox 气厂（终评）|

**VVV 处置**：DOSE 4-char，page-top RFC-0003 Note 已加，PN 渲染为纯文本待 RFC-0003，PN 数据有效。
prose-gate awk（含 `!/^> /` 跳 Note）首过仅 Participants bullet 块合并误报（三 bullet 各 163/186/153 字，均 <400）。pn_validator --mode strict ✓。

event 计数 36→37，registry total 1511→**1512**，unknown 恒 0。add_page 一次成型（rev t9xkc2，size 3395，
quality 自动 featured）。
location=Quiquendone、pn_anchor=DOSE-015、book=Doctor Ox's Experiment、aliases=[Doctor Ox's Oxygen Experiment, The Quiquendone Epidemic]。
链 *[[doctor-oxs-experiment|Doctor Ox's Experiment]]*（Doctor Ox、Ygène、Van Tricasse、Niklausse 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| quiquendone-frenzy | t9xkc2 | Doctor Ox's Experiment | Quiquendone | DOSE-015 | 9 distinct | Ox 氧气实验单指（机理→狂热→爆炸→揭底→复归）；剔逐场景插曲（醉舞会、议会争吵、恋情加速）；DOSE 4-char → RFC-0003 Note；event slug quiquendone-frenzy 避与工作页 doctor-oxs-experiment 混淆 |

- **quiquendone-frenzy**：9 distinct solid PN（DOSE-013/014/015/016/017，五章分配）；aliases [Doctor Ox's Oxygen Experiment, The Quiquendone Epidemic]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ox 氧气实验；逐场景插曲剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（163/186/153，awk 块合并误报已核）；Note blockquote 由 `!/^> /` 跳过。✔
- **G3 ≥5 distinct PN**：9 solid（DOSE-013/014/015/016/017），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；DOSE 4-char → RFC-0003 Note 已加。✔
- **registry 一致**：total 1512 event 37 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug quiquendone-frenzy ABSENT；变体 ABSENT；非既有 36 event；工作页 doctor-oxs-experiment(type=work) 已辨明非冲突；无 alias 冲突。✔
- **单指核**：DOSE-013/014/015/016/017 逐句确认框定实验立意与转折；插曲别线排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R264 起始计数）

| 字段 | R263 起始 | R264 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 263 | 264 |
| type_round | 29 | 30 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 199 | 200 |
| last_updated_round | 263 | 264 |

## 遗留问题

1. **event 页数 37**：本轮 +1（DOSE 首 event）。queue(event) 3→**2**（建序 22 消费，余 23-24）。registry 全库 **1512**，unknown 0。
2. **下轮 R264 = NEW1（event）**：建 queue 建序 23 **finding-of-louis-cornbutte**（WAI，WAI-011）。
   since_evv5=8<10、streak=0、queue(event)=2>0 → §3(7) NEW1。**WAI 3-char 无需 Note**。
   建时核 Jean Cornbutte 北极搜寻队雪屋寻获 Louis 与幸存者单指、剔前段搜寻航程泛述；*[[winter-amid-the-ice]]* 链回工作页（若存）。
3. **消歧方法论沉淀（R256/R260/R261）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。已积三例修正。
4. **event 覆盖**：25/36 部作品含 event；本会话由 15/36 经 WC/TT/BR/DOSE 增至 25/36。
5. **event PN 回填债（R244/R255 EVV5 记录）**：13/36 早期页 <5 PN，DEFERRED，下次 EVV5（约 R267）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=199→200（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
