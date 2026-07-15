---
round: 12
date: 2026-07-15
type_round: 3
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R12 · SCN28 · organization — 队列低水位 discover

## 本轮公告

**R12 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮）**

R11 NEW1 建 5 页后 queue_size=5 < discover_queue_threshold=10 → priority-3 SCN28 触发。
本轮做红链发现（label-aware），刷新候选队列。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=5 < 10 | **触发** |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =10 | 否 |
| 4/5 | RCH2 / NEW1+RCH2 | stub%=0 | 否 |

## SCN28 — discover

### 红链法（label-aware 未解析 wikilink 扫描）

**工具偏差**：`build_wanted_pages.py` 第 73 行将**含空格的 wikilink target 误判为"解析伪迹"过滤掉**，
只保留单词 target。故对 LAW §9 mandated 的 label 形式链接（`[[Jaspar Hobson]]` 等含空格）完全失明——
全库 1097 链接目标仅报 1 条红链（Kennedy）。改用 label-aware 扫描（比对 alias_index + slug + 页 id），
得真实未解析 target **12 条**。

**分类**：

| 类别 | 候选 | 计数 | 处置 |
|------|------|------|------|
| character | Jacques Paganel(×2)、Dr. Ferguson、Kennedy、Dr. Clawbonny、Jaspar Hobson、Paulina Barnett、J.T. Maston、Major Noltitz、Sir Francis Cromarty、Joam Garral | 10 | 入 queue P2，待 character 类型轮消费 |
| place | Stone's Hill | 1 | 入 queue P2，待 place 类型轮消费 |
| **organization（当前类型）净新增** | — | **0** | organization 语料在 R10 已穷尽（11 候选全部已建/在队/预存）|
| 数据问题（非候选）| Twenty Thousand Leagues Under the Seas | (6 链) | label 复数错配，见 housekeeping |

> 10 条 character + 1 place 多为 R11 organization 页的 member wikilink 指向（Hobson/Ferguson/Barnett/
> Clawbonny/Maston/Noltitz/Cromarty）及 Pilot 期既有红链（Paganel/Garral/Stone's Hill）。均语料充分、可建，
> 但**非当前 organization 类型**，故不计入 organization 的 new_candidates。

| 结果 | 数值 |
|------|------|
| label-aware 红链 target | 12 |
| 跨类型候选入队（character 10 + place 1）| 11 |
| **organization new_candidates** | **0** |
| discover_streak_low | 0 → 1（0 < type_close_new_candidate_min=3，累加）|

> **队列效应**：queue P2 增 11 条 → queue_size = 5(org) + 11 = 16 ≥ 10。R13 预检：queue_size≥10 且
> queue(organization)=5≠0 且 streak=1<3 → **priority-6 NEW1**，续建剩余 5 org 候选
> （Cambridge Observatory / St Louis Fur / Royal Society / Royal Institution / East India Company）。
> organization 建满 10 页（R11+R13）后 queue(org)=0 触发 `queue(current_type)==0` 强制 SCN28，
> streak 累至 3 关闭 organization；跨类型候选留存供 character/place 类型轮回补。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志产出；queue.md P2 入 11 跨类型候选；grow_state step-six→R13（type_round 2→3，since_evv5 2→3，since_discover→0，discover_streak_low 0→1，since_corpus 10→11）|

> discover 轮不建页，G1/G2/G3/G5 不适用。

## state 更新

`current_round 12→13`，`type_round 2→3`，`rounds_since_last_evv5 2→3`，
`rounds_since_last_discover→0`，`discover_streak_low 0→1`，
`rounds_since_last_corpus_discover 10→11`。`current_type` 仍 organization，`last_updated_round→13`。

## 遗留问题

1. **R13 = organization NEW1 续建**：取 queue P1 剩 5 org 候选建 standard 档。
   Royal Society 与已建 royal-geographical-society 语料重叠（FWB 混用 "Royal Society"），建页时内容/label 消歧。
   Cambridge Observatory borderline place/org，按咨询机构功能定 organization（R10 已议）。
2. **build_wanted_pages 空格误滤缺陷**：含空格 target 被当伪迹过滤，红链发现对 label 形式链接失明。
   已记 housekeeping（HK-wanted-pages-space-filter）。修复前红链发现须用 label-aware 扫描。
3. **`[[Twenty Thousand Leagues Under the Seas]]` label 错配**：6 页链复数 "Seas"，work 页 label 为单数
   "Twenty Thousand Leagues Under the Sea"。加 alias 或改链修复，已记 housekeeping。Pilot 既有，非本轮引入。
4. **跨类型候选留队**：11 条 character/place 候选（P2）待各自类型轮消费；character 为 type_queue 末位。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、discover 漏判既有页
   五项债务照旧 PARK/记录。
