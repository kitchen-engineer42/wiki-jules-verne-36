---
round: 34
date: 2026-07-15
type_round: 6
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - shark-gulf
  - flotsam-point
  - twofold-bay
  - lake-tchad
  - snowy-river
result: accept
---

# GROW 2.1-B · R34 · NEW1 · place — Lincoln Island 收尾 + 真实地理（+5 页，standard 档）

## 本轮公告

**R34 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档**

queue(place)=10（≠0），queue_size≥10，无门抢先，落 NEW1 默认门。
建第五批 5 页 place，消费 R32 深扫余量：**Lincoln Island 收尾 2**（Shark Gulf / Flotsam Point，MI）+
**真实地理 3**（Twofold Bay / Snowy River 澳洲 ISC，Lake Tchad 非洲 FWB）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =1 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=10 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| shark-gulf | The Mysterious Island (MI/SI)| iCzF3E | 2436 | 18 | fictional / Lincoln Island | accept |
| flotsam-point | The Mysterious Island | EtoX1N | 2415 | 26 | fictional / Lincoln Island | accept |
| twofold-bay | In Search of the Castaways (SC)| 7AghAy | 2439 | 36 | real / NSW Australia | accept |
| lake-tchad | Five Weeks in a Balloon (FWB)| FuoXFI | 2512 | 32 | real / Central Africa | accept |
| snowy-river | In Search of the Castaways | 55qbz5 | 2137 | 20 | real / Victoria Australia | accept |

> **候选勘误（承 R30/R31/R33 实测惯例）**：queue「Flag Point」估值 14 系跨源聚合误报——实测
> `Flag Point` 0 命中于 MI/SI，实属 **Godfrey Morgan (GM)**（GM-015/016/017/021，仅 4 distinctPN，
> 薄且异源），本轮**弃建**，改以 Snowy River（SC，20 distinctPN，接 Twofold Bay 澳洲链）补位。
> 记 HK：深扫聚合 distinctPN 须按源作 grep 拆分校准。

> **互链**：Shark Gulf → Serpentine Peninsula / Port Balloon（MI 岛地理链，R33 建）；
> Flotsam Point → Granite House；Twofold Bay ⇄ Snowy River（ISC 澳洲搜寻链，Snowy River 为
> Twofold Bay 最后障碍）；Lake Tchad → Victoria Balloon（既有 technology）/ Dr. Ferguson（红链，
> 留 character 轮）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MI,SI,SC,FWB}-*.jsonl`，段级 PN 为 sid 前三段。MI/SI 重复段
统一引 MI PN 避免跨卷重复。散文门 ≤400：shark-gulf（427）/ twofold-bay（432）两超长段拆分后过门；
flotsam-point / lake-tchad / snowy-river 无超长段。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | shark-gulf / twofold-bay 拆分后 add 前核验通过 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选 + Flag Point 弃建注；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 34→35`；`type_round 5→6`；`rounds_since_last_evv5 5→6`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 1→2`；`last_updated_round→35`。

## 遗留问题

1. **R35 = place NEW1（消费深扫末批）**：queue(place) 由 10 降至 5（Flag Point 弃建，实余
   Lake Kirdall / Loch Katrine / Christmas Harbour / Port Barnett 4）。R35 建末批 4 页后 P1 place 再见底。
2. **EVV5 临近**：since_evv5=6，R38 达 evv5_interval=10 → EVV5 place 质量评估轮（样本已 ≥23 页）。
3. **place CLOSE 展望**：深扫候选 R35 建完 → queue(place) 归零。R36 起若无独立 place 候选，
   zombie-guard/SCN28 触发再深扫；连续低产 streak≥3 → CLOSE place 转 event（type_queue 队首）。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
