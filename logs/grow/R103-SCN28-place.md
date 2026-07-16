---
round: 103
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R103 决策矩阵（读 R102 末计数器：queue=7、since_evv5=8、since_discover=4、discover_streak_low=0、since_corpus=39）。R102 已把可建国级积压消化至 queue=7（其中 5 薄候选 Mongolia/Austria/Kamtschatka/Prussia/Belgium 逼近门 + 2 permanent hold Long Island/Bay of Bengal）——**国名裸词层近枯**。矩阵字面：priority 3 SCN28 触发（queue=7<10）；priority 3.5 corpus-discover 亦名义触发（since_corpus=39≥30）。二者皆 discover 类，priority 3 序位在前 → **执行 SCN28 表层复扫**（表层未证竭，corpus 深扫顺延）。承 R98 教训——NEW1-override 前提为「可建 backlog 充裕」，现仅剩 5 薄候选严扫恐掉 <5，backlog 近枯 → 放行 genuine 表层 discover 补种，不再续 override。

承 R95/R98 方法论（**裸词绕过 geo 关键词后缀模式**），本轮改扫前几轮未及的粒度层——**洋/海/洲/大区/城市/河流**裸词，对 Verne 高频设定地逐一 `\bName\b` 全库词边界核 distinctPN，surface **约 30 个强真地名**，各 ≫5 且多有单源集中可定 book。queue 7→~37（+30）。new_candidates≈30≥3 → discover_streak_low 保持 0。**place 广度五度否证饱和**（R91 区/洲级 → R95 国级东亚 → R98 国级欧美亚 → R103 洋/海/城/河/大区级）；CLOSE 远未到。本轮不建页。

## 候选处理记录（表层复扫 surface，distinctPN 全库词边界核）

| 候选 | distinctPN | 主源集中 | 入队 | 层 | 备注 |
|------|-----------|---------|------|----|------|
| Pacific | 330 | TTLU:43/SC:28/GM:27/RC:27/FC:20 | ✓ | 洋 | 主作待择（TTLU 或按航段）|
| America | 259 | 跨源 | ✓ | 洲 | 泛指双义，建页须严筛洲级确指 vs United States 重叠 |
| Atlantic | 226 | TTLU:39/SC:24/EHLA:18/FF:16/AWED:14 | ✓ | 洋 | 主作待择 |
| Europe | 201 | 跨源 | ✓ | 洲 | 泛指风险，聚焦确指句 |
| New York | 137 | WC:27/AWED:25/TTLU:14/ASC:12/TT:10 | ✓ | 城 | 城市页密度评 link |
| United States | 131 | FEM/AWED/TT | ✓ | 国 | 与 America 分工：国 vs 洲 |
| Paris | 121 | ASC:19/TTLU:17/TT:11/AWED:10/RC:10 | ✓ | 城 | 主作待择 |
| Mediterranean | 112 | OC:46/TTLU:40 | ✓ | 海 | 主作 Off on a Comet 或 TTLU |
| Asia | 86 | 跨源 | ✓ | 洲 | 泛指风险 |
| Turkestan | 67 | ASC:56/MS:8 | ✓ | 大区 | 主作 The Adventures of a Special Correspondent |
| Nile | 51 | FWB:42 | ✓ | 河 | 主作 Five Weeks in a Balloon |
| Moscow | 45 | MS:39 | ✓ | 城 | 主作 Michael Strogoff |
| Argentine | 37 | SC:30/TT:3 | ✓ | 大区 | 主作 In Search of the Castaways；核 Argentine Republic 全称 |
| Congo | 27 | DSCF:19 | ✓ | 河 | 主作 Dick Sand（注 book 冒号）|
| Hamburg | 27 | JCE 待核 | ✓ | 城 | Lidenbrock 故乡，主作 A Journey to the Center of the Earth 待核 |
| Rome | 21 | 跨源 | ✓ | 城 | — |
| Petersburg | 20 | MS 待核 | ✓ | 城 | 异名 St. Petersburg，主作 Michael Strogoff 待核 |
| Valparaiso | 18 | DSCF:12/WC:3 | ✓ | 城 | Chili 港，主作 Dick Sand 待核（book 冒号）|
| Ural | 17 | 跨源 | ✓ | 河/山 | 核 Ural Mountains vs Ural River 分义 |
| Sahara | 16 | FWB:6/RC:4/OC:3 | ✓ | 沙漠 | 跨源待择 |
| Caucasus | 14 | 跨源 | ✓ | 大区 | 高加索山区 |
| Mississippi | 14 | 跨源 | ✓ | 河 | — |
| Geneva | 10 | 跨源 MZ | ✓ | 城 | Master Zacharius 舞台 |
| Amsterdam | 10 | 跨源 | ✓ | 城 | — |
| Guiana | 9 | 跨源 EHLA | ✓ | 大区 | 四圭亚那 |
| Marseilles | 8 | 跨源 | ✓ | 城 | — |
| Bordeaux | 8 | 跨源 | ✓ | 城 | — |
| Berlin | 8 | 跨源 | ✓ | 城 | — |
| Athens | 8 | 跨源 | ✓ | 城 | 核 Athens vs Athenian demonym |
| Vienna | 7 | 跨源 | ✓ | 城 | — |
| Madrid | 7 | 跨源 | ✓ | 城 | — |
| Lisbon | 7 | 跨源 | ✓ | 城 | — |
| Constantinople | 7 | 跨源 | ✓ | 城 | — |
| Thames | 7 | 跨源 | ✓ | 河 | — |
| Rhine | 7 | 跨源 | ✓ | 河 | — |
| Plata | 7 | 跨源 SC | ✓ | 河 | Rio de la Plata |
| Calais | 6 | 跨源 | ✓ | 城 | — |
| Ganges | 5 | 跨源 | ✓ | 河 | 恰达门槛 |
| Java / Pekin / England / France | — | — | ✗ | — | Java=Cunard 汽船（词边界剔）；Pekin=Peking 异名（核既建）；England 221/France 169 续暂缓（城市页密集，国级页价值 R104+ 专项评）|

## EXIT-GATE 检查

- discover 轮不建页，G4/place-schema/GROW-JUDGMENT-R50 页级门不适用（无新页）✓
- 候选 distinctPN 全部 `\bName\b` 词边界全库核（非子串 agg），≥5 方入队 ✓
- 多实体筛查：Java 剔（the Java=Cunard 汽船系，承 TTLU-001-021 船名清单）；America/Asia/Europe 标注泛指双义须建页时严筛；Ural 标注山/河分义待核；Athens 标注 demonym 风险 ✓
- 城市异名去重：Petersburg=St. Petersburg、Pekin=Peking，建页前核既建 ✓
- covered 去重：Siberia/Greenland/Iceland/Zanzibar/Patagonia/Gobi 已建，probe 跳过 ✓
- 门下未入队：Ganges 恰达 5 入队；未列 <5 者不入队 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R103→R104，SCN28）

- current_round 103→104
- type_round 74→75
- rounds_since_last_evv5 8→9
- rounds_since_last_discover 4→**0**（表层 discover 复位）
- discover_streak_low 0（new_candidates≈30≥3，保持 0，不累加）
- rounds_since_last_corpus_discover 39→40
- last_updated_round 103→104

## 遗留问题

- **R104 预测 = NEW1（消化新洋/海/城/河积压）**：R103 末 queue=~37（约 30 新可建 + 5 薄国级残余 + 2 hold）。矩阵字面 since_discover=0、queue≥10 → priority 3 不触发；default priority 6 NEW1。**建议 R104 起连续 NEW1** 按 distinctPN 降序消化：首批可取 Pacific/Atlantic/Mediterranean（洋/海层，各 ≥112）或 Nile/Moscow/Turkestan（单源集中易定 book）。每轮 5 页，聚焦主作确指句。
- **洋/海/洲级泛指风险**：Pacific/Atlantic/Mediterranean/America/Europe/Asia 单义模糊——洋级须聚焦「Verne 航段中之设定海域」确指句，洲级（America/Europe/Asia）须严筛洲级确指 vs 泛指/国名重叠。America↔United States 分工：一为洲、一为国，建页须错开引注句避免重叠。
- **城市页 link 密度顾虑**：New York/Paris/Rome 等城市页与既有人物/事件页潜在高重叠，建页前评 backlink 密度；若与既有城市页（伦敦/巴黎待核）碰撞则合并或聚焦。
- **主作待核候选**：Hamburg（JCE?Lidenbrock 故乡待核）、Petersburg（MS 待核，异名 St. Petersburg）、Valparaiso（DSCF 待核，book 冒号）、Congo（DSCF，book 冒号）——建页前 gather.py 核主源确指句 + LAW §8 冒号引号预防。
- **薄候选严扫风险**：Ganges=5、Calais=6、Vienna/Madrid/Lisbon/Constantinople/Athens=7 逼近门，建页词边界复核若掉 <5 转 hold（同 Long Island/Bay of Bengal 处置）。5 国级残余（Mongolia/Austria/Kamtschatka/Prussia/Belgium）同理。
- **corpus-discover 顺延临界**：since_corpus R103 末=40，priority 3.5（≥30）名义持续触发，但表层未竭 → 待新积压再度排空且表层确认 0 新时再评 corpus 深扫。
- **EVV5 逼近**：since_evv5 R103 末=9，R105 触发（priority 1b，序位最高，届时 override 一切）。
- **England/France 国级页评估**（承 R96-R102）：国级 backlog 已消化，但城市页密集顾虑未解 → R104 后专项评估是否纳入。
- **R77 五页补核 + peru/lima + spain/gibraltar 交叉核**：待新积压消化后专项处理。
