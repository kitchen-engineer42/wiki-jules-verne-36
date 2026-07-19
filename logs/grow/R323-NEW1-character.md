---
round: 323
date: 2026-07-19
type_round: 16
phase: "2.1"
current_type: character
gene: NEW1
pages: [mary-grant]
result: success
---

# GROW 2.1-B · R323 · NEW1 · character — 建 Mary Grant（Captain Grant 之女、随 Duncan 号寻父）

## 执行摘要

Phase 2.1-B character 第 13 建（type_round 16），消费 R322 第三批 discover 队列**建序 63**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Mary Grant**（*In Search of the Castaways*）——失踪船长 Grant 之幼女。十四岁沦孤，「resolved to face her situation bravely, and to devote herself entirely to her little brother」（SC-004-007）；述其悲史「in so simple and unaffected a manner」，未尝自视为英雌（SC-004-011）。至 Malcolm Castle 跪 [[Lord Glenarvan]] 前（SC-004-025），Lady Helena 引见「Miss Mary Grant and her brother, the two children condemned to orphanage」（SC-004-027）。受助时自答「we'll both go together」（SC-004-033）；Duncan 号上为恩人祈祷、感泣（SC-005-015）；长搜中「nerved herself to the resolution never to utter the name of her father」（SC-046-002）。少校赞「That Mary Grant must be a brave girl」（SC-004-015）；护弟情深——Robert 临险，其「in an agony of terror, speechless」伸臂向之（SC-040-055）。与 John Mangles 渐生情愫（SC-027-024/028-007）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-004、affiliation 空、aliases 空。

**10 distinct solid PN**（SC-004×5/005/027/028/040/046）：004-007、004-011、004-015、004-025、004-027、004-033、005-015、027-024、028-007、040-055、046-002 —— 计 11 distinct（grep 去重 10；034-020 于 Relationships-Captain Grant bullet 另引，实际页内 SC 引注含 034-020 亦有效）。核对：strict 校验计入全部。

**查重**：exact-slug mary-grant filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Lord Glenarvan]]（R320 既建）、[[In Search of the Castaways]]（work）——二链均存在无悬挂。John Mangles/Captain Grant/Robert Grant/Lady Helena/McNabbs 纯文本（未建；John Mangles/McNabbs 已在 R322 队列 建序 64/65 待建，建后可回填互链）。

prose-gate：add_page 初稿 1 段超门（436，Overview 二段）→ 建前 /tmp 拆为两段 → 0 超门。**pn_validator strict 首过 ✓**（无角色页 edit_page，quality featured 未剥离）。

character 计数 27→**28**，registry total 1551→**1552**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6>0、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=6>0，按既有实践走 NEW1 消费建序 63。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| mary-grant | O5ZNRB | In Search of the Castaways | supporting | SC-004 | 10+ distinct | 孤女-寻父-护弟-Mangles 情愫单指；SC 2-char 无 Note；初稿 1 段 436 超门→拆段→0 超；strict 首过 ✓；[[Lord Glenarvan]]/work 互链 |

- **mary-grant**：10 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev O5ZNRB。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Mary Grant 孤女-寻父-护弟因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：初稿 1 段 436 → 拆段后 0 超门。✔
- **G3 ≥5 distinct PN**：10 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1552 character 28 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Lord Glenarvan/In Search of the Castaways 二链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R324 起始计数）

| 字段 | R323 起始 | R324 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 323 | 324 |
| type_round | 15 | 16 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 259 | 260 |
| last_updated_round | 323 | 324 |

## 遗留问题

1. **character 页数 28**：本轮 +1（mary-grant）。queue(character) 6→**5**（建序 63 消费；余 64-68：john-mangles/mcnabbs/thalcave/nadia/ivan-ogareff）。registry 全库 **1552**，unknown 0。
2. **下轮 R324 = NEW1（§3(7)）**：since_evv5=5<10；queue(character)=5>0 → §3(7) NEW1，消费建序 64（john-mangles）。John Mangles（book In Search of the Castaways，pn_anchor SC-001，role supporting，SC 2-char 无 Note）——Duncan 号年轻船长，272 mentions 富矿；与既建 glenarvan/mary-grant 同书可互链（并可回填 mary-grant 之 John Mangles 悬钩）。
3. **SC 簇持续深化**：glenarvan/paganel/ayrton/mary-grant 四页；建序 64-66（Mangles/McNabbs/Thalcave）建成后 SC 簇成大群，回链密度提升。
4. **EVV5 下次约 R328**（since_evv5 于 R318 复位，+10）——预计落于消费建序 68 前后；届时 §3(1b) EVV5 反射轮优先。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=259→260（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
