---
round: 167
date: 2026-07-16
type_round: 138
phase: "2.1"
current_type: place
gene: NEW1
pages: [sou-tcheou]
result: success
---

# GROW 2.1-B · R167 · NEW1 · place — 建 sou-tcheou（ASC 单源 8PN，长城西端/Grand Transasiatic 华属段城）

## 执行摘要

Phase 2.1-B place 广度扩张第 138 轮（type_round 138）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、streak=0<3、since_discover=0<10、queue(place)>0、stub%=0 → §3(7)）。
承 R166 SCN28 discover 建序（**Sou-Tcheou**→Lan-Tcheou→Baikal→Tai-Youan），建第 1 项 Sou-Tcheou。

**消歧裁定**：Sou-Tcheou = Grand Transasiatic 铁路华属段城（长城内），Vernean 归属**全在《The Adventures
of a Special Correspondent》**——抵站电报修复处（ASC-022-050）、停 2h 奔电报局（022-061）、
despatch dateline「Sou-Tcheou, 25th May, 2:25 P.M.」（022-063）、2h 访城（022-066）、
双 town（Tai-Tchen 外/Le-Tchen 内）Mussulman 破↔华复得（022-068）、双墙内复兴（022-069）、
**长城西端确指**（022-071 the Great Wall of China ends）、补给（023-002）。
净 solid = 8（全 ASC 单源，城主体确指，无 enumeration）。

place 计数 374→375，registry total 1442→1443，unknown 恒 0。
**建后拆段**：首版 Geography 494、Connections 408 超 G2 门 → edit_page 拆 Geography 为二段、Connections 收紧，
末版全段 ≤400（395/324/200/257/236/364）。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10、R166 补种 queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| sou-tcheou | tQjgfo | The Adventures of a Special Correspondent | real | China | 8 | Grand Transasiatic 华属段城；长城西端；双 town Tai-Tchen/Le-Tchen |

- **sou-tcheou**：8 distinct solid PN — ASC-022-050（抵站电报修复）/022-061（停 2h 奔电报局）/022-063（despatch dateline）/022-066（2h 访城）/022-068（双 town 战破）/022-069（双墙复兴）/022-071（长城西端）/023-002（补给）。ASC 单源。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：sou-tcheou 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 Geography 494/Connections 408 超门 → edit_page 拆分/收紧；末版全段 ≤400。✔
- **G3 ≥5 distinct PN**：8（ASC 单源，全 solid，无 enumeration）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 拆段，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1443 place 375 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R168 起始计数）

| 字段 | R167 起始 | R168 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 167 | 168 |
| type_round | 138 | 139 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 103 | 104 |
| last_updated_round | 167 | 168 |

## 遗留问题

1. **place 页数 375**：本轮 +1（Sou-Tcheou）。registry 全库 1443，unknown 0。
2. **下轮 R168 = NEW1**：since_evv5=7<10、since_discover=1<10、queue>0 → §3(7) NEW1。
   建 **Lan-Tcheou**（R166 discover 序第 2，ASC 华属段重镇，8 distinctPN，抽样 ≥5 solid）。
3. **R166 discover 建序进度**：✔Sou-Tcheou → **Lan-Tcheou**(下轮) → Baikal(re-vet) → Tai-Youan(re-vet)；Yeniseisk/Tioumen 建前严剔。
4. **净 buildable**：R166 补 6 项，消 1（Sou-Tcheou），余 5（Lan-Tcheou/Baikal/Tai-Youan/Yeniseisk/Tioumen，后三 re-vet）。
5. **建后拆段复现**：Sou-Tcheou 首版两段超 400——ASC 城史信息密度高易超门。后续 ASC 城页首版即压缩段落，减少 edit 往返。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页末版 over-400=0。
7. **EVV5 节奏**：since_evv5=6→7，约 R171 触发。
8. **corpus-discover 顺延**：since_corpus=103→104（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、Colorado/Michigan 河湖歧义；R166 待定 Yeniseisk/Tioumen。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
