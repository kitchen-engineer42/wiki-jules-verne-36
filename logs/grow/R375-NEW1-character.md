---
round: 375
date: 2026-07-19
type_round: 67
phase: "2.1"
current_type: character
gene: NEW1
pages: [frycollin]
result: success
---

# GROW 2.1-B · R375 · NEW1 · character — 建 Frycollin（Robur the Conqueror Uncle Prudent 之胆怯仆从、Albatross 上的喜剧配角；RC 簇补 uncle-prudent/phil-evans/robur；第九批建序 104）

## 执行摘要

Phase 2.1-B character 第 54 建（type_round 67），消费 R373 第九批 discover 队列**建序 104**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Frycollin**（*Robur the Conqueror*）——Uncle Prudent 之胆怯仆从、随主同囚 Albatross、以其无可救药之怯懦为航程之喜剧负累。初现「for his only servant had his valet Frycollin, who was hardly worthy of being the servant to so audacious a master」（RC-002-019），随主候于club外「the valet Frycollin waited for Uncle Prudent, his master」（RC-005-008）。与主同遭伏「two onto Frycollin」（RC-005-030），缚囚「Uncle Prudent, Phil Evans, and Frycollin were anything but pleased with their position」（RC-006-002），舟上别居「Frycollin, the valet, was quartered forward in a cabin adjoining that of the cook」（RC-009-003），聒噪遭禁「the engineer ordered them to shut up Frycollin in his cabin」（RC-013-053）。其性一言以蔽「Frycollin was a thorough coward」（RC-005-021），「Frycollin's cowardice had brought him many arduous trials」（RC-005-019）；凌空则溃「did not conceal his terror at finding himself borne through space on such a machine」（RC-008-003），临海复惧「finding himself above the boundless sea, was seized with another fit of terror」（RC-013-050）；哀求 Phil Evans「with piteous pleadings to be put 'on the ground'」（RC-013-032）；于 Robur 眼中「a quantity of no importance」（RC-011-002）。

**role=supporting**。book='Robur the Conqueror'、first_appearance=RC-002、affiliation 空、**label=Frycollin，aliases=[]**。

**12 distinct solid PN**（RC-002-019、005-008/019/021/030、006-002、008-003、009-003、011-002、013-032/050/053）：均 solid，逾门。

**查重**：exact-slug frycollin filesystem test -f ABSENT + registry entity ABSENT（R373 discover 已验，本轮建前复验一致）。

**RC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（RC 簇补 uncle-prudent/phil-evans/robur）**：[[Uncle Prudent]]（character，R364 建）/ [[Phil Evans]]（character，R370 建）/ [[Robur]]（character，存）/ [[Robur the Conqueror]]（work，存）——四链互链无悬挂。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 68→**69**，registry total 1592→**1593**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1、queue=2>0 → NEW1 消费建序 104。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| frycollin | nRC2Y5 | Robur the Conqueror | supporting | RC-002 | 12 distinct | Uncle Prudent 胆怯仆从-随主同囚 Albatross-别居近厨-聒噪遭禁-彻底懦夫-凌空临海皆溃-哀求落地；label Frycollin + aliases 空；RC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Uncle Prudent]]/[[Phil Evans]]/[[Robur]]/[[Robur the Conqueror]] |

- **frycollin**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev nRC2Y5（size 2466）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Frycollin 仆从身份-同囚-别居-怯懦本色因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；role=supporting ∈ enum；RC 2-char 无 Note。✔
- **registry 一致**：total 1593 character 69 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Frycollin 唯一）。✔
- **wikilink 完整性**：Uncle Prudent / Phil Evans / Robur / Robur the Conqueror 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R376 起始计数）

| 字段 | R375 起始 | R376 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 375 | 376 |
| type_round | 67 | 68 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 311 | 312 |
| last_updated_round | 375 | 376 |

## 遗留问题

1. **character 页数 69**：本轮 +1（frycollin）。queue(character) 2→**1**（建序 104 消费）。registry 全库 **1593**，unknown 0。
2. **下轮 R376 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 105（kinko，book The Adventures of a Special Correspondent，pn_anchor ASC-013，role supporting）。消费后 queue=0。**下次 EVV5 于 R382 起始达 since_evv5=10。**
3. **第九批剩 1 候选（建序 105）**：kinko。R376 NEW1 消费后 queue 归 0 → R377 SCN28-zombie 补第十批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + ker-karraje/engineer-serko/simon-hart→Captain Spade、uncle-prudent/phil-evans→Frycollin（本轮建，可回填）、faruskiar/claudius-bombarnac→Kinko。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=311→312（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
