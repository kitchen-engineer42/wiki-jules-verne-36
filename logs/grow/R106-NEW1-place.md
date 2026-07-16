---
round: 106
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [mediterranean, valparaiso, hamburg, geneva, sahara]
result: success
---

## 执行摘要

R106 决策矩阵（读 R105 末计数器：queue≈32、since_evv5=0、since_discover=2、discover_streak_low=0、since_corpus=42）。按**权威算法 `grow-state-machine.md §3`**（GROW.spec.md 决策表明文让位于此）逐条：since_evv5=0<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue≈32≥10 且 since_discover=2<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

> **corpus-discover（priority 3.5）辨析**：GROW.spec.md §决策表列有 priority 3.5「since_corpus≥30 → SCN28-corpus」，但**权威算法 `grow-state-machine.md §3` 的决策伪码不含该分支**（RFC-memex-0071 只改了汇总表、未同步进状态机算法）。这正解释了 R94 起 since_corpus 连续 ≥30（今 42）却从未触发 corpus-discover——操作性算法根本无此分支。本轮据权威算法执行 NEW1。此表/算法不一致属 memex 层规范缺陷，依 RFC-parking 记 housekeeping，不自主起 RFC（须走 memex RFC 流程，用户末期批量评审）。

承 R104 续批 NEW1 消化 R103 discover 补种候选，本轮取洋/海/城/沙漠层 5 候选：

**建页前多实体筛查**：
- Mediterranean：OC:46/TTLU:40，86 distinctPN 全真（彗星撕走 Algerian 岸/Nautilus 掠海），无噪声。
- Valparaiso：DSCF:12/WC:3，15 distinctPN 全真（Pilgrim 目的港）；**book 冒号 'Dick Sand: A Captain at Fifteen' 首建引号**。
- Hamburg：JCE:20 全真（Liedenbrock 故乡 Königstrasse），无同名干扰。
- Geneva：MZ:19 单源全真（钟匠之城），无 demonym 干扰。
- Sahara：FWB:6/RC:4/OC:3/FC:2/ASC:1，16 distinctPN 全真（900 里荒漠）；alias Sahara Desert。
- **本轮剔候选 2**：Petersburg（裸词仅 3 distinctPN<门——"St. Petersburg" 因 "St." 缩写点被句切分器碎片化，转 HOLD）、Rome（25 distinctPN 但 16 源极散且大量比喻 "Rome of Islam"=Bokhara/"Rome of Turkestan"/"all roads lead to Rome"，真城确指剔比喻后 <5，转 HOLD——明喻系）。

本轮建 5 页：Mediterranean（OC 彗星撕海）、Valparaiso（DSCF 目的港）、Hamburg（JCE Liedenbrock 故乡）、Geneva（MZ 钟匠之城）、Sahara（FWB 荒漠之惧）。place 页数 260→265，registry 1328→1333，unknown 0。queue ~32→~25（消化 5 + 2 转 hold）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| mediterranean | nKMOAw | Off on a Comet | real | 5 (OC-006-001/005-005/007-007/002-016/007-034) | 无 | 彗星撕走 Algerian 岸/新海岸线 |
| valparaiso | CwjRnh | Dick Sand: A Captain at Fifteen | real | 6 (DSCF-001-017/005-002/009-045/010-003/004-043/007-060) | 无 | Pilgrim 目的港；book 冒号引号 |
| hamburg | u8CPLL | A Journey to the Center of the Earth | real | 5 (JCE-001-002/001-024/007-002/001-028/008-002) | 无 | Liedenbrock 故乡 Königstrasse/下潜起点 |
| geneva | swnkeD | Master Zacharius | real | 6 (MZ-001-002/001-005/001-007/003-004/001-017/002-002) | 无 | 钟匠之城/湖西端/前 Calvinism 之城 |
| sahara | eY5vaf | Five Weeks in a Balloon | real | 5 (FWB-024-009/034-023/038-022/008-017 + FC-023-042) | 无 | 900 里荒漠/气球西驱之惧；alias Sahara Desert |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 8 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：5/6/5/6/5，全部达标 ✓
- 多实体筛查：Petersburg（3<门 hold）、Rome（比喻系剔后 <门 hold）本轮不建；5 建页均词边界核确指地名 ✓
- 跨源 book 惯例：各取单作最集中之作定 book（Mediterranean OC、Valparaiso DSCF、Hamburg JCE、Geneva MZ、Sahara FWB）✓
- YAML 冒号门（LAW §8）：valparaiso `book: 'Dick Sand: A Captain at Fifteen'` 首建即加引号 → unknown=0 ✓
- ≤400 字门：建前复验 5 页 0 段 over-400 ✓
- 前向红链：0（book label ×5 + Gibraltar/Africa/Chili/California/Germany/Iceland/Switzerland/Nile 均核既建）✓
- 交叉核既有页：5 slug/label 均无既有页碰撞 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R106→R107，NEW1）

- current_round 106→107
- type_round 77→78
- rounds_since_last_evv5 0→1
- rounds_since_last_discover 2→3
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 42→43
- last_updated_round 106→107

## 遗留问题

- **R107 预测 = NEW1（续消化 discover 残余）**：R106 末 queue≈25（洋/洲/城/河残余）。矩阵 since_evv5=1、since_discover=3、queue≥10 → priority 3 不触发；default NEW1。建议 R107 取 Pacific/Atlantic（洋级，聚焦航段确指句避泛指）或 United States（国级，与 America 分工）或 Mississippi/Rhine/Thames（河流层，跨源）或 Amsterdam/Marseilles/Bordeaux/Berlin（城市层，跨源凑句）。
- **洋/洲级泛指风险（承 R104/R105）**：Pacific/Atlantic/America/Europe/Asia 单义模糊，建页须严筛「Verne 航段设定」确指句 vs 泛指；America↔United States 错开引注句。
- **HOLD 累积**：Petersburg（缩写碎片 3<门）、Rome（明喻系剔后 <门）、Long Island、Bay of Bengal——待专项凑句或 sentence_index 缩写处理改进后再评。
- **薄候选严扫风险**：Ganges=5、Calais=6、Vienna/Madrid/Lisbon/Constantinople/Athens=7 逼近门；5 国级残余（Mongolia/Austria/Kamtschatka/Prussia/Belgium）同理。
- **memex 规范缺陷（记 housekeeping）**：GROW.spec.md §决策表 priority 3.5 corpus-discover 未同步进权威算法 `grow-state-machine.md §3`；表/算法不一致。依 RFC-parking 记录，不自主起 RFC。
- **EVV5 节奏**：since_evv5 R106 末=1，下次约 R116。
- **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型 EVV6 全库评审并回填均分。
- **England/France 国级页评估 + R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理。
