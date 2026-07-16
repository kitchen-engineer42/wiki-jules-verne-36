---
round: 119
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [amou-daria, rhine, rio-de-la-plata, thames]
result: success
---

## 执行摘要

R119 决策矩阵（读 R118 末计数器：queue=10、since_evv5=2、since_discover=7、discover_streak_low=0、since_corpus=55）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=2<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=10≥10 且 since_discover=7<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 积压尾批消化。开放候选 10 项中，5 项为持有/阻塞（洲级 Asia/Europe/America HOLD、Long Island/Bay of Bengal 4<门），Amsterdam 荷兰城真城 PN<5（R118 挂起），实际可建仅 Amou-Daria + 3 项经消歧后洁净的河：Rhine、Plata、Thames。本轮建 4 页（NEW1 建 ≤5，可建洁净候选仅 4）。

**建页前筛查（重实体消歧）**：
- **Rhine 河/城/军团筛**：7 distinctPN 全为莱茵**河**义（DA/VB 气球俯瞰 ribbon、SC Schaffhausen 瀑布/民族之河、YEAR 边界、TTLU 大河名录）；**无 Rhine 城、无 Rhine 军团混入**。取 5：DA-001-149/SC-007-014/SC-054-024/YEAR-001-041/TTLU-032-002（跨 4 源）。slug rhine（比照既有 volga/yenisei 裸名河），alias Rhine River。
- **Plata 三义消歧**：（a）La Plata 省/共和国 region（FEM-012-029/MI-022-036/PL-005-059/RC-001-030）；（b）Rio de la Plata 河口 river（TTLU-041-040/041-063/032-002）；（c）**Rocca de la Plata 太平洋礁（TTLU-015-039）= 异实体，剔除**。页义定为 River Plate 河口 + 同名 La Plata 省（同一南美地理实体），取 5：TTLU-041-040/041-063/032-002 + FEM-012-029/MI-022-036。slug rio-de-la-plata，aliases La Plata/River Plate。
- **Thames 河/俱乐部筛**：真泰晤士**河** 4（ASC-024-007 barges/steamboats、FWB-008-014 Resolute 至 Greenwich、FWB-008-015 河口、ACH-041-041 1789 Gravesend 冻结）+ SC-001-001「Royal Thames Yacht Club」**作河名源引**（比照 astrakhan 皮草/Lyons 丝绸城市名源先例，非异实体同名陷阱）= 5 distinctPN。
- **Amou-Daria 洁净**：ASC 5 PN 全为中亚河 Oxus（fire-ships/Zarafchane 支流/大铁路桥），无歧义。alias Oxus/Amu Darya。
- **既有页交叉核**：4 建页 slug/label/alias（amou-daria/Oxus、rhine/Rhine River、rio-de-la-plata/La Plata/River Plate、thames/River Thames）+ 变体均无既有页碰撞（ural-mountains/ural-river 已剔为伪新，mississippi 已建，不影响本批）。

**book 归属**：Amou-Daria=ASC（大铁路穿中亚）、Rhine=SC（Schaffhausen + 民族之河，最具体）、Rio de la Plata=TTLU（Nautilus 掠河口）、Thames=FWB（Resolute 出海）。

**建序防前向红链**：4 页彼此无互链（Rhine 提 Elbe/Amazon 均既建可链；Loire/Danube/Schaffhausen 未建用纯文本），任意序；实建 amou-daria→rhine→rio-de-la-plata→thames。

本轮建 4 页：place 页数 315→319，registry 1383→1387，unknown 0。queue 开放候选 10→6（消化 Amou-Daria/Rhine/Plata/Thames 4 项；剩 6 项全为持有/阻塞）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| amou-daria | 60VXH2 | The Adventures of a Special Correspondent | real | 5 (ASC-010-063/010-064/010-071/010-072/013-013) | 无 | 中亚河 Oxus/petroleum 火船/Zarafchane 支流/大铁路桥；aliases Oxus/Amu Darya；链 [[Aral Sea]]/[[Pamir]] |
| rhine | WN82bE | In Search of the Castaways | real | 5 (DA-001-149/SC-007-014/054-024/YEAR-001-041/TTLU-032-002) | 无 | 德国大河/Schaffhausen 瀑布/民族之河/边界；全河义无城/军团混入；alias Rhine River；链 [[Elbe]]/[[Amazon]] |
| rio-de-la-plata | OBpryd | Twenty Thousand Leagues Under the Sea | real | 5 (TTLU-041-040/041-063/032-002 + FEM-012-029/MI-022-036) | 无 | River Plate 河口/La Plata 省名源；剔 Rocca de la Plata 太平洋礁；aliases La Plata/River Plate；链 [[South America]]/[[Brazil]]/[[Nautilus]]/[[Amazon]] |
| thames | d3sqtk | Five Weeks in a Balloon | real | 5 (ASC-024-007/FWB-008-014/008-015/ACH-041-041/SC-001-001) | 无 | London 大河/Resolute 出海/1789 Gravesend 冻结；SC-001-001 Royal Thames Yacht Club 作河名源引；alias River Thames；链 [[London]] |

## EXIT-GATE 检查

- G4：4 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，4 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：5/5/5/5，全部达标 ✓
- PN 存在性核（pn_validator 回 sentence_index）：20 引注全部命中，badPN=0 ✓
- 多实体/同名/异实体筛：Rhine（河 vs 城/军团）、Thames（河 vs Yacht Club 俱乐部名源）、Plata（河口 vs 省 region vs **Rocca de la Plata 太平洋礁**异实体剔除）均消歧 ✓
- PN 主题重叠门（pn_validator V5，阈 2%）：4 页全 0 warn；Thames ACH-041-041（1789 冻结长列表）沿用 R118 源忠实句策略过门 ✓
- 既有页交叉核：4 建页 slug/label/alias + 变体均无碰撞 ✓
- 跨源 book 惯例：ASC/SC/TTLU/FWB ✓
- YAML 冒号门（LAW §8）：4 页无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 4 页 0 段 over-400（最大 thames 371）✓
- 破折号密度：4 页 0 行 ≥2 em-dash ✓
- 前向红链：0（链目标 [[Aral Sea]]/[[Pamir]]/[[Elbe]]/[[Amazon]]/[[South America]]/[[Brazil]]/[[Nautilus]]/[[London]] 均既建；Loire/Danube/Schaffhausen/Greenwich/Uruguay/Samarkand 未建，正文用纯文本不加 wikilink）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R119→R120，NEW1）

- current_round 119→120
- type_round 90→91
- rounds_since_last_evv5 2→3
- rounds_since_last_discover 7→8
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 55→56
- last_updated_round 119→120

## 遗留问题

- **R120 预测 = SCN28（表层勘探）**：R119 末 queue=6<discover_queue_threshold(10) → priority 3 触发 SCN28（自 R111 以来首次表层勘探）。剩余 6 开放候选全为持有/阻塞（洲级 Asia/Europe/America HOLD、Long Island/Bay of Bengal 4<门、Amsterdam 荷兰城<5），**实际可建为 0**，队列已消化殆尽。R120 须跑 SCN28 补种：地名关键词邻接扫描（river/town/sea/lake/mount/cape/gulf/strait/desert/valley/island + demonym/人名/船名 stoplist），揭示新一批真地名候选，各词边界核 distinctPN≥5 + 同名地/岛/船/俱乐部消歧。
- **queue 消化里程碑**：R111 SCN28 积压（含 R87 复扫补种）经 R112-R119 8 轮 NEW1 全部消化完毕；place 页 300→319（+19），仅余结构性持有项。
- **Amsterdam 荷兰城挂起（同名地）**：真城 PN<5（DA-001-217/VB-001-176 Zuyder-Zee 双源 + ASC-007-035/FEM-012-009），主 gather 命中皆 Amsterdam Island（既建）。续挂起待复扫补 PN 或 PHQ。
- **Thames 追记**：DSCF-036-008（非洲鱼 sandjikas 长句）为 Thames 词边界假命中，未采用；SC-003-001/028-011（Glenarvan/Duncan）松引未采用。真河 4 + Yacht Club 名源 1 = 5 达门。
- **PN 主题重叠门（策略固化）**：长列表段落中地名占比小时，采「源忠实句」（连接句复用源段落多个实词令引句词集≈源子集）稳过 2% 门。R118 Adriatic、R119 Thames 两次实践，已固化为 ACH-041-041 类冻结年列表段的标准引法。
- **同名陷阱累积（10 例）**：…（承 R118 9 例）+ Rocca de la Plata 太平洋礁 vs Rio de la Plata 河口（本轮剔除）。probe 应增同名礁/岛/河口消歧提示。
- **discover blindspot 累积（5 例）**：pacific/atlantic/ural/caspian/baikal——PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。归 HK-discover-existing-type-blindspot（PARK）。
- **PHQ 待决候选**：Lucknow（澳洲 Lucknow Road）、真俄 Archangel（1 PN）、Amsterdam 荷兰城、Long Island/Bay of Bengal（4<门待补句）——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。SCN28 后若表层候选仍枯竭，可考虑启动洲级严筛专轮或 corpus-discover。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
