---
round: 348
date: 2026-07-19
type_round: 40
phase: "2.1"
current_type: character
gene: NEW1
pages: [dirk-peters]
result: success
---

# GROW 2.1-B · R348 · NEW1 · character — 建 Dirk Peters（化名 Hunt 之 Pym 混血水手；AM 簇配对；第六批建序 83）

## 执行摘要

Phase 2.1-B character 第 33 建（type_round 40），消费 R345 第六批 discover 队列**建序 83**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=5。**

**Dirk Peters**（*An Antarctic Mystery*）——混血水手、Arthur Pym 之忠仆，化名 Hunt 潜行于 _Halbrane_。「a half-breed named Dirk Peters」，正是「whom Captain Len Guy had gone to look for in Illinois」（AM-005-026）；因 Poe「stated explicitly that Dirk Peters would be able to furnish information relating to the non-communicated chapters, and that he lived at Illinois」（AM-004-046）而为 Len Guy 所寻。Poe 前传中曾于 _Grampus_ 哗变「rushed upon the others, seconded by Augustus Barnard, Arthur Pym, and the dog Tiger」（AM-005-043）。

航程大半藏身为沉默水手 Hunt——「distinguished himself by his activity」（AM-013-026），依约「went on in front, as it had been agreed that he was to be our guide」（AM-015-015），且寻得当年「through which Arthur Pym and Dirk Peters had crossed the reef」之隘口（AM-016-017）。伪装终破：叙者录「Hunt was the half-breed Dirk Peters, the devoted companion of Arthur Pym」（AM-017-132），Peters 自陈「He had said, 'I am Dirk Peters.' He was Dirk Peters」（AM-017-139）；其「had hidden himself in the Falklands under the name of Hunt」（AM-017-135）之由，Jeorling 直询「what it was that induced you to reveal it」（AM-018-127）。其人巨力寡言：得寻踪则「suddenly uttered a cry, or rather a sort of savage growl, and held out his enormous hand」（AM-016-054），全身南向以寻故友——投「such a lightning glance from his brilliant hawk-like eyes」向南天（AM-015-031），船上「gaze never quitted the horizon of that southern zone for an instant」（AM-015-042）。

**role=supporting**。book=An Antarctic Mystery、first_appearance=AM-004、affiliation 空、**label=Dirk Peters，aliases=['Hunt']**（Hunt 为其潜行 _Halbrane_ 之化名，AM-017-132 grounding）。

**13 distinct solid PN**（AM-004-046、005-026/043、013-026、015-015/031/042、016-017/054、017-132/135/139、018-127）：均 solid，逾门。

**查重**：exact-slug dirk-peters filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**AM 2-char VVV**：无需 RFC-0003 Note。

**wikilink（AM 簇配对）**：[[Len Guy]]（character，存）+ [[An Antarctic Mystery]]（work，存）——互链无悬挂，AM 簇 len-guy↔dirk-peters 配对成型。Arthur Pym（Poe 主角，未建）暂纯文本，待建后回填（DEFERRED）。

prose-gate：add_page 初稿 3 超段（504、500、465），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 47→**48**，registry total 1571→**1572**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=6>0，按既有实践走 NEW1 消费建序 83。消费后 queue=5。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| dirk-peters | EmIPyC | An Antarctic Mystery | supporting | AM-004 | 13 distinct | Pym 混血水手-化名 Hunt-南航向导-伪装破露；label Dirk Peters + alias Hunt；AM 2-char 无 Note；拆 3 超段；strict 首验通过；互链 [[Len Guy]]/[[An Antarctic Mystery]] |

- **dirk-peters**：13 distinct solid PN；alias ['Hunt']；character-schema 五 H2。add_page rev EmIPyC。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Peters 身份-Hunt 潜行-向导-伪装破露-巨力寻友因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；AM 2-char 无 Note。✔
- **registry 一致**：total 1572 character 48 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Dirk Peters 唯一；alias Hunt 唯一）。✔
- **wikilink 完整性**：Len Guy/An Antarctic Mystery 链存在无悬挂；Arthur Pym 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R349 起始计数）

| 字段 | R348 起始 | R349 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 348 | 349 |
| type_round | 40 | 41 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 284 | 285 |
| last_updated_round | 348 | 349 |

## 遗留问题

1. **character 页数 48**：本轮 +1（dirk-peters）。queue(character) 6→**5**（建序 83 消费）。registry 全库 **1572**，unknown 0。
2. **下轮 R349 = NEW1（§3(7)）**：since_evv5=8<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 84（william-guy）。William Guy（book An Antarctic Mystery，pn_anchor AM-005，role supporting，AM 2-char 无 Note）——失踪 _Jane_ 船长、Len Guy 之兄、全远征救援目标；AM 簇再配对 len-guy/dirk-peters。
3. **AM 簇渐成**：len-guy + dirk-peters + an-antarctic-mystery(work)；R349 补 william-guy 后三主角齐。Arthur Pym 可续为 AM/深池候选。
4. **下次 EVV5 预判**：since_evv5 上次归零 R340，**R350 起始达 10 → EVV5 于 R350 触发**（§3(1b)，优先于 NEW1；届时 queue≈4 仍余，EVV5 后 R351 续 NEW1）。R349 续 NEW1（william-guy）。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
6. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、captain-grant→Robert。
7. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
8. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
9. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
10. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
11. **corpus-discover 顺延**：since_corpus=284→285（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
