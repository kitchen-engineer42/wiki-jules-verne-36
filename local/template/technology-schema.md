# Schema: `technology`（机器/发明/科学概念）

> MTD3 页面图式模板。凡尔纳标志性类型（Nautilus、Columbiad 等）。只记引注。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 定位：发明/机器/概念、所属作品、发明者 |
| 2 | Design & Operation | ✅ | 结构、工作原理、原文描述的参数（附 PN）|
| 3 | Role in the Story | ○ | 在情节中的功能与关键使用场景 |
| 4 | Science & Speculation | ○ | 凡尔纳的科学依据 vs 想象；现实对照 |

## Frontmatter 专属字段

```yaml
---
id: nautilus
type: technology
label: Nautilus
aliases: []
tags: [technology, invention]
description: 'Captain Nemo''s electric-powered submarine in Twenty Thousand Leagues Under the Sea.'
book: Twenty Thousand Leagues Under the Sea
inventor: Captain Nemo        # 发明者/建造者（wikilink 目标，可空）
category: vehicle             # vehicle / weapon / instrument / concept
---
```

## 引文规范

- Design & Operation 节引原文技术参数处必附 PN 引注。
- 数值/尺寸引用用 blockquote ≤ 3 行 + 引注，保留原书单位。

## 写作指引（EVV5 r1，2026-07-13 追加）

- **Science & Speculation 建议纳入 standard 页**：凡尔纳技术类实体多改编自真实器械（Ruhmkorff 感应线圈、Rouquayrol-Denayrouze 潜水调节器）或以弹道/轨道力学为据（Columbiad、Projectile）。以"真实器械 vs 凡尔纳外推"的框架收束，能显著提升条目价值；technology r1 全部 5 页均自发采用此节。虽仍标 ○（选填），实践上 standard 档应尽量写。
- **段落 ≤400 字**：`edit_page.py` 质量门对段落上限 400 字符（退出码 8），每节按论点拆多段。
- **引文逐字核验**：只采用对章节页原文 grep 核验过的引文；`corpus_search.py` 快照与页面正文存在个别 PN 错位（如 spindle 描述实际在 MW-015-026 而非快照标注处），一律以页面正文为准。

## 跨作品实体（EVV5 r2，2026-07-13 追加）

- **`category=concept` 亦适用本 schema**：抽象物质/科学概念（如 gun-cotton/pyroxyle）可复用四节结构——Design & Operation 述「制法/理化性质」，Role in the Story 述「跨作品用途」。已验证无空节张力。
- **单值 `book` 字段处置跨作品实体**：`book` 只填**主作品**（信息最丰富者），其余作品在正文点名并引 PN 即可（如 gun-cotton：book=From the Earth to the Moon，正文兼述 The Mysterious Island）。勿臆造多值字段。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Design & Operation，≥ 2 条 PN |
| standard | + Role in the Story，≥ 5 条引注 |
| featured | 全部 4 节，≥ 8 条引注，Science & Speculation 有现实对照 |

## EVV6 定稿（converged，2026-07-13）

- **收敛结论**：三轮差异化批次（具象机器/仪器 → 航空航海载具+concept → 边缘/复杂案例）15 页零结构偏差；模板追加量 3→2→0，r3 边缘批次零追加。schema **converged**，四节结构 + `book`/`inventor`/`category` 专属字段定稿，不再变更。
- **quality 工具计算权威**：以 `compute_quality.py` 客观评级为准。**建页时省略 frontmatter 的 `quality` 字段**，交 `add_page.py` 自动回填；日志不手记档位。此前 r1/r2 人工写 `quality: standard` 属最低 floor 下压，已由 compute_quality 统一升级对齐（16 页均 featured）。BIRTH「standard」目标理解为 floor 而非固定值。
- **跨作品实体 book 字段**：维持单值填主作品 + 正文引其余作品 PN。暂不提多值字段 RFC（个案 <5，正文补偿充分）。

## 插图引用

不适用（无正文插图）。
