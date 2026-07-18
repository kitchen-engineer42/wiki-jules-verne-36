---
round: 225
date: 2026-07-18
type_round: 196
phase: "2.1"
current_type: place
gene: NEW1
pages: [raleigh]
result: success
---

# GROW 2.1-B · R225 · NEW1 · place — 建 Raleigh（北卡首府，内陆 150 英里；跨作品 FF×2+MW×3 单指；Strock 出发地，飞行器降落邻邑）

## 执行摘要

Phase 2.1-B place 广度扩张第 196 轮（type_round 196）。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10、streak=1<3、since_discover=1<10、queue(place)=1>0 → §3(7)）。

取 R223 SCN28 队列**建序 2** **Raleigh**（MW 主，FF 辅）。建前 pages.json 子串（raleigh）+
`the-` 前缀双查皆 NEW（exact-slug；`ra/raleigh.md` 不存在）。**跨作品单指**：FF 与 MW 中 Raleigh
全指北卡首府一城，无同名异指。**净 5 distinct solid PN**（恰达门，逐句确凿）：

- **FF-001-006**：Raleigh 为北卡首府，内陆 150 英里的重要城镇。
- **FF-004-016**：失踪讯电传 New Berne，再转 Raleigh。
- **MW-001-014**：飞行器降落 Raleigh 邻邑（北卡首府）。
- **MW-002-002**：Strock 4 月 27 日抵 Raleigh（离 Washington 前夜）。
- **MW-002-038**：Strock 归家备行，翌晚复至 Raleigh，由此启程赴山。

place 计数 417→418，registry total 1485→1486，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检 0 超段（初稿即达标）。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region United States、book Master of the World、aliases=[]。
Connections/正文含 [[New-Berne]]/[[North Carolina]]（两页均存）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| raleigh | YzIzcT | Master of the World | real | United States | 5 | 北卡首府，内陆 150 英里；Strock 出发地；飞行器降落邻邑；FF+MW 跨作品单指一城 |

- **raleigh**：5 distinct solid PN（FF×2+MW×3 跨作品单指）；aliases []。链 New-Berne/North Carolina。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指北卡首府 Raleigh；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，初稿即 0 超段。✔
- **G3 ≥5 distinct PN**：5 solid（恰达门，逐句确凿；FF+MW 跨作品单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（两 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1486 place 418 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（raleigh）+ `the-` 前缀双查 + test -f 皆 NEW（exact-slug）。✔
- **单作品单指核**：FF/MW 逐句确认 Raleigh 指北卡首府一城，无同名异指。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R226 起始计数）

| 字段 | R225 起始 | R226 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 225 | 226 |
| type_round | 196 | 197 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 161 | 162 |
| last_updated_round | 225 | 226 |

## 遗留问题

1. **place 页数 418**：本轮 +1（Raleigh）。registry 全库 1486，unknown 0。
2. **下轮 R226 = EVV5**：since_evv5 届 10 → §3(1b)。schema 反思轮，不建页，reset since_evv5=0。
   R223 SCN28 队列 2 项（New-Berne/Raleigh）已全消费，queue(place)==0。
3. **R227 = SCN28-zombie**：EVV5 后 queue(place)==0 → §3(4)。第三次 place discover。
   试二/三字混合 toponym 正则或未建小特征细扫；若 new_candidates<3 → streak 1→2。
4. **discover_streak_low=1**：R227 SCN28 若续 <3 → streak=2；再一轮 <3 → streak=3 触 §3(2) CLOSE place → event。
5. **HK-dupcheck-bareterm-vs-slug**〔R223 记〕：bare-term gather ≥5 ≠ 可建，须 exact-slug 核。本轮已遵。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿达标）。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=161→162（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
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
