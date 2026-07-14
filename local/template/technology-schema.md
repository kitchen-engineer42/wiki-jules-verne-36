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

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Design & Operation，≥ 2 条 PN |
| standard | + Role in the Story，≥ 5 条引注 |
| featured | 全部 4 节，≥ 8 条引注，Science & Speculation 有现实对照 |

## 插图引用

不适用（无正文插图）。
