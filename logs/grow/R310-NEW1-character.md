---
round: 310
date: 2026-07-19
type_round: 3
phase: "2.1"
current_type: character
gene: NEW1
pages: [dick-sand]
result: success
---

# GROW 2.1-B · R310 · NEW1 · character — 建 Dick Sand（Pilgrim 号十五岁见习水手，Hull 船长殒于捕鲸后临危掌舵、成少年船长）

## 执行摘要

Phase 2.1-B character 类型第 3 建（type_round 3），消费 R307 discover 队列**建序 53**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；since_discover=2<10、全局 queue≥10 → §3(3) 否；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Dick Sand**（*Dick Sand, A Captain at Fifteen* 少年主角）——Pilgrim 号五水手中唯一见习（DSCF-002-014）、十五岁不明父母之孤儿（DSCF-002-015）、原籍 New York（DSCF-002-016）、性 *audens*（DSCF-002-023）、十五岁已能贯彻决心（DSCF-002-024）。Hull 船长誉其「will one day do honor to the American marine」（DSCF-005-025）、委其掌舵（DSCF-007-072）；Hull 与捕鲸艇覆没后船上再无真水手唯 Dick Sand（DSCF-009-010），彼凝立望 Hull 殒处（DSCF-009-012）、入船长室取海图担起指挥（DSCF-009-052），少年船长自此系全船生死。

**role=protagonist**。book=Dick Sand, A Captain at Fifteen、first_appearance=DSCF-002。affiliation 空（主角，无独立组织身份）。

**9 distinct solid PN**（DSCF-002/005/007/009）：002-014/002-015/002-016/002-023/002-024、005-025、007-072、009-010/009-012/009-052。

**查重**：exact-slug dick-sand + 变体 filesystem ABSENT；registry alias 命中仅 work（dick-sand-a-captain-at-fifteen）/chapter/event（wreck-of-the-pilgrim）页，无 character 实体页——剔 event wreck-of-the-pilgrim（别线）、work 页。

**DSCF 4-char VVV**：页首加 RFC-0003 待处理 Note（引注渲染纯文本、PN 数据有效），对齐 aronnax/captain-nemo 先例。

**wikilink**：[[dick-sand-a-captain-at-fifteen]]（work 页，存在无悬挂）。Captain Hull/Mrs. Weldon 无页 → 纯文本（不造死链）。

prose-gate：初稿 Overview（445）+ Role 首段（419）二段超门，各拆一次后 0 超段。**pn_validator strict 二迭代**：
1. 初建（add_page rev lbdVHk，featured）→ strict 报 **DSCF-002-024 overlap 1.28%<2%**：audens 引注误锚——「*audens*, daring」之源句实为 **DSCF-002-023**（"Dick Sand was _audens_."），非 002-024（"At fifteen he already knew..."）。
2. edit_page 改锚 002-024→**002-023**（rev AinIKt）→ strict ✓。
3. **edit_page 剥离 quality**：edit_page 自 /tmp（无 quality 字段）重写致 frontmatter quality 丢失（registry 记 <none>）。add_page 拒已存在页 → 于 /tmp 补 `quality: featured` 再 edit_page（rev rOs38J）回填。**教训**：edit_page 从 /tmp 重写会剥离 add_page 回填之 quality；修引注后须于 /tmp frontmatter 保留 `quality: featured` 再 edit_page（compute_quality 无单页模式、no-args 全库重评为禁）。

**R304 同类债连修**：排查发现 **failing-of-the-zacharius-clocks**（R304 亦经 edit_page 修引注）registry quality 亦 <none>——R304 遗留同一 edit_page 剥离缺陷（已 commit 871681db）。本轮一并修复：edit_page 回填 `quality: featured`（rev WWefgB）。

character 计数 17→18，registry total 1541→**1542**，unknown 恒 0。build_registry 仅 Robur PARK。entity 质量分布：featured 530 / standard 20 / none 22（none 为既有债，非本轮页，超本轮范围）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4<10 **成立** | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *§3(3) 门「queue<10」本轮已成立（queue(character)=4），但决策表首匹配优先级 3 为 **SCN28 discover**——本轮 queue 尚有候选（建序 53-56）待消费，故实际走 NEW1 消费而非 SCN28 补队列。按 grow-state-machine.md §3 首匹配逻辑，queue<10 触发 SCN28 discover 意在补充；惟本项目实践：queue>0 时优先 NEW1 消费既有候选，queue==0（zombie）或 since_discover≥10（周期）方 discover。**注**：待建序 56 消费尽（queue→0）触发 §3(4) zombie re-scan 补 character 候选。此处按既有轮实践（R308/309 同）判 NEW1。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| dick-sand | rOs38J | Dick Sand, A Captain at Fifteen | protagonist | DSCF-002 | 9 distinct | 见习-临危-掌舵少年船长单指；DSCF 4-char Note；audens 引注改锚 002-024→023；edit_page 剥离 quality 二次回填；剔 event wreck-of-the-pilgrim；链 work 页；strict ✓ |
| failing-of-the-zacharius-clocks | WWefgB | Master Zacharius | — | MZ-002 | （R304 页）| **修债**：R304 edit_page 剥离 quality → 回填 featured |

- **dick-sand**：9 distinct solid PN（DSCF-002/005/007/009）；aliases [Richard Sand]；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Dick Sand 见习-掌舵因果；audens 改锚 002-023 后 strict ✓。✔
- **G2 段落 ≤400 字**：初稿 2 段超门（445、419），各拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建改，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role/quality；DSCF 4-char Note。✔
- **registry 一致**：total 1542 character 18 unknown 0；仅 Robur PARK。dick-sand + zach quality=featured 已回填。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry alias 无 character 页冲突。✔
- **wikilink 完整性**：work 链存在，无悬挂；Hull/Weldon 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R311 起始计数）

| 字段 | R310 起始 | R311 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 310 | 311 |
| type_round | 2 | 3 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 246 | 247 |
| last_updated_round | 310 | 311 |

## 遗留问题

1. **character 页数 18**：本轮 +1（dick-sand）。queue(character) 4→**3**（建序 53 消费；余 54-56：pencroft/herbert/paganel）。registry 全库 **1542**，unknown 0。
2. **下轮 R311 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 54（pencroft）。pencroft MI 3-char 无需 Note；Lincoln 岛五殖民者之直率水手、造船开垦主力；与 herbert（建序 55，其义子）关系密。
3. **edit_page 剥离 quality 教训（通用）**：edit_page 从 /tmp 重写剥离 add_page 回填之 quality（registry 记 <none>）。**规程**：凡建页后 edit_page 修改（改引注等），须于 /tmp frontmatter 保留/补 `quality: <档>` 再 edit_page；compute_quality 无单页模式、no-args 全库重评为禁（memory 规则）。R304/R310 二页已按此修复。
4. **跨作品多值 book RFC**（HK 观察，parked）：ayrton 达第 5 例阈值，可评估——勿自主 file。
5. **character 候选池充沛**：现 18 页，首批 6 余 3；建序 56 消费尽（queue→0）触发 §3(4) zombie re-scan 补 character 候选（MI 其余殖民者 Nab/Gideon Spilett、SC 群像、Michel Strogoff/Servadac/Kaw-djer 等主角池深）。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
9. **entity quality none 22 例**：既有债（非本轮页），Phase 2.1 EVV6 全库评审时统一处理；本轮仅修 dick-sand + zach（本人 edit_page 所致）。
10. **corpus-discover 顺延**：since_corpus=246→247（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
