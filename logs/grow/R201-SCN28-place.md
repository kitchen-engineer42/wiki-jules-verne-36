---
round: 201
date: 2026-07-17
type_round: 172
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 5
---

# GROW 2.1-B · R201 · SCN28 · place — discover（R197 队列建罄，转掘 SC 巴塔哥尼亚/澳洲 + EHLA 亚马逊 toponym，净新 5 buildable）

## 执行摘要

Phase 2.1-B place 广度扩张第 172 轮（type_round 172）。决策机 §3：since_evv5=7<10（未达 EVV5）、
queue(place)=0 → §3(3)（queue<10）&§3(4)（zombie）触 **SCN28 discover**。
R197 补种 4 项 R198–R200 建齐（chimneys 判 DUPLICATE 剔 + corral/new-georgia/coppermine-river 3 建），队列归零，本轮复扫补种。

**矿脉转向——FC 极地长尾近罄，转 SC 巴塔哥尼亚/澳洲 + EHLA 亚马逊**：
首扫 FC 极地 fort/river 长尾（Coronation Gulf/Bathurst Inlet/Mackenzie〔river〕/Great Slave Lake/Fort Confidence/
Fort Providence/Fort Resolution/Fort Good Hope/Fort Enterprise/Turnagain/Fort Franklin）——**多为既有页或净<5**：
coronation-gulf/great-slave-lake/fort-confidence/fort-providence 皆已建；Mackenzie〔river referent〕剔 explorer-name
enumeration 后净<5 DEFER；Fort Good Hope（2）/Fort Resolution（2）/Turnagain（3）/Fort Franklin（3）/Fort Enterprise（4）
/Cape Dundas（4）/Bathurst Inlet（1）/Athabasca（1）/Back River（1）均 <5 DEFER。**FC 极地层深挖收益递减**。

遂转掘 **In Search of the Castaways（SC）巴塔哥尼亚 + 澳洲地理**（未采层）——广度扫描证多数 SC toponym 已建
（bay-of-talcahuano/twofold-bay/snowy-river/cape-bernouilli/torres-strait/new-america/victoria-bay/sierra-tandil 等），
但**净新 5 项达门**。另掘 EHLA（Eight Hundred Leagues on the Amazon）亚马逊水系一项。

**净新 5 buildable（均 pages.json 子串 + `the-` 前缀双查〔承 HK-dupcheck-the-prefix-blindspot〕，均 ≥5 solid distinctPN）**：

1. **Rio Negro → rio-negro**（EHLA×40 主 / SC×4）：**亚马逊大支流**（EHLA 叙事主河，The Giant Raft/Jangada 顺流之河）。
   **同名异指剔除**：全库 44 distinctPN 中 40 为 EHLA 亚马逊 Rio Negro、4 为 SC 巴塔哥尼亚 Rio Negro——**采 EHLA 亚马逊 referent（40 solid，远超门），剔 4 SC**。real，region Amazon Basin。建序 1。
2. **Wimerra → wimerra**（SC×11，单指）：澳洲 Victoria 省河流/地区（143d meridian，Apsley 教区），Ayrton 叛迹枢纽
   （SC-037-001 Wimerra camp / SC-043-034 与 blacksmith 通信留迹）。real，region Australia。建序 2。
3. **Guamini → guamini**（SC×10，单指）：巴塔哥尼亚 salt-lake/locale。real，region Patagonia。建序 3。
4. **Carmen → carmen**（SC×7，单指）：巴塔哥尼亚 Rio Negro 河口镇（SC-021-062 Tandil–Carmen 商道 / SC-016-019 Carmen–Mendoza route）。real，region Patagonia。建序 4。
5. **Rio Colorado → rio-colorado**（SC×6 主 / DSCF×1）：巴塔哥尼亚河，越 37th parallel（SC-016-015），Rio Negro 姊妹河
   （SC-032-011 二河入海）。real，region Patagonia。建序 5。

new_candidates=5 ≥ type_close_new_candidate_min=3 → discover_streak_low 保持 0。
**未建页**：SCN28 为发现轮，仅入队 + 抽样验 solidity，since_discover 归 0。registry 恒 1468，place 恒 400。

## 决策矩阵（SCN28 discover）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=7<10 | 否 |
| 1b | EVV5（since_evv5≥10）| =7<10 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **queue=0<10** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| =0（同触）| （3 已触）|
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | （前置已触）|

> §3(3) 与 §3(4) 同时成立（queue=0）。since_evv5=7<10 未达 EVV5，SCN28 discover 触发。

## 页面处理记录

本轮为 discover 轮，未建页。入队候选（建序）：

| 建序 | slug | label | book | rof | region | distinctPN | 状态 |
|------|------|-------|------|-----|--------|-----------|------|
| 1 | rio-negro | Rio Negro | Eight Hundred Leagues on the Amazon | real | Amazon Basin | EHLA×40（剔 4 SC）| 入队待建 R202 |
| 2 | wimerra | Wimerra | In Search of the Castaways | real | Australia | SC×11 | 入队待建 |
| 3 | guamini | Guamini | In Search of the Castaways | real | Patagonia | SC×10 | 入队待建 |
| 4 | carmen | Carmen | In Search of the Castaways | real | Patagonia | SC×7 | 入队待建 |
| 5 | rio-colorado | Rio Colorado | In Search of the Castaways | real | Patagonia | SC×6（剔 1 DSCF）| 入队待建 |

**排除**：coronation-gulf/great-slave-lake/fort-confidence/fort-providence/cape-bathurst/fort-kearney/fort-reliance/
sierra-tandil/fort-independence/bay-of-talcahuano/twofold-bay/snowy-river/cape-bernouilli/torres-strait/new-america/
victoria-bay/vanikoro/vigo-bay/ceylon/zanzibar/gibraltar/suez/aden/yokohama/bombay/calcutta/lake-tchad/kazeh/gondokoro（皆已建）；
Mackenzie〔river referent 净<5〕/Fort Good Hope（2）/Fort Resolution（2）/Fort Enterprise（4）/Turnagain（3）/Fort Franklin（3）/
Cape Dundas（4）/Bathurst Inlet（1）/Athabasca（1）/Back River（1）/Mendoza（4）/Neuquem（2）/Araucania（3）DEFER（净<5）。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：候选均抽样 solid full PN（见执行摘要），建页时逐句 grounding。✔（deferred to build）
- **查重充分**：5 候选均 pages.json 子串 + `the-` 前缀双查（承 HK-dupcheck-the-prefix-blindspot，R198 教训）+ 语义排除既有 SC/FC 地理页。✔
- **净新 ≥3**：5 buildable 达 min。✔
- **同名异指纪律**：Rio Negro 剔 4 SC 采 40 EHLA；Rio Colorado 剔 1 DSCF 采 6 SC。建时逐句核 VVV referent。✔
- **矿脉未宣布饱和**：FC 极地长尾近罄，转 SC 巴塔哥尼亚/澳洲 + EHLA 亚马逊新层，仍余项（SC 澳洲段/EHLA 亚马逊支流待复扫）。✔
- **排除检查**：本轮仅改 queue.md/grow_state.json/log，见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R202 起始计数）

| 字段 | R201 起始 | R202 起始（本轮末写入）| 变更 |
|------|----------|---------------------|------|
| current_round | 201 | 202 | +1 |
| type_round | 172 | 173 | +1 |
| rounds_since_last_evv5 | 7 | 8 | +1 |
| rounds_since_last_discover | 3 | 0 | **RESET**（discover）|
| discover_streak_low | 0 | 0 | 不变（new_cand=5≥3）|
| rounds_since_last_corpus_discover | 137 | 138 | +1 |
| last_updated_round | 201 | 202 | — |

## 遗留问题

1. **place 页数 400（不变）**：本轮 discover 未建页。registry 全库 1468，unknown 0。
2. **下轮 R202 = NEW1**：since_evv5=8<10、since_discover=0<10、queue(place)=5>0 → §3(7) NEW1。
   建 **Rio Negro**（rio-negro，EHLA×40 亚马逊大支流），建前 pages.json 子串 + `the-` 双查 + **逐句核 EHLA referent 剔 4 SC**，抽样 ≥5 solid。
3. **R202+ 建序**：Rio Negro → Wimerra → Guamini → Carmen → Rio Colorado（5 项），R206 建毕队列罄 → 再 SCN28。
4. **EVV5 逼近**：since_evv5=7→8，R204 前后触 §3(1b) EVV5（schema 反思，非建页）。届时 place schema 全库评审。
5. **矿脉信号**：FC 极地 fort/river 长尾近罄（本轮多既有/净<5）；SC 巴塔哥尼亚+澳洲 + EHLA 亚马逊为新富矿层。
   **未宣布饱和**（承 memory：须复扫余项——SC 澳洲段〔Murray/Yarrow/Torrens 待查〕、EHLA 亚马逊支流、20KL 海洋 toponym 长尾）。
6. **HK-dupcheck-the-prefix-blindspot**：本轮 5 候选均应用子串 + the- 双查，无复现。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 discover 未建页。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=137→138（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：17+ place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；本轮 +Mackenzie〔river〕/Fort Good Hope/Fort Resolution/
    Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
