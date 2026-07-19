---
round: 396
date: 2026-07-19
type_round: 88
phase: "2.1"
current_type: character
gene: NEW1
pages: [kalumah]
result: success
---

# GROW 2.1-B · R396 · NEW1 · character — 建 Kalumah（The Fur Country 眷恋 Mrs Barnett 之因纽特少女、独渡海 70 小时以寻漂流故友；FC 簇补 paulina-barnett/lieutenant-hobson/sergeant-long，第十四批建序 118，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 68 建（type_round 88），消费 R395 第十四批 discover 队列**建序 118（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 119-120 待 R397/R398）。**

**Kalumah**（*The Fur Country*）——眷恋 Mrs Barnett 之因纽特少女、于浮冰绝境独渡海 70 小时以寻漂流故友的向导。初现即亲近 Barnett「the name of the young girl was Kalumah, and she seemed to have taken a great fancy to Mrs Barnett」（FC-019-043），其族「the young Esquimaux girl Kalumah」（FC-031-087）。极夜中日至堡听读「when Mrs Barnett read aloud, Kalumah listened with great attention」（FC-019-053），春回践约寻友「the month of May having come round, Kalumah set out to fulfil her pledge」（FC-032-015），临风雨预感下海「a kind of presentiment led Kalumah to venture down to the beach, and, braving the wind and rain」（FC-032-029）。意志坚定「Kalumah did not doubt or hesitate a moment」（FC-032-033），海上历 70 小时而不屈「Kalumah had then been seventy hours at sea since she embarked」（FC-032-051），失友恸哭「Kalumah's tears flowed fast at the loss of those whom she had come so far to see」（FC-032-019）。挚爱 Barnett 惜别「sorry to part with Mrs Barnett」（FC-019-075）、获救后谢忱「seated on the sand between Mrs Barnett and Madge」（FC-032-013）；Hobson 惊其归「what must Lieutenant Hobson have thought when he saw her leaning on Mrs Barnett」（FC-033-004）；堡众欢迎「Mrs Mac-Nab, Mrs Rae and Mrs Joliffe overwhelmed her with caresses」（FC-033-002）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-019、affiliation 空、**label=Kalumah，aliases=[]**。

**12 distinct solid PN**（FC-019-043/053/075、031-087、032-013/015/019/029/033/051、033-002/004）：均 solid，逾门。

**查重**：exact-slug kalumah filesystem test -f ABSENT（bucket ka）+ registry entity/label（Kalumah）ABSENT（R395 discover 已验，本轮建前复验一致）。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Paulina Barnett]]（character→paulina-barnett，存，FC-019-075）/ [[Jaspar Hobson]]（character→lieutenant-hobson，存，FC-033-004）/ [[The Fur Country]]（work，存，FC-033-002）——三链互链无悬挂（label→slug 经 alias_index 解析）。Madge（建序 120，R398 待建）、Mrs Mac-Nab/Rae/Joliffe 正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 82→**83**，registry total 1606→**1607**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 1）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0<10、queue=3>0 → NEW1 消费建序 118。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| kalumah | BJ2WiC | The Fur Country | supporting | FC-019 | 12 distinct | 因纽特少女-亲近 Barnett-听读-春回践约-预感下海-意志坚定-70 小时海上-失友恸哭-惜别 Barnett-获救谢忱-Hobson 惊归-堡众欢迎；label Kalumah + aliases 空；FC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Paulina Barnett]]/[[Jaspar Hobson]]/[[The Fur Country]] |

- **kalumah**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev BJ2WiC（size 2344）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Kalumah 因纽特少女-听读-践约-渡海-恸哭-谢忱因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1607 character 83 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Kalumah 唯一）。✔
- **wikilink 完整性**：Paulina Barnett / Jaspar Hobson / The Fur Country 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R397 起始计数）

| 字段 | R396 起始 | R397 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 396 | 397 |
| type_round | 88 | 89 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 332 | 333 |
| last_updated_round | 396 | 397 |

## 遗留问题

1. **character 页数 83**：本轮 +1（kalumah）。queue(character) 3→**2**（建序 118 消费）。registry 全库 **1607**，unknown 0。
2. **下轮 R397 = NEW1（§3(7)）**：since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 119（phina-hollaney，book Godfrey Morgan，pn_anchor GM-003，role supporting）。**下次 EVV5 于 R403 起始达 since_evv5=10（§3(1b)）。**
3. **第十四批余 2 候选（建序 119-120）**：phina-hollaney（R397）/madge（R398），R398 消费后 queue 归 0 → R399 SCN28-zombie 补第十五批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + paulina-barnett/lieutenant-hobson→Kalumah、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=332→333（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
