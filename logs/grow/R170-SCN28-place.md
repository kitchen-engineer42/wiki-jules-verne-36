---
round: 170
date: 2026-07-16
type_round: 141
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R170 · SCN28 · place — Yeniseisk/Tioumen 建前严剔 DEFER；深层 discover 开 FWB 非洲尼罗河富矿，new_candidates=5，place 第 5 次证非饱和

## 执行摘要

Phase 2.1-B place 广度扩张第 141 轮（type_round 141）。决策机 §3 首匹配 **SCN28**
（since_evv5=9<10、streak=0<3；R166 补种批消 3 建 + 1 DUPLICATE + 2 DEFER 全尽，净 buildable=0 →
§3(3) 实务触发，HK-queue-size-scope 情形）。**本轮不建页**。

**R166 余项建前严剔（承 Brindisi 纪律，两项 DEFER）**：
- **Yeniseisk DEFER**：净 clean solid TOWN=1（仅 MS-029-002「Yenisei 河入湖，town of Yeniseisk 上方」为城确指）；
  剔 002-021/003-002 省列举 + 003-065/017-002/017-025/018-007/026-002 五处「government/province of Yeniseisk」区域泛指。远低门。
- **Tioumen DEFER**：净 clean solid=3（013-005 road as far as Tioumen 近 Ural/013-030 22 July 抵/013-031 人口万级平时倍增）；
  剔 002-025/003-005 电报站列举。<5 门。

**深层 discover 转 FWB 非洲富矿**：前批 MS/ASC 西伯利亚·华属段渐尽，本轮转《Five Weeks in a Balloon》
中非·尼罗河源探险史 toponym（前所未深挖）+ SC 巴塔哥尼亚/澳洲城。

**feature-aware 双式查重（承 R169 Baikal 纪律强化）**：全候选比对 pages.json 时对 geographic-feature 类
双测「{name}」与「{feature}-{name}」两式。命中既有页 4 个：Zanzibar/Twofold Bay(=twofold-bay)/Gibraltar/Aden。

**净 new_candidates = 5 buildable**（≥3 → discover_streak_low 保持 0，place 未饱和第 5 次证实）：
Kazeh(16 FWB 商旅 rendezvous)、Gondokoro(8 FWB 白尼罗河北限)、Carmen(7 SC Carmen de Patagones)、
Tandil(8 SC；⚠ Sierra vs village 消歧)、Mozambique(11 多源；⚠ 海岸海峡泛指风险高)。
below-gate 剔除：Castlemaine(3)、Otago(0)。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=9 | 否 |
| 1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue_size<10 或 since_discover≥10）** | **净 buildable=0 实务触发（HK-queue-size-scope）** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| — | — |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 discover，无建页。候选入队 `logs/butler/queue.md`（R170 SCN28 块）。

| slug | distinctPN | 源 | region | 判定 |
|------|-----------|-----|--------|------|
| kazeh | 16 | FWB | East Africa | 入队，抽样 ≥5 solid（商旅 rendezvous/抵/返）|
| gondokoro | 8 | FWB | East Africa | 入队，抽样 ≥5 solid（白尼罗河探险北限点）|
| carmen | 7 | SC | Patagonia | 入队，建前复核（剔命名段）|
| tandil | 8 | SC | Patagonia | 入队，⚠ Sierra vs village 消歧 |
| mozambique | 11 | 多源 | — | 入队，⚠ 海岸/海峡泛指，大概率 DEFER |
| ~~castlemaine~~ | 3 | SC | — | below-gate，不入队 |
| ~~yeniseisk~~ | 8→1 | MS | — | **DEFER**：净 solid town=1（enum/province 泛指）|
| ~~tioumen~~ | 5→3 | MS | — | **DEFER**：净 solid=3（剔电报站列举）|

查重命中既有页（不建，feature-aware 双测规避）：Zanzibar/Twofold Bay(twofold-bay)/Gibraltar/Aden — 4 个。

## EXIT-GATE 检查

SCN28 discover 轮无建页，EXIT-GATE 仅核 G4 + 不变量：

- **G4 无 Write/Edit 建页**：本轮未建页，仅 Edit queue.md/grow_state.json/写 log。✔
- **I1 registry 一致**：未动页面，registry 不变（total 1445 place 377 unknown 0）。✔
- **I2 grow_state 与 log 同步**：last_updated_round=171 与本轮末一致。✔
- **I3 查重充分**：全候选 feature-aware 双式查重，命中既有 4 页规避。✔
- **I4 candidate honest**：nominal count 附建前 re-vet 标注（Brindisi/Baikal 纪律）；Yeniseisk/Tioumen 已建前严剔定 DEFER。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（SCN28，grow_state 存 R171 起始计数）

| 字段 | R170 起始 | R171 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 170 | 171 |
| type_round | 141 | 142 |
| rounds_since_last_evv5 | 9 | **10** |
| rounds_since_last_discover | 3 | **0（RESET）** |
| discover_streak_low | 0 | 0（new_candidates=5≥3）|
| rounds_since_last_corpus_discover | 106 | 107 |
| last_updated_round | 170 | 171 |

## 遗留问题

1. **place 页数 377**：本轮 discover 无建。registry 全库 1445，unknown 0。
2. **⚠ 下轮 R171 = EVV5**：since_evv5=10≥10 → §3(1b) EVV5 触发（周期质量/模板全库反思，无建页；EXIT-GATE 仅 G4+I1–I5）。
   自 R160 EVV5 起 place +7 页（Kachgar/Tachkend/Douchak/Concepcion/Sou-Tcheou/Lan-Tcheou/Tai-Youan），本轮 EVV5 复检模板稳定性。
3. **R172 起建序**：Kazeh → Gondokoro → Carmen(re-vet) → Tandil(disambig) → Mozambique(严剔，大概率 DEFER)。
4. **place 未饱和第 5 次证实**：R161 找 5、R166 找 6、R170 找 5 净新（FWB 非洲尼罗河 + SC 巴塔哥尼亚开新矿）。
   HK-premature-saturation-claim 第五度被证伪。FWB《Five Weeks in a Balloon》非洲探险史 toponym 层为新富矿。
5. **建前严剔纪律见效**：Yeniseisk（8→1）、Tioumen（5→3）——nominal count 严重高估 solid，enum/province 泛指须剔。
   续守 5-solid 门，DEFER 而非勉强建。
6. **feature-aware 查重纪律确立（承 R169 Baikal）**：geographic-feature toponym 查重双测「{name}」+「{feature}-{name}」，
   本轮规避 Twofold Bay(twofold-bay) 等潜在漏检。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮无建页。
8. **corpus-discover 顺延**：since_corpus=106→107（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3；待定 Mozambique。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
