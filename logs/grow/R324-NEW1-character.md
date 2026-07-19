---
round: 324
date: 2026-07-19
type_round: 17
phase: "2.1"
current_type: character
gene: NEW1
pages: [john-mangles]
result: success
---

# GROW 2.1-B · R324 · NEW1 · character — 建 John Mangles（Duncan 号年轻船长）

## 执行摘要

Phase 2.1-B character 第 14 建（type_round 17），消费 R322 第三批 discover 队列**建序 64**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**John Mangles**（*In Search of the Castaways*）——游艇 *Duncan* 之年轻船长，初以「John Mangles, the captain」引出（SC-001-003）。备航时「had only to attend to her interior arrangements」（SC-005-003）。开篇即预：验鲨腹文书，即辨「This is written in German」（SC-002-021）。航海之能于大风暴中见真章：信其晴雨表，「remained on deck the whole night... every precaution that prudence could suggest」（SC-031-013），最烈处「never left his post, not even to take food」（SC-031-043）；船逼礁石，「did not lose a second in extricating his ship」（SC-031-039），获 Glenarvan 平实之谢「Thank you, John」（SC-032-002）。其人「a prudent captain」（SC-026-017），危局中语带威权（SC-031-036），然待幼者温和——勉 Robert「Your conduct has been worthy of your name」（SC-027-006）。与 [[Mary Grant]] 渐生情愫（SC-027-024/028-007）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-001、affiliation 空、aliases 空。

**10+ distinct solid PN**（SC-001-003/002-021/005-003/026-017/027-006/027-024/028-007/031-013/031-036/031-039/031-043/032-002）：均 solid，逾门。

**查重**：exact-slug john-mangles filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Mary Grant]]（R323 既建）、[[Lord Glenarvan]]（R320 既建）、[[In Search of the Castaways]]（work）——三链均存在无悬挂。Robert Grant 纯文本。SC 簇壮大（glenarvan/paganel/ayrton/mary-grant/john-mangles 五页互链）。

prose-gate：add_page 初稿 0 超段。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未剥离）。

character 计数 28→**29**，registry total 1552→**1553**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=5>0、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=5>0，按既有实践走 NEW1 消费建序 64。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| john-mangles | pfzqIr | In Search of the Castaways | supporting | SC-001 | 10+ distinct | 船长-航海-风暴-Mary 情愫单指；SC 2-char 无 Note；strict 首过 ✓；[[Mary Grant]]/[[Lord Glenarvan]]/work 互链 |

- **john-mangles**：10+ distinct solid PN；aliases 空；character-schema 五 H2。add_page rev pfzqIr。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 John Mangles 船长-航海-情愫因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：10+ solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1553 character 29 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Mary Grant/Lord Glenarvan/In Search of the Castaways 三链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R325 起始计数）

| 字段 | R324 起始 | R325 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 324 | 325 |
| type_round | 16 | 17 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 260 | 261 |
| last_updated_round | 324 | 325 |

## 遗留问题

1. **character 页数 29**：本轮 +1（john-mangles）。queue(character) 5→**4**（建序 64 消费；余 65-68：mcnabbs/thalcave/nadia/ivan-ogareff）。registry 全库 **1553**，unknown 0。
2. **下轮 R325 = NEW1（§3(7)）**：since_evv5=6<10；queue(character)=4>0 → §3(7) NEW1，消费建序 65（mcnabbs）。Major McNabbs（book In Search of the Castaways，pn_anchor SC-001，role supporting，SC 2-char 无 Note）——Glenarvan 之表兄少校、沉稳冷静，167 mentions；与既建 glenarvan/mary-grant/john-mangles 同书可互链。
3. **SC 簇壮大**：glenarvan/paganel/ayrton/mary-grant/john-mangles 五页；建序 65-66（McNabbs/Thalcave）建成后成六七页大群。
4. **EVV5 下次约 R328**（since_evv5 于 R318 复位，+10）——预计落于消费建序 68 前后；届时 §3(1b) EVV5 反射轮优先。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=260→261（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
