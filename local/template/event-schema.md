# Schema: `event`（事件/情节节点）

> MTD3 页面图式模板。情节转折、关键场景。只记引注，不整段复制原文。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 一句话概括：何事、何时（书内）、涉及谁 |
| 2 | What Happens | ✅ | 事件经过（按原书次序，附 PN 引注）|
| 3 | Significance | ○ | 对情节/人物的影响 |
| 4 | Participants & Setting | ○ | 相关 character / place 的 wikilink |

## Frontmatter 专属字段

```yaml
---
id: eighty-day-wager
type: event
label: The Eighty-Day Wager
aliases: []
tags: [event]
description: 'Phileas Fogg''s bet at the Reform Club to circle the globe in eighty days.'
book: Around the World in Eighty Days
location: London               # 主要发生地（wikilink 目标，可空）
pn_anchor: AWED-001-XXX        # 事件起点 PN（可空）
---
```

## 引文规范

- What Happens 节按时间线组织，每个关键节点附 PN 引注。
- 引原文动作/对白用 blockquote ≤ 3 行 + 引注。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + What Happens，≥ 2 条 PN |
| standard | + Significance，≥ 4 条引注 |
| featured | 全部 4 节，≥ 6 条引注，Participants 完整 wikilink |

## 插图引用

不适用（无正文插图）。
