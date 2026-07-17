---
round: 136
date: 2026-07-15
type_round: 107
phase: "2.1"
current_type: place
gene: NEW1
pages: [iowa]
result: success
---

# GROW 2.1-B · R136 · NEW1 · place — 建 iowa（MI 林肯岛拓殖终地/AWED 铁路/RC 平原，5PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 107 轮（type_round 107）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、streak=1<3、queue 充盈、since_discover=7<10、queue(place)>0、stub%=0 → §3(7)）。
消费 place 候选 **Iowa**（5 distinctPN，The Mysterious Island 主源）。

**Oregon 跳过裁定**：原 R135 log 建议序 Oregon→Iowa，但 gather Oregon 得 8 distinctPN 中仅 2 项 solid
（FC-001-024 皮毛公司之争、RC-010-024 Albatross 掠 Oregon）；余 AWED-026-006/GM-001-004/MW-007-010 系州列举泛指、
FF-004-031 系 Oregon Inlet（北卡异指）、RC-001-042 疑误配。<5 clean → DEFER，改建 Iowa。

**Iowa 消歧**：定主体为**州**。5 solid PN：AWED-031-036（Fogg 火车横越）、MI-062-044 + SI-020-045
（Nemo 遗产购 Iowa 领地安置林肯岛拓殖者，两版同文异 PN）、RC-009-014/015（Albatross 掠 Iowa/西部平原）。
剔 AWED-026-006（铁路支线枚举）/MW-004-023/008-041（州列举泛指）。

place 计数 351→352，registry total 1419→1420，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≥10、since_discover=7 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| iowa | RtXYZf | The Mysterious Island | real | United States | 5 | 草原州/林肯岛拓殖终地；Nemo 遗产购 Iowa 领地；Fogg 火车经 Council Bluffs/Des Moines/Iowa City；Albatross 掠 Iowa City；西部平原至落基山 |

- **iowa**：5 distinct PN — AWED-031-036（Fogg 火车横越 State of Iowa，Council Bluffs/Des Moines/Iowa City）、MI-062-044（Nemo 遗产购 Iowa 领地安置林肯岛拓殖者）、SI-020-045（同文异版异 PN）、RC-009-014（Albatross 掠 Iowa，Iowa City）/009-015（西 Iowa/Nebraska 大平原至落基山麓）。四源 AWED(1)/MI(1)/SI(1)/RC(2)。剔 AWED-026-006 铁路支线枚举 + MW×2/GM 州列举泛指。链 phileas-fogg/around-the-world-in-eighty-days/the-mysterious-island/captain-nemo/lincoln-island/robur-the-conqueror/albatross/rocky-mountains/nebraska。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：iowa 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：5（AWED×1 + MI×1 + SI×1 + RC×2；剔泛指枚举 3 项）。✔
- **G4 脚本建页**：add_page.py（quality 自动回填 featured），未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1420 place 352 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R137 起始计数）

| 字段 | R136 起始 | R137 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 136 | 137 |
| type_round | 107 | 108 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 7 | 8 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 72 | 73 |
| last_updated_round | 136 | 137 |

## 遗留问题

1. **place 页数 352**：本轮 +1。registry 全库 1420，unknown 0。
2. **place 候选**：queue 尚余 Illinois/Michigan/Missouri/Ohio/Colorado/Wisconsin/Soudan/Guinea/Abyssinia/Indiana 等 10 候选；Oregon 已标 DEFER（<5 clean）。
3. **待筛河/湖重叠候选**：Missouri/Ohio/Colorado（疑河）、Michigan（须与 lake-michigan 区分）。
4. **下轮 R137 预测**：NEW1（since_evv5=9<10、streak=1、queue 充盈、stub%=0）。建议序 Wisconsin→Illinois（AWED/RC/MW 段，须先 gather 验 solid≥5）。
5. **EVV5 节奏**：since_evv5=9，**下轮 R137 末将达 10 → R138 起 §3(1b) EVV5 触发**（届时改跑 EVV5 评审轮，非 NEW1）。
6. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
7. **散文门债**：32 页 >400（DEFERRED）；本轮页 over-400=0。
8. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（32 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
9. **洲级 America/Europe/Asia 续 HOLD**。
