---
round: 330
date: 2026-07-19
type_round: 23
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R330 · SCN28 · character — 第四批 discover：6 候选补给（queue 归零后勘探）

## 执行摘要

Phase 2.1-B character 第 4 次 discover（`SCN28-zombie`）。决策机 §3 首匹配 **SCN28**
（since_evv5=0<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。

**本轮为勘探补给轮，不建页（pages: []）**。动作：向 character 候选队列补 **6** 个 grounded + dup-checked 候选（建序 69-74），更新 grow_state（since_discover→0）+ 写日志。registry 不变（total 1557、character 33、unknown 0）。

**6 候选 ≥ type_close_new_candidate_min(3)** → discover_streak_low 保持 **0**（无 type-close 压力，character 类型远未饱和）。

## 候选清单（建序 69-74，均 filesystem + alias dup-check ABSENT）

| 建序 | slug | label | book | pn_anchor | role | mentions | 簇/要点 |
|------|------|-------|------|-----------|------|----------|---------|
| 69 | marfa-strogoff | Marfa Strogoff | Michael Strogoff | MS-004 | supporting | 73 | Michael 之母；Omsk 认子佯不识护其密使身份；与 nadia MS-021 同陷 |
| 70 | alcide-jolivet | Alcide Jolivet | Michael Strogoff | MS-002 | supporting | 95 | 法国记者、诙谐、「表妹」暗语发报；与 blount 亦敌亦友 |
| 71 | harry-blount | Harry Blount | Michael Strogoff | MS-002 | supporting | 124 | 英国 Daily Telegraph 记者、刻板；与 jolivet 竞逐新闻 |
| 72 | feofar-khan | Feofar-Khan | Michael Strogoff | MS-003 | antagonist | 66 | Bukhara 埃米尔、入侵名义首领、判 Michael 目盲之刑；event the-sentence-of-feofar-khan |
| 73 | captain-grant | Captain Grant | In Search of the Castaways | SC-001 | supporting | — | 失踪苏格兰船长、瓶中文书所寻之人、Mary/Robert 之父；work the-children-of-captain-grant |
| 74 | robert-grant | Robert Grant | In Search of the Castaways | SC-003 | supporting | 262 | Grant 船长幼子、勇毅随队寻父；thalcave SC-018-027 已引 |

> **dup-check**：6 slug filesystem `docs/wiki/pages/*/<slug>.md` 全 ABSENT；registry alias_index 命中仅 event/work 页标题（the-sentence-of-feofar-khan / the-rescue-of-robert-grant / the-children-of-captain-grant），非 character alias 冲突——为其提供 wikilink 目标。
> **簇效应**：MS 簇（+marfa/jolivet/blount/feofar 四）与 SC 簇（+captain-grant/robert-grant 二）双深化。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=0 | — |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6/7 | RCH2/NEW1 | — | 未达 |

> queue(character)==0（R328 末位消费后归零），§3(4) 触发勘探。补 6 候选后 queue(character)=6。

## EXIT-GATE 检查（SCN28 勘探轮，仅 G4）

- **G4 记录完整性**：本轮 pages: []，无建页；6 候选清单、dup-check、pn_anchor、role、簇归属完整入日志 + queue.md。✔
- **G1/G2/G3/G5 跳过**：SCN28 勘探轮无建页/改页，按规程跳过。✔
- **registry 一致**：total 1557 character 33 unknown 0，本轮未变。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R331 起始计数）

| 字段 | R330 起始 | R331 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 330 | 331 |
| type_round | 22 | 23 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 7 | **0**（SCN28 复位）|
| discover_streak_low | 0 | 0（new_candidates=6≥3）|
| rounds_since_last_corpus_discover | 266 | 267 |
| last_updated_round | 330 | 331 |

## 遗留问题

1. **character 页数 33**：本轮 discover 未建页。queue(character) 0→**6**（建序 69-74）。registry 全库 **1557**，unknown 0。
2. **下轮 R331 = NEW1（§3(7)）**：since_evv5=1<10；since_discover=0；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 69（marfa-strogoff）。Marfa Strogoff（book Michael Strogoff，pn_anchor MS-004，role supporting，MS 2-char 无 Note）——Michael 之母、Omsk 广场认子佯不识；与 michel-strogoff/nadia 可互链。
3. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。
4. **第四批消费预判**：R331-336 依次建 marfa/jolivet/blount/feofar/captain-grant/robert-grant；R337 queue 再归 0 → §3(4) 第五批 discover（深池：Sangarre/Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz 等单作品主角）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=266→267（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
