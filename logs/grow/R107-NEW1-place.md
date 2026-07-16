---
round: 107
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [united-states, mississippi, caucasus, bordeaux, marseilles]
result: success
---

## 执行摘要

R107 决策矩阵（读 R106 末计数器：queue≈25、since_evv5=1、since_discover=3、discover_streak_low=0、since_corpus=43）。按**权威算法 `grow-state-machine.md §3`**（GROW.spec.md 决策表明文让位于此）逐条：since_evv5=1<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue≈25≥10 且 since_discover=3<10 → 非 SCN28；queue(place)≠0 → 非僵尸；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → NEW1**。（priority 3.5 corpus-discover 仍为死分支，见 R106 辨析 / HK-corpus-discover-not-in-statemachine，不赘。）

承 R106 续批 NEW1 消化 R103 discover 补种候选，本轮取国/河/山区/港城层 5 候选。

**建页前多实体 + 既有页交叉核（本轮 3 候选被剔为伪新/重复，关键）**：
- **Pacific / Atlantic → 剔（伪新候选）**：交叉核 pages.json 发现二者**早已建**为 `pacific-ocean`（label Pacific Ocean，R66）/`atlantic-ocean`（label Atlantic Ocean，R67）。R103 discover 专名扫描未比对既有页 label，误列为新候选——即 HK-discover-existing-type-blindspot 的又一实例。若未交叉核径建 `pacific`/`atlantic`，将触 LAW §10 label 冲突（同 R78 tsalal 重复页）。已在 queue 标注并建议给二既有页补 alias 'Pacific'/'Atlantic'。
- **Ural → 剔（山脉义重复）**：`ural-mountains` 已建（R42）。裸 "Ural" 35 distinctPN 几全指 "Ural Mountains"（=既有页）；Ural River 独立义仅 MS-003-005 等 <5，不足门，ural-river 暂不单建。
- **Caucasus → 建，但重度船名污染**：MS 中 "the Caucasus" **主体是汽船名**（MS-006/008/009 全程指 steam-packet），非山脉。仅 ASC-001-010/001-014/003-066/010-014 + MS-004-039/006-037 = 6 枚为高加索**山区/地域**确指句，全部剔船名引后建页。
- **Rome/Petersburg（承 R106 HOLD）、Rhine/Thames/Plata → 本轮不取**：Rhine/Thames 明喻+假匹配剔后 <5；Plata 真河义（Rio de la Plata 河口）仅 ~3，余为 "provinces of La Plata" 地域（与 argentine 重叠）。
- **Marseilles**：剔 TTLU-031-036 伪匹配、OC "wines" 产品指后 6 枚港城确指句。**Bordeaux**：剔 OC "wines of Bordeaux" 后 8 枚 Gironde 河港确指句。

本轮建 5 页：United States（FEM Gun Club 母国/铁路横贯）、Mississippi（AWED king of rivers/Fogg 夜渡）、Caucasus（MS 山区屏障）、Bordeaux（AWED Fogg 目标港）、Marseilles（JCE 归航登陆港）。place 页数 265→270，registry 1333→1338，unknown 0。queue 开放候选 ~33→25（消化 5 + Pacific/Atlantic/Ural 3 伪新剔除）。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| united-states | ItE41W | From the Earth to the Moon | real | 8 (FEM-001-002/003-009/003-013/010-005/024-018 + AWED-005-005/021-011/026-002) | 无 | Gun Club 母国/十倍法国/铁路横贯；精确短语无 America 洲级重叠 |
| mississippi | 2KWOLK | Around the World in Eighty Days | real | 6 (AMB-001-008/AWED-031-036/EHLA-008-006/FEM-024-018/RC-009-014/TTLU-029-090) | 无 | king of rivers/Davenport 夜渡；剔河名列举+paddle-wheeler 形容 |
| caucasus | ochltK | Michael Strogoff | real | 6 (ASC-001-010/001-014/003-066/010-014 + MS-004-039/006-037) | 无 | 山区屏障/Transcaucasia 门户；**剔全部 MS 船名 "Caucasus" 引** |
| bordeaux | wzqaua | Around the World in Eighty Days | real | 8 (ASC-001-051/002-026/AWED-032-029/032-040/033-004/033-017/DA-001-090/VB-001-085) | 无 | Gironde 河港/Fogg Henrietta 目标港/气球升空地；剔 OC wines 产品指 |
| marseilles | kBFWPC | A Journey to the Center of the Earth | real | 6 (ACH-041-041/DSCF-032-075/JCE-045-004/TT-019-057/TTLU-024-049/031-010) | 无 | 地中海归航登陆港/Provençal 渔场；剔 TTLU-031-036 伪匹配 |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 9 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：8/6/6/8/6，全部达标 ✓
- 多实体筛查：Caucasus 剔船名引（仅山区义 6 枚）、Mississippi 剔河名列举/形容、Bordeaux 剔 wines 产品、Marseilles 剔伪匹配、United States 用精确短语避 America 洲级 ✓
- **既有页交叉核**：Pacific（=pacific-ocean R66）/Atlantic（=atlantic-ocean R67）/Ural（=ural-mountains R42）三伪新候选**建前查出并剔除**，未误建重复页 ✓
- 跨源 book 惯例：各取单作最集中/最具叙事分量之作定 book（US=FEM、Mississippi=AWED、Caucasus=MS、Bordeaux=AWED、Marseilles=JCE）✓
- YAML 冒号门（LAW §8）：5 页 description 均无裸冒号，unknown=0 ✓
- ≤400 字门：建前复验 5 页 0 段 over-400 ✓
- 前向红链：0（book label ×5 均既建；[[Mississippi]]/[[United States]]/[[Mediterranean]] 同批或既建；[[Russia]] 既建；New York/Paris/Illinois/New Orleans 等未既建者一律不链）✓
- 交叉核既有页：5 建页 slug/label 均无既有页碰撞 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R107→R108，NEW1）

- current_round 107→108
- type_round 78→79
- rounds_since_last_evv5 1→2
- rounds_since_last_discover 3→4
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 43→44
- last_updated_round 107→108

## 遗留问题

- **R108 预测 = NEW1（续消化 discover 残余）**：R107 末 queue≈25。矩阵 since_evv5=2、since_discover=4、queue≥10 → priority 3 不触发；default NEW1。建议 R108 取 America/Europe/Asia（洲级，须严筛洲级确指句 vs 泛指，America 并与 united-states 错开引注句）或 New York/Paris（城市层，主作待择，先评 link 密度）或 Berlin/Athens/Vienna/Madrid/Lisbon/Constantinople/Calais（城市层，7±；核 demonym）。
- **discover blindspot 实证累加（本轮 3 例）**：Pacific/Atlantic/Ural 三候选因既有页 label 未被 discover 比对而虚列为新候选——HK-discover-existing-type-blindspot 再获强证（此前 Reform Club R11、lake-tanganyika R64）。**修复方向不变**：discover 专名过滤须与 alias_index（含既建 pacific-ocean/atlantic-ocean/ural-mountains）比对去重。属 discover 逻辑债，PARK 待批量评审。宜给 pacific-ocean/atlantic-ocean 补 alias 'Pacific'/'Atlantic'（本地页面数据，character 轮或 PHQ 时处理）。
- **HOLD 累积**：Rome（明喻系）、Petersburg（缩写碎片）、Rhine/Thames（明喻+假匹配 <5）、Plata（真河 <5，余为 La Plata 地域）、Amsterdam（SC:13 多为 Amsterdam Isles 岛群非城，多实体筛后待核）、Long Island/Bay of Bengal——待专项凑句或 sentence_index 改进后再评。
- **薄候选严扫风险**：Ganges=5、Calais=6、Vienna/Madrid/Lisbon/Constantinople/Athens=7 逼近门；洲级 America/Europe/Asia 泛指风险高。
- **memex 规范缺陷（记 housekeeping，不赘）**：GROW.spec.md priority 3.5 corpus-discover 未同步权威算法（HK-corpus-discover-not-in-statemachine，P3 PARK）。
- **EVV5 节奏**：since_evv5 R107 末=2，下次约 R116。
- **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型 EVV6 全库评审并回填均分。
- **England/France 国级页评估 + R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理。
