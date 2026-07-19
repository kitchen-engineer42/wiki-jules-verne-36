---
round: 398
date: 2026-07-19
type_round: 90
phase: "2.1"
current_type: character
gene: NEW1
pages: [madge]
result: success
---

# GROW 2.1-B · R398 · NEW1 · character — 建 Madge（Mrs Paulina Barnett 之忠仆兼终身伴侣、探险全程相随而信念不摇的坚毅女性；FC 簇补 paulina-barnett/lieutenant-hobson/sergeant-long/kalumah，第十四批建序 120，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 70 建（type_round 90），消费 R395 第十四批 discover 队列**建序 120（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R399 = §3(4) SCN28-zombie 补第十五批。**

**Madge**（*The Fur Country*）——Mrs Paulina Barnett 之忠仆兼终身伴侣、探险全程相随而信念不摇的坚毅女性。初现即巨旅之仆「the celebrated traveller was accompanied by a servant named Madge」（FC-001-028），主仆情逾骨肉「Paulina looked upon Madge as an elder sister, and Madge treated Paulina as her daughter」（FC-001-028）。北极相随「the sledge provided for Mrs Barnett and her faithful Madge」（FC-004-064），随队探真「Lieutenant Hobson, Mrs Barnett, Madge, and a few others at once went to ascertain the truth」（FC-028-003）。性沉实过其主「more matter of fact than her mistress...neither the dangers of an expedition to the Arctic Ocean」（FC-005-031），记性让情「I have not the gift of remembering like you」（FC-005-024），善钓如 Walton 之徒「the faithful Madge, another worthy disciple of Isaak Walton」（FC-014-019）。勇入土穴复出「she bravely entered the narrow tunnel in imitation of her guide」（FC-019-047）/「Madge could not stand it, and hurried out at once」（FC-019-048），信念不摇「her usual unshaken confidence」（FC-031-034）/「God would never permit that」（FC-025-032）。侍主 Barnett 病榻守夜「Mrs Barnett and Madge watched by him until the next morning」（FC-021-063）、随其独探「Madge agreed at once to Mrs Barnett's proposal」（FC-031-028）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-001、affiliation 空、**label=Madge，aliases=[]**。

**12 distinct solid PN**（FC-001-028、004-064、005-024/031、014-019、019-047/048、021-063、025-032、028-003、031-028/034）：均 solid，逾门。

**查重**：exact-slug madge filesystem test -f ABSENT（bucket ma）+ registry entity/label（Madge）ABSENT（R395 discover 已验，本轮建前复验一致）。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Paulina Barnett]]（character→paulina-barnett，存，FC-021-063/031-028）/ [[The Fur Country]]（work，存）——二链互链无悬挂。Isaak Walton/Hobson/Long 正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：add_page warn 一处（FC-005-026 误标，实为 FC-005-024），edit_page 修正后 strict 首验通过。quality featured 回填。

character 计数 84→**85**，registry total 1608→**1609**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2<10、queue=1>0 → NEW1 消费建序 120。消费后 queue=0 → R399 SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| madge | 8CZAw6 | The Fur Country | supporting | FC-001 | 12 distinct | 巨旅之仆-主仆情逾骨肉-北极相随-随队探真-性沉实-记性让情-善钓-勇入土穴复出-信念不摇-病榻守夜-随主独探；label Madge + aliases 空；FC 2-char 无 Note；0 超段直建；add_page warn FC-005-026→024 修正后 strict 通过；互链 [[Paulina Barnett]]/[[The Fur Country]] |

- **madge**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev Qalr2C→edit_page rev 8CZAw6（size 2236）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Madge 忠仆-主仆情-相随-沉实-善钓-信念-守夜因果；FC-005-026 误标经 edit_page 修正为 FC-005-024；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页 + edit_page 修 PN（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1609 character 85 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Madge 唯一）。✔
- **wikilink 完整性**：Paulina Barnett / The Fur Country 二链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R399 起始计数）

| 字段 | R398 起始 | R399 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 398 | 399 |
| type_round | 90 | 91 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 334 | 335 |
| last_updated_round | 398 | 399 |

## 遗留问题

1. **character 页数 85**：本轮 +1（madge）。queue(character) 1→**0**（建序 120 消费，第十四批全数消费完毕）。registry 全库 **1609**，unknown 0。
2. **下轮 R399 = SCN28-zombie（§3(4)）**：since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第十五批候选（≥3），since_discover 归零。**下次 EVV5 于 R403 起始达 since_evv5=10（§3(1b)）。**
3. **第十四批全数消费**（建序 118-120：kalumah/phina-hollaney/madge）R396-R398 NEW1 消费完毕，queue 归 0。R399 SCN28-zombie 补第十五批。**候选池（R395 已 dup-check ABSENT）**：thomas-black（FC，64）、mac-nab（FC，87）、corporal-joliffe（FC，89）、taskinar（GM，20）、marbre（FC，66）、sabine（FC，53）——R399 建前须 filesystem+registry 复验，避单作品集中，另可 fresh corpus sweep。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、paulina-barnett/lieutenant-hobson→Kalumah、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=334→335（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
