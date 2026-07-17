---
round: 171
date: 2026-07-16
type_round: 142
phase: "2.1"
current_type: place
gene: EVV5
pages: []
result: success
---

# GROW 2.1-B · R171 · EVV5 · place — 周期 schema 反思：4-H2 结构全库稳定（377/377），legacy H1 遗留 150 页记为新 housekeeping；模板无需变更

## 执行摘要

Phase 2.1-B place 周期质量检查（type_round 142）。决策机 §3 首匹配 **EVV5**
（since_evv5=10≥10 → §3(1b)；since_discover=0<10 故非 §3(1a) 合并式）。**本轮不建页**，
对 place 类型全部 **377 页**执行 schema 反思，EXIT-GATE 仅核 G4 + 不变量。

**核心结论：place 模板结构全库稳定，无需变更。**
- **4-H2 结构 377/377 全合规**：所有 place 页恰含 `Overview / In the Narrative / Geography & Features / Connections`
  四 H2 且顺序正确（`non-standard H2 order/set: 0`）。schema 核心约束零漂移。
- **必填字段齐备**：`book`/`real_or_fictional`/`region`/`description` 缺失均为 0（pages.json 仅投影 book，
  实测页文件 frontmatter 四字段全备）。
- **GROW 建页纪律清洁**：自 R160 EVV5 起 7 页（Kachgar/Tachkend/Douchak/Concepcion/Sou-Tcheou/Lan-Tcheou/Tai-Youan）
  逐页复检 H1=0、H2=4、字段全 —— add_page.py 建页管线合规，无结构漂移。

**发现一项 legacy 遗留（非 schema 缺陷，记 housekeeping 不即行）**：
- **legacy H1 内嵌 150 页**：150 个 place 页携带一个 H1 标题（`# {Label}`），与现行 place-schema「无 H1」相悖。
  经比对，命中者皆为 **GROW Phase 2.1-B 之前**的 butler/BIRTH 批建页（如 aberfoyle/aleutian-islands/
  atlantic-ocean/baffin-bay 等地理泛类页）；本阶段 add_page 建页无一命中。
- 按 EVV5 规则「结构性问题 → 更新 schema + backfill + 写 RFC」本应触发批量回填，但：
  (1) RFC 全线 PARK（不自主 file）；(2) 存量批量 backfill 属 DEFERRED（featured 全库 re-grade 同批待办）；
  (3) 页面仅经 edit_page.py 改，禁 Write/Edit。**故记为新 housekeeping 项 HK-legacy-h1-in-place-pages，
  不即行**。本阶段建页纪律已恒定 omit H1，向前无漂移。
- `quality` 字段存在 361 页 —— 系 add_page.py 建后自动回填（featured），非违规；source 侧 omit、脚本侧 backfill 为既定行为。

**EVV5 裁定：模板稳定，无需更新**（schema 设计无缺，遗留仅存量 legacy 一致性，已 DEFER 记录）。

## 决策矩阵（EVV5）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10、since_discover=0 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10 达门** | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| — | 否（1b 已先匹配）|
| 4 | SCN28-zombie（queue(place)==0）| — | — |
| 5/6 | RCH2 系（stub%≥15）| — | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 EVV5 schema 反思，无建页无改页。全库 place 结构扫描结果：

| 检查项 | 结果 | 判定 |
|--------|------|------|
| place 页总数 | 377 | — |
| 4-H2 结构合规（顺序+集合）| 377/377 | ✔ 零漂移 |
| H1 内嵌（schema 禁）| 150（皆 legacy 批建）| ⚠ 记 HK-legacy-h1-in-place-pages（DEFER）|
| 缺 book / real_or_fictional / region / description | 0 / 0 / 0 / 0 | ✔ 字段齐备 |
| GROW R160+ 建页（7 页）H1/H2 复检 | H1=0、H2=4 全数 | ✔ 建页纪律清洁 |
| quality 字段存在 | 361（add_page 自动回填）| — 非违规 |

## EXIT-GATE 检查

EVV5 无建页/改页，EXIT-GATE 仅核 G4 + 不变量（跳过 G1/G2/G3/G5）：

- **G4 无 Write/Edit 建页**：本轮未建/改页，仅 Edit grow_state.json + 写 log。✔
- **I1 registry 一致**：未动页面，registry 不变（total 1445 place 377 unknown 0）。✔
- **I2 grow_state 与 log 同步**：last_updated_round=172 与本轮末一致。✔
- **I3（查重）**：EVV5 无新建，不适用。✔
- **I4（candidate honest）**：EVV5 无候选，不适用。✔
- **I5（模板反思记录）**：本 log 载全库扫描结论「模板稳定」+ legacy H1 遗留登记。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（EVV5，grow_state 存 R172 起始计数）

| 字段 | R171 起始 | R172 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 171 | 172 |
| type_round | 142 | 143 |
| rounds_since_last_evv5 | 10 | **0（RESET）** |
| rounds_since_last_discover | 0 | **1** |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 107 | 108 |
| last_updated_round | 171 | 172 |

## 遗留问题

1. **place 页数 377**：本轮 EVV5 无建。registry 全库 1445，unknown 0。
2. **下轮 R172 = NEW1**：since_evv5=0<10、since_discover=1<10、queue>0、stub%=0 → §3(7) NEW1。
   建 R170 discover 批首项 **Kazeh**（16 distinctPN，FWB 白尼罗河商旅 rendezvous），建前抽样 ≥5 solid。
3. **R172 起建序**：Kazeh → Gondokoro → Carmen(re-vet 剔命名段) → Tandil(Sierra vs village 消歧) →
   Mozambique(严剔，大概率 DEFER)。
4. **EVV5 裁定「模板稳定」**：4-H2 结构全库 377/377 合规，字段齐备，GROW 建页管线零漂移。schema 无需变更。
5. **新增 housekeeping — HK-legacy-h1-in-place-pages**：150 legacy place 页内嵌 H1（schema 禁），
   皆 GROW 2.1-B 前批建。批量 backfill 属 DEFERRED（RFC PARK + featured 全库 re-grade 同批），
   与 HK-addpage-prose-gate-bypass（37 页 >400）同性质——存量一致性债，待阶段末批处理。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮无建页。
7. **corpus-discover 顺延**：since_corpus=107→108（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
   Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3；待定 Mozambique。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    **HK-legacy-h1-in-place-pages（新，150 页）**、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
