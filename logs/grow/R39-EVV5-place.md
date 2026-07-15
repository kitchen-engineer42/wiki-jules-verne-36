---
round: 39
date: 2026-07-15
type_round: 11
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: schema-stable
---

# GROW 2.1-B · R39 · EVV5 · place — place schema 反思轮（52 页）

## 本轮公告

**R39 — Phase 2.1 — EVV5 — place — 0 建页 / 不消费队列 / schema 稳定性反思**

轮首 `rounds_since_last_evv5=10 ≥ 10`（R38 末达 10，承 R20 先例轮首触发）。决策矩阵优先级
1a 判否（since_discover=2 < 10），落 **1b EVV5**。本轮为 place 类型 schema 反思轮：
不建页、不消费队列，扫全 52 place 页评模板稳定性 + 反哺，EXIT-GATE 仅 G4。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=10, since_discover=2 | 否 |
| **1b** | **EVV5（since_evv5 ≥ 10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | — |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=15, since_discover=2 | — |
| NEW1（默认）| — | — | — |

## 反思方法

样本：全部 52 place 页（Pilot 8 + GROW 44）。逐页解析 frontmatter + body，量五维：
H2 结构 / PN 接地数（去重）/ 散文字符数 / wikilink 数 / 类型专属字段完整性。

## 稳定性维度表

| 维度 | 观测 | 判定 |
|------|------|------|
| **H2 结构** | 52/52 页均为 4 H2：Overview / In the Narrative / Geography & Features / Connections。无缺节、无越界节。| ✅ 100% 一致 |
| **PN 接地** | distinctPN 范围 4–14，中位 ~8。全页 ≥4（standard 门 ≥5 达标 50/52；仅 hong-kong=4、snaefellsjokull=4 两 Pilot 页低于 5）| ✅ 达标（两 Pilot 边界记 HK）|
| **散文体量** | prose 1289–2876 字符。最小 reform-club(1289)、最大 stony-hill(2876)。无空节、无超薄页。| ✅ 稳定 |
| **wikilink** | 0–12 条。5 页零链（christmas-harbour / gourbi-island / lake-kirdall / pacific-railroad / spencer-island），均因源作暂无既有页可链，Connections 用纯文本——schema 允许。| ✅ 合规 |
| **类型专属字段** | book / real_or_fictional / region 三必填字段 52/52 全present（frontmatter 层）。| ✅ 完整 |

## 结论

**place-schema 稳定，无需变更。** 四段式模板经 44 轮 GROW 扩张（38→52 页）结构零漂移；
PN 接地、散文体量、字段完整性均在健康区间。**不更新模板、不回填、不起 schema RFC。**

## EXIT-GATE 检查

| 门 | 结果 | 说明 |
|----|------|------|
| G4 记录完整性 | PASS | 本日志；queue 不消费（EVV5 反思轮）；grow_state six-step |

> EVV5 反思轮仅核 G4（不建页故 G1 PN / G2 散文门 / G3 schema 不适用）。

## state 更新（EVV5 six-step）

`current_round 39→40`；`type_round 10→11`；`rounds_since_last_evv5 10→0`（重置）；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 6→7`；`last_updated_round→40`。

## 遗留问题（housekeeping）

1. **两 Pilot 页 PN=4 低于 standard 门（≥5）**：hong-kong、snaefellsjokull 系 GROW 前 Pilot 建页，
   PN=4。非本轮扩张产物，不阻塞；若未来深度轮（Phase 3）触及可补引。记录不处置。
2. **registry typefield 未透传**（承 PARK）：`pages.json` 未携带 `real_or_fictional`/`region`，
   本轮扫描该二字段须回读 frontmatter（脚本内 real/fictional 计数从 registry 取值全落 other）。
   八项债务之一，PARK/记录，不起 RFC。
3. **queue(place) 余 15**：R36 补种 26 − R37 消费 5 − R38 消费 6 = 15。R40 恢复 NEW1，
   下批优选：Lake Erie(MW:27) / Fort Providence(ACH:22) / Beechey Island(ACH:20) /
   Gulf Stream(TTLU:18) / Torres Strait(TTLU:15) / Polar Sea(FC:14)。建前逐页复核 distinctPN、查同实体合并。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录。
