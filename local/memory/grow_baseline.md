# GROW 基线摸底 — Vernean Voyages Wiki

date: 2026-07-14
butler_round: R1
grow_phase: Phase 2（广度扩张）

## 页面库现状

总页数: 1031（含章节 968 个、overview 2 个）
词条类页面: 61（character 15 / place 15 / technology 16 / event 15 / work 0 / organization 0）
质量分布: featured 61（standard 0 / basic 0 / stub 0 / premium 0）
stub 比率: 0.0%
featured+ 比率: 100.0%（⚠️ 信号虚高，见下）

> **质量分布上限严重违反**：featured+premium 硬上限 10%，实测 100%。根因是 `add_page.py`/
> `compute_quality.py` 的 featured 判据纯结构性（h2≥3 且 PN≥3 且散文≥200 字符），add_page.py
> 建页即自动回填、无 notability 门、只升不降。故 featured% **不能**作为"质量已高"的证据。
> 已记 housekeeping P1 `HK-featured-inflation`（PARKED RFC 种子）。

## 候选池评估

当前队列条目数: 0（空队列——discover 基因尚未运行，非候选枯竭）
各类型估算剩余候选量（type-survey 估算 − 已建）:
- character: ~165–225
- place: ~85–125
- technology: ~54–84
- event: ~30–55
- work: 35（零词条）
- organization: ~10–18（零词条）
- 合计剩余: ~380–560
总体判断: 候选极充足（已建 61 / 估算 440–620，覆盖约 11%）

## Pilot 遗留债务

1. 跨作品实体累计 4 例（gun-cotton/the-moon/captain-nemo/robur），逼近多值 `book` 字段 RFC 阈值(5)。**非阻塞**——Phase 2 持续观察，达 5 提 RFC（PARKED）。
2. 变长 VVV 三 RFC（0001 pn-structure-verify / 0002 sentence-index / 0003 pn-citation）。**非阻塞**——渲染/校验侧问题，PN 数据正确，PARKED。
3. featured 结构性虚高（2026-07-14 自检）。**非阻塞但重要**——影响 Phase 2/3 质量分级与升档 pre-flight；每个新建页会被自动标 featured，加剧上限违反。已记 housekeeping P1。

## 链接网络

wikilink 总数: 2239
平均每词条: ~37 条（含 968 章 wikify 后的 1079 条）
backlinks 覆盖: 1009/1009 页，2153 条反链

## 阶段定位

定位结论: Phase 2 — 广度扩张
理由: 种子层仅 61 词条，语料估算 440–620，覆盖约 11%，work/organization 两类型零词条，候选极充足；命中 spec 路由 "stub%=0 且 N_entries<80 → Phase 2"。featured%=100% 不触发 Phase 4（该信号虚高且路由以词条数>300 为门）。

## 下一步优先动作（Top 3）

1. **决策 featured 分级策略**：Phase 2 会用 add_page.py 批量建页，每页被自动标 featured，进一步违反 10% 上限。进入 Phase 2 前需与用户对齐：是接受"featured 暂无意义、后续批量重评"，还是先本地约束分级（不改 memex，PARKED）。
2. **补齐零词条类型**：work（35 部作品，1:1 建 work 词条，是跨作品导航枢纽）与 organization（Gun Club/Reform Club 等）优先启动，收益高且候选明确。
3. **discover 填充候选队列**：队列为空，Phase 2 首步跑 discover（SCN 基因）从语料surface候选，再按类型轮次扩张。
