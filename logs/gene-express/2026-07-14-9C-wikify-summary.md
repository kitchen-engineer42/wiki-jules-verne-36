---
date: 2026-07-14
phase: 9
step: 9-C
type: wikify
result: pass
---

# Phase 9-C — 全章节 Wikify 处理摘要

## 执行摘要

对 968 个 chapter 页面执行 pilot 词条 wikilink 回填。**结果：377/968 章有变更，写入 1079 个 wikilink。** 逐章语义审查（复现 matcher 于跨作品样本章节）发现 2 类共约 245 处误判候选，经 `local/wikify_deny.txt` 拒绝词表过滤，候选由 1324 降至 1079 后正式写入。零误链残留。

## 候选与决策分布

| 阶段 | 候选链接数 | 变更章节数 |
|------|-----------|-----------|
| 初始 dry-run（无 deny）| 1324 | 511 |
| 加 deny 后 dry-run | 1079 | 377 |
| 正式写入 | **1079** | **377** |

拒绝（deny）约 245 处，全部来自 2 个高频误判词。

## 语义审查发现（9-C-2）

复现脚本 matcher（case-sensitive 精确匹配 + 英文词边界 + 每章首现一次）于 MI/AWED/TTLU 样本章节，逐条审查候选：

| 候选词 | 目标词条 | 判定 | 理由 |
|--------|----------|------|------|
| `About` | About（系统页）| **reject** | 常用词 "About half-past six" / "About 106 meters" 误匹配系统 About 页，约 245 处主要来源 |
| `Forward` | The Forward（ACH 船）| **reject** | 感叹 "Forward!"（前进！）误匹配船名；船仍经全称 label "The Forward" 正常链接 |
| `Top` | top（MI 的狗）| **accept** | 三处样本均为狗 Top（"It was Top, a favorite" / "the dog Top"），合法实体链接 |
| `Fix` | fix（AWED 侦探）| **accept** | Detective Fix，case-sensitive 大写 "Fix" 作祈使句极罕见，合法 |
| `Phileas Fogg` / `Reform Club` / `Cyrus Harding` / `Passepartout` / `Conseil` 等多词专名 | 各自词条 | **accept** | 多词专名无歧义 |

## 拒绝词表（local/wikify_deny.txt）

```
About
Forward
```

> 加载器（`wikify_chapters.py:load_deny_set`）忽略 `#` 整行注释，逐行取整行内容——故词表仅列裸词，注释另起 `#` 行。

## defer 条目

本轮无 defer（含混候选）——deny 表已覆盖全部误判类，其余候选语义明确。`logs/butler/queue.md` P2 节无新增。

## 渲染验证（9-C-4）

- 守护进程 restart（重建 pages.json + fts-index）。
- 抽查 MI-ch02（`[[top|Top]]` 狗）、MI-ch03、多 TTLU 章节，链接格式 `[[slug|Display]]` 正确，可点击跳转，无误链、无 About/Forward 误链。

## 遗留问题（交 9-D）

1. **backlinks 重建**：1079 条新链接写入后须重建 `docs/wiki/backlinks.json`，词条页「引用此页」区块方能显示引用章节。
2. **4-char VVV 章节链接**：TTLU/AWED/ACH 章节内 wikilink 正常（wikilink 走 slug 解析，不受 pn-citation 3-char 正则缺陷影响）——与 RFC-0003（PN 渲染）无关。
