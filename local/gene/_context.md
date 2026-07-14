# Vernean Voyages Wiki — Butler 执行上下文

> butler / enrich 等 skill 每轮读取本文件，获取本 wiki 专属约定。

## 语言

- `WIKI_LANG=en`：所有页面正文、label、tags、description 用英文。
- slug 用 kebab-case（`captain-nemo`），禁止大写/下划线。

## PN 格式与作品范围

- 三段 PN：`VVV-NNN-PPP`（VVV=作品码，NNN=章号，PPP=段号）。
- 语料为 36 部作品合集；每部作品一个 VVV 码，映射表见 `ref/chapter-order.md`（Phase 3 后补全）。
- 章节页段首标注 `[VVV-NNN-PPP]`；实体页行内引注半角 `(VVV-NNN-PPP)`。

## 页面类型

`chapter` · `character` · `place` · `technology` · `event` · `work` · `organization` · `overview` · `list`

- 语料切分页一律 `type: chapter`。
- `overview` 仅限手工创建的综述页。

## 质量档位

- 档位序列：stub → basic → standard → featured → premium（memex 通用）。
- 实体页引用语料只记录 PN 位置，不整段复制原文。

## 其他约定

- 语料 `corpus/` 只读（Phase 3 例外）。
- 提交走 `wiki/scripts/skill_commit.sh`；直接 `git commit` 被拦截。
