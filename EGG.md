# Vernean Voyages Wiki — 孵化入口 (EGG)

> **机器入口文件**：Claude agent 进入新 wiki 项目后第一个要读的文件。
> 本文件来自 `$MEMEX_ROOT/EGG.spec.md`，是通用模板。新 wiki 建立 `EGG.md` 后按实际进度填写。

---

## 前置检查

- [x] **确认 `$MEMEX_ROOT` 存在**且指向 memex 仓库：
  ```bash
  echo "$MEMEX_ROOT"   # 应为 ~/memex 或其真实路径
  ls "$MEMEX_ROOT/CONSTITUTION.md"
  ```
- [x] **确认共享 skills 可用**（全局安装，只需一次）：
  ```bash
  bash "$MEMEX_ROOT/wiki/scripts/init_skills.sh"
  ```
  安装后 `/boot`、`/comply`、`/butler`、`/commit` 等 skill 自动可用。
- [x] **确认 Claude 版本支持 skills 和 slash commands**（本项目所需）。

---

## Step 0 — 项目初始化

> 从零开始的项目，先完成以下两步基础建设。

### 0-A 建立 Git 仓库

```bash
git init --initial-branch=master
git add -A && git commit -m "chore: init"
```

### 0-B 准备语料

将原始语料文件放入 `corpus/raw/`：

```
corpus/raw/
├── <project-name>/
│   ├── doc_final.md        # 校对终稿（若已有）
│   ├── book.epub           # epub 来源（可选）
│   └── book.pdf            # PDF 来源（可选）
```

- 若已有 `doc_final.md`，直接进入 Step 1
- 若只有 epub/pdf，留待 BIRTH Phase 3 处理
- 若完全没有语料，先准备好语料再继续

### 0-C 确认工具链

- [x] Git 已安装并配置 user.name / user.email
- [x] Python 3.10+ 可用（3.12.7）
- [x] pandoc（可选，epub 转换用）
- [x] Node.js（可选，引擎本地预览用，v24.16.0）

### 0-D 安装 Python 依赖

将 memex 的通用依赖模板复制为本项目 `requirements.txt`，并按需安装：

```bash
cp "$MEMEX_ROOT/requirement.template.txt" requirements.txt
# 编辑 requirements.txt，取消注释本 wiki 需要的依赖
# 然后安装：
pip install -r requirements.txt
```

- [x] `requirements.txt` 已建立（从 `$MEMEX_ROOT/requirement.template.txt` 复制）
- [ ] 必装依赖已安装

  > **CJK wiki（中文/日文/韩文）必须安装 `pypinyin`**，否则 `page_bucket.py` 在遇到汉字 slug 时会抛出 ImportError，导致 BIRTH/GROW/Butler 中所有涉及页面创建的步骤失败。
  > 安装：`pip install pypinyin`（或 `uv pip install pypinyin`）

---

## Step 1 — 接入 Boot 流程

完成 Step 0（git + corpus）后，进入 boot 主循环。

BIRTH（启动流程）分 10 个 Phase，从 Phase 1 到 Phase 10 逐阶段推进。
每个 Phase 执行以下三命令循环：

```
/boot init phaseN      # 从 BIRTH.spec.md 复制 Phase N 规范，填写本 wiki 参数
/comply BIRTH.md phase N  # 合规检查：参数完整、无遗漏步骤、无违宪内容
/boot phaseN           # 执行 Phase N：逐项完成 [ ] 步骤
```

**执行说明**：

| 步骤 | 命令 | 作用 |
|------|------|------|
| 初始化 | `/boot init phaseN` | 从 `$MEMEX_ROOT/BIRTH.spec.md` 复制 Phase N。每行 `[ ]` 保持空白 |
| 合规检查 | `/comply BIRTH.md phase N` | 验证是否忠实于 spec、`{{占位符}}` 是否全部替换 |
| 执行 | `/boot phaseN` | 从第一个未勾选的 `[ ]` 开始执行 |

**Phase 概要**：

| Phase | 内容 | 关键产出 |
|-------|------|---------|
| 1 | 引擎接通 | `docs/wiki/index.html`，本地预览可启动 |
| 2 | Wiki 配置 | 插件配置、About 页、主题配色、Hero |
| 3 | 语料准备 | `corpus/raw/<project>/doc_final.md`，质检完成 |
| 4 | 章节导入 | 所有章节进入 `docs/wiki/pages/`，目录页、首页导航 |
| 5 | PN 段落编号 | 全书 `[NNN-PPP]` 赋号 |
| 6 | 基础数据 | 句子库、全文索引 |
| 7 | 类型勘探 | 类型体系确定、图式模板设计 |
| 8 | Butler 准备 | 队列、配置、章节映射、试跑 |
| 9 | 类型 Pilot | 每类型 15 页 pilot，模板收敛 |
| 10 | 总结复盘 | `boot_summary.md`，Butler 实例命名 |

---

## Step 2 — 执行 Boot 循环

### 循环体

```
对 N = 1, 2, 3, ..., 10：
  /boot init phaseN
  /comply BIRTH.md phase N
  /boot phaseN
```

### 循环规则

1. **顺序执行**：Phase N 全部 `[x]` 完成后才能进入 Phase N+1
2. **遇到问题**：一个 Phase 中若发现 BIRTH.spec.md 模板缺陷，提 RFC 后再继续
3. **用户确认**：关键节点（发布配置、语料确认、NNN 次序表等）需用户确认，`/boot` 会自动暂停等待
4. **Phase 0 不需要走此循环**：Step 0（git + corpus）即 Phase 0 的内容

---

## Step 3 — Boot 完成

Phase 10 正常结束后，`local/memory/boot_summary.md` 已写入，Boot 结束宣告已打印。

此时 Wiki 已具备以下能力：

- 章节页面完整，PN 可引用
- 类型体系确定，每种类型有 >= 15 个 standard 页
- Butler 试跑成功，`actions.jsonl` 有记录
- `local/config.md` 包含但不限于：`WIKI_LANG`、`CORPUS_PATH`、`WIKI_NAME`、`PORT`

**进入增长阶段**：

```
$MEMEX_ROOT/GROW.spec.md  # 阅读增长流程规范
```

Boot 完成后的 wiki 处于 GROW Phase 0（基线摸底），执行 GROW 流程前先读 `GROW.spec.md`。

---

## 附：Phase 执行中遇到模板缺陷

在任何 Phase 中发现 `$MEMEX_ROOT/BIRTH.spec.md` 模板描述与实际操作不一致或有改进空间：

1. 在本 wiki `ref/rfc/` 下创建 `rfc-<wiki>-NNNN-slug.md`（status: proposed）
2. `/rfc ref/rfc/rfc-<wiki>-NNNN-slug.md`
3. 继续执行当前 Phase（除非用户明确指示阻塞）

---

*完成后勾选 checkbox，逐 step 推进。*
