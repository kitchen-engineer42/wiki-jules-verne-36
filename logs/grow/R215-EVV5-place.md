---
round: 215
date: 2026-07-17
type_round: 186
phase: "2.1"
current_type: place
gene: EVV5
pages: []
result: reflect
---

# GROW 2.1-B · R215 · EVV5 · place — schema 反思（自 R204 EVV5 以来 10 轮，R205–R214 建 8 页 + 1 DUPLICATE + 1 SCN28 复盘）

## 执行摘要

Phase 2.1-B place 第 186 轮（type_round 186）。决策机 §3 首匹配 **§3(1b) EVV5**
（since_evv5=10≥10、since_discover=2<10 → 单 EVV5，非 EVV5+SCN28）。本轮**不建页**，
对 R205–R214 期间 place schema 实践作反思，执行后 reset since_evv5=0。

**区间产出**：R205 guamini、R206 carmen、R207 rio-colorado、R209 healthful-house、
R210 arctic-ocean、R211 upper-amazon、R213 uzun-ada、R214 saville-row（8 建页）；
R208 SCN28（+4 候选）、R212 SCN28（Celestial Empire DUPLICATE + 8 候选）。
place 计数 402→410（净 +8），registry 1470→1478，unknown 恒 0。

## schema 符合度评估

| 维度 | 观察 | 判定 |
|------|------|------|
| 四 H2 结构 | 8 页全四节（Overview / In the Narrative / Geography & Features / Connections），无空节、无 H1 | ✔ converged 保持 |
| ≥5 distinct solid PN | 8 页分别 9/7/8/11/13/13/15/12，均远超门 | ✔ |
| 段落 ≤400 字 | awk 预检全 0 超段 | ✔ |
| region 弹性 | Argentina/United States/Arctic/Amazon Basin/Central Asia/England 均自然成立 | ✔ 承 EVV6「region 可容非常规层级」 |
| real/fictional 双档 | 7 real + 1 fictional（healthful-house）四节均成立 | ✔ |
| quality 省略回填 | 8 页全省 quality，add_page 回填 featured | ✔ 承定策 |
| aliases | 8 页全 []（含 Long Island 释名亦不设 alias） | ⚠ 见下 |

## 本区间新增消歧维度（较 R204 EVV5）

1. **DUPLICATE 语义同指（R212 Celestial Empire）**：slug/label/alias 三查皆 NEW，但
   **Celestial Empire=China 别称**，既有 china〔ASC〕已覆盖同书同域 → 建之即重复。
   现有 dup-check（test -f + label/alias）**盲于语义同义词**。反思结论：建前除机械查重外，
   须对「候选是否为既有实体的别称/雅称」作语义判断（帝国雅号、古称、译名尤须警惕）。
   记 **HK-dupcheck-semantic-synonym-blindspot**（PARK，纳 RFC 批审）。
2. **父/子域异指（R211 upper-amazon vs amazon）**：既有 amazon 为大河全流父域，
   upper-amazon 为上游子域，二者非碰撞可各立。承 Rio Negro 双指纪律，扩展至父/子包含关系。
3. **跨作品单指 vs 异指**：arctic-ocean（FC/ACH 单指真实北冰洋，采全）对 rio-colorado
   （SC 阿根廷 vs AWED 美国 Colorado，剔 5 非 SC PN）。判据：**是否同一真实/虚构指称**。

## 待决张力（不改 schema，记 HK/DEFER）

- **⚠ aliases 一律 [] 的保守惯性**：为避 Robur alias 冲突（build_registry warn），
  近 8 页即便存在正当 in-text 别名（Uzun Ada=Long Island、Rio Colorado=Colorado）
  亦不设 alias，仅散文提及。**代价**：wikilink 以别名指向时不解析。**收益**：零新 alias 冲突。
  现阶段收益 > 代价（featured/alias 债务已 DEFER 至 RFC 批审），维持保守；记
  **HK-place-alias-suppression**（PARK），RFC 批审时统一评估正当 alias 回填。
- schema 本体 **converged 不动**：四节 + book/real_or_fictional/region 定稿，本轮无追加。

## 六步状态机（EVV5，grow_state 存 R216 起始计数）

| 字段 | R215 起始 | R216 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 215 | 216 |
| type_round | 186 | 187 |
| rounds_since_last_evv5 | 10 | 0（EVV5 RESET）|
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 151 | 152 |
| last_updated_round | 215 | 216 |

## 遗留问题

1. **place 页数 410**：本轮不建（EVV5 反思）。registry 全库 1478，unknown 0。
2. **下轮 R216 = NEW1**：since_evv5=0<10、since_discover=3<10、queue(place)=2>0 → §3(7)。
   建 **Villa Rica**（villa-rica，EHLA×8，巴西钻石区矿镇/监狱），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region Brazil，real。
3. **R216+ 建序**：Villa Rica → Coal Town（2 项），建毕队列罄 → SCN28。
4. **新增 HK**：HK-dupcheck-semantic-synonym-blindspot（语义同指盲区）、HK-place-alias-suppression（正当 alias 抑制）。
5. **HK-dupcheck-the-prefix-blindspot**：区间内持续应用，无复现。PARK。
6. **散文门债**：37 页 >400（既有 DEFERRED）；区间建页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=151→152（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
