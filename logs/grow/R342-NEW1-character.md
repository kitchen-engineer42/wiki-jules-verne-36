---
round: 342
date: 2026-07-19
type_round: 34
phase: "2.1"
current_type: character
gene: NEW1
pages: [lieutenant-hobson]
result: success
---

# GROW 2.1-B · R342 · NEW1 · character — 建 Jaspar Hobson（漂流冰岛之极地毛皮堡领队；FC 新簇种子；第五批建序 78）

## 执行摘要

Phase 2.1-B character 第 28 建（type_round 34），消费 R337 第五批 discover 队列**建序 78**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。**

**Jaspar Hobson**（*The Fur Country*）——哈德逊湾公司中尉。Craventy 上尉宴上首现于「some sixty soldiers or employés of the Hudson's Bay Company」（FC-001-011），「a man of forty years of age」、「a child of the Company」、「no mere hunter, but a soldier, a brave and intelligent officer」（FC-001-024）。受命于北冰洋岸建新堡，率队四月启程，「the lady traveller was to join ... for the exploration of the north」（FC-001-029）；上尉担保「Jaspar Hobson has never yet drawn back from a task imposed upon him」（FC-002-010）。北行「Hobson determined to get to the coast by the shortest route」（FC-010-007），知需「penetrate a good deal further north」（FC-010-033）。筑 Fort Hope 于似半岛之地，地震断其颈——他悟灾变及其怪果「converted our peninsula into a floating island, and this explains why the furred ... animals ... have become so numerous round the fort!」（FC-024-032），然「we have absolutely no control over our floating island」（FC-025-014）。领袖之重稳压其肩：以天文钟测位至秒「'Seventy degrees, forty-four minutes, and thirty-seven seconds,' replied Hobson」（FC-023-080），择险差遣「his office imposed caution ... he chose the Sergeant」（FC-021-041），为安众心而藏危「kept a profound secret, as Hobson was unwilling to render his companions anxious」（FC-023-030）。终堡失，Verne 恕之「no one could possibly blame Hobson or his companions」（FC-047-003）。

**role=protagonist**。**label=Jaspar Hobson，aliases=['Lieutenant Hobson']**（slug 沿队列 lieutenant-hobson；canonical 名 Jaspar Hobson 由 FC-001-024 grounding，「Lieutenant Hobson」为频用称谓存 alias）。book=The Fur Country、first_appearance=FC-001、affiliation 空。

**12 distinct solid PN**（FC-001-011/024/029、002-010、010-007/033、021-041、023-030/080、024-032、025-014、047-003）：均 solid，逾门。

**查重**：exact-slug lieutenant-hobson + jaspar-hobson filesystem + registry entity 全 ABSENT。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FC 新簇种子）**：[[The Fur Country]]（work，存）——互链无悬挂。Mrs Paulina Barnett（未建，深池候选）、Sergeant Long（未建）暂纯文本，待建后回填（DEFERRED）。

prose-gate：add_page 初稿 1 超段（586），插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 42→**43**，registry total 1566→**1567**，unknown 恒 0。build_registry 仅 Robur + Hector Servadac(HK(e)) 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=4 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费建序 78。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| lieutenant-hobson | nZgwHt | The Fur Country | protagonist | FC-001 | 12 distinct | HBC 中尉-率队建极地堡-半岛化冰岛漂流-领袖之重；label Jaspar Hobson + alias Lieutenant Hobson；FC 2-char 无 Note；拆 1 超段；strict 首验通过；[[The Fur Country]] 互链 |

- **lieutenant-hobson**：12 distinct solid PN；alias ['Lieutenant Hobson']；character-schema 五 H2。add_page rev nZgwHt。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Hobson 军旅-率队-灾变-领袖因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；FC 2-char 无 Note。✔
- **registry 一致**：total 1567 character 43 unknown 0；Robur + Hector Servadac(HK(e) parked) 两 alias warn。✔
- **查重充分**：exact-slug（含 jaspar-hobson 变体）+ entity ABSENT；registry 无 character 冲突（label Jaspar Hobson 唯一）。✔
- **wikilink 完整性**：The Fur Country 链存在无悬挂；Barnett/Long 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R343 起始计数）

| 字段 | R342 起始 | R343 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 342 | 343 |
| type_round | 34 | 35 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 278 | 279 |
| last_updated_round | 342 | 343 |

## 遗留问题

1. **character 页数 43**：本轮 +1（lieutenant-hobson）。queue(character) 3→**2**（建序 78 消费）。registry 全库 **1567**，unknown 0。
2. **下轮 R343 = NEW1（§3(7)）**：since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 79（thomas-roch）。Thomas Roch（book Facing the Flag，pn_anchor FF-001，role supporting，FF 2-char 无 Note）——疯狂发明家、Fulgurator 超级武器创造者；FF 新簇种子。
3. **FC 簇种子**：lieutenant-hobson + the-fur-country(work)。深池 paulina-barnett（Mrs Barnett）可续为 FC 簇配对。
4. **Mrs Barnett / Sergeant Long 回链回填**：本页二者纯文本，待建后 edit_page 回填（DEFERRED，非阻塞）。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。EVV6/HK 批处理裁决。
6. **第五批消费预判**：R343-344 建 thomas-roch/len-guy（建序 79-80），R345 queue 归 0 → 第六批 discover。
7. **hector-servadac→Ben Zoof / captain-grant→Robert 回链回填**：DEFERRED。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（R321 裁例，R339 具化）。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=278→279（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
