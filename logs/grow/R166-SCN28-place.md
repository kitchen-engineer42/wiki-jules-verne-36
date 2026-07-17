---
round: 166
date: 2026-07-16
type_round: 137
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R166 · SCN28 · place — 深层 discover：西伯利亚（MS）+ 华属铁路城（ASC）宽扫，new_candidates=6 buildable，place 第 4 次证非饱和

## 执行摘要

Phase 2.1-B place 广度扩张第 137 轮（type_round 137）。决策机 §3 首匹配 **SCN28**
（since_evv5=6<10、streak=0<3；R161 补种批 4 建 1 DEFER 全消，净 buildable=0 → §3(3) 实务触发，
HK-queue-size-scope 情形：名义 since_discover=4<10 不满足，但净可建罄，按「exhaustively re-scan before
claiming saturation」纪律执行深层 discover）。**本轮不建页**。

**宽扫范围**：前批已深挖 ASC（Grand Transasiatic）中亚站（Samarkand/Kachgar/Tachkend/Douchak）。
本轮转向两条未测富矿：
- **Michael Strogoff（MS）西伯利亚 toponym**：Omsk/Tomsk/Irkutsk/Kolyvan/Krasnoiarsk/Perm/Ichim/
  Nijni-Novgorod/Ekaterenburg/Zabediero/Baikal/Yeniseisk/Tioumen。
- **ASC 华属段（长城内）城**：Sou-Tcheou/Lan-Tcheou/Tai-Youan/Khotan/Tchardjoui。

**HK-discover-existing-type-blindspot 主动规避**：全部候选建前比对 pages.json 的 label+aliases+id
（含拼写变体）。命中既有页 **13 个**（Omsk/Tomsk/Irkutsk/Kolyvan/Krasnoiarsk/Perm/Ichim/
Nijni-Novgorod/Merv/Bokhara/Pamir/Ekaterenburg/Zabediero），不入队。特别捕获两处拼写变体误报：
**Irkoutsk = 既有 irkutsk**、**Ekaterinburg = 既有 ekaterenburg**——若不查重会重复建页。

**净 new_candidates = 6 buildable**（≥3 → discover_streak_low 保持 0，place 未饱和第 4 次证实）：
Sou-Tcheou(8)、Lan-Tcheou(8)、Baikal(17)、Tai-Youan(6)、Yeniseisk(8)、Tioumen(5)。
below-gate 剔除：Khotan(3)、Tchardjoui(4)。

**建前复核预判（承 R165 Brindisi 纪律）**：Yeniseisk 8 hits 多为「governments of Yeniseisk,
Omsk...」省列举（enumeration-heavy），疑同 Brindisi 净 <5 solid；Tioumen 临界 5；Baikal 多处
「Lake Baikal provinces」区域引/省列举须严剔，且湖非城（参 Michigan/Colorado 湖河消歧先例）。
Sou-Tcheou/Lan-Tcheou 抽样确为主体确指（停站/访城/governor 电报），solid 稳。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=6 | 否 |
| 1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue_size<10 或 since_discover≥10）** | **净 buildable=0 实务触发（HK-queue-size-scope）** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| — | — |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 discover，无建页。候选入队 `logs/butler/queue.md`（R166 SCN28 块）。

| slug | distinctPN | 源 | region | 判定 |
|------|-----------|-----|--------|------|
| sou-tcheou | 8 | ASC | China | 入队，抽样 ≥5 solid（停站/访城/华战复兴）|
| lan-tcheou | 8 | ASC | China | 入队，抽样 ≥5 solid（重镇/抵站/governor 电报）|
| baikal | 17 | MS | Siberia | 入队，⚠ 建前严剔省列举+湖体消歧 |
| tai-youan | 6 | ASC | China | 入队，建前复核 solid 数 |
| yeniseisk | 8 | MS | Siberia | 入队，⚠ enumeration-heavy，疑 DEFER |
| tioumen | 5 | MS | Siberia | 入队，⚠ 临界，建前复核 |
| ~~khotan~~ | 3 | ASC | — | below-gate，不入队 |
| ~~tchardjoui~~ | 4 | ASC | — | below-gate，不入队 |

查重命中既有页（不建，HK-blindspot 规避）：Omsk/Tomsk/Irkutsk(=Irkoutsk)/Kolyvan/Krasnoiarsk/
Perm/Ichim/Nijni-Novgorod/Merv/Bokhara/Pamir/Ekaterenburg(=Ekaterinburg)/Zabediero — 13 个。

## EXIT-GATE 检查

SCN28 discover 轮无建页，EXIT-GATE 仅核 G4 + 不变量：

- **G4 无 Write/Edit 建页**：本轮未建页，仅 Edit queue.md/grow_state.json/写 log。✔
- **I1 registry 一致**：未动页面，registry 不变（total 1442 place 374 unknown 0）。✔
- **I2 grow_state 与 log 同步**：last_updated_round=167 与本轮末一致。✔
- **I3 查重充分**：全候选比对 label+aliases+id 含变体，捕获 2 处变体误报。✔
- **I4 candidate honest**：nominal count 附建前 re-vet 标注（Brindisi 纪律）。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（SCN28，grow_state 存 R167 起始计数）

| 字段 | R166 起始 | R167 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 166 | 167 |
| type_round | 137 | 138 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 4 | **0（RESET）** |
| discover_streak_low | 0 | 0（new_candidates=6≥3）|
| rounds_since_last_corpus_discover | 102 | 103 |
| last_updated_round | 166 | 167 |

## 遗留问题

1. **place 页数 374**：本轮 discover 无建。registry 全库 1442，unknown 0。
2. **下轮 R167 = NEW1**：since_evv5=6<10、since_discover=0<10、queue(place)>0 → §3(7) NEW1。
   建序：**Sou-Tcheou → Lan-Tcheou → Baikal(re-vet) → Tai-Youan(re-vet)**；Yeniseisk/Tioumen 建前严剔，未达门即 DEFER。
3. **place 未饱和第 4 次证实**：R161 找 5 净新、R166 又找 6 净新（西伯利亚 MS + 华属 ASC 两富矿）。
   HK-premature-saturation-claim 第四度被证伪。MS/ASC toponym 层仍有深度可挖。
4. **建前复核纪律延续（承 R165 Brindisi）**：Yeniseisk enumeration-heavy、Tioumen 临界、Baikal 湖体+省列举——
   均须建前严剔，nominal count 偏乐观，DEFER 而非勉强建页，守 5-solid 门。
5. **Baikal 特殊消歧**：湖非城；Michigan/Colorado 曾因湖河歧义 DEFER。Baikal 若净 solid 达门可建为 place（湖泊地理体），
   但须确认引注确指湖体而非「Baikal 省」区域泛指。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮无建页。
7. **EVV5 节奏**：since_evv5=5→6，约 R171 触发（since_evv5 达 10）。
8. **corpus-discover 顺延**：since_corpus=102→103（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义；本轮预判追加候选 Yeniseisk/Tioumen（待建前定）。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
