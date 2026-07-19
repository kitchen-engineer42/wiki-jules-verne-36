---
round: 309
date: 2026-07-19
type_round: 2
phase: "2.1"
current_type: character
gene: NEW1
pages: [ayrton]
result: success
---

# GROW 2.1-B · R309 · NEW1 · character — 建 Ayrton（Britannia 叛徒舵手 Ben Joyce，Tabor 岛放逐赎罪、Lincoln 岛第六殖民者）

## 执行摘要

Phase 2.1-B character 类型第 2 建（type_round 2），消费 R307 discover 队列**建序 52**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；since_discover=1<10、全局 queue≥10 → §3(3) 否；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Ayrton**（跨作品角色，SC 叛徒 → MI 赎罪殖民者）——*In Search of the Castaways* 中初为 Britannia 三桅船雇之舵手 Tom Ayrton（SC-033-052），对 Glenarvan 认「Yes, it was I」自称 Scotchman（SC-033-004）、述 Britannia 太平洋航程（SC-033-041），实为囚犯 Ben Joyce 率匪徒叛探险队（MI-039-057）。Glenarvan 罚其孤悬 Tabor 岛、许「罪愆既赎方来接」（MI-041-016）；数年后 Lincoln 岛殖民者寻获（已沦野人 MI-039-050、点明「Ayrton was a traitor」MI-039-054），复其理性与honesty，成第六殖民者；Duncan 号终至，Ayrton 识其昔日所乘之艇（MI-043-018）。

**role=supporting**（MI 赎罪殖民者；SC 中为 antagonist，取 book=MI 语境 supporting）。**跨作品 book=The Mysterious Island**（最详赎罪弧 + 24 章复现最多；正文引 SC 源起 SC-033-004/041/052，对齐 captain-nemo book=TTLU 引 MI、robur book=RC 引 MW 先例）。first_appearance=MI-039。affiliation 空（叛徒/孤客，无稳定组织身份）。

**8 distinct solid PN**（MI-039/041/043 + SC-033）：MI-039-050/039-054/039-057、041-016、043-018、SC-033-004/033-041/033-052。

**查重**：exact-slug ayrton + 变体（tom-ayrton/ben-joyce）filesystem ABSENT；registry alias 无 character 页命中（tabor-island-castaway 为 event 页，别线，剔）。

**MI 3-char / SC 2-char VVV**：均非 4-char，**无需 RFC-0003 Note**。

**wikilink**（4 链全存在，无悬挂）：[[the-mysterious-island]]、[[in-search-of-the-castaways]]、[[lincoln-island]]、[[cyrus-harding]]。Glenarvan/Captain Grant 无页 → 纯文本（不造死链）。

prose-gate：初稿 Overview（421）+ Role 二段（503、426）三段超门，各拆一次后 0 超段。add_page 一次成型（rev HQHOEl，size 2716），quality 自动 featured。**pn_validator --mode strict ✓**。

character 计数 16→17，registry total 1540→**1541**，unknown 恒 0。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| ayrton | HQHOEl | The Mysterious Island | supporting | MI-039 | 8 distinct | 叛徒-放逐-赎罪-第六殖民者单指；跨作品 book=MI 正文引 SC 源起；剔 event tabor-island-castaway；MI/SC 无需 Note；链 4 页；strict ✓ |

- **ayrton**：8 distinct solid PN（MI-039/041/043 + SC-033）；aliases [Tom Ayrton, Ben Joyce]；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ayrton 叛徒-赎罪弧；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 3 段超门（421/503/426），各拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（MI+SC 跨作品），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role；MI/SC 非 4-char 无 Note。✔
- **registry 一致**：total 1541 character 17 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry alias 无 character 页冲突。✔
- **wikilink 完整性**：4 链全存在，无悬挂；Glenarvan/Grant 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R310 起始计数）

| 字段 | R309 起始 | R310 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 309 | 310 |
| type_round | 1 | 2 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 245 | 246 |
| last_updated_round | 309 | 310 |

## 遗留问题

1. **character 页数 17**：本轮 +1（ayrton）。queue(character) 5→**4**（建序 52 消费；余 53-56：dick-sand/pencroft/herbert/paganel）。registry 全库 **1541**，unknown 0。
2. **下轮 R310 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；since_discover=2<10 且全局 queue≥10 → §3(3) 否；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 53（dick-sand）。dick-sand DSCF 4-char VVV → 页首加 RFC-0003 Note；Pilgrim 号临危掌舵之十五岁船长；剔 event wreck-of-the-pilgrim 别线。
3. **跨作品角色 book 计数**：ayrton 为跨作品 book 单值填主作品 + 正文引他作之第 5 例（累计 captain-nemo/robur/gun-cotton/the-moon + ayrton）。schema EVV6 定稿：累积 ≥5 例再评估多值 book 字段 RFC——**本例达阈值，记 HK 观察：多值 book RFC 可评估**（parked，勿自主 file）。
4. **character 候选池充沛**：现 17 页，首批 6（建序 51-56）余 4；queue(character) 降至 <10 已成立（=4）→ **下轮起 §3(3) SCN28 条件「queue<10」已满足**，惟 §3 优先级 7 NEW1 在 queue>0 时仍先于消费；待 queue(character)==0 触发 §3(4) zombie re-scan 或 since_discover≥10 触发 §3(3) 补队列。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）**新增**：跨作品多值 book 字段 RFC（达 5 例阈值，见 §3）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
8. **corpus-discover 顺延**：since_corpus=245→246（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（五类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
