---
round: 68
date: 2026-07-15
type_round: 39
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 15
pages: []
result: discover
---

# GROW 2.1-B · R68 · SCN28 · place — 表层复扫补种（15 候选，非建页）

## 本轮公告

**R68 — Phase 2.1 — SCN28 — place — 0 建页 / 表层复扫 discover / 补种 15 候选 / queue 9→24**

R67 后 since_evv5=6、since_discover=8、discover_streak_low=0、queue(place)=9、since_corpus=4。
决策矩阵：since_evv5=6<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
**queue=9<10 → 优先级 3 SCN28 触发**（抢占 NEW1），since_corpus=4<30 → 非 corpus 型。
本轮为表层复扫 discover：补种 place 候选入 queue，不建任何页；since_discover 归 0。
补种 15 强候选（城市/地点，各精核词边界 distinctPN ≥5、非既有页/人物）：
Irkutsk / Omsk / Tomsk / Kazounde / Iquitos / Manaos / Pekin / Zanzibar / San Francisco /
London / Stockholm / Christiania / Bergen / Buffalo / Mounts Doerfel。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=6 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =4 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=9 | 否 |
| RCH2（stub% ≥ 20%）| —（未评估，SCN28 先占）| 否 |
| NEW1（默认）| —（被优先级 3 抢占）| 否 |

## 复扫方法与候选核验

三趟表层复扫 `data/sentence_index/*.jsonl`，逐候选精核**词边界** distinctPN（段级 PN =
sid 前三段），排除既有页 label/alias/id 与人物名。仅保留单作 distinctPN ≥5 的真地点。

| 候选 | 单作 distinctPN（top） | region / real | 排除污染核验 |
|------|----------------------|---------------|--------------|
| Irkutsk | MS:203 / WC:4 | 东西伯利亚 / real | 词边界，纯地名 |
| Omsk | MS:77 | 西西伯利亚 / real | 词边界，纯地名 |
| Tomsk | MS:70 | 西西伯利亚 / real | 词边界，纯地名 |
| Kazounde | DSCF:97 | Angola 内陆 / real | 专名，无同形词 |
| Iquitos | EHLA:83 | 秘鲁亚马逊上游 / real | 专名 |
| Manaos | EHLA:80 | 巴西内格罗河口 / real | 专名（alias Manaus 待核）|
| Pekin | ASC:88 | 清帝国京城 / real | 词边界（alias Peking 待核）|
| Zanzibar | FWB:27 / DSCF:18 / TT:14 | 东非 / real | 专名 |
| San Francisco | GM:27 / AWED:27 / DSCF:14 / RM:12 | 加州 / real | 双词专名 |
| London | AWED:62 / FWB:28 / SC:8 | 英格兰 / real | 词边界 |
| Stockholm | WC:57 | 瑞典 / real | 专名 |
| Christiania | TN:62 / FC:3 | 挪威（今 Oslo）/ real | 专名（alias Oslo 待核）|
| Bergen | TN:43 / WC:18 | 挪威西岸 / real | 词边界 |
| Buffalo | MW:13 | 纽约州 Erie 湖 / real | **已核为城非动物**（MW-014 Lake Erie 段）|
| Mounts Doerfel | RM:5 | 月面南极 / real | 专名，distinctPN=5 恰达门 |

> **Buffalo 反污染复核**：`\bBuffalo\b` 在 MW 命中 13，逐句核 MW-014-003/004/007/013 均指
> Erie 湖东北端港城（"toward the northeast end of the lake, and hence toward Buffalo"），
> 非 bison 动物，判 real 城建。
> **noise/碎片剔除**（不入 queue）：Granite/Fort/Lincoln/Will/Back/Cape/Mount/Lake 等孤词，
> Bank of England（机构非地理），Victoria（人物/多义），Amazones（河流别名待核），
> Klock（人名疑），以及既有页/别名 dupe（Arctic Ocean→polar-sea、Isle of Paques→easter-island、
> The Torres Strait→torres-strait、Isle Tabor→tabor-island、Hong→hong-kong）。

## PN 接地核验

本轮不建页，无正文 PN 落地。候选 distinctPN 仅为 queue 强度参考，来自 `data/sentence_index/`
词边界精核；建页轮（R69+）消费时须再逐句复核页内引注 ≥5。

## EXIT-GATE 检查（discover 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 补种 15 候选（9→24）；grow_state SCN28 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 discover six-step）

`current_round 68→69`；`type_round 39→40`；`rounds_since_last_evv5 6→7`；
`rounds_since_last_discover 8→0`（discover 轮，RESET）；
`discover_streak_low` 保持 0（new_candidates=15≥3，不自增）；
`rounds_since_last_corpus_discover 4→5`；`last_updated_round→69`。

## 遗留问题

1. **queue(place) 9→24**：补种 15 强候选后 discover 门解除；R69 起 since_discover=0，
   优先级 3 不再触发，回落 NEW1 建页。
2. **下轮 R69：queue=24≥10、since_evv5=7<10、since_discover=0<10、since_corpus=5<30 → NEW1**。
   建 5 新页（standard 档），消费 queue 头部候选（优先单作强候选 Irkutsk/Kazounde/Iquitos/
   Stockholm/Zanzibar 或跨源 North Sea 等）。
3. **alias 待核（建页时定）**：Manaos↔Manaus、Pekin↔Peking/Beijing、Christiania↔Oslo。
   Verne 原文用旧称（Pekin/Christiania/Manaos），建页 label 从原文，现代名收 alias。
4. **Kazounde region**：DSCF 内非洲奴隶市场镇，real（Verne 依 real Angola 内陆设定），建页 region Angola。
5. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）；Kara Sea 建前须精扫。
6. **跨源候选照旧**：North Sea/Firth of Clyde/Long Island/Goat Island/Bay of Bengal/Cape Bon。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
8. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
