---
round: 80
date: 2026-07-15
type_round: 51
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - krasnoiarsk
  - perm
  - obi
  - ekaterenburg
  - yenisei
result: accept
---

# GROW 2.1-B · R80 · NEW1 · place — 建 5 新页（standard 档，MS Ural-西伯利亚河/城群）

## 本轮公告

**R80 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 24→19**

R79（SCN28 discover 补种 15）后 since_evv5=7、since_discover=0、discover_streak_low=0、queue(place)=24、since_corpus=16。
决策矩阵：since_evv5=7<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=24≥10 且 since_discover=0<10 → SCN28 不触发；since_corpus=16<30 → 非 corpus；落 NEW1。
建 5 新页，消费 R79 补种头部 MS Ural-西伯利亚群：**Krasnoiarsk**（Yenisei 高岸城）+ **Perm**（Ural 西坡）+
**Obi**（西伯利亚大河）+ **Ekaterenburg**（Ural 东坡首站）+ **Yenisei**（大河）。五页均 MS 单源、
与既建 Irkutsk/Omsk/Tomsk/Kolyvan/Nijni-Novgorod 同源互链，页内引注 5–6 全达门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=7 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =7 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=24≥10, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =16 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=24 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| krasnoiarsk | Michael Strogoff (MS) | — | 5 | real / Eastern Siberia | accept |
| perm | Michael Strogoff (MS) | — | 5 | real / Russia (Ural) | accept |
| obi | Michael Strogoff (MS) | — | 6 | real / Western Siberia | accept |
| ekaterenburg | Michael Strogoff (MS) | — | 5 | real / Russia (Ural) | accept |
| yenisei | Michael Strogoff (MS) | — | 5 | real / Eastern Siberia | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——5/5/6/5/5 全达门。
> **河名首度建页**：Obi（Ob 河，alias Ob）+ Yenisei——Verne 西伯利亚地理骨架的大河，distinctPN 稳固，
> 补 place 类型「自然水系」盲区。二者接地句均确指河流（词边界，非 Obi 人名/其他）。
> **散文门五页全 ≤400**（add 前分段核验，Obi 一段 413 微调后通过）。
> **alias**：obi→Ob；余四页 Verne 原文即用现名，无 modern alias。

## 命名与互链

- **命名**：krasnoiarsk / perm / obi（alias Ob）/ ekaterenburg / yenisei——均 real。
- **互链**（与既建 MS 驿路群密织）：
  Krasnoiarsk ⇄ [[Michael Strogoff]]/[[Yenisei]]/[[Tomsk]]/[[Irkutsk]]；
  Perm ⇄ [[Michael Strogoff]]/[[Ekaterenburg]]/[[Omsk]]/[[Nijni-Novgorod]]；
  Obi ⇄ [[Michael Strogoff]]/[[Kolyvan]]/[[Tomsk]]/[[Baraba]]；
  Ekaterenburg ⇄ [[Michael Strogoff]]/[[Perm]]/[[Omsk]]/[[Tomsk]]/[[Irkutsk]]；
  Yenisei ⇄ [[Michael Strogoff]]/[[Krasnoiarsk]]/[[Irkutsk]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/MS-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（Obi 微调一段）。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 5/5/6/5/5，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：5/5/6/5/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，Obi 413 微调后全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；obi 有 alias（Ob）；无新 alias 冲突 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（24→19）；grow_state NEW1 six-step；registry 1253→1258，unknown 0（仅 Robur alias 旧账 PARK）|
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 80→81`；`type_round 51→52`；`rounds_since_last_evv5 7→8`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 16→17`；`last_updated_round→81`。

## 遗留问题

1. **place 页数 185→190**：本轮 +5，registry 全库 1253→1258，unknown 0。
2. **queue(place) 19≥10**：24 − R80 消费 5 = 19（含 R79 剩余 10：Amazon/Volga/Omaha/Liverpool/Suez/
   Auckland/Shanghai/Singapore/Ega/Zabediero + R76 剩 2：Allahabad/Benares + 既有 7 跨源/hold）。
3. **下轮 R81 = NEW1**：queue=19≥10、since_evv5=8<10、since_discover=1<10、since_corpus=17<30
   → 优先级 6 NEW1 建 5 页。优先消费大河/大港（Amazon/Volga/Omaha/Liverpool/Suez）。
4. **EVV5 将于 R82 触发**（since_evv5 R80 后=8，R82 达 10；届时 since_discover=3<10 → 优先级 1b 单 EVV5）。
5. **place runway 充足**：河/湖名纳入后候选池仍余 12+；后续尚有美西铁路镇、南美港待精核。
6. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
8. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
