---
round: 122
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R122 决策矩阵（读 R121 末计数器：queue=7、since_evv5=5、since_discover=1、discover_streak_low=0、since_corpus=58）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=5<10 → 非 EVV5；streak=0<3 → 非 CLOSE+SCN28；**queue=7<discover_queue_threshold(10) → priority 命中 → gene = SCN28**（队列低水位，R121 建 5 页后回落）。

> **corpus-discover 说明**：since_corpus=58≥corpus_discover_interval(30)，表面上「定期 corpus 勘探」逾期近两个周期。但权威 `grow-state-machine.md §3`（L127–140）**不含 corpus-discover 分支**——该计数器与 thresholds 为项目扩展，尚未并入状态机（归 HK-corpus-discover-not-in-statemachine，已 park）。故本轮按权威算法执行**表层 SCN28**，since_corpus 继续累加，逾期状态记入遗留问题待 PHQ，不自创深挖流程。

SCN28 为 discover 轮，不建页，只补充候选队列。执行 broken-link 复扫（Phase 1）+ curated 主要地名批测 72 名（Phase 2，2 批）。

**Phase 1 — broken-link 复扫**（`discover_by_broken_link.py --top 50`）：返回 20 项，**place 相关仅 1 项——Stone's Hill(×1)**。经交叉核：gather「Stone's Hill」distinctPN=0、「Stony Hill」distinctPN=24（FEM Columbiad 基地，既建 stony-hill「Stony Hill」）。「Stone's Hill」为某 wiki 页 wikilink 的拼写误植（corpus 无此拼写），**非新候选、非可支撑 alias**；正解为修源页 wikilink 而非补无 corpus 支撑的 alias——留 PHQ 修源。余 19 项（Lunar Projectile×11、Twenty Thousand Leagues Under the Seas×7 复数变体、Ker Karraje、J.T. Maston、Paganel 等）均为 character/work 变体，非 place，本轮不处理（work 复数变体归 PHQ）。

**Phase 2 — curated 主要地名批测**（72 名 × gather + 既有页交叉核）：既建已核（Suez 54/Liverpool 76/Zanzibar 62/Melbourne 70/Greenland 68/Calcutta 43/Yokohama 44/Auckland 47/Lima 41/Cape Horn 39/Moscow 45/… 均既建，不重列）。**新候选（distinctPN≥5 且无既有 slug）20 项入队**：Washington(78)、Charleston(49)、Philadelphia(39)、Newfoundland(34)、Richmond(30)、Boston(24)、Spitzbergen(15)、Montreal(13)、Panama(11)、Adelaide(10)、New Orleans(9)、Quebec(9)、Rio de Janeiro(8)、Labrador(8)、Perth(7)、Tasmania(7)、Sydney(6)、Detroit(6)、Vancouver(6)、Madras(5)。

其中标 ⚠ 者建前须重消歧：Washington（城/人/州/堡）、Charleston（SC 城 vs FEM Charlestown MA）、Richmond（VA vs 伦敦）、Panama（城 vs 地峡 vs 运河）、Adelaide（城 vs 南极岸 vs 人名）、Perth（西澳 vs 苏格兰）、Sydney（城 vs Cape Sidney/人名）、Vancouver（岛 vs 城 vs 人）。

低产/剔除：Cairo(3)/Havana(4)/Naples(4)/Cadiz(4)/Nagasaki(4)/Java(4)/Cape Town(3)/Tahiti(2)/Sumatra(2)/Canton(2)/Cincinnati(2)/Warsaw(1)/Denver(1)/Pittsburgh(1)/Buenos Aires(1)/Montevideo(1)/Borneo(1)/Odessa(0)/Honolulu(0)/Brisbane(0)/Manilla(0) 均 <5 门，暂不入队。

本轮不建页：place 页数维持 324，registry 1392，unknown 0。queue 开放候选 7→27（+20 新候选），低水位大幅解除。

## 页面处理记录

| 动作 | 对象 | rev | 说明 |
|------|------|-----|------|
| queue 补种 | +20 place 候选 | — | Washington/Charleston/Philadelphia/Newfoundland/Richmond/Boston/Spitzbergen/Montreal/Panama/Adelaide/New Orleans/Quebec/Rio de Janeiro/Labrador/Perth/Tasmania/Sydney/Detroit/Vancouver/Madras |

（本轮无建页、无编辑；broken-link Stone's Hill 判为拼写误植留 PHQ，未 edit_page。）

## EXIT-GATE 检查

- G4：无新建页、无页面编辑 ✓
- discover 产出：new_candidates=20 ≥ type_close_new_candidate_min(3) → 非低产，discover_streak_low 维持 0 ✓
- 队列水位：7→27 ≥ discover_queue_threshold(10)，低水位已解除 ✓
- 伪新交叉核：72 curated 名逐一核 pages.json label/alias；既建（Suez/Liverpool/Melbourne 等）未误入队 ✓
- broken-link 复核：place 项 Stone's Hill 识别为既有 stony-hill 拼写误植（corpus 0 PN），未误入队/未补无支撑 alias ✓
- 消歧标注：8 个 ⚠ 高风险候选（Washington/Charleston/Richmond/Panama/Adelaide/Perth/Sydney/Vancouver）已在 queue 注明建前消歧要求 ✓
- unknown=0；place 维持 324 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean（待 commit 时复核）

## 六步状态机（R122→R123，SCN28）

- current_round 122→123
- type_round 93→94
- rounds_since_last_evv5 5→6
- rounds_since_last_discover 1→0（SCN28 RESET）
- discover_streak_low 0（new_candidates=20≥3，维持 0）
- rounds_since_last_corpus_discover 58→59（SCN28 表层，非 corpus）
- last_updated_round 122→123

## 遗留问题

- **R123 预测 = NEW1**：R122 末 queue=27≥10、since_evv5=6<10、streak=0<3、since_discover=0<10、queue(place)≠0、stub%=0 → 默认 NEW1。续消化 R122 补种 20 候选，逐一 same-name/entity 消歧后建。建议首批取无消歧风险且高 PN 者：Philadelphia(39)、Newfoundland(34)、Boston(24)、Spitzbergen(15)、Montreal(13) 五页。⚠消歧候选（Washington/Charleston/Richmond/Panama 等）建前逐句核确指主体后分批建。
- **corpus-discover 逾期（HK-corpus-discover-not-in-statemachine）**：since_corpus=59，逾 interval(30) 近两周期，但状态机无分支触发。park 待 PHQ 决定是否将 corpus-discover 分支正式并入 `grow-state-machine.md §3`（属 memex 共享文件，须走 RFC）。
- **work 复数变体红链（新）**：`[[Twenty Thousand Leagues Under the Seas]]`（复数 Seas，×7）指向既有 work 页 twenty-thousand-leagues「Twenty Thousand Leagues Under the Sea」（单数）——label-variant 红链。本轮 place 类型域内未处理；PHQ 批量为 work 页补复数 alias。
- **Stone's Hill wikilink 误植**：某 wiki 页写 `[[Stone's Hill]]`（corpus 无此拼写），正解为修源页 wikilink 为 `[[Stony Hill]]`；留 PHQ 修源。另注：stony-hill 页 `real_or_fictional` 字段为 None（缺值），PHQ 一并回填 fictional。
- **discover blindspot（label-prefix「The X」，承 R120）**：north-pole/great-eyrie 已补裸名 alias；PHQ 待批量排查所有 label 带「The」前缀页（The Moon/the-moon、The Chimneys 等）补裸名 alias。
- **discover blindspot（后缀变体，承 R117，5 例）**：pacific/atlantic/ural/caspian/baikal——PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。
- **PHQ 待决候选**：Salt Lake City(5 恰达门)、Madras(5 恰达门)、Long Island/Bay of Bengal(4<门)、Amsterdam 荷兰城(<5)、Lucknow(澳洲路名)、真俄 Archangel(1 PN)、label-prefix「The X」批量 alias、后缀变体批量 alias、work 复数变体 alias、Stone's Hill 修源——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127（since_evv5 R122 末=6）。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
