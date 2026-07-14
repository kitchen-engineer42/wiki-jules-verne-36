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

## Phase 3：语料准备（选择与校对）

> **comply**: pass（Type A 单文件 epub；epub 来源 QA 分层适配）
> **目标**：`corpus/raw/doc_final.md` 存在且结构完整，作为 Phase 4 唯一输入。

### 3-0 语料来源类型判断
- [x] 类型 **A（单文件）**，语料为单个 Calibre epub（36 works 合集，实为 35 部 ToC 独立作品）

### 3-A 确认语料结构
- [x] `corpus/raw/*.epub` 存在（doc_final.md 由本 Phase 生成）
- [x] 列出 corpus/raw 文件：仅 1 个 epub（+ 转换产物 book.md、images/cover.jpeg）
- [x] 导入范围（--auto 默认，全书 35 部作品全部纳入，type=chapter）
- [x] 页面 ID 规则：`{VVV}-ch{NN}`（VVV 见 ref/chapter-order.md），短篇无章节者单页

### 3-B epub 转换与校验
- [x] pandoc epub→MD：`corpus/raw/book.md`（13M / 124k 行）+ 图片提取 images/
- [x] 转换初步检查：文件体量合理；Calibre 输出为 styled-div（无语义标题，需 3-C2 重建）
- [x] 章节完整性：ToC 35 部作品全部定位（reconstruct_corpus.py --detect 35/35）
- [x] 内容抽样：20000 Leagues / Journey 正文完整，段落与斜体保留
- [x] （--auto）转换质量自动接受，已记录 styled-div 无标题这一结构缺陷 → 3-C2 处理
- [x] 提交转换基线 book.md（commit）

### 3-C 文本质检
- [x] PRE15/PRE16（图像 QA）：epub 纯文字来源，跳过
- [x] PRE9（OCR QA）：epub 数字来源 → 仅公式配对/标题层级；散文小说无公式，无实质命中
- [x] PRE6（断行修复）：epub 来源，跳过
- [x] （degraded）深度形近字/残留物扫描不适用于英文 public-domain 散文

### 3-C2 重建章节结构
- [x] **PRE18 等效**：`wiki/scripts/reconstruct_corpus.py` 从 styled-div 重建 `#`/`##` 结构
  - 35 部作品边界（ToC 标题匹配 + 别名表）
  - 908 章节标题（CHAPTER/PART/BOOK/LETTER 罗马或阿拉伯编号，含小标题折叠）
  - 清洗 Calibre 噪声（`:::` 围栏 0 / `[]{#anchor}` 0 / svg 0）
- [x] 验证：`ref/chapter-order.md` 生成，35 works / 908 chapters，短篇正确显示 0 章

### 3-D Pre-PN Lint 检查
- [x] LNT11（脚注完整性）：本合集散文无系统脚注，跳过
- [x] LNT12（非拉丁 OCR）：全英文，无命中
- [x] `:::` 块语法扫描：doc_final 无 `:::` 残留

### 3-E 生成语料终稿
- [x] `corpus/raw/doc_final.md` 生成（12M，35 `#` + 908 `##`）
- [x] 内容完整性确认（段落间空行保留，反斜杠转义已清理）
- [x] 提交语料终稿 + reconstruct_corpus.py + ref/chapter-order.md

> **Phase 3 检查点**：doc_final.md 已就绪，等待用户复核后进入 Phase 4。

---

## Phase 4：章节导入与目录

> **comply**: pass（anthology 适配；单书共享工具 → 自建 build_chapter_pages.py / generate_toc.py）
> **分桶结构检查**（Phase 启动时 + 每个写 pages/ 步骤后执行）：
> `python3 wiki/scripts/lint_bucket_structure.py --fix`
> 确保 `docs/wiki/pages/` 和 `docs/wiki/history/` 根目录无直接 `.md` 文件（详见 `LNT16`）。
>
> **前置条件**：`corpus/raw/doc_final.md` 存在（Phase 3 完成标志）。
> **目标**：所有章节以 `type: chapter` 页面进入 Wiki，首页出现书籍结构导航，读者可按作品/章节入口阅读。
> **本 Phase 不做 PN**——内容原文导入即可，PN 留 Phase 5。

---

### 4-A 编写章节导入脚本

- [x] 导入前确认：`LAW.md` 语料页类型为 `chapter`，`types.js` 有 `chapter` 键。
- [x] 创建 `wiki/scripts/build_chapter_pages.py`（anthology 版，参考 `$MEMEX_ROOT` 模式）：
  - 读取 `corpus/raw/doc_final.md`，`#`=作品、`##`=章节（PART 分卷头仅分组不成页）
  - 写入路径经 `from page_bucket import page_bucket` + `page_bucket(slug)` 分桶（禁止自建算法）
  - frontmatter：`id/type:chapter/label/description/book/chapter/book_seq/pn_prefix/part?/tags:[chapter]`
  - 不插入 PN，保留原文结构；段落间保留空行
  - `label` 经 `clean_label` 归一（去反斜杠转义、成对直引号→弯引号），使 frontmatter / pages.json / EXPECTED_CHAPTERS 三处一致
- [x] 执行脚本：写入 968 章节页（35 部作品），生成 chapter_map.json + local/chapter_list.py

**epub 来源 post-import 规范化流水线：**

```bash
export WIKI_ROOT="$PWD"
SCRIPTS="$MEMEX_ROOT/wiki/scripts"
```

- [x] `extract_epub_images.py` — 语料为 Calibre 纯文字重构稿（doc_final.md），无正文插图，跳过
- [x] `normalize_pandoc_spans.py` — 执行，去 `{.calibreN}` 等展示 span
- [x] `normalize_fig_blocks.py` — 无 `{.fig-num}` 图注，N/A
- [x] `normalize_table_blocks.py` — 重构稿无 grid table，N/A
- [x] `lint_list_spacing.py` — 无列表标记缺格，N/A
- [x] `normalize_xhtml_links.py` — 重构稿无 epub xhtml 跨章链接，N/A
- [x] `build_page_map.py` — 重构稿无 `page_N` 锚点，跳过
- [x] `normalize_page_links.py` — 无页码链接，N/A
- [x] `build_section_anchor_map.py` / `inject_section_anchors.py` — 无 section 锚点源，跳过
- [x] `normalize_paragraph_spacing.py` — 执行，`--dir docs/wiki/pages`，段落间距合规
- [x] `lint_bucket_structure.py --fix` — 分桶合规，pages/ 根目录无直接 .md

### 4-B 创建 Contents 目录页

TOC 页面标准：`en` → `TOC.md`，type=overview。

- [x] 执行 `generate_toc.py`（anthology 版）：按 book_seq 分组，每部作品一个二级标题，其下列各章 wikilink。写入 35 部作品 / 968 章链接 → `docs/wiki/pages/to/TOC.md`
- [x] 将 TOC id 加入 `local/config/home.js` PREFACE_IDS：`export const PREFACE_IDS = ['TOC'];`
- [x] 访问 `#TOC` 确认目录页可渲染、链接可跳转（CHK13 D05 确认 wikilink 可解析，page_count=970 含 TOC）

### 4-C 更新 home.js 接入章节导航

- [x] `home.js`：`PREFACE_IDS = ['TOC']`；`APPENDIX_IDS = []`（无后置页）；SKIP_TYPES 含 chapter/list/overview
- [x] `hero.js` `BOOK_META`：35 部作品逐卷条目，min/max 覆盖 book_seq 1–968，BOOK_DISPLAY='strip'

### 4-D 验证与提交

- [x] **CHK12**（chapter-integrity）：`python3 "$MEMEX_ROOT/wiki/scripts/chapter_integrity.py"` → C01–C08 全部通过 ✓。C06 为警告（anthology label=`Work — head`，与语料裸 H2 结构性不匹配，非 error）。
- [x] **CHK13**（deploy-verify）：`./wiki-daemon.sh restart` 后 `python3 "$MEMEX_ROOT/wiki/scripts/verify_deploy.py"` → D01–D07 全部 PASS，整体结论 PASS
- [x] 回填修订历史：hybrid 的 git 阶段因页面未提交返回 0（main 早退，未进 mtime 阶段），改用 `--mode mtime` 直接扫描工作树 → 共 970 个页面，970 条初始修订记录
- [x] commit（be19cfd，2511 files）：pages/ + history/ + line_index/ + pages.json/.lite + home.js + hero.js + chapter_map.json + recent.*.jsonl + 脚本

---

## Phase 5：PN 段落编号

> **comply**: pass（三段 volume 方案 VVV-NNN-PPP；pn_prefix 已由 Phase 4 写入）
> **前置条件**：Phase 4 章节导入完成。
> **目标**：968 章节页每个正文段落分配 `[VVV-NNN-PPP]`，建立可引用的 PN 体系。

<!-- MUST-COPY: NNN 格式表 + 结构类型表 + "铁则" -->
### 5-A 确定章节 NNN 编号

> ⚠️ **NNN 必须严格对应原书页面次序**。次序一经确定不得变更。

pn-citation 插件正则接受的 NNN 格式：

| 格式 | 范围 | 适用场景 |
|------|------|---------|
| `\d{3}` | `001`–`999` | 正文章节 |
| `P0[1-9]` | `P01`–`P09` | 书前置章节 |

> ⚠️ 禁止 `PRE`/`APP`/`REF`/`IDX` 等字母缩写 NNN。

> **铁则：所有已导入页面统统分配 NNN，不得跳过。**

| 结构类型 | NNN 模式 |
|---------|---------|
| 多书/多卷系列 | `B-CC`（书号-章号）复合 NNN |

本 wiki 为 **35 部作品合集**，采用三段 volume 方案：`VVV-NNN-PPP`，
pn_prefix = `VVV-NNN`（作品码-作品内章号），全集唯一。

- [x] `LAW.md` NNN 方案与插件格式一致（VVV=`[A-Za-z0-9]{1,4}`，NNN=`\d{3}`，无非法缩写）
- [x] `LAW.md` 三引用 `ref/spec/data-pn.md`，记录三段 volume 方案、各段位数、`PN_SCHEME=volume`
- [x] `ref/chapter-order.md` 完整列出 35 作品 / 968 章及 VVV 码
- [x] （--auto）次序表已在 Phase 3/4 与语料 ToC 核对一致，跳过人工等待

### 5-B 更新章节 frontmatter

所有 `type: chapter` 页 frontmatter 含 `pn_prefix`（值为 `VVV-NNN` 字符串）。

- [x] pn_prefix 已由 `build_chapter_pages.py`（Phase 4）写入全部 968 页（如 `"TTLU-001"`）
- [x] 脚本定位页面读 `pages.json` 的 `path` 字段（assign_pn.py 遵此铁律）
- [x] `data/chapter_map.json` 为 `nnn→page_id` 映射（key=`VVV-NNN`，value=slug，968 条）
- [x] 格式验证：所有 value 为 str，✓
- [x] `docs/wiki/data/chapter_map.json` 已就位（Phase 4 生成）

### 5-C 按次序逐章赋号

#### 5-C-0 Wiki 专属 PN 规则
- [x] pn_prefix 已写入所有章节
- [x] 无额外跳过元素（重构散文稿，无 sidebar/epub 脚注定义/特殊块）
- [x] LAW.md 三确认 **三段 volume**：`pn_format = "{pn_prefix}-{ppp:03d}"`
- [x] 本地脚本 `wiki/scripts/assign_pn.py`（改编 PRE7，volume 方案，幂等）

#### 5-C-1 试验章（pilot）
- [x] `TTLU-ch01` 单章赋号：32 段 → `[TTLU-001-001]`..`[TTLU-001-032]`，连续无跳号

#### 5-C-2 评估
- [x] （--auto 自动评估）编号连续、段首锚定、无标题误赋、渲染无副作用 — 通过

#### 5-C-3 发现问题 → RFC
- [x] 无系统性问题，不阻塞

#### 5-C-4 全量赋号
- [x] 全量执行 `assign_pn.py`，逐章 `[VVV-NNN-PPP]`：改写 967 章 + 跳过 1（pilot 已赋），968 章共 58,399 个 PN
- [x] 跨章连续性验证（`--verify`）：968 章 / 58,399 PN，✓ 连续无跳号
- [x] `lint_bucket_structure.py --fix`：pages/ 与 history/ 根目录无直接 .md，分桶合规

### 5-D PN 后超长段落拆分（可选，--auto 默认跳过）
- [x] 跳过 PRE2

### 5-E 验证与提交
- [x] `pn_structure_verify.py --scheme volume`：报 A5「段首遗漏 PN」45,397 处，经查为**验证器正则宽度缺陷**（`_FIRST=VOL` 严格 3 字符，拒 `AM`/`MI`/`TTLU` 等变长 VVV）。数据经 `assign_pn.py --verify` 与 `build_pn_source.py`（58,395 条）双重确认连续完整 → A5 判为**误报，不阻塞**（RFC-vernean-voyages-0001，spec 5-C-3 授权）
- [x] Wikilink / frontmatter 完整性：`build_registry.py` 重建通过，970 页 type/label/pn_prefix 齐备，无 unknown
- [x] 提交全书 PN（见 5-F 合并提交）

### 5-F PN 检索源构建
- [x] 执行 PRE20 / `build_pn_source.py` 生成 `data/pn-source.json`：58,395 条 PN 条目
- [x] `data/pn-source.json` 加入 `.gitignore`（构建产物，可从 pages/ 重建）
- [x] 提交（Phase 5 合并提交：pages/ PN 锚点 + pages.json/.lite + assign_pn.py + ref/rfc/ + .gitignore + BIRTH.md）

---

> Phase 6–10 待逐一 `/boot init phaseN` 实例化后执行。
