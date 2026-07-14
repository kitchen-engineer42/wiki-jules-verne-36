---
round: 5
date: 2026-07-13
phase: 9
gene: SCN27
type: technology
pages: [giant-telescope, nitroglycerine, granite-house-lift, nemo-electricity, jangada]
result: accept
---

# R5 — SCN27 technology r3（Phase 9-B 第三轮 · 边缘/复杂案例）

## 执行摘要

technology 类型第三轮，按 schema 流程要求专选**边缘/复杂案例**做最后一轮压力测试，使用 EVV5 r2 更新后的模板。5 页覆盖 4 部作品，全部 corpus-grounded（每句有据）：

- **Giant Telescope**（FEM）— Long's Peak 280 英尺巨型反射望远镜，边缘=巨型固定仪器，强耦合 columbiad/lunar-projectile
- **Nitroglycerine**（MI）— Cyrus Harding 合成的液体炸药，边缘=与 gun-cotton 近重复（差异化测试）
- **Granite House Lift**（MI）— 水力升降机，边缘=多组件机械系统（水轮+缆绳+basket）
- **Nemo's Electricity**（TTLU）— 海水钠电池自给电力，边缘=强耦合 nautilus + 4 字符 VVV 渲染 caveat
- **Jangada**（EHLA）— 亚马逊巨型木筏（浮动村落），边缘=复杂建造载具，全新作品

引注方法一如既往：`corpus_search.py` 定位候选 → 读章节/句子索引原文 grep 逐字核验 → 仅采用核验过的引文。

## 页面处理记录

| slug | type | category | 作品(VVV) | 引注(occur) | PN 来源示例 | quality | QUO7 |
|------|------|----------|-----------|-------------|-------------|---------|------|
| giant-telescope | technology | instrument | FEM | 9 | FEM-024-014/015/016/022/023/024/025, FEM-028-002, RM-007-048 | featured | 无问题 |
| nitroglycerine | technology | concept | MI | 11 | MI-017-050/053/054/055/056/058/063/064/066/067, MI-018-003 | featured | 无问题 |
| granite-house-lift | technology | instrument | MI | 9 | MI-031-018/019/020/021, MI-033-079, MI-034-033 | featured | 无问题 |
| nemo-electricity | technology | concept | TTLU | 8 | TTLU-012-011/014/015/017/019/021/023/025 | featured | 无问题 |
| jangada | technology | vehicle | EHLA | 6 | EHLA-006-005/010/015/016 | featured | 无问题 |

## 边缘案例压力测试结果

- **近重复实体（nitroglycerine vs gun-cotton）**：两者均 `category=concept` 化学炸药，同属 MI 语境。差异化成功——nitroglycerine 的 Design & Operation 述「azotic acid + glycerine 合成 + 冲击敏感」，Science & Speculation 显式对照 gun-cotton 条目并点出「同一 castaway-as-chemist 主题的不同外推」。schema 四节足以承载两个相邻实体而不塌缩为重复。
- **多组件机械系统（granite-house-lift）**：水轮+缆绳+wheel+basket 的复合结构在 Design & Operation 单节内以「动力源→传动→载体」层次清晰展开，无需为子部件另开节。schema 对复合机械稳健。
- **强耦合抽象概念（nemo-electricity）**：紧贴 nautilus，但独立成页无空节张力——Design & Operation 承载 Bunsen 电池/钠汞齐/海水成分理化细节，与 nautilus 载具页职责不重叠。concept 页第二次验证适配（首次为 gun-cotton）。
- **全新作品（jangada/EHLA）**：首次为 EHLA 建页，schema 无摩擦即适配「夸张而非虚构」型 technology（真实巴西木筏放大至岛屿尺度）。

## EVV5 r2 模板应用检查

- **Science & Speculation 常态化**：5 页全部写此节，均以「真实基础 vs 凡尔纳外推/夸张」收束，验证该指引在边缘案例仍适用。
- **`category=concept` 指引（EVV5 r2）**：nitroglycerine/nemo-electricity 两个 concept 页均按指引，Design & Operation 述制法/理化性质，Role 述情节用途，无空节。
- **单值 book 字段（EVV5 r2）**：nitroglycerine 主作品 MI；nemo-electricity 主作品 TTLU；均无跨作品张力（gun-cotton 式的跨作品实体本轮未再现）。
- **段落 ≤400 字**：5 页无退出码 8。
- **quality 自动回填 featured**：本轮 5 页 `add_page.py` 均自动回填 `quality=featured`（全 4 节 + 引注达量 + Science & Speculation 含现实对照，满足 featured 三条件）。这是「达标即提 featured」问题的首次实际触发——**工具已自动判档，非人工提档**。与前两轮（r1/r2 记 standard）产生档位不一致，留 EVV6 统一裁决批次档位策略。

## EXIT-GATE 检查

- QUO7：5 页 `pn_format_lint --fix` 全部「无问题」。
- `lint_bucket_structure --fix`：「分桶结构正常，pages/ 与 history/ 根无散落 .md」。
- 继承 caveat：TTLU 4 字符 VVV 行内引注渲染为纯文本（RFC-0003 parked），nemo-electricity 页已在 Science & Speculation 末尾标注此已知问题；数据合法待上游修复。
- 完整 E1–E5 出口门在 technology 三轮结束后（EVV6 之后）统一执行。

## 遗留问题

- **档位不一致**：r1/r2 记 standard，r3 工具自动回填 featured。EVV6 须裁决：是回填统一 r1/r2 至 featured（若达标），还是确立「工具自动判档为准、日志不再手记档位」策略。倾向后者。
- want-link（[[Gun Club]]、[[Cyrus Harding]]、[[Joam Garral]]、[[Captain Nemo]] 等）待 character/organization 轮次建页后由 9-C wikify 回填。已建交叉链接：giant-telescope→Columbiad/Lunar Projectile、nitroglycerine→Gun-Cotton、nemo-electricity→Nautilus。
- 三轮（15 页）SCN27 完成，结构零偏差延续。QUO23 配额检查（R=6）与 EVV5 r3（R=7）待执行，EVV6（R=8）判收敛。
