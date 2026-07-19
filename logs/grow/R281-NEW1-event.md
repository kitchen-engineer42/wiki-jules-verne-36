---
round: 281
date: 2026-07-18
type_round: 47
phase: "2.1"
current_type: event
gene: NEW1
pages: [destruction-of-back-cup]
result: success
---

# GROW 2.1-B · R281 · NEW1 · event — 建 The Destruction of Back Cup（Roch 面三色旗拒射·全岛爆炸夷焦礁，FF 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 34 建（type_round 47），消费 R280 discover 队列**建序 34**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Destruction of Back Cup**（FF 第二 event，作品原仅 abduction-of-thomas-roch）——书名 *Facing the Flag* 之同名高潮。
五国舰队进击 Ker Karraje 海盗巢穴 Back Cup；法国发明家 Thomas Roch 以 fulgurator 击沉首舰；法舰 Tonnant 升三色旗闯入，
Roch 面祖国之旗幡然醒悟、拒向其施射、掷碎起爆药瓶；随后炮击与爆炸夷 Back Cup 为焦礁、Ker Karraje 匪帮尽灭、唯 Simon Hart 生还。

**锚核（本轮跨章取 PN）**：R280 队列记 pn_anchor=**FF-018**（章题「ON BOARD THE TONNANT」，Tonnant 视角之毁灭全程），
并标「FF-017 邻章 Roch 认旗拒射可补」。逐句核 FF-017（Simon Hart 手记，含「面旗」高潮）+ FF-018（Tonnant 视角毁灭），
「面旗」核心情节实在 **FF-017-069~083**（法号→升三色旗→Roch 醒悟拒射→掷碎药瓶），毁岛在 **FF-018-016~025**。
故本页跨 FF-017/018 取 PN，pn_anchor 保持 **FF-018**（毁灭章）。

**单指核**：全 11 distinct PN 单指 Back Cup 之毁灭这一连续高潮（引擎击沉首舰→升旗→面旗拒射→碎药瓶→Tonnant 闯入→巨震→夷岛→匪灭→Hart 生还）。
**排除**：FF-002/003 abduction-of-thomas-roch（已建独立页）；FF-017 前半 Simon Hart 潜行出洞子线（仅取与毁灭直接相关句）；Serko/Spade 别线细节剔除。
exact-slug destruction-of-back-cup ABSENT（变体 fall-of-back-cup/back-cup-destruction 亦 ABSENT）。**facing-the-flag 为 work 页非 event**，故 aliases 避用「Facing the Flag」（与 work label 冲突），采 [The Fall of Back Cup, The End of Ker Karraje]。**FF 2-char → 无需 page-top Note**。

**工作页处置**：FF 有 work 页 **[[Facing the Flag]]**；链回之 + [[Back Cup]]（place）+ [[The Abduction of Thomas Roch]]（同作首 event 交叉链）。Thomas Roch/Ker Karraje/Simon Hart 无对应页，纯文本叙述（不造死链）。
book=Facing the Flag、location=Back Cup, Bermuda archipelago。

**逾达门 11 distinct solid PN**（跨 FF-017/018，Back Cup 毁灭高潮）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | FF-018-006 | 议决如攻堡垒炮击夷平 Back Cup 山（缘起）|
| What Happens | FF-017-052 | Roch 掷三引擎、三百尺高长弧射向首舰（击发）|
| What Happens | FF-017-056 | 首舰爆碎、fulgurator 无穷之威（沉首舰）|
| What Happens | FF-017-072 | 三色旗迎风展、蓝白红耀于天（升旗）|
| What Happens | FF-017-078 | 面祖国之旗 Roch 幡然醒悟而退（面旗）|
| What Happens | FF-017-083 | Roch 掷药瓶于地、以足碾碎、自毁其械（碎瓶）|
| Significance | FF-018-016 | Tonnant 冒毁险闯危区半里、升旗迂回（闯入）|
| Significance | FF-018-019 | 骇天巨震撼山（巨震）|
| Significance | FF-018-020 | Back Cup 夷为焦礁碎石、海浪拍打（夷岛）|
| Participants | FF-018-011 | 海盗 Ker Karraje 曾握 Roch 之 fulgurator（人物）|
| Setting | FF-018-025 | 独一具完整之尸 Simon Hart 尚存、手执笔记（生还）|

**VVV 处置**：FF 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 269/187/209 字，均 <400）。pn_validator --mode strict ✓。

event 计数 47→48，registry total 1522→**1523**，unknown 恒 0。add_page 一次成型（rev qJtQIX，size 2906，
quality 自动 featured）。
location=Back Cup, Bermuda archipelago、pn_anchor=FF-018、book=Facing the Flag、aliases=[The Fall of Back Cup, The End of Ker Karraje]。
链 [[Facing the Flag]]+[[Back Cup]]+[[The Abduction of Thomas Roch]]。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| destruction-of-back-cup | qJtQIX | Facing the Flag | Back Cup, Bermuda archipelago | FF-018 | 11 distinct | 击沉首舰-面旗拒射-碎瓶-夷岛单指（跨 FF-017/018）；「面旗」核心在 FF-017-069~083 逐句核；剔 abduction(FF-002/003 已覆盖)/Hart 潜行子线/Serko 别线；aliases 避「Facing the Flag」(work label 冲突)；FF 2-char 无 Note；链 [[Facing the Flag]]+[[Back Cup]]+[[The Abduction of Thomas Roch]] |

- **destruction-of-back-cup**：11 distinct solid PN（跨 FF-017/018，Back Cup 毁灭高潮）；aliases [The Fall of Back Cup, The End of Ker Karraje]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Back Cup 毁灭；abduction/Hart 潜行/Serko 别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（269/187/209，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：11 solid（跨 FF-017/018），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；FF 2-char 无需 Note。✔
- **registry 一致**：total 1523 event 48 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug destruction-of-back-cup ABSENT；变体 ABSENT；facing-the-flag 为 work 页非 event，aliases 避同名；无 alias 冲突。✔
- **单指核**：FF-017/018 毁灭高潮逐句确认；「面旗」核心 FF-017-069~083 核实；pn_anchor FF-018 保持。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R282 起始计数）

| 字段 | R281 起始 | R282 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 281 | 282 |
| type_round | 47 | 48 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 217 | 218 |
| last_updated_round | 281 | 282 |

## 遗留问题

1. **event 页数 48**：本轮 +1（FF 第二 event）。queue(event) 3→**2**（建序 34 消费，余 35/36）。registry 全库 **1523**，unknown 0。
2. **下轮 R282 = NEW1（§3(7)）**：since_evv5=4<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=2>0 → NEW1。
   建建序 35 **drawing-lots-on-the-raft**（SC2，SC2-053）。SC2 3-char 无需 Note；建时核漂流-饥渴-抽签-临刑-获救单指、剔 chancellor-fire(SC2-009 已覆盖)别线；须逐句复核抽签 PN；链 [[The Survivors of the Chancellor]]。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。R278/R279/R281 均遇 queue 候选偏铺垫或跨章、改采动作/高潮序列句，锚本身无误。十一例核实无误（R265/R268-274/R276/R278/R279/**R281**）+ R272 dup 教训。
4. **event 覆盖策略**：R280 discover 队列（建序 34/35/36）余 35/36。18 单事件作品续为矿脉，后续 zombie 轮续掘。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可补 PN 至 ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债**：13/48 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解；R278/R279/R281 新建页各 ≥10 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=217→218（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
