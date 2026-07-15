---
round: 37
date: 2026-07-15
type_round: 9
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - fort-hope
  - cape-michael
  - claw-cape
  - red-creek
  - tsalal-island
result: accept
---

# GROW 2.1-B · R37 · NEW1 · place — R36 复扫首批 5 页（standard 档）

## 本轮公告

**R37 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档**

queue(place)=26（R36 复扫补种），无高优先门抢先，落 NEW1 默认门。
建 R36 复扫首批 5 页，取高 distinctPN 且互链密集者：
**FC 漂流簇**（Fort Hope FC:66 / Cape Michael FC:25）+ **MI 林肯岛簇补漏**（Claw Cape MI:32 /
Red Creek MI:24）+ **AM**（Tsalal Island AM:61，接 christmas-harbour）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=26, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =4 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=26 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| fort-hope | The Fur Country (FC)| lstwEI | 2292 | 66 | fictional / Arctic N. America | accept |
| cape-michael | The Fur Country (FC)| GBNbot | 2191 | 25 | fictional / Arctic N. America | accept |
| claw-cape | The Mysterious Island (MI)| 2RcOUB | 2260 | 32 | fictional / Lincoln Island | accept |
| red-creek | The Mysterious Island (MI)| cPY4rJ | 2014 | 24 | fictional / Lincoln Island | accept |
| tsalal-island | An Antarctic Mystery (AM)| 2xuDfE | 2186 | 61 | fictional / Antarctic | accept |

> **校准**：5 候选 R36 主源 distinctPN 全数复核可引，与 queue 值一致（FC/MI/AM 单源集中，无跨源
> 误报）。全 accept。Red Creek 引 MI-012-062 时 OCR「casuannas」以省略号规避，不损句意。

> **互链**：Fort Hope ⇄ [[cape-bathurst]] / [[port-barnett]] / [[victoria-island]]（FC 漂流链）；
> Cape Michael ⇄ [[cape-bathurst]] / [[port-barnett]] / [[fort-hope]]（FC 同簇互引）；
> Claw Cape → [[lincoln-island]] / [[granite-house]] / [[union-bay]]（MI 岛地理链）；
> Red Creek → [[lincoln-island]] / [[lake-grant]]（红溪注入湖）/ [[granite-house]]；
> Tsalal Island → [[christmas-harbour]]（Halbrane 出发港）/ Arthur Gordon Pym（红链，character 轮）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{FC,MI,AM}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段拆分核验通过（add 前 `\n\n` 分段，无超长段）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页无超长段 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 37→38`；`type_round 8→9`；`rounds_since_last_evv5 8→9`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 4→5`；`last_updated_round→38`。

## 遗留问题

1. **R38 = EVV5 到期**：since_evv5 本轮 8→9，R38 达 evv5_interval=10 → **EVV5 place 质量评估轮**
   （不建页、不消费队列，抽样评分 + 反哺模板）。样本 47 页，充足。EVV5 后 R39 恢复 NEW1 消费剩余 21 候选。
2. **queue(place) 余 21**：R36 补种 26 − R37 消费 5 = 21。约 R39–R43 五轮消费（EVV5 穿插）。
   下批优选：Gourbi Island(OC:41) / Phina Island(GM:40) / Red Sea(TTLU:28) / Lake Erie(MW:27) /
   Cape Esquimaux(FC:23) / Behring Strait(FC:22) / Fort Providence(ACH:22) / Beechey Island(ACH:20)。
3. **建前二次校准照旧**：剩余 21 候选主源 distinctPN 为 R36 grep 值，建页前逐页复核 PN 句可引性。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
