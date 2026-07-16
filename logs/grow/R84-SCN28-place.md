---
round: 84
date: 2026-07-15
type_round: 55
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 6
pages: []
result: discover
---

# GROW 2.1-B · R84 · SCN28 · place — 表层复扫补种 6 候选（queue 9→15）

## 本轮公告

**R84 — Phase 2.1 — SCN28 — place — discover 补种 6 候选 / 非建页 / since_discover 归 0 / queue 9→15**

R83（EVV5 反思）后 since_evv5=0、since_discover=4、discover_streak_low=0、queue(place)=9、since_corpus=20。
决策矩阵：since_evv5=0<10 → EVV5 不触发；discover_streak_low=0<3 → CLOSE 不触发；
**queue=9<10 → 优先级 3 SCN28 触发**（表层复扫补种）；since_corpus=20<30 → 非 corpus。
本轮不新建/编辑页面，仅向 queue 补种 place 候选。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =20 | 否 |
| 6 | NEW1（默认）| — | 否（被 3 抢占）|

## 扫描方法

对全部 122,989 句 `data/sentence_index/*.jsonl` 执行两轮扫描：
1. **geo-2gram**（`Cape/Lake/Mount/Port/Fort/Gulf/Bay/…` + 专名）——多为既有页或截断名，去噪后无新增 ≥5。
2. **裸词 + 介词上下文**（`at/in/to/from/of/near/toward/reached … [A-Z][a-z]{3,}`）——按单作 distinctPN 排序，
   人工剔除人名/船名/片段污染（Joam/Torres/Pencroft/Paganel/Glenarvan/Cyrus/Granite House/Prospect
   Heights 等，续 R79 裸词污染教训），保留确为地名者，再逐一 `\bName\b` 词边界复核单作 distinctPN。

## 既有 held 候选精核（词边界复量）

| 候选 | 单作 max distinctPN（词边界）| 处置 |
|------|------|------|
| North Sea | TTLU:2 / RC:2 | 续 hold（单作 <5，跨源过散）|
| Cape Bon | OC:3 / RC:1 | 续 hold（单作 <5）|
| Bay of Bengal | TTLU:3 / AWED:1 | 续 hold（RM:1 疑子串，单作 <5）|
| Long Island | TTLU:3 / AWED:1 | 续 hold（ASC:2 = 里海 Uzun Ada 异地同名，真长岛 <5）|
| Black Sea | ASC:2 | 续 hold（跨源过散）|
| Lake Ontario | MW:4 | 续 hold（MW:4<5）|
| **Kara Sea** | **TTLU:1** | **剔除**（词边界仅 1；原 queue「agg 5」系 kara 子串污染，58 命中多非地名）|

## 补种候选（6，均单作 ≥5 词边界 distinctPN）

| slug | 源作 | 单作 distinctPN | real/fictional / region（拟）| 依据 |
|------|------|-----------------|------------------------------|------|
| Gallia | Off on a Comet (OC) | 156 | fictional / space (comet) | 携地球碎块绕日的新小行星/居民世界 |
| Australia | In Search of the Castaways (SC) | 93 | real / Oceania | 沿 37°线横穿之陆/Ayrton 线索地 |
| Siberia | Michael Strogoff (MS) | 78 | real / Russia (Siberia) | Michael 东行主区域/鞑靼入侵战场 |
| Noroe | The Waif of the Cynthia (WC) | 45 | fictional / Norway | 挪威西岸近 Bergen 渔村/Erik 成长地 |
| Aden | Around the World in Eighty Days (AWED) | 6 | real / Yemen | Suez→Aden 红海加煤港/1310 英里段终点 |
| Yakutsk | Michael Strogoff (MS) | 5 | real / Eastern Siberia | 远东驿路城，distinctPN 恰达门 |

> **交叉核既有页**：6 候选均经 pages.json（1267 页）label/slug/alias 比对，无既有页（承 HK-R78-tsalal-dup
> 教训，discover 即核）。Gallia 非既有 technology/place；Australia/Siberia 为宽域 region 页（Verne wiki
> 既有 region 型 place 先例）。
> **real/fictional 待建时定案**：Gallia（彗星世界）、Noroe（Verne 虚构挪威村，设定于真实海岸）暂标 fictional，
> 建页前据接地句复核。

## EXIT-GATE 检查（SCN28 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 discover 日志；queue.md 补种 6 候选（9→15）+ Kara Sea 剔除批注；grow_state SCN28 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 six-step）

`current_round 84→85`；`type_round 55→56`；`rounds_since_last_evv5 0→1`；
`rounds_since_last_discover 4→0`（discover，RESET）；`discover_streak_low` 保持 0
（new_candidates=6≥3，非低产 discover）；`rounds_since_last_corpus_discover 20→21`；`last_updated_round→85`。

## 遗留问题

1. **place 页数保持 199**：本轮非建页，registry 全库 1267，unknown 0。
2. **queue(place) 15≥10**：9 − 剔除 Kara Sea + 补种 6 = 15（新 6 + 既有 Ega/Zabediero 两单源 +
   6 跨源 held + Kara Sea 已剔）。
3. **下轮 R85 = NEW1（优先级 6）**：since_evv5=1<10、queue=15≥10、since_discover=0<10、since_corpus=21<30
   → 优先级 6 NEW1 建 5 页。优先消费高 distinctPN 新候选（Gallia/Australia/Siberia/Noroe/Aden）。
   注：Gallia/Australia/Siberia 为宽域/虚构世界页，建前须精选 5 条最确指接地句（避免泛指），
   Australia 尤须区分「Australia」实指与泛指（南半球/继续词）。
4. **HK-R78-tsalal-dup 后续**：R85+ 附带补核 R77 五页（nijni-novgorod/bombay/melbourne/lima/gibraltar）
   是否另有既有重复页（本轮 discover 6 候选已交叉核，均无既有页）。
5. **两 Pilot 页 PN=4**、**24 既有页散文>400**：均已录 housekeeping/PARK。
6. **runway**：剔 Kara Sea 后跨源 held 6 仍单作 <5 不可单源建；新候选池尚有美西铁路（Ogden/Salt Lake
   City/Reno 单作 <5，需跨源或降级）、南美/亚洲港零星。place 类型广度渐近饱和，后续 discover 产出或走低。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
