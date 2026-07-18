---
round: 227
date: 2026-07-18
type_round: 198
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 2
---

# GROW 2.1-B · R227 · SCN28 · place — 队列罄 zombie；多词特征扫 + Arctic 细扫；撇号/连字符地名盲区（Baffin's Bay/North-West Passage）补获 2 净新，streak 1→2

## 执行摘要

Phase 2.1-B place 第 198 轮（type_round 198）。R223 SCN28 队列 2 项（New-Berne/Raleigh）经 R224/R225
全消费，queue(place)==0 → §3(4) **SCN28-zombie** 触发。

承 R226 EVV5 计划「二/三字混合 toponym 正则或未建小特征细扫」，**新建 `/tmp/feature_scan.py`**：
多词地理特征正则（`{PRE} Name` / `Name {SUF}`，PRE/SUF 覆盖 Cape/Port/Fort/Lake/Bay/Sound/Strait/
Inlet/Channel/Passage 等），捕多词 toponym 短语，exact-slug（含 slugify + `the-`）去重。

**feature_scan 低产**：仅得 Bay Company〔Hudson's Bay Company 片段，组织〕、West Passage〔North-West Passage
片段〕、Cape Mandible〔MI×4+SI×1，但 SI-001-080 系 MI-043-081 逐字翻印 → 净 4<门〕、Long Island
〔NY 指 AWED×1+TTLU×3=4<门；ASC 二处系 Uzun Ada 译名已建〕——**均不达门或系片段/组织**。

**再运 single_toponym_scan.py 复核**：Lincoln/Franklin/Bathurst/Horn/Tabor/Victoria/Balloon/Serpentine/
Tsalal/Melville/Behring/Shark/Twofold/Tchad/Ural/Erie/Snowy/Beechey/Lancaster/Pamlico 逐一 exact-slug
**皆已建**；person/泛指剔除（Grant/Phina/Michael/Barnett/Bernouilli/Gourbi/Esquimaux/Falls/Union）。
Lincoln 岛内特征 spot 核：union-bay/prospect-heights/rocky-mountains/fort-reliance **均已建**。

**关键补获——撇号/连字符地名盲区**：三扫（discover3 多词、single_toponym 单词、feature_scan 多词特征）
**皆盲于含撇号/连字符的 toponym**（`Baffin's Bay`、`North-West Passage`、`Smith's Sound`——撇号/连字符
断正则）。改以 ACH/FC Arctic 语境**手动定向 gather**，得 **2 净新**（exact-slug 皆 absent）：

- **North-West Passage**（ACH×6+FC×4=10 distinct）：连接大西洋与太平洋的北极海路，ACH 全书主线
  （Behring 海峡 ↔ Baffin's Bay，McClure 发现）。real，region Arctic。
- **Baffin's Bay**（ACH×26 distinct）：格陵兰西侧北极海，捕鲸场，Forward 号北航必经。real，region Arctic。

**DEFER（同指/不达门）**：Lancaster Sound（ACH×5，但 **lancaster-strait 已建同指** Verne 异名，
HK-dupcheck-semantic-synonym → DEFER，RFC 批审评估 alias 回填）；Cape Mandible（净 4，SI 翻印）；
Long Island〔NY 净 4〕；Barrow Strait/Melville Bay/Wellington Channel（已建）；Fort Good Hope（2）/
Cape Hatteras（3）/Cape Dundas（4）/Wilmington（4）续 DEFER（<5）。

**得 2 净新 place 候选**（new_candidates=2<3 → discover_streak_low **1→2**；但**非饱和**，续 NEW1）。
第二次连续低产（R223=2、R227=2）；若下一 SCN28 续 <3 → streak=3 触 §3(2) CLOSE 评估。

本轮**不建页**。place 计数恒 418，registry total 1486，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10；全局 queue_size≥10（HK-queue-size-scope）| （回落）|
| **4** | **SCN28-zombie（queue(place)==0）** | **R223 队列全消费** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | 否（补池后 R228 再 NEW1）|

## 页面处理记录

| slug | 动作 | 结果 |
|------|------|------|
| （无新建）| SCN28 多词特征扫 + Arctic 定向 gather | 2 净新 place 候选入队（North-West Passage 建序 1、Baffin's Bay 建序 2）；撇号/连字符地名盲区补获 |

## EXIT-GATE 检查

- **G1–G4**：本轮不建页，无 PN grounding/段长/建页门适用。✔（NA）
- **饱和前重扫**：新建 feature_scan.py（多词特征）+ 复运 single_toponym_scan.py + Lincoln 岛内特征 spot 核
  + Arctic 手动定向 gather，逐候选 exact-slug 复核。捕获三扫共盲的撇号/连字符 toponym。✔（满足记忆律）
- **exact-slug 查重**：2 候选（north-west-passage/baffins-bay 含变体 the-/连字符）逐一 grep pages.json 皆 absent；
  bare-term 命中数仅作候选信号，须核实际 slug（承 HK-dupcheck-bareterm-vs-slug）。✔
- **同指剔除**：Lancaster Sound 认定 lancaster-strait 同指（Verne 异名），DEFER 不建（HK-dupcheck-semantic-synonym）。✔
- **翻印/混指剔除**：Cape Mandible 剔 SI-001-080（MI-043-081 逐字翻印）→ 净 4 不达门；Long Island 剔 ASC〔Uzun Ada〕。✔
- **person/泛指过滤**：排除 Grant/Phina/Michael/Barnett/Bernouilli〔人〕、Gourbi〔窝棚〕、Esquimaux〔族称〕、Union/Falls〔泛指〕。✔
- **registry 一致**：total 1486 place 418 unknown 0；仅 Robur PARK。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R228 起始计数）

| 字段 | R227 起始 | R228 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 227 | 228 |
| type_round | 198 | 199 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 0（SCN28 RESET）|
| discover_streak_low | 1 | 2（new_candidates=2<3）|
| rounds_since_last_corpus_discover | 163 | 164 |
| last_updated_round | 227 | 228 |

## 遗留问题

1. **place 页数 418**：本轮不建（SCN28）。registry 全库 1486，unknown 0。
2. **下轮 R228 = NEW1**：since_evv5=1<10、streak=2<3、since_discover=0<10、queue(place)=2>0 → §3(7)。
   建 **North-West Passage**（north-west-passage，ACH×6+FC×4=10 distinct，北极海路，Atlantic↔Pacific，ACH 主线），
   建前 pages.json 子串 + 连字符/`the-` 双查，抽样 ≥5 solid，region Arctic，real。
3. **R228+ 建序**：North-West Passage → Baffin's Bay（2 项）。建毕队列罄 → R230 SCN28。
4. **discover_streak_low=2（第二次连续低产）**：R223=2、R227=2。若 R230 SCN28 续 <3 → streak=3 触 §3(2)
   CLOSE 评估。下一 SCN28 试：撇号/连字符 toponym 专项正则（补本轮手动补获的盲区）；确认饱和则 CLOSE place → event。
5. **HK-discover-possessive-hyphen-toponym-blindspot**〔R227 新记〕：discover3/single_toponym/feature_scan 三扫
   皆盲于含撇号（Baffin's Bay/Smith's Sound）或连字符（North-West Passage）的 toponym，须手动定向补。并入 RFC 批审。
6. **HK-dupcheck-bareterm-vs-slug**〔R223〕：本轮续遵，Lancaster Sound 认定 lancaster-strait 同指。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮不建。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=163→164（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；lancaster-sound〔R227 同指 lancaster-strait〕；
    tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建）；cape-mandible〔净 4〕/long-island〔NY 净 4〕/
    Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/
    Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot〔新〕、HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、
    HK-dupcheck-bareterm-vs-slug、HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
