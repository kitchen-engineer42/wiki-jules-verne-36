---
round: 385
date: 2026-07-19
type_round: 77
phase: "2.1"
current_type: character
gene: NEW1
pages: [tom-turner]
result: success
---

# GROW 2.1-B · R385 · NEW1 · character — 建 Tom Turner（Robur the Conqueror Albatross 之舵手兼 Robur 心腹水手长、铁骨英国人、司号操炮掌舵；第十一批建序 111，末候选，消费后 queue 归 0）

## 执行摘要

Phase 2.1-B character 第 61 建（type_round 77），消费 R381 第十一批 discover 队列**建序 111（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → 下轮 R386 = §3(4) SCN28-zombie 补第十二批。**

**Tom Turner**（*Robur the Conqueror*）——Albatross 之舵手兼 Robur 心腹水手长、铁骨英国人、司号操炮掌舵，跳出 ASC 单作品集中回归 RC 簇。为 Robur 副手「Robur, his mate Tom Turner, an engineer and two assistants, two steersman and a cook--eight men all told」（RC-007-032），铁骨形貌「an Englishman of about forty-five, broad in the shoulders and short in the legs, a man of iron, with one of those enormous characteristic heads that Hogarth rejoiced in」（RC-010-003）。随主行止「his mate, Tom Turner, accompanied him」（RC-008-044），主令己行「gave the orders, while Tom Turner was at the helm」（RC-012-027），司瞭望报讯「to the engineer and said, 'Do you see that black spot on the horizon, sir'」（RC-017-018）。司号为艇之厉声「the trumpet which blared its startling fanfares through the air was that of the mate, Tom Turner」（RC-008-048），操炮猎鲸「seized the arquebus, which was resting against a cleat on the rail」（RC-011-033），旋涡中坚守炮位「crouching behind the swivel amidships where the effect of the centrifugal force was least felt」（RC-016-020），合恩角掌舵「Tom Turner was at the helm, and it required all his skill to keep her straight」（RC-018-018）。为 Robur 所倚「'That is nearer than I supposed,' said Robur to Tom Turner」（RC-019-014），奉命看管俘虏「the engineer ordered them to shut up Frycollin in his cabin」（RC-013-053），终报天候「Tom Turner came up to the engineer」（RC-020-025）。

**role=supporting**。book='Robur the Conqueror'、first_appearance=RC-007、affiliation 空、**label=Tom Turner，aliases=[]**。

**12 distinct solid PN**（RC-007-032、008-044/048、010-003、011-033、012-027、013-053、016-020、017-018、018-018、019-014、020-025）：均 solid，逾门。

**查重**：exact-slug tom-turner filesystem test -f ABSENT + registry entity/label（Tom Turner）ABSENT（R381 discover 已验，本轮建前复验一致）。

**RC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Robur]]（character，存，RC-019-014）/ [[Frycollin]]（character，存，RC-013-053）/ [[Robur the Conqueror]]（work，存，RC-020-025）——三链互链无悬挂。Tapage（cook）/ Uncle Prudent / Phil Evans 于正文纯文本无提及，不涉链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 75→**76**，registry total 1599→**1600**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 仅显 2：Hector Servadac / Robur the Conqueror）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=3<10、queue=1>0 → NEW1 消费建序 111。消费后 queue=0。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| tom-turner | kTXhjt | Robur the Conqueror | supporting | RC-007 | 12 distinct | Albatross 舵手兼水手长-Robur 心腹-铁骨英国人-司号-操炮猎鲸-旋涡守炮位-合恩角掌舵-看管俘虏；label Tom Turner + aliases 空；RC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Robur]]/[[Frycollin]]/[[Robur the Conqueror]] |

- **tom-turner**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev kTXhjt（size 2554）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Tom Turner 副手-掌舵-司号-操炮-看管因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；RC 2-char 无 Note。✔
- **registry 一致**：total 1600 character 76 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Tom Turner 唯一）。✔
- **wikilink 完整性**：Robur / Frycollin / Robur the Conqueror 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R386 起始计数）

| 字段 | R385 起始 | R386 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 385 | 386 |
| type_round | 77 | 78 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 321 | 322 |
| last_updated_round | 385 | 386 |

## 遗留问题

1. **character 页数 76**：本轮 +1（tom-turner）。queue(character) 1→**0**（建序 111 消费，第十一批全数消费完毕）。registry 全库 **1600**，unknown 0。
2. **下轮 R386 = SCN28-zombie（§3(4)）**：since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**。补第十二批候选（pages:[]，仅 G4，since_discover 归零）。**下次 EVV5 于 R393 起始达 since_evv5=10。**
3. **第十二批 discover（R386）**：queue 归 0，需补 ≥3 grounded+dup-checked 候选。ASC/RC 旅伴群像续挖或跨作品拓展。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan、claudius-bombarnac/caterna→Ephrinell、claudius-bombarnac/major-noltitz→Pan Chao。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=321→322（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
