---
round: 67
date: 2026-07-15
type_round: 38
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - coronation-gulf
  - platte-river
  - atlantic-ocean
  - caribbean-sea
  - ice-bank
result: accept
---

# GROW 2.1-B · R67 · NEW1 · place — 建 5 新页（standard 档）

## 本轮公告

**R67 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 14→9**

R66 后 since_evv5=5、since_discover=7、discover_streak_low=0、queue(place)=14、since_corpus=3。
决策矩阵：since_evv5=5<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=14≥10 且 since_discover=7<10 → SCN28 不触发；since_corpus=3<30 → SCN28-corpus 不触发；落 NEW1。
建 5 新页：**Coronation Gulf**（FC 北极湾）+ **Platte River**（AWED 内布拉斯加河）+
**Atlantic Ocean**（SC 大西洋）+ **Caribbean Sea**（TTLU 加勒比海）+ **Ice Bank**（TTLU 南极冰障）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=5 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=14≥10, since_discover=7 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =3 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=14 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| coronation-gulf | The Fur Country (FC) | gcZIeN | 5 | real / Arctic (North American coast) | accept |
| platte-river | Around the World in Eighty Days (AWED) | PrThrX | 6 | real / United States (Nebraska) | accept |
| atlantic-ocean | In Search of the Castaways (SC) | 658ycD | 5 | real / Atlantic Ocean | accept |
| caribbean-sea | Twenty Thousand Leagues Under the Sea (TTLU) | QwfNAc | 5 | real / Atlantic (Caribbean) | accept |
| ice-bank | Twenty Thousand Leagues Under the Sea (TTLU) | uBUzV8 | 7 | real / Antarctic (Southern Ocean) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——5/6/5/5/7 全达门。
> **Ice Bank 类型裁定**：queue 记「feature/place 待核」。作为大南极冰障（named barrier），
> 既是地理实体亦是航行屏障，按 place 建（region Antarctic / Southern Ocean，real）。alias「The Ice Bank」。
> **Platte River alias**：语料含「North Platte River」支流称谓，收为 alias。
> **Caribbean/Coronation 引注复核**：建前逐句核 5 处均真正命名该地（非子串/并列误配），确认达门。

## 命名与互链

- **命名**：coronation-gulf / platte-river（alias North Platte River）/ atlantic-ocean / caribbean-sea /
  ice-bank（alias The Ice Bank）。
- **互链**：Coronation Gulf ⇄ [[The Fur Country]]；Platte River ⇄ [[Around the World in Eighty Days]]；
  Atlantic Ocean ⇄ [[In Search of the Castaways]]；Caribbean Sea ⇄ [[Twenty Thousand Leagues Under the Sea]] /
  [[Gulf of Mexico]]；Ice Bank ⇄ [[Twenty Thousand Leagues Under the Sea]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{FC,AWED,SC,TTLU}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：5/6/5/5/7 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（14→9）；grow_state NEW1 six-step；无新 alias 冲突 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 67→68`；`type_round 38→39`；`rounds_since_last_evv5 5→6`；
`rounds_since_last_discover 7→8`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 3→4`；`last_updated_round→68`。

## 遗留问题

1. **place 页数 145→150**：本轮 +5，registry 全库 1213→1218。
2. **queue(place) 9 < 10**：14 − R67 消费 5 = 9（含 2 holds Lake Ontario/Black Sea + Kara Sea 待精扫，
   即真候选约 6：North Sea/Firth of Clyde/Long Island/Goat Island/Bay of Bengal/Cape Bon 跨源候选）。
3. **下轮 R68：queue=9<10 → 优先级 3 SCN28 抢占 NEW1**（表层复扫 discover 轮，非建页）。
   since_evv5=6<10、since_discover=8<10、since_corpus=4<30，故仅 SCN28（queue_size<10 条件）触发。
   SCN28 深/表层复扫补种 place 候选入 queue，since_discover 归 0；若 new_candidates<3 则 discover_streak_low+=1。
   注：剩余单作强候选渐稀，跨源候选（North Sea 等）与 Kara Sea 精扫为主要补给源。
4. **Kara Sea 建前须精扫**：承 R63–R66，「kara」子串过配，建前须精确重扫。
5. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
