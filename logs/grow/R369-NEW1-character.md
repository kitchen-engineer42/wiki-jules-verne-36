---
round: 369
date: 2026-07-19
type_round: 61
phase: "2.1"
current_type: character
gene: NEW1
pages: [faruskiar]
result: success
---

# GROW 2.1-B · R369 · NEW1 · character — 建 Faruskiar（The Adventures of a Special Correspondent 伪贵族铁道劫匪首领；ASC 簇补 major-noltitz/claudius-bombarnac；第八批建序 100）

## 执行摘要

Phase 2.1-B character 第 50 建（type_round 61），消费 R367 第八批 discover 队列**建序 100**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2。**

**Faruskiar**（*The Adventures of a Special Correspondent*）——伪装尊贵旅客之 Grand Transasiatic 总经理、实为劫掠御用金库之匪首。初现于列车「This leading star, I soon learned from Popof, bore the name of Faruskiar」（ASC-008-082）；Bombarnac 慕其「his superb lordship Faruskiar」（ASC-009-006）；边境验关时华官躬身「General Manager, that is what he is, this lord Faruskiar!」（ASC-016-042）。其华贵乃伪——叙事者终见「this abominable bandit hidden beneath the skin of a manager」（ASC-025-007），其谋「Faruskiar's scheme--in the execution of which he had executed his rival Ki-Tsang--had been cleverly contrived in utilizing this branch line leading to the unfinished viaduct」（ASC-025-009），诱车入 Nanking 支线「to walk off with the imperial treasure, is Faruskiar」（ASC-025-044），终暴为「the most consummate bandit who had ever disgraced Central Asia」（ASC-025-052）。伪勇夺誉——匪袭时「pistol in one hand, kandijar in the other, his eyes gleaming, his lips covered with a slight foam」（ASC-020-029），「extraordinary intrepidity... using his kandijar like a man who had often faced death」（ASC-020-036）；然其护库实为除其匪敌 Ki-Tsang「whose attack would have interfered with his criminal projects」（ASC-024-063）。Major Noltitz 独疑之「his eye on his lordship Faruskiar」（ASC-013-003），常伴 Ghangir「talking together in a low tone」（ASC-009-013）；末章报馆讽致「compliments and respects to the heroic Seigneur Faruskiar」（ASC-027-064）。

**role=antagonist**。book='The Adventures of a Special Correspondent'、first_appearance=ASC-008、affiliation='Grand Transasiatic Railway'、**label=Faruskiar，aliases=[]**。

**13 distinct solid PN**（ASC-008-082、009-006/013、013-003、016-042、020-029/036、024-063、025-007/009/044/052、027-064）：均 solid，逾门。

**查重**：exact-slug faruskiar filesystem + registry entity ABSENT（R367 discover 已验，本轮建前 test -f 复验 ABSENT 一致）。

**ASC 3-char VVV**：无需 RFC-0003 Note（Note 仅 4-char VVV 需）。

**wikilink（ASC 簇补 major-noltitz/claudius-bombarnac）**：[[Major Noltitz]]（character，R366 建）/ [[Claudius Bombarnac]]（character，存）/ [[The Adventures of a Special Correspondent]]（work，存）——三链互链无悬挂。Ghangir（未建，无候选）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

**事故记录（CWD 漂移）**：本轮 add_page 首次调用时 CWD 残留于 `data/sentence_index/`（源于 PN 采集 grep 阶段的 cd），致脚本将整页树误写入 `data/sentence_index/docs/**`（自包含副本，真实 docs/wiki 未受污染，git status 确认真实 pages.json 未改）。清理：`rm -rf data/sentence_index/{docs,logs,local}`（均 untracked，真实 ASC-*.jsonl 完好），cd 回 repo 根后重跑 add_page 成功（rev gE9gWL 一致）。**教训**：跨命令 CWD 持久，采集后须显式 cd 回根再调脚本。

character 计数 64→**65**，registry total 1588→**1589**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1、queue=3>0 → NEW1 消费建序 100。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| faruskiar | gE9gWL | The Adventures of a Special Correspondent | antagonist | ASC-008 | 13 distinct | 伪贵族总经理-实为匪首-诱车 Nanking 支线-伪勇除敌 Ki-Tsang-Noltitz 独疑-末章报馆讽誉；label Faruskiar + aliases 空；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Major Noltitz]]/[[Claudius Bombarnac]]/[[The Adventures of a Special Correspondent]] |

- **faruskiar**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev gE9gWL（size 3066）。pn_validator --mode strict ✓。CWD 漂移事故已清理并重建。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Faruskiar 伪贵族-匪首双面-诱车夺库-伪勇除敌因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**（stray tree 事故已 rm 清理，真实 docs/wiki 仅经 add_page 脚本写入）。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；ASC 3-char 无 Note。✔
- **registry 一致**：total 1589 character 65 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Faruskiar 唯一）。✔
- **wikilink 完整性**：Major Noltitz / Claudius Bombarnac / The Adventures of a Special Correspondent 三链存在无悬挂；Ghangir 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R370 起始计数）

| 字段 | R369 起始 | R370 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 369 | 370 |
| type_round | 61 | 62 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 305 | 306 |
| last_updated_round | 369 | 370 |

## 遗留问题

1. **character 页数 65**：本轮 +1（faruskiar）。queue(character) 3→**2**（建序 100 消费）。registry 全库 **1589**，unknown 0。
2. **下轮 R370 = NEW1（§3(7)）**：since_evv5=8<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 101（phil-evans，book Robur the Conqueror，pn_anchor RC-002，role supporting）。**下次 EVV5 于 R371 起始达 since_evv5=10（§3(1b) 先于 NEW1）。**
3. **第八批剩 2 候选（建序 101-102）**：phil-evans/simon-hart。R370 NEW1 消费 phil-evans；R371 起始 since_evv5=10 → §3(1b) EVV5 先行，simon-hart（建序 102）顺延至 EVV5 后 R372 NEW1。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + major-noltitz→Faruskiar（本轮建，可回填）、uncle-prudent→Phil Evans、ker-karraje→Engineer Serko/Simon Hart、thomas-roch→Simon Hart/Ker Karraje、engineer-serko→Captain Spade/Simon Hart、claudius-bombarnac→Faruskiar。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=305→306（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
