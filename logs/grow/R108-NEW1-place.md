---
round: 108
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [new-york, paris, madrid, constantinople, lisbon]
result: success
---

## 执行摘要

R108 决策矩阵（读 R107 末计数器：queue≈25、since_evv5=2、since_discover=4、discover_streak_low=0、since_corpus=44）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=2<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue≈25≥10 且 since_discover=4<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。（priority 3.5 corpus-discover 死分支，见 HK-corpus-discover-not-in-statemachine，不赘。）

承 R107 续批 NEW1 消化 discover 城市层候选，本轮取欧美城市层 5 候选，全部先经既有页交叉核 + 多实体/称号筛。

**建页前筛查（本轮 1 候选 HOLD）**：
- **Athens → HOLD（称号系明喻）**：8 distinctPN 中 6+ 为「Athens of X」epithet/明喻——"Athens of India"=Benares、"Northern/Modern Athens"=Edinburgh、"Athens of the North"=Stockholm/Krasnoiarsk。真雅典城确指仅 ASC-017-036(37°线过雅典)/UC-014-069(Parthenon at Athens)/TTLU-033-062(古雅典 Atlantis) ≈2-3<门。同 Rome 明喻处置。
- **Constantinople 多实体筛**：MS-006-005/032「the sign of the City of Constantinople」= 客栈招牌名，非城市，剔；取 FEM(攻城/银行)/RC(飞人)/TT(时区)/DOSE(拜占庭皇帝) 5 枚真城确指句。
- **Madrid**：剔纯列举，取 OC(彗星撕走旧址)/TTLU(Philip V 维哥令)/WC(Bredejord 电报中继)/TT(时区)/YEAR(prefecture) 6 枚。
- **Lisbon**：取 DSCF(殖民政府/Lisbon 口音)/WC(Gibraltar-Suez 途经港)/SC(180 里格外)/RC(飞僧 Volador) 5 枚。
- **既有页交叉核**：new-york/paris/madrid/constantinople/lisbon 五 slug/label 均无既有页碰撞（吸取 R107 Pacific/Atlantic/Ural 伪新教训，建前逐一 pages.json 核）。

本轮建 5 页：New York（WC Cynthia 调查枢纽/跨洋门户）、Paris（AWED 环球首站/Passepartout 故里）、Madrid（WC 电报中继/OC 彗星）、Constantinople（FEM 攻城巨炮史）、Lisbon（DSCF 殖民政府）。place 页数 270→275，registry 1338→1343，unknown 0。queue 开放候选 25→19（消化 5 + Athens HOLD）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| new-york | 10zt4V | The Waif of the Cynthia | real | 8 (AWED-024-008/024-010/025-006/026-002 + WC-006-043/008-003/008-004/008-021) | 无 | 跨洋汽船枢纽/Cynthia 调查地/Broadway；alias New York City |
| paris | 45yIVv | Around the World in Eighty Days | real | 8 (AWED-002-007/004-020/004-032/007-031/008-012/025-006 + ASC-001-035/009-003) | 无 | Fogg 环球首站/Passepartout 故里/Boulevard des Italiens |
| madrid | 5h0a8u | The Waif of the Cynthia | real | 6 (OC-016-022/TTLU-032-060/WC-015-023/015-031/TT-019-008/YEAR-001-041) | 无 | WC 电报中继/彗星撕走旧址/Philip V 维哥宝藏令 |
| constantinople | x8wIdh | From the Earth to the Moon | real | 5 (DOSE-001-002/FEM-007-055/012-009/RC-004-046/TT-019-010) | 无 | 1453 攻城巨炮史/Ottoman Bank；**剔 MS 客栈招牌名** |
| lisbon | Cr2UaH | Dick Sand: A Captain at Fifteen | real | 5 (DSCF-025-022/027-037/RC-004-046/SC-007-054/WC-015-023) | 无 | 殖民政府/大西洋港/飞僧 Volador；book 冒号引号 |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：8/8/6/5/5，全部达标 ✓
- 多实体/称号筛查：Athens 称号系剔（HOLD）、Constantinople 剔客栈招牌名、Madrid/Lisbon 剔纯列举取确指 ✓
- 既有页交叉核：5 建页 slug/label 均无既有页碰撞（承 R107 教训逐一核 pages.json）✓
- 跨源 book 惯例：各取单作最集中/最具叙事分量之作定 book（NY=WC、Paris=AWED、Madrid=WC、Constantinople=FEM、Lisbon=DSCF）✓
- YAML 冒号门（LAW §8）：lisbon `book: 'Dick Sand: A Captain at Fifteen'` 加引号 → unknown=0 ✓
- ≤400 字门：建前复验 5 页 0 段 over-400 ✓
- 前向红链：0（book label ×5 均既建；[[San Francisco]]/[[London]]/[[Suez]]/[[United States]]/[[Gun Club]]/[[Mediterranean]] 均既建；未既建者不链）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R108→R109，NEW1）

- current_round 108→109
- type_round 79→80
- rounds_since_last_evv5 2→3
- rounds_since_last_discover 4→5
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 44→45
- last_updated_round 108→109

## 遗留问题

- **R109 预测 = NEW1（续消化 discover 残余）**：R108 末 queue≈19。矩阵 since_evv5=3、since_discover=5、queue≥10 → priority 3 不触发；default NEW1。建议 R109 取 Berlin/Vienna（城市层，7±，列举/机构义为主但真城，含 observatory 争议 RC-001-025 substantive）或 Europe/Asia/America（洲级，严筛泛指，America 与 united-states 错开）或 Guiana（EHLA 9）/Calais（6）。
- **城市层列举义顾虑**：Berlin/Vienna 真城确指多为「地理学会/observatory/Gun Club 认捐城」列举，叙事场景少；仍达 ≥5 真城义门（非明喻），可建但偏薄。建页须取 substantive 句（observatory 争议/Berlin Conference/aeronaut 离散）为主。
- **HOLD 累积**：Athens（称号系）、Rome（明喻系）、Petersburg（缩写碎片）、Rhine/Thames（明喻+假匹配）、Plata（真河<5）、Amsterdam（SC:13 多 Amsterdam Isles 岛群非城，待核）、Long Island/Bay of Bengal。
- **洲级泛指风险**：America(259)/Europe(201)/Asia(86) 泛指高发；America 须与 united-states 错开引注句。
- **discover blindspot（承 R107）**：宜给 pacific-ocean/atlantic-ocean 补 alias 'Pacific'/'Atlantic'，ural-mountains 补 'Ural'（本地页面数据，PHQ 时处理）；discover 专名过滤须比对 alias_index 去重（PARK 待评审）。
- **memex 规范缺陷**：GROW.spec.md priority 3.5 corpus-discover 未同步权威算法（HK-corpus-discover-not-in-statemachine，P3 PARK）。
- **EVV5 节奏**：since_evv5 R108 末=3，下次约 R116。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
- **England/France 国级页 + R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理。
