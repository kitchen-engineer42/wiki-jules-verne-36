# 内务任务队列（Housekeeping）

> butler housekeeping 轮次消费此队列。空队列时 butler 自行发现内务任务。

## P1 — 高优先级

### HK-featured-inflation — `featured` 等级虚高（结构填充 ≠ 质量/notability）

**现象**：`add_page.py` 新建页面即被自动标 `featured`，即便实体在语料中极少出现、内容单薄。boot 期间 61/61 pilot 页全部 featured，被我误当作"收敛=高质量"信号。

**根因（自检 2026-07-14 确认）**：
1. `compute_quality.py:84-87` 的 featured 判据是纯**结构性**：`h2≥3 AND (PN≥3 OR 引文≥5) AND 散文≥200 字符`。200 字符 ≈ 2–3 句，门槛极低；只测"模板是否填满"，不测 notability 或实质密度。
2. `add_page.py:168-171`（RFC-central-empire-fiscal-code-0007）新建页**无人工复核、无 notability 门**即自动回填 quality → 填满模板的页面瞬间 featured。
3. `compute_quality.py:163-167` `upgrade_only=True` 默认**只升不降**：featured 具粘性，事后删内容也不降级。

**实证**：`tabor-island-castaway`、`liedenbrock-cipher`（描述性标题的 event 页，语料直接提及 ≈0）与 `captain-nemo`（601 次）同为 featured。featured 与语料出现频次零相关。

**修复方向（择一或组合）**：
- 给 featured 加 notability/实质门：如散文下限提到 ~800–1000 字符，或引入语料提及频次阈值；
- `add_page.py` 自动回填**封顶 `standard`**，featured 需显式人工提升；
- 重新定义：featured=编辑/notability 判断，另设 `complete`=结构完整（机械可判）。

**处置**：属共享 memex 组件（`compute_quality.py`/`add_page.py`）—— 依 RFC 停靠决策 **PARK**，不自动提交；全站建成 + 用户签署后连同 VVV 宽度三 RFC 一并批量评审。此条为待起草 RFC 的种子。

## P2 — 中优先级

## P3 — 低优先级
