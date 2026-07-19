---
round: 339
date: 2026-07-19
type_round: 31
phase: "2.1"
current_type: character
gene: NEW1
pages: [hector-servadac]
result: success
---

# GROW 2.1-B · R339 · NEW1 · character — 建 Hector Servadac（彗星 Gallia 之法国上尉主角；第五批建序 76，OC 新簇种子）

## 执行摘要

Phase 2.1-B character 第 26 建（type_round 31），消费 R337 第五批 discover 队列**建序 76**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=4。**

**Hector Servadac**（*Off on a Comet*）——法国参谋上尉，名片自记「Captain Hector Servadac, Staff Officer, Mostaganem」（OC-002-009），「thirty years of age, an orphan without lineage and almost without means」（OC-003-009），仪表「quite the type of an officer ... a clear blue eye」（OC-003-011）。决斗前夕彗星撞地，将其连同一角地表掷入太空。他推断真相「we must be the population of a young little world called Gallia」（OC-016-051），此名遂定「using Gallia as the name of the new world」（OC-017-001）。由难民而为统帅，戏称「Governor General of Algeria!」（OC-007-040），远航时委仆代掌「'invested with governor's powers,' and took an affecting leave of his master」（OC-010-036）。终归地球而两鬓染霜「Colonel, no longer Captain, Servadac, his hair slightly streaked with grey」（OC-045-023），而彗星之谜终不可解「the career of the comet was ever a mystery」（OC-045-024）。勇毅之证：填隙以身「filling up the breach by his own body, shouted, 'March on!'」（OC-003-012）；情敌为「the Russian Count Timascheff」（OC-003-015）；挚友为勤务兵「his orderly, Ben Zoof」（OC-003-016），生死两报「Servadac had saved Ben Zoof's life in Japan; Ben Zoof had rendered his master a like service in the Soudan」（OC-003-018）。

**role=protagonist**。book=Off on a Comet、first_appearance=OC-002、affiliation 空、aliases 空。

**14 distinct solid PN**（OC-002-009/013、003-009/011/012/015/016/018、007-040、010-036、016-051、017-001、045-023/024）：均 solid，逾门。

**查重**：exact-slug hector-servadac filesystem + registry entity ABSENT。

**OC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Off on a Comet]]（work，存）——互链无悬挂。Ben Zoof（建序 77 未建）、Count Timascheff（未建）暂以纯文本，待建后可 edit_page 回填（DEFERRED）。

**⚠ 新增 alias 冲突（HK(e) 具化）**：off-on-a-comet work 页 aliases 含 'Hector Servadac'（该书原题即 *Hector Servadac*），本轮建 character 页 label 'Hector Servadac' 与之在 alias_index 碰撞。build_registry warn：`alias conflict: 'Hector Servadac' → hector-servadac vs off-on-a-comet`。此即 R321 裁例遗留之 **character-vs-work 同名 label 张力（HK 待批项 e）**，属 parked 范围，**不自主编辑 work 页**；仿 Robur alias 冲突先例，仅 warn、提交照常。本页自身 wikilink 用 [[Off on a Comet]]（work label），未用 [[Hector Servadac]]，故本页链接无歧义；歧义仅存于外部 [[Hector Servadac]] 之解析，留 HK 统一裁决。

prose-gate：add_page 初稿 4 超段（463、522、574、408），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过，无需修正。quality featured 未剥离。

character 计数 40→**41**，registry total 1564→**1565**，unknown 恒 0。build_registry 仅 Robur + 新增 Hector Servadac 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=5、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=5>0，按既有实践走 NEW1 消费建序 76。消费后 queue=4。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| hector-servadac | SYGAm9 | Off on a Comet | protagonist | OC-002 | 14 distinct | 彗星 Gallia 主角-填隙以身-Gallia 命名-governor-归地染霜；OC 2-char 无 Note；拆 4 超段；strict 首验通过；[[Off on a Comet]] 互链；⚠ 与 work 页 alias 'Hector Servadac' 冲突→HK(e) parked |

- **hector-servadac**：14 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev SYGAm9。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Servadac 军旅-遇难-统领-归地因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；OC 2-char 无 Note。✔
- **registry 一致**：total 1565 character 41 unknown 0；Robur + Hector Servadac 两 alias warn（后者 HK(e) parked）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Off on a Comet 链存在无悬挂；Ben Zoof/Timascheff 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R340 起始计数）

| 字段 | R339 起始 | R340 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 339 | 340 |
| type_round | 31 | 32 |
| rounds_since_last_evv5 | 9 | **10**（R340 起始达门）|
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 275 | 276 |
| last_updated_round | 339 | 340 |

## 遗留问题

1. **character 页数 41**：本轮 +1（hector-servadac）。queue(character) 5→**4**（建序 76 消费）。registry 全库 **1565**，unknown 0。
2. **下轮 R340 = EVV5（§3(1b)）**：R340 起始 since_evv5=10≥10 → **§3(1b) EVV5 schema 反射轮触发**（pages:[]，仅 G4，since_evv5 复位→0）。扫描全 41 character 页，校验五 H2 / frontmatter 全字段 / role enum / PN 密度 / 散文门 / wikilink，决定模板是否需改。此即先前修正之「EVV5 于 R340 而非 R339 触发」的兑现轮。
3. **HK(e) character-vs-work 同名 label 张力具化**：off-on-a-comet work 页 alias 'Hector Servadac' 与本轮 character 页 label 冲突（build_registry warn）。R321 裁例之遗留，**parked，勿自主编辑 work 页**；EVV6/HK 批处理时统一裁决（如剥离 work 页该 alias，或以 disambiguation 消歧）。仿 Robur alias 先例，仅 warn、提交照常。
4. **Ben Zoof / Count Timascheff 回链回填**：本页二者为纯文本（未建）。ben-zoof 为建序 77（预计 R341 建），建后可 edit_page 将本页 Ben Zoof 回填为 [[Ben Zoof]]（DEFERRED，非阻塞）。
5. **第五批消费预判（EVV5 时点修正后）**：R340 EVV5 反射（pages:[]）→ R341-344 续建 ben-zoof/lieutenant-hobson/thomas-roch/len-guy（建序 77-80），R345 queue 归 0 → 第六批 discover。
6. **captain-grant→Robert 回链回填**：DEFERRED（R335/R336 记录）。
7. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例，**本轮 hector-servadac 具化**）。
8. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
9. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill；R340 EVV5 复评。
10. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
11. **corpus-discover 顺延**：since_corpus=275→276（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
