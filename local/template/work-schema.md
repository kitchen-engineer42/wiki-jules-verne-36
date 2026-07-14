# Schema: `work`（作品：长篇/短篇）

> MTD3 页面图式模板。每部作品一个 work 词条（共 35），作为跨作品导航枢纽。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 体裁、出版背景、一句话梗概 |
| 2 | Plot Summary | ✅ | 分卷/分章梗概（链接 `[[VVV-chNN]]`）|
| 3 | Main Characters | ○ | 核心 character wikilink 列表 |
| 4 | Key Places & Technology | ○ | 相关 place / technology wikilink |
| 5 | Themes | ○ | 主题（探险、科学、殖民等）|

## Frontmatter 专属字段

```yaml
---
id: twenty-thousand-leagues
type: work
label: Twenty Thousand Leagues Under the Sea
aliases: []
tags: [work, science-fiction]
description: 'An 1870 Jules Verne novel following Captain Nemo aboard the Nautilus.'
vvv: TTLU                     # 作品码（对应 chapter_map / pn_prefix）
chapter_count: 47             # 该作品章节数
genre: novel                  # novel / short-story
---
```

## 引文规范

- Plot Summary 每卷/大段附代表性 PN 引注。
- work 页以 wikilink 导航为主，PN 密度低于 character/event 页。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Plot Summary，链接全部章节页 |
| standard | + Main Characters + Key Places，≥ 3 条 PN |
| featured | 全部 5 节，Themes 有分析，双向 wikilink 完整 |

## 插图引用

不适用（无正文插图）。
