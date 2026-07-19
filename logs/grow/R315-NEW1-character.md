---
round: 315
date: 2026-07-19
type_round: 8
phase: "2.1"
current_type: character
gene: NEW1
pages: [neb]
result: success
---

# GROW 2.1-B · R315 · NEW1 · character — 建 Neb（Cyrus Harding 之忠仆、Lincoln 岛第五殖民者）

## 执行摘要

Phase 2.1-B character 类型第 7 建（type_round 8），消费 R314 第二批 discover 队列**建序 57**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Neb**（*The Mysterious Island* 五殖民者之忠仆）——engineer [[Cyrus Harding]] 之仆。闻主被囚 Richmond，毫不迟疑离 Massachusetts、冒死二十次潜入围城寻主（MI-002-011）；随主所往（MI-002-036），与水手 [[Pencroft]] 同司炊事（MI-012-071）。气球坠岛、Harding 没于浪中，Neb 悲恸逾恒（MI-003-020），红眼泣尽绝望（MI-005-034）、彻夜徘徊海滩（MI-005-066），然拒弃搜寻直至亲眼见亲手触主之遗体（MI-006-006）——终跪见 Harding 卧草榻犹生（MI-007-079）。其忠至死：若非 Top 寻得主人，彼「would have buried my master, and then have lain down on his grave to die」（MI-008-017）；「the Negro Neb」乃殖民地情感核心、命运系于 Harding（MI-004-001）。

**role=supporting**。book=The Mysterious Island、first_appearance=MI-002。affiliation 空。aliases 空。

**10 distinct solid PN**（MI-002×2/003/004/005×2/006/007/008/012）：002-011、002-036、003-020、004-001、005-034、005-066、006-006、007-079、008-017、012-071。

**查重**：exact-slug neb + 变体（nab）filesystem ABSENT；registry type=character 无命中。

**MI 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇内互链首用）**：[[The Mysterious Island]]（work）、[[Cyrus Harding]]（R 既建）、[[Pencroft]]（R311）、[[Herbert]]（R312）——四链均存在无悬挂。Gideon Spilett 纯文本（建序 58 待建）。

prose-gate：初稿 0 超段。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

character 计数 21→**22**，registry total 1545→**1546**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6>0、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover 本轮=1（R314 SCN28 刚复位 0，本轮 +1），queue(character)=6>0，按既有实践走 NEW1 消费。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| neb | rp3Fmp | The Mysterious Island | supporting | MI-002 | 10 distinct | 忠仆-寻主不懈-殖民者单指；MI 2-char 无 Note；strict 首过 ✓；同书簇互链 [[Cyrus Harding]]/[[Pencroft]]/[[Herbert]] |

- **neb**：10 distinct solid PN；aliases 空；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Neb 忠仆-寻主-殖民因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：10 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MI 2-char 无 Note。✔
- **registry 一致**：total 1546 character 22 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：work/Cyrus Harding/Pencroft/Herbert 四链存在无悬挂；Spilett 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R316 起始计数）

| 字段 | R315 起始 | R316 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 315 | 316 |
| type_round | 7 | 8 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 251 | 252 |
| last_updated_round | 315 | 316 |

## 遗留问题

1. **character 页数 22**：本轮 +1（neb）。queue(character) 6→**5**（建序 57 消费；余 58-62：gideon-spilett/negoro/hercules/glenarvan/michel-strogoff）。registry 全库 **1546**，unknown 0。
2. **下轮 R316 = NEW1（§3(7)）**：since_evv5=8<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 58（gideon-spilett）。Gideon Spilett（book The Mysterious Island，pn_anchor MI-002，MI 2-char 无 Note）——New York Herald 战地记者、Lincoln 岛殖民者，冷静善射兼医护；与 neb/cyrus-harding/pencroft/herbert 同书可互链。
3. **同书簇互链推进**：neb 首用 MI 簇内 [[Cyrus Harding]]/[[Pencroft]]/[[Herbert]] 链。建序 58 gideon-spilett 建成后，MI 五殖民者（Harding/Pencroft/Herbert/Neb/Spilett）全数成页，可回填早期页（如 cyrus-harding）交叉链、成完整簇。
4. **EVV5 临近**：since_evv5=8，距阈值 10 尚 2 轮 → 约 R318 触发 §3(1) EVV5。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
8. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理。
9. **corpus-discover 顺延**：since_corpus=251→252（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
