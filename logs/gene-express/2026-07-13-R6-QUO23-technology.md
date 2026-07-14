---
round: 6
date: 2026-07-13
phase: 9
gene: QUO23
type: technology
pages: [columbiad, lunar-projectile, the-terror, ruhmkorff-apparatus, diving-apparatus, albatross, victoria-balloon, the-forward, gun-cotton, ships-compass, giant-telescope, nitroglycerine, granite-house-lift, nemo-electricity, jangada]
result: pass
---

# R6 — QUO23 technology 配额核查（三轮累计覆盖）

## 执行摘要

对 technology 类型三轮（r1/r2/r3）累计建成的 15 个 pilot 页面（+ 9-A 试建 nautilus，共 16 页）做配额覆盖核查。核查维度：**建页数量达标**、**category 枚举全覆盖**、**作品分布无过度集中**、**quality 达标**。结论：**全部达标，PASS**。技术类型 pilot 页面在四个 category、十部作品间分布均衡，无单一子领域垄断，无 basic 欠档页。

## 数量配额

| 项 | 目标 | 实际 | 判定 |
|----|------|------|------|
| pilot 页面数 | ≥15（3 轮 × 5） | 15 | ✓ |
| 含 9-A 试建 | — | 16（+nautilus） | ✓ |
| quality ≥ standard | 100% | 16/16（11 standard + 5 featured） | ✓ |
| 无 basic 欠档 | 0 | 0 | ✓ |

registry 核查（`pages.json`）：`type=technology` 计 16 页，`quality` 分布 = 11 standard / 5 featured（5 featured 为 r3 批次工具自动回填），无 basic。

## Category 枚举覆盖

schema 定义 category 枚举 = {vehicle, weapon, instrument, concept}，四类全部覆盖：

| category | 页数 | 页面 |
|----------|------|------|
| vehicle | 7 | nautilus, lunar-projectile, the-terror, albatross, victoria-balloon, the-forward, jangada |
| weapon | 1 | columbiad |
| instrument | 5 | ruhmkorff-apparatus, diving-apparatus, ships-compass, giant-telescope, granite-house-lift |
| concept | 3 | gun-cotton, nitroglycerine, nemo-electricity |

- **无空枚举**：四类均有实例，schema 各分支均经建页验证。
- **weapon 仅 1 例**：凡尔纳语料中纯武器类实体本就稀少（Columbiad 为标志性个案），非选页偏差；后续 butler 循环若发现更多（如 the-terror 的舰载武器）可补。记为观察项，非配额缺口。

## 作品分布

15 pilot 页覆盖 10 部作品，无单部垄断：

| 作品(VVV) | 页数 |
|-----------|------|
| FEM | 3（columbiad, lunar-projectile, giant-telescope）|
| MI | 3（gun-cotton*, nitroglycerine, granite-house-lift）|
| TTLU | 2（diving-apparatus, nemo-electricity；+9-A nautilus）|
| MW | 1（the-terror）|
| JCE | 1（ruhmkorff-apparatus）|
| RC | 1（albatross）|
| FWB | 1（victoria-balloon）|
| ACH | 1（the-forward）|
| DSCF | 1（ships-compass）|
| EHLA | 1（jangada）|

*gun-cotton 跨 FEM+MI，主作品计 FEM，此处按内容主体归 MI 侧统计。

- **最大集中度**：FEM/MI 各 3 页（20%），未超 1/3 阈值 → 无过度集中。
- 36 部作品中 pilot 触及 10 部；其余作品的 technology 实体留 butler 后续循环覆盖（符合 pilot「验证 schema」而非「穷尽建页」的定位）。

## 每句有据 / 引注配额

15 页引注数区间 6–13，全部 ≥ standard 门槛（≥5）。三轮引注方法一致（corpus_search 定位 → 章节页 grep 逐字核验）。无凑数引注。

## 判定

**PASS**。数量、category 枚举、作品分布、quality、引注五项配额全部达标。technology pilot 覆盖充分，可进入 EVV5 r3 收敛反思与 EVV6 元反思。

## 遗留问题

- weapon category 样本偏少（仅 columbiad），非缺陷，记为 butler 循环补页观察项。
- quality 档位 standard/featured 混杂（r1/r2 手记 standard，r3 工具回填 featured），配额上均 ≥ standard 达标，但档位口径不一致问题移交 EVV6 裁决（见 R5 日志遗留问题）。
