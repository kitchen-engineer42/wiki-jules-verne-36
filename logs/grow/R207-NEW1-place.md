---
round: 207
date: 2026-07-17
type_round: 178
phase: "2.1"
current_type: place
gene: NEW1
pages: [rio-colorado]
result: success
---

# GROW 2.1-B · R207 · NEW1 · place — 建 Rio Colorado（SC 巴塔哥尼亚 37th-parallel 河，净 solid 8 单指；剔 3 AWED 美 Colorado + 1 DSCF + 1 RC 同名异指）——R201 队列建罄

## 执行摘要

Phase 2.1-B place 广度扩张第 178 轮（type_round 178）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、since_discover=5<10、queue(place)=1>0、stub%=0 → §3(7)）。

取 R201 discover 队列**建序 5（末项）** **Rio Colorado**（SC）。建前 pages.json 子串
（colorado）+ `the-` 前缀双查皆 NEW。**同名异指剔除纪律（承 Rio Negro/Far West）**：
全库 "Colorado" 13 distinctPN 跨四作——
- **SC 巴塔哥尼亚 Rio Colorado**（本页 referent，8 PN）：越 37th parallel、Rio Negro 姊妹河。
- **AWED 美 Colorado**（3 PN）：环游八十日途经美国 Colorado——**异指，剔**。
- **DSCF**（1 PN）/ **RC**（1 PN）：异指，剔。

本页仅采 SC referent，**净 8 distinct solid SC PN**：
- **SC-008-076**："Go up the Rio Colorado instead"。
- **SC-010-033**：Rio Negro/Rio Colorado 支流被 37th parallel 切，漂瓶可能路径。
- **SC-010-043**：Paganel 路线经 Neuquem 与 Rio Colorado 下 Pampas。
- **SC-013-015**：Colorado 谷入暮，安第斯东坡夜幕。
- **SC-016-015**：距 Rio Colorado 越 37th parallel 处 90 mile（约两日）。
- **SC-016-074**：Colorado 与 Rio Negro 间部落，欧人为奴。
- **SC-021-057**：法人被拖至 Colorado 岸后逃脱。
- **SC-032-011**：巴塔哥尼亚 Rio Colorado/Rio Negro 注海于荒寂之地。

place 计数 404→405，registry total 1472→1473，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Argentina、book In Search of the Castaways、aliases=[Colorado]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=5<10；queue=1 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> **队列建罄**：R201 discover 5 项（Rio Negro/Wimerra/Guamini/Carmen/Rio Colorado）全建毕。
> **下轮 R208 = SCN28-zombie**（queue(place)==0 → §3(4)）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| rio-colorado | 4MWSuw | In Search of the Castaways | real | Argentina | 8 | 巴塔哥尼亚 37th-parallel 河，Rio Negro 姊妹河；剔 3 AWED 美 Colorado + 1 DSCF + 1 RC |

- **rio-colorado**：8 distinct solid SC PN（剔 5 异指）；aliases [Colorado]。链 Rio Negro/Neuquem/37th parallel 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且 VVV=SC 巴塔哥尼亚 referent；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（SC referent，剔 5 AWED/DSCF/RC 同名异指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1473 place 405 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（colorado）+ `the-` 前缀双查。✔
- **同名异指剔除**：剔 3 AWED（美国 Colorado）+ 1 DSCF + 1 RC。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R208 起始计数）

| 字段 | R207 起始 | R208 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 207 | 208 |
| type_round | 178 | 179 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 143 | 144 |
| last_updated_round | 207 | 208 |

## 遗留问题

1. **place 页数 405**：本轮 +1（Rio Colorado）。registry 全库 1473，unknown 0。
2. **下轮 R208 = SCN28-zombie**：queue(place)==0 → §3(4) 触发。**非建页**，全库掘 place
   toponym 补种。承 **premature-saturation 纪律（memory rule）**：不得凭 queue 空断言饱和，
   须全库 sentence_index 重扫（SC 巴塔哥尼亚长尾、EHLA 亚马逊、FWB 非洲、ACH 极地等未掘脉），
   净新 ≥3 buildable 方入队；若 new_candidates<3 则 discover_streak_low+1。
3. **R201 队列已罄**：5 项全建（Rio Negro/Wimerra/Guamini/Carmen/Rio Colorado）。
4. **同名异指剔除**：本轮 Rio Colorado 剔 5（3 AWED 美 Colorado + 1 DSCF + 1 RC）；
   承 Rio Negro/New Georgia/Far West 纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=143→144（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）；AWED 美 Colorado/DSCF/RC 同名并入或剔除。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
