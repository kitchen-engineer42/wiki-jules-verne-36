---
round: 111
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R111 决策矩阵（读 R110 末计数器：queue=9、since_evv5=5、since_discover=7、discover_streak_low=0、since_corpus=47）。按**权威算法 `grow-state-machine.md §3`**逐条：since_evv5=5<10 → 非 EVV5；streak=0<3 → 非 CLOSE；**queue_size=9 < discover_queue_threshold=10 → priority 3 命中 → gene = SCN28**（队列低水位触发）。（priority 3.5 corpus-discover 死分支，不赘。）

R110 末 queue 9 开放候选中，可建者近乎归零：Long Island/Bay of Bengal 真指=4<门（续 hold）；Asia/Europe/America 洲级留严筛专轮；Amsterdam(岛群)/Thames/Rhine/Plata(明喻/真河<5) 皆 hold。故 SCN28 须补种。

前几轮 discover（R91 区/洲级、R95/R98 国级）已四度否证国家层饱和。本轮**转城市/山脉/河流/海湾特征层**扫描：对 Verne 高频城市、港口、山系、河流、内海/海湾候选逐一 `\bName\b` 全库词边界核 distinctPN，先去既建（2641 name/alias/slug tokens 集合过滤），≥5 方入队。**surface 35 个新候选**，多有单源高度集中（ASC 大铁路沿线城 Bokhara/Tiflis/Merv/Baku、JCE Copenhagen、MS Baikal、WC Brest、OC Malta/Sicily/Algiers/Sardinia），可定 book。queue 9→44。new_candidates=35 ≫ type_close_new_candidate_min=3 → discover_streak_low 保持 0，CLOSE 远未到。**「place 广度饱和」假设再度被否证**（城市-地理特征层富矿）。本轮不建页。

## 候选处理记录（表层复扫 surface，distinctPN 全库 \bName\b 词边界核）

| 候选 | distinctPN | 主源集中 | 入队 | 类别/备注 |
|------|-----------|---------|------|------|
| Caspian | 53 | ASC:30/RC:10/MS:6 | ✓ | 内海；大铁路横渡；alias Caspian Sea |
| Edinburgh | 35 | UC:15/FWB:7 | ✓ | 城；建页剔「Modern/Northern Athens」称号句 |
| Bokhara | 34 | ASC:22/MS:12 | ✓ | 中亚城/大铁路 |
| Andes | 34 | SC:18/DSCF:7 | ✓ | 南美山脉 |
| Tiflis | 30 | ASC:30 | ✓ | 高加索城/大铁路西端 |
| Alps | 29 | SC:13/AMB:4 | ✓ | 欧洲山脉；核比喻/列举 |
| Merv | 26 | ASC:26 | ✓ | 中亚城/大铁路 |
| Malta | 22 | OC:9/WC:6 | ✓ | 地中海岛 |
| Baku | 22 | ASC:22 | ✓ | 里海油城/大铁路端点 |
| Sicily | 19 | OC:8/TTLU:3 | ✓ | 地中海岛 |
| Copenhagen | 17 | JCE:8 | ✓ | 地心游记起点城 |
| Brest | 17 | WC:14/TTLU:3 | ✓ | 法国大西洋军港 |
| Baikal | 17 | MS:17 | ✓ | 西伯利亚大湖 |
| Frankfort | 16 | VB:7/DA:6 | ✓ | 气球史城；核美国同名 |
| Algiers | 15 | OC:12 | ✓ | 北非城 |
| Etna | 11 | RM:3/SI:2 | ✓ | 西西里火山 |
| Riga | 10 | MS:8 | ✓ | 波罗的海港城 |
| Lyons | 10 | 跨源 | ✓ | 法国城；alias Lyon |
| Havre | 9 | WC 等跨源 | ✓ | 法国港 Le Havre |
| Lucknow | 7 | SC:7 | ✓ | 印度城 |
| Corsica | 7 | MI:2/OC:2 | ✓ | 地中海岛 |
| Baltic | 7 | MS:3 | ✓ | 波罗的海；alias Baltic Sea |
| Archangel | 7 | FC:6 | ✓ | 俄北冰洋港 |
| Sardinia | 6 | OC:5 | ✓ | 地中海岛 |
| Teheran | 5 | ASC:3 | ✓ | 波斯首都；跨源凑门 |
| Lena | 5 | WC:3/MS:2 | ✓ | 西伯利亚河 |
| Himalaya | 5 | ASC:2/AWED:2 | ✓ | 山脉；alias Himalayas |
| Elbe | 5 | JCE:4 | ✓ | 德国河 |
| Dublin | 5 | 跨源 | ✓ | 爱尔兰城 |
| Crete | 5 | TTLU:5 | ✓ | 地中海岛/Nautilus 掠岸 |
| Astrakhan | 5 | RC:3/MS:2 | ✓ | 里海口城 |
| Aral | 5 | ASC:3 | ✓ | 咸海；alias Aral Sea |
| Amou-Daria | 5 | ASC:5 | ✓ | 中亚河 Oxus |
| Alexandria | 5 | WC:2 跨源 | ✓ | 埃及港城；核美国同名 |
| Adriatic | 5 | TTLU:2 | ✓ | 亚得里亚海；alias Adriatic Sea |
| （既建跳过）Bombay/Benares/Copenhagen∗… | — | — | — | Bombay/Benares 等已建，probe 前 2641-name 集合已滤 |

## EXIT-GATE 检查

- discover 轮不建页，G4/place-schema/GROW-JUDGMENT-R50 页级门不适用（无新页）✓
- 候选 distinctPN 全部 `\bName\b` 词边界全库核（非子串 agg），≥5 方入队 ✓
- covered 去重：probe 前以 pages.json 全量 name/alias/slug（2641 tokens）集合过滤，既建（Bombay/Benares/Naples/Venice/Geneva/Moscow… 等）自动跳过 ✓
- 门下剔除：<5 distinctPN 者（Warsaw/Odessa/Cairo… 若有）未入队 ✓
- 多实体/称号预警（建页时复核）：Edinburgh(「Modern Athens」称号)、Frankfort/Alexandria(美国同名地)、Caspian/Baltic/Aral/Adriatic(海洋泛指须取确指句)、Merv/Baku(词边界已核纯专名)✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R111→R112，SCN28）

- current_round 111→112
- type_round 82→83
- rounds_since_last_evv5 5→6
- rounds_since_last_discover 7→**0**（表层 discover 复位）
- discover_streak_low 0（new_candidates=35≥3，保持 0，不累加）
- rounds_since_last_corpus_discover 47→48
- last_updated_round 111→112

## 遗留问题

- **R112 预测 = NEW1（消化 SCN28 新积压）**：R111 末 queue=44。矩阵 since_discover=0、queue=44≥10 → priority 3 不触发；default priority 6 NEW1。**建议 R112 起连续 NEW1** 按 distinctPN 降序消化：首批 Caspian/Edinburgh/Bokhara/Andes/Tiflis（各 ≥30），每轮 5 页，聚焦主源确指句。
- **建页前复核清单**：Edinburgh 剔「Modern/Northern Athens」称号句；Frankfort/Alexandria 核与美国同名城错开；Caspian/Baltic/Aral/Adriatic 海洋类取确指句非泛指；Andes/Alps/Himalaya 山脉类核比喻/列举；Lyons(alias Lyon)/Havre(Le Havre)/Amou-Daria(Oxus) 别名规范。
- **主源集中利好**：ASC 大铁路沿线（Bokhara/Tiflis/Merv/Baku/Teheran/Amou-Daria）高度集中，book=The Adventures of a Special Correspondent；跨源薄候选建页须凑 ≥5 确指句。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD。
- **discover blindspot（承 R107）**：pacific/atlantic/ural 补 alias（PHQ）。
- **memex 规范缺陷**：HK-corpus-discover-not-in-statemachine（P3 PARK）。
- **EVV5 节奏**：since_evv5 R111 末=6，下次约 R115。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
- **R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待 discover 积压消化后专项处理；注 Malta/Sicily/Sardinia/Corsica 地中海岛群若建，与既有 Mediterranean 页联动。
