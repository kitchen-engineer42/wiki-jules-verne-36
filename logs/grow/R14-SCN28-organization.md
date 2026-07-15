---
round: 14
date: 2026-07-15
type_round: 5
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R14 · SCN28 · organization — zombie-guard 强制 discover

## 本轮公告

**R14 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮）**

R13 建满 5 页后 queue(organization)=0，决策矩阵 `queue(current_type)==0` zombie-guard 强制 SCN28。
本轮做 label-aware 红链发现，确认 organization 语料候选是否真已穷尽。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =1 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=12, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =12 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(organization)=0 | **触发 SCN28** |

## SCN28 — discover

### 红链法（label-aware 未解析 wikilink 扫描）

`build_wanted_pages.py` 空格误滤缺陷仍在（HK-wanted-pages-space-filter，PARK），继续用 label-aware
扫描（比对 alias_index label/alias + slugify + 页 id）。全库扫描得 13 条 distinct 未解析 target：

| 类别 | 候选 | 计数 | 处置 |
|------|------|------|------|
| character（已在 queue P2）| Jacques Paganel、Dr. Ferguson、Kennedy、Dr. Clawbonny、Jaspar Hobson、Paulina Barnett、J.T. Maston、Major Noltitz、Sir Francis Cromarty、Joam Garral | 10 | R12 已入队，不重复计 |
| **character（本轮新增）**| **James Starr** | **1** | R13 royal-institution 页 member wikilink 引入；入 queue P2 |
| place（已在 queue P2）| Stone's Hill | 1 | R12 已入队 |
| **organization（当前类型）净新增** | — | **0** | organization 语料 R10 corpus + R12 红链均判穷尽，本轮复核仍 0 |
| 数据问题（非候选）| Twenty Thousand Leagues Under the Seas | (6 链) | label 复数错配，HK-20kleagues-seas-alias |

> 本轮唯一新 target 是 **James Starr**（UC 矿工程师），由 R13 `royal-institution` 页的
> `[[James Starr]]` member wikilink 引入 —— 属 organization 建页外溢的 character 候选，非 organization 本类。

| 结果 | 数值 |
|------|------|
| label-aware 红链 target（distinct）| 13 |
| 跨类型候选新入队（character: James Starr）| 1 |
| **organization new_candidates** | **0** |
| discover_streak_low | 1 → 2（0 < type_close_new_candidate_min=3，累加）|

> **关闭轨迹**：organization new_candidates 连续 R12(0)→R14(0) 为 0，streak 1→2。R15 queue(org) 仍 0
> → zombie-guard 再触 SCN28，预期 new_candidates=0 → streak 2→3。R16 streak≥3 → CLOSE+SCN28
> 关闭 organization（final_count=10），current_type 转 technology（type_queue 首位）。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志产出；queue.md P2 新增 James Starr；grow_state step-six→R15（type_round 4→5，since_evv5 4→5，since_discover→0，discover_streak_low 1→2，since_corpus 12→13）|

> discover 轮不建页，G1/G2/G3/G5 不适用。

## state 更新

`current_round 14→15`，`type_round 4→5`，`rounds_since_last_evv5 4→5`，
`rounds_since_last_discover→0`，`discover_streak_low 1→2`，
`rounds_since_last_corpus_discover 12→13`。`current_type` 仍 organization，`last_updated_round→15`。

## 遗留问题

1. **R15 = organization SCN28（zombie-guard 续）**：queue(org) 仍 0，预期再 discover、new_candidates=0
   → streak 2→3。若 R15 corpus 复扫仍 0 org 候选，organization 关闭进入倒计时。
2. **R16 = CLOSE+SCN28 关闭 organization**：streak 达 3 → 关闭，final_count=10，转 technology。
3. **跨类型候选留队**：queue P2 现 12 条（11 R12 + James Starr）待 character/place 类型轮消费。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 漏判既有页 六项债务照旧 PARK/记录。
