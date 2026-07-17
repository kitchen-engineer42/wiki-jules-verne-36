---
round: 140
date: 2026-07-15
type_round: 111
phase: "2.1"
current_type: place
gene: NEW1
pages: [connecticut]
result: success
---

# GROW 2.1-B · R140 · NEW1 · place — 建 connecticut（An Antarctic Mystery Jeorling 故乡，7PN，散文守 ≤400 门）

## 执行摘要

Phase 2.1-B place 广度扩张第 111 轮（type_round 111）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、streak=0<3、queue≈14≥10、since_discover=0<10、queue(place)>0、stub%=0 → §3(7)）。
消费 R139 SCN28 新种 **Connecticut**（7 solid distinctPN，An Antarctic Mystery 主源）。

**消歧裁定**：定主体为**州**，Vernean 意义核心为《An Antarctic Mystery》（Sphinx of the Ice Fields）
叙述者 **Jeorling 的故乡州**——反复言及归乡（Providence 归属）、与 Arthur Gordon Pym 家族关联。
加 MW×2（Terror 巡 Connecticut 岸 / Bridgeport The Protector 两栖艇）+ RC×1（1882 CT 暴风为 Robur 风速对照）=7 distinctPN。
剔 DSCF-019-010（废奴州列举泛指）、RM-023-013（巡游州列举）。

**散文纪律续守（承 R138 EVV5 自纠）**：add_page 首版四段过 400（Overview 426/Narrative 505/Geography 450/
Connections 555），随即 edit_page 分段复拆，**max para 374 ≤400**。本轮不再新增散文债（对比 R131–R136 五页自致）。

place 计数 353→354，registry total 1421→1422，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈14≥10、since_discover=0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| connecticut | 1j3x7g | An Antarctic Mystery | real | United States | 7 | 州/Jeorling 故乡（Providence 归属、Pym 家族关联）；MW Terror 巡岸 + Bridgeport The Protector；RC 1882 暴风对照 |

- **connecticut**：7 distinct PN — AM-001-019（归 Connecticut/Providence 首府）/003-048（"You come from Connecticut?"）/004-023（belonging to Connecticut + Nantucket/Pym）/007-038（"Mr. Jeorling, of Connecticut"）、MW-006-025（Terror scurrying along Connecticut shores）、MW-007-055（Bridgeport The Protector 水陆两栖艇）、RC-018-016（1882-03-22 Connecticut 暴风 300mph，Robur 对照）。三源 AM(4)/MW(2)/RC(1)。剔 DSCF-019-010 废奴州列举泛指、RM-023-013 巡游列举。链 an-antarctic-mystery/the-master-of-the-world/robur-the-conqueror。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：connecticut 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：max para 374（首版四段过门，edit_page 分段复拆后达标）。✔
- **G3 ≥5 distinct PN**：7（AM×4 + MW×2 + RC×1；剔泛指 2 项）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 复拆，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2（Overview/In the Narrative/Geography & Features/Connections），无 H1，Connections 散文。✔
- **registry 一致**：total 1422 place 354 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R141 起始计数）

| 字段 | R140 起始 | R141 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 140 | 141 |
| type_round | 111 | 112 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 76 | 77 |
| last_updated_round | 140 | 141 |

## 遗留问题

1. **place 页数 354**：本轮 +1。registry 全库 1422，unknown 0。
2. **下轮 R141 = NEW1**：since_evv5=2<10、streak=0、queue≈13≥10、since_discover=1<10 → §3(7) NEW1。
   建议序（承 R139 discover）：Sacramento（AWED/GM 加州）→ Pennsylvania（DSCF/MW）→ Kentucky（Mammoth Cave）→ Massachusetts（Salem/granite/MW）。
3. **待筛/DEFER 项**：Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Soudan/Guinea/Abyssinia/Indiana（既有 queue）。
4. **散文门债**：37 页 >400（既有 DEFERRED，RFC 后 edit_page 复拆）；**本轮页 over-400=0**（首版过门即就地复拆，纪律续守）。
5. **EVV5 节奏**：since_evv5=2，下次约 R149。
6. **corpus-discover 顺延临界**：since_corpus=76，远过阈 30 但非 §3 分支（HK-corpus-discover-not-in-statemachine PARK）。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧。
