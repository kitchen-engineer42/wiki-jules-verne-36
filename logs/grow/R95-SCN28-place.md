---
round: 95
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R95 决策矩阵（读 R94 末计数器：queue=2<10、since_evv5=0、since_discover=3、discover_streak_low=0、since_corpus=31）→ 优先级 3 **SCN28 表层复扫**（queue<10 触发；首匹配抢先于 since_corpus=31≥30 本会触发的 3.5 corpus-discover）。不建页。选表层而非 corpus-deep：表层 discover 的 discover_streak_low 才是 place-CLOSE 触发器，须让其在真实枯竭时正当累加。

**表层 geo-adjacency 扫回噪声 0 新**（Victoria 多实体/America 泛指/Klock 子串/Niagara 既建裸名/Floridian·Algerian demonym）。但注意到 **geo 关键词模式漏掉裸国名**（国名后无 river/sea/mount 等后缀），遂承 R91「国级层未穷尽」预告，对 Verne 高频设定国逐一 `\bName\b` 全库核 distinctPN——surface 一批国家级真地名。**new_candidates=10 ≥ 3 → discover_streak_low 保持 0**，否证「表层 0 新 → place 趋 CLOSE」假信号：place 广度在国级层仍有大量未穷尽。queue 2→12。

## 页面处理记录

（discover 轮，无建页）

### 新增候选（国家级，各词边界核 distinctPN ≫5）

| 候选 | distinctPN | 主源 | rof | 备注 |
|------|-----------|------|-----|------|
| China | 107 | ASC:56 / AWED:14 | real | Claudius Bombarnac 大铁路穿华，主作 The Adventures of a Special Correspondent |
| India | 93 | AWED:28 / SC:13 / RC:9 | real | 八十天环游主段，主作 Around the World in Eighty Days |
| Russia | 115 | MS:49 / ASC:16 / TT:16 | real | Michael Strogoff 全书舞台，主作 Michael Strogoff |
| Scotland | 43 | SC:19 / UC:9 | real | Glenarvan 故乡 + 地下城，主作 In Search of the Castaways |
| Brazil | 58 | EHLA:39 | real | 八百里亚马逊之国，主作 Eight Hundred Leagues on the Amazon |
| Peru | 49 | EHLA:19 / PL:13 | real | 亚马逊上游/利马之珠，主作 Eight Hundred Leagues on the Amazon |
| Sweden | 42 | WC:13 / TT:11 / TN:7 | real | Cynthia 弃儿之国，主作 The Waif of the Cynthia |
| Japan | 36 | AWED:11 / TTLU:9 | real | 八十天环游横滨段，主作 Around the World in Eighty Days |
| Egypt | 26 | DSCF:7 / TTLU:6 / OC:3 | real | 跨源；主作待建页复核 |
| Ceylon | 17 | TTLU:13 | real | Nautilus 采珠场，主作 Twenty Thousand Leagues Under the Seas |

### 剔除/噪声（未入队）

| 候选 | distinctPN | 裁定 |
|------|------|------|
| Victoria | 22 | 多实体污染（Queen Victoria/Victoria Island[已建]/Victoria Bay[已建]/Victoria balloon[tech]），剔 |
| No / America | 12 / 9 | 假匹配 / 泛指（North/South America 已建），剔 |
| Klock | 7 | 「Klock-Klock」（已建 klock-klock）子串，剔 |
| Niagara | 5 | niagara-falls/niagara-river（已建）裸名污染，剔 |
| Floridian / Algerian | 5 / 5 | demonym（stoplist），剔 |
| England / France | 221 / 169 | distinctPN 极高但城市页密集（伦敦/巴黎等），国级页价值待评估，暂缓 |
| Denmark / Turkey / Persia / Arabia | 18 / 17 / 16 / 8 | 中等候选，留后续 discover 续挖 |

## EXIT-GATE 检查

- G4：本轮无建页，无 add_page/edit_page 调用 ✓
- 词边界核验：10 新候选均以 `\bName\b` 全库扫描核 distinctPN（China 107/India 93/Russia 115/Scotland 43/Brazil 58/Peru 49/Sweden 42/Japan 36/Egypt 26/Ceylon 17）✓
- 接地诚信：geo-adjacency 表层扫 0 新如实记录；裸国名探测系补扫（非表层模式所及），已注明方法差异；demonym stoplist 滤 Floridian/Algerian；Victoria/Niagara/Klock 多义或既建变体剔除 ✓
- 交叉核既有页：10 新候选 label/slug 均不在 pages.json（仅 Iceland 既建，10 候选均无页）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R95→R96，SCN28 discover）

- current_round 95→96
- type_round 66→67
- rounds_since_last_evv5 0→1
- rounds_since_last_discover 重置为 0
- discover_streak_low 0（保持；new_candidates=10≥3，高产不累加）
- rounds_since_last_corpus_discover 31→32
- last_updated_round 95→96

## 遗留问题

- **R96 预测 = NEW1（优先级 6）**：R95 末 queue=12≥10（矩阵字面 queue≥10 且 since_discover=0 → 不触发 priority 3；since_evv5=1、streak=0、since_corpus=32）。矩阵落 **优先级 6 NEW1** 消化国级候选。**建议 R96 起连续 NEW1** 建国级页：优先高 distinctPN 者（China/Russia/India/Brazil/Peru/Scotland/Sweden/Japan…），每轮 ≤5。
- **国级页写法要求**：同洲级 Africa——须以「Verne 笔下之设定」聚焦确指句（如 China 聚焦 ASC 大铁路穿华段；Russia 聚焦 MS Michael Strogoff 信使穿越；India 聚焦 AWED 环游段），避免泛写地理。各页 ≥5 distinctPN，主源集中。
- **place 广度重估**：R89/R90 疑饱和 → R91 以区域/洲级否证 → R95 再以**国家级**否证。广度按「微地理→城市/地点→区域→国家→洲」层级递进，国级层至少 10+ 候选（+England/France 待评 + Denmark/Turkey/Persia/Arabia 等中候选）。place CLOSE 远未到；type_queue 下一型 event 顺延。
- **corpus-discover 顺延**：since_corpus=32≥30 未触发（被 priority 3 抢占）；R96 若走 NEW1，since_corpus 续涨，待 queue 再降 <10 且无高优先级时评估 3.5 深扫。
- **EVV5 下次约 R105**：R94 EVV5 已重置，since_evv5 R95 末=1。
- **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补，R96+ 附带。
- Egypt 主源待建页时复核（DSCF/TTLU/OC 分散，无单作 ≥10）；England/France 国级页价值待评估（城市页密集，避免重复覆盖）。
