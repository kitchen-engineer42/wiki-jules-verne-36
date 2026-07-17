---
round: 209
date: 2026-07-17
type_round: 180
phase: "2.1"
current_type: place
gene: NEW1
pages: [healthful-house]
result: success
---

# GROW 2.1-B · R209 · NEW1 · place — 建 Healthful House（FF 私立疗养院/Thomas Roch 囚所，净 solid 11 单指；Neuse 右岸围墙庄园，Facing the Flag 开篇场所）

## 执行摘要

Phase 2.1-B place 广度扩张第 180 轮（type_round 180）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、since_discover=0<10〔R208 SCN28 RESET〕、queue(place)=4>0、stub%=0 → §3(7)）。

取 R208 discover 队列**建序 1** **Healthful House**（FF）。建前 pages.json 子串
（healthful）+ `the-` 前缀双查皆 NEW。**单指无混淆**：全库 72 distinctPN 全指 FF
Facing the Flag 私立疗养院，无同名异指。**净 11 distinct solid FF PN**（远超门）：
- **FF-001-002**：director 收 carte de visite（开篇）。
- **FF-001-009**：私立机构，select personnel，名医协作。
- **FF-001-010**：situation 极宜人。
- **FF-001-011**：慢病为主，亦收精神病患。
- **FF-001-012**：世界级名人囚此 18 月，招关注。
- **FF-001-013**：Pavilion No.17 于 HH Park 尽头，专设 warder。
- **FF-001-037**：非疯人院，Roch 迁 HH 疗治。
- **FF-001-042**：Simon Hart（alias Gaydon）任 attendant 15 月。
- **FF-002-012**：Count d'Artigas 携 Captain Spade 至门（Ebba 舰长）。
- **FF-002-031**：法国发明家 Roch 为 HH 最著 inmate（Pavilion 17）。
- **FF-002-034**：Count 获准访 HH 见 Roch。
- **FF-003-002**：beech 道隔 HH 庄园与 Neuse 右岸。
- **FF-003-003**：高墙环庄园，不可攀。
- **FF-003-103**：Ebba 近 HH 招疑，Count 匿俘。

place 计数 405→406，registry total 1473→1474，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK。
real_or_fictional=fictional、region United States、book Facing the Flag、aliases=[]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；queue=4 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Arctic Ocean / Upper Amazon / Celestial Empire（3 项）。R212 建毕队列罄 → SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| healthful-house | oXgFqT | Facing the Flag | fictional | United States | 11 | Neuse 右岸私立疗养院；Thomas Roch 囚所（Pavilion 17）；单指无混淆 |

- **healthful-house**：11 distinct solid FF PN（单指）；aliases []。链 Thomas Roch/Count d'Artigas/Neuse 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 FF Healthful House；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：11 solid（单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1474 place 406 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（healthful）+ `the-` 前缀双查。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R210 起始计数）

| 字段 | R209 起始 | R210 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 209 | 210 |
| type_round | 180 | 181 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 145 | 146 |
| last_updated_round | 209 | 210 |

## 遗留问题

1. **place 页数 406**：本轮 +1（Healthful House）。registry 全库 1474，unknown 0。
2. **下轮 R210 = NEW1**：since_evv5=5<10、since_discover=1<10、queue(place)=3>0 → §3(7)。
   建 **Arctic Ocean**（arctic-ocean，55 distinct，真实北冰洋跨作品单指），建前 pages.json
   子串 + `the-` 双查，抽样 ≥5 solid，核跨作品单指非异指，region Arctic，real。
3. **R210+ 建序**：Arctic Ocean → Upper Amazon → Celestial Empire（3 项），R212 建毕队列罄 → SCN28。
4. **同名异指剔除**：本轮无（Healthful House 单指）；承纪律。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=145→146（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
