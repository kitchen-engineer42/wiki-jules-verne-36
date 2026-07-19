---
round: 353
date: 2026-07-19
type_round: 45
phase: "2.1"
current_type: character
gene: NEW1
pages: [claudius-bombarnac]
result: success
---

# GROW 2.1-B · R353 · NEW1 · character — 建 Claudius Bombarnac（跨里海—中国 Grand Transasiatic 铁道之特派记者叙者；ASC 开簇；第六批建序 87）

## 执行摘要

Phase 2.1-B character 第 37 建（type_round 45），消费 R345 第六批 discover 队列**建序 87**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1。**

**Claudius Bombarnac**（*The Adventures of a Special Correspondent*）——法国波尔多记者、Twentieth Century 报之特派员、第一人称叙者。「Claudius Bombarnac, of Bordeaux」（ASC-002-026），自陈「I am a reporter sent by the Twentieth Century to do this journey」（ASC-002-019）。使命随电报至：「Claudius Bombarnac will repair to Uzun Ada, a port on the east coast of the Caspian」（ASC-001-007）。任务遣其跨 Grand Transasiatic 铁道，拥其无常——「here was the unexpected, indeed; the uncertainty of a special correspondent's life」（ASC-001-009）。视列车为可采之众——「to find out who are my traveling companions, whence they come, where they go, is that not the duty of a special correspondent in search of interviews?」（ASC-002-007），信「a special correspondent of the Twentieth Century will know how to make it interesting」（ASC-001-042）。念其编辑，抵 Uzun Ada 遂决「I must telegraph to the Twentieth Century... that I am at my post」（ASC-005-007），惟求「a few incidents of the journey... worthy of the Twentieth Century」（ASC-005-021）；向挚友全衔自介「I am a Frenchman, Claudius Bombarnac, special correspondent of the Twentieth Century」（ASC-007-004）。奉精确为记者首德——「a special correspondent who is not precise is a geometer who neglects to run out his calculations to the tenth decimal」（ASC-002-001），视此业为绝对「either one is a correspondent or one is not!」（ASC-001-035），好奇无尽「there are moments when a special correspondent is metamorphosed into a daughter of Eve」（ASC-007-075），声名先至，同车客呼其「Monsieur Claudius Bombarnac, correspondent of the Twentieth Century」（ASC-009-038）。

**role=narrator**。book=The Adventures of a Special Correspondent、first_appearance=ASC-001、affiliation 空、**label=Claudius Bombarnac，aliases=[]**。

> 队列 book 载「The Special Correspondent」，本轮以既有 work 页 label **The Adventures of a Special Correspondent**（slug adventures-of-a-special-correspondent，存）为准定稿 book 字段，互链一致无悬挂。

**14 distinct solid PN**（ASC-001-007/009/035/042、002-001/007/019/026、005-007/021、007-004/007/075、009-038）：均 solid，逾门。

**查重**：exact-slug claudius-bombarnac filesystem + registry entity ABSENT（R345 discover 已验，本轮建前复验一致）。

**ASC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（ASC 开簇）**：[[The Adventures of a Special Correspondent]]（work，存）——互链无悬挂。Major Noltitz（未建）暂纯文本（DEFERRED）。ASC 簇本轮开簇，claudius-bombarnac + adventures-of-a-special-correspondent(work) 两页起步。

prose-gate：add_page 初稿 2 超段（405、408），各插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 51→**52**，registry total 1575→**1576**，unknown 恒 0。build_registry 仅 Hector Servadac(HK(e)) + Robur the Conqueror 两 alias warn。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=7 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费建序 87。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| claudius-bombarnac | mTu4UG | The Adventures of a Special Correspondent | narrator | ASC-001 | 14 distinct | 波尔多记者-Twentieth Century 特派员-Grand Transasiatic 铁道叙者；label Claudius Bombarnac + aliases 空；book 从队列「The Special Correspondent」定稿为 work 页 label；ASC 2-char 无 Note；拆 2 超段；strict 首验通过；互链 [[The Adventures of a Special Correspondent]] |

- **claudius-bombarnac**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev mTu4UG。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Bombarnac 记者身份-使命-采访职守-精确信条-声名因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；ASC 2-char 无 Note。✔
- **registry 一致**：total 1576 character 52 unknown 0；Hector Servadac(HK(e) parked) + Robur 两 alias warn。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Claudius Bombarnac 唯一）。✔
- **wikilink 完整性**：The Adventures of a Special Correspondent 链存在无悬挂；Major Noltitz 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R354 起始计数）

| 字段 | R353 起始 | R354 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 353 | 354 |
| type_round | 45 | 46 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 7 | 8 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 289 | 290 |
| last_updated_round | 353 | 354 |

## 遗留问题

1. **character 页数 52**：本轮 +1（claudius-bombarnac）。queue(character) 2→**1**（建序 87 消费）。registry 全库 **1576**，unknown 0。
2. **下轮 R354 = NEW1（§3(7)）**：since_evv5=3<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 88（erik）。Erik（book The Waif of the Cynthia，pn_anchor WC-001，role protagonist，WC 2-char 无 Note）——海上拾得之孤儿主角；建后启 WC 簇。**建序 88 为第六批末位，消费后 queue 归 0 → R355 触第七批 SCN28 discover。**
3. **ASC 开簇**：claudius-bombarnac + adventures-of-a-special-correspondent(work) 两页起步。Major Noltitz 可续为 ASC 候选。
4. **UC 簇配对成型**：james-starr + nell + the-underground-city(work)。
5. **AM 簇三主角齐**：len-guy + dirk-peters + william-guy + an-antarctic-mystery(work)。Arthur Pym 深池候选。
6. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。
7. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、captain-grant→Robert。
8. **第六批将尽**：R354 建 erik（建序 88）后 queue 归 0，R355 触第七批 SCN28 discover（≥3 grounded+dup-checked 候选）。下次 EVV5 于 R360 起始达门。
9. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
10. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
11. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
12. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
13. **corpus-discover 顺延**：since_corpus=289→290（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
