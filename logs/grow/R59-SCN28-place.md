---
round: 59
date: 2026-07-15
type_round: 31
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 19
pages: []
result: discover
---

# GROW 2.1-B · R59 · SCN28 · place — 广式重扫推翻 R57 穷尽结论，19 新候选，关闭倒计时撤销

## 本轮公告

**R59 — Phase 2.1 — SCN28 — place — discover / 0 建页 / new_candidates=19 / streak 1→0（撤销关闭倒计时）**

R58 后 since_evv5=8、since_discover=1、discover_streak_low=1、queue(place)=2（仅 holds）。queue_size 2 < 10 命中优先级 3（SCN28）。
本轮改用**宽式 toponym pattern** 重扫全 36 部，**推翻 R57「standard 表层已穷尽」结论**——
得 ≥5 单源新候选 **19 枚**。`discover_streak_low 1→0`，**place 关闭倒计时撤销**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=8 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =1 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=2 < 10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =26 | （未评估）|
| NEW1（默认）| — | — | （未评估）|

## R57 误判根因（discover 双盲区，量化）

R57 记「≥5 单源 0 枚，表层穷尽」为**系统性漏计**，根因两类：

1. **单复数/大小写变体漏匹配**：`Smith's Strait`（单数，ACH-013-034/036）被 `Smith's Straits`（复数）主式漏掉 → R57 记 [4]，实为 ACH:7 distinctPN。`bay of Talcahuano`（小写）+ 裸 `Talcahuano` 被 `Bay of Talcahuano` 主式漏掉 → R57 记 [3]，实为 SC:13。
2. **构式盲区**：`GEO of X`（Strait of Gibraltar / Cape of Good Hope / Gulf of Mexico）与 `X Ocean`（Indian / Pacific / Atlantic Ocean）整类未进 R57 扫描 pattern，零命中。

改用 `(?:[A-Z]\w+ ){1,2}(Sea|Strait|Bay|Cape|Island|Mountains|Lake|Gulf|River|Ocean|…) | GEO of [A-Z]\w+` 宽式重扫，排除 120 既有 place + 变体后，得 19 枚 ≥5 单源。

## 扫描结果（新候选，主源单源 distinctPN 严扫）

| 候选 | 主源 | distinctPN | 备注 |
|------|------|-----------|------|
| Bay of Talcahuano | SC | 13 | 智利湾，Duncan 补给港/南美搜索起点 ⭐R57误分[3] |
| Indian Ocean | SC | 13 | 印度洋 |
| Isle of Paques | DSCF | 10 | 复活节岛（label Easter Island）|
| Pacific Ocean | SC | 9 | 太平洋 |
| Cape of Good Hope | TTLU | 8 | 好望角 |
| Antarctic Sea | AM | 7 | 南极海 |
| Smith's Straits | ACH | 7 | Kane 1853 航路 ⭐R57误分[4] |
| Strait of Gibraltar | TTLU | 7 | 直布罗陀海峡 |
| Washburn Bay | FC | 7 | FC 北极湾 |
| Chatham Islands | RC | 7 | Robur 抛锚/Pitt Island |
| Gulf of Mexico | TTLU | 6 | 墨西哥湾 |
| Detroit River | MW | 6 | ⭐R51误 hold |
| Sandwich Islands | AM | 6 | 夏威夷旧称 |
| Coronation Gulf | FC | 5 | 北极湾 |
| Platte River | AWED | 5 | |
| Atlantic Ocean | SC | 5 | 大西洋 |
| Caribbean Sea | TTLU | 5 | |
| Blue Ridge Mountains | MW | 5 | Great Eyrie 区 ⭐R51误 hold |
| Shannon Island | WAI | 5 | A Winter Amid the Ice 北极岛 |

**排除项（非新建）**：Arctic Ocean FC:42 → 并入 polar-sea 别名（同一北冰洋，Verne 互用 Polar Sea/Arctic Ocean）；
Long's Peak FEM:8/RM:7 → rocky-mountains 子地点，overlap，hold；Black Rock MW → 待与 black-rock-creek 消歧；
Behring's Straits(WC)/The Torres Strait(TTLU) → 既有 behring-strait/torres-strait 变体。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 记 R59 广式重扫 + 19 候选 + R57 修正说明；grow_state discover six-step；本轮无建页故无 G1/G2/G3 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（SCN28 discover six-step）

`current_round 59→60`；`type_round 30→31`；`rounds_since_last_evv5 8→9`；
`rounds_since_last_discover RESET 1→0`（discover 轮）；`discover_streak_low RESET 1→0`（new_candidates=19 ≥ 3）；
`rounds_since_last_corpus_discover 26→27`；`last_updated_round→60`。

## 遗留问题

1. **本轮 discover，无建页**：place 页数维持 120，registry 1189。
2. **queue(place) 21**：2 holds + 19 新候选。真候选池充盈，place 远未穷尽。
3. **place 关闭路径撤销**：R57/R58 关闭倒计时基于误判，本轮 streak 归 0 撤销。后续 NEW1 分批消费 19 候选：
   拟 R60 起每轮 NEW1 消费 5，约 4 轮清空（R60–R63）；期间 since_corpus 达 30（~R62）或触发 SCN28-corpus 深扫。
4. **discover 双盲区债务升格**：此前 PARK 的「discover 双盲区」经本轮证实致 R57 false-exhaustion + R58 关闭倒计时误启动——
   **实质缺陷，非纯记录**。已记 housekeeping，build 完成后提 RFC（宽式 discover pattern：覆盖单复数变体 + GEO-of-X + X-Ocean 构式）。承 PARK-until-build-done 原则不自主 file。
5. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
6. **SCN28-corpus 深扫倒计时**：since_corpus=27，距阈值 30 尚 3 轮（~R62）；深扫或自 3–4 富矿带再升格若干跨源 place。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
8. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录（discover 双盲区已升格见 #4）。
