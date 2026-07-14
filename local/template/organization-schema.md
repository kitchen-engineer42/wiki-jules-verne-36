# Schema: `organization`（组织/团体）

> MTD3 页面图式模板。Gun Club、Reform Club、探险队/船员团体等。只记引注。
> （占比 ~3%，< 5% 阈值，模板为可选补充；因该类型在多章复现且驱动情节，一并设计。）

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 性质、所属作品、成立背景 |
| 2 | Role in the Story | ✅ | 在情节中的作用（附 PN 引注）|
| 3 | Members | ○ | 核心成员 character wikilink |
| 4 | Activities | ○ | 主要行动/计划 |

## Frontmatter 专属字段

```yaml
---
id: gun-club
type: organization
label: Gun Club
aliases: []
tags: [organization]
description: 'The Baltimore artillery club that launches a projectile to the Moon.'
book: From the Earth to the Moon
org_type: club                # club / crew / expedition / society
founded: ''                   # 书内成立背景（可空）
---
```

## 引文规范

- 每节 ≥ 1 条 PN 引注。成员/宗旨引原文用 blockquote ≤ 3 行 + 引注。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Role in the Story，≥ 2 条 PN |
| standard | + Members，≥ 4 条引注，成员 wikilink |
| featured | 全部 4 节，≥ 6 条引注，Members/Activities 完整 |

## 插图引用

不适用（无正文插图）。
