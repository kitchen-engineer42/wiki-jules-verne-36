# Vernean Voyages Wiki

An encyclopedia of Jules Verne's *Voyages Extraordinaires* — the people, places, machines, and events across 36 novels and short stories.

遵循 Memex Wiki 宪法（`$MEMEX_ROOT/CONSTITUTION.md`）。
本地法律见 [LAW.md](LAW.md)。

## 目录结构

```
├── corpus/          原文语料
├── docs/wiki/       发布站点（由 publish.sh 生成，纳入版本控制）
├── data/            中间数据
├── local/           本地定制
└── ...
```

完整规范见 `$MEMEX_ROOT/CONSTITUTION.md` §0.2。

## 快速开始

```bash
# 本地预览（端口 1828 — Jules Verne 生于 1828 年）
./wiki-daemon.sh start          # http://localhost:1828

# 发布（推荐统一走 /wiki skill：重建注册表 → publish.sh → commit）
./publish.sh
```

## 相关链接

- Memex 共享代码库（`$MEMEX_ROOT`）
- （GitHub Pages URL 待仓库创建后补充）
