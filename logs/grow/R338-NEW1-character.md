---
round: 338
date: 2026-07-19
type_round: 30
phase: "2.1"
current_type: character
gene: NEW1
pages: [sangarre]
result: success
---

# GROW 2.1-B · R338 · NEW1 · character — 建 Sangarre（Ogareff 之吉普赛女密探；第五批队列首位）

## 执行摘要

Phase 2.1-B character 第 25 建（type_round 30），消费 R337 第五批 discover 队列**建序 75（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=5。**

**Sangarre**（*Michael Strogoff*）——Ogareff 之吉普赛女党羽、密探，「Sangarre and her Zingari, well paid spies, were absolutely devoted to him」（MS-015-050），首现 MS-006。自始参与密谋暗语「'You are right, Sangarre!'」（MS-006-024），一见 Michael 即牢记其貌「regarding him with a peculiar gaze, as if to fix his features indelibly in her memory」（MS-009-012）。奉命监视 Marfa「without losing sight of her whom she was watching」（MS-021-011），终于揭穿母子相认之私情「had been observed by Sangarre, Ogareff's spy」（MS-022-026），坚称「'I am not mistaken, Ivan,' she said」（MS-022-041），进逼「Sangarre advanced towards the group, in the midst of which stood Marfa」（MS-022-051），以一言设陷「Sangarre, close to him, said one word, 'The knout!'」（MS-022-079）。

**role=antagonist**。book=Michael Strogoff、first_appearance=MS-006、affiliation 空、aliases 空。

**13 distinct solid PN**（MS-006-024、009-009/012、015-050、021-008/009/010/011/023、022-026/041/051/079）：均 solid，逾门。

**查重**：exact-slug sangarre filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Ivan Ogareff]]（存）、[[Marfa Strogoff]]（存）、[[Michel Strogoff]]（存）、[[Michael Strogoff]]（work，存）——四链均存在无悬挂，MS 簇经 sangarre 完形（Ogareff 之党羽补齐）。

prose-gate：add_page 初稿 2 超段（412、474），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过，无需修正。quality featured 未剥离。

character 计数 39→**40**，registry total 1563→**1564**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=6、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=6>0，按既有实践走 NEW1 消费建序 75（首位）。消费后 queue=5。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| sangarre | kdnBIJ | Michael Strogoff | antagonist | MS-006 | 13 distinct | Ogareff 之吉普赛女密探-牢记 Michael 貌-监视 Marfa-揭穿母子-「The knout!」设陷；MS 2-char 无 Note；拆 2 超段；strict 首验通过；[[Ivan Ogareff]]/[[Marfa Strogoff]]/[[Michel Strogoff]]/work 互链 |

- **sangarre**：13 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev kdnBIJ。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Sangarre 密探-监视-揭穿因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1564 character 40 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Ivan Ogareff/Marfa Strogoff/Michel Strogoff/Michael Strogoff 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R339 起始计数）

| 字段 | R338 起始 | R339 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 338 | 339 |
| type_round | 30 | 31 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 274 | 275 |
| last_updated_round | 338 | 339 |

## 遗留问题

1. **character 页数 40**：本轮 +1（sangarre）。queue(character) 6→**5**（建序 75 首位消费）。registry 全库 **1564**，unknown 0。
2. **EVV5 时点修正（off-by-one）**：R329 为 EVV5（since_evv5 复位→0，R330 起始=0）。逐轮递增：R338 起始=8、R339 起始=9、**R340 起始=10 → EVV5 于 R340 触发**，而非既往 R330-R337 日志误载之「约 R339」。R339 为 NEW1（建序 76 hector-servadac）。此修正取代先前所有「EVV5 下次约 R339」记载。
3. **下轮 R339 = NEW1（§3(7)）**：since_evv5=9<10 → 非 §3(1)；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 76（hector-servadac）。Hector Servadac（book Off on a Comet，pn_anchor OC-002，role protagonist，OC 2-char 无 Note）——法国上尉、彗星 Gallia 撞击后随之遨游太空之主角；OC 新簇种子，与 ben-zoof（建序 77）可配对起簇。
4. **第五批消费预判（修正 EVV5 时点后）**：R339 建 hector-servadac（建序 76）→ **R340 触发 §3(1b) EVV5 schema 反射轮（pages:[]）** → R341-344 续建 ben-zoof/lieutenant-hobson/thomas-roch/len-guy（建序 77-80），R345 queue 再归 0 → 第六批 discover。
5. **captain-grant→Robert 回链回填**：DEFERRED（R335/R336 记录），可择轮 edit_page 将 captain-grant 页 Robert Grant 纯文本回填为 [[Robert Grant]]。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=274→275（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
