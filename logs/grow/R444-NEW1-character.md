---
round: 444
date: 2026-07-22
type_round: 136
phase: "2.1"
current_type: character
gene: NEW1
pages: [benito-garral]
result: success
---

# GROW 2.1-B · R444 · NEW1 · character — 建 Benito Garral（Eight Hundred Leagues on the Amazon 之 Joam 之子/手刃 Torres）；完足 EHLA 三角（joam-garral↔torres↔benito），消费第二十五批建序 151，queue 3→2

## 执行摘要

Phase 2.1-B character 第 101 建（type_round 136），消费 R443 第二十五批 discover 队列**建序 151**。决策机 §3 首匹配 **NEW1**（since_evv5=6<10；discover_streak_low=0；since_discover=0<10 且 queue=3>0；stub%=0 → §3(7)）。**消费后 queue(character)=2（建序 152 andre-letourneur、153 niklausse）。EHLA 簇达 3 页闭环。**

**Benito Garral**（*Eight Hundred Leagues on the Amazon*）——Joam Garral 与 Yaquita 之子（EHLA-002-079 / 003-029），年二十一、勇敏热忱之少年猎手（EHLA-003-040 / 012-046）。父被奸人 Torres 敲诈告发后，横身护父于警前（EHLA-020-077），矢志追凶「resolution admitted of no discussion」（EHLA-026-015），决斗手刃 Torres「I have killed him!」（EHLA-027-009）；然证父清白之文书随尸沉江，遂自责「accused himself of having destroyed his father」（EHLA-027-001），亲潜水搜寻（EHLA-029-011），终得文书「proves my father's innocence!」（EHLA-031-058）。性格：性情开朗（EHLA-003-031）、猎中英勇（EHLA-007-055）、护父怒炽（EHLA-026-021）、决斗沉着（EHLA-026-097）、搜寻竭力（EHLA-030-031）。

**role=supporting**。book=Eight Hundred Leagues on the Amazon、first_appearance=EHLA-002、affiliation 空、**label=Benito Garral，aliases=[Benito]**（裸名 Benito 消歧为全名 label，alias 收裸名，符 LAW §十 + character-schema EVV5「裸名消歧」）。

**18 distinct solid PN**（EHLA-002-079、003-029/031/040、007-055、010-016、012-046、020-077、026-015/021/090/097/122、027-001/009、029-011、030-031、031-058）：逾门。全 18 引文经程序化逐字子串复核 + pn_validator strict 双通过。

**质量档（cap 持守）**：add_page 回填 featured，regrade_quality --apply 复定档——benito 未入前 34，落 **standard**。featured 恒 34/670=5.1%。

**方法（ultracode workflow + 转录恢复）**：mine→verify 双阶 workflow（9 miner + 9 skeptic）扫 EHLA 33 现章。**注**：workflow 进程于空闲窗口中断、output 未落盘（0 字节），遂自 9 个 verify 子代理转录（`agent-*.jsonl` 之 StructuredOutput `validated` 数组）恢复——得 90 valid / 88 distinct PN（`local/tmp/benito_facts.json`）；择 18 铺陈「少年猎手—护父—决斗—伏 Torres—自责—潜搜—得文书昭雪」全弧。全引文另经 Python 逐字子串复核。

**查重**：exact-slug benito-garral test -f ABSENT（bucket be）+ registry entity/label/alias（含 Benito Garral / Benito）复验 ABSENT——无冲突。

**wikilink**：[[Joam Garral]]（既建 R435，EHLA-026-090）+ [[Torres]]（既建 R440，EHLA-026-122）+ [[Eight Hundred Leagues on the Amazon]]（work，存，EHLA-010-016）；Minha/Manoel/Yaquita 未建，PN-grounded 纯文本。**EHLA 簇成 3 页闭环，joam-garral↔torres↔benito 三角互链成型。**

prose-gate：0 超段。**引注**：strict 首验即通过。

character 计数 115→**116**，registry total 1639→**1640**，featured 恒 34，unknown 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =0 | 否 |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | first_app | 引注 | quality | 要点 |
|------|-----|------|------|-----------|------|---------|------|
| benito-garral | Ij2sFe | Eight Hundred Leagues on the Amazon | supporting | EHLA-002 | 18 distinct | standard | Joam 之子/少年猎手—护父—决斗手刃 Torres—自责—潜搜得文书；label Benito Garral / alias [Benito]；[[Joam Garral]]+[[Torres]] 反向链（EHLA 三角）；workflow mine→verify（进程中断，自转录恢复 90 valid）+ Python 逐字校；regrade 落 standard；strict 通过 |

- **benito-garral**：18 distinct solid PN；aliases [Benito]；五 H2。add_page rev Ij2sFe（size 2895）。regrade → standard（top-5% cap）。pn_validator --mode strict ✓。**EHLA 三角闭环。**

## EXIT-GATE 检查

- **G1 PN grounding**：全句源自 sentence_index 单指 Benito；90 valid（自 skeptic 转录恢复）+ Python 逐字校；strict ✓。✔
- **G2 段落 ≤400 字**：0 超门。✔
- **G3 ≥5 distinct PN**：18 solid，逾门。✔
- **G4 脚本建页**：add_page；未用 Write/Edit 于 pages/**。✔
- **schema 一致**：五 H2；frontmatter 全字段（description 单引号转义撇号）；role=supporting ∈ enum；label 消歧 + alias。✔
- **quality cap**：regrade 持守 5% cap；benito 落 standard。✔
- **registry 一致**：total 1640 character 116 unknown 0 featured 34。✔
- **查重充分**：exact-slug + entity/label/alias（含 Benito）ABSENT。✔
- **wikilink 完整性**：[[Joam Garral]]+[[Torres]]+[[Eight Hundred Leagues on the Amazon]] 存在无悬挂；Minha/Manoel 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R445 起始计数）

| 字段 | R444 起始 | R445 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 444 | 445 |
| type_round | 136 | 137 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 380 | 381 |
| last_updated_round | 444 | 445 |

## 遗留问题

1. **character 页数 116**：本轮 +1（benito-garral，standard）。queue(character) 3→**2**（余 152 andre-letourneur、153 niklausse）。registry 全库 **1640**，featured 34（5.1%）。
2. **下轮 R445 = NEW1（§3(7)）**：queue=2>0 且 since_discover=1<10 → NEW1，消费建序 152 **andre-letourneur**（SC2 跛足青年、Herbey 之「兄」，supporting，85 名指 Andre，首现 SC2-002；深耕 SC2 簇）。
3. **EVV5 时点**：since_evv5 R445 起始=7，逐轮 +1 → R448 起始=10 → **R448 = §3(1b) EVV5**。消费计划：R445（152 andre）→ R446（153 niklausse）→ queue 归 0 → R447 SCN28-zombie 补第二十六批 → R448 EVV5。
4. **簇闭环里程碑**：EHLA 三角（joam-garral↔torres↔benito）成型；SC2（robert-curtis↔miss-herbey，待 andre）、DOSE（van-tricasse↔doctor-ox，待 niklausse）待第三员补足。
5. **PN 渲染 bug**（已定案）：本地影子插件为本 wiki 最终修复；引擎多卷宽度经团队裁决推迟后续版本，RFC #562 closed。
6. **workflow 韧性教训**：长 workflow（9+ 组、18+ 代理）遇会话空闲可能中断致 output 未落盘；**补救法**：自 `subagents/workflows/<runId>/agent-*.jsonl` 之 verify 代理 StructuredOutput `validated` 数组恢复，无需重跑。
7. **HK / Pilot 债 / event PN 债**：承前，DEFERRED EVV6（下次 EVV5 R448 复评）。
8. **corpus-discover 顺延**：since_corpus=380→381。
