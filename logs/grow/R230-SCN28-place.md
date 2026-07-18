---
round: 230
date: 2026-07-18
type_round: 201
phase: "2.1"
current_type: place
gene: SCN28
pages: []
new_candidates: 2
result: discover
---

# GROW 2.1-B · R230 · SCN28-zombie · place — 撇号/连字符专项扫（第三次 place discover，关键分岔轮）

## 执行摘要

Phase 2.1-B place 广度扩张第 201 轮（type_round 201）。决策机 §3 首匹配 **SCN28-zombie**
（§3(4)：queue(place)==0——R229 Baffin's Bay 消费罄 R227 队列；且 since_evv5=3<10、
streak=2<3、since_discover=2<10，前三门皆否，落 §3(4)）。

本轮为 place **第三次** discover，专攻 R229 记录的 **HK-discover-possessive-hyphen-toponym-blindspot**：
discover3/single_toponym/feature_scan 三扫皆盲于**撇号 `X's Feature`** 与**连字符 `Cap-Cap`** toponym
（North-West Passage、Baffin's Bay 皆手动 gather 补得）。故新建 `/tmp/possessive_scan.py`
（撇号 `[A-Z][a-z]+'s\s+SUF`、连字符 `[A-Z][a-z]+-[A-Z][a-z]+(?:\s+SUF)?`、`SUF of Name`，
slugify 去撇号后对 pages.json known 集去重）系统化扫描。

**净新 2 地名**（<type_close_new_candidate_min=3 → discover_streak_low 2→3，达 type_close_streak）：

- **Plaza-Mayor**（PL×14 distinct，单指）：利马「古王城之广场」（forum of the ancient city of kings），
  中央喷泉、副王宫踞北侧，Martin Paz 于此挥独立黑旗。book The Pearl of Lima，real，region Peru。
- **Saint-Pierre-Miquelon**（TN×5 distinct，单指）：纽芬兰外法属群岛，Viking 号启航港。
  book Ticket No. 9672，real，region North Atlantic。恰达 ≥5 门（TN-001-081/011-072/013-027/013-046/020-016）。

**剔除**（possessive_scan + feature_scan 复扫）：
person（Mac-Nab FC×28、Feofar-Khan MS×21、Tio-King/Ki-Tsang/Pan-Chao/Cha-Coua ASC、
Milne-Edwards、Jose-Antonio DSCF×8、Kara-Tete/Kai-Koumou SC）、ship（Jeune-Hardie WAI×10）、
报名（Morgen-Blad TN×5，挪威 Morgenbladet 报）、title（Governor-General）、demonym（Anglo-Saxon(s)）、
已建片段（Cape of Good→cape-of-good-hope、Behring's Straits→behring-strait、North-West→north-west-passage）；
feature_scan 复扫仍仅 Cape Mandible 净4（SI 翻印不加成）/Long Island NY 净4 多指/West Passage 片段/
Bay Company 组织，皆不达门（俱 DEFERRED）。

**关键分岔**：new_candidates=2<3 → **discover_streak_low 2→3**（三连低产，达 type_close_streak=3）
→ **R231 = §3(2) CLOSE+SCN28 place→event 评估**。place 是否真饱和于 R231 判定；若 CLOSE，
Plaza-Mayor/Saint-Pierre-Miquelon 两待建项随评估复核（或作 place 收尾建页后再切 event）。

无建页：pages: []，registry total 恒 1488，place 恒 420，unknown 恒 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =2（本轮末方 →3）| 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| **4** | **SCN28-zombie（queue(place)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | 未达 |

## 页面处理记录

本轮为 discover，无建页。发现候选入队 `logs/butler/queue.md`（R230 SCN28 block）：

| 建序 | 候选 | slug | distinctPN | book | rof | region | 状态 |
|------|------|------|-----------|------|-----|--------|------|
| 1 | Plaza-Mayor | plaza-mayor | PL×14 | The Pearl of Lima | real | Peru | 待建（R231 评估后）|
| 2 | Saint-Pierre-Miquelon | saint-pierre-miquelon | TN×5 | Ticket No. 9672 | real | North Atlantic | 待建（R231 评估后）|

- 建前 exact-slug 复核：plaza-mayor / saint-pierre-miquelon 皆 ABSENT（pages.json 无子串、无 label 命中）。
- Plaza-Mayor 逐句核 PL 全书单指利马中心广场，无同名异指。
- Saint-Pierre-Miquelon：bare「Saint-Pierre」含 FEM-019-026（Bernardin de Saint-Pierre 作家，剔）；
  全称「Saint-Pierre-Miquelon」TN×5 皆指群岛/启航港，单指。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：本轮无建页，候选 distinctPN 均经 gather.py word-boundary 核。✔（建页时逐句 strict）
- **G2 段落 ≤400 字**：无建页，N/A。
- **G3 ≥5 distinct PN**：两候选均达（14/5）；<5 者（Cape Mandible/Long Island 等）DEFERRED。✔
- **G4 脚本建页**：本轮无建页；建页时经 add_page.py。✔（N/A）
- **schema 一致**：无建页，N/A。
- **registry 一致**：total 1488 place 420 unknown 0 恒定；无新页故仅 Robur PARK（未跑 build_registry，无写入）。✔
- **查重充分**：possessive_scan slugify 去重 + feature_scan 复扫 + exact-slug 手核。✔
- **单指核**：Plaza-Mayor（PL 逐句）、Saint-Pierre-Miquelon（TN 逐句，剔 FEM 作家）。✔
- **排除检查**：提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R231 起始计数）

| 字段 | R230 起始 | R231 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 230 | 231 |
| type_round | 201 | 202 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 0（SCN28 reset）|
| discover_streak_low | 2 | 3（new_candidates=2<3，+1）|
| rounds_since_last_corpus_discover | 166 | 167 |
| last_updated_round | 230 | 231 |

## 遗留问题

1. **place 页数 420**：本轮无建（discover）。registry 全库 1488，unknown 0。
2. **R231 = §3(2) CLOSE+SCN28 评估（关键）**：discover_streak_low=3 达 type_close_streak。
   R231 首匹配 §3(2)：评估 place 是否饱和 → 若 CLOSE，切 event（type_queue 首项）；
   Plaza-Mayor/Saint-Pierre-Miquelon 两待建随评估复核。**注意**：三连低产（R223/R227/R230 各 2 净新）
   非零产——每轮仍掘出真净新地名，故 CLOSE 评估须权衡「掘尽 vs 边际递减」；若判未尽可 override 续建两队列项再评。
3. **HK-discover-possessive-hyphen-toponym-blindspot〔R227〕已由 possessive_scan.py 系统化闭合**：
   本轮撇号/连字符 toponym 全扫，无遗漏真净新（除已入队 2 项）。四扫（discover3/single_toponym/
   feature_scan/possessive_scan）now 覆盖：多词专名/单词地名/多词特征/撇号连字符。
4. **HK-place-apostrophe-label-slug-divergence〔R229〕**：建 Plaza-Mayor/Saint-Pierre-Miquelon 时，
   连字符 label 无撇号，slugify 天然对齐 id（plaza-mayor/saint-pierre-miquelon），无分歧风险。
5. **HK-dupcheck-bareterm-vs-slug〔R223〕**：本轮续遵，bare gather ≥5 必 exact-slug 复核。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮无建页。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=166→167（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；
    lancaster-sound〔同指 lancaster-strait〕；tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait
    （bare-term 净新但 slug 已建）；cape-mandible〔净4〕/long-island〔NY 净4〕/Wilmington/Catawba/Cape Hatteras/
    Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/
    Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot〔已闭合〕、HK-place-apostrophe-label-slug-divergence、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、
    featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
