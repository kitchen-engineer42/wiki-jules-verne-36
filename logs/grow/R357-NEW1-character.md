---
round: 357
date: 2026-07-19
type_round: 49
phase: "2.1"
current_type: character
gene: NEW1
pages: [captain-nicholl]
result: success
---

# GROW 2.1-B · R357 · NEW1 · character — 建 Captain Nicholl（Barbicane 之装甲宿敌、后同乘炮弹之伙伴；FEM 簇四主角齐；第七批建序 90）

## 执行摘要

Phase 2.1-B character 第 40 建（type_round 49），消费 R355 第七批 discover 队列**建序 90**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=9>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=8。**

**Captain Nicholl**（*From the Earth to the Moon*）——Barbicane 之宿敌、装甲板锻造大师，终与之和解并同乘炮弹。「His name was Captain Nicholl」（FEM-010-007），二人分执矛盾两端「Barbicane was a great caster of projectiles, and Nicholl was an equally great forger of plate-armour」（FEM-010-009）。宿仇为永续军备竞赛——「As soon as Barbicane had invented a new projectile, Nicholl invented a new plate armour」（FEM-010-010），近验盾胜矛「the cylindro-conical shots of Barbicane had no more effect than pins upon Nicholl's armour-plate」（FEM-010-012），战止于「the war ended the very day that Nicholl terminated a new forged armour-plate」（FEM-010-013）。月弹之议重燃旧怨——Gun Club 通告时「the anger of Captain Nicholl reached its maximum」（FEM-010-021），以科学攻之「to prove by A + B the falseness of his formulae, and he accused him of being ignorant of the rudimentary principles of ballistics」（FEM-010-023），穷途「not being able to fight for his opinion, resolved to pay for it」（FEM-010-027），层层下注。其疑者威望重——「the Greenwich Observatory... took up Captain Nicholl's theories」（FEM-012-006）；然守信偿负「Captain Nicholl cleared off his debt to President Barbicane」（FEM-016-014），至终「against the success of which Captain Nicholl had laid his third bet」（FEM-025-002）。悍中藏柔——林中见其「forgetting the dangers of his situation... occupied in delivering as delicately as possible the victim taken in the meshes of the monstrous spider」（FEM-021-050），自陈宿仇「there is such rivalry that the death of one of us--」（FEM-021-059）；Maston 见和解遂「resolved to join them, and make a party of four」（FEM-022-018）。

**role=antagonist**（Barbicane 之宿敌，后和解同行）。book=From the Earth to the Moon、first_appearance=FEM-010、affiliation 空、**label=Captain Nicholl，aliases=[]**。

**14 distinct solid PN**（FEM-010-007/009/010/012/013/021/023/027、012-006、016-014、021-050/059、022-018、025-002）：均 solid，逾门。

**查重**：exact-slug captain-nicholl filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**FEM 2-char VVV**：无需 RFC-0003 Note。

**wikilink（FEM 补配对）**：[[Impey Barbicane]] / [[Michel Ardan]] / [[J. T. Maston]] / [[From the Earth to the Moon]]——四链互链无悬挂（J. T. Maston R356 新建）。

prose-gate：add_page 初稿 3 超段（431、513、435），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 54→**55**，registry total 1578→**1579**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=9、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =9>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=9>0，按既有实践走 NEW1 消费建序 90。消费后 queue=8。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| captain-nicholl | E5V0RH | From the Earth to the Moon | antagonist | FEM-010 | 14 distinct | Barbicane 之装甲宿敌-矛盾竞赛-月弹重燃旧怨-守信下注-悍中藏柔-和解同乘；label Captain Nicholl + aliases 空；FEM 2-char 无 Note；拆 3 超段；strict 首验通过；互链 [[Impey Barbicane]]/[[Michel Ardan]]/[[J. T. Maston]]/[[From the Earth to the Moon]] |

- **captain-nicholl**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev E5V0RH。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Nicholl 装甲宿敌-竞赛-下注-藏柔-和解因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；FEM 2-char 无 Note。✔
- **registry 一致**：total 1579 character 55 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Captain Nicholl 唯一）。✔
- **wikilink 完整性**：Impey Barbicane / Michel Ardan / J. T. Maston / From the Earth to the Moon 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R358 起始计数）

| 字段 | R357 起始 | R358 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 357 | 358 |
| type_round | 49 | 50 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 293 | 294 |
| last_updated_round | 357 | 358 |

## 遗留问题

1. **character 页数 55**：本轮 +1（captain-nicholl）。queue(character) 9→**8**（建序 90 消费）。registry 全库 **1579**，unknown 0。
2. **下轮 R358 = NEW1（§3(7)）**：since_evv5=7<10；discover_streak_low=0<3；queue(character)=8>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 91（cousin-benedict，book Dick Sand A Captain at Fifteen，pn_anchor DSCF-001，role supporting）——痴迷昆虫学之表亲，启 DSCF 簇。**下次 EVV5 于 R360 起始达 since_evv5=10。**
3. **FEM 簇四主角齐**：barbicane + j-t-maston + captain-nicholl + michel-ardan + from-the-earth-to-the-moon(work)。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、captain-nicholl↔barbicane 互链已建、captain-grant→Robert。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=293→294（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
