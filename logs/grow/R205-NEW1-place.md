---
round: 205
date: 2026-07-17
type_round: 176
phase: "2.1"
current_type: place
gene: NEW1
pages: [guamini]
result: success
---

# GROW 2.1-B · R205 · NEW1 · place — 建 Guamini（SC 阿根廷 Pampas 河/盐湖地带，净 solid 9 单指；Sierra Ventana 近旁，Glenarvan 队解渴枢纽）

## 执行摘要

Phase 2.1-B place 广度扩张第 176 轮（type_round 176）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10〔R204 EVV5 已 RESET〕、since_discover=3<10、queue(place)=3>0、
stub%=0 → §3(7)）。

取 R201 discover 队列**建序 3** **Guamini**（SC）。建前 pages.json 子串（guamini）+
`the-` 前缀双查皆 NEW。**单指无混淆**：全库 10 distinctPN 全指 SC 阿根廷 Pampas
Guamini 河/盐湖地带，无同名异指。**净 9 distinct solid SC PN**（剔 SC-018-006
分队泛述，未含 Guamini 主指）：
- **SC-018-001**：Lake Salinas 收束与 Sierras Ventana/Guamini 相连的潟湖串。
- **SC-018-015**：Paganel 谙 37th parallel 与 river Guamini 及全 Pampas。
- **SC-018-025**：若 Guamini 失望则南趋 80 mile 外 Sierra Ventana。
- **SC-018-054**：Thalcave 谓 Guamini 若干涸方言绝望。
- **SC-018-075**：Guamini 岸为四野猎物总汇。
- **SC-019-001**：Guamini 之水静流如大理石面上油。
- **SC-020-001**：七时抵 Guamini 岸围栏。
- **SC-020-004**：Guamini 之水助消化。
- **SC-020-007**：离 Guamini 后气温显变，旅人大慰。

place 计数 402→403，registry total 1470→1471，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Argentina、book In Search of the Castaways、aliases=[river Guamini]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R204 RESET）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；queue=3 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Carmen / Rio Colorado（2 项）。R207 建毕队列罄 → SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| guamini | eDAIoc | In Search of the Castaways | real | Argentina | 9 | 阿根廷 Pampas 河/盐湖地带；Sierra Ventana 近旁；单指无混淆 |

- **guamini**：9 distinct solid SC PN（单指）；aliases [river Guamini]。链 Pampas/Sierra Ventana 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 SC Guamini；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1471 place 403 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（guamini）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R206 起始计数）

| 字段 | R205 起始 | R206 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 205 | 206 |
| type_round | 176 | 177 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 141 | 142 |
| last_updated_round | 205 | 206 |

## 遗留问题

1. **place 页数 403**：本轮 +1（Guamini）。registry 全库 1471，unknown 0。
2. **下轮 R206 = NEW1**：since_evv5=1<10、since_discover=4<10、queue(place)=2>0 → §3(7)。
   建 **Carmen**（carmen，SC×7，巴塔哥尼亚 Rio Negro 口镇），建前 pages.json 子串 +
   `the-` 双查，**须核同名异指**（Carmen 恐跨作品/人名），仅采单指 solid，抽样 ≥5。
3. **R206+ 建序**：Carmen → Rio Colorado（2 项），R207 建毕队列罄 → SCN28。
4. **同名异指剔除**：本轮无（Guamini 单指）；承 Rio Negro/New Georgia/Far West 纪律。
   下轮 Carmen 须警惕人名/异地同名。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=141→142（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
