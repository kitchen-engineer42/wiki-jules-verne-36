---
round: 28
date: 2026-07-15
type_round: 6
phase: "2.1"
current_type: technology
gene: CLOSE+SCN28
new_candidates: 6
pages: []
result: accept
---

# GROW 2.1-B · R28 · CLOSE+SCN28 · technology→place — 关闭 technology（final=20），place 首轮 discover

## 本轮公告

**R28 — Phase 2.1 — CLOSE+SCN28 — technology 关闭 → place 开启 — 0 建页 / +6 place 候选**

R27 后 discover_streak_low 达 3（type_close_streak 门），gate 2 触 **CLOSE+SCN28**。关闭 technology
（final_count=20），`current_type` 转 **place**（type_queue 弹出，余 [event, character]），同轮 SCN28
为 place **首轮 discover**，补种 6 个命名重要地点候选。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =6 | 否（未达 10，不抢先）|
| **2** | **CLOSE+SCN28（discover_streak_low ≥ 3）** | **=3** | **触发** |
| 3 | SCN28（queue/periodic）| — | （CLOSE 已含 SCN28）|
| 3.9 | zombie-guard | — | — |

## CLOSE — technology 关闭

| 项 | 值 |
|----|-----|
| closed_type | technology |
| closed_at_round | 28 |
| final_count（pages.json type==technology 计数）| **20** |
| evv6_score | null（待 Phase 2.1-Z-0 EVV6 回填）|

**final 20 页清单**：albatross / columbiad / diving-apparatus / **fulgurator** / giant-telescope /
**go-ahead** / granite-house-lift / gun-cotton / jangada / lunar-projectile / nautilus / nemo-electricity /
nitroglycerine / **oxyhydric-gas** / ruhmkorff-apparatus / ships-compass / the-forward / **the-sword** /
the-terror / victoria-balloon。（粗体 = GROW 2.1-B 新建 4 页：Pilot 16 + GROW 4。）

> technology 周期：R21 切入 → R22 建 Go-Ahead → R23 broadened 复扫 +3 → R24 建 3 → R25/R26/R27 三轮
> +0（streak 0→3）→ R28 CLOSE。GROW 净增 4 页（+25%）。debt：the tug（无专名，borderline）留 place 复议。

## SCN28 — place 首轮 discover（补种）

closed 后 current_type=place。首扫命名重要地点（distinctPN≥3，优先虚构/中心场景）。

> **⚠ R28 修正（首稿错误）**：首稿误将 **Granite House / Lincoln Island / Sneffels** 列为新候选，实为
> BIRTH Phase 9-C 既有 Pilot 页（`granite-house` / `lincoln-island` / `snaefellsjokull`，@86943ff）。place
> 已有 **15 页 Pilot**（baltimore / granite-house / great-eyrie / hong-kong / iceland / liedenbrock-sea /
> lincoln-island / mount-franklin / north-pole / reform-club / sargasso-sea / snaefellsjokull / stromboli /
> tampa-town / the-moon）。补种前须 diff 排除既有页——**同 technology R21 需排除 16 Pilot 页之教训**。已重扫
> 剔除 3 重复项，替换为下列 **12 真新候选**（全部经 pages.json 核验不在 15 既有页内）。

| distinctPN | 候选 | 源作 | 判定 | 处置 |
|-----|------|------|------|------|
| 56 | the Chimneys | MI | 虚构：殖民者初到的岩缝临时居所 | 新候选 → P1 |
| 45 | Prospect Heights | MI | 虚构：Granite House 所在高地平台 | 新候选 → P1 |
| 35 | Cape Bathurst | FC | Hudson's Bay 远征建 Fort Esperance 之角 | 新候选 → P1 |
| 29 | Tabor Island | MI | 虚构：Ayrton 流放岛 | 新候选 → P1 |
| 20 | Victoria Island | FC | 载 Fort Esperance 漂流的巨型冰岛（核心）| 新候选 → P1 |
| 20 | Fort Reliance | FC | Hudson's Bay 出发要塞 | 新候选 → P1 |
| 18 | Aberfoyle | UC | 苏格兰 Aberfoyle 煤矿区 | 新候选 → P1 |
| 15 | Quiquendone | DOSE | 虚构：佛兰德实验小镇 | 新候选 → P1 |
| 14 | Fort Providence | FC | Fur Country 远征沿途要塞 | 新候选 → P1 |
| 12 | New Aberfoyle | UC | 地下城 Coal City 所在新煤田 | 新候选 → P1 |
| 11 | Back Cup | FF | 虚构：Ker Karraje 海盗巢穴火山岛 | 新候选 → P1 |
| 7 | Crespo Island | 20KL | 虚构：Nautilus 海底森林猎场 | 新候选 → P1 |
| ~~65/60/4~~ | ~~Granite House / Lincoln Island / Sneffels~~ | MI / JCE | **既有 Pilot 页** | **剔除（不重建）** |
| 51 / 30 / 14 | Iceland / Baltimore / Tampa Town | JCE / FEM | 既有 Pilot 页（真实地理）| 不重建 |
| — | Stone's Hill / Pacific Railroad | FEM / 多作 | 已在 P2 队列 | place 轮消费 |
| — | reform-club | AWED | 既有 place 页（Pilot）| 不重建 |

| 结果 | 数值 |
|------|------|
| place 首轮 new_candidates（修正后，distinctPN≥3，均非既有页）| **12** |
| 首稿误列既有 Pilot 页（已剔除）| 3（Granite House / Lincoln Island / Sneffels）|
| discover_streak_low | **CLOSE 重置 0**（且 new_candidates 12 ≥ 3）|

> **place 首轮说明**：place 为 type-survey 第 2 权重（character > **place** > technology > …），候选池远大于
> technology。本轮仅首扫强候选补种，未穷尽——36 部合集地名（各航线/城市/岛屿/地质奇观）待后续 SCN28 深扫。
> Iceland/Baltimore/Tampa Town 均既有 Pilot 页，真实地理新候选门槛留 R30+ 深扫裁定。

## EXIT-GATE 检查（CLOSE+discover 轮仅 G4 + 状态机不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md place P1 +6 / technology 归档；grow_state CLOSE 六步 |
| I1 type_queue ∩ closed_types = ∅ | PASS | [event,character] ∩ [work,organization,technology] = ∅ |
| I2 current_type ∉ closed_types | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ grow_phase=="3" | PASS | False / "2.1" 一致 |

## state 更新（CLOSE 六步）

`current_round 28→29`；`current_type technology→place`；`type_queue [place,event,character]→[event,character]`；
`closed_types` append {technology, 28, 20, null}；`type_round` 重置 0；`rounds_since_last_evv5` 重置 0；
`discover_streak_low` 重置 0；`rounds_since_last_discover→0`（SCN28）；
`rounds_since_last_corpus_discover 26→27`；`last_updated_round→29`。

## 遗留问题

1. **R29 = place NEW1（≤5 页 standard 批）**：从修正后 12 真新候选建首批。建议先建 MI 同源虚构场景可互链：
   the Chimneys / Prospect Heights / Tabor Island（均 MI）+ FC 簇 Cape Bathurst / Victoria Island。
   ⚠ 严禁重建既有 Pilot 页（Lincoln Island / Granite House / Sneffels / Iceland / Baltimore / Tampa Town）。
   place-schema 专属字段：`book`、`real_or_fictional`、`region`。
2. **place discover 未穷尽**：R30+ SCN28 深扫 36 部合集地名（含真实地理门槛裁定 Iceland/Baltimore/Tampa）。
3. **the tug / Ebba borderline**：place 轮若建 Back Cup（含 lagoon）或 Ebba，回链复议 the tug 是否补建 technology。
4. **EVV5 临近**：since_evv5 重置 0，下次 EVV5 在 R38（+10）；place 周期中段会触。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
