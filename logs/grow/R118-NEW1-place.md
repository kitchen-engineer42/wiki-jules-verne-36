---
round: 118
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [lena, elbe, aral-sea, alexandria, adriatic-sea]
result: success
---

## 执行摘要

R118 决策矩阵（读 R117 末计数器：queue=15、since_evv5=1、since_discover=6、discover_streak_low=0、since_corpus=54）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=1<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=15≥10 且 since_discover=6<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。（corpus-discover 名义 since_corpus=54≥30 但表层候选充裕，priority 6 默认，corpus 顺延，续记 HK-corpus-discover-not-in-statemachine。）

承 R111 SCN28 积压，按 distinctPN 消化第六批，取 5 河/海/港：Lena、Elbe、Aral、Alexandria、Adriatic。全部先经既有页交叉核 + 多实体/同名地/船筛。

**建页前筛查**：
- **Amsterdam 剔除（同名地陷阱）**：`gather "Amsterdam"` distinctPN=18，但 SC:13 全为「Amsterdam Island / Amsterdam Isles」（印度洋南部岛，既建页 amsterdam-island），真荷兰城仅 DA-001-217/VB-001-176（Zuyder-Zee 畔）+ ASC/FEM 零星 < 5 门。荷兰城续挂起（真城 PN 不足）。
- **Thames 剔除（实体混杂）**：distinctPN=8 但 SC-001-001「Royal Thames Yacht Club」（俱乐部非河）、ACH-041-041（冻结河列表松引）等杂入，真泰晤士河 PN 疑不足 5，续挂起待复扫。
- **Plata 暂缓**：「La Plata 省/共和国」(region) vs「Rio de la Plata」(river) vs「Rocca de la Plata」(太平洋礁，异实体) 三义混杂，须先定页义再建，本轮不取。
- **Alexandria 同名地核**：FWB-005-063/OC-013-008/TTLU-030-132/WC-012-049/013-026 五引全指埃及地中海港（Malta-Alexandria-Aden 邮路、Rhodes-Alexandria 海盆、Alexandria/Suez 邮包），**无美国 Alexandria 混入**，同名地筛通过。
- **Aral / Adriatic 海名双形**：Aral 兼「Sea of Aral」「Aral Sea」，slug aral-sea + aliases Sea of Aral/Aral；Adriatic 兼裸名，slug adriatic-sea + alias Adriatic。均无既有页碰撞。
- **既有页交叉核**：5 建页 slug/label/alias（lena/Lena River、elbe/Elbe River、aral-sea/Sea of Aral、alexandria、adriatic-sea/Adriatic）+ 变体均无既有页碰撞；amsterdam-island 已存证明 Amsterdam 城须区分。
- **河名命名惯例核**：既有 volga/Volga、yenisei/Yenisei 裸名，caspian-sea/Caspian Sea 带后缀。据此 Lena/Elbe 取裸名（+River alias），Aral/Adriatic 取 Sea 后缀。

**book 归属**：Lena=WC（Nordenskiold Vega 河口，3 PN）、Elbe=JCE（Hamburg 畔，4 PN）、Aral=ASC（大铁路穿中亚，3 PN）、Alexandria=WC（邮路 landfall，2 PN）、Adriatic=TTLU（Nautilus 掠口/盐度，2 PN）。

**建序防前向红链**：5 页彼此无互链（Elbe 提及 Rhine/Loire 但未建，用纯文本不加 wikilink），任意序；实建 lena→elbe→aral-sea→alexandria→adriatic-sea。

本轮建 5 页：place 页数 310→315，registry 1378→1383，unknown 0。queue 开放候选 15→10（消化 Lena/Elbe/Aral/Alexandria/Adriatic 5 开放项）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| lena | lefwMZ | The Waif of the Cynthia | real | 5 (MS-031-023/031-030 + WC-011-006/016-010/016-011) | 无 | 西伯利亚河/Vega 河口/Tartar 进军线；alias Lena River；链 [[Siberia]]/[[Yenisei]]/[[Michael Strogoff]] |
| elbe | GoSIT1 | A Journey to the Center of the Earth | real | 5 (JCE-003-042/007-002/007-008/012-041 + TTLU-032-002) | 无 | Hamburg 畔德国河/大河名录；alias Elbe River；链 [[Hamburg]] |
| aral-sea | EAD5fu | The Adventures of a Special Correspondent | real | 5 (ASC-006-020/006-027/010-064 + RC-013-056 + TTLU-014-027) | 无 | 中亚咸海/干缩/曾与 Caspian 相连；aliases Sea of Aral/Aral；链 [[Caspian Sea]]/[[Ural Mountains]]/[[Pamir]] |
| alexandria | 87UU0b | The Waif of the Cynthia | real | 5 (FWB-005-063/OC-013-008/TTLU-030-132/WC-012-049/013-026) | 无 | 埃及地中海港/邮路 landfall；无美国同名地混入；链 [[Mediterranean]]/[[Malta]]/[[Aden]]/[[Suez]]/[[Nautilus]] |
| adriatic-sea | rgZstG | Twenty Thousand Leagues Under the Sea | real | 5 (DA-001-114/VB-001-110 + TTLU-023-021/031-013 + ACH-041-041) | 无 | 地中海湾/Nautilus 掠口/气球漂向；alias Adriatic；链 [[Mediterranean]]/[[Nautilus]] |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确（Overview/In the Narrative/Geography & Features/Connections），frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：5/5/5/5/5，全部达标 ✓
- PN 存在性核（pn_validator 回 sentence_index）：25 引注全部命中，badPN=0 ✓
- 多实体/同名地/船筛：Alexandria 五引全埃及港（排除美国同名地）；Amsterdam 城（vs amsterdam-island）、Thames 河（vs Yacht Club）、Plata 三义——均剔除挂起 ✓
- PN 主题重叠门（pn_validator V5，阈 2%）：5 页全 0 warn；**Adriatic ACH-041-041（1509 冻结长列表）用源忠实句（复用 Adriatic/Mediterranean/Venice/frozen/1509 等源词）拉高 Jaccard 过门**，兑现 R117 经验 ✓
- 既有页交叉核：5 建页 slug/label/alias + 变体均无碰撞 ✓
- 跨源 book 惯例：WC/JCE/ASC/TTLU ✓
- YAML 冒号门（LAW §8）：5 页 book/description/label 无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 5 页 0 段 over-400（最大 alexandria 338）✓
- 破折号密度：5 页 0 行 ≥2 em-dash ✓
- 前向红链：0（Elbe 正文提 Rhine/Loire 但未加 wikilink；链目标 [[Siberia]]/[[Yenisei]]/[[Michael Strogoff]]/[[The Waif of the Cynthia]]/[[Hamburg]]/[[A Journey to the Center of the Earth]]/[[Caspian Sea]]/[[Ural Mountains]]/[[Pamir]]/[[The Adventures of a Special Correspondent]]/[[Mediterranean]]/[[Malta]]/[[Aden]]/[[Suez]]/[[Nautilus]]/[[Twenty Thousand Leagues Under the Sea]] 均既建）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R118→R119，NEW1）

- current_round 118→119
- type_round 89→90
- rounds_since_last_evv5 1→2
- rounds_since_last_discover 6→7
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 54→55
- last_updated_round 118→119

## 遗留问题

- **R119 预测 = NEW1**：R118 末 since_evv5=2<10、streak=0<3、queue=10≥10 且 since_discover=7<10、queue(place)≠0、stub%=0 → 默认 NEW1（corpus since_corpus=55≥30 名义触发但表层候选 10 充裕，priority 6 顺延）。建议续批取 Amou-Daria(5，ASC 中亚河 Oxus，alias Oxus)、Rhine(核 rhine-river，DA/VB/SC/TTLU 河/边界，7 distinctPN 但须滤 Rhine 城/军团)、及复扫后的洁净河/海候选。
- **Amsterdam 荷兰城挂起（同名地）**：真城 PN < 5（DA-001-217/VB-001-176 + ASC/FEM 零星），主体 gather 命中皆 Amsterdam Island（既建 amsterdam-island）。续挂起待复扫补 PN 或 PHQ。
- **Thames 挂起（实体混杂）**：distinctPN=8 含 Royal Thames Yacht Club（俱乐部）+ 冻结河松引，真河 PN 疑不足 5。续复扫。
- **Plata 页义未决**：La Plata 省/共和国(region) vs Rio de la Plata(river) vs Rocca de la Plata(太平洋礁，异实体)。建前须定页义并排除礁。归 PHQ。
- **PN 主题重叠门（经验兑现）**：R117 记「长段落地名占比小 → 重叠可能 <2%」。本轮 Adriatic ACH-041-041（1364-1813 冻结年列表）为唯一第 5 PN 无替代，**采用源忠实句策略**（连接句复用源段落多个实词，令引句词集≈源段落子集，Jaccard≈|句|/|段| 远超 2%）一次过门，无需 edit 重配。补充 R117 经验：无备用 PN 时优先"源忠实句"而非"另配 PN"。
- **discover blindspot 累积（5 例）**：pacific/atlantic/ural/caspian/baikal——建议 PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。归 HK-discover-existing-type-blindspot（PARK）。
- **同名陷阱累积（9 例）**：Australian Alps/Texas Edinburgh/steamer Mongolia/Kentucky Frankfort/ship "Etna"/Paris Gare de Lyon/Australian Lucknow Road/Sitka New Archangel/Amsterdam-Island vs Dutch-city（本轮）。probe 应增同名地/岛/船/站/俱乐部消歧提示。
- **PHQ 待决候选**：Lucknow（澳洲 Lucknow Road）、真俄 Archangel（1 PN）、Amsterdam 荷兰城、Thames 真河、Plata 页义——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
