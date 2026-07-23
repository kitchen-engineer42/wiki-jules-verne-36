# Schema: `place`（地点/地理）

> MTD3 页面图式模板。真实地理与虚构地点通用。只记引注，不整段复制原文。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 定位：真实/虚构、所属作品、地理位置 |
| 2 | In the Narrative | ✅ | 在情节中的角色、发生的关键事件（附 PN）|
| 3 | Geography & Features | ○ | 地形、气候、自然特征描写 |
| 4 | Connections | ○ | 相关 character / event / 相邻 place 的 wikilink |

## Frontmatter 专属字段

```yaml
---
id: lincoln-island
type: place
label: Lincoln Island
aliases: []
tags: [place]
description: 'The volcanic island where the castaways settle in The Mysterious Island.'
book: The Mysterious Island
real_or_fictional: fictional   # real / fictional
region: South Pacific          # 大区域（可空）
---
```

## 引文规范

- **散文/主张节**（Overview、In the Narrative、Geography & Features）每节 ≥ 1 条 PN 引注。地理描写引原文时用 blockquote ≤ 3 行 + 引注。
- **Connections 为 wikilink 交叉引用节**，质量准则是**链接完整性**（见质量阈值表「Connections 完整」），不强制 PN——该节列相关 character/event/相邻 place 的 wikilink，属跨引而非语料主张。若某条关系需佐证可选附 PN，但非硬性要求。
- 真实地名标注凡尔纳时代拼写与现代拼写差异（若有）。

## 写作指引（EVV5 r1，2026-07-13 追加）

- **real/fictional 双档均适配四节**：真实地点（snaefellsjokull、tampa-town、reform-club）以 Geography & Features 述真实地理，虚构地点（lincoln-island、liedenbrock-sea）以该节述作者构造的地形。r1 全 5 页四节自然成立，无空节张力。虽 Geography & Features / Connections 标 ○（选填），实践上 standard 档应尽量写全四节。
- **`region` 可容非常规地理层级**：不限于洲际大区，subterranean（地底海 liedenbrock-sea）、城镇级（Florida/London）均可填，按「地点所属的最有辨识度的空间归属」取值。
- **段落 ≤400 字**：`edit_page.py` 质量门对段落上限 400 字符（退出码 8），每节按论点拆多段。
- **引文逐字核验 + sentence_index 兜底**：只采用对章节页原文核验过的引文；`corpus_search.py` 为关键词 AND 语义，多关键词易零命中，改用 1–2 关键词或直接读 `data/sentence_index/{PN前缀}.jsonl` 后以精确短语回定 PN（liedenbrock-sea 的 JCE-031-009/038/002 即此法）。
- **quality 字段省略**：建页时省略 frontmatter 的 `quality`，交 `add_page.py` 自动回填（沿用 technology EVV6 定策）。r1 全 5 页自动回填 featured。

## 写作指引（EVV5 r2，2026-07-13 追加）

- **无陆地地形地点的 Geography & Features 替代维度**：都市（baltimore）、海域（sargasso-sea）、极地目标（north-pole）等无常规山川地形的地点，Geography & Features 节改述**该地点的定义性物理特征**——都市写行政/交通枢纽与市政规模、海域写洋流环抱与漂浮植被、极地写岛体尺寸与火山构造。避免为凑「地形」硬写不存在的山河。r2 五页均以此法填满该节，无空节。
- **抽象地理点可作 place**：地理概念（北极点）在语料中被具象化（Queen's Island 火山岛）时即为合法 place 实体；label 用具象名或概念名均可，aliases 收另一名（north-pole aliases=[Queen's Island]）。
- **meta 表述触发 overlap warn**：Geography 等节避免「Its X is explicit in the narrative...」式元叙述句挂引注——`add_page.py` 的 overlap 校验会因 token 重叠过低告警。改为直接引原文子句（「the volcano arose in the north」），warn 消除。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + In the Narrative，≥ 2 条 PN |
| standard | + Geography & Features，≥ 5 条引注 |
| featured | 全部 4 节，≥ 8 条引注，Connections 完整 |

## EVV6 定稿（converged，2026-07-13）

- **收敛结论**：三轮差异化批次（最强实体 → 新子领域 → 边缘/复杂案例）15 页零结构偏差；模板追加量 5→3→0，r3 边缘批次零追加。schema **converged**，四节结构（Overview / In the Narrative / Geography & Features / Connections）+ `book`/`real_or_fictional`/`region` 专属字段定稿，不再变更。与 technology schema（追加量 3→2→0）收敛轨迹同构。
- **quality 工具计算权威**：以 `compute_quality.py` 客观评级为准。建页时省略 frontmatter 的 `quality` 字段，交 `add_page.py` 自动回填；日志不手记档位。15 页 place 经 compute_quality 统一后全部 featured。
- **edit_page 后补跑 compute_quality**：用 `edit_page.py` 修改页面内容后，`quality` 不会自动回填（仅 `add_page.py` 回填），需补跑 `compute_quality.py` + `build_registry.py`，否则 registry quality 可能失配（R12 mount-franklin 即此坑，已于 R14 修正）。此为通用操作提示，适用所有类型。
- **跨作品地点 book 字段**：维持单值填主作品（信息最丰富者）+ 正文点名其余作品并引 PN（the-moon：book=Round the Moon，正文兼述 From the Earth to the Moon）。跨作品实体累计 2 例（+technology gun-cotton）<5 阈值，暂不提多值字段 RFC。

## 插图引用

不适用（无正文插图）。
