---
round: 30
date: 2026-07-15
type_round: 2
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - aberfoyle
  - new-aberfoyle
  - fort-reliance
  - back-cup
  - quiquendone
result: accept
---

# GROW 2.1-B · R30 · NEW1 · place — 第二批 place NEW1（+5 页，standard 档）

## 本轮公告

**R30 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档**

queue_size=20（≥ discover_queue_threshold 10），queue(place)=9（≠0），无门抢先，落入 NEW1 默认门。
建第二批 5 页 place：**UC 簇**（Aberfoyle / New Aberfoyle 互链地下煤城）+ **FC**（Fort Reliance）+
**FF**（Back Cup）+ **DOSE**（Quiquendone）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=20, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =28 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=9 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | citations | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------|---------------------------|------|
| aberfoyle | UC(The Underground City)| SK7z10 | 2294 | 6 | real / Stirling, Scotland | accept |
| new-aberfoyle | UC | lemUhm | 2513 | 7 | fictional / Stirling, Scotland | accept |
| fort-reliance | FC(The Fur Country)| gH2ols | 2574 | 7 | real / Great Slave Lake | accept |
| back-cup | FF(Facing the Flag)| CgRXkQ | 2882 | 8 | fictional / Bermuda archipelago | accept |
| quiquendone | DOSE(Doctor Ox's Experiment)| xuFXo6 | 2563 | 7 | fictional / Flanders | accept |

> **候选替换（Fort Providence 剔除）**：queue 原列 Fort Providence（distinctPN≈14 估值），但语料实测
> `Fort Providence` 仅 3 处直接命名（多为「Fort Providence or Fort Resolution」并列地名），无法支撑
> standard 档 ≥5 distinct-PN 引注——判为**薄候选**，本轮以 **Back Cup**（FF，111 命中/11 distinct-PN）替换。
> Fort Providence 降级留 queue P2 或后续 list 页提及，不单建 place。**教训：queue 的 distinctPN 估值须以
> 建页前实测校准**（同 Coal City→Coal Town 命名勘误）。

> **互链**：Aberfoyle ⇄ New Aberfoyle（旧矿枯竭→地下新煤田 Coal Town/Loch Malcolm）；Fort Reliance →
> Cape Bathurst / Victoria Island（FC 远征链，接 R29 两页）；Back Cup → Fulgurator（既有 technology 页，
> Roch 炸毁 Back Cup）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{UC,FC,FF,DOSE}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
aberfoyle（初稿 410）与 back-cup（初稿 427/511 两段）拆分后过门；aberfoyle 经 edit_page.py 复核 rev SK7z10。
勘误：New Aberfoyle 的地下村落语料名为 **Coal Town**（非 queue 误记的「Coal City」，后者 0 命中）；
其地下湖为 **Loch Malcolm**（UC-010-006）。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | aberfoyle / back-cup 拆分修正；余页 add 前核验 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 4 候选 + Fort Providence 降级注；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 30→31`；`type_round 1→2`；`rounds_since_last_evv5 1→2`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 28→29`；`last_updated_round→31`。

## 遗留问题

1. **R31 = place（P1 余 2 强候选 + P2）**：P1 place 余 Crespo Island（20KL，distinctPN≈7）；
   Fort Providence 降级（薄候选）。P2 place：Stone's Hill（FEM 红链）/ Pacific Railroad（borderline）。
   place P1 接近见底 → R31 或 R32 或触 SCN28 深扫补种。
2. **place discover 补种临近**：P1 place 建完后 queue(place) 将主要剩 P2 的 Stone's Hill/Pacific Railroad；
   若 queue(place) 降至低位，SCN28 深扫 36 部合集地名（真实地理门槛 + 各航线/城市/岛屿）。
3. **the tug / Ebba borderline 复议**：back-cup 已建（含 the tug 电力潜航穿隧道入洞、Ebba schooner 母船
   语境）。the tug 仍无专名，维持不建 technology 之判；Ebba 作叙事载具留 place/2.1-Z。
4. **queue distinctPN 估值失准**：Fort Providence（估 14 实 3）、Coal City（估有实 0，实为 Coal Town）
   两处勘误——后续建页前一律实测 distinct-PN 校准 queue 估值。记 HK。
5. **registry typefield 未透传**：real_or_fictional/region 未进 pages.json（frontmatter 正确，book 已透传）。
   既有 PARK 债务。
6. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区 六项债务照旧 PARK/记录。
