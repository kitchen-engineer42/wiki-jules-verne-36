---
round: 212
date: 2026-07-17
type_round: 183
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 8
---

# GROW 2.1-B · R212 · SCN28 · place — Celestial Empire 判 DUPLICATE 后队列罄触发 zombie discover；全库重扫得 8 净新地名，place 未饱和

## 执行摘要

Phase 2.1-B place 第 183 轮（type_round 183）。R212 起始决策机 §3 本为 **NEW1**
（since_evv5=7<10、since_discover=3<10、queue=1>0、stub%=0 → §3(7)），拟建队列末项
**Celestial Empire**。建前查重发现 **Celestial Empire=China 别称**，同一真实指称；既有
**china**（ASC real，East Asia）已覆盖**同书同域**（gather：42 distinct 全指 China 国，
ASC×14 主）。建之即**重复**（承 chimneys R198 DUPLICATE 纪律），弃建，队列罄。

队列罄 → §3(4) **SCN28-zombie** 触发。遵「饱和前须全库重扫」记忆律，运行
`discover3.py` 扫全 968 sentence_index，person-lead（Captain/Major/Lord/…）+ 既有
slug/label/alias + `the-` 前缀过滤后，取 **≥6 distinct PN 且单作品集中 ≥6** 的净新地名。
得 **8 项净新 place 候选**（new_candidates=8≥3 → place **未饱和**，discover_streak_low 保持 0）。

抽样核实 4 强候选（入建序）均为确凿单指地名：
- **Uzun Ada**（ASC×10）：里海东岸港，大 Transasiatic 铁路西端起点（ASC-001-007/003-042）。real。
- **Saville Row**（AWED×8）：伦敦 Burlington Gardens 街，Fogg 宅 No.7，Sheridan 1814 卒此（AWED-001-002/010/012）。real。
- **Villa Rica**（EHLA×8）：巴西钻石区矿镇兼监狱，Joam Dacosta 越狱地（EHLA-019-031/035/020-007/023-002）。real。
- **Coal Town**（UC×7）：Loch Katrine 东岬地下矿村，电力照明（UC-010-004/005/009/011）。fictional。

备选 4（待下轮 SCN28 复核 solid）：Montgomery Street（GM×10）/ Kamtchatka Current（FC×7）/
Pleasant Garden（MW×7）/ North Carolina（MW×7+FF×6，双书需逐句核同指）。

本轮**不建页**（SCN28 勘探轮）。place 计数恒 408，registry total 1476，unknown 0。

## 决策矩阵（R212 起始 → 实际执行 SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1<10 | （本可触发）|
| **4** | **SCN28-zombie（queue==0）** | **Celestial Empire DUPLICATE 后 queue→0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | 否（无 buildable 候选）|

> R212 起始名义 NEW1，但唯一队列项 Celestial Empire 判 DUPLICATE，queue 归零 → §3(4)
> zombie，转 SCN28 全库重扫。避免空转，一轮内完成弃建+补池。

## 页面处理记录

| slug | 动作 | 结果 |
|------|------|------|
| celestial-empire | 弃建（DUPLICATE）| Celestial Empire=China 别称，既有 china 已覆盖同书同域；queue 归零 |
| （无新建）| SCN28 discover | 8 净新 place 候选入队，建序 1–4 抽样确认 solid |

## EXIT-GATE 检查

- **G1–G4**：本轮不建页，无 PN grounding/段长/建页门适用。✔（NA）
- **DUPLICATE 甄别**：Celestial Empire=China 同指，既有 china〔ASC〕已覆盖；gather 42 distinct 全指 China；弃建正确。✔
- **饱和前重扫**：discover3.py 全 968 sentence_index，非仅凭 queue 推断；得 8 净新 → 未饱和。✔（满足记忆律）
- **person-lead 过滤**：排除 Captain/Major/Lord/Lady/Mrs/Miss/Count/… 头衔人名。✔
- **查重充分**：8 候选 test -f 逐一核 NEW；discover3 已内嵌既有 slug/label/alias + the- 前缀过滤。✔
- **registry 一致**：total 1476 place 408 unknown 0；仅 Robur PARK（无新 alias 冲突→无重复误建）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R213 起始计数）

| 字段 | R212 起始 | R213 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 212 | 213 |
| type_round | 183 | 184 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 0（SCN28 RESET）|
| discover_streak_low | 0 | 0（new_candidates=8≥3）|
| rounds_since_last_corpus_discover | 148 | 149 |
| last_updated_round | 212 | 213 |

## 遗留问题

1. **place 页数 408**：本轮不建（SCN28）。registry 全库 1476，unknown 0。
2. **下轮 R213 = NEW1**：since_evv5=8<10、since_discover=0<10、queue(place)=4（新池）>0 → §3(7)。
   建 **Uzun Ada**（uzun-ada，ASC×10，里海东岸港/Transasiatic 西端），建前 pages.json 子串 +
   `the-` 双查，抽样 ≥5 solid，region Central Asia/Caspian，real。
3. **R213+ 建序**：Uzun Ada → Saville Row → Villa Rica → Coal Town（4 项），建毕再 SCN28 或转备选核。
4. **备选待核**：Montgomery Street/Kamtchatka Current/Pleasant Garden/North Carolina（后两 MW/FF 双书需逐句核同指）。
5. **Celestial Empire DUPLICATE**：已记 queue ✘；china 可后补 alias「Celestial Empire」（DEFER，避 Robur alias 类冲突，顺延 RFC 批审）。
6. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮不建。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=148→149（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**（North America/Central Asia/Central Africa 等大区综述不建）。
