# Vernean Voyages Wiki — 本地法律

> 宪法（`$MEMEX_ROOT/CONSTITUTION.md`）优先。本文件是宪法之下的项目特定补充规范（法源体系 L3）。
> 如有冲突，宪法优先。

---

## 一、项目基本参数

| 参数 | 值 |
|------|-----|
| Wiki 名称 | Vernean Voyages Wiki |
| WIKI_LANG | en |
| 本地端口 | 1828（Jules Verne 生于 1828 年）|
| GitHub remote | （待创建）|
| 发布方案 | Cloudflare Pages |
| 服务器域名 | （待定）|

本地预览：`./wiki-daemon.sh start`，访问 `http://localhost:1828`。

---

## 二、语料声明

- `corpus/raw/`：The Collected Works of Jules Verne（36 部长篇与短篇），**只读，不可修改**。
- 语料为 **public-domain 模式**：全文纳入 git 跟踪，按 Phase 3 默认提交规则。
- 引用语料时只记录位置（作品、章节、段落号），不复制大段原文到实体页。

| 文件/目录 | 内容 | 文件数 | 备注 |
|-----------|------|--------|------|
| `corpus/raw/The Collected Works of Jules Verne ... .epub` | 36 部作品合集（EPUB 原始来源）| 1 | public domain；Phase 3 转为 `doc_final.md` |

---

## 三、PN（段落编号）映射规则

> PN 格式规范来源：`ref/spec/data-pn.md`。

### 格式定义

本 wiki 为多作品合集，采用**三段 PN（volume 方案）**，每部作品为一「卷」：

```
PN = VVV-NNN-PPP
VVV = {作品码}            1–4 个字母/数字，标识 36 部作品之一（见卷号映射表）
NNN = {章号:03d}         该作品内章号，纯数字 (001–999)
PPP = {段号:03d}         段号，纯数字 (001–999)
pn_prefix = VVV-NNN       每章 frontmatter 存此值；全集范围内必须唯一
```

> **VVV 约束**：长度 1–4 字符（正则 `[A-Za-z0-9]{1,4}`），如 `20KL`、`80DA`、`MYST`。
> **pn_prefix 唯一性**：不同作品的「第 1 章」必须有不同 `pn_prefix`（`20KL-001` vs `80DA-001`），否则 `build_fts_index.py` 与 `build_sentence_index.py` 会跨作品碰撞。

### 括号格式（`WIKI_LANG=en`）

| 场景 | 格式 | 示例 |
|------|------|------|
| 章节页段首标注 | `[VVV-NNN-PPP]` | `[20KL-001-007]The sea is everything...` |
| 实体页行内引注 | 半角 `(VVV-NNN-PPP)` | `Nemo commands the Nautilus. (20KL-008-012)` |

### 卷号（VVV）映射表

> 36 部作品各分配一个 VVV 码。完整清单在 Phase 3 解析 EPUB 目录后写入 `ref/chapter-order.md`。

| VVV | 作品 | 说明 |
|-----|------|------|
| （待 Phase 3 补全）| — | 每部作品一码 |

### 规则

1. PN 格式为三段 `VVV-NNN-PPP`。
2. 各章独立计数，PPP 从 `001` 起，PN 一经分配不得变更。
3. 禁止使用 `PRE`、`APP`、`REF`、`IDX` 等非本约定格式的代码。

---

## 四、页面类型

本 wiki 使用以下页面类型（Phase 7 类型勘探后定稿）：

| 类型 | 说明 | 示例 |
|------|------|------|
| `chapter` | 原文章节页（从语料切分）| 20,000 Leagues Ch.1 |
| `character` | 人物角色 | Captain Nemo、Phileas Fogg |
| `place` | 地点/地理 | Nautilus 航线、Iceland |
| `technology` | 机器/发明/科学概念 | Nautilus、Columbiad 巨炮 |
| `event` | 事件/情节节点 | 环球赌约、火山喷发 |
| `work` | 作品（长篇/短篇）| Around the World in Eighty Days |
| `organization` | 组织/团体 | Gun Club、Reform Club |
| `overview` | 综述/导引页（wiki 编辑者手工创建）| Themes overview |
| `list` | 列表页 | List of Verne inventions |

> ⚠️ 所有从语料切分的页面均使用 `type: chapter`；禁止使用 `document` 等不兼容类型。
> `type: overview` 仅用于 wiki 编辑者手工创建的综述/导引页。

---

## 五、页面 slug 命名规范（`WIKI_LANG=en`）

slug（文件名、`id` 字段）**必须使用英文小写 + 连字符**（kebab-case）。

| 规则 | 说明 |
|------|------|
| ✅ 英文 kebab | `captain-nemo`、`phileas-fogg`、`nautilus` |
| ❌ 大写/下划线 | `Captain_Nemo` — 禁止 |
| ❌ 混合格式 | `nemo-船长` — 禁止 |

**例外**：`overview` 类型的系统页面（`About`、`目录` 等）由 memex 框架定义，不受此约束。

**理由**：slug 与 wikilink 解析、文件路径一致，避免双轨并存导致的 alias 冲突和重复页面。

---

## 六、Corpus 只读声明

任何 skill、脚本、Claude 操作，均**禁止修改** `corpus/` 目录下的任何文件。
如需标注，写入 `data/` 目录，不得回写 corpus。

**例外**：BIRTH.md Phase 3（语料准备与校对）期间允许向 `corpus/` 写入。
Phase 3 最后一次提交后恢复只读，后续阶段（Phase 4 起）不再写入。

---

## 七、提交门控

- 直接 `git commit` 被 deny 拦截
- 授权提交须走：`bash wiki/scripts/wiki_commit.sh`
- Skill 提交须走：`bash wiki/scripts/skill_commit.sh`

---

## 八、Frontmatter 书写规范

**YAML 值含冒号或引号时必须加单引号**，否则 `build_registry.py` 的 YAML 解析失败，
整个 frontmatter 被丢弃，导致 `type` 变成 `"unknown"`、`aliases` 变成 `[]`。

```yaml
# ❌ 错误：description 值含冒号
description: A novel: Twenty Thousand Leagues Under the Seas.

# ✅ 正确：用单引号包裹含冒号或双引号的值
description: 'A novel: Twenty Thousand Leagues Under the Seas.'
```

受影响字段：`description`、`label`（含特殊字符时）、任何自由文本字段。

---

## 九、Wikilink 书写规范

Wikilink 应优先使用 **label 形式**，而非 slug 形式：

```markdown
✅ [[Captain Nemo]]         ← label 形式，人类可读
❌ [[captain-nemo]]         ← slug 形式，仅在无对应 label 时使用
```

章节页使用 id（含大写和连字符）可接受：

```markdown
✅ [[20KL-Chapter-1]]    ✅ [[80DA-Chapter-28]]
```

---

## 十、Label 唯一性约束

每个词条的 `label` 在本 wiki 内必须唯一。`build_registry.py` 将 label 写入 `alias_index`，
若两个词条共享同一 label，后者会覆盖前者，导致链接解析错误。

- 新建词条前先搜索现有 label 确认无重名
- 若确实存在同名概念，用更具体的 label 区分
- `aliases` 字段同样受此约束

---

## 十一、日志格式规范

### 文件命名

`{YYYY-MM-DD}-R{轮次}-{gene}-{type}-{摘要}.md`

例：`2026-05-26-R128-NEW1-new-pages.md`

### 标准结构

每轮 gene-express 日志必须包含 frontmatter 字段：`round`、`date`、`phase`、`gene`、`pages`、`result`。

内容章节：`## 执行摘要`、`## 页面处理记录`（表格）、`## EXIT-GATE 检查`、`## 遗留问题`。

---

## 十二、标签约定（`WIKI_LANG=en`）

标签（`tags:` 字段）**一律使用英文**：

- 主题标签：`science-fiction`、`adventure`、`exploration`、`submarine`、`ballooning` 等
- 时代标签：`1860s`、`1870s`、`1880s` 等
- 性质标签：`character`、`technology`、`voyage`、`invention` 等

---

*本文档适用于 Vernean Voyages Wiki 项目，受 `$MEMEX_ROOT/CONSTITUTION.md` 约束。*
