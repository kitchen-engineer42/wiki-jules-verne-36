---
round: 142
date: 2026-07-15
type_round: 113
phase: "2.1"
current_type: place
gene: NEW1
pages: [pennsylvania]
result: success
---

# GROW 2.1-B · R142 · NEW1 · place — 建 pennsylvania（Robur Weldon Institute/Philadelphia，8PN，引注对齐修正）

## 执行摘要

Phase 2.1-B place 广度扩张第 113 轮（type_round 113）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、streak=0<3、queue≈12≥10、since_discover=2<10、queue(place)>0、stub%=0 → §3(7)）。
消费 R139 SCN28 新种 **Pennsylvania**（8 solid distinctPN，Robur the Conqueror 主源）。

**消歧裁定**：Vernean 核心为《Robur the Conqueror》Weldon Institute（Walnut St, Philadelphia, PA）——
Robur 闯气球俱乐部、Albatross 离「宾州首府」、Fairmount Park 现身。加《Dick Sand》Tom 等自由黑人
「State of Pennsylvania 公民」+《The Master of the World》Terror 剧场州 +《The Waif of the "Cynthia"》石油矿。
**剔州列举泛指**：AWED-031-037（Indiana/Ohio/PA/NJ）、DSCF-019-010（废奴州列举）、MW-008-044（自动车穿六州）、
MW-011-021（五大湖边界州列举）、RM-023-013（巡游州列举）。净 solid = 8（RC×4+DSCF×2+MW×1+WC×1）。

**引注对齐修正（诚实记录）**：add_page 首版 Connections 收束句将 (MW-004-013)/(WC-022-004) 挂在综合陈述句上，
pn_validator warn 关键词重叠 0%/1%（<2% 阈）。此为**引注放置不当**——PN 虽真实且已在正文段确指，但收束句
词面不匹配。edit_page 两次修正：终改收束句引 DSCF-004-043（"return to the State of Pennsylvania"，词面对齐），
MW/WC 保留在「In the Narrative」确指段。strict 复核 ✓ 全通过。承 GROW-JUDGMENT：引注须句内词面可溯，非仅 PN 真。

place 计数 355→356，registry total 1423→1424，unknown 恒 0。散文 max para 358 ≤400。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈12≥10、since_discover=2 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| pennsylvania | ghSEt5 | Robur the Conqueror | real | United States | 8 | 州；RC Weldon Institute/Philadelphia/Albatross/Fairmount Park；DSCF 自由黑人所属州；MW Terror 剧场；WC 石油矿 |

- **pennsylvania**：8 distinct PN — RC-002-016（Weldon Institute, Walnut St, Philadelphia, PA）/005-037（Philadelphia+PA 报道）/009-011（Albatross 离宾州首府）/022-014（Fairmount Park, 宾州首府）、DSCF-004-023（"subjects of the State of Pennsylvania, citizens of free America"）/004-043（Tom 归 State of Pennsylvania, Weldon 家）、MW-004-013（PA 为 Terror 剧场州）、WC-022-004（PA 石油矿 Erik 继承）。四源 RC(4)/DSCF(2)/MW(1)/WC(1)。剔 5 项州列举泛指。链 robur-the-conqueror/dick-sand-a-captain-at-fifteen/the-master-of-the-world/philadelphia。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：pennsylvania 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过（首版 2 项 warn 经 edit_page 引注对齐修正后清零）。✔
- **G2 段落 ≤400 字**：max para 358。✔
- **G3 ≥5 distinct PN**：8（RC×4+DSCF×2+MW×1+WC×1；剔 5 项州列举泛指）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 引注修正，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1424 place 356 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R143 起始计数）

| 字段 | R142 起始 | R143 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 142 | 143 |
| type_round | 113 | 114 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 78 | 79 |
| last_updated_round | 142 | 143 |

## 遗留问题

1. **place 页数 356**：本轮 +1。registry 全库 1424，unknown 0。
2. **下轮 R143 = NEW1**：since_evv5=4<10、streak=0、queue≈11≥10、since_discover=3<10 → §3(7) NEW1。
   建议序（承 R139 discover）：Kentucky（FF Mammoth Cave/JCE 猛犸洞）→ Massachusetts（Salem/granite/MW）。
3. **待筛/DEFER 项**：Virginia/Louisiana（solid 边界，建前凑句）、Arkansas（多 Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）、Missouri/Ohio/Colorado（疑河）、Michigan（vs lake-michigan）、Illinois（泛指列举待筛）、Soudan/Guinea/Abyssinia/Indiana（既有 queue）。
4. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
5. **引注对齐教训**：Connections 综合句慎挂 PN；PN 真实 ≠ 句内可溯，须词面对齐。已 warn→修正闭环，无残留。
6. **EVV5 节奏**：since_evv5=4，下次约 R149。
7. **corpus-discover 顺延临界**：since_corpus=78（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
