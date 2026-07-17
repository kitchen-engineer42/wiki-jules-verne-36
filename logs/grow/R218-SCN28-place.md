---
round: 218
date: 2026-07-17
type_round: 189
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 4
---

# GROW 2.1-B · R218 · SCN28 · place — 队列罄触发 zombie；R212 备选复核 + 全库多词重扫得 4 净新地名，place 未饱和

## 执行摘要

Phase 2.1-B place 第 189 轮（type_round 189）。R212 discover 队列 4 项（Uzun Ada/Saville Row/
Villa Rica/Coal Town）经 R213–R217 全消费，queue(place)==0 → §3(4) **SCN28-zombie** 触发。

遵「饱和前须全库重扫」记忆律，双路补池：
1. **R212 备选复核**：4 项各 gather 逐句核 referent，均确凿单指净新地名（≥5 solid）→ 入建序。
2. **全库多词重扫**：discover3 逻辑（≥7 distinct、单作品集中 ≥7、person-lead + 既有过滤）。

得 **4 净新 place 候选**（new_candidates=4≥3 → place **未饱和**，discover_streak_low 保持 0）：
- **Montgomery Street**（GM×13+AWED×3=16 distinct）：跨作品单指真实旧金山主街，文中比作 Regent Street/Broadway（AWED-025-006/012/017、GM）。real，California。
- **North Carolina**（MW×11+FF×7+MI/TTLU 各1=20 distinct）：单指真实美州，首府 Raleigh，含 Pamlico Sound；Great Eyrie〔MW〕与 Healthful House〔FF〕所在州（FF-001-006/002-009/004-025）。real。
- **Pleasant Garden**（MW×16）：北卡 Morganton 近村，Great Eyrie 山脚，火山灰飘落地（MW-001-004/009/010）。real。
- **Kamtchatka Current**（FC×15）：白令海域洋流，与 Behring Current 交汇，牵动浮岛漂向（FC-025-025/026/031）。real。

**池深信号**：多词 ≥7-PN 净新地名池已薄——余 North America/Central Asia/Central Africa
皆洲/大区泛指（HOLD）。**单词地名**（Raleigh/Morganton/Wilmington/Pamlico/Behring 等）
为 discover3 多词正则盲区（承 HK-discover-existing-type-blindspot），留待下一 SCN28 单词扫。

本轮**不建页**。place 计数恒 412，registry total 1480，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0<10 | （本可触发）|
| **4** | **SCN28-zombie（queue==0）** | **R212 队列全消费** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | 否（补池后 R219 再 NEW1）|

## 页面处理记录

| slug | 动作 | 结果 |
|------|------|------|
| （无新建）| SCN28 discover | 4 净新 place 候选入队（备选复核 + 多词重扫），建序 1–4 |

## EXIT-GATE 检查

- **G1–G4**：本轮不建页，无 PN grounding/段长/建页门适用。✔（NA）
- **饱和前重扫**：R212 备选逐句核 + discover3 全库多词扫，非仅凭 queue 推断；得 4 净新 → 未饱和。✔（满足记忆律）
- **跨作品单指核**：Montgomery Street（GM/AWED 同指 SF 街）、North Carolina（MW/FF 同指美州）逐句确认单一真实指称，采全。✔
- **person-lead 过滤**：排除头衔人名；4 候选皆确凿 toponym/地理特征。✔
- **查重充分**：4 候选 test -f 逐一核 NEW；discover3 内嵌既有 slug/label/alias + the- 前缀过滤。✔
- **registry 一致**：total 1480 place 412 unknown 0；仅 Robur PARK。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R219 起始计数）

| 字段 | R218 起始 | R219 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 218 | 219 |
| type_round | 189 | 190 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 5 | 0（SCN28 RESET）|
| discover_streak_low | 0 | 0（new_candidates=4≥3）|
| rounds_since_last_corpus_discover | 154 | 155 |
| last_updated_round | 218 | 219 |

## 遗留问题

1. **place 页数 412**：本轮不建（SCN28）。registry 全库 1480，unknown 0。
2. **下轮 R219 = NEW1**：since_evv5=3<10、since_discover=0<10、queue(place)=4（新池）>0 → §3(7)。
   建 **Montgomery Street**（montgomery-street，GM×13+AWED×3，真实 SF 主街），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region United States/California，real。
3. **R219+ 建序**：Montgomery Street → North Carolina → Pleasant Garden → Kamtchatka Current（4 项）。
4. **多词池薄 + 单词盲区**：下一 SCN28 须转**单词地名扫**（改 discover3 正则容单词 toponym），否则多词池将过早报饱和（承 HK-premature-saturation-claim / HK-discover-existing-type-blindspot）。
5. **同名/跨作品单指**：Montgomery Street、North Carolina 跨作品同指，已核采全；承纪律。
6. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮不建。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=154→155（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**（North America/Central Asia/Central Africa 大区综述不建）。
