---
round: 109
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [guiana, calais, berlin, vienna, austria]
result: success
---

## 执行摘要

R109 决策矩阵（读 R108 末计数器：queue≈19、since_evv5=3、since_discover=5、discover_streak_low=0、since_corpus=45）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=3<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue≈19≥10 且 since_discover=5<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。（priority 3.5 corpus-discover 死分支，见 HK-corpus-discover-not-in-statemachine，不赘。）

承 R108 续批 NEW1 消化 discover 残余，本轮取欧洲城市/国别/海岸层 5 候选（Guiana/Calais/Berlin/Vienna/Austria），全部先经既有页交叉核 + 多实体/称号筛。洲级（Europe/Asia/America）与 Amsterdam/Ganges/Mongolia/Long Island/Bay of Bengal 本轮继续 HOLD，留严筛专轮。

**建页前筛查**：
- **Berlin/Vienna 天文台争议取实**：RC-001-025「柏林 vs 维也纳 observatory 争一望，俄国调停证两方皆对」为两页 substantive 主句，避列举义偏薄。Berlin 另取 TT Berlin Conference(殖民划界)/时区无震、FEM Mendelssohn 银行认捐、ASC 巴黎-柏林-彼得堡陆路。Vienna 另取 FWB 皇家地理学会、ASC Zeitung 装箱旅行、DA 飞人离散、SC Petersburg-Vienna-NY 学会授荣。
- **Austria 帝国/国别层**：MW 六强之一/FEM 财困仍认捐/SC Paganel 列强/TT Francis Joseph 极地/TTLU 海牙条约+Sadova 停战，6 枚跨源真国确指。
- **Guiana 岸线层**：TTLU Nautilus 近 Dutch Guiana(Maroni 河口)/SC2 Chancellor 幸存者距圭亚那 800 里筏航/EHLA 法-巴西边界争议(1857 亚马逊自由)，6 枚；aliases French/Dutch Guiana。
- **Calais 海峡港层**：AWED Fogg 首途 Dover-Calais/ASC 隧道设想/SC 童谬地理/DA Blanchard-Jeffries 气球跨海/RC Pilâtre 殉难，8 枚。**Dover 无既有页 → 不链 Dover wikilink**（LAW §10 前向红链规避）。
- **既有页交叉核**：guiana/calais/berlin/vienna/austria 五 slug/label 均无既有页碰撞（承 R107 Pacific/Atlantic/Ural 伪新教训，建前逐一 pages.json 核）。

本轮建 5 页：place 页数 275→280，registry 1343→1348，unknown 0。queue 开放候选 19→14（消化 5）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| guiana | R9iWkG | The Survivors of the Chancellor | real | 6 (TTLU-041-062/041-044 + SC2-016-018/020-004/026-004 + EHLA-005-040) | 无 | Nautilus 近 Dutch Guiana/Chancellor 筏航目标岸/法-巴西边界争；aliases French/Dutch Guiana |
| calais | NmPOMu | Around the World in Eighty Days | real | 8 (AWED-004-010/004-020 + ASC-011-046 + SC-038-092 + DA-001-118/001-139 + RC-004-047 + VB-001-114) | 无 | Fogg 首途/Dover-Calais 隧道/气球跨海史；**Dover 未既建不链**；VB-001-114 warn(重叠 1.6%<2%)，余 7 PN 达门 |
| berlin | Wwh0cQ | Topsy-Turvy | real | 6 (RC-001-025 + TTLU-001-015 + TT-001-026/019-017 + FEM-012-009 + ASC-022-007) | 无 | observatory 争议/Berlin Conference/Mendelssohn 认捐/陆路枢纽 |
| vienna | MQUOTc | The Adventures of a Special Correspondent | real | 6 (RC-001-025 + FWB-001-035 + ASC-007-035 + DA-001-008 + FEM-012-009 + SC-006-075) | 无 | observatory 争议/皇家地理学会/Zeitung 装箱/学会授荣 |
| austria | w3C27K | Twenty Thousand Leagues Under the Sea | real | 6 (MW-008-054 + FEM-012-015 + SC-038-087 + TT-001-061 + TTLU-032-052/044-033) | 无 | 六强之一/认捐/Francis Joseph 极地/海牙条约+Sadova 停战；region Central Europe |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：6/8/6/6/6，全部达标 ✓
- 多实体/称号筛查：Berlin/Vienna observatory 争议取实避列举薄；Austria 取国别确指；Guiana aliases 标 French/Dutch；Calais Dover 未既建不链 ✓
- 既有页交叉核：5 建页 slug/label 均无既有页碰撞（承 R107 教训逐一核 pages.json）✓
- 跨源 book 惯例：各取单作最集中/最具叙事分量之作定 book（Guiana=SC2、Calais=AWED、Berlin=TT、Vienna=ASC、Austria=TTLU）✓
- YAML 冒号门（LAW §8）：本轮 5 页 book 值无冒号，无需引号 → unknown=0 ✓
- ≤400 字门：建前复验 5 页 0 段 over-400 ✓
- 前向红链：0（未既建 place（Dover 等）不链；book label ×5 均既建）✓
- add_page warn：calais VB-001-114 重叠 1.6%<2%（mode=warn 非阻断，余 7 PN≥5 达门，保留）
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R109→R110，NEW1）

- current_round 109→110
- type_round 80→81
- rounds_since_last_evv5 3→4
- rounds_since_last_discover 5→6
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 45→46
- last_updated_round 109→110

## 遗留问题

- **R110 预测 = NEW1**：R109 末 queue≈14。矩阵 since_evv5=4、since_discover=6、queue=14≥10 → priority 3 不触发（queue<10 阈值未达，since_discover<10）；default NEW1。queue 逼近 discover_queue_threshold=10，约 R111 触发 SCN28 补充勘探。R110 建议取 Kamtschatka(5)/Prussia(6)/Belgium(6)/Ganges(5) 或启动洲级严筛（Europe/Asia/America）。
- **洲级泛指风险（累积未决）**：America(259)/Europe(201)/Asia(86) 泛指高发；America 须与 united-states 错开引注句，取「新大陆/美洲发现史」义而非美国指代。留严筛专轮。
- **HOLD 累积**：Amsterdam（SC:13 多 Amsterdam Isles 岛群非城）、Athens（称号系）、Rome（明喻系）、Petersburg（缩写碎片）、Rhine/Thames/Plata（明喻/真河<5）、Long Island/Bay of Bengal、Mongolia（Caucasus 类 ship-screen 待核）。
- **discover blindspot（承 R107）**：宜给 pacific-ocean/atlantic-ocean 补 alias 'Pacific'/'Atlantic'，ural-mountains 补 'Ural'（本地页面数据，PHQ 时处理）。
- **memex 规范缺陷**：GROW.spec.md priority 3.5 corpus-discover 未同步权威算法（HK-corpus-discover-not-in-statemachine，P3 PARK）。
- **EVV5 节奏**：since_evv5 R109 末=4，下次约 R115-116。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
- **England/France 国级页 + R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理。
