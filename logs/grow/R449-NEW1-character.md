---
round: 449
date: 2026-07-22
type_round: 141
phase: "2.1"
current_type: character
gene: NEW1
pages: [hulda]
result: success
---

# GROW 2.1-B · R449 · NEW1 · character — 建 Hulda Hansen（Ticket No. 9672 之 Dal 客栈忠贞挪威少女）；开 TN 新簇，消费第二十六批建序 154，queue 3→2

## 执行摘要

Phase 2.1-B character 第 104 建（type_round 141），消费 R447 第二十六批 discover 队列**建序 154**。决策机 §3 首匹配 **NEW1**（since_evv5=0<10；discover_streak_low=0；since_discover=1<10 且 queue=3>0；stub%=0 → §3(7)）。**消费后 queue(character)=2（建序 155 jean-cornbutte、156 james-playfair）。开 TN 新簇（首建页）。**

**Hulda Hansen**（*Ticket No. 9672*）——Telemark 之 Dal 镇客栈少女，Dame Hansen 之贤女、Joel 之妹：客栈之「froken, the young lady of the house」（TN-003-017），北国忧郁而妩媚（TN-003-018），modest and honest（TN-005-001）。许字水手 Ole Kamp，痴心不渝「united in thought, in spite of the distance」（TN-001-074）。山中力主救难客 Sylvius Hog（TN-008-033）；Ole 之 Viking 号沉没，遗瓶书与彩票 9672 予她（TN-011-116 / 011-113）——她视为「last farewell of her shipwrecked lover」拒售于任何高价（TN-012-029 / 012-030），长候「lived only upon the recollection of Ole」（TN-015-050）。终 Ole 生还、彩票中奖，Dal 小教堂完婚（TN-020-025）。关系：Ole Kamp（表兄兼未婚夫）、Joel（兄）、Sylvius Hog（获救之恩公）。

**role=protagonist**。book=Ticket No. 9672、first_appearance=TN-001、affiliation 空、**label=Hulda Hansen，aliases=[Hulda]**（消歧裸名 Hulda）。

**16 distinct solid PN**（TN-001-074、003-017/018、004-006、005-001、007-014、008-033、011-113/116、012-029/030、013-022、015-003/050、020-025/031）：逾门。全 16 引文经程序化逐字子串复核 + pn_validator strict 双通过。

**质量档（cap 持守）**：add_page 回填 featured，regrade_quality --apply 复定档——hulda 落 **standard**。featured 恒 34/673=5.1%。

**方法（ultracode workflow + 转录恢复）**：mine→verify 双阶（7 miner + 7 skeptic）扫 TN 19 现章（明嘱区分 Hulda 与 Joel/Dame Hansen/Ole/Sylvius Hog/Sandgoist）。output 迟落盘期间先自 6/7 verify 转录恢复 68 valid，后 workflow 完成得 80 validated / 75 distinct PN（复验一致 + 更富 overview）；择 16 铺陈「客栈贤女—忠贞许字—救难客—瓶书彩票—拒售守情—Ole 归完婚」全弧。

**查重**：exact-slug hulda test -f ABSENT（bucket hu）+ registry entity/label/alias（含 Hulda Hansen / Hulda）复验 ABSENT——无冲突。

**wikilink**：TN 首建页，关系人（Ole Kamp/Joel/Sylvius Hog）均未建，依 schema 以 PN-grounded 纯文本列、不挂悬链；Appearances 挂 [[Ticket No. 9672]]（work，存，TN-020-031）。**TN 簇由此开纵深。**

prose-gate：0 超段。**引注**：strict 首验即通过。

character 计数 118→**119**，registry total 1642→**1643**，featured 恒 34，unknown 0。**character 覆盖作品 23→24 部（+TN）。**

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =1 | 否 |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | first_app | 引注 | quality | 要点 |
|------|-----|------|------|-----------|------|---------|------|
| hulda | O2px7S | Ticket No. 9672 | protagonist | TN-001 | 16 distinct | standard | 客栈贤女—忠贞许字 Ole—救 Sylvius Hog—瓶书彩票 9672—拒售守情—Ole 归完婚；label Hulda Hansen / alias [Hulda]；TN 首建页（关系人纯文本）；workflow mine→verify（转录恢复兜底）+ Python 逐字校；regrade 落 standard；strict 通过；Appearances 挂 [[Ticket No. 9672]] |

- **hulda**：16 distinct solid PN；aliases [Hulda]；五 H2。add_page rev O2px7S（size 2642）。regrade → standard（cap）。pn_validator --mode strict ✓。**TN 簇开纵深。**

## EXIT-GATE 检查

- **G1 PN grounding**：全句源自 sentence_index 单指 Hulda；80 validated + Python 逐字校；strict ✓。✔
- **G2 段落 ≤400 字**：0 超门。✔
- **G3 ≥5 distinct PN**：16 solid，逾门。✔
- **G4 脚本建页**：add_page；未用 Write/Edit 于 pages/**。✔
- **schema 一致**：五 H2；frontmatter 全字段（description 单引号转义撇号）；role=protagonist ∈ enum；label 消歧 + alias。✔
- **quality cap**：regrade 持守 5% cap；hulda 落 standard。✔
- **registry 一致**：total 1643 character 119 unknown 0 featured 34。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT。✔
- **wikilink 完整性**：TN 首建页，关系人纯文本无悬链；[[Ticket No. 9672]] 存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R450 起始计数）

| 字段 | R449 起始 | R450 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 449 | 450 |
| type_round | 141 | 142 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 385 | 386 |
| last_updated_round | 449 | 450 |

## 遗留问题

1. **character 页数 119**：本轮 +1（hulda，standard）。queue(character) 3→**2**（余 155 jean-cornbutte、156 james-playfair）。registry 全库 **1643**，featured 34（5.1%）。**覆盖作品 24 部。**
2. **下轮 R450 = NEW1（§3(7)）**：queue=2>0 且 since_discover=2<10 → NEW1，消费建序 155 **jean-cornbutte**（WAI Dunkirk 老船长/入北冰洋寻子，protagonist，151 mentions，首现 WAI-001；开 WAI 新簇）。
3. **消费计划**：R450（155 jean-cornbutte）→ R451（156 james-playfair）→ queue 归 0 → R452 SCN28-zombie 补第二十七批。覆盖作品 R451 后 →26 部。
4. **PN 渲染 bug**（已定案）：本地影子为本 wiki 最终修复；引擎多卷宽度团队推迟（RFC #562 closed）。
5. **HK / Pilot 债 / event PN 债**：承前，DEFERRED（下次 EVV5 R458）。
6. **corpus-discover 顺延**：since_corpus=385→386。
