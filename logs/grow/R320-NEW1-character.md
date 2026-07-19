---
round: 320
date: 2026-07-19
type_round: 13
phase: "2.1"
current_type: character
gene: NEW1
pages: [glenarvan]
result: success
---

# GROW 2.1-B · R320 · NEW1 · character — 建 Lord Glenarvan（Duncan 号船主、寻 Grant 探险队领袖）

## 执行摘要

Phase 2.1-B character 类型第 11 建（type_round 13），消费 R314 第二批 discover 队列**建序 61**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Lord Edward Glenarvan**（*In Search of the Castaways* 主角）——苏格兰贵族、游艇 *Duncan* 之主，其航行驱动全书。鲨腹得瓶，Glenarvan 坚主查验，知海中瓶常藏珍贵文书（SC-001-021）；*Duncan* 乃其私人游艇、所泊皆众目焦点（SC-005-014）。由残信立志：陈述过于明确，英国断不会迟疑援其三个流落荒岸之子（SC-002-081）。果决之人：破译文书即别娇妻、跃上驶往 Glasgow 之快车备船（SC-002-084）；越 pampas 守搜寻之诺，言「we'll find him — Thalcave has set us on the track」并深信之（SC-018-042）。领袖能凝众御险：困于洪泛之树开庄严之议（SC-023-068）；澳洲途中定谁为信使（SC-042-091）。其勇系于对妻之爱：Maori 中为免 Lady Helena 受女巫扰，径趋酋长 Kai-Koumou（SC-055-011）。其大错生于慷慨之信任：托事于水手长 [[Ayrton]]、简言「I will trust to you, Ayrton」（SC-063-036）；纵遭背叛犹守信——「you have kept your word, and I will keep mine」（SC-063-071）。

**role=protagonist**。book=In Search of the Castaways、first_appearance=SC-001。affiliation 空。aliases=[Edward Glenarvan]（label 唯一性校验通过，无新 alias 冲突）。

**11 distinct solid PN**（SC-001/002×2/005/018/023×2/042/055/063×2）：001-021、002-081、002-084、005-014、018-042、023-068、023-109、042-091、055-011、063-036、063-071。

**查重**：exact-slug glenarvan filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇内互链）**：[[In Search of the Castaways]]（work）、[[Ayrton]]（建序 52 既建）、[[Paganel]]（R313 既建）——三链均存在无悬挂。Lady Helena/Mary Grant/McNabbs/Captain Grant/Thalcave 纯文本（未建）。**SC 簇渐成**（glenarvan/paganel/ayrton 三页互链）。

prose-gate：add_page 初稿 0 超段。**pn_validator**：初稿 SC-018-042 于 Relationships-Paganel bullet 误引（该 PN 述 Glenarvan+Thalcave，与 Paganel 断言 0% 重叠）→ edit_page 改引 **SC-023-109**（Paganel 呼「looking for Captain Grant where he is not to be found」，词汇契合）→ **strict 复验全过 ✓**（rev zLHX1O→W8REAw，quality featured 于 /tmp 重申未剥离）。

character 计数 25→**26**，registry total 1549→**1550**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2>0、since_discover=5 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| glenarvan | W8REAw | In Search of the Castaways | protagonist | SC-001 | 11 distinct | Duncan 船主-探险领袖-信任 Ayrton 单指；SC 2-char 无 Note；初引 PN 误配→改 SC-023-109 strict 复过 ✓；[[Ayrton]]/[[Paganel]]/work 互链 |

- **glenarvan**：11 distinct solid PN；aliases=[Edward Glenarvan]；character-schema 五 H2。add_page rev zLHX1O→edit_page 修 PN rev W8REAw。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Glenarvan 领袖-搜寻-信任因果；初稿 1 PN 误配已修，strict 复过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page + edit_page，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1550 character 26 unknown 0；仅 Robur PARK；无新 alias 冲突。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：In Search of the Castaways/Ayrton/Paganel 三链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R321 起始计数）

| 字段 | R320 起始 | R321 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 320 | 321 |
| type_round | 12 | 13 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 256 | 257 |
| last_updated_round | 320 | 321 |

## 遗留问题

1. **character 页数 26**：本轮 +1（glenarvan）。queue(character) 2→**1**（建序 61 消费；余 62：michel-strogoff）。registry 全库 **1550**，unknown 0。
2. **下轮 R321 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费**队列末条建序 62**（michel-strogoff）。Michel Strogoff（book Michel Strogoff，pn_anchor MS-004，**role=protagonist**，MS 2-char 无 Note）——沙皇信使，穿越西伯利亚送密令；单作品主角，暂无同书已建角色互链。
3. **queue 归零预警**：R321 消费建序 62 后 queue(character)→**0** → **R322 触发 §3(3)/§3(4) SCN28 第三批 discover** 补给。深池仍充沛：SC 群像（Mary Grant/Robert Grant/John Mangles/McNabbs/Thalcave/Captain Grant）、DSCF 余角（Mrs. Weldon/Cousin Benedict/Tom）、单作品主角（Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz 等）。
4. **SC/DSCF/MI 簇渐成**：SC（glenarvan/paganel/ayrton）、DSCF（dick-sand/negoro/hercules）、MI 五殖民者全建。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=256→257（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
