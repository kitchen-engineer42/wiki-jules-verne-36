---
round: 15
date: 2026-07-15
type_round: 6
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 2
pages: []
result: accept
---

# GROW 2.1-B · R15 · SCN28 · organization — org-suffix 语料复扫（发现 2 漏判候选）

## 本轮公告

**R15 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮）**

R14 后 queue(organization)=0，zombie-guard 再触 SCN28。本轮不重复 R14 的红链扫描（结果不会变），
改做 **org-suffix 语料复扫**（Company/Society/Club/Institution/Association/Expedition… 专名模式）
以彻底验证 organization 是否真穷尽 —— 结果发现 **2 个此前漏判的候选**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=12, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =13 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(organization)=0 | **触发 SCN28** |

## SCN28 — discover（org-suffix 语料复扫）

### 方法

对 `data/sentence_index/*.jsonl` 全库扫描 org 后缀专名（`… (Company|Society|Club|Institution|
Institute|Association|Expedition|Corporation|League|Academy)`），统计 count≥3 的专名，
与已建 organization 页 label/alias 比对，筛未建者。此法覆盖**未被 wikilink** 的组织专名，
补 R10 corpus discover 与 R12/R14 红链扫描（只看 wikilink target）的盲区。

### 结果

| count | 专名 | 状态 | 处置 |
|-------|------|------|------|
| 186 | Gun Club | 已建 | — |
| 66 | Weldon Institute | 已建 | — |
| 33 | (Hudson's) Bay Company | 已建 | — |
| 25 | Reform Club | 已存在（place 页）| HK-reform-club-place-vs-org，不重建 |
| 23/14 | (Royal) Geographical Society | 已建 | — |
| 13 | North Polar Practical Association | 已建 | — |
| 7/7 | Royal Society / Royal Institution | 已建（R13）| — |
| 6/4 | Oriental / Peninsular Company | 已建（P&O）| — |
| 4/4/4 | St Louis Fur / East India / Grand Transasiatic | 已建 | — |
| **5** | **Canadian General Transportation Company** | **未建** | **新候选 → queue P1** |
| **3** | **North-West Company** | **未建** | **新候选 → queue P1** |
| 4 | "Academy" | 泛词误报 | 弃 |

**两个漏判候选**（均 distinctPN≥3，达建页门；R10 corpus discover 漏因二者在语料中**从未被
wikilink**，红链扫描（R12/R14）自然看不到，而 R10 corpus 扫描的专名过滤也未命中）：

1. **Canadian General Transportation Company**（WC《The Waif of the Cynthia》，distinctPN≈5）：
   Cynthia 号的加拿大船东公司（WC-006-042），ex-director Joshua Churchill（WC-008-003），
   保险诉讼、旧船员档案构成 Erik 寻亲主线的关键机构。全名首现为 "Canadian General
   Transportation Company"，后文简称 "Canadian Transportation Company"。
2. **North-West Company**（FC《The Fur Country》，distinctPN=4）：1784 年蒙特利尔商人创立的
   皮货公司（FC-002-020），Hudson's Bay 的宿敌，1821 年被后者吸收（FC-002-022）。此前仅作为
   hudsons-bay-company / st-louis-fur-company 页内历史背景出现，无独立页。

| 结果 | 数值 |
|------|------|
| org-suffix 专名（count≥3）| 17 |
| 已建/已存在 | 15 |
| **organization new_candidates（漏判补捞）** | **2** |
| discover_streak_low | **保持 2（判断性处置，见下）** |

### discover_streak_low 处置说明（判断性偏差，待用户复审）

严格机械规则（grow-state-machine.md §4.6 步六）：`new_candidates(2) < type_close_new_candidate_min(3)`
→ streak +1（2→3）。若照此，R16 将命中 CLOSE+SCN28（streak≥3），**关闭 organization 并遗弃
这 2 个 queue 中可建的、语料充分的候选**。

本轮**不增 streak，保持 2**，理由：`discover_streak_low` 语义为「连续 discover 低产→候选池枯竭」
（§spec 行75「候选枯竭信号」）。R15 恰恰**证否了枯竭**——补捞出 2 个达门候选，候选池被回填。
将其计为「低产枯竭轮」会误报池状态，并使 R16 遗弃与本会话已建的 st-louis-fur-company（同 distinctPN≈4）
同档的 grounded 候选，违背 Phase 2 广度**全覆盖**目标。

> **偏差标记 GROW-JUDGMENT-R15**：streak 机械值应为 3，本轮判断性保持 2 以先建后闭。
> 与既有 PARK 债务一并交用户批量复审。若用户判定应严格遵循机械规则，则回退为 streak=3 并于
> R16 CLOSE，2 候选留 queue 作已记录 straggler。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志产出；queue.md P1 新增 2 org 候选；grow_state step-six→R16（type_round 5→6，since_evv5 5→6，since_discover→0，streak 保持 2[判断性]，since_corpus 13→14）|

> discover 轮不建页，G1/G2/G3/G5 不适用。

## state 更新

`current_round 15→16`，`type_round 5→6`，`rounds_since_last_evv5 5→6`，
`rounds_since_last_discover→0`，`discover_streak_low` **保持 2**（GROW-JUDGMENT-R15），
`rounds_since_last_corpus_discover 13→14`。`current_type` 仍 organization，`last_updated_round→16`。

## 遗留问题

1. **R16 = organization NEW1 建 2 页**：queue(org)=2（Canadian General Transportation Company /
   North-West Company），streak 2<3 → priority-6 NEW1。建 standard 档，PN-grounded。
2. **R17 = organization SCN28（zombie）**：R16 建满后 queue(org)=0，再 discover。org-suffix 已复扫尽，
   预期 new_candidates=0 → streak 2→3。R18 CLOSE+SCN28 关闭 organization（final_count=12）。
3. **org 漏判根因**：R10 corpus discover 与红链扫描均未捕获**无 wikilink** 的组织专名。已存
   HK-discover-existing-type-blindspot（既有页漏判）；本轮暴露的是**未建且无链**组织漏判，
   补记 housekeeping（HK-corpus-discover-orgname-blindspot）。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤
   五项债务照旧 PARK/记录。
