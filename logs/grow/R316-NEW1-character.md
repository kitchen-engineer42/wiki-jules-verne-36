---
round: 316
date: 2026-07-19
type_round: 9
phase: "2.1"
current_type: character
gene: NEW1
pages: [gideon-spilett]
result: success
---

# GROW 2.1-B · R316 · NEW1 · character — 建 Gideon Spilett（New York Herald 战地记者、Lincoln 岛殖民者）

## 执行摘要

Phase 2.1-B character 类型第 8 建（type_round 9），消费 R314 第二批 discover 队列**建序 58**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Gideon Spilett**（*The Mysterious Island* 五殖民者之一）——New York Herald 战地记者、Lincoln 岛殖民地之史官。属 Stanley 一流不屈之英美纪事者，为得确讯无所不至（MI-002-005）；十年间任 New York Herald 记者，以书信与素描丰之，笔铅二技俱精（MI-002-008）。与 engineer [[Cyrus Harding]] 同囚 Richmond，闻气球脱逃计划毫不迟疑加入（MI-002-036）。殖民地命名地物，皆由其记录成岛之地理名录（MI-011-062）；风暴将至犹抱臂立于海滩凝望大海（MI-007-001）；Harding 半溺获救，彼久察而后起（MI-008-007）。记者本能不离：观海鸟过而思末书是否托彼寄 New York Herald（MI-035-031）。善射，持射程近一英里之来复枪（MI-045-004）；兼司医护，历生平诸变而略通医术（MI-049-014），[[Herbert]] 重伤时与 Harding 竭力如良医之所为（MI-049-048）；随犬 Top 入林、枪备待发蔽身树后，不倦而警（MI-051-033）。

**role=supporting**。book=The Mysterious Island、first_appearance=MI-002。affiliation 空。aliases 空。

**11 distinct solid PN**（MI-002×3/007/008/011/035/045/049×2/051）：002-005、002-008、002-036、007-001、008-007、011-062、035-031、045-004、049-014、049-048、051-033。

**查重**：exact-slug gideon-spilett + 变体（spilett/gideon）filesystem ABSENT；registry type=character 无命中（pages.json 命中皆 chapter 页描述文本，非实体页）。

**MI 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇内互链）**：[[The Mysterious Island]]（work）、[[Cyrus Harding]]、[[Pencroft]]、[[Herbert]]、[[Neb]]——五链均存在无悬挂。**MI 五殖民者（Harding/Pencroft/Herbert/Neb/Spilett）全数成页，簇完整。**

prose-gate：add_page 初稿 3 段 over-400（456/488/456），edit_page 拆分为短段后 **over-400=0**（rev 8lbIXJ→aNCfka，2851→2814）。**pn_validator strict 首过 ✓**（edit 后复验仍 ✓，quality featured 于 /tmp 重申未被剥离）。

character 计数 22→**23**，registry total 1546→**1547**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=5>0、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=5>0，按既有实践走 NEW1 消费。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| gideon-spilett | aNCfka | The Mysterious Island | supporting | MI-002 | 11 distinct | 记者-史官-善射-医护单指；MI 2-char 无 Note；初稿 3 over-400→拆分 0；strict 首过 ✓；MI 五殖民者簇成 |

- **gideon-spilett**：11 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev 8lbIXJ→edit_page 拆段 rev aNCfka。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Spilett 记者-史官-善射-医护因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：初稿 3 超门（456/488/456）→ edit_page 拆分后 0 超门。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page + edit_page，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MI 2-char 无 Note。✔
- **registry 一致**：total 1547 character 23 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：work/Cyrus Harding/Pencroft/Herbert/Neb 五链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R317 起始计数）

| 字段 | R316 起始 | R317 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 316 | 317 |
| type_round | 8 | 9 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 252 | 253 |
| last_updated_round | 316 | 317 |

## 遗留问题

1. **character 页数 23**：本轮 +1（gideon-spilett）。queue(character) 5→**4**（建序 58 消费；余 59-62：negoro/hercules/glenarvan/michel-strogoff）。registry 全库 **1547**，unknown 0。
2. **下轮 R317 = NEW1（§3(7)）**：since_evv5=9<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 59（negoro）。Negoro（book Dick Sand, A Captain at Fifteen，pn_anchor DSCF-002，**role=antagonist**）——阴险葡籍船厨，篡改罗盘诱船入非洲之反派；DSCF 4-char VVV **须 RFC-0003 Note**。
3. **MI 五殖民者簇完整**：Harding/Pencroft/Herbert/Neb/Spilett 全数成页。可回填早期页（如 cyrus-harding）交叉链、成完整簇（DEFERRED，非本轮动作）。
4. **EVV5 临近**：since_evv5=9，距阈值 10 尚 1 轮 → **R318 触发 §3(1) EVV5**（模板演化评审轮）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0（初稿 3 超已拆分）。
8. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理。
9. **corpus-discover 顺延**：since_corpus=252→253（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
