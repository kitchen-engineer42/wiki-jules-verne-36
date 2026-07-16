---
round: 125
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [madras, sydney, perth, adelaide, vancouver-island]
result: success
---

## 执行摘要

R125 决策矩阵（读 R124 末计数器：queue=16、since_evv5=8、since_discover=2、discover_streak_low=0、since_corpus=61）。按**权威算法 `grow-state-machine.md §3`**：since_evv5=8<10 → 非 EVV5；streak=0<3 → 非 CLOSE；queue=16≥10 且 since_discover=2<10 → 非 SCN28；queue(place)≠0 → 非 zombie；stub%=0 → 非 RCH2/NEW1+RCH2；**default → gene = NEW1**。

低消歧候选渐稀，本轮转攻 R122 补种之 ⚠ 标记候选，逐句核实指涉主体后建 5 页。每页 4 H2、每句 PN-grounded、≥5 distinct PN、段落 ≤400 字、pn_validator warn 模式 0 issues。

**建页明细**：

| slug | rev | book | rof | region | distinctPN 引注 |
|------|-----|------|-----|--------|----------------|
| madras | eNxcyq | Around the World in Eighty Days | real | India | 5（AWED×3+FEM+SC）|
| sydney | hAroyY | In Search of the Castaways | real | Australia | 6（SC×5+RC）|
| perth | hdypn9 | In Search of the Castaways | real | Western Australia | 6（SC×6，剔苏格兰同名）|
| adelaide | vNw7Cb | In Search of the Castaways | real | South Australia | 8（SC×7+RC，剔南极/北极同名）|
| vancouver-island | 5lHdxD | The Waif of the Cynthia | real | Pacific | 5（WC×4+RC，重定主体=岛）|

**同名/实体消歧核查（本轮关键）**：
- **perth**：⚠**Perth 双指涉**——SC-004-010「started off for Perth... arrived at Malcolm Castle」实指 **Perth 苏格兰**（Grant/Glenarvan 家族城堡在苏格兰），剔除；余 6 PN（SC-037-055/039-042/041-018/043-013/046-063/063-059）均明指 **Perth, Western Australia** 囚犯流放地首府（Ben Joyce 越狱、Penitentiary、capital of Western Australia）。页定 real/Western Australia。
- **adelaide**：⚠剔 2 同名地物——TTLU-038-094「Adelaide Land at latitude 67」（Biscoe 1832 发现之南极地）+ ACH-015-010「Adelaide Bay」（Prince Regent's Channel 旁北极湾）；余 8 PN（SC×7 城/省 + RC-001-030 观测台）均指南澳首府城。
- **vancouver-island**：⚠**重定主体=岛非城**——候选原为「Vancouver」城，但全 6 gather 命中均为「Vancouver('s) Island」（RC-011-003 海岸曲线、WC×4 Tudor Brown 游艇母港/Victoria on coast of Vancouver）；无城市直接引注。改建 `vancouver-island`（label Vancouver Island）。剔 TT-015-015 子午线（命中不确定）。⚠WC 中「Albatross」为 Tudor Brown 游艇（≠ Robur 飞艇），未链 albatross。
- **madras**：印度城，AWED 东印度公司立足点/总督驻地 + FEM 贺电 + SC 商埠列举，5 源一致；borderline 5 恰达门，逐句核确指城。
- **sydney**：⚠核 Cape Sidney/人名同名——6 PN 均明指新州港城（SC 前首府、Twofold Bay 无船通 Sydney、RC 观测台），无 Cape Sidney 歧义。

place 页数 334→339，registry 1402→1407，unknown 0。queue 开放候选 16→11（-5 建成）。backlinks 覆盖 1231 页 / 3225 条。

## 页面处理记录

| 动作 | 对象 | rev | 说明 |
|------|------|-----|------|
| add_page | madras | eNxcyq | 东印度公司立足点/南印度总督城；链 bombay/calcutta/around-the-world-in-eighty-days |
| add_page | sydney | hAroyY | 新州港城/前首府；链 adelaide/melbourne/in-search-of-the-castaways |
| add_page | perth | hdypn9 | 西澳流放地首府；剔 Perth 苏格兰 PN；链 melbourne/in-search-of-the-castaways |
| add_page | adelaide | vNw7Cb | 南澳首府港；剔南极 Adelaide Land + 北极 Adelaide Bay；链 sydney/melbourne/in-search-of-the-castaways |
| add_page | vancouver-island | 5lHdxD | Tudor Brown 游艇母港，重定主体为岛；链 aleutian-islands/the-waif-of-the-cynthia |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 写入 ✓
- PN grounding：5 页 pn_validator warn 模式各 0 issues；每页 ≥5 distinct PN（最低 madras/vancouver-island 5）✓
- 段落长度 ≤400 字；每页恰 4 H2 ✓
- frontmatter 9 字段齐，quality 由 add_page 回填 featured ✓
- LAW §8 含冒号 description 单引号 ✓；§9 wikilink 均指既有页（建前核；victoria/new-south-wales/malcolm-castle 缺页未链；同批 adelaide↔sydney 互链建后 registry 重建已解析）✓
- 同名消歧：perth 剔苏格兰、adelaide 剔南极/北极同名、vancouver 重定为岛、sydney 无 Cape Sidney 歧义——见上 ✓
- unknown=0；place 334→339；registry 1402→1407 ✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean（待 commit 复核）

## 六步状态机（R125→R126，NEW1）

- current_round 125→126
- type_round 96→97
- rounds_since_last_evv5 8→9
- rounds_since_last_discover 2→3
- discover_streak_low 0（NEW1 不改）
- rounds_since_last_corpus_discover 61→62
- last_updated_round 125→126

## 遗留问题

- **R126 预测 = NEW1（末轮 NEW1，EVV5 前夜）**：R125 末 queue=11≥10、since_evv5=9<10、streak=0<3、since_discover=3<10、queue(place)≠0、stub%=0 → 默认 NEW1。**R126 建成后 since_evv5→10，R127 将触发 EVV5**（since_discover R127 时=5<10，故预期纯 EVV5 非 EVV5+SCN28）。
- **R126 候选建议**：低风险剩 Amsterdam(10，逐句核阿姆斯特丹城确指)、Salt Lake City(5 borderline，AWED 摩门篇)；其余多为 ⚠ 重消歧（Washington 78/Charleston 49/Richmond 30/Panama 11）或结构 hold（Long Island/Bay of Bengal 4<门、Asia/Europe/America 洲级）。R126 可取 Amsterdam+Salt Lake City + 谨慎启 Panama（城 vs 地峡 vs 运河，逐句定主体）或 Charleston（SC 城 vs FEM Charlestown MA）等大 PN ⚠候选。
- **queue 渐稀预警**：非 ⚠ 非 hold 的低风险候选仅余 2（Amsterdam/Salt Lake City）。R126 后若 queue 低风险耗尽，R127 EVV5 之后或需 SCN28 补种（since_discover 届时=5，未达 10；但若 queue<10 亦触发 SCN28）。当前 queue=11，R126 建 5 后 queue≈6<10 → **R127 即便非 EVV5 亦会因 queue<10 触发 SCN28**；实际 R127 EVV5 优先（§3 first-match EVV5 在 SCN28 之前）。
- **消歧待决候选（留次批）**：Washington（城/人/州/堡）、Charleston（SC vs Charlestown MA）、Richmond（VA vs 伦敦）、Panama（城/地峡/运河）——建前逐句核。
- **Detroit 弃建备忘（承 R124）**：类「城名实为同名水道/地物」候选建前 gather 逐句核指涉主体。
- **EVV5 节奏**：R127 触发（since_evv5 R125 末=9，R126 建后=10）。
- **corpus-discover 逾期（HK-corpus-discover-not-in-statemachine）**：since_corpus=62，逾 interval(30) 两周期；状态机无分支触发，park 待 PHQ/RFC。
- **work 复数变体红链（承 R122）**：`[[Twenty Thousand Leagues Under the Seas]]`（复数，×7）→ 既有单数 work 页；PHQ 补复数 alias。
- **discover blindspot（label-prefix「The X」+ 后缀变体，承 R117/R120）**：PHQ 批量补裸名 alias。
- **PHQ 待决候选**：Tasmania 的 Van Diemen's Land 别名、Perth 的 Perth 苏格兰独立页评估（仅 SC-004-010 一句，<门，暂缓）、Salt Lake City(5)、Long Island/Bay of Bengal(4<门)、Amsterdam、Lucknow、真俄 Archangel(1)、Stone's Hill 修源 + stony-hill rof 缺值回填、各类 alias 批量——挂起待 PHQ。
- **洲级严筛专轮（未决）**：America/Europe/Asia 续 HOLD；America 须与 united-states 消歧。
- **EVV6 封存点预告**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填均分。
