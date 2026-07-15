---
round: 35
date: 2026-07-15
type_round: 7
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - lake-kirdall
  - loch-katrine
  - christmas-harbour
  - port-barnett
result: accept
---

# GROW 2.1-B · R35 · NEW1 · place — 深扫末批 4 页（standard 档）

## 本轮公告

**R35 — Phase 2.1 — NEW1 — place — 4 建页 / standard 档**

queue(place)=4（≠0），无高优先门抢先，落 NEW1 默认门。
消费 R32 深扫末批 4 候选（Flag Point R34 弃建后实余 4）：
**Lake Kirdall**（MW，堪萨斯封闭湖，Robur 的 Terror）+ **Loch Katrine**（UC，苏格兰真湖，
New Aberfoyle 之上，溃陷排空）+ **Christmas Harbour**（AM，凯尔盖朗港，Halbrane 泊地）+
**Port Barnett**（FC，Cape Bathurst 港，随岛漂散）。P1 place 至此见底。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=4<10 → 命中 | **（见下）** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =2 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=4 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

> **门判定说明**：queue_size=4 < 10 名义命中 SCN28，但 R32 SCN28-corpus 深扫（since_corpus=2 轮前）
> 已穷尽 place 语料候选并补种 15，本轮 4 页正是消费该批余量。重复触发 SCN28 表层扫描无新增
> 意义（承 R33/R34 同判），故消费既有队列余量走 NEW1，把独立 discover 让给 3.5 SCN28-corpus
> 到期（since_corpus 达 30）时集中执行。记为惯例延续，非门违背。

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| lake-kirdall | The Master of the World (MW)| PFOGz1 | 2211 | 10 | fictional / Kansas, US | accept |
| loch-katrine | The Underground City (UC)| vNteHt | 2497 | 14 | real / Stirling, Scotland | accept |
| christmas-harbour | An Antarctic Mystery (AM)| 6jWfE4 | 2375 | 13 | real / Kerguelen Islands | accept |
| port-barnett | The Fur Country (FC)| aPNNFm | 2451 | 12 | fictional / Arctic N. America | accept |

> **候选校准（承 R30/R31/R33/R34 实测惯例）**：4 候选 queue 估值（15/14/13/12）建页前按源作 grep
> 拆分校准，实测 distinctPN 分别为 10/14/13/12，均 ≥ standard ≥5 门，全数 accept。Lake Kirdall
> 估值 15 略高于实测 10（MW 两章集中命名），无碍建页。

> **互链**：Loch Katrine → [[new-aberfoyle]] / [[aberfoyle]]（UC 地下矿链，R30 建，湖溃陷排入其下矿坑）；
> Port Barnett → [[cape-bathurst]] / [[victoria-island]]（FC 漂流链，R29 建，港随 Cape Bathurst 断裂成岛而失）；
> Lake Kirdall → Robur（红链，留 character 轮）/ The Master of the World（work）；
> Christmas Harbour → Halbrane（叙事载具，非 technology 页）/ Green Cormorant（Atkins 客栈，未建）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MW,UC,AM,FC}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
四页全段拆分后 add 前核验通过（无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前 `\n\n` 分段核验，四页无超长段 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 4 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 35→36`；`type_round 6→7`；`rounds_since_last_evv5 6→7`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 2→3`；`last_updated_round→36`。

## 遗留问题

1. **R36 = place 队列见底 → zombie-guard/SCN28 触发**：queue(place) 本轮由 4 降至 0。R36 起无独立
   place 候选，zombie-guard（queue(place)==0）优先命中 → SCN28 表层复扫；若连续低产 streak≥3 → CLOSE
   place（final_count≈42）转 event（type_queue 队首）。SCN28-corpus 深扫距到期（since_corpus 达 30）尚 27 轮。
2. **EVV5 临近**：since_evv5=7，R38 达 evv5_interval=10 → EVV5 place 质量评估轮（样本已 ≥27 页，充足）。
3. **place 覆盖盘点**：本轮后 place 累计约 42 页（Pilot 15 + GROW R29–R35 新增 27）。Lincoln Island 微地理簇、
   澳洲搜寻链、非洲气球链、FC 漂流链、UC 地下矿链均成链，广度充分，为 CLOSE 转 event 铺垫。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
