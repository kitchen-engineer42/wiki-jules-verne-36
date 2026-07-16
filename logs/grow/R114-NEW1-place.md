---
round: 114
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [brest, frankfort, algiers, etna, riga]
result: success
---

## 执行摘要

R114 决策矩阵（读 R113 末计数器：queue=33、since_evv5=8、since_discover=2、discover_streak_low=0、since_corpus=50）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=8<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=33≥10 且 since_discover=2<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 积压，按 distinctPN 降序消化第三批。全部先经既有页交叉核（含 -sea/-lake/-river/the-/Mount- 变体）+ 多实体/称号/异地同名筛。

**建页前筛查（本轮 1 伪新剔除）**：
- **Baikal → 伪新剔除**：交叉核发现 **lake-baikal 页已建**（label Lake Baikal，type place，book MS，alias The Baikal）。裸 "Baikal" 17 distinctPN 系同一大湖 → 剔除。**HK-discover-existing-type-blindspot 第 5 例**（续 pacific/atlantic/ural/caspian）：probe 的 existing 集合含 "lake baikal"/"the baikal" 但无裸 "baikal"，漏网。建议 PHQ 给 lake-baikal 补 alias 'Baikal'。替补 Riga（10 distinctPN）入本轮。
- **Frankfort 异地同名剔**：MW-004-013「in Kentucky near Frankfort」= 美国肯塔基州府同名城，剔；取 DA/VB 气球升空之城 Frankfort-on-the-Main（德国 Frankfurt）+ ASC-004-047 德式 bier-halle 共 8 枚真德国城确指。alias Frankfort-on-the-Main/Frankfurt。
- **Etna 多实体剔**：TTLU-001-012 系 Inman 轮船 "Etna"（撞怪物报告），非火山，剔；取 JCE/OC/RC/RM/MI 6 枚真西西里火山确指。链 [[Sicily]]（R113 建）。alias Mount Etna。
- **既有页交叉核**：brest/frankfort/algiers/etna/riga 五 slug/label/alias 均无既有页碰撞（Baikal 幸赖交叉核截获）。

**book 归属**：Brest=WC（法国大西洋军港，WC:14）、Frankfort=A Drama in the Air（DA/VB 气球史）、Algiers=OC（Off on a Comet，北非城彗星吞没，OC:12）、Etna=OC（西西里火山，11000ft 峰随岛消失）、Riga=MS（Nadia Fedor 故乡，MS:8）。

本轮建 5 页：place 页数 295→300，registry 1363→1368，unknown 0。queue 开放候选 33→27（消化 5 + Baikal 伪新剔 1）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| brest | GVYoy9 | The Waif of the Cynthia | real | 8 (WC-012-062/013-002/013-003/013-032/014-035/022-002 + TTLU-019-041/044-054) | 无 | 法国大西洋军港/Alaska 靠岸/d'Entrecasteaux 出航 |
| frankfort | 7puzsL | A Drama in the Air | real | 8 (DA-001-001/001-002/001-003/001-061/001-082/001-091 + VB-001-058 + ASC-004-047) | 无 | 气球升空之城/September fair；**剔 MW-004-013 美国肯塔基同名**；alias Frankfort-on-the-Main/Frankfurt |
| algiers | 6WuAgj | Off on a Comet | real | 8 (OC-007-007/008-017/011-017/012-003/022-022/022-023 + RC-015-013 + TTLU-031-041) | 1 段 403→trim Trans-Saharan 句 | 北非城/彗星吞没/amphitheater |
| etna | HlMrrP | Off on a Comet | real | 6 (JCE-044-053 + OC-018-026 + RC-001-027 + RM-010-016/017-027 + MI-057-003) | 无 | 西西里火山/11000ft 峰；**剔 TTLU-001-012 轮船 "Etna"**；链 [[Sicily]]，alias Mount Etna |
| riga | ismidD | Michael Strogoff | real | 8 (MS-005-078/007-010/009-039/009-046/009-050/031-063/034-023 + WC-021-015) | 无 | Nadia Fedor 故乡/波罗的海港城；链 [[Irkutsk]]/[[Siberia]] |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：8/8/8/6/8，全部达标 ✓
- 多实体/称号/异地同名筛：Baikal 伪新剔（lake-baikal 已建）；Frankfort 剔美国肯塔基同名；Etna 剔轮船 "Etna" ✓
- 既有页交叉核：5 建页 slug/label/alias（含 -lake/-river/Mount-/the- 变体）均无碰撞；Baikal 幸赖交叉核截获 ✓
- 跨源 book 惯例：Brest=WC、Frankfort=A Drama in the Air、Algiers=OC、Etna=OC、Riga=MS ✓
- YAML 冒号门（LAW §8）：本轮 5 页 book/description 无冒号裸值 → unknown=0 ✓
- ≤400 字门：algiers 1 段 403 已 trim，建后复验 5 页 0 段 over-400 ✓
- 前向红链：0（链目标 [[The Waif of the Cynthia]]/[[Twenty Thousand Leagues Under the Sea]]/[[A Drama in the Air]]/[[Mediterranean]]/[[Off on a Comet]]/[[Sicily]]/[[Irkutsk]]/[[Siberia]]/[[Michael Strogoff]] 均既建；Timbuktu/Vesuvius/Oran/Provence 未既建，不链）✓
- add_page warn：本轮 5 页 0 PN 警告 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R114→R115，NEW1）

- current_round 114→115
- type_round 85→86
- rounds_since_last_evv5 8→9
- rounds_since_last_discover 2→3
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 50→51
- last_updated_round 114→115

## 遗留问题

- **R115 预测 = NEW1（续消化 SCN28 积压）**：R114 末 queue=27。矩阵 since_evv5=9<10、since_discover=3、queue≥10 → priority 1/3 均不触发；default NEW1。建议续按 distinctPN 降序：Lyons(10)/Havre(9)/Lucknow(7)/Corsica(7)/Archangel(7)。
- **EVV5 节奏修正**：since_evv5 R114 末=9。R115 末→10，故 **EVV5 于 R116 触发**（priority 1 抢占 NEW1），非此前估的 R115。
- **建页前复核清单（承 R111/R112/R113）**：Lyons(Lyon)/Havre(Le Havre) 别名规范；Lena/Baltic 等带 River/Sea 后缀候选建前须核 lena-river/baltic-sea 是否已建（防又一 blindspot）；Baltic/Aral/Adriatic 海洋取确指句；Corsica/Sardinia 地中海岛无异地同名。
- **discover blindspot 累积（本轮 Baikal 第 5 例）**：pacific/atlantic/ural/caspian **+ baikal** 均系 probe 裸词漏既建页 → 建议 PHQ 批量给 pacific-ocean/atlantic-ocean/ural-mountains/caspian-sea/lake-baikal 补裸名 alias，且改进 probe：既建集合应含「去 Sea/Mountains/River/Ocean/Lake 前后缀的裸词」变体。归 HK-discover-existing-type-blindspot（PARK）。
- **交叉链回补**：Samarkand 建后回补 Merv/Bokhara；Etna 已链 Sicily，Vesuvius 建后可与 Etna 交叉链。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
