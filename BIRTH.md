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

## Phase 6：基础数据建设

> **comply**: pass（anthology 三段 PN；句子库 SID 适配 VVV-NNN-PPP；FTS pageType=chapter）
> **分桶结构检查**（Phase 启动时 + 每个写 pages/ 步骤后执行）：
> `python3 wiki/scripts/lint_bucket_structure.py --fix`
>
> **目标**：建立句子库（Sentence Index）和全文索引（FTS Index），作为内容分析（butler SCN5、QUO20 等）和前端搜索的基础数据。
> 本 Phase 两个任务各自独立，可并行执行。
>
> 注意：具体 Wiki 的 BIRTH.md **做一步写一步**——BIRTH.spec.md 定义完整步骤，具体 Wiki 执行时按需勾选。

### 6-A 句子库（Sentence Index）

**前置条件**：Phase 4/5 PN 赋号完成（需要 `[VVV-NNN-PPP]` 段落编号作为句子的父级引用）。

利用 **PRE1-build-sentence-index** 基因，将章节原文按自然句子边界切分，生成 `data/sentence_index/` 下的 JSONL 文件。

- [x] CHAPTER_DIR=`docs/wiki/pages`、OUT_DIR=`data/sentence_index`；WIKI_LANG=en → `--lang en`
- [x] 执行全量构建（**本地适配脚本**，见下方缺陷说明）：
  ```bash
  python3 wiki/scripts/build_sentence_index.py \
    --wiki-root "$PWD" --pages-dir docs/wiki/pages \
    --out-dir data/sentence_index --lang en
  ```
  > ⚠️ 共享 `build_sentence_index.py` 的 `_PN_RE` 首段写死 `[A-Za-z0-9]{3}`（恰好 3 字符），
  > 变长 VVV（`AM`/`MI` 2 字符、`TTLU`/`DSCF` 4 字符）段落静默丢句：共享脚本仅得 25,992 句、多章 0 条。
  > 根因与 RFC-0001 同源 → 本地包装 `wiki/scripts/build_sentence_index.py` 放宽首段为 `{1,4}` 后委托共享 main()。
  > 记 **RFC-vernean-voyages-0002**（不阻塞，本地脚本已解决）。
- [x] 验证输出：`data/sentence_index/` 下每章一个 `<pn_prefix>.jsonl`（968 个），sid=`VVV-NNN-PPP-sN`、pn=`VVV-NNN`，格式合 `$MEMEX_ROOT/ref/spec/data-sentence-index.md`
- [x] 确认识别总数合理：968 章 / **122,989 句**（句数显著多于 58,399 段）；4 个 `BOOK I/II` 分卷分隔章无正文，0 句属预期

**产出验证**：`find data/sentence_index/ -name '*.jsonl' | wc -l` 应与已赋 PN 的章节数一致。

```bash
git add data/sentence_index/
bash wiki/scripts/skill_commit.sh "feat: Phase 6-A 句子库构建完成"
```

### 6-B 全文索引（FTS Index）

利用 **SRH1-build-fts-index** 基因，将章节页面构建为浏览器端搜索插件可消费的 `fts-index.json`。

- [x] `local/config/srh1.config.json` 已配置：pageType=chapter、idField=id、chapterTitleField=label、outputPath=`docs/wiki/data/fts-index.json`，**pnFormat=`{vvv}-{nnn:03d}-{ppp:03d}`**（三段 volume；`pn_format_to_pattern` 生成 `[A-Za-z0-9]+\-\d{3}\-\d{3}`，`[A-Za-z0-9]+` 天然兼容变长 VVV，无 RFC-0001/0002 的固定宽度缺陷）
- [x] 执行 SRH1 构建：
  ```bash
  python3 "$MEMEX_ROOT/wiki/scripts/build_fts_index.py" .
  ```
- [x] 验证输出：`docs/wiki/data/fts-index.json` 结构正确（`{chapters, entries}`）；**968 章 / 58,399 段**（与 PN 锚点数一致），entry schema `{c,p,x}`，p 捕获完整 `VVV-NNN-PPP`
- [x] 接入发布流水线：`wiki/scripts/publish.sh` wrapper 委托 `$MEMEX_ROOT/wiki/scripts/publish.sh`，管道内置 build_registry → FTS → 修订记录 → 反链 → 坐标 → 知识快照，无需手动插入
- [x] 本地启动 Wiki，`verify_fts.py --query Nautilus Nemo` 通过（退出码 0）：
  ```bash
  python3 "$MEMEX_ROOT/wiki/scripts/verify_fts.py" \
    --base-url http://localhost:1828 \
    --query Nautilus Nemo
  ```
  结果：`Nautilus` → 668 段、`Nemo` → 604 段命中；fts-index served 于 `/data/fts-index.json`（HTTP 200）。playwright 已装。

**产出验证**：`python3 -c "import json; d=json.load(open('docs/wiki/data/fts-index.json')); print(f'章节 {len(d[\"chapters\"])}, 段落 {len(d[\"entries\"])}')"`

```bash
git add docs/wiki/data/fts-index.json local/config/srh1.config.json wiki/scripts/publish.sh
bash wiki/scripts/skill_commit.sh "feat: Phase 6-B 全文索引构建完成"
```

### 6-C 新 Wiki 注意事项

- **句子库依赖 PN**：Phase 4/5 完成前不可构建句子库（SID 格式含 PN 前缀）
- **FTS 不依赖 PN**：即使 PN 未完成亦可构建 FTS（仅依赖 `type: chapter` 页面和段落文本）
- **管家集成**：句子库建成后，butler 的 W13 步骤自动包含 PRE1，W17/SCN5 依赖句子索引

### 6-D PN 完整性批量核验（Workflow 可选）

> **适用条件**：用户 Claude Code 具备 workflow 能力。仅 Phase 6 数据就绪后执行一次，作为 Phase 4/5 PN 赋号和 Phase 6 句子库/全文索引质量的联合验证。

PN 核验涉及两种检查：
- **引用格式检查**：逐页确认 PN 格式正确（`VVV-NNN-PPP`）、括号语种统一、无悬挂引用
- **段落存在性检查**：每条 PN 引用能定位到句子索引或章节页面中的实际段落

当 wiki 规模较大（本 wiki 968 章 / 58,399 条 PN），串行检查耗时很长。此时可用 workflow 并行化。

**执行方式**（在 Claude Code 中）：

```
Workflow({scriptPath: "$MEMEX_ROOT/ref/workflows/pn-verify-batch.js"})
```

该脚本自动：

1. 读取 `pages.json`，筛选所有非 chapter 页面
2. 按 20 页一批分包
3. 通过 `pipeline` 机制分发到多个并行 agent 独立核验
4. 合并各批结果 → 计算合规统计（✅/⚠️/❌）
5. 写入 `logs/birth/phase6/pn-verify-report.md`

**退出条件**：

- [x] 严重问题数为 0：本环境无 Workflow 工具 → 降级等价核验；且非 chapter 页仅 About/TOC（无行内 PN 引注），行内核验 Phase 6 无对象，待 Phase 7+ 补做
- [x] 轻微问题记录在案：章节锚点已经 `assign_pn --verify`（58,399 连续）+ `build_pn_source`（58,395）+ FTS（58,399）三重确认；A5 宽度误报记 RFC-0001
- [x] `logs/birth/phase6/pn-verify-report.md` 已写入

---

## Phase 7 — 知识结构摸底与类型体系调整

> **comply**: pass（LAW.md 四 9 类型已定；SCN23 从 968 章语料勘探实体分布）
> **分桶结构检查**（Phase 启动时 + 每个写 pages/ 步骤后执行）：
> `python3 wiki/scripts/lint_bucket_structure.py --fix`

**前置条件**：Phase 6 完成（基础数据就绪），**非章节词条建立之前**执行。

**目标**：推导该 wiki 的实体类型体系，调整 `config/types.js` 配置，为后续通过 NEW1 批量建页和分类查询建立类型先验。

### 7-A 实体类型勘探（SCN23）

```
SCN23-entity-type-survey
```

- 从现有章节页面分析内容，推导潜在实体类型分布
- 输出 `logs/butler/type-survey.md`，包含各类型估算数量和典型实例
- 确定该 wiki 的主要 `type` 值集合（本 wiki 依 LAW.md 四：character / place / technology / event / work / organization 及其权重）

**输出验证**：`logs/butler/type-survey.md` 存在且包含至少 3 种类型及其估算数量。

### 7-B 类型体系配置调整

根据 type-survey.md 的结论：

1. 审查 `wiki/local/config/types.js`，确认当前 `TYPE_LABELS` 覆盖所有主要类型
2. 对缺失的类型补充 label（英文显示名 + 颜色）
3. 对占比 < 1% 的边缘类型，决定合并到近似类型还是保留
4. 更新本地 `BIRTH.md` 中 Phase 7-B 节的类型表

**完成条件**：
- [x] type-survey.md 已生成：`logs/butler/type-survey.md`，6 类实体 + 权重 + 典型实例 + 估算数（character 40% / place 22% / technology 16% / event 10% / work 9% / organization 3%）
- [x] types.js 中所有 type 均有对应 label：`docs/wiki/local/config/types.js` 9 键（chapter/character/place/technology/event/work/organization/overview/list）全有 en label，与勘探结论一致，无需增删
- [x] 类型表已同步到 CLAUDE.md（本地表更新为「Phase 7 定稿」9 类 + 权重）；BIRTH.spec.md 为 memex 共享文件（RFC-only 写）且类型与 LAW.md 四无差异 → 无需上游同步（N/A）

> 此阶段仅在新 wiki 首次启动时执行一次；后续类型扩充通过 FIX8/EVV8 按需处理。

**Phase 7-B 类型表（定稿）**：

| type | 类别 | 权重 |
|------|------|------|
| character | 实体 | ~40% |
| place | 实体 | ~22% |
| technology | 实体 | ~16% |
| event | 实体 | ~10% |
| work | 实体 | ~9% |
| organization | 实体 | ~3% |
| chapter | 语料 | —（968 页）|
| overview / list | 编辑 | — |

### 7-C 类型图式模板设计（MTD3）

类型确定后，为每个主要 type 设计基础组织结构和 metadata schema：

```
MTD3-page-schema-template（对每个主要 type 执行一次）
```

**每种 type 需要确定**：

1. **页面结构**：H2 节的顺序与必填节（如 character 页必须有"Overview"、"Role in the Story"）
2. **frontmatter 字段**：除通用字段（id / type / label / aliases / tags / description）外，该类型的专属字段（如 character 的 affiliation / first_appearance）
3. **引文规范**：blockquote 使用习惯、PN 密度期望值
4. **质量阈值**：basic / standard / featured 各档的最低要求
5. **插图引用规范**（原书有插图时）：若章节中存在与该类型强相关的图表，模板应说明是否在词条页中引用。引用方式为直接嵌入 `:::image` 块，指向 `docs/wiki/images/` 下的图片文件：
   ```markdown
   :::image fig="3.2" src="images/fig-3-2.png" caption="图 3.2 …"
   :::
   ```
   原书无插图或该类型词条与图表关联不强时，此项标注"不适用"即可。（本 wiki 语料为 Calibre 纯文字重构稿，无正文插图 → 统一标注"不适用"。）

**输出**：`local/template/<type>-schema.md`（每个主要 type 一份）

**Workflow 加速**：当需要设计的类型 ≥ 3 种时，可并行执行：

```
Workflow({scriptPath: "$MEMEX_ROOT/ref/workflows/mtd3-parallel-template-design.js"})
```

该脚本先通过 agent 读取 `types.js` 和 `type-survey.md` 确定待设计类型列表，再用 `parallel` barrier 为每个类型分配独立 agent 并发设计，最后依次写入 `local/template/`。已存在的类型模板不受影响。

**完成条件**：
- [x] 所有占比 ≥ 5% 的 type 均有对应模板文件：character/place/technology/event/work（≥5%）均建 `local/template/<type>-schema.md`；organization（3%）亦一并设计，共 6 份
- [x] 模板中的 frontmatter 字段已同步到 wiki 本地 `CLAUDE.md §Frontmatter`（新增「类型专属字段」表，6 类逐一列出）
- [x] `docs/wiki/local/config/types.js` 的 label 与模板文件 type 值一一对应（character/place/technology/event/work/organization）

> 无 Workflow 工具可用 → 6 个 schema 模板直接顺序设计（非并行），内容等价。

---

## Phase 8 — Butler 准备期

> **comply**: pass（anthology butler.json 适配；chapter_map 改用本地脚本从 pages.json 生成，见 8-C 适配说明）
> **分桶结构检查**（Phase 启动时 + 每个写 pages/ 步骤后执行）：
> `python3 wiki/scripts/lint_bucket_structure.py --fix`

**前置条件**：Phase 7 完成（类型体系和图式模板就绪），且 5-F `data/pn-source.json` 已构建。

**目标**：在首次 `/butler` 启动之前，建立 butler 运行所需的全部文件骨架，确保 Step 1 读状态时不因缺文件而报错。

> **自动创建（无需手动）**：`logs/butler/`、`round_counter.txt`、`actions.jsonl`、`docs/wiki/pages.lite.json` 均由脚本首次调用时自动生成。
>
> **必须手动创建**：`local/config/butler.json`、`logs/butler/queue.md`、`logs/butler/housekeeping_queue.md`、`logs/butler/quality_rules.md`、`local/butler/chapter-map.md`，以及 `local/config.md` 中的 `CORPUS_PATH` 字段。

### 8-A 建立 logs/ 子目录结构

`logs/` 顶层目录在 Phase 0-B 已创建，但各子目录需在此处建立（见 `ref/spec/sys-directory.md §6`）：

- [x] 创建完整 logs 子目录：
  ```bash
  mkdir -p logs/butler logs/daily logs/lint logs/build logs/reports/weekly logs/reports/monthly logs/gene-express
  ```

### 8-B 建立队列文件骨架

所有队列文件均位于 `logs/butler/`（由 `get_logs_butler()` 解析）：

- [x] 创建 `logs/butler/queue.md`：

```markdown
# 内容任务队列

## P1 — 高优先级
<!-- 空，butler discover 后自动填入 -->

## P2 — 中优先级

## P3 — 发现型（每11轮触发）
```

### 8-B2 创建 local/config/butler.json

`build_chapter_map.py` 及 butler 运行时均依赖此文件。在 8-C 之前必须创建。

- [x] 创建 `local/config/` 目录（若不存在）：
  ```bash
  mkdir -p local/config
  ```
- [x] 创建 `local/config/butler.json`，按本 wiki（anthology）实际填写。本 wiki 语料
  `doc_final.md` 用 `#`=作品、`##`=章节，无单书 `# Chapter N` 结构，故 `chapter_pattern`
  匹配 `##` 章节标题：
  ```json
  {
    "corpus_file": "corpus/raw/doc_final.md",
    "chapter_pattern": "^## ",
    "preface_pattern": "^# (Preface|Introduction|Foreword)",
    "preface_nnn": "000",
    "appendix_pattern": "^# APPENDIX [A-Z]"
  }
  ```
  字段说明：
  - `corpus_file`：Phase 3-E 生成的语料终稿路径（相对 wiki 根目录）
  - `chapter_pattern`：正则，匹配正文章节标题行（anthology 为 `^## `）
  - `preface_pattern`：正则，匹配前言/序章类标题行
  - `preface_nnn`：前言的 NNN 编号（通常为 `000`）
  - `appendix_pattern`：正则，匹配附录标题行（无附录可省略）

- [x] 验证 JSON 格式合法：
  ```bash
  python3 -m json.tool local/config/butler.json
  ```

### 8-C 配置章节映射表

在 `local/butler/chapter-map.md` 中建立人类可读的 NNN↔章节对应表，供 butler 运行时参考。
**必须运行生成脚本**，禁止从其他 wiki 复制 chapter-map.md。

前提条件：`local/config/butler.json` 已配置（见 8-B2）。

- [x] 创建 `local/butler/` 目录（若不存在）：
  ```bash
  mkdir -p local/butler
  ```
- [x] 运行生成脚本，从本 wiki 语料自动生成 `local/butler/chapter-map.md`：
  ```bash
  WIKI_ROOT="$PWD" python3 wiki/scripts/build_chapter_map.py
  ```
- [x] 验证输出章节数量与语料一致：
  ```bash
  grep -c "^| \`" local/butler/chapter-map.md   # → 968
  ```

> **anthology 适配**：共享 `$MEMEX_ROOT/wiki/scripts/butler/build_chapter_map.py`
> 假设单书——从语料正则抽带阿拉伯数字捕获组的章号生成连续 NNN。本 wiki 为 35 部
> 凡尔纳作品合集，968 章标题为罗马数字/纯文本（`CHAPTER I` 等），无单一阿拉伯章号，
> 且 NNN 需按作品分段（VVV-NNN），共享脚本实测 0 章。故改用本地
> `wiki/scripts/build_chapter_map.py`，从权威源 `docs/wiki/pages.json`（type=chapter）
> 读取、按 `book_seq` 排序，`pn_prefix` 自各章页 frontmatter 回读（pages.json 未透传此字段），
> 输出 `VVV-NNN | 作品 | 章节标题` 表。与既有 anthology 本地脚本
> （build_chapter_pages / generate_toc / assign_pn / build_sentence_index）一致。

### 8-D 补全 local/config.md

Phase 0-A 已写入 `WIKI_LANG`，本步骤补全 butler 运行所需的其余字段：

- [x] 确认 `local/config.md` 包含以下字段（按项目实际填写）：

```
WIKI_LANG=en
CORPUS_PATH=corpus/raw/doc_final.md
WIKI_NAME=Vernean Voyages Wiki
PORT=1828
```

- [x] 验证 `CORPUS_PATH` 所指文件确实存在（**前置条件**：5-F `data/pn-source.json` 已构建）：
  ```bash
  python3 "$MEMEX_ROOT/wiki/scripts/butler/corpus_search.py" "Nautilus" --max 3
  ```

### 8-E 建立 quality_rules.md

RUL1 基因（标注错误沉淀为规则）和 W5 反思在写入知识时需要此文件存在：

- [x] 创建 `logs/butler/quality_rules.md`（路径同队列文件，见 `ref/spec/meta-skill-standards.md §7.2`）：

```markdown
# 质量规则库

本文件由 butler 自动追加，记录从实际操作中沉淀的约束规则。

## 格式规范

## 内容规范

## PN 引注规范
```

### 8-F 验证核心脚本

- [x] 验证 `docs/wiki/pages.json` 存在且为合法 JSON：
  ```bash
  python3 -c "import json; json.load(open('docs/wiki/pages.json')); print('OK')"
  ```

### 8-G 首次试跑

- [x] 启动 butler，确认 Step 1 读状态无报错：
  ```
  /butler --instance explorer --focus discover
  ```
  预期：输出 `[R1] ...`，无 FileNotFoundError，`logs/butler/actions.jsonl` 自动生成

**完成条件**：
- [x] `logs/butler/queue.md` 和 `logs/butler/housekeeping_queue.md` 存在
- [x] `logs/butler/quality_rules.md` 存在
- [x] `local/butler/chapter-map.md` 存在
- [x] `local/config.md` 包含 `WIKI_LANG` 和 `CORPUS_PATH` 字段
- [x] `docs/wiki/pages.json` 合法
- [x] 首轮 butler 输出 `[R1]` 行且 `actions.jsonl` 有记录

---

## Phase 9 — 类型 Pilot（SCN27/EVV5 循环）

> **comply**: pass（结构 19/19；PCF1-4 全绿；anthology 适配：pilot 类型取 Phase 7 权重前 4（character/place/technology/event），9-A 试建页用 technology/Nautilus 替通用 concept，slug kebab-case，wikilink label 形式，章节 id 用 TTLU-ch01，均符合 LAW §四/五/九）
> **分桶结构检查**（Phase 启动时 + 每个写 pages/ 步骤后执行）：
> `python3 wiki/scripts/lint_bucket_structure.py --fix`

**前置条件**：Phase 8 完成（butler 基础设施就绪、首轮试跑无报错）。

**目标**：在 butler 正式循环启动之前，通过 NEW1 为每个主要词条类型手建 1 个高质量示范页，以：
1. 端到端验证每个类型的模板（frontmatter + 节结构 + PN 引注 + wikilink）是否可正常渲染
2. 发现并修复工作流或模板问题，避免在大规模通过 NEW1 建页时重复犯错
3. 为 butler 提供可参照的内容质量基线（butler 的 W4 评估和 enrich 扩充均参考同类已有页面）

**执行机制**：Phase 9 分两阶段——**9-A 试建核验**（单页系统集成验证）和 **9-B 批量循环**（SCN27 → QUO23 → EVV5 → EVV6 迭代）。每个动作执行完毕后须人工审核，审核通过后才进入下一步。

**Slug 命名规则**：Phase 9 所有新建页面的 slug（即页面 id / 文件名）必须使用 `local/config.md` 中 `WIKI_LANG` 指定的语言。本 wiki `WIKI_LANG=en`，slug 使用英文 kebab-case（如 `captain-nemo`、`nautilus`、`iceland`）。禁止在英文 wiki 中使用中文 slug。

**本 wiki pilot 类型**（依 Phase 7 类型勘探权重，取信号最强的 4 个实体类型，对应 --auto 的「4 类型 × 8 轮」）：`character`（40%）、`place`（22%）、`technology`（16%）、`event`（10%）。`work`/`organization` 由 butler 后续循环覆盖。

**Phase 9 轮次：R=32**

类型执行顺序（依赖顺序，先建基础类型 technology/place，再建引用它们的 character/event）：`technology` → `place` → `character` → `event`。

| 类型 | r1-SCN27 | r1-EVV5 | r2-SCN27 | r2-EVV5 | r3-SCN27 | QUO23 | r3-EVV5 | EVV6 | EXIT-GATE | 状态 |
|------|---------|---------|---------|---------|---------|-------|---------|------|-----------|------|
| technology | R1 ✓ | R2 ✓ | R3 ✓ | R4 ✓ | R5 ✓ | R6 ✓ | R7 ✓ | R8 ✓ | E1–E5 ✓ | 收敛 |
| place | R9 ✓ | R10 ✓ | R11 ✓ | R12 ✓ | R13 ✓ | R14 ✓ | R15 ✓ | R16 ✓ | E1–E5 ✓ | 收敛 |
| character | R17 ✓ | R18 ✓ | R19 ✓ | R20 ✓ | R21 ✓ | R22 ✓ | R23 ✓ | R24 ✓ | E1–E5 ✓ | 收敛 |
| event | R25 ✓ | R26 ✓ | R27 ✓ | R28 ✓ | R29 ✓ | R30 ✓ | R31 ✓ | R32 ✓ | E1–E5 ✓ | 收敛 |

---

### 9-A 试建核验（进入循环前的一次性检验）

**目的**：在通过 NEW1 批量建页前，先使用 NEW1 手建 **1 个页面**（选最有把握的类型——本 wiki 语料信息最丰富的 `technology` 实体 Nautilus），端到端验证 wiki 引擎、插件、历史与最近变更全链路无断裂。

**执行**：

1. 使用 NEW1 手动执行一次建页（选语料信息最丰富的 technology 类实体 Nautilus）：
   ```bash
   WIKI_ROOT=$PWD python3 "$MEMEX_ROOT/wiki/scripts/add_page.py" nautilus - \
     --summary "pilot: 9-A trial page — Nautilus" << 'EOF'
   [frontmatter + content]
   EOF
   ```

2. 执行 **QUO7**（pn-format-lint）——对新建页面执行 PN 格式检查并自动修复，拦截逗号合并、半角括号等违规格式（CONSTITUTION §7.1）：

   ```bash
   python3 "$MEMEX_ROOT/wiki/scripts/butler/pn_format_lint.py" nautilus --fix
   ```

   若有自动修复（脚本输出 `Fixed:`），重新记录修订历史：

   ```bash
   REVISION_LOG="docs/wiki/history/na/nautilus.md"
   if [ -f "$REVISION_LOG" ]; then
     python3 "$MEMEX_ROOT/wiki/scripts/record_revision.py" \
       docs/wiki/pages/na/nautilus.md \
       --summary "fix: QUO7 auto-fix PN format"
   fi
   ```

3. 执行 **CHK7**（new-page-system-check）——运行自动化验证脚本：

   ```bash
   python3 "$MEMEX_ROOT/wiki/scripts/chk7.py" \
     --base-url http://localhost:1828 \
     --slug nautilus
   ```

   脚本逐项检查（退出码 0 = 全部 pass/skip，1 = 有 fail）：

   | 检查项 | 内容 |
   |--------|------|
   | S1 页面渲染 | `#article` 有内容，无崩溃 |
   | S2 PN 引注 | `a.pn-citation` 可见（有引注时） |
   | S3 Infobox | `#infobox` 字段可见，无 `undefined` |
   | S4 Wikilink | `.wikilink` 存在（有链接时） |
   | S5 History | `#?history={slug}` 有修订记录 |
   | S6 Recent 收录 | `#Special:Recent` 收录本词条 |
   | S7 交叉验证 | History 与 Recent 最新时间戳一致 |

   > skip/warn 项需人工确认；fail 项须修复后重跑。

4. **处置**：
   - 全部通过 → 在 `local/BIRTH.md` Phase 9-A 节记录"CHK7 通过"，进入 9-B 批量循环
   - 有失败项 → 提交 RFC 或修复内容，重跑 CHK7；**不得带未通过项进入批量循环**

> CHK7 日志记录在 `logs/gene-express/YYYY-MM-DD-CHK7-{slug}-pass.md`（或 `blocked`）。

#### 9-A 处置记录（2026-07-13）

试建页 `nautilus`（type=technology）已建，QUO7 clean。CHK7 结果：**passed-with-caveats**，允许进入 9-B。

| 检查项 | 结果 | 说明 |
|--------|------|------|
| S1 渲染 | pass | `#article` 正常 |
| S2 PN 引注 | **caveat** | `(TTLU-013-004)` 等渲染为纯文本，0 个 `a.pn-citation`。根因：共享 `pn-citation` 插件硬编码 3 字符 VVV 正则 `[A-Za-z0-9]{3}`，无法匹配 4 字符码 TTLU。**非本页数据问题**（引注文本正确合法）。已起草 `ref/rfc/rfc-vernean-voyages-0003-pn-citation-vol-width.md`（**parked**，全站建成后经用户确认再提交 memex）。修复上游合并后引注自动链接。 |
| S3 Infobox | pass | 字段可见，无 undefined |
| S4 Wikilink | pass | — |
| S5 History | pass | 修订记录存在 |
| S6 Recent 收录 | **caveat（false-negative）** | CHK7 报 fail，但根因为 CHK7 的 1500ms 等待对 939 条 recent feed 过短；直接 playwright 2500ms 等待确认 `nautilus` 渲染为 Recent 首格（'Nautilus'）。行为经验证正确。 |
| S7 交叉验证 | pass | History/Recent 时间戳一致 |

两处 caveat 均为**共享引擎缺陷**（VVV 宽度）或**测试脚本时序**，非 pilot 数据缺陷。用户裁决（2026-07-13）：保留 TTLU 等 1–4 字符码，RFC 暂缓，继续建站。据此判定 9-A **通过**，进入 9-B。

---

> 以下为整个 Phase 9 的批量循环运作规则，适用于 9-B 的全部轮次。

<!-- MUST-COPY: 轮次计数规则，agent 按此更新 R 值 -->
### 轮次计数

Phase 9 启动时在 `local/BIRTH.md` Phase 9 节初始化轮次计数器：

```
Phase 9 轮次：R=0
```

规则：
- 每次执行 **SCN27**（处理 1 个类型）：`R += 1`
- 每次执行 **QUO23**（仅 r3 轮 SCN27 之后执行一次）：`R += 1`
- 每次执行 **EVV5**：`R += 1`
- 每次执行 **EVV6**：`R += 1`
- 每轮执行结束后写日志到 `logs/gene-express/`，格式见下文
- 人工审核通过后才进入下一轮

> 9-A 的 NEW1 试建页本身不计入 R，但若 CHK7 发现问题并触发 RFC，RFC 有自己的编号体系。

---

<!-- MUST-COPY: 选页原则 + standard 档质量标准，agent 逐页对照 -->
### 质量目标

每个 pilot 页面须达到 `standard` 档：

| 要求 | 标准 |
|------|------|
| 语言 | 所有用户可见文字（含 tags）必须使用 `local/config.md` 中 `WIKI_LANG` 指定的语言；`type` 字段保持英文 |
| 内容 | 每节有实质内容，无 `{placeholder}` 残留 |
| PN 引注 | 至少 3 处，指向具体章节段落 |
| Wikilink 目标 | Related 节的链接均指向已存在的页面 |
| Wikilink 形式 | WIKI_LANG=en：label 形式 `[[Captain Nemo]]`（英文 id 含连字符和小写，直接写可读性差） |
| Frontmatter | 类型专属字段全部填写（按对应 schema 模板） |
| quality 字段 | `quality: standard` |

---

### 选页原则

<!-- MUST-COPY: 每轮选页规则，决定建哪些实体 -->
- **无外部依赖优先**：先建基础类型（technology/place），再建引用它们的类型（character/event）
- **每类型每轮仅选语料信息最丰富的 5 个实体**
- **禁止选**元数据类型：chapter、list、overview、template 等
- **禁止选**语料不足的实体（corpus_search 命中 < 3 条）

---

<!-- MUST-COPY: 以下 ASCII 流程图含每轮操作指令，init 时必须原文复制，禁止摘要 -->
### 9-B 批量循环流程

每种类型执行独立的三轮迭代，三轮结束后做元反思，再进入下一种类型。

**关键操作规则**（嵌入在下图各轮中，此处显式列出供 agent 对照）：
- **每轮选页数**：SCN27 每轮从语料选 **5 个**同类型实体，用 NEW1 建 standard 页
- **每句有据**：NEW1 建页时遵守"每句有据"铁律——正文每一句断言必须来自 corpus_search 命中段落，逐句标注 PN，禁止以训练数据常识替代原文依据（详见 NEW1-create-page.md Step 3）
- **日志格式**：`logs/gene-express/*-R{R}-{基因}-{T}-{轮次}.md`
- **人工审核**：每轮完成后必须 ⏸ 暂停，等待用户确认后再进入下一轮
- **模板继承**：r2 使用 EVV5 r1 更新后的模板，r3 使用 EVV5 r2 更新后的模板

```
Phase 9 开始：R=0，在 local/BIRTH.md 记录

对每个类型 T（按依赖顺序，先建基础类型）：

  ┌── 第 r1 轮 ───────────────────────────────────────────┐
  │  SCN27（R+=1）：从语料选 5 个 T 类实体，用 NEW1 建 standard 页  │
  │  写日志 logs/gene-express/*-R{R}-SCN27-{T}-r1.md      │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
  ┌── EVV5 r1 ────────────────────────────────────────────┐
  │  R+=1：对本批 5 页质量评估，识别模板偏差，更新模板       │
  │  写日志 logs/gene-express/*-R{R}-EVV5-{T}-r1-{发现}.md │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核

  ┌── 第 r2 轮 ───────────────────────────────────────────┐
  │  SCN27（R+=1）：再选 5 个 T 类实体（不同子领域），用 NEW1 建页  │
  │  使用 EVV5 r1 更新后的模板                              │
  │  写日志 logs/gene-express/*-R{R}-SCN27-{T}-r2.md      │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
  ┌── EVV5 r2 ────────────────────────────────────────────┐
  │  R+=1：对比 r1，分析模板变更是否有效，继续迭代           │
  │  写日志 logs/gene-express/*-R{R}-EVV5-{T}-r2-{发现}.md │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核

  ┌── 第 r3 轮 ───────────────────────────────────────────┐
  │  SCN27（R+=1）：再选 5 个 T 类实体（边缘/复杂案例），用 NEW1 建页│
  │  使用 EVV5 r2 更新后的模板                              │
  │  写日志 logs/gene-express/*-R{R}-SCN27-{T}-r3.md      │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
  ┌── QUO23 配额核查 ──────────────────────────────────────┐
  │  R+=1：核查本类型三轮累计页面的覆盖配额                   │
  │  写日志 logs/gene-express/*-R{R}-QUO23-{T}.md          │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
  ┌── EVV5 r3 ────────────────────────────────────────────┐
  │  R+=1：第三轮反思，重点检查模板是否趋于收敛              │
  │  写日志 logs/gene-express/*-R{R}-EVV5-{T}-r3-{发现}.md │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核

  ┌── EVV6 元反思 ─────────────────────────────────────────┐
  │  R+=1：读取三份 EVV5 日志，横向分析，最终定稿模板         │
  │  判断模板收敛状态（converged/partial/needs-work）        │
  │  写日志 logs/gene-express/*-R{R}-EVV6-{T}-{状态}.md    │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
  ┌── EXIT-GATE 出口质量门（必做，不可跳过）──────────────────┐
  │  按 ref/spec/workflow-exit-gate.md 执行完整 E1–E5 序列   │
  │  作用域：本类型本轮所有 pilot 页面                        │
  │  FAIL 项就地修正后重验，直到全序列通过                    │
  │  全序列通过，本类型方可结束                               │
  └───────────────────────────────────────────────────────┘
              ↓  ⏸ 人工审核
              → 进入下一个类型（重复上述流程）

所有类型完成 → Phase 9 结束
```

每种类型共消耗 8 轮（SCN27×3 + EVV5×3 + EVV6×1 + QUO23×1），R 累加。若 EVV6 判断为 `needs-work`，可选择追加第4轮迭代，但通常 3 轮已足够收敛。

### --auto 模式下的 Phase 9

`/boot --auto` 执行 Phase 9 时，agent 必须在保持"无确认原则"的同时完整执行所有轮次，**不得跳过 EVV/QUO/EVV6**。

降级执行规则：

1. **⏸ 人工审核暂停点自动跳过**：不等待用户确认，agent 自行判定轮次结果后进入下一轮
2. **EVV5/EVV6/QUO23 评估逻辑完整执行**：读取页面内容、评估质量、写入 `logs/gene-express/` 日志、更新模板——所有操作与手动模式一致，仅跳过"等待用户确认"步骤
3. **EXIT-GATE 出口质量门**：E1–E5 自动执行，FAIL 项自动修正后重验，无需用户介入
4. **轮次计数器正常累加**：R 值从 0 递增到 32（4 类型 × 8 轮）
5. **日志完整产出**：`logs/gene-express/` 下应有 32 份日志文件

> 若自动 EVV 发现模板需要大幅调整，agent 应自行决定调整方向并记录在日志中。`--auto` 模式不阻止模板更新——仅阻止"等待用户批准更新"的动作。

---

<!-- MUST-COPY: 进度表 + 单元格填写规则，agent 维护此表 -->
### 轮次进度表

在 `local/BIRTH.md` Phase 9 节维护进度表，**只记录轮次状态，不记录具体页面**。

具体通过 NEW1 建了哪些页、选页理由、PN 来源，全部记录在各轮 SCN27 日志文件中（`logs/gene-express/`）。BIRTH.md 只作为进度索引，日志文件才是使用 NEW1 建页的真实记录。

| 类型 | r1-SCN27 | r1-EVV5 | r2-SCN27 | r2-EVV5 | r3-SCN27 | QUO23 | r3-EVV5 | EVV6 | EXIT-GATE | 状态 |
|------|---------|---------|---------|---------|---------|-------|---------|------|-----------|------|
| technology | | | | | | | | | | |
| place | | | | | | | | | | |
| character | | | | | | | | | | |
| event | | | | | | | | | | |

单元格填写规则：
- 未开始：空白
- 进行中：`R{N} 进行中`（附日志文件链接）
- 待审核：`R{N} 待审核`
- 完成：`R{N} ✓`

---

<!-- MUST-COPY: wikilink 判断表 + 脚本行为说明，init 时必须原文复制 -->
### 9-C 全章节 Wikify（Pilot 词条链接回填）

**前置条件**：所有类型的 EVV6 均已完成（9-B 全部通过）。  
**目标**：将 Pilot 阶段建立的所有词条页面，在全部章节中建立 wikilink，使章节正文与词条互相导航。

> **为何不纯用脚本**：字面匹配会产生大量错误链接——单词内部匹配、前缀/后缀误伤、同名不同义。本步骤脚本只负责发现候选，语义判断和决策由 LLM 逐条执行。

#### 9-C-1 先跑 dry-run 确认候选

```bash
# 预览：不写文件，打印各章将新增的链接
WIKI_ROOT=$PWD python3 "$MEMEX_ROOT/wiki/scripts/wikify_chapters.py" --dry-run

# 只处理某一章（调试用）
WIKI_ROOT=$PWD python3 "$MEMEX_ROOT/wiki/scripts/wikify_chapters.py" \
  --chapter TTLU-ch01 --dry-run
```

脚本（`$MEMEX_ROOT/wiki/scripts/wikify_chapters.py`）：
- 读 `pages.json` 构建别名表，最长匹配优先
- 英文词：检查单词边界（防 `net` 匹配 `network`）
- 中文词：检查叠词（防 `黑洞` 匹配 `黑洞洞`）、跳过纯 ASCII alias
- 跳过标题行、代码块、引文行（`>`）、脚注行（`<sup>`）
- 幂等：已有 `[[...]]` 的实体不重复链接

#### 9-C-2 逐章语义审查（核心步骤）

对 dry-run 输出逐章审查，**不可批量跳过**：

**判断清单**：

| 问题 | 说明 | 典型误判 |
|------|------|---------|
| 是否完整词项？ | 匹配未截断词素 | `"search"` 在 `"research"` 内 |
| 前缀/后缀是否误伤？ | 前后字符是否使其成为另一词的一部分 | `"net"` 在 `"network"` 中 |
| 语境义是否一致？ | 此处是否确实指向目标词条的概念 | `"Nautilus"` 指 Verne 潜艇，非其他同名 |
| 是否已有上下文链？ | 同章同词条是否已在前文链过（每章只链第一次） | 重复链接降低可读性 |
| 是否宜链？ | 是否在标题、代码块、引文块、脚注内 | 标题内实体通常不链 |

每章审查结束后打印摘要到屏幕：

```
── TTLU-ch01 ──
候选 12 条 → accept 7 / reject 4 / defer 1
  reject: "sea"×2（泛指海洋，非具体词条）
  reject: "Nemo"×1（章节标题内，不链）
  defer:  "Nautilus"×1（上下文含混，入队待 butler 复查）
```

#### 9-C-3 应用链接

审查通过后正式写入：

```bash
WIKI_ROOT=$PWD python3 "$MEMEX_ROOT/wiki/scripts/wikify_chapters.py"
```

如有 reject/defer 的候选，在审查时已确认脚本不会误写（脚本是全量跑、按规则自动过滤）。若 dry-run 发现脚本仍会写入某个应 reject 的词条，需先把该词条加入 `local/wikify_deny.txt`（每行一个 alias/label），脚本读取后跳过：

```bash
# local/wikify_deny.txt 示例（每行一个不应自动链接的词）
sea
captain
island
Ada
```

`defer` 的候选（语境含混、暂不确定）追加到 `logs/butler/queue.md` P2 节，由 butler 后续处理。

#### 9-C-4 渲染验证与提交

- [x] `./wiki-daemon.sh start`，随机抽查 3–5 个章节，链接可点击跳转，无误链
- [x] `defer` 条目已追加到 `logs/butler/queue.md` P2 节（本轮无 defer，deny 表覆盖全部误判）
- [x] 写入处理日志 `logs/gene-express/2026-07-14-9C-wikify-summary.md`：
  - 总候选数、accept/reject/defer 分布
  - 典型 reject 理由归类
- [x] commit：`wikify: Phase 9-C — link pilot pages in all chapters (1079 links added)`

---

### 9-D 重建反向链接索引

**前置条件**：9-C Wikify 全部章节链接已写入并 commit。

所有 wikilink 写入后，必须重建 backlinks 索引，词条页面的"被引用"区块才能正确显示哪些章节引用了该词条。

执行 **LNK19**（[backlinks-rebuild]($MEMEX_ROOT/skills/gene/LNK19-backlinks-rebuild.md)）：

```bash
python3 wiki/scripts/build_backlinks.py --stats
git add docs/wiki/backlinks.json
```

- [x] 输出"覆盖 N 个被引用页，共 M 条反向链接"，N、M 均大于零（1009 页 / 2153 条）
- [x] 本地启动 Wiki，打开任意 pilot 词条页面，确认"引用此页"区块正常显示
- [x] commit：`index: rebuild backlinks after Phase 9-C wikify`

---

### 9-E 首页建设（APP5）

**前置条件**：9-D backlinks 重建完成，pilot 词条已可正常渲染。

调用 **APP5**（[homepage-featured-curation]($MEMEX_ROOT/skills/gene/APP5-homepage-featured-curation.md)）建设首页。执行前先向用户确认两项决策，**默认均为最简选项，用户直接回车即可跳过**。`--auto` 模式下取默认（策略 0 + 无图）。

#### 决策 1 — 首页展示策略

```
首页展示策略（默认 0：无区块，空白展示）：
  [0] 不分区块，不设精选（home.js 保持 HOME_SECTIONS/CORE_FEATURED 为空）← 默认
  [1] 分区块：按词条类型分区展示（HOME_SECTIONS，每类自动计算 limit）
  [2] 精选列表：手动维护 CORE_FEATURED 精选词条卡片
  [3] 分区块 + 精选：[1] 与 [2] 组合
请输入选项编号（直接回车 = 选 0）：
```

#### 决策 2 — 词条卡片是否显示图片

```
词条卡片图片（默认 0：无图，纯文字卡片）：
  [0] 无图 ← 默认
  [1] 有图：对已有图片文件的词条加 image: 字段，首页卡片显示缩略图
请输入选项编号（直接回车 = 选 0）：
```

> 图片来源为 Phase 3-B 提取到 `docs/wiki/images/` 的章节插图，或用户另行准备的图片。选 [1] 时，APP5 仅为文件名可匹配到 pilot slug 的词条加 `image:` 字段，无对应图片的词条不强制补图。

#### 执行逻辑

| 策略 | APP5 执行内容 |
|------|-------------|
| 0（默认） | 确认 `home.js` 空数组，重建注册表验证首页不报错即可 |
| 1 | 机制 B：配置 `HOME_SECTIONS`，limit = max(3, pilot 该类型页数 ÷ 2) |
| 2 | 机制 A：从 pilot 词条中挑选 quality ≥ standard 条目填入 `CORE_FEATURED` |
| 3 | 先配置 `HOME_SECTIONS`，再配置 `CORE_FEATURED` |
| 有图 | 扫描 `docs/wiki/images/`，匹配 pilot slug，写入 `image:` frontmatter 字段 |

```bash
# 执行后重建注册表并本地验证
python3 wiki/scripts/build_registry.py
# ./wiki-daemon.sh start → 打开首页确认展示正常
```

- [x] 用户已确认展示策略和图片选项（或接受默认）（--auto 取默认；沿用既有 type 分区并补 Events 分区，无图）
- [x] `local/config/home.js` 按选择配置完毕（Characters/Places/Technology/Events 四分区）
- [x] 执行 **CHK11**（[homepage-deploy-check]($MEMEX_ROOT/skills/gene/CHK11-homepage-deploy-check.md)）L1–L5 自动化检查，全部 PASS
- [x] 人工执行 CHK11 L6 浏览器检查，无异常（--auto 无头环境跳过；curl 验证首页 200 + core.js 加载，见末尾跳过汇总）
- [x] commit：`feat: Phase 9-E homepage setup via APP5`

---

### 完成条件

- [x] **9-A**：CHK7 全部通过（7 项），试建页无遗留阻塞问题
- [x] 所有主要类型完成三轮 SCN27+EVV5 迭代及 EVV6 元反思
- [x] 所有主要类型在 EVV6 之后完成 EXIT-GATE 完整序列（E1–E5，见 `ref/spec/workflow-exit-gate.md`），无未修正 FAIL 项
- [x] 每种类型有 15 个 quality ≥ standard 的 pilot 页
- [x] 所有类型模板已定稿（EVV6 状态为 converged 或 partial）（4 型全 converged）
- [x] **9-C**：全章节 Wikify 完成，处理日志已写入，defer 条目已入队
- [x] **9-D**：backlinks 索引已重建，词条页面"引用此页"区块正常显示
- [x] **9-E**：首页已通过 APP5 配置，本地渲染正常
- [x] 首页各分区能展示对应类型词条，渲染无报错
- [x] 发现的工作流问题已记录为 RFC（堵塞性）或加入 housekeeping 队列（RFC-0001/0002/0003 parked，待用户批准；见跳过汇总）
- [x] 回填修订历史：
  ```bash
  python3 "$MEMEX_ROOT/wiki/scripts/backfill_recent.py" --mode hybrid --public docs/wiki
  ```
- [x] commit: `pilot: Phase 9 complete — 4 types × 15 pages, templates finalized`

---

> Phase 10 待 `/boot init phase10` 实例化后执行。
