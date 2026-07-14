---
round: 22
date: 2026-07-14
phase: 9
gene: QUO23
type: character
pages: [captain-nemo, phileas-fogg, professor-lidenbrock, cyrus-harding, captain-hatteras, axel, passepartout, fix, ned-land, michel-ardan, top, robur, aouda, conseil, barbicane]
result: pass
---

# R22 — QUO23 character 配额核查（三轮累计覆盖）

## 执行摘要

对 character 类型三轮（r1/r2/r3）累计建成的 15 个 pilot 页面做配额覆盖核查。核查维度：**建页数量达标**、**role 四档全覆盖**、**作品分布无过度集中**、**五节结构完整**、**quality 达标**、**引注配额**。结论：**全部达标，PASS**。15 页覆盖 role 四档、7 部作品，无单一作品垄断，五节结构 15/15 齐全，quality 15/15 featured。

## 数量配额

| 项 | 目标 | 实际 | 判定 |
|----|------|------|------|
| pilot 页面数 | ≥15（3 轮 × 5） | 15 | ✓ |
| quality ≥ standard | 100% | 15/15 featured | ✓ |
| 无 basic 欠档 | 0 | 0 | ✓ |

registry 核查（`pages.json`）：`type=character` 计 15 页，`quality` 分布 = `{'featured': 15}`，无 standard/basic。

## role 枚举四档覆盖

schema 定义 `role` 枚举 = {protagonist, antagonist, supporting, narrator}，四档均覆盖：

| role | 页数 | 页面 |
|------|------|------|
| protagonist | 6 | captain-nemo, phileas-fogg, professor-lidenbrock, cyrus-harding, captain-hatteras, barbicane |
| supporting | 6 | passepartout, ned-land, michel-ardan, top, aouda, conseil |
| antagonist | 2 | fix, robur |
| narrator | 1 | axel |

- **无空枚举**：四档均有实例，schema 各分支经建页验证。
- protagonist/supporting 各 6 均衡，antagonist（误判型 fix + 傲慢发明家 robur）、narrator（axel）覆盖较少但足证枚举可用。

## 作品分布

15 pilot 页覆盖 7 部作品，无单部垄断：

| 作品(VVV) | 页数 |
|-----------|------|
| AWED | 4（phileas-fogg, passepartout, fix, aouda）|
| TTLU | 3（captain-nemo, ned-land, conseil）|
| JCE | 2（professor-lidenbrock, axel）|
| FEM | 2（michel-ardan*, barbicane*）|
| MI | 2（cyrus-harding, top）|
| ACH | 1（captain-hatteras）|
| RC | 1（robur*）|

\* michel-ardan/barbicane 出场跨 FEM+RM，主作品计 FEM；robur 跨 RC+MW，主作品计 RC。

- **最大集中度**：AWED 4 页（27%），未超 1/3 阈值 → 无过度集中。AWED 集中因该书角色群完整（Fogg + 仆从 Passepartout + 反派 Fix + 女主 Aouda 构成完整人物网），属叙事结构而非选页偏差。
- 35 部作品中 pilot 触及 7 部；其余作品 character 实体留 butler 后续循环覆盖。

## 五节结构 / 引注配额

| 项 | 区间 | 判定 |
|----|------|------|
| H2 节数 | 15 页均 = 5 | ✓ 全五节 |
| PN 引注（pn_count）| 4–9 | ✓ 全 ≥ standard 门槛（≥4 distinct，密度达标）|
| wikilink 数 | 3–7 | ✓ 全 ≥ 2（standard 门槛）|

三轮引注方法一致（corpus_search / sentence_index 定位 → 逐字核验 → 回定 PN）。r1 一处 overlap warn（professor-lidenbrock）已 edit_page 修正，r2/r3 全程零 warn。无凑数引注。

## 跨作品实体累计

| 实体 | 类型 | 作品 |
|------|------|------|
| gun-cotton | technology | FEM + MI |
| the-moon | place | FEM + RM |
| captain-nemo | character | TTLU + MI |
| robur | character | RC + MW |

累计 **4 例**（<5 经验阈值）。维持单值 `book`（主作品）+ 正文点名其余作品并引 PN。**逼近阈值，EVV6 评估 butler 观察计数机制**。

## 判定

**PASS**。数量、role 四档、作品分布、五节结构、quality、引注六项配额全部达标。character pilot 覆盖充分，可进入 EVV5 r3 收敛反思与 EVV6 元反思。

## 遗留问题

- 跨作品实体累计 4 例（robur 新增），逼近 5 阈值，EVV6 评估是否启动 butler 观察计数。
- 4-char VVV（TTLU/AWED）引注渲染问题仍待 RFC-0003 建站后统一处理，配额上不受影响。
