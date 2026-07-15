---
round: 32
date: 2026-07-15
type_round: 4
phase: "2.1"
current_type: place
gene: SCN28-corpus
new_candidates: 15
pages: []
result: accept
---

# GROW 2.1-B · R32 · SCN28-corpus · place — 全集深扫补种（+15 候选，0 建页）

## 本轮公告

**R32 — Phase 2.1 — SCN28-corpus — place — discover 轮（0 建页 / +15 候选）**

`rounds_since_last_corpus_discover=30`（达 `corpus_discover_interval=30`），决策表优先级 3.5 抢先命中，
早于 zombie-guard（queue(place)=0）。执行 36 部合集**地名深扫**，按地理标记
（Island/Cape/Mount/Fort/Lake/Loch/River/Sea/Bay/Gulf/Strait/Point/Peninsula/Harbour…）
提取专名，distinctPN≥4 且排除既有 28 place 页后，得 15 强候选补种 queue P1 place。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=11, since_discover=3 | 否 |
| **3.5** | **SCN28-corpus（since_corpus ≥ 30）** | **=30** | **触发** |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=0 | （被 3.5 抢先）|
| NEW1（默认）| — | — | 否 |

## 扫描方法

`data/sentence_index/*.jsonl` 全量（36 部）。正则提取「大写词 + 地理标记」与「Cape/Mount/Fort/Lake/
Loch/Port/New + 大写词」两式专名，按 sid 前三段聚 distinctPN。排除：既有 28 place 页 label/别名 token；
人名误报（Ned Land 257 剔除）；裸标记词（Strait/Plateau/Desert/Ocean/River/Falls 单词剔除）。

## 补种候选（15，distinctPN 为扫描估值，建页前须实测校准）

| 候选 | 源作（VVV）| scan distinctPN | 类别 | 备注 |
|------|-----------|-----------------|------|------|
| Port Balloon | The Mysterious Island (MI/SI)| 43 | fictional | Lincoln Island 南岸良港 |
| Twofold Bay | In Search of the Castaways (SC)| 39 | real | 澳洲 NSW 真实海湾 |
| Lake Tchad | Five Weeks in a Balloon (FWB)| 32 | real | 非洲乍得湖 |
| Lake Grant | The Mysterious Island (MI/SI)| 28 | fictional | Lincoln Island 中央湖 |
| Flotsam Point | The Mysterious Island (MI/SI)| 26 | fictional | Lincoln Island 岬角 |
| Falls River | The Mysterious Island (MI/SI)| 25 | fictional | Lincoln Island 河流 |
| Serpentine Peninsula | The Mysterious Island (MI/SI)| 24 | fictional | Lincoln Island 蛇形半岛 |
| Union Bay | The Mysterious Island (MI/SI)| 22 | fictional | Lincoln Island 东岸海湾 |
| Snowy River | In Search of the Castaways (SC)| 20 | real | 澳洲斯诺伊河 |
| Shark Gulf | The Mysterious Island (MI/SI)| 18 | fictional | Lincoln Island 鲨鱼湾 |
| Lake Kirdall | The Master of the World (MW)| 15 | fictional | Great Eyrie 邻近湖（Robur）|
| Loch Katrine | In Search / Underground City (SC/UC)| 14 | real | 苏格兰卡特琳湖 |
| Flag Point | The Mysterious Island (MI/SI)| 14 | fictional | Lincoln Island 旗岬 |
| Christmas Harbour | An Antarctic Mystery (AM)| 13 | real | 凯尔盖朗岛克里斯马斯港 |
| Port Barnett | The Fur Country (FC)| 12 | fictional | Cape Bathurst 要塞港（接既有 FC 链）|

> **Lincoln Island 富矿**：MI/SI 合为 The Mysterious Island（SI 首句 "IT IS NOT THE DUNCAN" 系第三卷，
> Ayrton/Duncan 情节），岛屿地图专名密集（Port Balloon / Lake Grant / Falls River / Serpentine
> Peninsula / Union Bay / Shark Gulf / Flotsam Point / Flag Point 八处），承既有 lincoln-island /
> granite-house / mount-franklin / prospect-heights / the-chimneys 微地理链，NEW1 可成簇消费。

> **排除既有真实地理 Pilot 页**：Iceland / Baltimore / Tampa Town 已建，深扫已剔除（承 R28 教训）。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | N/A | discover 轮不建页 |
| G2 散文门 | N/A | 同上 |
| G3 schema | N/A | 同上 |
| G4 记录完整性 | PASS | 本日志；queue.md 补种 15 候选；grow_state discover 更新 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（SCN28-corpus discover）

`current_round 32→33`；`type_round 3→4`；`rounds_since_last_evv5 3→4`；
`rounds_since_last_discover 3→0`（discover 轮重置）；
`new_candidates=15 ≥ corpus_new_candidate_min=3` → `discover_streak_low` 保持 0、
`corpus_discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 30→0`（corpus 深扫重置）；`last_updated_round→33`。

## 遗留问题

1. **R33 = place NEW1（消费深扫候选）**：queue(place) 由 0 补至 15。R33 落 NEW1，优先建
   Lincoln Island 微地理簇（Port Balloon / Lake Grant / Falls River / Serpentine Peninsula / Union Bay），
   一批 5 页 standard 档。建页前逐一实测 distinctPN 校准（承 Stone's Hill/Coal City/Fort Providence 教训）。
2. **distinctPN 为扫描估值**：本表 15 候选 distinctPN 系正则聚合估值，含 MI/SI 跨卷合计；
   实际 standard 门槛为 ≥5 distinct-PN 引注，建页前 grep 校准，薄候选（如 Port Barnett 12 估值）实测优先。
3. **真实/虚构分类待建页确认**：Twofold Bay/Snowy River/Lake Tchad/Loch Katrine/Christmas Harbour 标 real，
   Lincoln Island 簇标 fictional，Lake Kirdall（MW）虚构美国湖——建页 frontmatter `real_or_fictional` 定稿。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传** 七项债务照旧 PARK/记录。
