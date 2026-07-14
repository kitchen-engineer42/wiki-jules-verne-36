# Vernean Voyages Wiki — 启动流程 (BIRTH)

> 本文件由 `/boot` 从 `$MEMEX_ROOT/BIRTH.spec.md` 逐 Phase 实例化。
> 阅读顺序：CONSTITUTION.md → LAW.md → 本文档。

## Wiki 基本信息

| 字段 | 值 |
|------|-----|
| WIKI_NAME | Vernean Voyages Wiki |
| WIKI_LANG | en |
| PORT | 1828（Jules Verne 生于 1828）|
| DEPLOY_TARGET | cloudflare |
| CDN_BASE | https://baojie.github.io/memex/dist |
| PYTHON_ENV | system（python3）|
| 语料来源 | The Collected Works of Jules Verne (36 Novels and Short Stories) — Jules Verne (epub) |
| CORPUS_PATH | corpus/raw/ |

---

## Phase 0：前置决策与基础文件

> **comply**: pass（Phase 0 由 EGG + 本次 boot 实执行，非模板占位）

### 0-0 Bootstrap
- [x] 共享 skills 已全局链接到 `~/.claude/skills/`（`init_skills.sh` 已生效，21 个 skill 可用）

### 0-A 两个前置决策
- [x] **WIKI_LANG**：`en`（English）→ 写入 `local/config.md`
- [x] **TIMEZONE**：`Europe/Paris`（Verne 为法国人，Nantes）→ 写入 `local/config.md`
- [x] **验证工具链**：`$MEMEX_ROOT=/Users/mac/memex` 有效；独立 git 仓库已建（EGG，隔离于 memex 工作树）
- [x] **PYTHON_ENV**：`system`（python3 3.12.7 全局可用，无 pyproject）；`PYTHON_BIN=python3`、`PIP_CMD=pip3`

### 0-B 基础文件
- [x] `README.md`（从 README.spec.md 复制并填写）
- [x] `CHANGELOG.md`（初始化首条记录 2026-07-13）
- [x] `CLAUDE.md`（从 CLAUDE.spec.md 复制，填 Wiki Name、初拟页面类型）
- [x] `.gitignore`（从 .gitignore.example，含 MUST-TRACK 检查；public-domain → 不排除 corpus/raw）
- [x] `LAW.md`（三段 PN volume 方案、英文 slug、页面类型、public-domain 语料声明）
- [x] 目录结构（corpus/ docs/ ref/ logs/ data/ local/ wiki/scripts/）
- [x] `docs` submodule 初始化 —— **跳过**：DEPLOY_TARGET=cloudflare，docs/ 为普通目录，无需 submodule
- [x] `local/gene/_context.md`（butler 执行上下文：语言、PN、类型、质量档位）

### 0-C 安全初始化
- [x] `init_security.py .` 生成 `.claude/settings.json`（deny 25 条 / allow 16→21 条 + PreToolUse hook）
- [x] deny 含精确 memex 写操作拦截（`cp/mv/rm *memex*`、重定向、python open 'w'/'a'）
- [x] allow 含 git 只读、registry 构建、publish、butler、memex 共享脚本调用
- [x] Skill commit 门控：deny `git commit*`；allow `skill_commit.sh`/`wiki_commit.sh`；已复制三个包装脚本
- [x] 承诺规则：CONSTITUTION §1.3 生效——禁止对 `$MEMEX_ROOT` 任何直接写操作
- [x] /tmp 读写默认放行（restrict_to_project.py 白名单）

### 0-D 发布配置
- [x] `DEPLOY_TARGET=cloudflare` 记录到 `local/config.md`
- [x] 方案 C：docs/wiki 为普通目录；`wiki/scripts/publish.sh` wrapper（委托 memex 管道，无 --push）
- [x] Cloudflare Pages 控制台接入 —— **延后**（external，需 GitHub 远端仓库先建立）
- [x] 根目录 `publish.sh` 快捷方式已创建且可执行（`test -x publish.sh` 通过）

### 0-E 初始提交
- [x] 提交 Phase 0 建立的所有基础文件（commit 2655e8d）

---

## Phase 1：引擎接通

> **目标**：Phase 1 结束后，`./wiki-daemon.sh start` 即可在浏览器打开一个可启动的 Wiki（页面可空白/报错，但进程不崩溃）。
> 本地不新增引擎代码，所有 JS/CSS 由 serve.js 从 `$MEMEX_ROOT/wiki/public/` 回退提供。本 Phase 全为机械操作。

### 1-A 确认本地调试端口
- [x] 查阅 `$MEMEX_ROOT/ref/spec/sys-ports.md`（只读）
- [x] 推荐端口 `1828`（Verne 生年），已确认
- [x] `PORT=1828` 写入 `local/config.md`
- [x] 端口登记到 memex 中央表 —— 走 `/rfc` 流程（--auto 下延后，见跳过汇总）

### 1-A2 确认引擎 CDN 来源
- [x] 选项 A（默认）：`https://baojie.github.io/memex/dist`
- [x] `CDN_BASE` 写入 `local/config.md`

### 1-B 建立 docs/ 结构
- [x] `docs/index.html`（重定向到 wiki/）
- [x] `docs/.nojekyll`
- [x] `docs/wiki/` 目录（index.html + pages/ + local/ + images/，不建 js/css/）
- [x] `docs/wiki/index.html`（从 index.html.template 复制，替换 Wiki Name / Footer / cdn-base / favicon）
- [x] 内联 SVG favicon（PRIMARY_COLOR=a02128，首字母 V）
- [x] 验证 index.html JS/CSS 路径未偏离模板（css/main.css、js/core.js）

### 1-C 适配 wiki-daemon.sh
- [x] 从 `wiki-daemon.sh.example` 复制，改 WIKI_NAME/PORT/PUBLIC_DIR/ENGINE_DIR
- [x] `chmod +x wiki-daemon.sh`
- [x] 更新 README.md 加入端口/启动方式

### 1-D 确认共享脚本可用
- [x] `$MEMEX_ROOT/wiki/scripts/page_utils.py` 存在（通过 WIKI_ROOT 调用，无需复制）

### 1-E 引擎接通提交
- [x] 提交 Phase 1 文件（docs/ + wiki-daemon.sh）

---

## Phase 2：Wiki 配置

> **comply**: pass（en 变体实例化，占位符已填，PCF1–5 通过）
> **目标**：Phase 2 结束后，空 Wiki 完整可用：页面正常渲染，About 页可访问，控制台无报错。

### 2-A 本地 JS 配置文件初始化
- [x] `docs/wiki/local/LocalSettings.js`（wgSiteName='Vernean Voyages Wiki'；启用非 core 无配置插件 autolink/pn-citation/footnote/backlinks/sealso/want-button/math/math-array/page-marker/export + optional semantic-block/semantic-query；地图插件保持注释）
- [x] `docs/wiki/local/config/i18n.config.js`（`defaultLang = 'en'`，required 插件）
- [x] `docs/wiki/local/config/chapter.config.js`（`TOC_PAGE_ID = 'TOC'`）
- [x] `docs/wiki/local/config/types.js`（9 类型 en 标签，依 LAW.md：chapter/character/place/technology/event/work/organization/overview/list）
- [x] `docs/wiki/local/config/infobox.js`（FIELD_LABELS/INFOBOX_SKIP/FIELD_GROUPS，en）
- [x] `docs/wiki/local/config/hero.js`（EYEBROW/TITLE/TAGLINE/DOC_TITLE，BOOK_DISPLAY='strip'，BOOK_META 占位待 Phase 4/5 补全）
- [x] `docs/wiki/local/config/home.js`（HOME_SECTIONS：Characters/Places/Technology；SKIP_TYPES）
- [x] `docs/wiki/local/config/variables.js`（AUTHOR=Jules Verne 等）
- [x] `docs/wiki/local/config/event-linkify.config.js`（required：LINKIFY_FIELDS，en）
- [x] required 插件核查：`i18n`、`event-linkify` 均已建配置；optional semantic-block/query 用默认值

### 2-B 使用 NEW1 创建 About 页面
- [x] `add_page.py About`（type=overview，label='About This Wiki'，含 Source Material / Usage Notes / Copyright），写入 `pages/ab/About.md`，注册表已重建

### 2-C-1 local.css 主题配色
- [x] 列出 50 套主题，选定 **55 纸质书亮色（paper-light）**，与 Hetzel 深红 favicon 协调
- [x] 应用主题（`local.css`，原占位备份为 `local.css.bak`）
- [x] 确认页面配色正常渲染

### 2-C-2 Hero 视觉设计
- [x] 视觉隐喻：古董航海图上沿正弦航线漂移的深红光点（凡尔纳"非凡旅行"）
- [x] 实现 `docs/wiki/local/config/hero.config.js`（`buildHeroBackground()` 返回 `<canvas class="hero-cosmos">`，`startHeroAnimation()` 注册清理）
- [x] 本地验证：Hero 背景与 paper-light 主题协调，无报错

### 2-D 验证
- [x] `./wiki-daemon.sh start`，访问 `http://localhost:1828`
- [x] 页面正常渲染（空 Wiki，无报错）
- [x] About 页正常显示（topnav → About）
- [x] 关键资产 + 配置文件均 HTTP 200，无非预期 404
- [x] local.css 加载正常，配色正确

### 2-E Wiki 配置提交
- [x] 提交 Phase 2 配置文件 + About 页 + 注册表

---

> Phase 3–10 待逐一 `/boot init phaseN` 实例化后执行。
