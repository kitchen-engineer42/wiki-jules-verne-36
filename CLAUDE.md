# Vernean Voyages Wiki — Claude 入口

> **首先阅读宪法：** `$MEMEX_ROOT/CONSTITUTION.md`（全局不可违背规则）
> **其次阅读本地法律：** `LAW.md`（本 wiki 补充规则）
> **然后启动 BIRTH：** `BIRTH.md`（引导建设流程）
> 如有冲突，宪法优先。本文档仅作入口说明。

告诉 Claude 本 wiki 的法律规范位于 `LAW.md`。

@LAW.md

---

## MEMEX_ROOT

共享代码源位于 `~/memex`（本机 symlink）。所有脚本、skills、CONSTITUTION 均通过此路径引用。

```bash
MEMEX_ROOT="$HOME/memex"
export MEMEX_ROOT
```

## Python 环境

Python 调用入口在 `local/config.md` 中配置（由 BIRTH 0-A 初始化）。本 wiki 为 `system` 模式：

| 键 | 值 |
|---|---|
| `PYTHON_ENV` | `system` |
| `PYTHON_BIN` | `python3` |
| `PIP_CMD` | `pip3` |

## /boot

定义在共享 skill。执行 `BIRTH.md`，推进下一个未完成的 phase。

## 项目配置

### PN 映射

| 范围 | 内容 |
|------|------|
| 待 Phase 5 赋号后填写 | 每部作品一段 NNN 前缀 |

### 页面类型（初拟，Phase 7 定稿）

| type | 含义 |
|------|------|
| character | 人物角色 |
| place | 地点/地理 |
| technology | 机器/发明/技术 |
| event | 事件 |
| organization | 组织/团体 |
| work | 作品（小说/短篇）|
| chapter | 原文章节页（从语料切分）|

### Frontmatter

```yaml
---
id: entry-name
type: character
label: Display Name
aliases: []
tags: []
description: One-sentence description
---
```

## 工作流

```bash
# 新建页面
python3 "$MEMEX_ROOT/wiki/scripts/add_page.py" SLUG - \
  --summary "add: SLUG" --author butler << 'EOF'
[frontmatter + content]
EOF

# 本地预览
./wiki-daemon.sh start    # http://localhost:1828

# 发布
./publish.sh
```
