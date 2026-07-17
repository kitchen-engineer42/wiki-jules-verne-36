---
round: 202
date: 2026-07-17
type_round: 173
phase: "2.1"
current_type: place
gene: NEW1
pages: [rio-negro]
result: success
---

# GROW 2.1-B · R202 · NEW1 · place — 建 Rio Negro（EHLA 亚马逊大支流，净 solid 14 EHLA-referent；剔 4 SC 巴塔哥尼亚同名）

## 执行摘要

Phase 2.1-B place 广度扩张第 173 轮（type_round 173）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、since_discover=0<10、queue(place)=5>0、stub%=0 → §3(7)）。

取 R201 discover 队列**建序 1** **Rio Negro**（EHLA）。建前 pages.json 子串（negro）+ `the-` 前缀双查皆 NEW。

**同名异指剔除纪律（承 Far West/New Georgia）**：全库 "Rio Negro" 44 distinctPN 跨两指——
- **EHLA 亚马逊 Rio Negro**（本页 referent，40 PN）：亚马逊最著支流，Manaos 汇流，The Giant Raft/jangada 顺流之河。
- **SC 巴塔哥尼亚 Rio Negro**（4 PN）：南美巴塔哥尼亚河——**异指，剔除**（净<5，不单独建）。

本页仅采 EHLA 亚马逊 referent，**净 14 distinct solid EHLA PN**（远超门）：
- **EHLA-018-020**：亚马逊最著支流。
- **EHLA-005-023**：Brazil frontier 至 Manaos 汇 Rio Negro，主流名 Solimaës。
- **EHLA-021-003**：Favella 1645 发现，源出 Popayan 省心，通 Orinoco。
- **EHLA-018-039**：raft 将抵 Rio Negro 口、Amazones 省会前。
- **EHLA-022-053**：raft 斜渡 Amazon（Rio Negro 倍其流），趋支流 embouchure。
- **EHLA-022-057**：raft 入 Rio Negro 黑水，近 cecropias 崖。
- **EHLA-026-017**：三人登 Rio Negro 岸赴镇。
- **EHLA-021-002**：Manaos 踞 Rio Negro 左岸。
- **EHLA-021-001**：距 Belem 420 leagues、Rio Negro 口 10 miles。
- **EHLA-022-055**：jangada 渡 Rio Negro 口上，入左岸大湾流。
- **EHLA-005-045**：Rio Negro 岸今仅少数混血，昔 24 族居。
- **EHLA-021-006**：Manaos 旧名 Moura / Barra de Rio Negro。
- **EHLA-005-034**：Orellana 十六世纪 descended Rio Negro，1540 抵主河。
- **EHLA-005-041**：汽船经 Tapajoz/Madeira/Rio Negro/Purus 上溯。

place 计数 400→401，registry total 1468→1469，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Amazon Basin、book Eight Hundred Leagues on the Amazon、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；queue=5 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Wimerra / Guamini / Carmen / Rio Colorado（4 项）。R206 建毕队列罄 → 再 SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| rio-negro | XOw23s | Eight Hundred Leagues on the Amazon | real | Amazon Basin | 14 | 亚马逊最著支流；剔 4 SC 巴塔哥尼亚同名异指 |

- **rio-negro**：14 distinct solid EHLA PN（剔 4 SC）；aliases []。链 Manaos/Amazon 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且 VVV=EHLA 亚马逊 referent；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：14 solid（EHLA referent，剔 4 SC 同名异指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1469 place 401 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（negro）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R203 起始计数）

| 字段 | R202 起始 | R203 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 202 | 203 |
| type_round | 173 | 174 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 138 | 139 |
| last_updated_round | 202 | 203 |

## 遗留问题

1. **place 页数 401**：本轮 +1（Rio Negro）。registry 全库 1469，unknown 0。
2. **下轮 R203 = NEW1**：since_evv5=9<10、since_discover=1<10、queue(place)=4>0 → §3(7) NEW1。
   建 **Wimerra**（wimerra，SC×11，澳洲 Victoria 河/地区），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid。
3. **R203+ 建序**：Wimerra → Guamini → Carmen → Rio Colorado（4 项），R206 建毕队列罄 → SCN28。
4. **EVV5 逼近**：since_evv5=8→9，**R204 = EVV5**（§3(1b)，since_evv5 达 10）——place schema 全库反思，非建页。届时暂停广度 1 轮。
5. **同名异指剔除**：本轮 +Rio Negro（剔 4 SC 巴塔哥尼亚）；承 Far West/New Georgia 纪律。
6. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=138→139（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：17+ place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）；SC 巴塔哥尼亚 Rio Negro 并入 EHLA 页。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
