---
round: 49
date: 2026-07-15
type_round: 21
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - baffin-bay
  - walruses-bay
  - davis-strait
  - caspian-sea
  - cape-tchelynskin
result: accept
---

# GROW 2.1-B · R49 · NEW1 · place — R48 补种首批 5 页（standard 档）

## 本轮公告

**R49 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R48 后 queue(place)=22，since_discover=0、since_evv5=9，决策矩阵高优先门全否，落 NEW1。
建 R48 SCN28 补种首批 5 强候选（北极极海簇 3 + FC 火山湾 1 + 中亚内海 1）：
**Baffin's Bay**(ACH 主源段级 ~38，label Baffin Bay) / **Davis's Straits**(ACH 16，label Davis Strait) /
**Walruses' Bay**(FC 22 fictional) / **Caspian Sea**(ASC 主源段级 >20) / **Cape Tchelynskin**(WC 10 欧亚极北)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=9 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=22, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =16 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=22 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测段级 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| baffin-bay | The Adventures of Captain Hatteras (ACH)| UuNCAQ | 2279 | ~38（含 Sea 变体，主源 ACH）| real / Arctic (Greenland–Baffin) | accept |
| walruses-bay | The Fur Country (FC)| F7XXMt | 2089 | 22 | fictional / Arctic (Cape Bathurst) | accept |
| davis-strait | The Adventures of Captain Hatteras (ACH)| rLAsgn | 2173 | 16 | real / Arctic (Greenland–Baffin) | accept |
| caspian-sea | The Adventures of a Special Correspondent (ASC)| 4PEBf3 | 2267 | >20（主源 ASC）| real / Asia (Transcaucasia) | accept |
| cape-tchelynskin | The Waif of the Cynthia (WC)| wYEK6v | 2073 | 10 | real / Arctic (N. Siberia) | accept |

> **建前主源段级严扫（承 R48 聚合校准铁律）**：R48 入队多为跨源 agg 估值，本轮建前逐页主源段级严扫——
> Baffin's Bay 主源 ACH 段级远超 5（含 Bay/Sea 双式，Verne 多用「Baffin's Sea」）；Caspian Sea 主源 ASC
> 段级 >20（RC-013 另有 9，Robur 飞越，纳为次源互链）；Davis's Straits ACH 16；Walruses' Bay FC 22；
> Cape Tchelynskin WC 10。五页主源全达 standard 门。**同名/org 辨析**：本批无 Hudson's Bay（水体 12 与
> Hudson's Bay Company org 语境难净分，且薄），已 R48 hold/本轮不建，续观察。

> **命名规范**：三页用现代规范 label + 语料变体 alias——baffin-bay（label Baffin Bay / alias Baffin's Bay·Baffin's Sea）、
> davis-strait（label Davis Strait / alias Davis's Straits）、cape-tchelynskin（Verne 拼写，alias Cape Severe 旧称）。
> caspian-sea alias The Caspian（语料多作省略式）。承 behring-strait 先例（语料 Behring's Straits → 页 label Behring Strait）。

> **互链**：Baffin Bay ⇄ [[The Adventures of Captain Hatteras]] / [[Davis Strait]] / [[Melville Bay]] / [[The Forward]]（ACH 极海簇）；
> Davis Strait ⇄ [[Baffin Bay]] / [[The Forward]] / [[Behring Strait]]（ACH 簇）；
> Walruses' Bay ⇄ [[The Fur Country]] / [[Cape Bathurst]] / [[Fort Hope]]（FC 簇）；
> Caspian Sea ⇄ [[The Adventures of a Special Correspondent]] / [[Grand Transasiatic Railway Company]] / [[Robur the Conqueror]] / [[Black Sea]]（中亚铁路簇；Black Sea 为 R48 在队红链）；
> Cape Tchelynskin ⇄ [[The Waif of the Cynthia]]（WC 单源）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{ACH,FC,ASC,WC,RC}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 317–363，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 363 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；label 含撇号者 YAML 单引号转义（Walruses'' Bay）|
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（27→22）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 49→50`；`type_round 20→21`；`rounds_since_last_evv5 9→10`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 16→17`；`last_updated_round→50`。

## 遗留问题

1. **since_evv5 达 10 → R50 触发 EVV5**：本轮 six-step 后 since_evv5=10，下轮决策矩阵优先级 1b（EVV5）触发，
   R50 落 EVV5 评估（既有 place 页均分/低分抽查/模板演进），非 NEW1。since_discover=1<10 故非 1a（EVV5+SCN28）。
2. **queue(place) 22**：R48 后 27 − R49 消费 5 = 22，充裕。EVV5 后续批优选：
   Sandwich Islands(agg 10)/Norfolk Island(agg 10)/Cape Verde(agg 9)/Faroe Islands(agg 8)/Fort Sumter(8)/Morris Island(10)。
3. **聚合 vs 主源段级铁律续**：R48 长尾候选（Lake Ontario/Black Sea/Cape Verde 等跨作 agg）建前必主源段级严扫；
   跨作 place 可纳次源互链（如 Caspian 纳 RC Robur 飞越）但 book 定主源。
4. **Hudson's Bay hold 续**：水体 12 与 Hudson's Bay Company（org 既有）语境难净分，暂不建；
   若后续严扫可净分水体≥5 再评估，否则留 list 提及。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5，PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
