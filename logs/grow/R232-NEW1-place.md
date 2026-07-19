---
round: 232
date: 2026-07-18
type_round: 203
phase: "2.1"
current_type: place
gene: NEW1
pages: [saint-pierre-miquelon]
result: success
---

# GROW 2.1-B · R232 · NEW1 · place — 建 Saint-Pierre-Miquelon（Viking 号启航法属群岛，TN 全书起点；CLOSE 覆盖轮之二）

## 执行摘要

Phase 2.1-B place 广度扩张第 203 轮（type_round 203）。R231 CLOSE 覆盖后 discover_streak_low=0，
决策机 §3 首匹配 **NEW1**（since_evv5=5<10；streak=0<3；since_discover=1<10、全局 queue≥10；
queue(place)=1>0 → §3(4) 否；stub=0 → §3(7)）。

取 R230 SCN28 队列**建序 2**（末项）**Saint-Pierre-Miquelon**（TN 主）。建前 exact-slug 复核
saint-pierre-miquelon ABSENT。**单指**：TN 全书 5 PN 皆指 Viking 号启航之法属群岛/Ole Kamp 末信落款地，
无同名异指（bare「Saint-Pierre」含 FEM-019-026 作家 Bernardin de Saint-Pierre，已剔——本页用全称 exact）。
label `Saint-Pierre-Miquelon`（连字符无撇号，slugify=id）。

**恰达门 5 distinct solid PN**（TN×5 全用，四节分配，含跨节复用）：

- **TN-001-081**：Ole Kamp 末信落款「Saint-Pierre-Miquelon, March 17th, 1862」。
- **TN-011-072**：Viking 号于末信所载之日离 Saint-Pierre-Miquelon。
- **TN-013-027**：离港约一月后（6月3日）彩票于 Iceland 西南 200 英里处被拾。
- **TN-013-046**：自 Viking 离港至丹麦船拾漂瓶间，狂风不辍（不可争之事实）。
- **TN-020-016**：Ole 获救后，被告知自末信（落款 Saint-Pierre-Miquelon）以来诸事。

**内容偏薄说明**：5 PN 皆以该地为「启航港/末信落款」之功能出现，无描述性地貌句。故严守 G1，
**不注入外部事实**（未称「off Newfoundland」——语料未明言；[[Newfoundland]] 链因无 PN 支撑而弃），
四节皆以在证句铺陈，Geography & Features 与 Connections 复用 TN-013-046/TN-013-027/TN-020-016
（distinct 计数仍为 5，达门）。链仅 [[Iceland]]（存）/[[Ticket No. 9672]]（存，work）。

place 计数 421→422，registry total 1489→1490，unknown 恒 0。
add_page 一次成型（rev LWA0xl，size 1985）；prose-gate awk 初 1 段 484 超（In the Narrative），
拆分后 0 超段。pn_validator strict ✓。real、region North Atlantic、book Ticket No. 9672、aliases=[]。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0（R231 覆盖复位）| 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| saint-pierre-miquelon | LWA0xl | Ticket No. 9672 | real | North Atlantic | 5 | Viking 号启航法属群岛；TN 全书单指；恰达门，严守 G1 不注外部事实 |

- **saint-pierre-miquelon**：5 distinct solid PN（TN 全用）；aliases []；label `Saint-Pierre-Miquelon`。链 Iceland/Ticket No. 9672。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该群岛；未注入未证外部事实；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：初 1 段 484 超，拆分后 0 超段。✔
- **G3 ≥5 distinct PN**：恰 5 solid（TN），达门。✔
- **G4 脚本建页**：add_page.py 建（quality 自动 featured），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（两 wikilink）；label 无撇号无冒号；description 无冒号/撇号。✔
- **registry 一致**：total 1490 place 422 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug saint-pierre-miquelon ABSENT + label 无命中；bare Saint-Pierre 作家义已剔。✔
- **单指核**：TN 逐句确认全称指一法属群岛。✔
- **排除检查**：提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R233 起始计数）

| 字段 | R232 起始 | R233 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 232 | 233 |
| type_round | 203 | 204 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 168 | 169 |
| last_updated_round | 232 | 233 |

## 遗留问题

1. **place 页数 422**：本轮 +1（Saint-Pierre-Miquelon）。R230 队列（Plaza-Mayor + Saint-Pierre-Miquelon）全消费。
   registry 全库 1490，unknown 0。
2. **下轮 R233 = SCN28-zombie（CLOSE 复评起点）**：queue(place)==0（§3(4)）；since_evv5=6<10、streak=0<3、
   since_discover=2<10。这是 R231 覆盖后**首次 place discover 复评**：
   - 若 discover 仍掘 ≥3 净新 → streak 保持 0，place 确证未饱和，续 NEW1。
   - 若 <3 净新 → discover_streak_low 0→1 起**重新累积**；须再连续三轮低产（R233/后续两轮）方复触 §3(2) CLOSE 评估。
   本次覆盖已重置饱和时钟，故 place 最早于 streak 再达 3 时（约 R235+）才可能真正 CLOSE。
   R233 试：四扫（discover3/single_toponym/feature_scan/possessive_scan）全跑 + 已 DEFER 项复核是否有新证过门 +
   PL/TN/MI 等未细扫作品的地名 spot。
3. **HK-close-override-productive-discover〔R231 新〕**：streak 达阈但 discover 非枯竭（在手候选+新盲区证据）时，
   可覆盖 CLOSE、复位 streak 续建；覆盖非永久豁免，place 终饱和时如实 CLOSE。R233 复评据此执行。
4. **HK-discover-possessive-hyphen-toponym-blindspot / HK-place-apostrophe-label-slug-divergence**：本轮连字符 label 无撇号，无风险；possessive 盲区已由 possessive_scan.py 闭合。
5. **HK-dupcheck-bareterm-vs-slug〔R223〕**：本轮续遵（bare Saint-Pierre 作家义剔除即此教训应用）。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=168→169（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：place 页 quality=none 若干，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUP R198）；celestial-empire（DUP R212）；lancaster-sound〔同指 lancaster-strait〕；
    tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait（bare-term 净新但 slug 已建）；cape-mandible〔净4〕/
    long-island〔NY 净4〕/Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/
    Fort Enterprise/Turnagain/Fort Franklin/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot、HK-place-apostrophe-label-slug-divergence、HK-close-override-productive-discover、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
