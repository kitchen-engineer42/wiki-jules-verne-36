---
round: 54
date: 2026-07-15
type_round: 26
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 9
pages: []
result: discover
---

# GROW 2.1-B · R54 · SCN28 · place — 表层复扫补种（queue<10 触发，自 R48 以来首次 discover）

## 本轮公告

**R54 — Phase 2.1 — SCN28 — place — discover / 0 建页 / +9 候选 / queue 7→16**

R53 后 since_evv5=3、since_discover=5、queue(place)=7，**queue_size 7 < 10** 命中决策矩阵优先级 3（SCN28）。
自 R48 以来首次 discover 轮。全 36 部作品 `(Cape|Lake|Mount|Fort|Port|Loch|Gulf|Isle|Bay of|Sea of)+Name`
及 `Name+(Island|Bay|River|Sea|Strait|...)` 全标记扫描，按源作拆分 distinctPN（排除跨源聚合误报）。
过滤 106 既有 place + 在队候选 + 变体后，得 **9 枚新候选（≫ type_close_new_candidate_min=3）**——证 place 表层仍未穷尽。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=3 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=7 < 10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =21 | （未评估）|
| 3.9 | zombie-guard | queue=7 | （未评估）|
| NEW1（默认）| — | — | （未评估）|

## 新候选（9 枚，主源单源严扫 distinctPN）

| slug 拟名 | 主源 | distinctPN | real/fictional | 说明 |
|-----------|------|-----------|----------------|------|
| Bay of Vigo (→vigo-bay) | TTLU | 9 | real | 维哥湾（西班牙），Nautilus 打捞沉船金；专章「The Bay of Vigo」|
| Ham Rock | SC2 | 9 | fictional | 木筏漂流者所命名之礁岛，Curtis 船长命名（《Chancellor》）|
| Gueboroa Island | TTLU | 8 | real | Torres 海峡搁浅之岛（Papua），Nautilus 触礁 |
| Sea of Clouds | RM | 8 | real/lunar | 月海 Mare Nubium（《Round the Moon》）|
| Sea of Rains | RM | 7 | real/lunar | 月海 Mare Imbrium |
| Port Gräuben | JCE | 7 | fictional | 地心之海内海滩，Liedenbrock 命名 |
| Island of Ljakow | WC | 6 | real | Liakhov 岛（西伯利亚北极），Nordenskiold 航线 |
| Island of Sein | WC | 5 | real | Île de Sein（布列塔尼），Cynthia 失事海域近旁 |
| Icy Cape | FC | 5 | real | 冰角（阿拉斯加），接 victoria-island 漂流簇 |

## 排除的变体/误报

| 扫描命中 | 处置 | 理由 |
|----------|------|------|
| Behring's Strait(s) | 排除 | 既有 behring-strait 变体 |
| The Torres Strait | 排除 | 既有 torres-strait 变体 |
| Isle Tabor | 排除 | 既有 tabor-island 变体 |
| Lake Tanganyika | 排除 | 既有 lake-tanganyika（R47 建）|
| Port Gr（截断）| 修正为 Port Gräuben | 正则截断非 ASCII 字符 ä，实名 Port Gräuben |

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md +9 候选（7→16）；grow_state discover six-step；本轮无建页故无 G1/G2/G3 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（SCN28 discover six-step）

`current_round 54→55`；`type_round 25→26`；`rounds_since_last_evv5 3→4`；
`rounds_since_last_discover RESET 5→0`（discover 轮）；`discover_streak_low` 保持 0（new_candidates=9 ≥ 3）；
`rounds_since_last_corpus_discover 21→22`；`last_updated_round→55`。

## 遗留问题

1. **本轮 discover，无建页**：place 页数维持 106，registry 1175。
2. **queue(place) 16**：7 + 9 新候选 = 16，重回 SCN28 阈值以上。**下轮 R55：since_discover 归 0、queue=16≥10 → 高优先门全否 → NEW1**，续消费本批强候选（Bay of Vigo TTLU:9 / Ham Rock SC2:9 / Gueboroa TTLU:8 等）。
3. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
4. **SCN28-corpus 深扫倒计时**：since_corpus=22，距阈值 30 尚 8 轮（~R62）。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
