---
round: 117
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [new-archangel, dublin, himalaya, crete, astrakhan]
result: success
---

## 执行摘要

R117 决策矩阵（读 R116 末计数器：queue=19、since_evv5=0、since_discover=5、discover_streak_low=0、since_corpus=53）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=0<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=19≥10 且 since_discover=5<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 积压，按 distinctPN 降序消化第五批。全部先经既有页交叉核 + 多实体/称号/异地同名筛。

**建页前筛查**：
- **New Archangel（承 R115 析出候选）**：FC:6 = Sitka 岛上的 Russian America 首府/Russian Fur Company 总部；`gather "New Archangel"` distinctPN=5（FC-034-007/036-035/045-033/047-004 + FC-030-054 的 Sitka/New-Archangel 建置句）。真俄北冰洋 Archangel（Arkhangelsk）仅 MS-029-020 1 PN<门，续挂起（见遗留）。取 label「New Archangel」、aliases Sitka/New-Archangel、book The Fur Country。
- **Astrakhan 同名/名源辨析**：RC:3 为真城确指（RC-013-060 鱼获运往/RC-014-009 里海北端 Star of the Desert/RC-014-011 距 Moscow 1200 英里）；MS-005-053 = 沙皇尊号「Czar of Kazan and Astrakhan」（阿斯特拉罕汗国/城，真地引）；MS-005-019 = 「cap of Astrakhan fur」，**皮草以城为名**（比照 Lyons 丝绸的城市名源引，非异地同名），作城市名源句引。合计 5 distinctPN。
- **Astrakhan PN 主题重叠门自查 + 修正**：add_page warn 报 MS-005-053 主题重叠 1.46%<2%（长段落沙皇尊号，Astrakhan 占比小）；Dublin 报 AWED-033-063 重叠 1.52%。二者引注真实（AWED-033-063 含「at dawn... they were in Dublin」；MS-005-053 含「Czar of Kazan and Astrakhan」），但连接句主题偏松。**edit_page 重配引注**：将两松句改配高重叠 PN（Dublin Connections 改配 AWED-033-060 邮路句、Astrakhan Connections 改配 RC-014-011 Volga 句，[[书]] 链移入 In the Narrative），复验二页 warn=0。
- **既有页交叉核**：5 建页 slug/label/alias（含 Sitka/New-Archangel/Himalayas/Candia）+ 变体（Archangel/Arkhangelsk/Bering Strait/Mount Everest 等）均无既有页碰撞。

**book 归属**：New Archangel=FC（Russian America 首府）、Dublin=AWED（邮路中转/Fogg 归程）、Himalaya=ASC（Pamir 山系确指最密）、Crete=TTLU（Nautilus 掠岸/反抗奥斯曼）、Astrakhan=RC（里海北端 aeronef 掠城）。

**建序防前向红链**：5 页彼此无互链，任意序；实建 new-archangel→dublin→himalaya→crete→astrakhan。

本轮建 5 页：place 页数 305→310，registry 1373→1378，unknown 0。queue 开放候选 19→15（消化 Himalaya/Dublin/Crete/Astrakhan 4 开放项 + New Archangel 由 ○ 候选转 ✔）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| new-archangel | YDtOgc | The Fur Country | real | 5 (FC-030-054/034-007/036-035/045-033/047-004) | 无 | Sitka 岛/Russian America 首府/Russian Fur Company 总部；aliases Sitka/New-Archangel；链 [[Aleutian Islands]]/[[Behring Strait]]/[[Victoria Island]] |
| dublin | f4vyPQ | Around the World in Eighty Days | real | 5 (AWED-033-060/033-063 + FC-001-024 + TT-015-015/015-024) | 无 | 爱尔兰城/跨大西洋邮路中转/Fogg 归程；**edit 重配 AWED-033-063→AWED-033-060 提主题重叠** |
| himalaya | OuPLmg | The Adventures of a Special Correspondent | real | 5 (ASC-015-033/018-042 + AWED-014-010/016-004 + DSCF-022-096) | 无 | Pamir 山系/最高峰/Everest；alias Himalayas；链 [[Pamir]] |
| crete | c3g4ex | Twenty Thousand Leagues Under the Sea | real | 5 (TTLU-018-005/030-071/030-072/030-083/032-079) | 无 | 地中海岛/Candia/反抗奥斯曼/Nautilus 掠岸；alias Candia；链 [[Nautilus]]/[[Captain Nemo]]/[[Mediterranean]] |
| astrakhan | xmlbg2 | The Clipper of the Clouds | real | 5 (RC-013-060/014-009/014-011 + MS-005-053/005-019) | 无 | 里海北端城/Star of the Desert/astrakhan 皮草名源；**edit 重配 MS-005-053→RC-014-011 提主题重叠**；链 [[Caspian Sea]]/[[Moscow]]/[[Volga]]/[[Michael Strogoff]] |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立（dublin/astrakhan 另经 `edit_page.py` 修正引注），未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：5/5/5/5/5，全部达标 ✓
- PN 存在性核（回 sentence_index sid 段号）：25 引注全部命中，badPN=0 ✓
- 多实体/称号/异地同名筛：New Archangel(Sitka) vs 真俄 Archangel(Arkhangelsk) 挂起；Astrakhan 皮草作城市名源引（非异地同名）✓
- PN 主题重叠门（pn_validator V5，阈 2%）：初建 dublin/astrakhan 各 1 warn → edit_page 重配后 5 页全 0 warn ✓
- 既有页交叉核：5 建页 slug/label/alias + 变体均无碰撞 ✓
- 跨源 book 惯例：FC/AWED/ASC/TTLU/RC ✓
- YAML 冒号门（LAW §8）：5 页 book/description/label 无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 5 页 0 段 over-400 ✓
- 破折号密度：5 页 0 行 ≥2 em-dash（Astrakhan 鱼获列表改用括号避免 dash 对）✓
- 前向红链：0（链目标 [[Aleutian Islands]]/[[Behring Strait]]/[[Victoria Island]]/[[The Fur Country]]/[[Liverpool]]/[[Ireland]]/[[London]]/[[Edinburgh]]/[[Paris]]/[[Around the World in Eighty Days]]/[[Pamir]]/[[The Adventures of a Special Correspondent]]/[[Nautilus]]/[[Captain Nemo]]/[[Mediterranean]]/[[Twenty Thousand Leagues Under the Sea]]/[[Caspian Sea]]/[[Moscow]]/[[Volga]]/[[Michael Strogoff]]/[[The Clipper of the Clouds]] 均既建）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R117→R118，NEW1）

- current_round 117→118
- type_round 88→89
- rounds_since_last_evv5 0→1
- rounds_since_last_discover 5→6
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 53→54
- last_updated_round 117→118

## 遗留问题

- **R118 预测 = NEW1**：R117 末 since_evv5=1<10、streak=0<3、queue=15≥10 且 since_discover=6<10、queue(place)≠0、stub%=0 → 默认 NEW1（corpus-discover 名义 since_corpus=54≥30 但表层候选 15 充裕，priority 6 默认，corpus 顺延）。建议续批取 Lena(5，核 lena-river/alias Lena River)、Elbe(5，alias Elbe River)、Aral(5，核 aral-sea/alias Aral Sea)、Amou-Daria(5，alias Oxus)、Alexandria(5，核与美国同名地)、Adriatic(5，核 adriatic-sea/alias Adriatic Sea)。建前逐一跑 slug/label/alias 变体交叉核 + 同名地/船/站消歧 + PN 主题重叠自查。
- **真俄 Archangel（Arkhangelsk）挂起**：MS-029-020 仅 1 PN<门，续挂起待 PHQ；已与本轮 New Archangel（Sitka）区分。
- **建页前复核清单（承 R116）**：Baltic 核 baltic-sea；Lena 核 lena-river；Aral 核 aral-sea；Adriatic 核 adriatic-sea；Amou-Daria(Oxus) 别名；Alexandria 核埃及港 vs 美国同名地。
- **PN 主题重叠门（新增经验）**：长段落（沙皇尊号、Fix/Fogg 叙事段）中地名占比小时，即便引注真实，pn_validator V5 重叠可能<2%。建页时连接句应优先配主题词密集的目标段（如城市直述句），或 edit_page 重配。已作本轮实践记录。
- **discover blindspot 累积（5 例）**：pacific/atlantic/ural/caspian/baikal——建议 PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。归 HK-discover-existing-type-blindspot（PARK）。
- **同名陷阱累积（8 例）**：Australian Alps/Texas Edinburgh/steamer Mongolia/Kentucky Frankfort/ship "Etna"/Paris Gare de Lyon/Australian Lucknow Road/Sitka New Archangel（本轮正解为 New Archangel 建页 + 真俄 Archangel 挂起）。probe 应增同名地/船/站消歧提示。
- **PHQ 待决候选**：Lucknow（SC:7 全澳洲 Lucknow Road，非印度城，过薄）、真俄 Archangel（1 PN<门）——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
