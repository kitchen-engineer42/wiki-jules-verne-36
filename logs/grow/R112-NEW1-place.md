---
round: 112
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [edinburgh, bokhara, andes, tiflis, alps]
result: success
---

## 执行摘要

R112 决策矩阵（读 R111 末计数器：queue=44、since_evv5=6、since_discover=0、discover_streak_low=0、since_corpus=48）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=6<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=44≥10 且 since_discover=0<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。

承 R111 SCN28 新积压，按 distinctPN 降序消化首批（各 ≥29），全部先经既有页交叉核 + 多实体/称号/异地同名筛。

**建页前筛查（本轮 1 伪新剔除）**：
- **Caspian → 伪新剔除**：交叉核发现 **caspian-sea 页已建**（label Caspian Sea）。裸 "Caspian" 53 distinctPN 系里海，与既有页同物 → 剔除（HK-discover-existing-type-blindspot 复现：R111 probe 的 2641-name 集合含 "caspian sea"/"caspian-sea" 但无裸 "caspian"，漏网）。建议 PHQ 给 caspian-sea 补 alias 'Caspian'。替补 Alps 入本轮。
- **Edinburgh 异地同名剔**：FEM-011-019「Edinburgh in Hidalgo」= 得克萨斯同名城，剔；另「Modern/Northern Athens」称号句避用。取 UC(James Starr 故乡)/AWED(Strand 落网)/FWB(Leith/Forth)/ACH(皇家学会/寄犬) 6 枚真苏格兰城确指。
- **Alps 异地同名剔**：SC:13 中 SC-041-* 系「Australian Alps」（澳洲异地同名山脉），SC-013-014 为「Swiss Alps」比喻。剔澳洲义，取 AMB(Mont Blanc 攀登)/ACH(瑞士红雪)/FEM(月山对比)/OC(Maritime Alps)/RC(Albatross 飞越) 6 枚真欧洲 Alps；book 改 Ascent of Mont Blanc（AMB，最具 Alps 叙事分量，label 已验证存在）。
- **既有页交叉核**：edinburgh/bokhara/andes/tiflis/alps 五 slug/label/alias（含变体 -sea/-mountains/-river/the-）均无既有页碰撞。

本轮建 5 页：place 页数 285→290，registry 1353→1358，unknown 0。queue 开放候选 44→38（消化 5 + Caspian 伪新剔 1）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| edinburgh | 4ILX0n | The Underground City | real | 6 (UC-001-006 + AWED-036-002 + FWB-003-004/033-005 + ACH-005-045/003-054) | 无 | Auld Reekie/Forth/皇家学会；**剔 FEM-011-019 得州同名城**；alias Auld Reekie |
| bokhara | ibDu8m | The Adventures of a Special Correspondent | real | 6 (ASC-005-018/006-008/006-021/010-053/010-073/011-002) | 无 | 大铁路绿洲/Rome of Islam/Khanate |
| andes | bYixX0 | In Search of the Castaways | real | 6 (SC-010-033/011-003 + DSCF-012-074 + EHLA-005-002 + FEM-024-020 + PL-002-004) | 无 | Cordilleras/37°线跨山/Lima 谷；aliases the Andes/Cordilleras |
| tiflis | 98A4T6 | The Adventures of a Special Correspondent | real | 6 (ASC-001-005/001-008/001-019/001-035/001-045/002-003) | 无 | Transcaucasia 起点城/三线枢纽/温泉；alias Tbilisi |
| alps | vR6O4P | Ascent of Mont Blanc | real | 6 (AMB-001-010/001-094 + ACH-051-037 + FEM-024-021 + OC-017-029 + RC-014-044) | 无 | Mont Blanc/Maritime/Pennine；**剔 SC-041 澳洲 Australian Alps**；alias the Alps |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：6/6/6/6/6，全部达标 ✓
- 多实体/称号/异地同名筛：Caspian 伪新剔（caspian-sea 已建）；Edinburgh 剔得州同名+雅典称号；Alps 剔澳洲 Australian Alps ✓
- 既有页交叉核：5 建页 slug/label/alias（含 -sea/-mountains/the- 变体）均无碰撞；Caspian 幸赖交叉核截获 ✓
- 跨源 book 惯例：Edinburgh=UC、Bokhara=ASC、Andes=SC、Tiflis=ASC、Alps=AMB（各取确指最集中/最substantive 之作）✓
- YAML 冒号门（LAW §8）：本轮 5 页 book/description 无冒号裸值 → unknown=0 ✓
- ≤400 字门：建后复验 5 页 0 段 over-400 ✓
- 前向红链：0（链目标 [[Liverpool]]/[[The Underground City]]/[[Peru]]/[[Lima]]/[[Atlantic Ocean]]/[[Black Sea]]/[[Caspian Sea]]/[[Switzerland]]/[[Ascent of Mont Blanc]]/[[The Adventures of a Special Correspondent]] 均既建；Glasgow/Samarkand/Merv/Baku/Mont Blanc 未既建，不链）✓
- add_page warn：本轮 5 页 0 PN 警告 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R112→R113，NEW1）

- current_round 112→113
- type_round 83→84
- rounds_since_last_evv5 6→7
- rounds_since_last_discover 0→1
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 48→49
- last_updated_round 112→113

## 遗留问题

- **R113 预测 = NEW1（续消化 SCN28 积压）**：R112 末 queue=38。矩阵 since_evv5=7、since_discover=1、queue≥10 → priority 3 不触发；default NEW1。建议续按 distinctPN 降序：Merv(26)/Baku(22)/Malta(22)/Sicily(19)/Copenhagen(17) 或 Brest/Baikal/Frankfort/Algiers。
- **建页前复核清单（承 R111）**：Frankfort/Alexandria 核美国同名城；Baltic/Aral/Adriatic 海洋取确指句；ASC 大铁路沿线（Merv/Baku/Teheran/Amou-Daria）book=ASC 高度集中；Havre(Le Havre)/Lyons(Lyon)/Amou-Daria(Oxus) 别名规范。
- **discover blindspot 累积（本轮 Caspian 复现）**：pacific/atlantic/ural **+ caspian** 均系 probe 裸词漏既建页 → 建议 PHQ 批量给 pacific-ocean/atlantic-ocean/ural-mountains/caspian-sea 补裸名 alias，且改进 probe：既建集合应含「去 Sea/Mountains/River/Ocean 后缀的裸词」变体。归 HK-discover-existing-type-blindspot（PARK）。
- **EVV5 节奏**：since_evv5 R112 末=7，下次约 R115。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
- **R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理；注 andes 已链 [[Peru]]/[[Lima]]，peru/lima 分工核可并入。
