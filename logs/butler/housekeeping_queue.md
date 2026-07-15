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

## P3 — 低优先级
