# 内务任务队列（Housekeeping）

> butler housekeeping 轮次消费此队列。空队列时 butler 自行发现内务任务。

## P1 — 高优先级

### HK-featured-inflation — `featured` 等级虚高（结构填充 ≠ 质量/notability）

**现象**：`add_page.py` 新建页面即被自动标 `featured`，即便实体在语料中极少出现、内容单薄。boot 期间 61/61 pilot 页全部 featured，被我误当作"收敛=高质量"信号。

**根因（自检 2026-07-14 确认）**：
1. `compute_quality.py:84-87` 的 featured 判据是纯**结构性**：`h2≥3 AND (PN≥3 OR 引文≥5) AND 散文≥200 字符`。200 字符 ≈ 2–3 句，门槛极低；只测"模板是否填满"，不测 notability 或实质密度。
2. `add_page.py:168-171`（RFC-central-empire-fiscal-code-0007）新建页**无人工复核、无 notability 门**即自动回填 quality → 填满模板的页面瞬间 featured。
3. `compute_quality.py:163-167` `upgrade_only=True` 默认**只升不降**：featured 具粘性，事后删内容也不降级。

**实证**：`tabor-island-castaway`、`liedenbrock-cipher`（描述性标题的 event 页，语料直接提及 ≈0）与 `captain-nemo`（601 次）同为 featured。featured 与语料出现频次零相关。

**修复方向（择一或组合）**：
- 给 featured 加 notability/实质门：如散文下限提到 ~800–1000 字符，或引入语料提及频次阈值；
- `add_page.py` 自动回填**封顶 `standard`**，featured 需显式人工提升；
- 重新定义：featured=编辑/notability 判断，另设 `complete`=结构完整（机械可判）。

**处置**：属共享 memex 组件（`compute_quality.py`/`add_page.py`）—— 依 RFC 停靠决策 **PARK**，不自动提交；全站建成 + 用户签署后连同 VVV 宽度三 RFC 一并批量评审。此条为待起草 RFC 的种子。

**GROW 决策（2026-07-14，用户拍板）**：Phase 2 广度扩张**照常进行**，接受所有新建页被 add_page.py 自动标 featured，扩张期间**将 featured 视为无意义信号、不作质量依据**。**欠一次全库批量重评**（notability/实质感知的 quality 重算 + 写回），待 featured-inflation RFC 落地后执行。**DEFERRED-REGRADE** 标记此债。

### HK-addpage-prose-gate-bypass — `add_page.py` 不执行散文质量门（与 `edit_page.py` 不一致）

**现象（GROW 2.1-Showcase R1，2026-07-14 发现）**：`edit_page.py` 强制单段 ≤400 字散文门
（`ref/散文质量强制规范.md`，退出码 8 拦截），但 `add_page.py` **无此检查**。本轮 4 页样板经
`add_page.py` 建立时均含超 400 字长段（TTLU 603 / MI 527 / Gun Club 474 / Weldon 604），
仍被写入并自动标 featured；只有事后 `edit_page.py` 触碰才暴露违规。

**影响**：新建页与编辑页走两套不一致门禁；违规长段可在 featured 页中长期潜伏，直到被编辑才触发。
样板作为 Phase 2 全期质量基线，本身违反散文规范会污染基线。

**修复方向**：`add_page.py` 对齐 `edit_page.py` 的散文门（或至少建时 warning）。

**处置**：属共享 memex 组件（`add_page.py`）—— 依 RFC 停靠决策 **PARK**，不自动提交；
与 HK-featured-inflation 及 VVV 宽度三 RFC 一并批量评审。本轮 4 页已手工拆分复检达标。

## P2 — 中优先级

### HK-robur-alias-conflict — `Robur the Conqueror` label/alias 撞名

**现象（GROW R9 BLK3，2026-07-15 发现）**：`build_registry.py` 报
`alias conflict: 'Robur the Conqueror' → robur-the-conqueror vs robur`。work 页
`robur-the-conqueror`（作品）与 character 页 `robur`（人物）共享 label/alias `Robur the Conqueror`，
`alias_index` 后写覆盖前写（LAW §10 label 唯一性）。Pilot 期既有数据，非 wikify 引入。

**影响**：`[[Robur the Conqueror]]` 解析歧义，可能误链到人物页或作品页。

**修复方向**：消歧——work 页 label 保留 `Robur the Conqueror`（作品全名），character 页
`robur` 的 label/alias 收窄为 `Robur`，去掉与作品同名的 alias。属本地页面数据，经 edit_page.py 可修，
非 memex 组件、无需 RFC。待 character 类型轮或 2.1-Z PHQ 消歧检查时处理。

### HK-discover-existing-type-blindspot — SCN28 corpus discover 未核对既有页 label，跨类型漏判

**现象（GROW R11，2026-07-15 发现）**：R10 organization corpus discover 将 **Reform Club** 列为新候选
（distinctPN≈23），但 `reform-club` 已作为 `type: place` 页存在（Pilot 期建）。build_wanted/corpus 扫描
只按语料专名统计，未核对既有页面的 label/alias，导致把「已建但类型不同」的实体误判为新候选。

**影响**：discover 计数虚高（new_candidates 含伪新条目）；建页时才由 add_page.py `页面已存在` 拦截，
浪费一个候选位。若某类型靠虚高 new_candidates 维持 discover_streak_low<3，可能延迟本应触发的类型关闭。

**修复方向**：SCN28 discover 的专名过滤增加一步——比对 `alias_index`（label + aliases）去除任何已建页
（不论 type），只保留真正无页的实体。属 discover 逻辑（GROW skill / 勘探脚本），非页面数据。

**处置**：记录待评审。当前 GROW 轮内以人工核对 + 顶替候选缓解（R11 已 P&O 顶替 Reform Club）。

### HK-corpus-discover-orgname-blindspot — corpus/红链 discover 漏判无 wikilink 的组织专名

**现象（GROW R15，2026-07-15 发现）**：organization 关闭倒计时中，R15 改用 **org-suffix 语料复扫**
（`… Company|Society|Club|Institution|Association|…` 专名模式）验证穷尽，补捞出 **2 个此前全程漏判**
的候选：**Canadian General Transportation Company**（WC，distinctPN≈5）、**North-West Company**
（FC，distinctPN=4）。二者 R10 corpus discover 与 R12/R14 红链扫描均未捕获。

**根因**：(1) 红链扫描（SCN28）只看 wikilink target，这 2 个组织**语料中从未被 `[[...]]` 链接**，故不可见；
(2) R10 corpus discover 的专名过滤显然也未命中此二者（疑似 distinctPN 阈值或后缀模式覆盖不全）。
结果 organization 差点在仍有 2 个达门候选未建时被 streak 机制关闭。

**影响**：类型「穷尽」判定不可靠——仅靠红链 + 单次 corpus discover 会漏掉无链的实体，导致 discover_streak_low
虚高、类型过早关闭、grounded 候选被永久遗弃（关闭后该 type 移出 type_queue，不再回访）。

**修复方向**：类型关闭前（streak 逼近 type_close_streak 时）强制跑一次 **suffix/pattern-based corpus 复扫**
（不依赖 wikilink），与 alias_index 比对后确认无达门未建候选，方可关闭。属 discover 逻辑（GROW skill）。

**处置**：本轮以人工 org-suffix 复扫缓解，2 候选入 queue P1 待 R16 建。记录待评审。
另见 R15 日志 **GROW-JUDGMENT-R15**：为不遗弃此 2 候选，R15 判断性保持 discover_streak_low=2（机械值应为 3）。

### HK-surface-discover-pattern-undercount — SCN28 表层复扫 pattern 漏计致 R57 false-exhaustion

**现象（GROW 2.1-B R59，2026-07-15 发现）**：R57 place 表层复扫记「≥5 单源 0 枚，标准表层穷尽」，
据此 R58 启动 place 关闭倒计时（discover_streak_low 0→1）。R59 改用宽式 toponym pattern 重扫，
**同一语料**捞出 **19 枚 ≥5 单源新候选**——R57 结论为**系统性误判**。

**根因（两类 pattern 盲区）**：
1. **单复数/大小写变体漏匹配**：`Smith's Strait`（单数）被 `Smith's Straits`（复数）主式漏掉
   → R57 记 [4]，实为 ACH:7；`bay of Talcahuano`（小写）+ 裸 `Talcahuano` 被 `Bay of Talcahuano` 主式漏掉
   → R57 记 [3]，实为 SC:13。
2. **构式盲区**：`GEO of X`（Strait of Gibraltar / Cape of Good Hope / Gulf of Mexico）与 `X Ocean`
   （Indian / Pacific / Atlantic Ocean）整类未进 R57 扫描 pattern，零命中。
   另 R51/R57 将 Detroit River(MW:6)/Chatham Islands(RC:7)/Washburn Bay(FC:7)/Antarctic Sea(AM:7)/
   Coronation Gulf(FC:5)/Platte River(AWED:5)/Blueridge Mountains(MW:5)/Shannon Island(WAI:5)
   误记为「agg 5–6 hold」，实为 ≥5 单源。

**影响（实质缺陷，非纯记录）**：致 R57 false-exhaustion → R58 关闭倒计时误启动。若无 R59 复核，
place 将在仍有 19 枚 grounded 达门候选未建时被 streak 机制误关闭，候选随类型移出 type_queue 永久遗弃。
此为此前 PARK 的「discover 双盲区」债务的具体量化实例，**性质升格**。

**修复方向**：SCN28 表层 discover pattern 需覆盖 (a) 单复数/大小写归一化；(b) `GEO of X`、`X Ocean/Sea`
等前置/后置介词构式；(c) 与 alias_index 比对去重后再统计单源 distinctPN。属 discover 逻辑（GROW skill / 勘探脚本）。

**处置**：R59 已人工宽式重扫缓解，19 候选入 queue 待 R60+ 建。依 PARK-until-build-done 原则**不自主 file RFC**；
build 完成后与 discover 双盲区诸项一并提 RFC，用户批量评审。

### HK-wanted-pages-space-filter — `build_wanted_pages.py` 误滤含空格的 wikilink target

**现象（GROW R12，2026-07-15 发现）**：`build_wanted_pages.py:73` 将任何含空格的 wikilink target
当作"解析伪迹"过滤（`过滤包含空格或格式异常的 target`）。但 LAW §9 mandated 的 label 形式链接
（`[[Captain Nemo]]`、`[[Jaspar Hobson]]`）本就含空格。结果全库 1097 链接目标只报出 1 条红链（Kennedy，
唯一单词 target），其余 label 形式红链（Ferguson/Hobson/Barnett/Clawbonny/Maston/Noltitz/Cromarty/
Paganel/Garral 等）全部漏报。

**影响**：红链发现（SCN28 的一半）对 label 形式链接完全失明，严重低报待建页面；WantedPages 特殊页失真。
GROW discover 若依赖此工具会误判候选耗尽。

**根因**：脚本假设 wikilink target 为 slug（无空格），与 LAW §9 label-form 约定冲突。

**修复方向**：改 target 解析——先按 alias_index（label→slug）解析，未命中再 slugify 比对页 id；
只有既非 label 又非合法 slug 的才判伪迹。属共享 memex 组件（`build_wanted_pages.py`）→ **PARK**，
与其余 memex 组件债一并批量评审。GROW 轮内红链发现改用 label-aware 手工扫描替代。

### HK-20kleagues-seas-alias — `[[Twenty Thousand Leagues Under the Seas]]` label 复数错配

**现象（GROW R12 发现）**：6 页（captain-nemo/conseil/ned-land/giant-squid-attack/sargasso-sea/
sea-monster-hunt）链向 `[[Twenty Thousand Leagues Under the Seas]]`（复数 Seas），但 work 页
`twenty-thousand-leagues` 的 label 为单数 `Twenty Thousand Leagues Under the Sea` → 6 条断链。

**修复方向**：给 work 页加 alias `Twenty Thousand Leagues Under the Seas`（原书名确为复数 Seas，
alias 更合适），或改 6 页链接。属本地页面数据，`edit_page.py` 可修，无需 RFC。Pilot 既有，
待 character 轮或 2.1-Z PHQ 消歧时处理。

### HK-reform-club-place-vs-org — `reform-club` 归类 place/org 待定

**现象**：`reform-club`（Pall Mall 绅士俱乐部）现为 `type: place`。作为有成员的俱乐部，org 属性强；
作为建筑/地点亦可 place。与 Cambridge Observatory（R10 flagged）并列 borderline。

**处置**：留待 character 轮后或 2.1-Z PHQ 统一裁定。若改 org 需 `edit_page.py` 改 type 并相应调整
place 类型 final_count（place 尚未开建，type_queue 中）。本地页面数据，无需 RFC。

### HK-registry-typefield-not-propagated — `build_registry.py` 不透出类型专属字段到 pages.json

**现象（GROW 2.1-B R20 EVV5 organization 扫描，2026-07-15 发现）**：organization 全部 15 页
frontmatter 均正确填 `org_type`（club/company/society/committee/…）与 `founded`，但
`build_registry.py` 生成的 `pages.json` 只透出通用字段 + `book`，**未透出 `org_type`/`founded`**
（pages.json 页对象 keys 无这两项）。其他类型的专属字段（character 的 affiliation/role、
place 的 region 等）预计同样受影响。

**影响**：前端无法按 `org_type` 分面/筛选（如"列出所有 company"）；类型专属字段仅存在于页面
frontmatter，registry 层不可见。不影响页面正文或 PN grounding——纯 registry 投影缺失。

**修复方向**：`build_registry.py` 读取 `local/template/{type}-schema.md` 声明的专属字段并透传到
pages.json（或至少白名单 org_type/founded/region/affiliation/role 等）。

**处置**：属共享 memex 组件（`build_registry.py`）—— 依 RFC 停靠决策 **PARK**，不自动提交；
与 featured-inflation / 散文门 / VVV 宽度诸 RFC 一并批量评审。本地 frontmatter 已正确，无需回填。

## P3 — 低优先级
