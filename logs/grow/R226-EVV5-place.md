---
round: 226
date: 2026-07-18
type_round: 197
phase: "2.1"
current_type: place
gene: EVV5
pages: []
result: reflect
---

# GROW 2.1-B · R226 · EVV5 · place — schema 反思（自 R215 EVV5 以来 10 轮，R216–R225 建 8 页 + 2 SCN28 单词地名扫）

## 执行摘要

Phase 2.1-B place 第 197 轮（type_round 197）。决策机 §3 首匹配 **§3(1b) EVV5**
（since_evv5=10≥10、since_discover=2<10 → 单 EVV5，非 EVV5+SCN28）。本轮**不建页**，
对 R216–R225 期间 place schema 实践作反思，执行后 reset since_evv5=0。

**区间产出**：R216 villa-rica、R217 coal-town、R219 montgomery-street、R220 north-carolina、
R221 pleasant-garden、R222 kamtchatka-current、R224 new-berne、R225 raleigh（8 建页）；
R218 SCN28（+4 候选，多词 discover3）、R223 SCN28（**首度单词地名扫** single_toponym_scan.py，+2 净新）。
place 计数 410→418（净 +8），registry 1478→1486，unknown 恒 0。

## schema 符合度评估

| 维度 | 观察 | 判定 |
|------|------|------|
| 四 H2 结构 | 8 页全四节（Overview / In the Narrative / Geography & Features / Connections），无空节、无 H1 | ✔ converged 保持 |
| ≥5 distinct solid PN | 8 页分别 10/13/15/14/14/14/10/5，均达门（raleigh 恰 5，逐句确凿）| ✔ |
| 段落 ≤400 字 | awk 预检全 0 超段（含 raleigh 初稿即达标）| ✔ |
| region 弹性 | Brazil/United States/North Pacific 均自然成立 | ✔ 承「region 可容非常规层级」（North Pacific 洋流域）|
| real/fictional | 8 页全 real（本区间无 fictional）| ✔ |
| quality 省略回填 | 8 页全省 quality，add_page 回填 featured | ✔ 承定策 |
| aliases | 8 页全 []（承 HK-place-alias-suppression 保守惯性）| ⚠ 见下 |

## 本区间新增消歧维度（较 R215 EVV5）

1. **单词地名 discover 盲区补救（R223）**：多词 discover3 对单词 toponym 盲（HK-discover-existing-type-blindspot）。
   新建 `single_toponym_scan.py`（地理上下文正则捕单词 Capitalized toponym）。首扫低产（净 2），
   证 place 库已高度成熟——高频单词 40+ 逐一 exact-slug 复核后绝大多数已建。
2. **HK-dupcheck-bareterm-vs-slug（R223 新，最要紧）**：bare-term gather ≥5 **≠ 可建**。
   Tsalal（AM×90）/Serpentine（MI×17）/Beechey（ACH×23）/Lancaster（ACH×14）皆 bare-term 净新，
   但 exact-slug 核（含 `the-` 前缀 + test -f）揭示 tsalal-island/serpentine-peninsula/beechey-island/
   lancaster-strait **均已建**。反思结论：dup-check **必以 exact-slug 实际页形态为准**，bare-term 命中数仅作候选信号。
   直接强化既有「dup-check via filesystem not queue lines」纪律。记 HK-dupcheck-bareterm-vs-slug（PARK，纳 RFC 批审）。
3. **句级 referent 甄别（R224 new-berne）**：同段内 FF-001-006-s2「州议会所在」实指首府 Raleigh（其 s1 在前），
   非 New-Berne。**剔除该 PN**，得 10 clean solid。承 rio-colorado「同书异指剔除」纪律，
   下沉至**同段跨句 referent 甄别**——gather 命中段须逐句核指称主体，勿因段内含目标词即全采。
4. **恰门跨作品单指（R225 raleigh）**：FF×2+MW×3=5 **恰达 ≥5 门**，无冗余余量。
   处理：逐句确认 5 PN 全 solid（首府定义/电讯节点/降落邻邑/Strock 抵离），四节分配无空节。
   判据延续 arctic-ocean「同一真实指称跨作品可全采」。

## 待决张力（不改 schema，记 HK/DEFER）

- **⚠ aliases 一律 [] 的保守惯性延续**：new-berne/raleigh 即便存正当 in-text 关系（New Berne 无连字符异写）
  亦不设 alias，仅散文提及。收益（零新 alias 冲突）现仍 > 代价（别名 wikilink 不解析）。
  维持保守，承 HK-place-alias-suppression（PARK），RFC 批审统一评估正当 alias 回填。
- schema 本体 **converged 不动**：四节 + book/real_or_fictional/region 定稿，本轮无追加。

## 六步状态机（EVV5，grow_state 存 R227 起始计数）

| 字段 | R226 起始 | R227 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 226 | 227 |
| type_round | 197 | 198 |
| rounds_since_last_evv5 | 10 | 0（EVV5 RESET）|
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 1 | 1 |
| rounds_since_last_corpus_discover | 162 | 163 |
| last_updated_round | 226 | 227 |

## 遗留问题

1. **place 页数 418**：本轮不建（EVV5 反思）。registry 全库 1486，unknown 0。
2. **下轮 R227 = SCN28-zombie**：since_evv5=0<10、streak=1<3、since_discover=3<10、queue(place)==0 → §3(4)。
   第三次 place discover。试二/三字混合 toponym 正则或未建河流/海角/湖泊等小特征细扫。
3. **discover_streak_low=1**：R227 SCN28 若 new_candidates<3 → streak=2；再一轮 <3 → streak=3 触 §3(2) CLOSE place → event。
   若确认饱和（连续低产）则 CLOSE place，切换 event。
4. **HK-dupcheck-bareterm-vs-slug**〔R223 记〕：本区间核心教训，已并入 dup-check 纪律。区间后续无复现。
5. **HK-discover-existing-type-blindspot**：R223 单词地名扫已部分补救；仍余语义同义/雅称盲区（HK-dupcheck-semantic-synonym-blindspot）。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本区间建页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=162→163（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；tsalal-island/serpentine-peninsula/
    beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建）；Wilmington/Catawba/Cape Hatteras/Mackenzie〔river〕/Fort Good Hope/
    Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、
    HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
