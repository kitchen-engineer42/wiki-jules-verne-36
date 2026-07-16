---
round: 78
date: 2026-07-15
type_round: 49
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - morganton
  - tijuco
  - kilimanjaro
  - tsalal
  - calcutta
result: accept
---

# GROW 2.1-B · R78 · NEW1 · place — 建 5 新页（standard 档，续消费 R76 城市候选）

## 本轮公告

**R78 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 14→9**

R77（NEW1 建 5）后 since_evv5=5、since_discover=1、discover_streak_low=0、queue(place)=14、since_corpus=14。
决策矩阵：since_evv5=5<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=14≥10 且 since_discover=1<10 → SCN28 不触发；since_corpus=14<30 → 非 corpus；落 NEW1。
建 5 新页，续消费 R76 补种城市候选：**Morganton**（MW Great Eyrie 山脚镇）+ **Tijuco**（EHLA 钻石区旧案城）+
**Kilimanjaro**（TT/Topsy Turvy Gun Club 巨炮山）+ **Tsalal**（AM Poe 续篇南极岛，**fictional**）+
**Calcutta**（AWED 印度铁路东终点）。五页页内引注 5–6 全达门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=5 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=14≥10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =14 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=14 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| morganton | The Master of the World (MW) | — | 5 | real / United States (North Carolina) | accept |
| tijuco | Eight Hundred Leagues on the Amazon (EHLA) | — | 5 | real / Brazil (Minas Gerais) | accept |
| kilimanjaro | Topsy Turvy (TT) | — | 6 | real / East Africa (Tanzania) | accept |
| tsalal | An Antarctic Mystery (AM) | — | 5 | **fictional** / Antarctic (Southern Ocean) | accept |
| calcutta | Around the World in Eighty Days (AWED) | — | 6 | real / India (Bengal) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——5/5/6/5/6 全达门。
> **Kilimanjaro book=Topsy Turvy**：TT=Topsy Turvy（Sans dessus dessous，Gun Club 续篇），非气球篇；
> 情节为 Baltimore Gun Club 于 Kilimanjaro 南麓凿 27 米口径巨炮欲移地轴。地物 real，region East Africa。
> **Tsalal 为 fictional**：AM（An Antarctic Mystery，Poe《Pym》续篇）虚构南极岛；real_or_fictional=fictional，
> alias 记 Tsalal（label=Tsalal Island）。
> **散文门五页全 ≤400**（add 前分段核验，Morganton 一段 435 拆分后通过）。

## 命名与互链

- **命名**：morganton / tijuco / kilimanjaro / tsalal（label Tsalal Island，alias Tsalal）/ calcutta。
- **互链**：
  Morganton ⇄ [[The Master of the World]]/[[Goat Island]]；
  Tijuco ⇄ [[Eight Hundred Leagues on the Amazon]]/[[Manaos]]/[[Belem]]/[[Tabatinga]]；
  Kilimanjaro ⇄ [[Topsy Turvy]]；
  Tsalal ⇄ [[An Antarctic Mystery]]；
  Calcutta ⇄ [[Around the World in Eighty Days]]/[[Bombay]]/[[Allahabad]]/[[Hong Kong]]/[[Yokohama]]。

> **前向链**：Tijuco/Calcutta 链既建 Belem/Tabatinga/Bombay/Yokohama（R74/75/77）；Calcutta 链 [[Allahabad]]（R76 候选，待建）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MW,EHLA,TT,AM,AWED}-*.jsonl`，段级 PN 为 sid 前三段。
散文门 ≤400：五页 add 前分段核验通过（Morganton 拆一段）。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 5/5/6/5/6，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：5/5/6/5/6 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，Morganton 435 段拆分后全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；tsalal 有 alias（Tsalal）；无新 alias 冲突 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（14→9）；grow_state NEW1 six-step；registry 1248→1253，unknown 0（仅 Robur alias 旧账 PARK）|
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 78→79`；`type_round 49→50`；`rounds_since_last_evv5 5→6`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 14→15`；`last_updated_round→79`。

## 遗留问题

1. **place 页数 180→185**：本轮 +5，registry 全库 1248→1253，unknown 0。
2. **queue(place) 9<10**：14 − R78 消费 5 = 9（含 R76 剩余 2：Allahabad/Benares + 既有 7：Lake Ontario/
   Black Sea/North Sea/Cape Bon/Kara Sea + Long Island/Bay of Bengal 两 hold）。
3. **下轮 R79 = SCN28（优先级 3）**：since_evv5=6<10、queue=9<10、since_discover=2<10、since_corpus=15<30
   → 优先级 3 SCN28 触发（表层复扫补种）。续裸词城市扫描（R76 已证 runway 充足）：印度次城、
   俄/西伯利亚镇、南美城、南太平洋岛群。
4. **EVV5 将于 R82 触发**（since_evv5 R78 后=6，R82 达 10）。
5. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
