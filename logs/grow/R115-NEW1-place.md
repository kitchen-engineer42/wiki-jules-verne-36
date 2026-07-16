---
round: 115
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [lyons, havre, corsica, sardinia, teheran]
result: success
---

## 执行摘要

R115 决策矩阵（读 R114 末计数器：queue=27、since_evv5=9、since_discover=3、discover_streak_low=0、since_corpus=51）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=9<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=27≥10 且 since_discover=3<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 积压，按 distinctPN 降序消化第四批。全部先经既有页交叉核 + 多实体/称号/异地同名筛。

**建页前筛查（本轮 2 候选剔除 + 1 同名义项剔）**：
- **Lucknow → 同名误判剔除**：SC:7 全系澳洲「Lucknow Road（往 Melbourne 之路，SC:41-44 澳洲段）」，**非印度勒克瑙城**；候选原注「印度城」有误。作澳洲小地名过薄 → 挂起，PHQ 决定。替补 Sardinia。
- **Archangel → 同名剔除**：FC:6 全系「New Archangel」= Sitka（Russian America/Alaska 首府），**非俄北冰洋 Archangel（Arkhangelsk）**；真俄 Archangel 仅 MS-029-020 1 PN < 门。挂起真俄义；FC:6 的 New Archangel 作**新候选**析出入队。替补 Teheran。
- **Lyons 同名义项剔**：AWED-008-012「between the Northern and the [Lyons]」= 巴黎 Gare de Lyon 火车站，非里昂城，剔；取 ASC/DA/VB/FWB/MS 9 枚真里昂城确指（丝绸城 + 1784 Laurencin/Dampierre 升空史）。
- **既有页交叉核**：lyons/havre/corsica/sardinia/teheran 五 slug/label/alias（含 Lyon/Le Havre/Tehran）均无既有页碰撞。

**book 归属**：Lyons=FWB（里昂丝绸做气球皮）、Havre=SC2（Letourneur 父子故乡）、Corsica=OC（彗星吞没）、Sardinia=OC（同）、Teheran=ASC（大铁路支线/波斯首都）。

**建序防前向红链**：Corsica 先于 Sardinia（Sardinia 链 [[Corsica]]）。

本轮建 5 页：place 页数 300→305，registry 1368→1373，unknown 0。queue 开放候选 27→19（消化 5 + Lucknow/Archangel/Baltic 转挂起标记）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| lyons | kx8cdo | Five Weeks in a Balloon | real | 8 (ASC-001-043/012-033 + DA-001-035/001-090 + FWB-002-012/007-013 + MS-006-037 + VB-001-085) | 无 | 丝绸城/气球皮/1784 升空史；**剔 AWED-008-012 巴黎 Gare de Lyon**；alias Lyon |
| havre | yzIz1C | The Survivors of the Chancellor | real | 8 (AWED-003-012/032-002 + SC2-002-006/009-014 + TTLU-042-052/043-072 + WAI-001-019 + EHLA-012-003) | 无 | Letourneur 父子故乡/海峡港；alias Le Havre |
| corsica | 3wVFAu | Off on a Comet | real | 5 (AM-001-005 + MI-015-041/057-108 + OC-018-012 + TTLU-019-019) | 无 | 花岗岩岛/Bonifacio 洞/Catalan 冶铁 |
| sardinia | MfiqH2 | Off on a Comet | real | 5 (FWB-004-017 + OC-018-012/018-023/028-075/031-005) | 无 | Bonifacio 海峡随彗星消失/Nina 故乡；链 [[Corsica]] |
| teheran | gGVTbo | The Adventures of a Special Correspondent | real | 5 (ASC-001-043/008-028/008-061 + MS-024-005 + RC-013-020) | 无 | 波斯首都/大铁路支线/Elburz 山下；alias Tehran |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：8/8/5/5/5，全部达标 ✓
- 多实体/称号/异地同名筛：Lucknow 剔澳洲 Lucknow Road；Archangel 剔 Sitka New Archangel；Lyons 剔巴黎 Gare de Lyon ✓
- 既有页交叉核：5 建页 slug/label/alias（含 Lyon/Le Havre/Tehran）均无碰撞 ✓
- 跨源 book 惯例：Lyons=FWB、Havre=SC2、Corsica=OC、Sardinia=OC、Teheran=ASC ✓
- YAML 冒号门（LAW §8）：本轮 5 页 book/description 无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 5 页 0 段 over-400 ✓
- 前向红链：0（链目标 [[Five Weeks in a Balloon]]/[[Michael Strogoff]]/[[The Survivors of the Chancellor]]/[[Twenty Thousand Leagues Under the Sea]]/[[Mediterranean]]/[[Off on a Comet]]/[[Corsica]]/[[The Adventures of a Special Correspondent]] 均既建；Corsica 先于 Sardinia 建，无同轮前向红链）✓
- add_page warn：本轮 5 页 0 PN 警告 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R115→R116，NEW1）

- current_round 115→116
- type_round 86→87
- rounds_since_last_evv5 9→10
- rounds_since_last_discover 3→4
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 51→52
- last_updated_round 115→116

## 遗留问题

- **R116 预测 = EVV5（priority 1 抢占）**：R115 末 since_evv5=10≥evv5_interval(10) → 矩阵 priority 1 触发 EVV5；since_discover=4<10，故**不**附加 SCN28（EVV5 单发，非 EVV5+SCN28）。R116 为 place 类型质量抽评轮，非建页轮。执行前须读 `grow-state-machine.md`/`GROW.spec.md` 的 EVV5 定义；注意本项目 featured 分级已判无意义（parked featured-grader），EVV5 评估须据 PN 接地/schema 合规等实质维度，不倚赖 featured 自动分。
- **New Archangel 新候选**：FC:6（Sitka/Russian America 首府/Russian Fur Company 总部），real，aliases Sitka/New-Archangel，book The Fur Country；已核 sitka/new-archangel 未建。EVV5 后 NEW1 轮可建。
- **建页前复核清单（承前）**：Baltic 建前核 baltic-sea（alias Baltic Sea，防 blindspot 第 6 例）；Lena 核 lena-river；Himalaya alias Himalayas；Aral/Adriatic 海洋取确指句；Amou-Daria(Oxus) 别名。
- **discover blindspot 累积（5 例）**：pacific/atlantic/ural/caspian/baikal。建议 PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。归 HK-discover-existing-type-blindspot（PARK）。
- **同名陷阱累积**：Australian Alps(R112)/Texas Edinburgh(R112)/steamer Mongolia(R110)/Kentucky Frankfort(R114)/ship "Etna"(R114)/Paris Gare de Lyon(R115)/Australian Lucknow Road(R115)/Sitka New Archangel(R115)。probe 应增同名地/同名船/同名站消歧提示。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
