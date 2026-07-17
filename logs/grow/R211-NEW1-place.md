---
round: 211
date: 2026-07-17
type_round: 182
phase: "2.1"
current_type: place
gene: NEW1
pages: [upper-amazon]
result: success
---

# GROW 2.1-B · R211 · NEW1 · place — 建 Upper Amazon（EHLA 亚马逊上游河域，净 solid 13 单指；Iquitos/Garral fazenda 摇篮，Eight Hundred Leagues on the Amazon 开篇流域）

## 执行摘要

Phase 2.1-B place 广度扩张第 182 轮（type_round 182）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、since_discover=2<10、queue(place)=2>0、stub%=0 → §3(7)）。

取 R208 discover 队列**建序 3** **Upper Amazon**（EHLA 主）。建前 pages.json 子串
（amazon）+ `the-` 前缀双查：既有 **amazon** 为父域（大河全流），upper-amazon 为**上游子域**
（Peru/Brazil 前沿），二者父/子域异指非碰撞，upper-amazon 本身 NEW。**净 13 distinct solid
EHLA PN**（远超门）：
- **EHLA-001-008**：水出自 Peru 森林，Torres 越界方入。
- **EHLA-001-018**：一旅者庆自大西洋岸抵上游终程。
- **EHLA-014-030**：Tabatinga 今为上游首府，1692 葡萄牙 Carmelites 建 Mission。
- **EHLA-003-002**：Iquitos 如盆地诸村由传教士建。
- **EHLA-003-018**：Garral 抵后 10 年 fazenda 成上游最富庄园。
- **EHLA-011-064**：变生时令上游诸 mission 备 escort。
- **EHLA-012-061**：Fragoso 为上游诸部落理发师入其镇。
- **EHLA-002-003**：上游森林卷尾猴 guariba 最奇。
- **EHLA-002-044**：巨 ficus 遍上游盆地。
- **EHLA-007-055**：貘（antas）于上游及支流岸近绝迹。
- **EHLA-016-072**：其沙洲为盆地最富龟场。
- **EHLA-005-044**：上游已灭诸部 Curicicurus/Sorimaos。
- **EHLA-007-137**：游走理发师沿岸村村服河民。
- **EHLA-039-021**：Ortega 无路返 Tijuco 遁上游 capitaes da mato 区。

place 计数 407→408，registry total 1475→1476，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Amazon Basin、book Eight Hundred Leagues on the Amazon、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；queue=2 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Celestial Empire（1 项）。R212 建毕队列罄 → SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| upper-amazon | K7K43n | Eight Hundred Leagues on the Amazon | real | Amazon Basin | 13 | 亚马逊上游子域；勿混父域 amazon；EHLA Iquitos/Garral 摇篮 |

- **upper-amazon**：13 distinct solid EHLA PN（单指）；aliases []。链 Iquitos/Tabatinga/Garral fazenda/Fragoso 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 EHLA 上游流域；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：13 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1476 place 408 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（amazon）+ `the-` 前缀双查；甄别父/子域（amazon vs upper-amazon）。✔
- **父/子域异指甄别**：upper-amazon（上游子域）≠ amazon（大河全流父域），非碰撞，各自指域。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R212 起始计数）

| 字段 | R211 起始 | R212 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 211 | 212 |
| type_round | 182 | 183 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 147 | 148 |
| last_updated_round | 211 | 212 |

## 遗留问题

1. **place 页数 408**：本轮 +1（Upper Amazon）。registry 全库 1476，unknown 0。
2. **下轮 R212 = NEW1**：since_evv5=7<10、since_discover=3<10、queue(place)=1>0 → §3(7)。
   建 **Celestial Empire**（celestial-empire，ASC×29，即中国），建前 pages.json 子串 +
   `the-` 双查，抽样 ≥5 solid，region Asia，real；注洲级 Asia 综述 HOLD 但 Celestial Empire=国家实体可建。
3. **R212 建毕队列罄**：R208 队列 4 项全消费 → R213 = SCN28（queue==0 zombie 或 since_discover 触发）。
4. **同名/父子域异指剔除**：本轮甄别 upper-amazon≠amazon（子/父域）；承 Rio Negro/Arctic 纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=147→148（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
