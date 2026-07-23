---
round: 478
date: 2026-07-23
type_round: 170
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R478 · SCN28-zombie · character — 第三十三批 discover：续「已引未建」簇心缺员（mr-bredejord/yaquita/hurliguerly），queue 0→3

## 执行摘要

Phase 2.1-B character discover 轮（type_round 170）。§3 首匹配 **§3(4) SCN28-zombie**（since_evv5=7<10；SCN28 周期 since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第三十二批（建序 172-174）R475-R477 全数消费（judge-jarriquez/jeorling/schwaryencrona），queue 归 0，本轮触发 zombie discover。

**簇策**：延续第三十一批之「已引未建」完足法——R476-R477 之 jeorling/schwaryencrona 各以纯文本引 Hurliguerly/Bredejord；minha（R471）引 Yaquita。本批据 proper-noun 频次扫描确认三者高频未建，一举补齐、完足三簇并起回链：

| 建序 | slug | book | VVV | pn_anchor | role | mentions/PN | dup-check | 簇 |
|------|------|------|-----|-----------|------|-------------|-----------|-----|
| 175 | mr-bredejord | The Waif of the Cynthia | WC | WC-004 | supporting | 94/93 | ABSENT | WC 接 schwaryencrona/erik/tudor-brown（→4 页）|
| 176 | yaquita | Eight Hundred Leagues on the Amazon | EHLA | EHLA-003 | supporting | 109/103 | ABSENT | EHLA 接 joam/benito/minha/manoel（→7 页）|
| 177 | hurliguerly | An Antarctic Mystery | AM | AM-002 | supporting | 73/73 | ABSENT | AM 接 jeorling/len-guy/dirk-peters（→5 页）|

**候选说明**：
- **mr-bredejord**（WC）——Stockholm 律师、Schwaryencrona 之挚友兼论辩对手，以怀疑论衬托考据；94 mentions/93 distinctPN，首现 WC-004-041。回填 schwaryencrona 页纯文本 Bredejord。
- **yaquita**（EHLA）——Joam Garral 之贤妻、Benito 与 Minha 之母；109 mentions/103 distinctPN，首现 EHLA-003-010。回填 minha 页纯文本 Yaquita，EHLA 簇将达 7 页（本 wiki 最密簇）。
- **hurliguerly**（AM）——Halbrane 号水手长、Isle of Wight 人、健谈斡旋助 Jeorling 登船；73 mentions/73 distinctPN，首现 AM-002-011。回填 jeorling 页纯文本 Hurliguerly。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT。distinctPN 全 ≥73。**排除（registry-catch）**：WC 既建 erik/tudor-brown/schwaryencrona；EHLA 既建 joam/benito/torres/manoel/minha/jarriquez；AM 既建 len-guy/dirk-peters/william-guy/jeorling。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| since_evv5=7 | 否 |
| 2 | CLOSE（streak_low≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 175-177）+ discover-note。

## EXIT-GATE 检查

- **G4**：discover 轮，仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、无冲突。✔
- **grounding**：distinctPN 93/103/73，足支撑 ≥16 solid PN。✔
- **网络价值**：三者皆前批纯文本引用之簇心角，建后可回链、三簇分别达 4/7/5 页密网。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R479 起始计数）

| 字段 | R478 起始 | R479 起始 |
|------|----------|----------|
| current_round | 478 | 479 |
| type_round | 170 | 171 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 414 | 415 |
| last_updated_round | 478 | 479 |

## 遗留问题

1. **character 139**：本轮无建页（discover 轮）。queue(character) 0→**3**（第三十三批建序 175-177）。registry **1663**，featured 35（5.1%），覆盖 32 部。
2. **下轮 R479 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 175 **mr-bredejord**（WC Schwaryencrona 挚友/论辩者，supporting，94 mentions；深耕 WC 至 4 页，回填 schwaryencrona 页 Bredejord）。
3. **深耕计划**：R479（175 mr-bredejord）→ **R480 = EVV5**（since_evv5 于 R480 起始达 10 → 触发；此前先建 175）→ 实为 R480 起始 since_evv5=9？校验：R478 起始 since_evv5=7；R478 SCN28 非 EVV5 → R479 起始=8；R479 NEW1 非 EVV5 → R480 起始=9；**R481 起始=10 → R481=EVV5**。故 R480/R481 消费 176 yaquita/177 hurliguerly，**R482=EVV5**（待 R479-R481 逐轮复核）。
4. **广度趋饱和观察**：连续以「已引未建」+ proper-noun 高频缺员深耕；若某批高频缺员将尽（候选 <3）→ discover_streak_low 累加，趋近 §3(2) CLOSE → character 收口 → Phase 3。当前仍稳定 3/批。
5. **目标**：grow 至 Phase 10。Phase 2.1-B 广度扩张持续，R478/~500。
6. **PN 渲染 / Martin Paz alias / HK / Pilot 债 / event PN 债 / 回链**：DEFERRED。
7. **corpus-discover 顺延**：since_corpus=414→415。
