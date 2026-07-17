---
round: 213
date: 2026-07-17
type_round: 184
phase: "2.1"
current_type: place
gene: NEW1
pages: [uzun-ada]
result: success
---

# GROW 2.1-B · R213 · NEW1 · place — 建 Uzun Ada（ASC 里海东岸港，净 solid 15 单指；大 Transasiatic 铁路西端起点，Bombarnac 入亚洲第一站）

## 执行摘要

Phase 2.1-B place 广度扩张第 184 轮（type_round 184）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、since_discover=0<10〔R212 SCN28 RESET〕、queue(place)=4>0、stub%=0 → §3(7)）。

取 R212 discover 队列**建序 1** **Uzun Ada**（ASC 主）。建前 pages.json 子串（uzun）+
`the-` 前缀双查皆 NEW。**单指无混淆**：全库 27 distinctPN 全指 ASC 里海东岸港，无同名异指。
**净 15 distinct solid ASC PN**（远超门）：
- **ASC-001-007**：里海东岸港，Bombarnac 受命前往。
- **ASC-004-004**：Transcaspian 行于 Uzun Ada 与中国边境间。
- **ASC-005-001**：Annenkof 建 Uzun Ada 以缩短里海横渡。
- **ASC-003-042**：其建成使原经 Baku 之贸易倍增。
- **ASC-004-089**：入其视野一时后即踏足亚洲。
- **ASC-004-005**：Bombarnac 于此会合旅伴。
- **ASC-005-007**：Uzun Ada 站，午后四时发车，Caspian cable 电报。
- **ASC-005-018**：自 Uzun Ada 至 Pekin 仅十一日。
- **ASC-005-006**：名意为 Long Island。
- **ASC-006-004**：堤约 1,200 码隔 Long Island 与大陆；两侧沙丘。
- **ASC-006-006**：荒瘠无植之地自港延一百五十里。
- **ASC-007-020**：Skobeleff 登 Mikhailov 时港尚未存，Annenkof 后建战略铁路。
- **ASC-006-005**：Mikhailov 距 Uzun Ada 一里格。
- **ASC-010-073**：Bokhara 距 Uzun Ada 1,107 versts。
- **ASC-015-045**：越中国边境，自港四日行近 2,300 公里。

place 计数 408→409，registry total 1476→1477，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Central Asia、book The Adventures of a Special Correspondent、aliases=[]（Long Island 为释名，散文提及，不设 alias 避冲突）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；queue=4 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Saville Row / Villa Rica / Coal Town（3 项）。R216 建毕队列罄 → SCN28（或 R215 EVV5 先插）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| uzun-ada | MR1Kbc | The Adventures of a Special Correspondent | real | Central Asia | 15 | 里海东岸港；Transasiatic 西端；Long Island 释名不设 alias；单指无混淆 |

- **uzun-ada**：15 distinct solid ASC PN（单指）；aliases []。链 Baku/Transasiatic/Annenkof/Bokhara 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 ASC Uzun Ada；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：15 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1477 place 409 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（uzun）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R214 起始计数）

| 字段 | R213 起始 | R214 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 213 | 214 |
| type_round | 184 | 185 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 149 | 150 |
| last_updated_round | 213 | 214 |

## 遗留问题

1. **place 页数 409**：本轮 +1（Uzun Ada）。registry 全库 1477，unknown 0。
2. **下轮 R214 = NEW1**：since_evv5=9<10、since_discover=1<10、queue(place)=3>0 → §3(7)。
   建 **Saville Row**（saville-row，AWED×8，伦敦 Fogg 宅街），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region England，real。
3. **R215 EVV5 预告**：R214 末 since_evv5→10，R215 起 §3(1b) EVV5 触发（schema 反思，非建页）。
4. **R214+ 建序**：Saville Row → Villa Rica → Coal Town（3 项），间插 R215 EVV5；建毕队列罄 → SCN28。
5. **同名异指剔除**：本轮无（Uzun Ada 单指）；承纪律。
6. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=149→150（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
