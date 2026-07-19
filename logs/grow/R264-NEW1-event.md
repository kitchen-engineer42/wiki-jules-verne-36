---
round: 264
date: 2026-07-18
type_round: 31
phase: "2.1"
current_type: event
gene: NEW1
pages: [finding-of-louis-cornbutte]
result: success
---

# GROW 2.1-B · R264 · NEW1 · event — 建 The Finding of Louis Cornbutte（北极搜寻队雪屋寻获生还之子 Louis，WAI）

## 执行摘要

Phase 2.1-B event 类型第 23 建（type_round 31），消费 R262 discover 队列**建序 23**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Finding of Louis Cornbutte**（WAI 首 event）。Jean Cornbutte 率 Penellan、Marie 等北极搜寻队循烟与呼救声横越 Shannon Island 冰原，
先遇冻毙水手 Courtois，终抵雪屋，濒死之子 Louis Cornbutte 爬出重逢获救。

**锚精修（第四例消歧）**：R262 队列记 pn_anchor=**WAI-011**，然逐句核 WAI-011 止于绝望——该章末（WAI-011-050）Jean 面对死者 Courtois 悲呼「我的儿子、Louis！」，Louis 生死未卜。
**真正的寻获**在下一章 **WAI-012**：WAI-012-002/003「一濒死之人爬出雪屋——是 Louis Cornbutte」，WAI-012-007 昏厥入父与 Marie 怀中经救护苏醒。锚改 **WAI-012**（Louis 生还现身之章）。slug 保持 finding-of-louis-cornbutte。

**单指核**：全 8 PN 单指此搜救-寻获事件（望烟→闻呼救→遇死者→抵雪屋→Louis 现身→苏醒→获救→归船之图），一连续事件。
**排除**：WAI-011 前段搜寻航程泛述、Vasling 觊觎 Marie 之别线剔除；Courtois 之死作为寻获途中之节取一句（WAI-011-039），非另立事件。
exact-slug finding-of-louis-cornbutte ABSENT（变体 louis-cornbutte-rescue/jeune-hardie-rescue 亦 ABSENT）。**WAI 3-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（WAI-011×4 + WAI-012×4，跨两章）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | WAI-011-024 | 东北方升起轻烟示有人烟、Penellan 喜呼确证不误（望烟）|
| What Happens | WAI-011-035 | 微弱可辨之声——呼救之音、两度重复、旋归寂静（闻呼救）|
| What Happens | WAI-011-039 | Penellan 遇冰上一人、乃水手 Courtois、Louis 之伴、已冻毙（遇死者）|
| What Happens | WAI-011-045 | 一哩外雪屋冒烟、木门紧闭、二人冲出、Penellan 认出 Pierre Nouquet（抵雪屋）|
| What Happens | WAI-012-003 | 一濒死之人爬出雪屋沿冰而行——乃 Louis Cornbutte、憔悴至仇敌 Vasling 不识（Louis 现身）|
| Significance | WAI-012-007 | Louis 昏厥入父与 Marie 怀、曳入屋中、精心救护得苏（苏醒）|
| Significance | WAI-012-014 | Louis 呼「吾友、吾辈得救！」迎冒万险来救之父（获救）|
| Significance | WAI-012-015 | 父告以其双桅 Jeune-Hardie 稳泊六十里外冰中、众将同归（归船）|

**VVV 处置**：WAI 3-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 211/181/170 字，均 <400）。pn_validator --mode strict ✓。

event 计数 37→38，registry total 1512→**1513**，unknown 恒 0。add_page 一次成型（rev xdAaRD，size 2858，
quality 自动 featured）。
location=Shannon Island、pn_anchor=WAI-012、book=A Winter Amid the Ice、aliases=[The Rescue at Shannon Island, The Finding of the Jeune-Hardie Castaways]。
链 *[[a-winter-amid-the-ice|A Winter Amid the Ice]]*（Jean Cornbutte、Penellan、Louis Cornbutte、Marie、André Vasling、Pierre Nouquet 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| finding-of-louis-cornbutte | xdAaRD | A Winter Amid the Ice | Shannon Island | WAI-012 | 8 distinct | 搜寻队雪屋寻获生还 Louis 单指；**锚由 queue 记 WAI-011（前段/死者绝望）精修为 WAI-012（Louis 现身 012-003）**；剔搜寻泛述/Vasling 别线；WAI 3-char 无 Note |

- **finding-of-louis-cornbutte**：8 distinct solid PN（WAI-011×4 + WAI-012×4，跨两章）；aliases [The Rescue at Shannon Island, The Finding of the Jeune-Hardie Castaways]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指搜救-寻获；搜寻泛述/Vasling 别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（211/181/170，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（WAI-011/012），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；WAI 3-char 无需 Note。✔
- **registry 一致**：total 1513 event 38 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug finding-of-louis-cornbutte ABSENT；变体 ABSENT；非既有 37 event；无 alias 冲突。✔
- **单指核**：WAI-012-003 Louis 生还现身逐句确认；WAI-011 死者绝望前段精修排除为锚。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R265 起始计数）

| 字段 | R264 起始 | R265 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 264 | 265 |
| type_round | 30 | 31 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 200 | 201 |
| last_updated_round | 264 | 265 |

## 遗留问题

1. **event 页数 38**：本轮 +1（WAI 首 event）。queue(event) 2→**1**（建序 23 消费，余 24）。registry 全库 **1513**，unknown 0。
2. **下轮 R265 = NEW1（event）**：建 queue 建序 24 **death-of-master-zacharius**（MZ，MZ-005）。
   since_evv5=9<10、streak=0、queue(event)=1>0 → §3(7) NEW1。**MZ 2-char 无需 Note**。
   建时核老钟匠钟毁人亡单指（末座大钟迸裂、Pittonaccio 攫魂、殁于 Andernatt 峰间）、剔前段钟表失灵泛述；*[[master-zacharius]]* 链回工作页（若存）。
   **注**：R265 后 since_evv5→10，**R266 = EVV5**（§3(1b) 触发），非 build；EVV5 后 queue(event)=0 → R267 = SCN28-zombie discover。
3. **消歧方法论沉淀（R256/R260/R261/R264）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。
   已积四例：R256 UC-005→UC-018、R260 TT-004→TT-018、R261 BR-003→BR-006、**R264 WAI-011→WAI-012**（前章绝望 vs 次章 Louis 生还现身）。
4. **event 覆盖**：26/36 部作品含 event；本会话由 15/36 经 WC/TT/BR/DOSE/WAI 增至 26/36。
5. **event PN 回填债（R244/R255 EVV5 记录）**：13/36 早期页 <5 PN，DEFERRED，下次 EVV5（约 R266）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=200→201（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
