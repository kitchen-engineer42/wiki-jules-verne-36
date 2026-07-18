---
round: 223
date: 2026-07-18
type_round: 194
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 2
---

# GROW 2.1-B · R223 · SCN28 · place — 队列罄 zombie；首度**单词地名扫**（补 discover3 盲区）；高频单词多已建，仅得 2 净新（New-Berne/Raleigh），streak 0→1

## 执行摘要

Phase 2.1-B place 第 194 轮（type_round 194）。R218 SCN28 队列 4 项（Montgomery Street/North Carolina/
Pleasant Garden/Kamtchatka Current）经 R219–R222 全消费，queue(place)==0 → §3(4) **SCN28-zombie** 触发。

遵「饱和前须全库重扫」记忆律，且承前诺「转单词地名扫」（多词 discover3 对单词 toponym 盲，
HK-discover-existing-type-blindspot）。**新建 `/tmp/single_toponym_scan.py`**：以地理上下文正则
（`Cape|Port|Mount|Lake|Gulf of|...|town of|village of|port of` + `X River|Island|Strait|Sound|...`）
扫全 sentence_index，捕单词 Capitalized toponym，排既有 id/label/alias + 停用词，取 ≥5 distinct。

**关键发现——place 库已高度成熟**：扫得高频单词 40+，逐一 exact-slug 复核后**绝大多数已建**：
Lincoln→lincoln-island、Franklin→mount-franklin、Bathurst→cape-bathurst、Horn→cape-horn、
Tabor→tabor-island、Victoria→victoria-island、Tsalal→**tsalal-island（已建！）**、Melville→melville-island、
Tchad→lake-tchad、Ural→ural-mountains、Baikal→lake-baikal、Erie→lake-erie、Pamlico→pamlico-sound、
Behring→behring-strait、Farewell→cape-farewell、Ontario→lake-ontario、Twofold→twofold-bay、
Snowy→snowy-river、Coronation→coronation-gulf、Verde→cape-verde、Bengal→bay-of-bengal、
Balloon→port-balloon、Shark→shark-gulf、Crespo→crespo-island、Paques→easter-island、
Serpentine→**serpentine-peninsula（已建！）**、Beechey→**beechey-island（已建！）**、Lancaster→**lancaster-strait（已建！）**。
person/非地名剔除：Torres〔EHLA 反派 302 hits〕、Barnett/Michael/Phina/Bernouilli〔人名〕、Grant〔探险家/General Grant 汽船〕、
Gourbi〔窝棚〕、Balloon/Falls/Union/Esquimaux/Indian〔泛指/族称〕。

**得 2 净新 place 候选**（new_candidates=2＜3 → discover_streak_low **0→1**；但仍**非饱和**，续 NEW1）：
- **New-Berne**（FF×11=11 distinct）：北卡 Neuse 河左岸真实港市，Ebba 停锚处，Healthful House 邻邑，
  Roch/Gaydon 绑架案枢纽（FF-001-005/002-009/003-036/004-023/013-022）。real，North Carolina。
- **Raleigh**（FF×2+MW×3=5 distinct）：北卡首府，内陆 150 英里，飞行器降落地、Strock 出发地
  （FF-001-006/004-016、MW-001-014/002-002/002-038）。跨 FF/MW 单指一城。real，North Carolina。

**池深信号**：单词扫首度低产（净 2）——多词≥7-PN 与单词高频 toponym 两池均近罄；余多为泛指/人名/已建。
discover_streak_low 首次累加（1）。若下两 SCN28 续 <3，streak→3 触 §3(2) CLOSE 评估。

本轮**不建页**。place 计数恒 416，registry total 1484，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=4<10；全局 queue_size≥10（HK-queue-size-scope）| （回落）|
| **4** | **SCN28-zombie（queue(place)==0）** | **R218 队列全消费** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | 否（补池后 R224 再 NEW1）|

## 页面处理记录

| slug | 动作 | 结果 |
|------|------|------|
| （无新建）| SCN28 单词地名扫 | 2 净新 place 候选入队（New-Berne 建序 1、Raleigh 建序 2）；高频单词多已建 |

## EXIT-GATE 检查

- **G1–G4**：本轮不建页，无 PN grounding/段长/建页门适用。✔（NA）
- **饱和前重扫**：新建单词地名扫全库 + 逐候选 exact-slug 复核（非仅凭 queue 或 bare-term gather），
  捕获 tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait 等「bare-term 净新但 slug 已建」的假阳。✔（满足记忆律 + HK-dupcheck 纪律）
- **exact-slug 查重**：2 候选 test -f（含 `the-` 前缀）逐一核 NEW；bare-term gather 不足恃，须核实际 slug 形态。✔
- **person-lead / 泛指过滤**：排除 Torres〔人〕、Grant〔人/汽船〕、Esquimaux/Indian〔族称〕、Balloon/Falls〔泛指〕。✔
- **registry 一致**：total 1484 place 416 unknown 0；仅 Robur PARK。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R224 起始计数）

| 字段 | R223 起始 | R224 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 223 | 224 |
| type_round | 194 | 195 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 4 | 0（SCN28 RESET）|
| discover_streak_low | 0 | 1（new_candidates=2<3）|
| rounds_since_last_corpus_discover | 159 | 160 |
| last_updated_round | 223 | 224 |

## 遗留问题

1. **place 页数 416**：本轮不建（SCN28）。registry 全库 1484，unknown 0。
2. **下轮 R224 = NEW1**：since_evv5=8<10、streak=1<3、since_discover=0<10、queue(place)=2>0 → §3(7)。
   建 **New-Berne**（new-berne，FF×11，北卡 Neuse 河港市，Healthful House 邻邑），建前 pages.json 子串 + `the-` 双查，
   抽样 ≥5 solid，region United States，real。
3. **R224+ 建序**：New-Berne → Raleigh（2 项）。建毕 R226 = EVV5（since_evv5 届 10）。
4. **discover_streak_low=1（首次）**：单词扫首度低产，place 库成熟。若 R226 后 SCN28 续 <3 两轮 → streak=3 → §3(2) CLOSE 评估。
   下一 SCN28 可试：(a) 二字/三字混合 toponym 正则；(b) 河流/海角/湖泊等未建小特征细扫；(c) 确认确已饱和后 CLOSE place → event。
5. **HK-dupcheck 纪律强化**：本轮验证 bare-term gather ≥5 ≠ 可建；**必须 exact-slug（含 the- 前缀）核实际页**。
   tsalal/serpentine/beechey/lancaster 皆 bare-term 净新但 slug 已建。记 HK-dupcheck-bareterm-vs-slug（并入 RFC 批审）。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮不建。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=159→160（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；tsalal-island/serpentine-peninsula/
    beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建，非候选）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/
    Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania/Wilmington/Catawba/Cape Hatteras DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug〔新〕、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
