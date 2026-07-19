---
round: 365
date: 2026-07-19
type_round: 57
phase: "2.1"
current_type: character
gene: NEW1
pages: [ker-karraje]
result: success
---

# GROW 2.1-B · R365 · NEW1 · character — 建 Ker Karraje（Facing the Flag 马来海盗、伪贵族 Count d'Artigas、觊觎 Roch 之 fulgurator；FF 配对 thomas-roch；第七批建序 97）

## 执行摘要

Phase 2.1-B character 第 47 建（type_round 57），消费 R355 第七批 discover 队列**建序 97**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Ker Karraje**（*Facing the Flag*）——马来海盗，伪贵族 Count d'Artigas。囚俘叙事者溯其源「I have now reason to believe that Ker Karraje is a Malay」（FF-010-053），澳洲金矿数年后结识党羽「and managed to seize a ship in the port of Melbourne」（FF-010-054），太平洋恣掠至「this series of crimes came to an end, and no more was heard of Ker Karraje」（FF-010-057）——遁于新伪身之后。伪身即豪贵——「no one imagined that Count d'Artigas was none other than Ker Karraje, the former pirate of the Pacific」（FF-010-065），以此名购潜艇「possessed of the admirable vessel which was to perform the double function of towing the schooner and attacking ships」（FF-010-076）。其谋在窃兵——囚发明家 Roch 于巢「Roch lives in a private room in Ker Karraje's 'mansion'」日探其秘（FF-011-016），叙事者惧「how much more so will he become if he ever obtains possession of Roch's fulgurator」（FF-010-084）。终局焚灭——党羽「scattered on the rocks of the island」（FF-018-017），Back Cup 爆炸卷之，「Ker Karraje and his pirates have disappeared」（FF-018-029）。恶而冷傲——对质真名唯答「the Count d'Artigas is Ker Karraje... just as Warder Gaydon is Engineer Simon Hart; and Ker Karraje will never restore to liberty Engineer Simon Hart, who knows his secrets」（FF-010-093）；至末仍警觉「advance to the extremity of the point, where they sweep the north-western horizon with their telescopes」（FF-017-028）；独欲终遂「the pirate Ker Karraje was in possession of Roch's fulgurator」（FF-018-011）。

**role=antagonist**。book='Facing the Flag'（YAML 单引号，LAW §8）、first_appearance=FF-010、affiliation 空、**label=Ker Karraje，aliases=[Count d'Artigas]**。

**12 distinct solid PN**（FF-010-053/054/057/065/076/084/093、011-016、017-028、018-011/017/029）：均 solid，逾门。

**查重**：exact-slug ker-karraje filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。**alias Count d'Artigas 无冲突**（build_registry 仅 3 恒 warn；正文 d'Artigas 提及非 alias 声明，不碰撞）。

**FF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FF 配对 thomas-roch）**：[[Thomas Roch]]（character，存）/ [[Facing the Flag]]（work，存）——二链互链无悬挂。Engineer Serko / Simon Hart（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 61→**62**，registry total 1585→**1586**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=9 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费建序 97。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| ker-karraje | Yypi6u | Facing the Flag | antagonist | FF-010 | 12 distinct | 马来海盗-伪贵族 d'Artigas-购潜艇-囚 Roch 觊觎 fulgurator-冷傲对质-Back Cup 焚灭；label Ker Karraje + aliases [Count d'Artigas]；FF 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Thomas Roch]]/[[Facing the Flag]] |

- **ker-karraje**：12 distinct solid PN；aliases [Count d'Artigas]；character-schema 五 H2。add_page rev Yypi6u。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ker Karraje 出身-伪身-购艇-囚 Roch-焚灭-冷傲因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；FF 2-char 无 Note。✔
- **registry 一致**：total 1586 character 62 unknown 0；3 alias warn（均 parked HK）；Count d'Artigas 无新冲突。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Ker Karraje 唯一，alias Count d'Artigas 唯一）。✔
- **wikilink 完整性**：Thomas Roch / Facing the Flag 二链存在无悬挂；Engineer Serko/Simon Hart 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R366 起始计数）

| 字段 | R365 起始 | R366 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 365 | 366 |
| type_round | 57 | 58 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 9 | 10 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 301 | 302 |
| last_updated_round | 365 | 366 |

## 遗留问题

1. **character 页数 62**：本轮 +1（ker-karraje）。queue(character) 2→**1**（建序 97 消费）。registry 全库 **1586**，unknown 0。
2. **下轮 R366 = NEW1（§3(7)，末位候选）**：since_evv5=4<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 98（major-noltitz，book The Adventures of a Special Correspondent，pn_anchor ASC-004，role supporting）。**注：R366 起始 since_discover=10，literal §3(3) SCN28 触发，但既有实践 queue>0 走 NEW1（SCN28 discover 仅在 queue==0 之 §3(4) zombie 或 since_discover≥10 且 queue<threshold 时于 queue 归零后启）。建序 98 消费后 queue(character)=0 → R367 起 §3(4) SCN28-zombie 第八批 discover。**
3. **第七批剩 1 候选（建序 98）**：major-noltitz。R366 NEW1 末位消费。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien/Tudor Brown、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert、doctor-clawbonny→Johnson/Bell/Simpson、tudor-brown→Patrick O'Donoghan、uncle-prudent→Phil Evans、ker-karraje→Engineer Serko/Simon Hart。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=301→302（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
