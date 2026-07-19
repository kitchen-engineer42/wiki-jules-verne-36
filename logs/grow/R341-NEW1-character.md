---
round: 341
date: 2026-07-19
type_round: 33
phase: "2.1"
current_type: character
gene: NEW1
pages: [ben-zoof]
result: success
---

# GROW 2.1-B · R341 · NEW1 · character — 建 Ben Zoof（Servadac 之忠仆勤务兵；OC 簇配对成型；第五批建序 77）

## 执行摘要

Phase 2.1-B character 第 27 建（type_round 33），消费 R337 第五批 discover 队列**建序 77**。决策机 §3 首匹配 **NEW1**
（since_evv5=0（R340 EVV5 复位）<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=3。**

**Ben Zoof**（*Off on a Comet*）——Hector Servadac 之勤务兵、蒙马特之子。流放阿尔及利亚海岸时，「Hector Servadac's sole companion was his orderly, Ben Zoof」，其人「devoted, body and soul, to his superior officer」（OC-003-016）。首现于上尉马上戏问「I say, Ben Zoof, did you ever compose any poetry?」（OC-002-029），憨仆自陈仅于蒙马特庙会「seen them made」（OC-002-030）。灾变后随主入太空，受命守阿尔及利亚残土「'invested with governor's powers,' and took an affecting leave of his master」（OC-010-036），行前尚有「whether or not it was desirable for Ben Zoof to accompany his master」之议（OC-010-035）。两年 Gallia 航程中为社群欢乐之柱：冰海溜冰「prodigies in the art」（OC-024-005），新卫星复现「to Ben Zoof's great satisfaction」（OC-024-013）；而彗星之谜终不可解「neither Servadac nor his orderly could eliminate from the regions of doubt」（OC-045-024）。其二痴为主与故乡：生于蒙马特「possessed the most unreserved admiration for his birthplace」（OC-003-017），闻其山仅差「some thirteen thousand feet to make it as high as Mont Blanc」（OC-003-020），自此「Hector Servadac and Montmartre held equal places in his affection」（OC-003-021）。忠诚为血债：「Servadac had saved Ben Zoof's life in Japan; Ben Zoof had rendered his master a like service in the Soudan」（OC-003-018）。

**role=supporting**。book=Off on a Comet、first_appearance=OC-002、affiliation 空、aliases 空。

**12 distinct solid PN**（OC-002-029/030、003-016/017/018/020/021、010-035/036、024-005/013、045-024）：均 solid，逾门。

**查重**：exact-slug ben-zoof filesystem + registry entity ABSENT。

**OC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（OC 簇配对成型）**：[[Hector Servadac]]（R339 建，存）、[[Off on a Comet]]（work，存）——互链无悬挂，OC 簇由 hector-servadac/ben-zoof 主仆配对起簇。Count Timascheff（未建）暂纯文本，待建后回填（DEFERRED）。

**引注格式教训（本轮遇）**：初稿 Character 段并置双 PN「(OC-003-020, OC-003-021)」——逗号分隔之双 PN 不被 distinct-PN 计数正则（`\(PN\)`）识别，且 strict 可能漏认。改为各自独立括号后 distinct 由 10→12。**教训：每 PN 单独括号，勿逗号并置。**

prose-gate：add_page 初稿 3 超段（513、417、434），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 41→**42**，registry total 1565→**1566**，unknown 恒 0。build_registry 仅 Robur + Hector Servadac(HK(e)) 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费建序 77。消费后 queue=3。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| ben-zoof | eKb5Od | Off on a Comet | supporting | OC-002 | 12 distinct | Servadac 勤务兵-蒙马特痴-守 governor-Gallia 航程-血债；OC 2-char 无 Note；拆 3 超段；并置双 PN 拆独立括号；strict 首验通过；[[Hector Servadac]]/[[Off on a Comet]] 互链 |

- **ben-zoof**：12 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev eKb5Od。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ben Zoof 勤务-忠诚-蒙马特-航程因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；OC 2-char 无 Note。✔
- **registry 一致**：total 1566 character 42 unknown 0；Robur + Hector Servadac(HK(e) parked) 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Hector Servadac/Off on a Comet 二链存在无悬挂；Count Timascheff 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R342 起始计数）

| 字段 | R341 起始 | R342 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 341 | 342 |
| type_round | 33 | 34 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 277 | 278 |
| last_updated_round | 341 | 342 |

## 遗留问题

1. **character 页数 42**：本轮 +1（ben-zoof）。queue(character) 4→**3**（建序 77 消费）。registry 全库 **1566**，unknown 0。
2. **下轮 R342 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 78（lieutenant-hobson）。Lieutenant Hobson（book The Fur Country，pn_anchor FC-001，role protagonist，FC 2-char 无 Note）——哈德逊湾公司中尉、率队建极地毛皮堡；FC 新簇种子。
3. **OC 簇成型**：hector-servadac/ben-zoof 主仆配对 + off-on-a-comet(work)。Count Timascheff 若后续入队可续扩。
4. **hector-servadac 页 Ben Zoof 回链回填**：ben-zoof 已建，可择轮 edit_page 将 hector-servadac 页 Ben Zoof 纯文本回填为 [[Ben Zoof]]（DEFERRED，非阻塞，同 captain-grant→Robert 例）。
5. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias 'Hector Servadac'，parked。EVV6/HK 批处理裁决。
6. **第五批消费预判**：R342-344 建 lieutenant-hobson/thomas-roch/len-guy（建序 78-80），R345 queue 归 0 → 第六批 discover。
7. **captain-grant→Robert 回链回填**：DEFERRED。
8. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（R321 裁例，R339 具化）。
9. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
10. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
11. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
12. **corpus-discover 顺延**：since_corpus=277→278（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
