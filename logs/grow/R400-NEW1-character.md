---
round: 400
date: 2026-07-19
type_round: 92
phase: "2.1"
current_type: character
gene: NEW1
pages: [thomas-black]
result: success
---

# GROW 2.1-B · R400 · NEW1 · character — 建 Thomas Black（The Fur Country 为观日全食随队北极的偏执天文学家、心无旁骛之 Greenwich 观测者；FC 簇补 paulina-barnett/lieutenant-hobson/sergeant-long/kalumah/madge，第十五批建序 121，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 71 建（type_round 92），消费 R399 第十五批 discover 队列**建序 121（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 122-123 待 R401/R402）。**

**Thomas Black**（*The Fur Country*）——为观日全食而随队北极的偏执天文学家、心无旁骛之 Greenwich 观测者。初现即以名衔并举「the astronomer, Thomas Black」（FC-003-022），身世卓然「an astronomer attached to the Greenwich Observatory...a sagacious and intelligent observer」（FC-003-053）。志在北天「seized with avidity the opportunity offered him of studying this luminous halo」（FC-003-057），目标精确「this solar eclipse...the 18th July 1860」（FC-012-035），事毕即急归「made no attempt to conceal his uneasiness...anxious to return...as soon as he had seen his eclipse」（FC-022-053）。一念独尊「never opened his lips except when his own special mission was discussed」（FC-004-035），漠视田猎「professed absolute indifference to all athletic exercise」（FC-006-021），肥硕慵懒「absorbed in his one idea, never got out of his sledge」（FC-007-030），美景不动其心「the only one who remained indifferent to the sublime beauty of the scene」（FC-017-012），闭舱执器「screwed and unscrewed his instruments...remaining almost always shut up in his cabin」（FC-018-009），冒寒观星「so anxious to take stellar observations...braved the rigour of the outside temperature」（FC-018-051）。Hobson 予其佳室「Hobson offered the other with the window in it to Thomas Black, and the astronomer took immediate possession of it」（FC-014-002）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-003、affiliation 空、**label=Thomas Black，aliases=[]**。

**12 distinct solid PN**（FC-003-022/053/057、004-035、006-021、007-030、012-035、014-002、017-012、018-009/051、022-053）：均 solid，逾门。注意 corpus 内单称「Black」/「Mr Black」多指同一人，本页取全称或明确指涉句。

**查重**：exact-slug thomas-black filesystem test -f ABSENT（bucket th）+ registry entity/label（Thomas Black）ABSENT（R399 discover 已验，本轮建前复验一致）。

**FC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[Jaspar Hobson]]（character→lieutenant-hobson，存，FC-014-002）/ [[The Fur Country]]（work，存）——二链互链无悬挂。Paulina Barnett/Sergeant Long/Greenwich/Airy 正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 85→**86**，registry total 1609→**1610**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 1）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=0<10、queue=3>0 → NEW1 消费建序 121。消费后 queue=2。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| thomas-black | x8Rk7l | The Fur Country | supporting | FC-003 | 12 distinct | Greenwich 天文学家-志在北天-目标精确-事毕急归-一念独尊-漠视田猎-肥硕慵懒-美景不动其心-闭舱执器-冒寒观星-Hobson 予佳室；label Thomas Black + aliases 空；FC 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Jaspar Hobson]]/[[The Fur Country]] |

- **thomas-black**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev x8Rk7l（size 2216）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Thomas Black 天文学家-一念-漠视-闭舱-观星因果；单称 Black/Mr Black 消歧后取明确指涉句；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1610 character 86 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Thomas Black 唯一）。✔
- **wikilink 完整性**：Jaspar Hobson / The Fur Country 二链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R401 起始计数）

| 字段 | R400 起始 | R401 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 400 | 401 |
| type_round | 92 | 93 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 336 | 337 |
| last_updated_round | 400 | 401 |

## 遗留问题

1. **character 页数 86**：本轮 +1（thomas-black）。queue(character) 3→**2**（建序 121 消费）。registry 全库 **1610**，unknown 0。
2. **下轮 R401 = NEW1（§3(7)）**：since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 122（taskinar，book Godfrey Morgan，pn_anchor GM-002，role supporting）。**消费节奏：R401 NEW1（taskinar）→ R402 NEW1（dick-kennedy）→ queue 归 0 → R403 起始 since_evv5=10 → §3(1b) EVV5（不消费队列）→ R404 SCN28-zombie 补第十六批。**
3. **第十五批余 2 候选（建序 122-123）**：taskinar（R401）/dick-kennedy（R402），R402 消费后 queue 归 0 → R403 EVV5 → R404 SCN28-zombie。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT 即此类）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=336→337（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
