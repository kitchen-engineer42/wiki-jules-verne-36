---
round: 270
date: 2026-07-18
type_round: 37
phase: "2.1"
current_type: event
gene: NEW1
pages: [ki-tsang-train-attack]
result: success
---

# GROW 2.1-B · R270 · NEW1 · event — 建 Ki-Tsang's Attack on the Grand Transasiatic（蒙古大盗掀轨截车、六十伏兵袭财车、Faruskiar 力战诛 Ki-Tsang，ASC）

## 执行摘要

Phase 2.1-B event 类型第 27 建（type_round 37），消费 R267 discover 队列**建序 27（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7)）。

**Ki-Tsang's Attack on the Grand Transasiatic**（ASC 首 event）。云南大盗 Ki-Tsang 于戈壁滩掀去百码铁轨、逼停大中亚铁路列车，
率六十蒙古游牧伏兵自丛林突袭欲夺运京帝室财宝；总经理 Faruskiar 力战护车、一击 kandijar 穿其胸诛之，匪徒溃退，己方三死十二伤、机车脱轨。

**锚核（本轮无精修）**：R267 队列记 pn_anchor=**ASC-020**，逐句核 ASC-020/021 两章确为掀轨-袭车-击退-正法全程所在
（布防 020 → 六十蒙古出丛 022 → 齐射 029 → 众入混战 030 → 匪溃退 045 → kandijar 诛首 050 → 名实 Ki-Tsang 021-001 → 机车脱轨待复 021-009），锚 **ASC-020** 确认无误、保持。

**单指核**：全 8 PN 单指此掀轨-袭车-击退这一连续事件（布防→出丛→齐射→接战→溃退→诛首→名实→善后）。
**排除**：Faruskiar 身份悬疑（Noltitz 疑其即云南大盗）、Kinko 藏匿、婚事插曲、复轨劳作细节等别线剔除，仅取袭击-击退本身之句。
exact-slug ki-tsang-train-attack ABSENT（变体 ki-tsang-raid/attack-on-the-grand-transasiatic/gobi-train-attack 亦 ABSENT）。**ASC 3-char → 无需 page-top Note**。

**工作页缺位处置**：Claudius Bombarnac 无 work 页（claudius-bombarnac ABSENT）。改链既有 organization 页
**[[Grand Transasiatic Railway Company]]**（Overview 段），book 字段用语料书名 **The Adventures of a Special Correspondent**（与 org 页 book 一致）。

**恰达门 8 distinct solid PN**（跨 ASC-020/021 两章，一次袭击全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | ASC-020-020 | 中国军官布兵于财车四周、备御来袭（布防）|
| What Happens | ASC-020-022 | 忽起呼喊、丛林放出伏兵——六十戈壁蒙古游牧（出丛）|
| What Happens | ASC-020-029 | 匪徒齐射、挥械呼号、逼近搁浅车厢（齐射）|
| What Happens | ASC-020-030 | Noltitz 少校与叙事者投身敌阵迎击（接战）|
| What Happens | ASC-020-045 | 匪徒即溃退、弃其死伤而不顾（溃退）|
| Significance | ASC-020-050 | Faruskiar 立伤匪之上、一击 kandijar 穿其心、终结袭击（诛首）|
| Significance | ASC-021-001 | 名实——正是 Ki-Tsang 于戈壁平原袭大中亚铁路（名实）|
| Significance | ASC-021-009 | 机车脱轨、首务即复轨越断线（善后）|

**VVV 处置**：ASC 3-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 179/136/187 字，均 <400）。pn_validator --mode strict ✓。

event 计数 41→42，registry total 1516→**1517**，unknown 恒 0。add_page 一次成型（rev xAiYGC，size 2435，
quality 自动 featured）。
location=Gobi Desert、pn_anchor=ASC-020、book=The Adventures of a Special Correspondent、aliases=[The Attack on the Grand Transasiatic, Ki-Tsang's Raid]。
链 [[Grand Transasiatic Railway Company]]（Ki-Tsang、Faruskiar、Noltitz 未建 character，散文提及）。
build_registry 仅 Robur PARK。

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
| ki-tsang-train-attack | xAiYGC | The Adventures of a Special Correspondent | Gobi Desert | ASC-020 | 8 distinct | 掀轨-袭车-击退单指（六十蒙古伏兵 → Faruskiar 诛 Ki-Tsang）；锚 ASC-020 核实无误保持；剔 Faruskiar 身份悬疑别线；ASC 3-char 无 Note；工作页缺位改链 org 页 |

- **ki-tsang-train-attack**：8 distinct solid PN（跨 ASC-020/021，一次袭击全程）；aliases [The Attack on the Grand Transasiatic, Ki-Tsang's Raid]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指袭击-击退；Faruskiar 身份悬疑/Kinko 藏匿/婚事/复轨劳作别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（179/136/187，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（跨 ASC-020/021），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；ASC 3-char 无需 Note。✔
- **registry 一致**：total 1517 event 42 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug ki-tsang-train-attack ABSENT；变体 ABSENT；非既有 41 event；无 alias 冲突。✔
- **单指核**：ASC-020/021 袭击全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R271 起始计数）

| 字段 | R270 起始 | R271 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 270 | 271 |
| type_round | 36 | 37 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 206 | 207 |
| last_updated_round | 270 | 271 |

## 遗留问题

1. **event 页数 42**：本轮 +1（ASC 首 event）。queue(event) 1→**0**（建序 27 消费，R267 三候选全建毕）。registry 全库 **1517**，unknown 0。
2. **下轮 R271 = SCN28-zombie discover（§3(4)）**：queue(event)==0 触发僵尸勘探。
   since_evv5=4<10、streak=0、queue(event)=0 → §3(4) SCN28-zombie。
   自剩余零/低 event 覆盖作品（**DA / SC / SC2 / VB / DSCF / AMB** 等）掘 ≥3 候选、逐章核 ≥8 distinct PN 可达、单指事件、exact-slug + 变体查重 ABSENT。
   若 new_candidates<3 则 discover_streak_low+1。
3. **消歧方法论四例沉淀（R256/R260/R261/R264）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。已积四例修正 + 四例核实无误（R265 MZ-005、R268 PL-009、R269 TN-019、R270 ASC-020）。
4. **event 覆盖**：30/36 部作品含 event；本会话由 15/36 经 WC/TT/BR/DOSE/WAI/MZ/PL/TN/ASC 增至 30/36。
5. **event PN 回填债（R244/R255/R266 EVV5 记录）**：13/42 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）或 EVV6 再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=206→207（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **工作页缺位记录**：Claudius Bombarnac 无 work 页（claudius-bombarnac ABSENT），本轮改链 organization 页 [[Grand Transasiatic Railway Company]]；后续若建 ASC work 页可回链。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
