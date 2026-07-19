---
round: 343
date: 2026-07-19
type_round: 35
phase: "2.1"
current_type: character
gene: NEW1
pages: [thomas-roch]
result: success
---

# GROW 2.1-B · R343 · NEW1 · character — 建 Thomas Roch（Fulgurator 之疯狂天才发明家；FF 新簇种子；第五批建序 79）

## 执行摘要

Phase 2.1-B character 第 29 建（type_round 35），消费 R337 第五批 discover 队列**建序 79**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Thomas Roch**（*Facing the Flag*）——法国天才发明家。「a Frenchman named Thomas Roch, forty-five years of age」（FF-001-013），囚于美国疯人院 Healthful House。「Thomas Roch was an inventor--an inventor of genius」（FF-001-020），癫狂独存其才「the demon of insanity had respected the man of science ... the flame of genius still burned brightly」（FF-001-041）。其名系于骇世凶器「Roch's Fulgurator」（FF-001-021），「a sort of auto-propulsive engine ... charged with an explosive composed of new substances」（FF-001-024）。曾求见海军部长「an audience in regard to a communication that Thomas Roch desired to make」（FF-001-017），执此者可得「the offensive and defensive superiority of his native country」（FF-001-026）。然贪傲误之——不得巨款不肯试验（FF-001-026），索价「excessive」（FF-001-022）；诸国拒之，癫而受囚（FF-001-040），终为海盗劫走欲以其才祸世。危局受命轰击来舰，识其旗后「Thomas Roch refuses」（FF-017-081）。天才与癫狂不可分，「this indifference was practically absolute」（FF-001-015），其名之盛使戒备之国「could not hesitate to receive the petitioner」（FF-001-019），众惧其「die during one of his paroxysms and carry his secret with him to the grave」（FF-001-043）。终为三色旗所动而赎——「Moved to his very soul at the sight of the tricolor flag ... Thomas Roch rushed through the passage to the magazine」（FF-018-028），以自毁易叛国。

**role=supporting**。book=Facing the Flag、first_appearance=FF-001、affiliation 空、aliases 空。

**14 distinct solid PN**（FF-001-013/015/017/019/020/021/022/024/026/040/041/043、017-081、018-028）：均 solid，逾门。

**查重**：exact-slug thomas-roch filesystem + registry entity ABSENT。

**FF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FF 新簇种子）**：[[Facing the Flag]]（work，存）——互链无悬挂。Simon Hart（化名 Gaydon 之守护者）、Ker Karraje（劫持之海盗首）暂纯文本（未建），待建后回填（DEFERRED）。

prose-gate：add_page 初稿 4 超段（457、506、464、407），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 43→**44**，registry total 1567→**1568**，unknown 恒 0。build_registry 仅 Robur + Hector Servadac(HK(e)) 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=5 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费建序 79。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| thomas-roch | rHKBGc | Facing the Flag | supporting | FF-001 | 14 distinct | 天才发明家-Fulgurator-囚疯人院-海盗劫持-三色旗赎罪；FF 2-char 无 Note；拆 4 超段；strict 首验通过；[[Facing the Flag]] 互链 |

- **thomas-roch**：14 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev rHKBGc。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Roch 发明-癫狂-劫持-赎罪因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；FF 2-char 无 Note。✔
- **registry 一致**：total 1568 character 44 unknown 0；Robur + Hector Servadac(HK(e) parked) 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Facing the Flag 链存在无悬挂；Simon Hart/Ker Karraje 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R344 起始计数）

| 字段 | R343 起始 | R344 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 343 | 344 |
| type_round | 35 | 36 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 279 | 280 |
| last_updated_round | 343 | 344 |

## 遗留问题

1. **character 页数 44**：本轮 +1（thomas-roch）。queue(character) 2→**1**（建序 79 消费）。registry 全库 **1568**，unknown 0。
2. **下轮 R344 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 80（len-guy，末位）。Len Guy（book An Antarctic Mystery，pn_anchor AM-001，role protagonist，AM 2-char 无 Note）——Halbrane 号船长、寻兄 William Guy 之南极远征领队；AM 新簇种子。**消费后 queue(character)=0，R345 触发第六批 SCN28-zombie discover。**
3. **FF 簇种子**：thomas-roch + facing-the-flag(work)。深池 ker-karraje/simon-hart 可续为 FF 簇配对。
4. **Simon Hart / Ker Karraje 回链回填**：本页二者纯文本，待建后 edit_page 回填（DEFERRED）。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。EVV6/HK 批处理裁决。
6. **第五批收官预判**：R344 建 len-guy（建序 80，末位）→ queue 归 0 → R345 第六批 discover（SCN28-zombie）。深池余续（R337 记）：claudius-bombarnac(ASC)/erik(WC)/james-starr(UC)/nell(UC)/paulina-barnett(FC)/palmyrin-rosette(OC)/dirk-peters(AM)/William Guy 等。
7. **hector-servadac→Ben Zoof / lieutenant-hobson→Barnett/Long / captain-grant→Robert 回链回填**：DEFERRED。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（R321 裁例，R339 具化）。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=279→280（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
