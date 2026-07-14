# 实体类型勘探报告（SCN23）— Vernean Voyages Wiki

- **日期**: 2026-07-13
- **执行**: `/boot --auto` Phase 7-A
- **语料范围**: 35 部凡尔纳作品 / 968 章 / 58,399 段 / 122,989 句
- **类型基准**: LAW.md 四（9 类型），本报告勘探其中 6 类**实体**类型的分布与权重
  （`chapter` 为语料页、`overview`/`list` 为编辑页，不计入实体勘探）

## 方法

- 章节页正文抽样 + 高频专有名词跨章计数（grep 定位复现实体）
- 结合 35 部作品的题材先验（探险 / 科幻 / 地理）估算各类型规模
- 估算数为**建页先验**（供 NEW1 批量建页与分类查询定容），非精确普查

## 类型分布估算

| type | 权重 | 估算词条数 | 典型实例 | 说明 |
|------|------|-----------|----------|------|
| `character` | ~40% | 180–240 | Captain Nemo（Nautilus 50 章复现）、Phileas Fogg（37）、Passepartout（33）、Axel、Professor Aronnax、Ned Land、Michel Ardan、Ayrton（61）、Captain Hatteras（64）、Dick Sand | 主角/配角/叙述者；跨作品同名需 label 消歧 |
| `place` | ~22% | 100–140 | Nautilus 航线、Iceland/Snæfell、Lincoln Island、the Moon、Central Africa、Siberia、Amazon、the North Pole | 真实地理 + 虚构地点（火山口、荒岛）|
| `technology` | ~16% | 70–100 | Nautilus（45 章）、Columbiad 巨炮（32）、Albatross 飞行器、Épouvante、气球 Victoria、electric devices | 机器/发明/科学概念——凡尔纳标志性 |
| `event` | ~10% | 45–70 | 环球 80 天赌约、Columbiad 发射、火山喷发脱险、海底森林狩猎、Lincoln Island 覆灭 | 情节节点/转折 |
| `work` | ~9% | 35 | Twenty Thousand Leagues…、Around the World in Eighty Days、From the Earth to the Moon … | 每部作品一个 work 词条（已知 35 部，1:1）|
| `organization` | ~3% | 10–18 | Gun Club（48 章）、Reform Club、Baltimore Gun Club 附属、探险队/船员团体 | 组织/团体，数量少但结构重要 |

**合计估算实体词条**：约 440–620（不含 968 章节页与 About/TOC）。

## 边缘类型判定

- 所有 6 类占比均 ≥ 3%，**无 < 1% 边缘类型**，无需合并。
- `work`（9%）虽数量固定为 35，但作为跨作品导航枢纽保留独立类型。
- `organization`（3%）为最小实体类型，但 Gun Club / Reform Club 等在多章复现且驱动情节，保留。

## 结论

- 主要实体 `type` 值集合（权重降序）：`character` > `place` > `technology` > `event` > `work` > `organization`。
- 与 `docs/wiki/local/config/types.js` 现有 9 键完全一致（LAW.md 四 Phase 2 已配置），**无需新增/删除类型**。
- 7-B 仅需核验 label 覆盖，7-C 为 6 个实体类型各设计 schema 模板。
