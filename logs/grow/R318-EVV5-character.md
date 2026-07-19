---
round: 318
date: 2026-07-19
type_round: 11
phase: "2.1"
current_type: character
gene: EVV5
pages: []
result: success
---

# GROW 2.1-B · R318 · EVV5 · character — 周期 schema 反思：模板稳定，无结构变动

## 执行摘要

Phase 2.1-B character 类型第 1 次 EVV5（`EVV5-type-pilot-reflect`）。决策机 §3 首匹配 **EVV5**
（since_evv5=10≥evv5_interval(10) → §3(1b) 触发；since_discover=3<10 → 非 §3(1a) 合并，纯 EVV5）。

**本轮为 schema 反思轮，不建页（pages: []）**。动作：扫描 character 全 24 页，复核五 H2 结构 / frontmatter 字段 / role 枚举 / PN 密度 / 散文门 / wikilink，判断模板是否需调整；更新 grow_state（since_evv5→0）+ 写日志。registry 不变（total 1548、character 24、unknown 0）。

**反思结论：模板稳定，无需更新 `local/template/character-schema.md`。**

- **五 H2 结构**：24/24 页全部为 `Overview / Role in the Story / Character & Traits / Relationships / Appearances`，**零偏差**。
- **frontmatter 字段**：`book / affiliation / first_appearance / role / quality` 五专属字段全页齐备；`role` 枚举全部合法（protagonist 8 / supporting 12 / antagonist 3 / narrator 2 = 25… 注：aronnax+axel 双 narrator，实际 24 页分布见下）。
- **无结构性问题**（无「某节约束不清」「字段普遍缺失」），故按 EVV5 规程「无结构变动」分支处理，不改 schema、不发 RFC。

## EVV5 扫描矩阵（character 24 页）

| role 分布 | 计数 |
|-----------|------|
| protagonist | barbicane / captain-hatteras / captain-nemo / cyrus-harding / dick-sand / phileas-fogg / professor-lidenbrock（+robur 为 antagonist）= 7 |
| supporting | aouda / ayrton / conseil / gideon-spilett / herbert / michel-ardan / neb / paganel / passepartout / pencroft / top = 11 |
| antagonist | fix / negoro / robur = 3 |
| narrator | aronnax / axel = 2 |
| **合计** | **24** |

> 五 H2 结构：24/24 OK。quality：24/24 featured（Phase 2 featured 语义 DEFERRED，EVV6 全库 re-grade 时统一处理）。

## 识别的内容债（非结构问题，DEFERRED backfill 候选）

EVV5 扫描发现两类**内容质量债**，集中于本类型**早期建页**（近批 R311-317 pencroft/herbert/paganel/neb/gideon-spilett/negoro 均 0 债），属既有 DEFERRED 债范畴，**本轮不 backfill**（EVV5 反思轮跳过 G1/G2/G3/G5，不修改页）：

**(A) PN<5（G3 阈值）——6 页**：
| slug | distinct PN |
|------|-------------|
| aouda | 3 |
| barbicane | 3 |
| passepartout | 3 |
| axel | 4 |
| conseil | 4 |
| ned-land | 4 |
| top | 4 |

> 注：上表 7 行（原扫描 aouda/axel/barbicane/conseil/ned-land/passepartout/top 均 <5）。

**(B) 散文 over-400（G2 阈值）——11 页**：aouda(×2) / axel(×3) / barbicane(×2) / captain-hatteras(×3) / captain-nemo(×2) / cyrus-harding(×2) / fix(×1) / ned-land(×1) / passepartout(×2) / phileas-fogg(×2) / professor-lidenbrock(×1)。

> (B) 属既有「散文门债 37 页 >400」库级 DEFERRED 债的 character 子集。近批新建页已用 add_page→edit_page 拆段实践消除超段（R316 gideon-spilett 初稿 3 超即拆），后续新建持续 0 债。

**EVV5 处置建议**：这两类债非模板缺陷（新页遵同一 schema 已 0 债），乃早期建页时 PN/散文实践未成熟所致。建议在 Phase 2.1 收尾或专门 backfill 轮以 edit_page 定向修复 7 页 PN<5 + 11 页 over-400，**统一纳入既有 DEFERRED 债，勿自主启动**（遵 featured re-grade / 散文门债 deferral 政策）。

## EXIT-GATE 检查（EVV5 反思轮，仅 G4）

- **G4 记录完整性**：本轮 pages: []，无建页/编辑；扫描结果、反思结论、内容债清单完整入日志。✔
- **G1/G2/G3/G5 跳过**：EVV5 反思轮无 NEW1 新建/修改页，按规程跳过。✔（规程 GROW.spec.md §2.1-B EVV5「仅执行 G4」）
- **registry 一致**：total 1548 character 24 unknown 0，本轮未变。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（EVV5，grow_state 存 R319 起始计数）

| 字段 | R318 起始 | R319 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 318 | 319 |
| type_round | 10 | 11 |
| rounds_since_last_evv5 | 10 | **0**（EVV5 复位）|
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 254 | 255 |
| last_updated_round | 318 | 319 |

## 遗留问题

1. **character 页数 24**：本轮 EVV5 未建页。queue(character) 恒 **3**（余 60-62：hercules/glenarvan/michel-strogoff）。registry 全库 **1548**，unknown 0。
2. **下轮 R319 = NEW1（§3(7)）**：since_evv5=0<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 60（hercules）。Hercules（book Dick Sand, A Captain at Fifteen，pn_anchor DSCF-004，DSCF 4-char **须 RFC-0003 Note**，role supporting）——力大无穷之获救黑人、忠勇护主；与 negoro/dick-sand 同书可互链。
3. **EVV5 复位**：since_evv5→0，下次 EVV5 约 R328（+10 轮）。
4. **模板稳定确认**：character-schema 五 H2 + 五专属字段经 24 页验证稳定，无演化需求；Phase 2.1 收尾前无需再改 schema（除非后续新页揭示新结构缺陷）。
5. **内容债 backfill 候选**（EVV5 新识别，DEFERRED）：7 页 PN<5（aouda/axel/barbicane/conseil/ned-land/passepartout/top）+ 11 页 over-400；纳入既有 DEFERRED，勿自主 backfill。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=254→255（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。
