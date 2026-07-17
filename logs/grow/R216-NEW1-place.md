---
round: 216
date: 2026-07-17
type_round: 187
phase: "2.1"
current_type: place
gene: NEW1
pages: [villa-rica]
result: success
---

# GROW 2.1-B · R216 · NEW1 · place — 建 Villa Rica（EHLA 巴西钻石区矿镇/审判地，净 solid 10 单指；钻石押运封印地兼监狱，Joam Dacosta 定罪越狱处）

## 执行摘要

Phase 2.1-B place 广度扩张第 187 轮（type_round 187）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10〔R215 EVV5 RESET〕、since_discover=3<10、queue(place)=2>0、stub%=0 → §3(7)）。

取 R212 discover 队列**建序 3** **Villa Rica**（EHLA 主）。建前 pages.json 子串（villa）+
`the-` 前缀双查皆 NEW。**单指无混淆**：全库 13 distinctPN 全指 EHLA 巴西钻石区审判镇，无同名异指。
**净 10 distinct solid EHLA PN**（远超门）：
- **EHLA-019-031**：钻石押运先至 Villa Rica，commandant 封印 sacks，再往 Rio de Janeiro。
- **EHLA-023-002**：Ribeiro 昔为 Villa Rica advocate，庭上辩护。
- **EHLA-039-019**：匪徒于 Villa Rica 外伏击押运，屠戮 escort。
- **EHLA-020-007**：钻石案定罪判死者即自 Villa Rica 狱越出。
- **EHLA-025-039**：Villa Rica 陪审团一致裁决无从宽。
- **EHLA-023-005**：行刑前夜 gallows 已立，Joam Dacosta 越 Villa Rica 狱。
- **EHLA-034-050**：Villa Rica assizes 判决之日为密码试值之一。
- **EHLA-037-036**：曾一度越 Villa Rica 狱，众以为畏罪潜逃。
- **EHLA-024-068**：Ribeiro 任本省法官前为 Villa Rica advocate。
- **EHLA-039-043**：Villa Rica 之囚终获昭雪。

place 计数 410→411，registry total 1478→1479，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=real、region Brazil、book Eight Hundred Leagues on the Amazon、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；queue=2 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Coal Town（1 项）。R217 建毕队列罄 → R218 SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| villa-rica | ibX8le | Eight Hundred Leagues on the Amazon | real | Brazil | 10 | 巴西钻石区矿镇/审判地；钻石押运封印+监狱；Dacosta 定罪越狱；单指无混淆 |

- **villa-rica**：10 distinct solid EHLA PN（单指）；aliases []。链 Rio de Janeiro/Joam Dacosta/Judge Ribeiro/diamond convoy 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 EHLA Villa Rica；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：10 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（附 wikilink [[Rio de Janeiro]]）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1479 place 411 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（villa）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R217 起始计数）

| 字段 | R216 起始 | R217 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 216 | 217 |
| type_round | 187 | 188 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 152 | 153 |
| last_updated_round | 216 | 217 |

## 遗留问题

1. **place 页数 411**：本轮 +1（Villa Rica）。registry 全库 1479，unknown 0。
2. **下轮 R217 = NEW1**：since_evv5=1<10、since_discover=4<10、queue(place)=1>0 → §3(7)。
   建 **Coal Town**（coal-town，UC×7，Loch Katrine 东岬地下矿村），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region Scotland underground，fictional。
3. **R217 建毕队列罄 → R218 = SCN28**（§3(4) zombie 或 §3(3)）；届时可核 R212 备选（Montgomery Street/Kamtchatka Current/Pleasant Garden/North Carolina）或再全库重扫。
4. **同名异指剔除**：本轮无（Villa Rica 单指）；承纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=152→153（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
