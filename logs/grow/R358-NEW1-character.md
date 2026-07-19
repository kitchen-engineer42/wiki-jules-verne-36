---
round: 358
date: 2026-07-19
type_round: 50
phase: "2.1"
current_type: character
gene: NEW1
pages: [cousin-benedict]
result: success
---

# GROW 2.1-B · R358 · NEW1 · character — 建 Cousin Benedict（Pilgrim 号上痴迷昆虫学之表亲、tsetse 泄露非洲落点；DSCF 开簇；第七批建序 91）

## 执行摘要

Phase 2.1-B character 第 41 建（type_round 50），消费 R355 第七批 discover 队列**建序 91**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；discover_streak_low=0<3；queue(character)=8>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=7。**

**Cousin Benedict**（*Dick Sand: A Captain at Fifteen*）——Mrs. Weldon 之表亲、心无旁骛之昆虫学家，其痴迷竟无意间泄露漂流者身陷非洲。「one of her relatives, her Cousin Benedict」（DSCF-001-013），「Cousin Benedict's life was entirely and solely consecrated to entomology」（DSCF-001-046）。随 Mrs. Weldon 归航「nothing more natural than for Cousin Benedict to accompany them during that passage」（DSCF-001-050），「carried all his curious collection of insects in a special box」（DSCF-001-053）。船上狂猎标本「examining closely the interstices of the netting, rummaging under the hen-cages, putting his hand between the seams of the deck」（DSCF-005-033），且欲「to initiate the young novice into the mysteries of entomology」（DSCF-005-083）。困非洲后成需看管之累赘——Hercules「undertook to watch him closely... he would act with Cousin Benedict as the latter would with an insect; that is, that he would catch him, if necessary, and bring him back」（DSCF-016-018）；其学问竟成关键——所珍之蝇「a fly smaller than a bee, of a dull color, streaked with yellow」（DSCF-017-113）即「the _tsetse_, that dipter picked up by Benedict」（DSCF-018-110），泄露真正大陆。学识可笑之偏狭——「in no sense, a botanist, nor a mineralogist, nor a geologist」（DSCF-001-027），「he was only an entomologist」（DSCF-001-042），门外则束手「would not know how to distinguish an earth-worm from a medicinal leech, a sand-fly from a glans-marinus, a common spider from a false scorpion」（DSCF-001-039），敬虫如信条「Sir John Franklin made a scruple of killing the smallest insect, be it a mosquito」（DSCF-005-069）。表姊力劝「I beg you very seriously not to go far away」（DSCF-016-011）。

**role=supporting**。book='Dick Sand: A Captain at Fifteen'（work 页 label 含冒号，YAML 单引号包裹，LAW §8）、first_appearance=DSCF-001、affiliation 空、**label=Cousin Benedict，aliases=[]**。

**14 distinct solid PN**（DSCF-001-013/027/039/042/046/050/053、005-033/069/083、016-011/018、017-113、018-110）：均 solid，逾门。

**查重**：exact-slug cousin-benedict filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**DSCF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（DSCF 开簇）**：[[Hercules]]（character，存）/ [[Dick Sand]]（character，存）/ [[Dick Sand: A Captain at Fifteen]]（work，存）——三链互链无悬挂。Mrs. Weldon / Captain Hull（未建，建序 92/93 待建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 2 超段（533、453），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 55→**56**，registry total 1579→**1580**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=8、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =8>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=8>0，按既有实践走 NEW1 消费建序 91。消费后 queue=7。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| cousin-benedict | 2ywAgu | Dick Sand: A Captain at Fifteen | supporting | DSCF-001 | 14 distinct | Mrs. Weldon 表亲-痴迷昆虫学-船上狂猎-非洲累赘-tsetse 泄露大陆-偏狭学识；label Cousin Benedict + aliases 空；book 冒号单引号；DSCF 2-char 无 Note；拆 2 超段；strict 首验通过；互链 [[Hercules]]/[[Dick Sand]]/[[Dick Sand: A Captain at Fifteen]] |

- **cousin-benedict**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev 2ywAgu。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Benedict 昆虫学痴迷-随航-非洲累赘-tsetse 泄露-偏狭因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 冒号单引号）；DSCF 2-char 无 Note。✔
- **registry 一致**：total 1580 character 56 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Cousin Benedict 唯一）。✔
- **wikilink 完整性**：Hercules / Dick Sand / Dick Sand: A Captain at Fifteen 三链存在无悬挂；Mrs. Weldon/Captain Hull 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R359 起始计数）

| 字段 | R358 起始 | R359 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 358 | 359 |
| type_round | 50 | 51 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 294 | 295 |
| last_updated_round | 358 | 359 |

## 遗留问题

1. **character 页数 56**：本轮 +1（cousin-benedict）。queue(character) 8→**7**（建序 91 消费）。registry 全库 **1580**，unknown 0。
2. **下轮 R359 = NEW1（§3(7)）**：since_evv5=8<10；discover_streak_low=0<3；queue(character)=7>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 92（mrs-weldon，book Dick Sand: A Captain at Fifteen，pn_anchor DSCF-001，role supporting）——船主之妻、Dick 所护乘客。**下次 EVV5 于 R360 起始达 since_evv5=10 → §3(1b) EVV5 触发。**
3. **DSCF 开簇**：cousin-benedict + dick-sand（既有）+ hercules（既有）+ dick-sand-a-captain-at-fifteen(work) 起步。Mrs. Weldon / Captain Hull（建序 92/93）续建。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、captain-grant→Robert。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=294→295（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
