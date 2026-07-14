# Vernean Voyages Wiki — 增长流程 (GROW)

> 前置：`BIRTH.md` Phase 0–10 全部完成，butler 日常循环已启动。
> BIRTH Phase 9（类型 Pilot）等同于 GROW Phase 1（种子层），无需重复执行。
>
> **参考文献**：`$MEMEX_ROOT/ref/spec/butler-phased-strategy-seed.md`
>
> 本文档按 `$MEMEX_ROOT/GROW.spec.md` 实例化。写作原则：做一步写一步——未执行的 Phase 待真正启动时才从模板复制。

---

## grow_state.json — Phase 2 显式状态机

Phase 2 控制状态存于 `local/state/grow_state.json`（Phase 2.1-A 末尾初始化）。
权威设计：`$MEMEX_ROOT/ref/spec/grow-state-machine.md`。当前尚未进入 Phase 2，文件待建。

---

## Phase 0：基线摸底

> **comply**: pass（Phase 0 自 spec 实例化并即时执行，本文件记录实际扫描结果）
>
> **目标**：进入建设阶段前，掌握页面库现状、候选池深度、质量分布，确定 GROW 起始 Phase。
> **执行时间**：2026-07-14（BIRTH Phase 10 完成后）
> **产出**：`local/memory/grow_baseline.md`

---

### 0-A 前置验证

- [x] `local/memory/boot_summary.md` 存在（boot_completed: 2026-07-14，phases 0–9，Pilot 4 类型）
- [x] butler 轮次计数文件存在：R_current = **1**（`logs/butler/round_counter.txt`）
- [x] 基础数据文件完整：`docs/wiki/pages.json`、`data/sentence_index/`、`logs/butler/queue.md`、`local/template/` 均存在
- [x] state 文件（Phase 2 及以后）：`local/state/grow_state.json` 尚不存在——Phase 2.1-A 时初始化

---

### 0-B 页面库现状扫描

- [x] **页面总数与类型分布**（`docs/wiki/pages.json`）：
  - 总页数 = **1031**
  - 章节类页面（type=chapter）= **968**（不参与 GROW 质量统计）
  - overview = 2
  - 词条类页面（非 chapter/overview/list）= **61**
  - 词条质量分布 = **featured 61**（stub 0 / basic 0 / standard 0 / premium 0）

- [x] **关键比率**：
  - stub 比率 = **0.0%**（目标 < 20%）
  - featured+ 比率 = **100.0%**

- [x] **质量分布上限检查（硬性约束）**：⚠️ **当前严重违反** —— featured+premium 上限为 10%，实测 100%。
  根因为 `add_page.py`/`compute_quality.py` 的 featured 结构性虚高（见 2026-07-14 自检，housekeeping P1 `HK-featured-inflation`）。**featured% 信号不可信**，不得据此判为"已高质量"。

  | 质量档 | 上限 | 实测 | 状态 |
  |--------|------|------|------|
  | premium | 5% | 0% | ✓ |
  | featured | 5% | 100% | ✗ 违反 |
  | featured+premium | 10% | 100% | ✗ 违反 |
  | standard | 30–60% | 0% | ✗ |
  | basic | < 30% | 0% | ✓ |
  | stub | < 20% | 0% | ✓ |

- [x] **类型覆盖完整性**（对照 `local/template/`，估算量来自 `logs/butler/type-survey.md`）：

  | type | 模板 | 当前词条 | 预估总量 | 覆盖率 |
  |------|------|---------|---------|--------|
  | character | ✓ | 15 | 180–240 | ~7% |
  | place | ✓ | 15 | 100–140 | ~12% |
  | technology | ✓ | 16 | 70–100 | ~19% |
  | event | ✓ | 15 | 45–70 | ~26% |
  | work | ✓ | **0** | 35 | **0%** |
  | organization | ✓ | **0** | 10–18 | **0%** |

- [x] **type 标签映射完整**：`docs/wiki/local/config/types.js` 的 9 键覆盖 pages.json 出现的全部 type（character/place/technology/event/chapter/overview），无缺失标签。

---

### 0-C Pilot 信息读取

- [x] 读取 `local/memory/boot_summary.md` Pilot EVV 汇总：四型（technology/place/character/event）均 EVV6 判 converged，模板追加量单调降至 0（3→2→0 / 5→3→0 / 8→5→0 / 7→0→0），骨架冻结。
- [x] Pilot 遗留问题处理状态：
  - 跨作品实体累计 4 例（gun-cotton/the-moon/captain-nemo/robur），逼近多值 `book` 字段 RFC 阈值(5) → **非阻塞债务**，Phase 2 扩张时持续观察，达 5 提 RFC（PARKED）。
  - 变长 VVV 三 RFC（0001/0002/0003）→ **非阻塞债务**，PARKED，渲染/校验侧问题，数据正确。
  - featured 结构性虚高（本次自检）→ **非阻塞但重要债务**，见 0-B，已记 housekeeping P1。

---

### 0-D 候选池评估

- [x] **当前队列**：`logs/butler/queue.md` 候选条目数 = **0**（空队列——discover 基因尚未运行，非枯竭）
- [x] **各类型估算剩余候选量**（type-survey 估算 − 已建）：
  - character: 180–240 − 15 = 剩余 **~165–225**
  - place: 100–140 − 15 = 剩余 **~85–125**
  - technology: 70–100 − 16 = 剩余 **~54–84**
  - event: 45–70 − 15 = 剩余 **~30–55**
  - work: 35 − 0 = 剩余 **35**
  - organization: 10–18 − 0 = 剩余 **~10–18**
  - 合计剩余 **~380–560**
- [x] **候选充足性判断**：语料候选**极充足**（已建 61 / 估算 440–620，仅约 11%）。队列本身为空是因 discover 未运行 → Phase 2 首步须跑 discover（SCN 基因）填充队列。

---

### 0-E 链接网络密度评估

- [x] **wikilink 数量**：**2239** 条（含章节页 wikify 1079 + 词条间链接）
- [x] **backlinks 索引**：**1009/1009** 页被引用，**2153** 条反链
- [x] **wikify 优先级判断**：wikilink/N_entries = 2239/61 ≈ 37，密度高（章节 wikify 已完成）。Phase 2 新建词条后按批次补 wikify 即可。

---

### 0-F GROW 阶段定位

- [x] 根据规则确认阶段：**GROW Phase 2（广度扩张）**
  - 命中规则："Pilot 已完成，stub% = 0，N_entries < 80"（61 < 80）。
  - **不**命中 Phase 3/4（要求词条数 >300；当前仅 61）。
  - featured%=100% **不**触发 Phase 4——spec 路由基于 stub% 与词条数，且该信号已知虚高。
- [x] 定位理由：种子层 61 词条 vs 语料估算 440–620，覆盖仅 ~11%，两类型（work/organization）零词条，候选极充足 → 明确处于广度扩张阶段。

---

### 0-G 基线快照写入

- [x] 写入 `local/memory/grow_baseline.md`（见该文件）
- [x] 提交基线文档

---

### 0-X 验收标准

- [x] `local/memory/grow_baseline.md` 存在且填写完整（无占位符）
- [x] 阶段定位明确：Phase 2（广度扩张）
- [x] 遗留债务已分类：均为非阻塞（跨作品 book 阈值、VVV 三 RFC、featured 虚高）
- [x] 非阻塞债务已记录：housekeeping P1（featured 虚高）、boot_summary（其余）
- [x] 阻塞债务：无

---

> **Phase 0 完成**。阶段定位 Phase 2（广度扩张）。进入 Phase 2 前需：`/grow init phase2`（初始化 grow_state.json）→ `/comply grow 2` → `/grow phase2`。

---

## Phase 1：种子层（Seed）

> 状态：已完成（等同 BIRTH Phase 9 类型 Pilot，60+1 页，四型 EVV6 converged）。详见 `local/memory/boot_summary.md`。

## Phase 2：广度扩张（Expansion）

> 状态：未开始

## Phase 3：深度扩张（Deep Expansion）

> 状态：未开始

## Phase 4：全库体检与体系固化

> 状态：未开始

## Phase 5：深化与洞察层

> 状态：未开始

## Phase 6：洞察落地与成熟期过渡

> 状态：未开始

## Phase 7：残差发现与终局收尾

> 状态：未开始

## Phase 8：残余质量重组与终局核验

> 状态：未开始

## Phase 9：语义聚合与洞察终章

> 状态：未开始

## Phase 10：GROW 终局质检与总结

> 状态：未开始
