---
round: 110
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [kamtschatka, prussia, belgium, mongolia, ganges]
result: success
---

## 执行摘要

R110 决策矩阵（读 R109 末计数器：queue=14、since_evv5=4、since_discover=6、discover_streak_low=0、since_corpus=46）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=4<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=14≥10（未低于阈值 10）且 since_discover=6<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。（priority 3.5 corpus-discover 死分支，见 HK-corpus-discover-not-in-statemachine，不赘。）

承 R109 续批 NEW1 消化 discover 残余中候选（国别/半岛/河流层），本轮取 Kamtschatka/Prussia/Belgium/Mongolia/Ganges，全部先经既有页交叉核 + 多实体/词边界筛。

**建页前筛查**：
- **Mongolia 词边界剔汽船**：totalHits 35、AWED:24 全系 Peninsular & Oriental 汽船「Mongolia」（同 Victoria 噪声型），非国名 → 剔尽 AWED，仅取 ASC:5（bazaars/brigands/Great Wall/deserts）+ TT:1（洲级重划）共 6 枚真国名确指。book=ASC。
- **Kamtschatka 恰达门**：5 distinctPN，RC:2（Robur 掠 Behring 海/Petropaulovski+Kloutschew 火山）substantive，MS:2（西伯利亚 Okhotsk-Kamtschatka 区划）、ASC:1（远东同义）；alias Kamchatka。book=Michael Strogoff（俄属远东，主题连贯）。
- **Prussia**：TTLU:3（Krupp 引擎/审查列国/Sadova 停战）为主，FEM(thaler 认捐)/SC(Paganel 列强)/OC(地图拟人)，6 枚真国确指，全非明喻。book=TTLU。
- **Belgium**：六源各 1（FEM 认捐/FF 溶洞/JCE 颌骨/UC 煤词源/VB 气球战役/WC 铁路过境），6 枚真国确指。book=FEM（认捐惯例，同其他欧洲国页）。
- **Ganges 真河充分**：8 distinctPN，AWED:6（Fogg 铁路/汽船/Allahabad 圣河汇/Benares 河谷）substantive、TTLU:1（恒河载尸出海）、ASC:1（Oxus 比拟）；alias Ganges River。book=AWED。
- **既有页交叉核**：kamtschatka/prussia/belgium/mongolia/ganges 五 slug/label 均无既有页碰撞（含 Kamchatka 别名）。

本轮建 5 页：place 页数 280→285，registry 1348→1353，unknown 0。queue 开放候选 14→9（消化 5）。**queue=9 已低于 discover_queue_threshold=10 → R111 触发 SCN28 补充勘探。**

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| kamtschatka | 6vpGmZ | Michael Strogoff | real | 5 (ASC-017-008 + MS-003-002/004-039 + RC-011-047/011-049) | 无 | Behring 海/Petropaulovski+Kloutschew 火山/西伯利亚区划；alias Kamchatka |
| prussia | i8nQs6 | Twenty Thousand Leagues Under the Sea | real | 6 (FEM-012-017 + SC-038-087 + TTLU-002-010/013-047/044-033 + OC-044-011) | 无 | Krupp 引擎/审查列国/Sadova 停战/thaler 认捐 |
| belgium | pJpQsS | From the Earth to the Moon | real | 6 (FEM-012-019 + FF-009-019 + JCE-038-007 + UC-004-005 + VB-001-102 + WC-021-029) | 无 | 认捐 513k 法郎/Han-sur-Lesse 溶洞/煤词源/气球战役 |
| mongolia | IG8l6H | The Adventures of a Special Correspondent | real | 6 (ASC-001-043/008-041/008-054/021-001/024-004 + TT-015-018) | 无 | 戈壁/大铁路/Great Wall；**词边界剔 AWED:24 汽船 Mongolia** |
| ganges | TpM9cR | Around the World in Eighty Days | real | 7 (AWED-010-004/010-005/012-010/014-006/014-024 + TTLU-025-040 + ASC-010-064) | 1 段（Mongolia 无关，此处 Ganges 建前复验合规）| 圣河/Allahabad 汇流/载尸出海；TTLU-025-040 warn(重叠 1.8%<2%) 保留，余 6 达门 |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：5/6/6/6/7，全部达标 ✓
- 多实体/词边界筛查：Mongolia 剔 AWED:24 汽船（保留 6 真国名）；Kamtschatka 恰达 5 门；Ganges 真河 substantive ✓
- 既有页交叉核：5 建页 slug/label/alias 均无既有页碰撞（含 Kamchatka 别名）✓
- 跨源 book 惯例：各取最集中/最具叙事分量之作（Kam=MS、Prussia=TTLU、Belgium=FEM、Mongolia=ASC、Ganges=AWED）✓
- YAML 冒号门（LAW §8）：本轮 5 页 book/description 无冒号裸值 → unknown=0 ✓
- ≤400 字门：mongolia Geography 段建前超限，已缩写至合规；建后复验 5 页 0 段 over-400 ✓
- 前向红链：0（链目标 [[Russia]]/[[Siberia]]/[[Caucasus]]/[[Austria]]/[[Nautilus]]/[[Gun Club]]/[[Sweden]]/[[China]]/[[Bombay]]/[[Benares]]/[[Twenty Thousand Leagues Under the Sea]] 均既建；France/England/Newfoundland/Great Eastern 未既建，不链）✓
- add_page warn：ganges TTLU-025-040 重叠 1.8%<2%（mode=warn 非阻断，余 6 PN≥5 达门，保留）
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R110→R111，NEW1）

- current_round 110→111
- type_round 81→82
- rounds_since_last_evv5 4→5
- rounds_since_last_discover 6→7
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 46→47
- last_updated_round 110→111

## 遗留问题

- **R111 预测 = SCN28（surface-discover）**：R110 末 queue=9 < discover_queue_threshold=10 → 权威算法 priority 3 触发 SCN28。执行 sentence_index 专名扫描补充 place 候选入 queue，同时递增 since_discover→重置。**扫描结果须逐一比对 alias_index 去重**（承 R107 blindspot：pacific/atlantic/ural 型伪新），并预筛多实体/明喻噪声。
- **洲级严筛专轮（未决）**：America(259)/Europe(201)/Asia(86) 仍 HOLD；泛指高发，America 须与 united-states 错开。SCN28 后择机专轮。
- **HOLD 累积**：Amsterdam（SC:13 岛群非城）、Athens/Rome（明喻系）、Petersburg（缩写碎片）、Rhine/Thames/Plata（明喻/真河<5）、Long Island/Bay of Bengal（真指<5）。
- **discover blindspot（承 R107）**：宜给 pacific-ocean/atlantic-ocean 补 alias 'Pacific'/'Atlantic'，ural-mountains 补 'Ural'（PHQ 处理）。
- **memex 规范缺陷**：GROW.spec.md priority 3.5 corpus-discover 未同步权威算法（HK-corpus-discover-not-in-statemachine，P3 PARK）。
- **EVV5 节奏**：since_evv5 R110 末=5，下次约 R115。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
- **England/France 国级页 + R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理。
