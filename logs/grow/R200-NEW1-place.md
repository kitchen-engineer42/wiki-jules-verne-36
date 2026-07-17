---
round: 200
date: 2026-07-17
type_round: 171
phase: "2.1"
current_type: place
gene: NEW1
pages: [coppermine-river]
result: success
---

# GROW 2.1-B · R200 · NEW1 · place — 建 Coppermine River（ACH+FC 北美极地大河，净 solid 10 单指；R197 队列末项，建罄 → R201 SCN28）

## 执行摘要

Phase 2.1-B place 广度扩张第 171 轮（type_round 171）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、since_discover=2<10、queue(place)=1>0、stub%=0 → §3(7)）。

取 R197 discover 队列**建序 4（末项）** **Coppermine River**（FC 主 + ACH）。
建前 pages.json 子串双查（copper 无既有页），`the-`/coppermine/copper-mine 变体皆 NEW（承 R198 教训）。

**单指无混淆**（异于 New Georgia/Far West）：全库 "Coppermine" 10 distinctPN 全指同一北美极地大河
（Coronation Gulf 入海），无同名异指。**净 10 distinct solid PN**（远超门）：
- **FC-010-007**：Hobson 决降 Coppermine 谷，流入 Coronation Gulf。
- **FC-010-011**：territory 曾未知，Hudson's Bay Company agents 开拓。
- **FC-010-019**：Hearne 苦战十九月，1772-07-13 发现，循至河口。
- **FC-008-041**：自湖东北下 Coppermine 达岸最短路。
- **FC-007-004**：诸溪多为 Mackenzie/Coppermine 支流，南向北流。
- **FC-010-033**：Hobson 须更北进，抵河口仅部分行程。
- **FC-010-031**：近北冰洋谷渐宽。
- **FC-011-002**：湾西角开 Coppermine 口，东有 Bathurst Inlet。
- **FC-002-023**：Hearne 1770 向 Polar Sea 发现 Coppermine，列 Franklin/Mackenzie 探险序。
- **ACH-014-023**：Richardson 七十岁赴加拿大，溯 Coppermine 至 Polar Sea。

place 计数 399→400，registry total 1467→1468，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Arctic North America、book The Fur Country、aliases=[Coppermine]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；queue=1 末项消费 | 否 |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> **本轮建毕 R197 队列罄**（chimneys DUPLICATE 剔 + corral/new-georgia/coppermine-river 3 建）。
> **下轮 R201 queue(place)=0 → §3(3)（queue<10）&§3(4)（zombie）触 SCN28 discover。**

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| coppermine-river | tpYUBY | The Fur Country | real | Arctic North America | 10 | 北美极地大河，Coronation Gulf 入海；Hearne 1772 发现；单指无混淆 |

- **coppermine-river**：10 distinct solid PN（FC 主 + ACH，单指）；aliases [Coppermine]。链 the-fur-country。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指北美极地 Coppermine River；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：10 solid（单指，无同名异指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1468 place 400 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（copper）+ `the-`/coppermine/copper-mine 变体双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R201 起始计数）

| 字段 | R200 起始 | R201 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 200 | 201 |
| type_round | 171 | 172 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 136 | 137 |
| last_updated_round | 200 | 201 |

## 遗留问题

1. **place 页数 400（里程碑）**：本轮 +1（Coppermine River）。registry 全库 1468，unknown 0。
2. **下轮 R201 = SCN28 discover（队列耗尽）**：R197 补种 4 项本轮建齐（chimneys DUPLICATE 剔），queue(place)=0
   → §3(3)&§3(4) 触发。须表层 toponym 复扫补种，目标净新 ≥3。**每候选须 pages.json 子串 + `the-` 前缀双查**（承 HK-dupcheck-the-prefix-blindspot）。
3. **R201 discover 矿脉预备**：承 R197/R199——MI 自然地理近饱和、人居设施（chimneys 既存/corral 已建）近罄，
   discover 宜向 **FC/AM/AWED/ACH 极地-铁路长尾**扩散。候选池：Coronation Gulf（FC，本页已引 mouth）、
   Bathurst Inlet（FC-011-002）、Mackenzie〔river〕（FC 密，待查 distinctPN 与既有页）、Great Slave Lake、
   Fort Confidence、AWED 铁路沿线站点、AM 南极 toponym 长尾。均须 ≥5 solid + 双查。
4. **HK-dupcheck-the-prefix-blindspot**：R198–R200 均应用子串 + the- 前缀双查，无复现。PARK 记录。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
7. **corpus-discover 顺延**：since_corpus=136→137（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。since_evv5=6→7，逼近 10（R204 附近触 EVV5）。
9. **featured re-grade DEFERRED**：17+ place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
10. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Fort Enterprise/North·South Mandible/Reptile Point DEFER；
    Medicine Bow/Grant Lake/Prospect Plateau DEFER，Salt Lake/Serpentine/Omaha/Cape Bathurst 等 DUPLICATE 照旧。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
