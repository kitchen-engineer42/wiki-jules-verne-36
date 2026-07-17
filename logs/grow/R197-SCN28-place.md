---
round: 197
date: 2026-07-17
type_round: 168
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 4
---

# GROW 2.1-B · R197 · SCN28 · place — discover（R192 队列建罄，掘 MI 人居设施 + FC/AM 极地 toponym，净新 4 buildable）

## 执行摘要

Phase 2.1-B place 广度扩张第 168 轮（type_round 168）。决策机 §3：since_evv5=3<10（未达 EVV5）、
queue(place)=0 → §3(3)（queue<10）&§3(4)（zombie）触 **SCN28 discover**。
R192 补种 3 项（The Mercy/Jacamar Wood/Far West）R194–R196 建罄，队列归零，本轮复扫补种。

**矿脉转向**：MI Lincoln Island 自然地理（岬/湾/沼/河/林/湖）近饱和——本轮首扫 MI 内陆水文
（Lake Grant/Red Creek/Falls River/Creek Glycerine）**全为既有页**，印证水文网已建齐。
遂转掘两个未采层：**MI 人居设施**（Chimneys/corral——非自然地物而叙事居所）+ **FC/AM 极地 toponym 长尾**。

**净新 4 buildable（均文件系统 + 后缀变体查重，均 ≥5 solid distinctPN）**：

1. **Chimneys → chimneys**（MI×144）：Lincoln Island 河口花岗岩堆叠洞穴，殖民者首居所（Granite House 前之临时家）。
   MI-004-020 得名/MI-004-021 塞口成居/MI-004-024 堪用/MI-004-025 出洞攀岸。fictional，region Lincoln Island。
2. **the corral → corral**（MI×286，极密）：Lincoln Island Red Creek 谷畜栏，圈 musmon/山羊，后为 Ayrton 居所、叙事枢纽。
   MI-030-029 划界/MI-030-032 骑巡/MI-030-034 驱兽入栏/MI-030-036 复访。fictional，region Lincoln Island。
3. **New Georgia → new-georgia**（AM×11）：亚南极岛，Isle de Saint Pierre / South Georgia / King George's Island
   （AM-010-020），距 Falklands 800 mi（AM-010-006），属 Falklands 辖（AM-010-023），海兽频出（AM-010-024）。real，region South Atlantic Ocean。
4. **Coppermine River → coppermine-river**（ACH+FC×10）：北美极地大河，Hearne 1770 发现（FC-002-023），
   Richardson 溯行至 Polar Sea（ACH-014-023），Mackenzie 支流水系（FC-007-004），流入 Coronation Gulf（FC-010-007）。real，region Arctic North America。

new_candidates=4 ≥ type_close_new_candidate_min=3 → discover_streak_low 保持 0。
**未建页**：SCN28 为发现轮，仅入队 + 抽样验 solidity，since_discover 归 0。registry 恒 1465，place 恒 397。

## 决策矩阵（SCN28 discover）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=3<10 | 否 |
| 1b | EVV5（since_evv5≥10）| =3<10 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **queue=0<10** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| =0（同触）| （3 已触）|
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | （前置已触）|

> §3(3) 与 §3(4) 同时成立（queue=0）。since_evv5=3<10 未达 EVV5，SCN28 discover 触发。

## 页面处理记录

本轮为 discover 轮，未建页。入队候选（建序）：

| 建序 | slug | label | book | rof | region | distinctPN | 状态 |
|------|------|-------|------|-----|--------|-----------|------|
| 1 | chimneys | Chimneys | The Mysterious Island | fictional | Lincoln Island | MI×144 | 入队待建 R198 |
| 2 | corral | the corral | The Mysterious Island | fictional | Lincoln Island | MI×286 | 入队待建 |
| 3 | new-georgia | New Georgia | An Antarctic Mystery | real | South Atlantic Ocean | AM×11 | 入队待建 |
| 4 | coppermine-river | Coppermine River | The Fur Country | real | Arctic North America | ACH+FC×10 | 入队待建 |

**排除**：lake-grant/red-creek/falls-river/creek-glycerine（MI 内陆水文皆已建）；cape-bathurst/fort-reliance/
great-bear-lake/platte-river/fort-kearney/omaha/salt-lake-city（FC/AWED 皆已建）；Fort Enterprise（FC×4 净<5 DEFER）、
North/South Mandible（各 3，mandible-cape overlap）、Reptile Point（3）、Grand View/Mount Bell/Balloon Rock（0 命中拼写待考）DEFER。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：候选均抽样 solid full PN（见执行摘要），建页时逐句 grounding。✔（deferred to build）
- **查重充分**：chimneys/corral/new-georgia/coppermine-river 均文件系统 test -f + 后缀变体 + 语义排除既有水文/堡站页。✔
- **净新 ≥3**：4 buildable 达 min。✔
- **矿脉未宣布饱和**：MI 自然地理近罄，转人居设施 + FC/AM 极地长尾，仍有余项（Coronation Gulf/Mackenzie〔river〕待复扫）。✔
- **排除检查**：本轮仅改 queue.md/grow_state.json/log，见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R198 起始计数）

| 字段 | R197 起始 | R198 起始（本轮末写入）| 变更 |
|------|----------|---------------------|------|
| current_round | 197 | 198 | +1 |
| type_round | 168 | 169 | +1 |
| rounds_since_last_evv5 | 3 | 4 | +1 |
| rounds_since_last_discover | 4 | 0 | **RESET**（discover）|
| discover_streak_low | 0 | 0 | 不变（new_cand=4≥3）|
| rounds_since_last_corpus_discover | 133 | 134 | +1 |
| last_updated_round | 197 | 198 | — |

## 遗留问题

1. **place 页数 397（不变）**：本轮 discover 未建页。registry 全库 1465，unknown 0。
2. **下轮 R198 = NEW1**：since_evv5=4<10、since_discover=0<10、queue(place)=4>0 → §3(7) NEW1。
   建 **Chimneys**（chimneys，MI×144，殖民者首居所），建前文件系统查重 + 抽样 ≥5 solid。
3. **R198+ 建序**：Chimneys → corral → New Georgia → Coppermine River（4 项），R201 建毕队列罄 → 再 SCN28。
4. **MI 自然地理近饱和信号**：本轮 MI 内陆水文候选（Lake Grant/Red Creek/Falls River/Creek Glycerine）全既有，
   岬/湾/沼/河/林/湖主干已建齐。**未宣布饱和**（承 memory：须复扫余项如 Coronation Gulf/Mackenzie〔river〕/
   MI 人居设施剩余〔如 the palisade/poultry-yard 待查是否够 place 门〕），但 MI 自然层深挖收益递减，
   后续 discover 宜向 FC/AM/AWED/ACH 极地-铁路长尾扩散。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 discover 未建页。
6. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
7. **corpus-discover 顺延**：since_corpus=133→134（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **featured re-grade DEFERRED**：17 place 页 quality=none（R193 EVV5 登记），full-library re-grade 顺延至 RFC 批审。
10. **DEFER/DUPLICATE 累积**：本轮 +Fort Enterprise（FC×4 DEFER）/North·South Mandible（mandible-cape overlap）/
    Reptile Point DEFER；既有 Medicine Bow/Grant Lake/Prospect Plateau DEFER，Salt Lake/Serpentine/Omaha/
    Cape Bathurst 等 DUPLICATE（已建）照旧。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
