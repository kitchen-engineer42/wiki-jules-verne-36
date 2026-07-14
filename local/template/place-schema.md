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

- 每节 ≥ 1 条 PN 引注。地理描写引原文时用 blockquote ≤ 3 行 + 引注。
- 真实地名标注凡尔纳时代拼写与现代拼写差异（若有）。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + In the Narrative，≥ 2 条 PN |
| standard | + Geography & Features，≥ 5 条引注 |
| featured | 全部 4 节，≥ 8 条引注，Connections 完整 |

## 插图引用

不适用（无正文插图）。
