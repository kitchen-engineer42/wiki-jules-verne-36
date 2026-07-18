---
round: 222
date: 2026-07-18
type_round: 193
phase: "2.1"
current_type: place
gene: NEW1
pages: [kamtchatka-current]
result: success
---

# GROW 2.1-B · R222 · NEW1 · place — 建 Kamtchatka Current（白令海域寒流，FC×15 单指；挟浮岛漂向北极孤域，与 Behring Current 反向）

## 执行摘要

Phase 2.1-B place 广度扩张第 193 轮（type_round 193）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、since_discover=3<10、queue(place)=1>0、全局 queue_size≥10〔HK-queue-size-scope〕、stub%=0 → §3(7)）。

取 R218 SCN28 队列**建序 4（末项）** **Kamtchatka Current**（FC 主）。建前 pages.json 子串（kamtchatka/kamchatka）+
`the-` 前缀双查皆 NEW。**单作品单指**：FC×15 = 15 distinctPN 全指 The Fur Country 中白令海域那条寒流，
无同名异指。**净 14 distinct solid PN**（远超门）：

- **FC-025-025**：其一名曰 Kamtchatka Current。
- **FC-025-026**：东至西距岸约百里，于海峡口相撞后南折趋 Russian America。
- **FC-040-015**：沿亚洲海岸而行。
- **FC-025-033**：Cape Bathurst 外唯一北西向之流，即危险的 Kamtchatka Current。
- **FC-031-024**：浮岛日近该寒流，恐被挟往北。
- **FC-033-026**：岛终入其掌，漂向北极孤域冰山之生地。
- **FC-033-032**：循其course 越 Cape Bathurst 外七十度。
- **FC-025-031**：于海峡或循 Kamtchatka Current 往西北，或随 Behring Current 南没。
- **FC-038-007**：两流反向——寒流北行而解冻期冰沿 Behring Current 南下。
- **FC-039-014**：Hobson 恐寒流先挟岛北去，不及入 Behring Current。
- **FC-025-038**：最安处在寒流与岸间某未标于图之大涡。
- **FC-038-006**：正是此寒流挟众至此，解冻期或复挟远去。
- **FC-039-027**：岛动，众问是否 Kamtchatka Current 所致。
- **FC-035-009**：Hobson 惧蚀岛终被携往太平洋或复被寒流所挟。

place 计数 415→416，registry total 1483→1484，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 2 段 >399（含一 =400），拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region North Pacific、book The Fur Country、aliases=[]。
Connections/正文含 [[Russian America]]/[[Cape Bathurst]]/[[Arctic Ocean]]（三页均存；Behring Current 无页，行文纯文本）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 建毕队列罄（R218 SCN28 4 项全消费）→ **R223 = SCN28**（§3(4) zombie）。届时转**单词地名扫**。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| kamtchatka-current | zGQiaT | The Fur Country | real | North Pacific | 14 | 白令海域寒流；挟浮岛漂北极；与 Behring Current 反向；FC 单指 |

- **kamtchatka-current**：14 distinct solid PN（FC 单指）；aliases []。链 Russian America/Cape Bathurst/Arctic Ocean。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 FC Kamtchatka Current；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：14 solid（FC 单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（三 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1484 place 416 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（kamtchatka/kamchatka）+ `the-` 前缀双查皆 NEW。✔
- **单作品单指核**：FC 逐句确认同指一寒流，采全；洋流亦地理实体（承 place 广义）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R223 起始计数）

| 字段 | R222 起始 | R223 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 222 | 223 |
| type_round | 193 | 194 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 158 | 159 |
| last_updated_round | 222 | 223 |

## 遗留问题

1. **place 页数 416**：本轮 +1（Kamtchatka Current）。registry 全库 1484，unknown 0。R218 SCN28 队列 4 项全消费。
2. **下轮 R223 = SCN28**：queue(place)==0（R218 队列全消费）→ §3(4) zombie。
   **须转单词地名扫**：多词≥7-PN 净新池已薄；改 discover3 正则容单词 toponym（承 HK-discover-existing-type-blindspot），
   否则过早报饱和（承 HK-premature-saturation-claim）。候选池：Raleigh/Wilmington/Pamlico/Hatteras/Catawba/Behring/
   Morganton〔已建〕之外单词地名。得 ≥3 净新 → place 未饱和续 NEW1；<3 连续则 discover_streak_low 累加逼近 CLOSE。
3. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
4. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
5. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
6. **corpus-discover 顺延**：since_corpus=158→159（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
9. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/
   Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
