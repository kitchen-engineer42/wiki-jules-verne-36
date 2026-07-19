---
round: 311
date: 2026-07-19
type_round: 4
phase: "2.1"
current_type: character
gene: NEW1
pages: [pencroft]
result: success
---

# GROW 2.1-B · R311 · NEW1 · character — 建 Pencroft（Lincoln 岛五殖民者之直率水手、造船开垦主力）

## 执行摘要

Phase 2.1-B character 类型第 4 建（type_round 4），消费 R307 discover 队列**建序 54**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；discover_streak_low=0<3；since_discover=3<10、queue(character)=3>0 → §3(3) 走 NEW1 消费；§3(4) zombie 否；stub%=0 → §3(7) NEW1）。

**Pencroft**（*The Mysterious Island* 五殖民者之一）——三十五至四十岁、体格健壮、饱经日晒之北方美国水手（MI-002-021），航遍七海、大胆无畏、临事不惊之「honest sailor」（MI-009-001）。曾任 Brooklyn 船坞木匠、州船助理裁缝、假日园丁，「like all seamen, fit for anything」（MI-013-008）；Lincoln 岛上为造船主力——Cyrus Harding 令「instead of a house we will build a boat, and Master Pencroft shall be put in command」（MI-014-059），彼五日成小舟（MI-024-001），终喜见全帆战舰随潮下水（MI-034-077），命名 *Bonadventure* 任船长。曾服役捕鲸船故能主持割鲸（MI-032-052）；与义子 Herbert Brown（MI-002-021/002-039）、engineer Cyrus Harding（MI-033-021）情深。

**role=supporting**。book=The Mysterious Island、first_appearance=MI-002。affiliation 空（殖民者，无独立组织身份）。

**10 distinct solid PN**（MI-002/009/013/014/019/024/032/033/034）：002-021、002-039、009-001、013-008、014-059、019-016、024-001、032-052、033-021、034-077。

**查重**：exact-slug pencroft + 变体（pencroff/pencroft-the-sailor/jack-pencroft）filesystem ABSENT；registry alias/label 无 pencroft 命中。

**MI 2-char VVV**：无需 RFC-0003 Note（仅 4-char 码需）。

**wikilink**：[[The Mysterious Island]]（work 页存在）。Herbert Brown/Cyrus Harding/Gideon Spilett/Neb 纯文本（无独立页则不造死链）。

prose-gate：初稿 0 超段（Relationships 三项 bullet-list 合计 425 字属列表非散文段，逐项均 <400，门不计）。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

## R310 遗留 alias 冲突连修

build_registry 报**新** alias conflict：`'Dick Sand' → dick-sand-a-captain-at-fifteen vs dick-sand`——R310 建 dick-sand character 页（label『Dick Sand』）与既有 work 页 dick-sand-a-captain-at-fifteen 之 alias『Dick Sand』撞车（违 LAW §10 label 唯一性）。裸名「Dick Sand」应解析至 character，故本轮从 **work 页剥离 alias『Dick Sand』**（保留『A Captain at Fifteen』），edit_page rev **OM7Vzn**。/tmp frontmatter 保留 `quality: standard`（按 edit_page 剥离教训预置），work quality 未丢。build_registry 复验：仅 Robur PARK，Dick Sand 冲突已消。

character 计数 18→**19**，registry total 1542→**1543**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3>0 → NEW1 消费 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *§3(3) queue<10 本轮成立（queue(character)=3），但按既有轮实践（R308/309/310 同）：queue>0 时优先 NEW1 消费既有候选，queue==0（zombie）或 since_discover≥10 方 discover。此处判 NEW1。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| pencroft | umpBbQ | The Mysterious Island | supporting | MI-002 | 10 distinct | 水手-造船-开垦主力单指；MI 2-char 无 Note；strict 首过 ✓；链 work 页；Herbert/Harding/Spilett/Neb 纯文本 |
| dick-sand-a-captain-at-fifteen | OM7Vzn | — (work) | — | — | （R310 债）| **修债**：剥离 work alias『Dick Sand』（与 R310 character label 冲突 LAW §10）；quality standard 保留 |

- **pencroft**：10 distinct solid PN；aliases 空；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Pencroft 水手-造船因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门（Relationships bullet-list 非散文段）。✔
- **G3 ≥5 distinct PN**：10 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建改，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role/quality；MI 2-char 无 Note。✔
- **registry 一致**：total 1543 character 19 unknown 0；Dick Sand alias 冲突已消，仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry 无 pencroft alias/label 冲突。✔
- **wikilink 完整性**：work 链存在，无悬挂；Herbert/Harding/Spilett/Neb 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R312 起始计数）

| 字段 | R311 起始 | R312 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 311 | 312 |
| type_round | 3 | 4 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 247 | 248 |
| last_updated_round | 311 | 312 |

## 遗留问题

1. **character 页数 19**：本轮 +1（pencroft）。queue(character) 3→**2**（建序 54 消费；余 55-56：herbert/paganel）。registry 全库 **1543**，unknown 0。
2. **下轮 R312 = NEW1（§3(7)）**：since_evv5=4<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 55（herbert）。herbert / Herbert Brown（book The Mysterious Island，pn_anchor MI-002，MI 2-char 无 Note）——Lincoln 岛十五岁少年博物学者、Pencroft 义子，与本轮 pencroft 关系密（MI-002-021/033-021 已引其父子情）。
3. **edit_page 剥离 quality 教训（通用，已入 memory）**：凡建页后 edit_page 修改，须于 /tmp frontmatter 保留/补 `quality: <档>`；本轮 work 页 edit 已按此预置 standard，未丢。R304/R310/R311 三页已验此规程。
4. **跨作品多值 book RFC**（HK 观察，parked）：ayrton 达第 5 例阈值，可评估——勿自主 file。
5. **character 候选池充沛**：现 19 页；建序 56 消费尽（queue→0）触发 §3(4) zombie re-scan 补 character 候选（MI 其余殖民者 Nab/Gideon Spilett/Cyrus Harding、SC 群像、Michel Strogoff/Servadac/Kaw-djer 等主角池深）。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）；（e）**新**：R310 Dick Sand alias 冲突本轮已就地修复（work 页剥离 alias），非 parked。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
9. **entity quality none 22 例**：既有债（非本轮页），Phase 2.1 EVV6 全库评审时统一处理；本轮页 pencroft featured、work 页 standard 均正常。
10. **corpus-discover 顺延**：since_corpus=247→248（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
