---
round: 120
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R120 决策矩阵（读 R119 末计数器：queue=6、since_evv5=3、since_discover=8、discover_streak_low=0、since_corpus=56）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=3<10 → 非 EVV5；since_discover=8<10 且未与 EVV5 同期 → 非 EVV5+SCN28；streak=0<3 → 非 CLOSE+SCN28；**queue=6<discover_queue_threshold(10) → priority 3 命中 → gene = SCN28**（队列低水位，自 R111 以来首次表层勘探）。

SCN28 为 discover 轮，不建页，只补充候选队列。执行 broken-link 扫描（Phase 1）+ 主要地名批测（Phase 2 place 专化：gather distinctPN + 既有页交叉核）。

**Phase 1 — broken-link 扫描**（`discover_by_broken_link.py --top 60`）：返回 22 待建词条，其中 place 相关 3 项——North Pole(×11)、Great Eyrie、Stone's Hill(×1)。经交叉核：
- **North Pole / Great Eyrie = 伪新 blindspot（label-prefix 变体）**：二者**均既建 Pilot 页**（north-pole label「The North Pole」、great-eyrie label「The Great Eyrie」），红链仅因 label 带「The」前缀致 `[[North Pole]]`/`[[Great Eyrie]]` 不解析。**非新候选**。已 `edit_page.py` 补 alias：north-pole +「North Pole」(rev ugJBtN)、great-eyrie +「Great Eyrie」(rev vTj3Zy)，11+ 处红链全解。归 HK-discover-existing-type-blindspot（新增 label-prefix「The X」变体）。
- Stone's Hill：gather distinctPN=0（撇号致词边界不匹配）；实为既建 stony-hill（FEM Columbiad 基地，R31 建）。剔。

**Phase 2 — 主要地名批测**（curated 40 名 × gather + 既有页交叉核）：揭示一批**高 PN 却从未入队的显著地名**（此前 keyword-adjacency 扫描盲区）。既建已核（Norway 101/Gibraltar 63/New Zealand 127/San Francisco 96/Baltimore 61/Stockholm 66/Bombay 54/Nile 51/… 均既建，不重列）。**新候选（distinctPN≥5 且无既有 slug）6 项入队**：
- South Pole（35，TTLU Nemo 立旗 + ACH 对照南极火山）
- Florida（52，FEM 发射地所在州 + 跨源）
- Kamtchatka（23，西伯利亚半岛）
- Timbuctoo（22，FWB 非洲名城）
- Chicago（8，美国城）
- Salt Lake City（5，AWED 摩门篇，borderline 恰达门）

低产/剔除：Naples(4)/Vesuvius(4)/Venice(4)/Table Mountain(2)/Reykjavik(0)/Trieste(1)/Persian Gulf(3)/Elsinore(2) 均 <5 门，暂不入队。

本轮不建页：place 页数维持 319，registry 1387，unknown 0。queue 开放候选 6→12（+6 新候选）。broken-link 总数经 alias 修复下降（North Pole/Great Eyrie 移出红链榜）。

## 页面处理记录

| 动作 | 对象 | rev | 说明 |
|------|------|-----|------|
| edit_page（alias 补） | north-pole | ugJBtN | +alias「North Pole」解 `[[North Pole]]`×11 红链；label 保持「The North Pole」不变 |
| edit_page（alias 补） | great-eyrie | vTj3Zy | +alias「Great Eyrie」解 `[[Great Eyrie]]` 红链；label 保持「The Great Eyrie」不变 |
| queue 补种 | +6 place 候选 | — | South Pole/Florida/Kamtchatka/Timbuctoo/Chicago/Salt Lake City |

## EXIT-GATE 检查

- G4：无新建页；2 处既有页编辑均经 `edit_page.py --author grow`，未直写 ✓
- discover 产出：new_candidates=6 ≥ type_close_new_candidate_min(3) → 非低产，discover_streak_low 维持 0 ✓
- 队列水位：6→12 ≥ discover_queue_threshold(10)，低水位已解除 ✓
- 伪新交叉核：North Pole/Great Eyrie 识别为既有页（label-prefix 变体），未误入队/未重建 ✓
- broken-link 修复复验：North Pole/Great Eyrie 移出红链榜 ✓
- alias 编辑安全：二页 label/description/正文不变，仅 aliases 增项（size +12/+11），edit_page 防缩减通过，unknown=0 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R120→R121，SCN28）

- current_round 120→121
- type_round 91→92
- rounds_since_last_evv5 3→4
- rounds_since_last_discover 8→0（SCN28 RESET）
- discover_streak_low 0（new_candidates=6≥3，维持 0）
- rounds_since_last_corpus_discover 56→57（SCN28 表层，非 corpus）
- last_updated_round 120→121

## 遗留问题

- **R121 预测 = NEW1**：R120 末 queue=12≥10、since_evv5=4<10、streak=0<3、since_discover=0<10、queue(place)≠0、stub%=0 → 默认 NEW1。续消化 R120 补种 6 候选：建前逐一 slug/label/alias 变体交叉核 + 同名地/船消歧 + PN 主题重叠自查。建议首批取 Florida(52，核 Florida Strait 混引 + 与 tampa-town/stony-hill 关系)、South Pole(35，对称 north-pole 写法 + 剔磁极/月面隐喻)、Kamtchatka(23)、Timbuctoo(22)、Chicago(8) 五页。Salt Lake City(5 恰达门) 次批逐句核后建。
- **discover blindspot 重大发现（label-prefix「The X」）**：north-pole/great-eyrie 因 label 带「The」前缀，`[[North Pole]]`/`[[Great Eyrie]]` 长期未解析成红链，且反使 SCN28 broken-link 误报为「待建」。本轮 alias 修复。**建议 PHQ 批量排查所有 label 带「The」前缀的 place/character 页**（如 The Moon/the-moon、The Chimneys/the-chimneys 等），统一补裸名 alias。归 HK-discover-existing-type-blindspot（label-prefix 变体，与既有 Sea/Mountains/River 后缀变体并列）。
- **discover blindspot（后缀变体，承 R117，5 例）**：pacific/atlantic/ural/caspian/baikal——PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。
- **主要地名入队盲区教训**：Florida(52)/South Pole(35)/Kamtchatka(23)/Timbuctoo(22) 等高 PN 显著地名此前从未入队，说明历轮 keyword-adjacency 表层扫描对「无地理后缀的裸名大地名」覆盖不足。probe 应增「国家/州/半岛/极点/名城」维度的显式枚举扫描。
- **Amsterdam 荷兰城挂起**：真城 PN<5（Zuyder-Zee 双源 + 零星）；主 gather 命中皆 amsterdam-island。续挂起待 PHQ。
- **PHQ 待决候选**：Lucknow（澳洲 Lucknow Road）、真俄 Archangel（1 PN）、Amsterdam 荷兰城、Long Island/Bay of Bengal（4<门）、label-prefix「The X」批量 alias、后缀变体批量 alias——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127（since_evv5 R120 末=4）。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
