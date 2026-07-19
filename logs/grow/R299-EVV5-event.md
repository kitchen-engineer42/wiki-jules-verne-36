---
round: 299
date: 2026-07-19
type_round: 65
phase: "2.1"
current_type: event
gene: EVV5
pages: []
result: stable
---

# GROW 2.1-B · R299 · EVV5 · event — event 类型全库 schema 反思（60 页），模板稳定无结构变动，PN/散文门债评审记录

## 执行摘要

Phase 2.1-B event 类型 EVV5 周期反思轮（type_round 65）。决策机 §3 首匹配 **§3(1b) EVV5**
（since_evv5=10≥10 → §3(1) 触发；since_discover=1<10 → §3(1a) EVV5+SCN28 否；**§3(1b) 纯 EVV5 触发**）。

**EVV5 = schema 反思轮，不建页**。EXIT-GATE 仅执行 G4（记录完整性），跳过 G1/G2/G3/G5（本轮无 NEW1 新建/修改页）。
扫描 event 类型**全库 60 页**，反思 event-schema 是否需结构性调整。

**扫描结论：模板稳定，无需更新。**
- **H2 结构**：60/60 页均为 event-schema 标准四 H2（Overview / What Happens / Significance / Participants & Setting），零偏差。
- **frontmatter 字段**：60/60 页均含类型专属字段 book / location / pn_anchor，零缺失。
- **type 一致**：60/60 页 type=event，registry unknown=0。
- **结论**：event-schema 无结构性问题（无某节约束不清、无字段普遍缺失）→ **不改 `local/template/event-schema.md`，不 backfill schema，不起 RFC**。继续建页节奏（R300 起 NEW1）。

## 全库债务评审（记录，零消解 — 沿 R288 EVV5 惯例）

### 债务一 · PN 回填债（13 页 <5 distinct PN）

早期 pilot 期页面单指 PN 不足门（<5），与 R288 EVV5 记录同批（13 页），本轮无新增、无消解：

| distinct PN | slug |
|-------------|------|
| 3 | date-line-revelation |
| 3 | liedenbrock-cipher |
| 3 | snaefells-descent |
| 4 | columbiad-launch |
| 4 | fogg-hires-passepartout |
| 4 | gun-club-moon-proposal |
| 4 | lincoln-island-landing |
| 4 | lunar-orbit-miss |
| 4 | nemo-death |
| 4 | north-pole-volcano |
| 4 | sea-monster-hunt |
| 4 | stromboli-eruption-return |
| 4 | tabor-island-castaway |

> 均 ≥3 PN（逾 G3 硬门 ≥5 的旧标准之前建；现行 target 8，近轮页稳定 16-17 PN）。**DEFERRED**：批量回填留 Phase 2.1 关闭前 event EVV6 统一处理，本轮零消解。

### 债务二 · 散文门债（37 页含 >400 字段落，43 段实例）

`awk RS="\n\n"` 全库扫描：37 distinct event 页存在 >400 字段落（部分页 2-3 段超门，如 nemo-death×3、sea-monster-hunt×2、north-pole-volcano×2、lunar-orbit-miss×2、fogg-hires-passepartout×2），计 43 段实例。最长 assault-on-irkutsk 671c、destruction-of-back-cup 664c、great-eyrie-investigation 641c、wreck-of-the-albatross 625c。

> 与既有「37 页 >400」DEFERRED 债一致，本轮无新增（近轮 NEW1 页建时已拆超段，over-400=0）。**DEFERRED**：留末批 featured re-grade / 散文门统一整改，本轮零消解。

## 决策矩阵（EVV5）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| **1a** | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10；since_discover=1<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10≥10** | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | — |
| 3 | SCN28（queue<10 或 since_discover≥10）| — | — |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | — |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

（EVV5 反思轮，不建页；全库 60 页扫描，模板稳定）

## EXIT-GATE 检查

- **G4 记录完整性**：本轮 EVV5 不建页，无 pages/** 写入；日志 frontmatter 完整（gene EVV5、pages []、result stable）。✔
- G1/G2/G3/G5：本轮无 NEW1 新建/修改页，跳过。—
- **registry 一致**：不建页，total 1535 event 60 unknown 0 不变。✔
- **schema 反思**：60/60 页四 H2 + book/location/pn_anchor 齐备，模板稳定无结构变动。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（EVV5，grow_state 存 R300 起始计数）

| 字段 | R299 起始 | R300 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 299 | 300 |
| type_round | 65 | 66 |
| rounds_since_last_evv5 | 10 | 0 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 235 | 236 |
| last_updated_round | 299 | 300 |

## 遗留问题

1. **event 页数 60**：本轮 EVV5 不建页。queue(event)=**2**（余建序 47 return-of-ole-kamp、48 lima-indian-uprising）。registry 全库 **1535**，unknown 0。
2. **下轮 R300 = NEW1（§3(7)）**：since_evv5=0（EVV5 已重置）→ §3(1) 否；streak=0<3；since_discover=2<10 且全局 queue≥10 → §3(3) 否；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 47 return-of-ole-kamp（TN，anchor TN-020）**。TN 2-char 无需 Note；逐句核 TN-020 Ole Kamp 生还归 Christiania 与 Hulda 重逢、中头奖序列、剔 christiania-lottery-drawing 开奖别线。
3. **EVV5 已执行**：since_evv5 归 0；下次 EVV5 于 R309（10 轮后）。event-schema 模板稳定，无结构变动。
4. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论；R300 建序 47 建时逐句复核 TN-020。教训延续（R283 改锚 / R286 改锚+改 slug）。
5. **event 覆盖策略·余矿**：单事件作品第二事件矿脉已建十六部（…/TT/ASC/WC/WAI），queue 余 TN/PL 二候选（建后共十八部）。MZ(5c)/GM(22c overlap-watch) 薄矿留察；BR/DOSE 判饱和；DA/SI/MI 排除。event 二次矿将近竭，type_close 判据渐近（连续 discover new_candidates<3 三轮则 CLOSE+SCN28 切 character）。
6. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
7. **event PN 回填债**：13/53→13/60 早期页 <5 PN，DEFERRED，本轮 EVV5 记录、零消解；留 event EVV6 统一回填。
8. **散文门债**：37 页 >400（43 段实例），既有 DEFERRED，本轮 EVV5 记录、零消解。
9. **corpus-discover 顺延**：since_corpus=235→236（dead 变量）。
10. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债 + 散文门债。
11. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
