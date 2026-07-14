---
round: 7
date: 2026-07-13
phase: 9
gene: EVV5
type: technology
pages: [giant-telescope, nitroglycerine, granite-house-lift, nemo-electricity, jangada]
result: converge
---

# R7 — EVV5 technology r3 质量评估（模板反思第三轮 · 收敛检查）

## 执行摘要

对 r3-SCN27 的 5 个**边缘/复杂案例**页做质量评估，重点：**检查模板是否趋于收敛**。结论：**模板结构确认收敛**——连续三轮（15 页）H2 节序、frontmatter、引文规范零偏差；r3 的四类边缘压力（近重复、多组件、强耦合、全新作品）schema 全部无摩擦吸收，无需新增结构或字段。本轮唯一新现象是 `add_page.py` 对 r3 批次自动回填 `quality=featured`，属工具行为，非模板缺陷，其档位口径统一问题移交 EVV6。

## r3 边缘案例适配复核

| 边缘类型 | 页面 | schema 承压点 | 结果 |
|----------|------|---------------|------|
| 近重复实体 | nitroglycerine（vs gun-cotton）| 两 concept 炸药是否塌缩为重复 | 无塌缩——Science & Speculation 显式对照 gun-cotton，四节承载两相邻实体 |
| 多组件机械 | granite-house-lift | 复合结构（水轮+缆+basket）是否需拆节 | 无需——Design & Operation 单节以「动力→传动→载体」层次容纳 |
| 强耦合概念 | nemo-electricity（→nautilus）| 与载具页职责是否重叠 | 不重叠——concept 页述电化学原理，载具页述航行；职责清晰 |
| 全新作品 | jangada（EHLA 首建）| 新作品是否暴露 schema 盲点 | 无盲点——「夸张而非虚构」型 technology 四节自然成立 |

## 逐页复核

| 页面 | H2 顺序 | 4 节 | frontmatter | 引注 | 判定 |
|------|---------|------|-------------|------|------|
| giant-telescope | ✓ | 4/4 | instrument, inventor='' | 9 | pass |
| nitroglycerine | ✓ | 4/4 | concept, inventor=Cyrus Harding | 11 | pass |
| granite-house-lift | ✓ | 4/4 | instrument, inventor=Cyrus Harding | 9 | pass |
| nemo-electricity | ✓ | 4/4 | concept, inventor=Captain Nemo | 8 | pass |
| jangada | ✓ | 4/4 | vehicle, inventor=Joam Garral | 6 | pass |

H2 节序 5 页严格遵循 Overview → Design & Operation → Role in the Story → Science & Speculation，脚本核验确认（`grep '^## '`）。

## 收敛判断（三轮汇总）

- **结构收敛确认**：r1（具象机器/仪器）、r2（航空航海载具 + concept 首现）、r3（边缘/复杂案例）三个差异化批次，H2 节序 / frontmatter 字段 / 引文规范三项 15 页零偏差。
- **模板迭代轨迹**：EVV5 r1 追加「写作指引」（Science & Speculation 常态化 + 段落≤400 + 引文核验）；EVV5 r2 追加「跨作品实体」指引（concept 适配 + 单值 book 处置）。两次追加均为**写作指引层面**，无一次触及结构性字段增删 → 模板骨架自 r1 起即稳定。
- **r3 无新增模板变更**：边缘案例未暴露任何需要模板改动的张力，仅记录 quality 自动回填现象。**这是收敛的直接证据**——最难的边缘批次也不再产生模板压力。

## 本轮新现象：quality 自动回填 featured

r3 批次 5 页 `add_page.py` 全部自动回填 `quality=featured`（前两批手记 standard）。根因：r3 页恰好全部满足 featured 三条件（全 4 节 + 引注≥8 + Science & Speculation 含现实对照）。这**验证了 EVV5 r2 遗留的「达标即提 featured」猜想**——工具已内建达标即提逻辑，无需人工干预。

处置建议（交 EVV6 定稿）：确立「**quality 以工具回填为准，日志不再手记档位**」策略，并回查 r1/r2 的 10 页是否亦达 featured 标准（若达标则一致化）。本轮不改模板质量阈值表（阈值定义本身正确，只是此前人工统一记 standard 与工具判档不一致）。

## EXIT-GATE 检查

评估轮，不新建页面；完整 E1–E5 在 EVV6 之后统一执行。

## 遗留问题（交 EVV6）

1. **档位口径统一**：确立工具回填为准策略，回查 r1/r2 10 页实际达标档位。
2. **跨作品 concept 的 book 字段**：EVV5 r2 记为框架层面小张力（gun-cotton），r3 未再现（nitroglycerine/nemo-electricity 均单作品）。是否向 memex 提 RFC 由 EVV6 判定——倾向暂不提（个案可正文补偿）。
3. **weapon category 样本偏少**（QUO23 观察项）：非模板问题，butler 循环补页。
