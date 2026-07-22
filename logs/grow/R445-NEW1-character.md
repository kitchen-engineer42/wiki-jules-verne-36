---
round: 445
date: 2026-07-22
type_round: 137
phase: "2.1"
current_type: character
gene: NEW1
pages: [andre-letourneur]
result: success
---

# GROW 2.1-B · R445 · NEW1 · character — 建 André Letourneur（The Survivors of the Chancellor 之跛足青年、Herbey 之「兄」）；深耕 SC2 簇，消费第二十五批建序 152，queue 2→1

## 执行摘要

Phase 2.1-B character 第 102 建（type_round 137），消费 R443 第二十五批 discover 队列**建序 152**。决策机 §3 首匹配 **NEW1**（since_evv5=7<10；discover_streak_low=0；since_discover=1<10 且 queue=2>0；stub%=0 → §3(7)）。**消费后 queue(character)=1（建序 153 niklausse）。SC2 簇达 3 页。**

**André Letourneur**（*The Survivors of the Chancellor*，corpus 作 "Andre"）——M. Letourneur 之独子、Havre 法国乘客（SC2-002-006），年约二十、面容温良而左腿残跛之「hopeless cripple」（SC2-004-004 / 018-012）。虽残不辞劳，与众轮值抽水（SC2-019-006），为筏上「the life of our party」（SC2-032-010），危难中救叙述者性命（SC2-038-021），抽死签时以身护父「throwing his arms about his father」（SC2-055-008 / 054-009）。性格：火警镇定慰父（SC2-011-013）、温良虔谢（SC2-018-009）、鼓众持勇（SC2-032-006）、博雅机敏（SC2-005-017）。关系：父 M. Letourneur 以身蔽波护之（SC2-035-004）；大副 [[Robert Curtis]] 待之亲厚（SC2-004-016）；[[Miss Herbey]] 终入其家、于 André「a brother」（SC2-057-016）。

**role=supporting**。book=The Survivors of the Chancellor、first_appearance=SC2-002、affiliation 空、**label=André Letourneur，aliases=[Andre]**（corpus 拼 Andre，label 用正字 André、alias 收 Andre）。

**16 distinct solid PN**（SC2-002-006、004-004/016、005-017、011-013、018-009/012、019-006、032-006/010、035-004、038-021、054-009、055-008、057-002/016）：逾门。全 16 引文经程序化逐字子串复核 + pn_validator strict 双通过。

**质量档（cap 持守）**：add_page 回填 featured，regrade_quality --apply 复定档——andre 落 **standard**。featured 恒 34/671=5.1%。

**方法（ultracode workflow）**：mine→verify 双阶（7 miner + 7 skeptic）扫 SC2 32 现章（André 分布稀疏；明嘱区分子 André 与父 M. Letourneur）。产 58 候选 / 58 validated / 48 distinct PN；择 16（皆全 PN）铺陈「残跛温良子—临危镇定—轮值抽水/救叙述者—护父—Herbey 入家」全弧。**注**：verify 输出个别 PN 缺 PPP 段（如 SC2-024），建页仅取全 PN 者，逐字复核兜底。

**查重**：exact-slug andre-letourneur test -f ABSENT（bucket an）+ registry entity/label/alias（含 André Letourneur / Andre）复验 ABSENT——无冲突。

**wikilink**：[[Robert Curtis]]（既建 R436，SC2-004-016）+ [[Miss Herbey]]（既建 R442，SC2-057-016）+ [[The Survivors of the Chancellor]]（work，存，SC2-057-002）；父 M. Letourneur 未建，PN-grounded 纯文本。**SC2 簇成 3 页，robert-curtis↔miss-herbey↔andre 互链丰满。**

prose-gate：0 超段。**引注**：strict 首验即通过。

character 计数 116→**117**，registry total 1640→**1641**，featured 恒 34，unknown 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =1 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | first_app | 引注 | quality | 要点 |
|------|-----|------|------|-----------|------|---------|------|
| andre-letourneur | ShYej8 | The Survivors of the Chancellor | supporting | SC2-002 | 16 distinct | standard | 残跛温良子—临危镇定—救叙述者—护父—Herbey 入家；label André Letourneur / alias [Andre]；[[Robert Curtis]]+[[Miss Herbey]] 反向链；workflow mine→verify（区分父子）+ Python 逐字校；regrade 落 standard；strict 通过 |

- **andre-letourneur**：16 distinct solid PN；aliases [Andre]；五 H2。add_page rev ShYej8（size 2902）。regrade → standard（cap）。pn_validator --mode strict ✓。**SC2 簇 3 页互链。**

## EXIT-GATE 检查

- **G1 PN grounding**：全句源自 sentence_index 单指 André（非父 M. Letourneur）；58 validated + Python 逐字校；strict ✓。✔
- **G2 段落 ≤400 字**：0 超门。✔
- **G3 ≥5 distinct PN**：16 solid，逾门。✔
- **G4 脚本建页**：add_page；未用 Write/Edit 于 pages/**。✔
- **schema 一致**：五 H2；frontmatter 全字段（description 单引号转义撇号）；role=supporting ∈ enum；label 正字 + alias。✔
- **quality cap**：regrade 持守 5% cap；andre 落 standard。✔
- **registry 一致**：total 1641 character 117 unknown 0 featured 34。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT。✔
- **wikilink 完整性**：[[Robert Curtis]]+[[Miss Herbey]]+[[The Survivors of the Chancellor]] 存在无悬挂；M. Letourneur 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R446 起始计数）

| 字段 | R445 起始 | R446 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 445 | 446 |
| type_round | 137 | 138 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 381 | 382 |
| last_updated_round | 445 | 446 |

## 遗留问题

1. **character 页数 117**：本轮 +1（andre-letourneur，standard）。queue(character) 2→**1**（余 153 niklausse）。registry 全库 **1641**，featured 34（5.1%）。
2. **下轮 R446 = NEW1（§3(7)）**：queue=1>0 且 since_discover=2<10 → NEW1，消费建序 153 **niklausse**（DOSE Van Tricasse 参事同僚，supporting，59 mentions，首现 DOSE-002；成 DOSE 三角 van-tricasse↔doctor-ox↔niklausse）。消费后 queue 归 0 → R447 SCN28-zombie 补第二十六批 → **R448 = §3(1b) EVV5**（since_evv5 R448 起始=10）。
3. **簇闭环里程碑**：SC2 达 3 页（robert-curtis↔miss-herbey↔andre）；EHLA 三角已成；DOSE 待 niklausse（R446）补足第三员。
4. **PN 渲染 bug**（已定案）：本地影子为本 wiki 最终修复；引擎多卷宽度团队推迟后续版本（RFC #562 closed）。
5. **HK / Pilot 债 / event PN 债**：承前，DEFERRED，R448 EVV5 复评。
6. **corpus-discover 顺延**：since_corpus=381→382。
