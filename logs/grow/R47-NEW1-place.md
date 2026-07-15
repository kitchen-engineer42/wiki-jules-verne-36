---
round: 47
date: 2026-07-15
type_round: 19
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - lake-tanganyika
  - victoria-bay
  - lake-superior
  - lake-michigan
  - cape-corrientes
result: accept
---

# GROW 2.1-B · R47 · NEW1 · place — R41 补种第六批 5 页（standard 档）

## 本轮公告

**R47 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R46 后 queue(place)=14，since_discover=5、since_evv5=7，轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种第六批 5 页（DSCF 非洲 1 + ACH 北极 1 + MW 大湖 2 + SC 阿根廷 1）：
**Lake Tanganyika**(DSCF:10 奴隶贸易大道/Livingstone 探险) / **Victoria Bay**(ACH:7 New America 湾) /
**Lake Superior**(MW:6 The Terror 现身之湖) / **Lake Michigan**(MW:6 赛道尽头之湖) /
**Cape Corrientes**(SC:6 Duncan 阿根廷岸巡弋岬)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=7 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =7 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=14, since_discover=5 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =14 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=14 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| lake-tanganyika | Dick Sand: A Captain at Fifteen (DSCF)| 450tmA | 2104 | 10 | real / Africa (Central African lakes) | accept |
| victoria-bay | The Adventures of Captain Hatteras (ACH)| VGg86x | 2074 | 7 | fictional / Arctic (New America) | accept |
| lake-superior | The Master of the World (MW)| eFSWW1 | 2169 | 6 | real / North America (Great Lakes) | accept |
| lake-michigan | The Master of the World (MW)| Vjrktq | 2157 | 6 | real / North America (Great Lakes) | accept |
| cape-corrientes | In Search of the Castaways (SC)| aEf8UC | 2123 | 6 | real / South America (Argentine coast) | accept |

> **建前二次校准（承铁律）+ 段级 distinctPN 复核**：queue 记 Cape Corrientes 5 / Lake Michigan 6 等为章级估值，
> 建前按段级（VVV-NNN-PPP）严扫：Lake Tanganyika 10 / Victoria Bay 7 / Lake Superior 6 / Lake Michigan（严 "lake michigan"）6 /
> Cape Corrientes 6，五页全达 standard 门（≥5）。Lake Michigan 排除单独 "Michigan"（并入 Superior 大湖链的裸词，含变体聚合 9），
> 只取 "Lake Michigan" 明确命名段。无跨实体同名混淆顾虑（本批地名均专有）。

> **互链**：Lake Tanganyika ⇄ [[Dick Sand: A Captain at Fifteen]] / [[Lake Tchad]]（非洲水体）；
> Victoria Bay ⇄ [[The Adventures of Captain Hatteras]] / [[Fort Providence]] / [[Beechey Island]]（ACH New America 簇）；
> Lake Superior ⇄ [[The Master of the World]] / [[Lake Michigan]] / [[Lake Erie]] / [[The Terror]]（MW 大湖链）；
> Lake Michigan ⇄ [[The Master of the World]] / [[Lake Superior]] / [[Great Eyrie]] / [[The Terror]]（MW 簇）；
> Cape Corrientes ⇄ [[In Search of the Castaways]] / [[Cape Bernouilli]] / [[Twofold Bay]]（SC 37 度线簇）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{DSCF,ACH,MW,SC}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 334–399，无超长段；cape-corrientes 399 贴门但达标）。
Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 399 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；lake-tanganyika alias「Tanganyika」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 47→48`；`type_round 18→19`；`rounds_since_last_evv5 7→8`；
`rounds_since_last_discover 5→6`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 14→15`；`last_updated_round→48`。

## 遗留问题

1. **queue(place) 余 9**：R46 后 14 − R47 消费 5 = 9。下批优选：
   Cape Washington(ACH:5) / Polar Sea(FC:14) / Bear Lake(FC:11) / Melville Island(ACH:9) /
   Gallian Sea(OC:12) / Cape Horn(TTLU:9) / Rocky Mountains(RM:9) / Loch Malcolm(UC:13) /
   Lake Tanganyika（本轮已建）等。余多为 5–14 候选，建前逐页复核段级 distinctPN。
2. **since_corpus 本轮达 15**：距 SCN28-corpus 深扫门（≥30）尚 15 轮，暂不触发。
3. **since_evv5 达 8**：距 EVV5 门（≥10）尚 2 轮，约 R49 触发。
4. **段级 vs 章级 distinctPN 校准**：本轮再证 queue 估值多为章级（VVV-NNN），
   建前须按段级（VVV-NNN-PPP）严扫方为 standard 门真值——章级低估（如 Tanganyika 章级 4 → 段级 10）。
   照旧建前逐页段级复核，承 R43–R46 铁律。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
