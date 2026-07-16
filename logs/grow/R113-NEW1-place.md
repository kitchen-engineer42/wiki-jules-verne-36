---
round: 113
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [baku, merv, malta, sicily, copenhagen]
result: success
---

## 执行摘要

R113 决策矩阵（读 R112 末计数器：queue=38、since_evv5=7、since_discover=1、discover_streak_low=0、since_corpus=49）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=7<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=38≥10 且 since_discover=1<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 积压，按 distinctPN 降序消化第二批（各 ≥17），全部先经既有页交叉核（含 -sea/-island/-city/the- 变体）+ 多实体/称号/异地同名筛。

**建页前筛查（本轮 0 伪新剔除）**：
- **交叉核**：Merv/Baku/Malta/Sicily/Copenhagen 五 slug/label/alias（含 Strait of/the-/island 变体）均无既有页碰撞（clear）。
- **同名筛**：五者均无异地同名歧义——Merv/Baku 系 ASC 大铁路唯一指（中亚绿洲城/里海油城）；Malta/Sicily 系地中海确指岛；Copenhagen 系丹麦都确指。
- **建序防前向红链**：Baku 先于 Merv（Merv 链 [[Baku]]）；Malta 先于 Sicily。Merv 未反链 Merv→Baku 之外无同轮前向链。

**book 归属**：Baku=ASC（里海端点，ASC:22 独占）、Merv=ASC（中亚绿洲，ASC:26 独占）、Malta=OC（Off on a Comet，彗星吞没叙事最substantive，OC:9）、Sicily=OC（Etna/西西里海峡陆桥，OC:8）、Copenhagen=JCE（地心游记起点城，JCE:8）。

本轮建 5 页：place 页数 290→295，registry 1358→1363，unknown 0。queue 开放候选 38→33（消化 5）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| baku | 1Tq2SA | The Adventures of a Special Correspondent | real | 8 (ASC-001-019/001-062/002-003/003-011/003-012/003-013/003-042/006-006) | 无 | 里海端点/Guebres 拜火城/naphtha；region Transcaucasia |
| merv | Lvoh8P | The Adventures of a Special Correspondent | real | 10 (ASC-005-018/006-008/006-036/009-008/010-001/010-005/010-012/010-020/010-040/010-045) | 无 | 中亚绿洲/四建之城/Tekke 村；链 [[Bokhara]]/[[Baku]] |
| malta | yBJvU5 | Off on a Comet | real | 8 (FEM-007-055/012-005 + OC-013-019/015-040/015-044/016-002/016-012 + TT-016-005 + WC-012-049) | 无 | 骑士岛/彗星吞没/属英；链 [[Mediterranean]]/[[Gibraltar]] |
| sicily | Hx2fjS | Off on a Comet | real | 7 (OC-012-005/012-006/013-017/013-022/018-026 + TTLU-031-016/031-019) | 无 | Etna 岛/西西里海峡陆桥；链 [[Italy]]/[[Twenty Thousand Leagues Under the Sea]] |
| copenhagen | QS12uP | A Journey to the Center of the Earth | real | 8 (JCE-007-053/007-055/008-023/008-035/010-006/017-004 + MS-027-003) | 无 | 丹麦都/Frelsers Kirk/学术城；链 [[Iceland]]/[[Sweden]]/[[Denmark]] |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：8/10/8/7/8，全部达标 ✓
- 多实体/称号/异地同名筛：五者均无异地同名歧义，0 伪新剔 ✓
- 既有页交叉核：5 建页 slug/label/alias（含 -sea/-island/Strait of/the- 变体）均无碰撞 ✓
- 跨源 book 惯例：Baku=ASC、Merv=ASC、Malta=OC、Sicily=OC、Copenhagen=JCE（各取确指最集中/最substantive 之作）✓
- YAML 冒号门（LAW §8）：本轮 5 页 book/description 无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 5 页 0 段 over-400 ✓
- 前向红链：0（链目标 [[Tiflis]]/[[Black Sea]]/[[Caspian Sea]]/[[The Adventures of a Special Correspondent]]/[[Bokhara]]/[[Baku]]/[[Mediterranean]]/[[Gibraltar]]/[[Off on a Comet]]/[[Italy]]/[[Twenty Thousand Leagues Under the Sea]]/[[Iceland]]/[[Sweden]]/[[Denmark]]/[[A Journey to the Center of the Earth]] 均既建；Samarkand/Etna 未既建，不链）✓
- add_page warn：本轮 5 页 0 PN 警告 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R113→R114，NEW1）

- current_round 113→114
- type_round 84→85
- rounds_since_last_evv5 7→8
- rounds_since_last_discover 1→2
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 49→50
- last_updated_round 113→114

## 遗留问题

- **R114 预测 = NEW1（续消化 SCN28 积压）**：R113 末 queue=33。矩阵 since_evv5=8、since_discover=2、queue≥10 → priority 3 不触发；default NEW1。建议续按 distinctPN 降序：Brest(17)/Baikal(17)/Frankfort(16)/Algiers(15)/Etna(11) 或 Riga/Lyons/Havre。
- **建页前复核清单（承 R111/R112）**：Frankfort 核美国肯塔基同名州府（取真德国 Frankfurt 义）；Baltic/Aral/Adriatic 海洋取确指句避比喻；Havre(Le Havre)/Lyons(Lyon)/Amou-Daria(Oxus) 别名规范；ASC 大铁路沿线 Teheran/Astrakhan/Amou-Daria book=ASC 集中。
- **EVV5 节奏**：since_evv5 R113 末=8，下次约 R115（≥10 触发）。届时 priority 1 抢占 NEW1。
- **discover blindspot 累积**：pacific/atlantic/ural/caspian probe 裸词漏既建页 → 建议 PHQ 批量补裸名 alias + 改进 probe 去 Sea/Mountains/River/Ocean 后缀。归 HK-discover-existing-type-blindspot（PARK）。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **交叉链回补**：Samarkand 建后可回补 Merv/Bokhara 交叉链；Etna 建后与 sicily 交叉链。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
