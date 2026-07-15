---
round: 36
date: 2026-07-15
type_round: 8
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 26
pages: []
result: discover
---

# GROW 2.1-B · R36 · SCN28 · place — 表层复扫重开候选池（+26，0 建页）

## 本轮公告

**R36 — Phase 2.1 — SCN28 — place — discover 轮 / 0 建页 / new_candidates=26**

R35 消费深扫末批后 queue(place)=0。R36 zombie-guard（queue==0）与 SCN28（queue_size<10）双双命中，
落 discover 轮。执行**全 36 部地理标记词全量表层扫描**，得 distinctPN≥5 候选 96 个，
按源作 grep 拆分校准后**精选 26 个入队**。

> **关键发现**：place **远未穷尽**。R32 SCN28-corpus「深扫」实仅覆盖窄簇（Lincoln Island 微地理 +
> 少量真实地理），本轮以完整地理标记正则 `(Cape|Lake|Mount|Fort|Port|Loch|Gulf|Isle)+Name` 及
> `Name+(Island|Bay|River|Sea|Point|Peninsula|Harbour|Strait|Falls|Creek)` 全量扫，暴露大量遗漏，
> 含 **Fort Hope（FC:66）**、**Tsalal Island（AM:61）**、**Claw Cape/Red Creek（MI，林肯岛簇补漏）**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =7 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）**| **queue_size=0<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =3 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| =0（亦命中，动作同 SCN28）| — |
| NEW1（默认）| — | — | 否 |

## 扫描方法

1. **标记词全量正则**：前置标记 `Cape/Lake/Mount/Fort/Port/Loch/Gulf/Isle/River` + 专名，
   及专名 + 后置标记 `Island(s)/Bay/River/Sea/Point/Peninsula/Harbour/Strait/Falls/Creek/Volcano/Mountains/Rock(s)`。
2. **全 `data/sentence_index/*.jsonl` 扫描**，按段级 PN（sid 前三段）计 distinctPN。
3. **排除 42 既有 place**（label + slug + aliases 归一化），及子串重叠既有页。
4. **源作拆分校准**（承 R30/R34 铁律）：对 Top 候选逐一按 VVV 文件 grep，取主源 distinctPN，
   剔除跨源聚合误报（如 Flag Point 聚合 14，实测 GM 仅 4，续弃）。

## 入队候选（26，建前二次实测校准）

| 候选 | 源作(VVV) | 主源 distinctPN | 预判 real/fictional | 簇/链 |
|------|-----------|-----------------|---------------------|-------|
| Fort Hope | FC | 66 | fictional | FC 漂流殖民地中心（重大补漏）|
| Tsalal Island | AM | 61 | fictional | Poe 之谜岛 |
| Gourbi Island | OC | 41 | fictional | Off on a Comet |
| Phina Island | GM | 40 | fictional | Godfrey Morgan 荒岛 |
| Claw Cape | MI | 32 | fictional | 林肯岛簇补漏 |
| Red Sea | TTLU | 28 | real | Nautilus 航线 |
| Lake Erie | MW | 27 | real | 真实地理 |
| Cape Michael | FC | 25 | fictional | port-barnett 邻岬 |
| Red Creek | MI | 24 | fictional | 林肯岛簇补漏 |
| Cape Esquimaux | FC | 23 | fictional | FC 漂流半岛 |
| Behring Strait | FC | 22 | real | FC 北极 |
| Fort Providence | ACH | 22 | real | Hatteras 越冬堡（R30 误降级勘误）|
| Beechey Island | ACH | 20 | real | Hatteras 北极 |
| Spencer Island | GM | 18 | fictional | Godfrey Morgan |
| Gulf Stream | TTLU | 18 | real | Nautilus 航线 |
| Torres Strait | TTLU | 15 | real | Nautilus 航线 |
| Polar Sea | FC | 14 | real | FC 北极 |
| Loch Malcolm | UC | 13 | fictional | New Aberfoyle 地下湖 |
| Lake Baikal | MS | 12 | real | Michael Strogoff |
| Gallian Sea | OC | 12 | fictional | 彗星 Gallia |
| Bear Lake | FC | 11 | real | FC 北极 |
| Cape Bernouilli | SC | 10 | real | 澳洲 37 度线起点（接 twofold-bay）|
| Cape Horn | TTLU/SC | 9（主源）| real | 跨作 |
| Melville Island | ACH | 9 | real | Hatteras（borderline）|
| Rocky Mountains | RM | 9（主源）| real | 跨作 |

> **勘误 1**：Fort Providence — R30 记「语料仅 3 处直接命名」判薄降级，系**源作误判**：
> 实测主源为 **ACH（Adventures of Captain Hatteras）22 distinctPN**（Hatteras 越冬堡），FC 仅 3。
> 本轮恢复入队，标 real。记 HK：候选降级前须先确定主源作再计数。
>
> **勘误 2**：Flag Point 续弃——聚合仍报 14，实测 GM 仅 4 distinctPN（R34 已弃），不入队。

## EXIT-GATE 检查（discover 轮）

| 门 | 结果 | 说明 |
|----|------|------|
| G4 记录完整性 | PASS | 本日志；queue.md 追加 26 候选 + 双勘误注；grow_state discover six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（SCN28 discover six-step）

`current_round 36→37`；`type_round 7→8`；`rounds_since_last_evv5 7→8`；
`rounds_since_last_discover 3→0`（discover 命中重置）；
`discover_streak_low` 保持 0（new_candidates=26 ≫ 3，高产非低产）；
`rounds_since_last_corpus_discover 3→4`（表层 SCN28 非 corpus 深扫，corpus 计数不重置）；
`last_updated_round→37`。

## 遗留问题

1. **CLOSE 展望大幅推迟**：本轮暴露 place 未穷尽，26 新候选入队。原「R36 起低产 streak→CLOSE」预期
   作废。按 NEW1 每轮 ≤5，26 候选约需 R37–R42 六轮消费；期间 EVV5（R38 到期）穿插。place 深度扩张延续。
2. **EVV5 R38 到期**：since_evv5=8，R38 达 10 → EVV5 place 质量评估（样本 42 页，充足）。
   EVV5 为质量轮不建页、不消费队列。
3. **建前二次校准铁律**：26 候选主源 distinctPN 为本轮 grep 值，NEW1 建页前仍须逐页复核 PN 句可引性
   （承 R33/R34：聚合估值 vs 实测偶有偏差，如 Lake Kirdall 15→10）。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报（本轮再证）** 八项债务照旧 PARK/记录。
