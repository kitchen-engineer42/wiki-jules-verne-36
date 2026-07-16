---
round: 121
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [florida, south-pole, kamtchatka, timbuctoo, chicago]
result: success
---

## 执行摘要

R121 决策矩阵（读 R120 末计数器：queue=12、since_evv5=4、since_discover=0、discover_streak_low=0、since_corpus=57）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=4<10 → 非 EVV5；streak=0<3 → 非 CLOSE+SCN28；queue=12≥discover_queue_threshold(10) 且 since_discover=0<10 → 非 SCN28；queue(place)≠0 → 非 zombie；stub%=0<20 → 非 RCH2、非 NEW1+RCH2；**default → gene = NEW1**。

NEW1 消化 R120 SCN28 补种的 6 新候选之首批 5 页。每页 4 个 H2（Overview / In the Narrative / Geography & Features / Connections），每句 PN-grounded（`data/sentence_index/`），≥5 distinct PN，段落 ≤400 字，pn_validator warn 模式 0 issues。Salt Lake City（5 恰达门）留次批逐句核后建。

**建页明细**：

| slug | rev | book | rof | region | distinctPN 引注 |
|------|-----|------|-----|--------|----------------|
| florida | JiVza6 | From the Earth to the Moon | real | Southeastern United States | 9（FEM×8+RM+TTLU）|
| south-pole | CN7mLW | Twenty Thousand Leagues Under the Sea | real | Antarctic | 9（TTLU×7+SC+GM）|
| kamtchatka | 11Qwkq | The Fur Country | real | Russian Far East | 9（FC×9）|
| timbuctoo | BxFzWZ | Five Weeks in a Balloon | real | West Africa | 11（FWB×11）|
| chicago | 8Et6kp | Around the World in Eighty Days | real | United States | 7（AWED×4+RC+MW+GM）|

**同名/实体消歧核查**：
- **florida**：剔 Florida Strait/Florida Keys 泛指海域混引；确认与既有 tampa-town/stony-hill（同为 FEM Columbiad 簇）为「州—城/工地」隶属关系，非同名；alias「Pascha Florida」（原名，Ponce de Leon 1512）。
- **south-pole**：**关键——RM（Round the Moon）多处「South Pole」实指月球南极（lunar spheroid），非地球南极，已全数剔除**（RM-011-006/017-002/017-007/019-069/016-009）；label 取裸名「South Pole」（不加「The」前缀）以规避 label-prefix 红链盲区；TTLU-037-022 磁极≠地理极的区分句保留作特征。
- **kamtchatka**：主导引注为「Kamtchatka Current」（以半岛命名的洋流）——属地名派生特征（如城名产品型 legitimate namesake），非异地同名陷阱；页面以半岛/地区为主体，洋流列为特征。
- **timbuctoo**：FWB 单源，非洲名城，无同名；alias「Timbuktu」现代拼写。
- **chicago**：美国伊利诺伊城，四源交叉（AWED Fogg 铁路 / RC Albatross 空视 / MW 机器现踪 / GM 胖子秀），无同名陷阱。

place 页数 319→324，registry 1387→1392，unknown 0。queue 开放候选 12→7（-5 建成）。backlinks 覆盖 1223 页 / 3161 条（+28 条）。

## 页面处理记录

| 动作 | 对象 | rev | 说明 |
|------|------|-----|------|
| add_page | florida | JiVza6 | FEM Gun Club 发射州；9 引注；链 gun-club/tampa-town/stony-hill/columbiad/from-the-earth-to-the-moon/round-the-moon |
| add_page | south-pole | CN7mLW | TTLU Nemo 立旗地球南极；9 引注；剔 RM 月面南极；链 nautilus/captain-nemo/ice-bank/north-pole/twenty-thousand-leagues |
| add_page | kamtchatka | 11Qwkq | FC 半岛+同名洋流；9 引注；链 victoria-island/cape-bathurst/aleutian-islands/behring-strait/siberia/the-fur-country |
| add_page | timbuctoo | BxFzWZ | FWB 沙漠名城；11 引注；alias Timbuktu；链 sahara/africa/lake-tchad/five-weeks-in-a-balloon |
| add_page | chicago | 8Et6kp | AWED 铁路枢纽；7 引注；链 phileas-fogg/omaha/new-york/albatross/lake-michigan/around-the-world/robur-the-conqueror |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 写入，未直写 docs/pages ✓
- PN grounding：5 页 pn_validator warn 模式各 0 issues；每页 ≥5 distinct PN（最低 chicago 7）✓
- 段落长度：均 ≤400 字 ✓
- 结构：每页恰 4 H2（Overview/In the Narrative/Geography & Features/Connections）✓
- frontmatter：9 字段齐（id/type/label/aliases/tags/book/real_or_fictional/region/description），quality 由 add_page 回填 featured，未手写 ✓
- LAW §8：含冒号的 description 均单引号包裹 ✓
- LAW §9：wikilink 均指向既有页（建前逐一核 pages.json；Texas/Niger/Antarctic 等缺页未链）✓
- 同名消歧：south-pole 剔 RM 月面南极；florida 剔海峡泛指；kamtchatka 洋流为特征非陷阱——见上 ✓
- unknown=0；place 319→324；registry 1387→1392 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean（待 commit 时复核）

## 六步状态机（R121→R122，NEW1）

- current_round 121→122
- type_round 92→93
- rounds_since_last_evv5 4→5
- rounds_since_last_discover 0→1
- discover_streak_low 0（NEW1 不改）
- rounds_since_last_corpus_discover 57→58
- last_updated_round 121→122

## 遗留问题

- **R122 预测 = NEW1**：R121 末 queue=7<10……需重核。queue=7≥？否——**7<discover_queue_threshold(10) → SCN28 优先级命中**。故 **R122 预测 = SCN28**（queue 低水位复现）。续消化前应先补种：R122 SCN28 表层勘探（broken-link 复扫 + 剩余 curated 地名批测），并处理 Salt Lake City（borderline 5，逐句核确指后可 NEW1 建）。若 SCN28 产出≥3 新候选，queue 回升后 R123 转 NEW1。
- **Salt Lake City 挂起**：5 distinctPN 恰达门（AWED 摩门篇），borderline，留 R122+ 逐句核确指后建（剔 Great Salt Lake 湖泊混引——已建 great-salt-lake rev 5hL12o）。
- **discover blindspot（label-prefix「The X」，承 R120）**：north-pole/great-eyrie 已补裸名 alias；**PHQ 待批量排查所有 label 带「The」前缀的 place/character 页**（The Moon/the-moon、The Chimneys/the-chimneys 等），统一补裸名 alias。
- **discover blindspot（后缀变体，承 R117，5 例）**：pacific/atlantic/ural/caspian/baikal——PHQ 批量补裸名 alias + probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。
- **主要地名入队盲区教训（承 R120）**：probe 应增「国家/州/半岛/极点/名城」显式枚举维度；本轮 5 高 PN 裸名地名（Florida 52/South Pole 35/Kamtchatka 23/Timbuctoo 22）均此前未入队。
- **PHQ 待决候选**：Long Island/Bay of Bengal（4<门）、Amsterdam 荷兰城（<5）、Lucknow（澳洲路名）、真俄 Archangel（1 PN）、label-prefix「The X」批量 alias、后缀变体批量 alias——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV5 节奏**：R116 已做（since_evv5 归 0）；下次约 R127（since_evv5 R121 末=5）。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
