---
round: 123
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [philadelphia, newfoundland, boston, spitzbergen, montreal]
result: success
---

## 执行摘要

R123 决策矩阵（读 R122 末计数器：queue=27、since_evv5=6、since_discover=0、discover_streak_low=0、since_corpus=59）。按**权威算法 `grow-state-machine.md §3`**：since_evv5=6<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=27≥10 且 since_discover=0<10 → 非 SCN28；queue(place)≠0 → 非 zombie；stub%=0<20 → 非 RCH2/NEW1+RCH2；**default → gene = NEW1**。

NEW1 消化 R122 补种 20 候选之首批 5 页——取无重消歧风险且高 PN 者。每页 4 H2、每句 PN-grounded、≥5 distinct PN、段落 ≤400 字、pn_validator warn 模式 0 issues。

**建页明细**：

| slug | rev | book | rof | region | distinctPN 引注 |
|------|-----|------|-----|--------|----------------|
| philadelphia | 6mAvp2 | Robur the Conqueror | real | United States | 9（RC×4+MW×3+FEM×2）|
| newfoundland | 8l4Y6q | Ticket No. 9672 | real | North Atlantic | 9（TN×6+ACH×3+AWED+RM）|
| boston | Sa5Cb0 | Master of the World | real | United States | 9（MW×4+BR×2+ASC+FEM）|
| spitzbergen | 7Pt8PL | The Adventures of Captain Hatteras | real | Arctic | 9（ACH×4+RC×2+WAI+TTLU×2+JCE）|
| montreal | adB03N | Robur the Conqueror | real | Canada | 8（RC×3+WC×2+FC×2）|

**同名/实体消歧核查（本轮关键）**：
- **newfoundland**：⚠**Newfoundland dog（犬种）陷阱**——gather 命中含 4 处犬种（AM-005-013/EHLA-014-013/FC-035-048/FEM-025-018），全数剔除；仅用地名 PN（TN 渔场/ACH Gulf Stream/AWED Banks/RM 电缆登陆）。
- **boston**：⚠剔 DA-001-155（英国气球家 Sadler「dragged over the town of Boston and dashed against the chimneys」，疑指 Boston 英格兰/林肯郡，非美国 Boston）；仅用明确美国 Boston PN（MW 海怪/BR 废奴/ASC 传教士/FEM 联邦城市列举）。
- **montreal**：⚠剔 ACH-017-015（北极「Montreal Island」同名岛，与 Maconochie/Ogle Point 并列）；TTLU「Montreal Ocean Co / Montreal lines」为以城命名的船司 namesake（未作城市直接引注）；仅用 RC（Albatross 空视 Victoria Bridge/St. Lawrence）+ FC（North-west Company 皮毛贸易 HQ）+ WC（电缆/煤补给）城市 PN。
- **philadelphia**：无同名陷阱；RC Weldon Institute/Walnut Street + MW Uncle Prudent 城 + FEM Baltimore 对铸城，四源一致指宾州城。
- **spitzbergen**：无同名陷阱；北极群岛，ACH/RC/TTLU/JCE/WAI 五源一致。

place 页数 324→329，registry 1392→1397，unknown 0。queue 开放候选 27→22（-5 建成，Richmond 消歧未决留次批）。backlinks 覆盖 1225 页 / 3187 条。

## 页面处理记录

| 动作 | 对象 | rev | 说明 |
|------|------|-----|------|
| add_page | philadelphia | 6mAvp2 | RC Weldon Institute 城；链 weldon-institute/baltimore/new-york/gun-club/robur-the-conqueror |
| add_page | newfoundland | 8l4Y6q | TN 渔场/北大西洋岛；剔犬种 4 PN；链 iceland/greenland/norway/gulf-stream/phileas-fogg/ticket-no-9672/around-the-world |
| add_page | boston | Sa5Cb0 | MW 海怪近岸 New England 港；剔 DA 英国 Boston；链 the-great-eyrie/new-york |
| add_page | spitzbergen | 7Pt8PL | ACH 北极群岛门户；链 greenland/iceland/norway/gulf-stream/the-adventures-of-captain-hatteras/robur-the-conqueror |
| add_page | montreal | adB03N | RC Albatross 空视 St. Lawrence 城；剔北极同名岛+船司 namesake；链 albatross/san-francisco/robur-the-conqueror/the-waif-of-the-cynthia/the-fur-country |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 写入 ✓
- PN grounding：5 页 pn_validator warn 模式各 0 issues；每页 ≥5 distinct PN（最低 montreal 8）✓
- 段落长度 ≤400 字；每页恰 4 H2 ✓
- frontmatter 9 字段齐，quality 由 add_page 回填 featured ✓
- LAW §8 含冒号 description 单引号 ✓；§9 wikilink 均指既有页（建前核；Texas/Ottawa/Labrador/Nova Zembla 等缺页未链）✓
- 同名消歧：newfoundland 剔犬种、boston 剔英国 Boston、montreal 剔北极同名岛+船司 namesake——见上 ✓
- unknown=0；place 324→329；registry 1392→1397 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean（待 commit 复核）

## 六步状态机（R123→R124，NEW1）

- current_round 123→124
- type_round 94→95
- rounds_since_last_evv5 6→7
- rounds_since_last_discover 0→1
- discover_streak_low 0（NEW1 不改）
- rounds_since_last_corpus_discover 59→60
- last_updated_round 123→124

## 遗留问题

- **R124 预测 = NEW1**：R123 末 queue=22≥10、since_evv5=7<10、streak=0<3、since_discover=1<10、queue(place)≠0、stub%=0 → 默认 NEW1。续消化 R122 补种候选。建议次批取无消歧风险高 PN 者：Charleston（先核 SC 城 vs FEM Charlestown MA）、Washington（重消歧：城/人/州/堡）、Panama（城 vs 地峡 vs 运河）、Adelaide、New Orleans；或先建低风险 Quebec/Rio de Janeiro/Labrador/Tasmania/Detroit。⚠高消歧候选建前逐句核确指主体。
- **消歧待决候选（留次批）**：Richmond（VA vs 伦敦）、Washington（城/人/州/堡）、Charleston（SC vs Charlestown MA）、Panama（城/地峡/运河）、Adelaide（城 vs 南极岸 vs 人名）、Perth（西澳 vs 苏格兰）、Sydney（城 vs Cape Sidney）、Vancouver（岛 vs 城 vs 人）——建前逐句核。
- **EVV5 节奏**：下次约 R127（since_evv5 R123 末=7）；R127 将 since_evv5≥10 触发 EVV5（或 EVV5+SCN28 若届时 since_discover 也≥10）。
- **corpus-discover 逾期（HK-corpus-discover-not-in-statemachine）**：since_corpus=60，逾 interval(30) 两周期；状态机无分支触发，park 待 PHQ/RFC。
- **work 复数变体红链（承 R122）**：`[[Twenty Thousand Leagues Under the Seas]]`（复数，×7）→ 既有单数 work 页；PHQ 补复数 alias。
- **discover blindspot（label-prefix「The X」+ 后缀变体，承 R117/R120）**：PHQ 批量补裸名 alias。
- **PHQ 待决候选**：Salt Lake City(5)、Madras(5)、Long Island/Bay of Bengal(4<门)、Amsterdam(<5)、Lucknow、真俄 Archangel(1)、Stone's Hill 修源 + stony-hill rof 缺值回填、各类 alias 批量——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
