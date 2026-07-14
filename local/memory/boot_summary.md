---
wiki: Vernean Voyages Wiki
boot_completed: 2026-07-14
phases: 0–9
---

# Boot 复盘总结

## 基本统计

| 指标 | 数量 |
|------|------|
| 导入章节 | 968 个 |
| PN 赋号段落 | 57,734 段 |
| Pilot 页面 | 60 个（4 种类型 × 15）+ 1 个 9-A 试建页（nautilus）|
| Wikify 链接 | 1,079 条（377/968 章）|
| Backlinks | 2,153 条（覆盖 1,009 页）|
| 提交 RFC（boot 期间）| 0 个已提交（3 个 proposed 草稿，全部 PARKED）|

## RFC 清单

> 所有在 boot 期间产出的 RFC 均逐条列入。本 wiki 的 3 个 RFC 均为**同一根因**（变长 VVV / volume 方案对 memex 共享组件的 3 字符硬编码假设），按项目决策 **PARKED**：草稿已写，暂不提交 memex，待全站建成 + 用户签署后再批量提交。

| 编号 | slug | status | 目标文件 | 一句话描述 |
|------|------|--------|---------|-----------|
| 0001 | pn-structure-verify-vol-width | proposed (parked) | `wiki/scripts/butler/pn_structure_verify.py` | A5 检查对变长 VVV 误报 |
| 0002 | sentence-index-vol-width | proposed (parked) | `wiki/scripts/build_sentence_index.py` | PN 正则对变长 VVV 静默丢句 |
| 0003 | pn-citation-vol-width | proposed (parked) | `pn-citation` 插件及同族组件 | VVV 段正则硬编码 3 字符，4 字符码渲染为纯文本 |

## Pilot 流程发现

### 基因层问题

| 基因 | 问题描述 | 处置 |
|------|---------|------|
| SCN27 | 无结构性问题；`corpus_search` 多关键词对冷门作品易零命中/淹没 | housekeeping（已沉淀"直读 sentence_index 兜底"方法）|
| EVV5 | 无——四型评估逻辑稳定，追加量单调收敛 | 无需处理 |
| EVV6 | 无——四型均干净判 converged | 无需处理 |
| CHK7 | 9-A 时 Recent 收录检查 1500ms 等待对 900+ 条 feed 过短，误报 false-negative | housekeeping（观察项）|

### Boot 流程层问题

| Phase | 问题描述 | 处置 |
|-------|---------|------|
| Phase 9 | 变长 VVV（TTLU/AWED/ACH 4 字符码）触发 3 处共享组件 3 字符假设 | RFC 0001/0002/0003（parked）|
| 其余 Phase | 未发现需要修改的规范 | 无需处理 |

### 脚本/规范层问题

| 文件 | 问题描述 | 处置 |
|------|---------|------|
| `pn_structure_verify.py` / `build_sentence_index.py` / `pn-citation` | 变长 VVV 硬编码 3 字符 | RFC 0001/0002/0003（parked）|
| `compute_quality.py` | `edit_page.py` 修改后不回填 quality，须手动补跑 | housekeeping（已固化为 schema 写作指引）|

## EVV Pilot 类型汇总

按 Phase 9 执行顺序，每种类型一行：

| 类型 | 质量（featured/总）| 模板主要改动（结构性）| 模板追加量 | 遗留问题 |
|------|---------|-------------------------------|-----------|---------|
| technology | 16/16 featured | 四节 Overview/Design & Operation/Role in the Story/Science & Speculation + book/inventor/category 定稿 | 3→2→0 | 无（weapon 样本偏少列 butler 观察）|
| place | 15/15 featured | 四节 Overview/In the Narrative/Geography & Features/Connections + book/real_or_fictional/region 定稿 | 5→3→0 | 无 |
| character | 15/15 featured | 五节 Overview/Role in the Story/Character & Traits/Relationships/Appearances + book/affiliation/first_appearance/role 定稿 | 8→5→0 | 无 |
| event | 15/15 featured | 四节 Overview/What Happens/Significance/Participants & Setting + book/location/pn_anchor 定稿 | 7→0→0 | 无 |

> 数据来源：各类型 EVV6 日志（`logs/gene-express/2026-07-14-R{8,16,24,32}-EVV6-{type}-*.md`）。四型均判 **converged**。

## Pilot 信息组织核心洞察

经过 4 种类型、每型 3 轮共 12 轮 Pilot（60 页），本次 boot 在信息组织层面形成以下核心认知：

**结构稳定性**
- 四型模板追加量全部单调收敛至 0（3→2→0 / 5→3→0 / 8→5→0 / 7→0→0），且**每型 r3（边缘/复杂案例批次）零结构追加**——最能暴露 schema 盲点的批次也不再产生新需求，是收敛的决定性共同证据。
- 骨架自 r1 即稳定：四型的 H2 节结构与专属 frontmatter 字段从第一轮定型后再未增删，后续追加全部落在**写作指引层面**（如何引用、如何取值），非结构层面。

**类型间共性与差异**
- 共性：所有实体类型都收敛到「Overview 起手 + 中段叙事/机制展开 + 末段交叉引用（wikilink 节）」的三段式骨架；wikilink 交叉引用节（character 的 Relationships/Appearances、place 的 Connections、event 的 Participants & Setting）一律为 **PN 豁免节**，质量准则是链接完整性而非引注密度。
- 差异：character 需 5 节（角色维度最多：性格/关系/登场分列），其余三型 4 节即足；character 追加量最高（8），因人物的关系网与性格描写维度最丰富、最需写作指引约束。

**最易忽略的内容维度**
- 跨类型最高发的扣分点是 **Significance/解释性节的 overlap warn**：解释句易把 PN 挂在元叙述上。统一修法——PN 必挂 verbatim 原文子句；event 尤甚（Significance 抽象性最高）。
- 单字/专名引文（如 "STROMBOLI"）overlap 天然偏低，需嵌入更长 verbatim 上下文。

**对 butler 使用 NEW1 建页的启示**
1. 引文一律先直读 `data/sentence_index/{VVV}-*.jsonl` 逐字核验再引 PN；`corpus_search` 仅作粗筛，冷门作品用 grep 定位。
2. 省略 frontmatter `quality`，交 `add_page.py` 自动回填；用 `edit_page.py` 改后必须补跑 `compute_quality.py` + `build_registry.py`。
3. 解释性节的每条 PN 都挂到 verbatim 子句上，杜绝 overlap warn；段落 ≤400 字符。

## EVV5/EVV6 遗留问题

- 跨作品**实体**累计 4 例（gun-cotton / the-moon / captain-nemo / robur），逼近多值 `book` 字段的 RFC 触发阈值（5）——交 butler 后续循环持续观察，达 5 时提 RFC（当前 PARK）。
- 跨作品**事件** 2 例（nemo-death / lunar-orbit-miss）不计入上述实体阈值。
- 变长 VVV 三 RFC（0001/0002/0003）PARKED，待全站建成 + 用户签署后批量提交。

## Butler 实例命名

> 主题取自 Verne 作品人物，体现各角色职能特质。--auto 模式下已写入 `local/config.md`，用户可随时改名。

| 角色 | focus | 实例名 | 由来 |
|------|-------|-------|------|
| 探索者 | discover | Nemo | 尼摩船长，深海未知的探索者 |
| 创建者 | create | Harding | Cyrus Harding，无中生有的工程师-建造者 |
| 丰富者 | enrich | Aronnax | Aronnax 教授，博物学家，细节的丰富者 |
| 发布者 | publish | Ardan | Michel Ardan，面向公众的传播者 |
| 管理者 | housekeeping | Fogg | Phileas Fogg，精确守序的秩序维护者 |

## 经验总结

四型 pilot 收敛轨迹完全同构（追加量单调降至 0、r3 边缘批次零追加），证明 memex 的「r1 定骨架 → r2/r3 只补写作指引 → EVV6 定稿冻结」模板演进模型对不同实体类型稳健有效。本次 boot 唯一系统性摩擦是变长 VVV（volume 多作品方案）与共享组件 3 字符假设的冲突——数据侧全部正确，仅渲染/校验侧需上游放宽正则，已成 3 个 parked RFC。下一个多作品合集 wiki 启动前，建议先合并这批 VVV 宽度 RFC。
