---
round: 15
date: 2026-07-13
phase: 9
gene: EVV5
type: place
pages: [the-moon, great-eyrie, stromboli, granite-house, hong-kong]
result: converge
---

# R15 — EVV5 place r3 质量评估（模板反思第三轮 · 收敛检查）

## 执行摘要

对 R13 r3-SCN27 的 5 个边缘/复杂地点页做质量评估，重点：**检查模板是否趋于收敛**。结论：**place 模板结构确认收敛**——连续三轮（15 页）H2 节序、frontmatter、引文规范零偏差；r3 的五类边缘压力（跨作品天体、神秘不可达、出口对称、人造居所近重复、短驻留航点）schema 全部无摩擦吸收，**零模板追加**。追加量轨迹 5→3→0，与 technology（3→2→0）同构。

## r3 边缘案例适配复核

| 边缘类型 | 页面 | schema 承压点 | 结果 |
|----------|------|---------------|------|
| 跨作品天体 | the-moon（FEM+RM）| 单值 book + 非地表天体 | 无摩擦——book=RM，FEM 正文引 PN；天体地理四节自然成立 |
| 神秘不可达 | great-eyrie | 「定义即未知」的 Geography 写什么 | 以「不可达性本身」为 Geography 核心，节不空 |
| 出口对称 | stromboli | 与 snaefells 入口职责重叠 | 不重叠——入口 vs 出口显式对称，Connections 串联 |
| 人造居所近重复 | granite-house | vs lincoln-island 塌缩 | 不塌缩——全域 vs 崖内居所，职责清晰 |
| 短驻留航点 | hong-kong | 情节驻留少能否四节成立 | 成立——In the Narrative 述 Fix 追捕转折 |

## 逐页复核

| 页面 | H2 顺序 | 4 节 | real_or_fictional | 引注 | 判定 |
|------|---------|------|-------------------|------|------|
| the-moon | ✓ | 4/4 | real | 7 | pass |
| great-eyrie | ✓ | 4/4 | fictional | 6 | pass |
| stromboli | ✓ | 4/4 | real | 8 | pass |
| granite-house | ✓ | 4/4 | fictional | 7 | pass |
| hong-kong | ✓ | 4/4 | real | 6 | pass |

H2 节序 5 页严格遵循 Overview → In the Narrative → Geography & Features → Connections（`grep '^## '` 核验）。

## 收敛判断（三轮汇总）

- **结构收敛确认**：r1（最强实体：岛/火山/城镇/俱乐部/地底海）、r2（新子领域：都市/海域/极地/真实国家）、r3（边缘案例）三个差异化批次，H2 节序 / frontmatter 字段 / 引文规范三项 15 页零偏差。
- **模板迭代轨迹**：EVV5 r1 追加 5 条写作指引（real/fictional 双档、region 非常规层级、段落≤400、引文核验+sentence_index 兜底、quality 省略）；EVV5 r2 追加 3 条（无地形 Geography 替代维度、抽象点作 place、meta 表述避 warn）；**r3 追加 0 条**。均为写作指引层面，无一次触及结构性字段增删。
- **r3 无新增模板变更**：最难的边缘批次也不再产生模板压力，**收敛的直接证据**。

## 本轮工具经验（交 EVV6）

- **edit_page 后需补跑 compute_quality**：mount-franklin 用 edit_page 修引文后 quality 变 None（edit_page 不回填 quality，仅 add_page 回填）。QUO23 已运行 compute_quality + build_registry 修正。建议固化为「edit_page 修改内容后补跑 compute_quality」流程提示，交 EVV6 定稿。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 EVV6 之后统一执行。

## 遗留问题（交 EVV6）

1. **收敛定稿**：place 模板追加量 5→3→0，与 technology 同构，EVV6 判 converged 并在 place-schema.md 追加定稿节。
2. **edit_page/compute_quality 流程提示**：是否固化为模板级操作提示。
3. **跨作品实体累计**：technology gun-cotton + place the-moon = 2 例，仍 <5 阈值，暂不提多值 book RFC。
