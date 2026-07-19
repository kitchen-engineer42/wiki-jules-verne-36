---
round: 312
date: 2026-07-19
type_round: 5
phase: "2.1"
current_type: character
gene: NEW1
pages: [herbert]
result: success
---

# GROW 2.1-B · R312 · NEW1 · character — 建 Herbert（Lincoln 岛五殖民者之少年博物学者、Pencroft 义子）

## 执行摘要

Phase 2.1-B character 类型第 5 建（type_round 5），消费 R307 discover 队列**建序 55**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；discover_streak_low=0<3；queue(character)=2>0 → §3(3) 走 NEW1 消费；§3(4) zombie 否；stub%=0 → §3(7) NEW1）。

**Herbert Brown**（*The Mysterious Island* 五殖民者之最年少）——New Jersey 十五岁、船长遗孤，随水手 Pencroft、彼爱如己出（MI-002-021）。gallant 且博物诸学早熟、于共同事业贡献良多（MI-013-006），水手可倚之——精于博物学、久怀热忱（MI-004-014）。恒守挚爱之 Natural History、为同伴辨识岛上动植（MI-012-053），渐成善射、以首枪自豪（MI-047-037）。历险中大勇兼「the reasoning of bravery」之镇定（MI-023-036）；剿匪之役中弹重伤（MI-049-082），继患间歇沼热、Gideon Spilett 守其榻不离（MI-052-028），终获救、热退还生（MI-050-009）。与义父 Pencroft 情深——彼拥「Herbert, his boy」难抑其情（MI-045-011）。

**role=supporting**。book=The Mysterious Island、first_appearance=MI-002。affiliation 空。aliases [Herbert Brown]。

**10 distinct solid PN**（MI-002/004/012/013/023/045/047/049/050/052）：002-021、004-014、012-053、013-006、023-036、045-011、047-037、049-082、050-009、052-028。

**查重**：exact-slug herbert + 变体（herbert-brown/herbert-the-boy）filesystem ABSENT；registry alias/label 无 herbert 命中。

**MI 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[The Mysterious Island]]（work 页存在）。Pencroft（本轮 R311 已建页，但正文以纯文本引名未加链——保守；下轮可回填 [[Pencroft]] 链）/Gideon Spilett/Cyrus Harding/Neb 纯文本。

prose-gate：初稿 0 超段（Relationships bullet-list 属列表非散文段）。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

character 计数 19→**20**，registry total 1543→**1544**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2>0 → NEW1 消费 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *§3(3) queue<10 成立（=2），但按既有轮实践（R308-311 同）：queue>0 优先 NEW1 消费；queue==0 或 since_discover≥10 方 discover。判 NEW1。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| herbert | OEF6NH | The Mysterious Island | supporting | MI-002 | 10 distinct | 少年博物学者-义子-中弹濒死单指；MI 2-char 无 Note；strict 首过 ✓；链 work 页；Pencroft/Spilett/Harding/Neb 纯文本 |

- **herbert**：10 distinct solid PN；aliases [Herbert Brown]；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Herbert 博物-勇气-伤病因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：10 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role/quality；MI 2-char 无 Note。✔
- **registry 一致**：total 1544 character 20 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry 无 herbert alias/label 冲突。✔
- **wikilink 完整性**：work 链存在，无悬挂；Pencroft/Spilett/Harding/Neb 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R313 起始计数）

| 字段 | R312 起始 | R313 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 312 | 313 |
| type_round | 4 | 5 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 248 | 249 |
| last_updated_round | 312 | 313 |

## 遗留问题

1. **character 页数 20**：本轮 +1（herbert）。queue(character) 2→**1**（建序 55 消费；余 56：paganel）。registry 全库 **1544**，unknown 0。
2. **下轮 R313 = NEW1（§3(7)）**：since_evv5=5<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费**末位建序 56（paganel）**。paganel / Jacques Paganel（book In Search of the Castaways，pn_anchor SC-006，SC 2-char 无 Note）——地理学者、健忘博学之喜剧角色，*In Search of the Castaways* 群像核心。
3. **建序 56 为 R307 队列末位**：R313 消费后 **queue(character)→0**，R314 触发 §3(4) **SCN28-zombie re-scan** 补 character 候选（MI 余殖民者 Nab/Gideon Spilett/Cyrus Harding、SC 群像 Glenarvan/Mary Grant、Michel Strogoff/Servadac/Kaw-djer/Mathias Sandorf 等主角池深）。
4. **wikilink 回填候选（低优）**：herbert 正文以纯文本引 Pencroft（R311 已建页）。可择机回填 [[Pencroft]]；本轮保守未链，无死链风险。
5. **edit_page 剥离 quality 教训（通用，已入 memory）**：本轮纯 add_page 无 edit，无涉。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
9. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理；本轮页 herbert featured 正常。
10. **corpus-discover 顺延**：since_corpus=248→249（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
