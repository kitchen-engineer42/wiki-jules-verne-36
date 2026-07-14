# Schema: `character`（人物角色）

> MTD3 页面图式模板。NEW1 建页时据此组织结构与字段。语料为 public-domain，
> 实体页只记引注（`(VVV-NNN-PPP)`），不整段复制原文。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 一段定位：身份、所属作品、核心特征 |
| 2 | Role in the Story | ✅ | 在情节中的作用、关键行动（附 PN 引注）|
| 3 | Character & Traits | ○ | 性格、动机、象征意义 |
| 4 | Relationships | ○ | 与其他 character 的 wikilink 关系 |
| 5 | Appearances | ○ | 出场章节列表（`[[VVV-chNN]]`）|

## Frontmatter 专属字段

```yaml
---
id: captain-nemo
type: character
label: Captain Nemo
aliases: []
tags: [character]
description: 'Commander of the Nautilus in Twenty Thousand Leagues Under the Sea.'
book: Twenty Thousand Leagues Under the Sea   # 主要出处作品
affiliation: ''            # 所属组织/团体（可空）
first_appearance: TTLU-006 # 首次出场 pn_prefix（可空）
role: protagonist          # protagonist / antagonist / supporting / narrator
---
```

## 引文规范

- 每个 H2 节至少 1 条 PN 引注 `(VVV-NNN-PPP)`，半角括号（WIKI_LANG=en）。
- blockquote 仅用于原文关键台词/描写，≤ 3 行，附引注。
- PN 密度期望：standard 档每 200 词 ≥ 1 条。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Role，≥ 2 条 PN 引注 |
| standard | + Character & Traits，≥ 5 条引注，≥ 2 条 wikilink |
| featured | 全部 5 节，≥ 10 条引注，Relationships 完整，无悬挂链接 |

## 插图引用

不适用（语料为 Calibre 纯文字重构稿，无正文插图）。
