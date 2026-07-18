---
round: 224
date: 2026-07-18
type_round: 195
phase: "2.1"
current_type: place
gene: NEW1
pages: [new-berne]
result: success
---

# GROW 2.1-B · R224 · NEW1 · place — 建 New-Berne（北卡 Neuse 河港市，FF×10 单指；Ebba 停锚处，Healthful House 邻邑，Roch/Gaydon 绑架案枢纽）

## 执行摘要

Phase 2.1-B place 广度扩张第 195 轮（type_round 195）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、streak=1<3、since_discover=0<10、queue(place)=2>0、stub%=0 → §3(7)）。

取 R223 SCN28 队列**建序 1** **New-Berne**（FF 主）。建前 pages.json 子串（new-berne）+
`the-` 前缀双查皆 NEW。**单作品单指**：FF 中 New-Berne 全指北卡 Neuse 河真实港市，无同名异指。
**净 10 distinct solid PN**（远超门；剔除 FF-001-006-s2「州议会所在」——该句指首府 Raleigh，非 New-Berne）：

- **FF-001-005**：Ebba 停锚 New-Berne 外，Pamlico Sound。
- **FF-002-009**：Ebba 首泊 New-Berne 港，主人任性至 Neuse 河口。
- **FF-003-036**：暮色中 New-Berne 于 Neuse 左岸渐隐。
- **FF-003-052**：潮将复涨，越 New-Berne 数英里强升。
- **FF-003-103**：Ebba 近 Healthful House，恐招 New-Berne 当局访查。
- **FF-004-002**：New-Berne 码头尽处见船员擦甲板。
- **FF-004-023**：讯至 New-Berne，当局初惑逃抑劫。
- **FF-004-028**：New-Berne 下 20 英里河湾折西北，注入 Pamlico Sound。
- **FF-004-045**：New-Berne 当局令 Falcon 号截搜 Ebba。
- **FF-013-022**：Healthful House 近 New-Berne，北卡——Roch/Gaydon 被劫。

place 计数 416→417，registry total 1484→1485，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 1 段 >399，拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region United States、book Facing the Flag、aliases=[]。
Connections/正文含 [[Pamlico Sound]]/[[Healthful House]]/[[North Carolina]]（三页均存）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| new-berne | eiJJkw | Facing the Flag | real | United States | 10 | 北卡 Neuse 河港市；Ebba 停锚处；Healthful House 邻邑；FF 单指（剔除 Raleigh 混指句）|

- **new-berne**：10 distinct solid PN（FF 单指）；aliases []。链 Pamlico Sound/Healthful House/North Carolina。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 FF New-Berne；剔除 FF-001-006-s2（指 Raleigh）；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：10 solid（FF 单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（三 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1485 place 417 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（new-berne）+ `the-` 前缀双查皆 NEW（exact-slug）。✔
- **单作品单指核 + 混指剔除**：FF 逐句确认 New-Berne 指一港市；FF-001-006-s2「州议会所在」剔除（属首府 Raleigh 上下文）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R225 起始计数）

| 字段 | R224 起始 | R225 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 224 | 225 |
| type_round | 195 | 196 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 160 | 161 |
| last_updated_round | 224 | 225 |

## 遗留问题

1. **place 页数 417**：本轮 +1（New-Berne）。registry 全库 1485，unknown 0。
2. **下轮 R225 = NEW1**：since_evv5=9<10、streak=1<3、since_discover=1<10、queue(place)=1>0 → §3(7)。
   建 **Raleigh**（raleigh，FF×2+MW×3=5 distinct 跨作品单指北卡首府；内陆 150 英里，飞行器降落地/Strock 出发地），
   建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid（恰 5，须逐句确凿），region United States，real。
3. **R226 = EVV5**：since_evv5 届 10 → §3(1b)。schema 反思轮，不建页。
4. **discover_streak_low=1**：R226 EVV5 后下一 SCN28 若续 <3 两轮 → streak=3 触 §3(2) CLOSE 评估。
   下一 SCN28 试二/三字混合 toponym 正则或未建小特征细扫；确认饱和则 CLOSE place → event。
5. **HK-dupcheck-bareterm-vs-slug**〔R223 新记〕：bare-term gather ≥5 ≠ 可建，须 exact-slug 核。本轮已遵。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=160→161（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；tsalal-island/serpentine-peninsula/
    beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建）；Wilmington/Catawba/Cape Hatteras/Mackenzie〔river〕/Fort Good Hope/
    Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
