---
round: 364
date: 2026-07-19
type_round: 56
phase: "2.1"
current_type: character
gene: NEW1
pages: [uncle-prudent]
result: success
---

# GROW 2.1-B · R364 · NEW1 · character — 建 Uncle Prudent（Weldon Institute 主席、气球派巨富、Robur 掳走之囚徒；RC 配对 robur；第七批建序 96）

## 执行摘要

Phase 2.1-B character 第 46 建（type_round 56），消费 R355 第七批 discover 队列**建序 96**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。**

**Uncle Prudent**（*Robur the Conqueror*）——Weldon Institute 主席、气球派（lighter-than-air）巨富。「the famous Uncle Prudent, Prudent being his family name」（RC-002-018），费城气球俱乐部主席、「a personage of consideration, and in spite of his name... well known for his audacity」（RC-002-019）。富而有党亦有敌「Uncle Prudent was rich, and therefore he had friends... but he also had enemies」（RC-002-020）。主持以汽笛代铃「turned on the steam whistle, which did duty for the presidential bell」（RC-003-018），巨球乃其资「the last installment of the hundred thousand paper dollars he had paid for his invention」（RC-003-008）。被掳登 Albatross，志在逃逸「Uncle Prudent and Phil Evans had quite made up their minds to escape」（RC-011-002），谋于飞船「may drop to within a few hundred feet of the ground」之机（RC-013-042）；飓风临而近乎望其毁船「if the cyclone was not playing their game in destroying the aeronef and with her the inventor--and with the inventor the secret of his invention」（RC-018-013）。性烈而暴——与冷静对手成对照「Uncle Prudent was furiously hot; Phil Evans was abnormally cool」（RC-002-021），恨窃天者至「in a sudden outburst of fury, he began to rave and stamp on the sonorous planks, while his hands sought to strangle an imaginary Robur」（RC-006-052）；主席之位仅以毫厘胜出，遗「Phil Evans... only secretary of the Weldon Institute, whereas Uncle Prudent was president」（RC-002-032）之潜怨。

**role=supporting**。book='Robur the Conqueror'（YAML 单引号，LAW §8）、first_appearance=RC-002、affiliation=Weldon Institute、**label=Uncle Prudent，aliases=[]**。

**11 distinct solid PN**（RC-002-018/019/020/021/032、003-008/018、006-052、011-002、013-042、018-013）：均 solid，逾门。

**查重**：exact-slug uncle-prudent filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**RC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（RC 配对 robur）**：[[Robur]]（character，存）/ [[Robur the Conqueror]]（work，存）——二链互链无悬挂。Phil Evans（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 60→**61**，registry total 1584→**1585**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=8 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费建序 96。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| uncle-prudent | ethUgI | Robur the Conqueror | supporting | RC-002 | 11 distinct | Weldon Institute 主席-气球派巨富-汽笛代铃-资助巨球-被掳志逃-性烈而暴-潜怨 Phil Evans；label Uncle Prudent + aliases 空；affiliation Weldon Institute；RC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Robur]]/[[Robur the Conqueror]] |

- **uncle-prudent**：11 distinct solid PN；aliases []；character-schema 五 H2。add_page rev ethUgI。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Uncle Prudent 主席身份-巨富-资助-被掳-逃逸-性烈因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号、affiliation Weldon Institute）；RC 2-char 无 Note。✔
- **registry 一致**：total 1585 character 61 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Uncle Prudent 唯一）。✔
- **wikilink 完整性**：Robur / Robur the Conqueror 二链存在无悬挂；Phil Evans 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R365 起始计数）

| 字段 | R364 起始 | R365 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 364 | 365 |
| type_round | 56 | 57 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 8 | 9 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 300 | 301 |
| last_updated_round | 364 | 365 |

## 遗留问题

1. **character 页数 61**：本轮 +1（uncle-prudent）。queue(character) 3→**2**（建序 96 消费）。registry 全库 **1585**，unknown 0。
2. **下轮 R365 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 97（ker-karraje，book Facing the Flag，pn_anchor FF-010，role antagonist）。**下次 EVV5 于 R371 起始达 since_evv5=10。**
3. **第七批剩 2 候选（建序 97-98）**：ker-karraje/major-noltitz。R365-R366 NEW1 续消费。**建序 98 消费后（R366 末）queue(character)=0 → R367 起 SCN28-zombie 第八批 discover。** 注：R366 起始 since_discover=10，literal §3(3) SCN28 触发，但既有实践 queue>0 走 NEW1；R367 queue==0 方 §3(4) SCN28-zombie discover。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien/Tudor Brown、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert、doctor-clawbonny→Johnson/Bell/Simpson、tudor-brown→Patrick O'Donoghan、uncle-prudent→Phil Evans。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=300→301（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
