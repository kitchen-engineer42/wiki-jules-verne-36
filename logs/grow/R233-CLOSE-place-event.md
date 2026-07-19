---
round: 233
date: 2026-07-18
type_round: 204
phase: "2.1"
current_type: place
next_type: event
gene: CLOSE+SCN28
pages: []
new_candidates: 4
result: close
---

# GROW 2.1-B · R233 · CLOSE+SCN28 · place→event — 关闭 place（final 422）+ 首轮 event discover 播种

## 执行摘要

Phase 2.1-B **place 类型关闭轮**（type_round 204）。R231 CLOSE 覆盖后，R230 队列两候选
（Plaza-Mayor R231、Saint-Pierre-Miquelon R232）已建，队列罄 → R233 = SCN28-zombie（§3(4)）。
本轮为 **place discover 复评**（R231 覆盖时承诺的「build 2, then re-eval」）。

**复评结论：place 确证饱和**。四扫（discover3 多词专名 / single_toponym 单词地名 /
feature_scan 多词特征 / possessive_scan 撇号连字符）**全跑，0 净新地名**：

- **single_toponym**：高频候选 exact-slug 复核**皆已建**（Tchad→`lake-tchad`、Twofold→`twofold-bay`、
  Ural→`ural-mountains`、Gourbi→`gourbi-island`、Lincoln/Franklin/Tabor/Serpentine/Victoria/Melville/Behring/
  Tsalal/Bathurst/Barnett/Erie/Horn/Rocky 等既有页）——典型 HK-dupcheck-bareterm-vs-slug。
- **possessive_scan**：全 person（Mac-Nab/Feofar-Khan/Tio-King/Ki-Tsang/Pan-Chao/Cha-Coua/Milne-Edwards/
  Jose-Antonio/Kara-Tete/Kai-Koumou）、ship（Jeune-Hardie）、报名（Morgen-Blad）、title/demonym、已建片段。
- **feature_scan**：仅 Cape Mandible（净4）/Long Island（NY 净4），皆 <5 门，既 DEFERRED。

前三次 discover（R223/R227/R230）各 2 净新，皆因**新建扫描器逐次闭合新盲区**（单词→多词特征→撇号连字符）；
四盲区今全覆盖，复扫归零 = 真饱和信号（异于早前「每轮掘 2」的边际递减）。

**加速 CLOSE 裁定**：机械 discover_streak_low 仅 0→1（距 type_close_streak=3 尚需两空轮），
但饱和证据充分。经用户裁定 **「CLOSE place now」**——免磨两空 zombie 轮，据实关闭。

**§5.1 类型切换**（原子）：
- closed_types += {type:place, closed_at_round:233, final_count:422, evv6_score:null}
- type_queue: [event, character] → [character]（event 出队为 current）
- current_type: place → **event**
- type-level 计数复位：type_round=0、discover_streak_low=0、rounds_since_last_evv5=0
- 不变式 I1–I5 全过；place final_count 422 与 pages.json 对账一致；unknown 0。

**首轮 event discover 播种**（CLOSE+SCN28 之 SCN28 部分）：event **非 toponym**，须以
「事件锚点 pn_anchor」定位（非专名扫描）。播种 **4 net-new event 候选**（皆非既有 15 showcase event）：

| 建序 | event | slug | 作品 | 锚点线索 | PN 丰度 |
|------|-------|------|------|---------|---------|
| 1 | South Pole Attained | south-pole-attained | Twenty Thousand Leagues | Nemo 抵南极点植旗 | "South Pole" 35 PN |
| 2 | The Drifting Ice-Island | ice-island-drift | The Fur Country | 半岛断裂成浮冰岛漂流 | peninsula 75 / floating island 17 |
| 3 | The Comet's Collision | comet-collision | Off on a Comet | 地球被彗星掠走一隅成 Gallia | collision 124 / Gallia 156 |
| 4 | The Forward Mutiny | forward-mutiny | The Adventures of Captain Hatteras | Forward 号船员哗变弃船焚船 | "the Forward" 10 + mutiny 语境 |

new_candidates=4 ≥ type_close_new_candidate_min(3) → **productive discover**，discover_streak_low 保持 0。
既有 event 15 页（columbiad-launch/eighty-day-wager/giant-squid-attack/nemo-death/... 五大名著），
event 空间广阔（36 部作品仅 5 部有 event 覆盖）。

无建页：pages: []，registry total 恒 1490，place 恒 422，event 恒 15，unknown 0。

## 决策矩阵（CLOSE+SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| **2** | **CLOSE+SCN28（streak≥3）** | 机械 streak=0→复评饱和；用户裁定加速 CLOSE | **触发（加速）** |
| 3 | SCN28（queue<10 或 since_discover≥10）| — | — |
| 4 | SCN28-zombie（queue(place)==0）| queue(place)=0，本为 zombie discover；复评归零后升级 CLOSE | （并入）|

> **注**：机械路径下 R233 本为 §3(4) SCN28-zombie（streak 未达 3）。复评 0 净新确证饱和后，
> 经用户裁定加速执行 §3(2) CLOSE+SCN28（据实关闭，免磨 R234/R235 两空轮）。记
> **HK-close-accelerated-on-exhaustive-zero**：四扫全覆盖后归零 = 强饱和信号，可越 streak 计数提前 CLOSE。

## 页面处理记录

本轮为 CLOSE+discover，无建页。place 关闭存档 + event 队列播种（见上表 4 候选）。

## EXIT-GATE 检查（CLOSE 轮）

- **G1 每句 PN grounding**：无建页；event 候选锚点线索经 gather 初核，建时逐句 strict。✔（建页时）
- **G2 段落 ≤400 字**：无建页，N/A。
- **G3 ≥5 distinct PN**：place 复评 0 净新（confirm 饱和）；event 候选 PN 丰度充足，建时抽 ≥5 solid。✔
- **G4 脚本建页**：本轮无建页。✔（N/A）
- **schema 一致**：无建页；event 建时用 event-schema（四 H2 + book/location/pn_anchor）。N/A。
- **registry 一致**：total 1490 place 422 event 15 unknown 0 恒定（无写页）。✔
- **不变式**：I1–I5 全过；place final_count 422 对账一致。✔
- **查重充分**：place 四扫全跑归零；event 4 候选 exact-slug 皆 ABSENT，非既有 15。✔

## 六步状态机（CLOSE+SCN28，grow_state 存 R234 起始计数）

| 字段 | R233 起始 | R234 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | place | **event** |
| type_queue | [event, character] | [character] |
| closed_types | [work, org, tech] | [work, org, tech, **place(422)**] |
| current_round | 233 | 234 |
| type_round | 204 | 0（§5.1 复位）|
| rounds_since_last_evv5 | 6 | 0（§5.1 复位）|
| rounds_since_last_discover | 2 | 0（SCN28 reset）|
| discover_streak_low | 0 | 0（§5.1 复位 + productive discover）|
| rounds_since_last_corpus_discover | 169 | 170 |
| last_updated_round | 233 | 234 |

## 遗留问题

1. **place 类型关闭：final_count 422**（work 33 / organization 15 / technology 20 / **place 422** 四类型已闭）。
   registry 全库 1490，unknown 0。place 为迄今最大类型（占实体页绝大多数）。
2. **event 类型启动（type_round 0）**：既有 15 showcase event，广阔待扩（31 部作品无 event）。
   下轮 **R234 = NEW1**（event）：建 queue 建序 1 **South Pole Attained**（TTLU）。
   since_evv5=0<10、streak=0、queue(event)=4>0 → §3(7) NEW1。
3. **event 建页方法论（关键转变）**：event 非 toponym，dup/discover 逻辑须改「事件锚点」制：
   - 先 gather 事件核心动作/对象的分布，定 pn_anchor（事件中心段）。
   - 逐句核事件单指（同一事件，非泛指同类动作）。
   - 抽 ≥5 distinct solid PN（事件不同侧面：起因/经过/结果/后果/相关方）。
   - event-schema 专属字段：`book`、`location`、`pn_anchor`（详见 local/template/event-schema.md，建前须读）。
4. **HK-close-accelerated-on-exhaustive-zero〔R233 新〕**：四扫全覆盖后 discover 归零 = 强饱和信号，
   可越 streak 计数（未达 3）经裁定提前 CLOSE，免磨空 zombie 轮。与 HK-close-override-productive-discover〔R231〕
   成对：前者「非枯竭则覆盖 CLOSE 续建」，后者「四扫归零则加速 CLOSE」——判据皆为 discover 实产而非纯计数。
5. **HK-close-override-productive-discover〔R231〕**：本 CLOSE 系覆盖后复评所得，方法论已闭环。
6. **HK-discover-* / HK-dupcheck-* 系列**：place 阶段教训（bareterm-vs-slug、possessive-hyphen-blindspot、
   apostrophe-label-slug-divergence）转入 event 阶段继承适用（event slug 亦 kebab、亦须 exact-slug 复核）。
7. **散文门债**：37 页 >400（既有 DEFERRED），跨类型延续。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=169→170（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点**：Phase 2.1 关闭前须对 **每类型（含新闭 place）** 执行一次 EVV6 全库评审并回填
    closed_types[].evv6_score（现四类型皆 null）。
11. **featured re-grade DEFERRED**：place/event 页 quality 若干 none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积（place 存档）**：cape-mandible〔净4〕/long-island〔NY 净4〕/lancaster-sound〔同指〕/
    Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Bathurst Inlet/Mendoza/Neuquem/Araucania（净<5 或同指）——place 关闭后此清单封存。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot、HK-place-apostrophe-label-slug-divergence、
    HK-close-override-productive-discover、HK-close-accelerated-on-exhaustive-zero〔新〕、HK-dupcheck-the-prefix-blindspot、
    HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**（place 关闭后转 DEFERRED 永久，除非 Phase 3 深度层重启）。
