# Schema: `character`（人物角色）

> MTD3 页面图式模板。NEW1 建页时据此组织结构与字段。语料为 public-domain，
> 实体页只记引注（`(VVV-NNN-PPP)`），不整段复制原文。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 一段定位：身份、所属作品、核心特征 |
| 2 | Role in the Story | ✅ | 在情节中的作用、关键行动（附 PN 引注）|
| 3 | Character & Traits | ○ | 性格、动机、象征意义 |
| 4 | Relationships | ○ | 与其他 character 的 wikilink 关系 |
| 5 | Appearances | ○ | 出场章节列表（`[[VVV-chNN]]`）|

## Frontmatter 专属字段

```yaml
---
id: captain-nemo
type: character
label: Captain Nemo
aliases: []
tags: [character]
description: 'Commander of the Nautilus in Twenty Thousand Leagues Under the Sea.'
book: Twenty Thousand Leagues Under the Sea   # 主要出处作品
affiliation: ''            # 所属组织/团体（可空）
first_appearance: TTLU-006 # 首次出场 pn_prefix（可空）
role: protagonist          # protagonist / antagonist / supporting / narrator
---
```

## 引文规范

- **散文/主张节**（Overview、Role in the Story、Character & Traits）每节至少 1 条 PN 引注 `(VVV-NNN-PPP)`，半角括号（WIKI_LANG=en）。
- **Relationships / Appearances 为 wikilink 交叉引用节**，质量准则是**链接完整性**（见质量阈值表「Relationships 完整」「无悬挂链接」），不强制 PN——该节列相关 character/place/work 的 wikilink 与出场章节，属跨引而非语料主张。若某条关系需佐证可选附 PN，但非硬性要求。此与 place schema 的 Connections 节同性质（place EVV6 已定此原则）。
- blockquote 仅用于原文关键台词/描写，≤ 3 行，附引注。
- PN 密度期望：standard 档每 200 词 ≥ 1 条。

## 写作指引（EVV5 r1，2026-07-14 追加）

- **五节对主角自然成立**：r1 五位标志性主角（nemo/fogg/lidenbrock/harding/hatteras）五节无空节张力。虽 Character & Traits / Relationships / Appearances 标 ○（选填），实践上 featured 档应写全五节。Appearances 至少列主作品一行 wikilink。
- **跨作品角色 book 字段**：维持单值填主作品（信息最丰富者）+ 正文点名其余作品并引 PN（captain-nemo：book=TTLU，正文兼述 MI 死亡场景引 MI-057-137/MI-058-005）。跨作品实体累计 3 例（+technology gun-cotton、place the-moon）<5 阈值，暂不提多值字段 RFC。
- **段落 ≤400 字**：`edit_page.py` 质量门对段落上限 400 字符（退出码 8），每节按论点拆多段。台词密集的 Role/Character 节尤易超限。
- **meta 表述触发 overlap warn**：性格节避免「X is a man of restless motion and formidable learning」式元叙述句挂引注——`add_page.py` 的 overlap 校验会因 token 重叠过低告警（professor-lidenbrock 的 JCE-002-036 即此坑）。改为直接引原文子句（「He was acknowledged to be quite a polyglot」），warn 消除。
- **4-char VVV 渲染 Note**：引注含 4 字符作品码（TTLU/AWED/DSCF/EHLA/MW/ACH…）时页首加 RFC-0003 待处理 Note，PN 数据有效但渲染为纯文本。
- **quality 字段省略 + edit_page 补跑**：建页省略 frontmatter 的 `quality`，交 `add_page.py` 自动回填。用 `edit_page.py` 修改内容后 quality 不回填，需补跑 `compute_quality.py` + `build_registry.py`（沿用 place EVV6 定稿流程提示，适用所有类型）。
- **引文逐字核验 + sentence_index 兜底**：只采用对章节页原文核验过的引文；`corpus_search.py` 多关键词易零命中，改用 1–2 关键词或直接读 `data/sentence_index/{PN前缀}.jsonl` 后以精确短语回定 PN。台词类引文（"I am Captain Hatteras!"）以精确短语一次命中。

## 写作指引（EVV5 r2，2026-07-14 追加）

- **role 枚举四档全覆盖**：r2 补齐 narrator（axel 第一人称叙述者）、antagonist（fix 误判追捕型反派）、supporting（passepartout/ned-land/michel-ardan），加 r1 的 protagonist——`role` 枚举 {protagonist, antagonist, supporting, narrator} 四档均经建页验证。antagonist 不限恶意，「误判/对立职能」（如追捕主角的侦探）即可归此档。
- **affiliation 非空档取值**：角色有明确组织归属时填 `affiliation`（fix=Scotland Yard）；无归属留空（r1 五主角、axel/ned-land 等均空）。按「角色在叙事中被反复标识的组织身份」取值，不强填。
- **裸名/常用词角色的 label 消歧**：角色名为常用英文词（fix、land 等）时，label 取更具辨识度的全称（"Detective Fix"），aliases 收裸名（"Fix"），避免 wikilink 解析与普通词碰撞，符合 LAW §十 label 唯一性。
- **featured 引注门以工具判定为准**：ned-land/michel-ardan 仅 4 引注仍 auto-backfill featured——`compute_quality.py` 综合「五节齐全 + Relationships 完整 + 无悬挂链接 + 密度」而非机械计 10 条。schema「≥10」为期望值非硬门（沿用 place EVV6「quality 工具计算权威」）。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + Role，≥ 2 条 PN 引注 |
| standard | + Character & Traits，≥ 5 条引注，≥ 2 条 wikilink |
| featured | 全部 5 节，引注充分（工具综合判定，期望 ≥8），Relationships 完整，无悬挂链接 |

## EVV6 定稿（converged，2026-07-14）

- **收敛结论**：三轮差异化批次（最强主角 → 新子领域 → 边缘/复杂案例）15 页零结构偏差；模板追加量 8→5→0，r3 边缘批次零追加。schema **converged**，五节结构（Overview / Role in the Story / Character & Traits / Relationships / Appearances）+ `book`/`affiliation`/`first_appearance`/`role` 专属字段定稿，不再变更。与 place（追加量 5→3→0）、technology（3→2→0）收敛轨迹同构。
- **role 枚举定稿**：{protagonist, antagonist, supporting, narrator} 四档经 15 页全覆盖验证（protagonist 6 / supporting 6 / antagonist 2 / narrator 1）。antagonist 含「误判/对立职能」型（fix），不限恶意。character 类型可容纳非人叙事角色（top 犬，role=supporting）。
- **quality 工具计算权威**：以 `compute_quality.py` 客观评级为准。建页省略 frontmatter 的 `quality` 字段，交 `add_page.py` 自动回填；日志不手记档位。15 页 character 经 add_page/compute_quality 统一后全部 featured。featured 引注门以工具综合判定（五节齐全 + Relationships 完整 + 无悬挂链接 + 密度）为准，非机械计 10 条。
- **edit_page 后补跑 compute_quality**：用 `edit_page.py` 修改页面内容后 `quality` 不自动回填（仅 `add_page.py` 回填），需补跑 `compute_quality.py` + `build_registry.py`（professor-lidenbrock R17 即此坑，已修）。通用操作提示，适用所有类型。
- **跨作品角色 book 字段**：维持单值填主作品（首现且最详）+ 正文点名其余作品并引 PN（captain-nemo：book=TTLU 正文兼述 MI；robur：book=RC 正文兼述 MW）。跨作品实体累计 4 例（+technology gun-cotton、place the-moon）逼近 5 经验阈值，**留 butler 观察计数，累积到 ≥5 例再评估多值 book 字段 RFC**；多值 book 会破坏 `build_registry.py` 既有单值语义。「出场跨作品」（主作品建实体、他作仅列 Appearances，如 michel-ardan/barbicane FEM+RM）不计入跨作品实体。
- **同名角色跨作品定位提示**：`corpus_search.py` 按相关度排序，热门作品命中可能淹没冷门作品（搜 "Robur" 前 40 全 MW，RC 被淹）。跨作品同名角色定位改用 `grep data/sentence_index/{VVV}-*.jsonl`（sid 格式 `VVV-NNN-PPP-sN` 内嵌 PPP）+ 精确短语 corpus_search 回验 PN。

## 插图引用

不适用（语料为 Calibre 纯文字重构稿，无正文插图）。
