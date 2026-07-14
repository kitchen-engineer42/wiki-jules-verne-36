# Schema: `event`（事件/情节节点）

> MTD3 页面图式模板。情节转折、关键场景。只记引注，不整段复制原文。

## 页面结构（H2 顺序）

| 顺序 | H2 节 | 必填 | 说明 |
|------|-------|------|------|
| 1 | Overview | ✅ | 一句话概括：何事、何时（书内）、涉及谁 |
| 2 | What Happens | ✅ | 事件经过（按原书次序，附 PN 引注）|
| 3 | Significance | ○ | 对情节/人物的影响 |
| 4 | Participants & Setting | ○ | 相关 character / place 的 wikilink |

## Frontmatter 专属字段

```yaml
---
id: eighty-day-wager
type: event
label: The Eighty-Day Wager
aliases: []
tags: [event]
description: 'Phileas Fogg''s bet at the Reform Club to circle the globe in eighty days.'
book: Around the World in Eighty Days
location: London               # 主要发生地（wikilink 目标，可空）
pn_anchor: AWED-001-XXX        # 事件起点 PN（可空）
---
```

## 引文规范

- **散文/主张节**（Overview、What Happens、Significance）每节至少 1 条 PN 引注 `(VVV-NNN-PPP)`，半角括号（WIKI_LANG=en）。What Happens 节按时间线组织，每个关键节点附 PN。
- **Participants & Setting 为 wikilink 交叉引用节**，质量准则是**链接完整性**（见质量阈值表「Participants 完整」），不强制 PN——该节列相关 character/place/work 的 wikilink，属跨引而非语料主张。此与 character schema 的 Relationships/Appearances 节、place schema 的 Connections 节同性质（character/place EVV6 已定此原则）。
- 引原文动作/对白用 blockquote ≤ 3 行 + 引注。
- PN 密度期望：standard 档每 200 词 ≥ 1 条。

## 写作指引（EVV5 r1，2026-07-14 追加）

- **Significance 节是 overlap warn 高发区**：Significance 天然解释性强，最易把 PN 挂在元叙述句上触发 `add_page.py` 的 overlap 校验告警（r1 三处 warn：eighty-day-wager AWED-003-063、columbiad-launch FEM-027-014、lincoln-island-landing MI-002-001 均在 Significance）。修法沿用 character EVV5：把 PN 嵌到 **verbatim 子句**后（"Saturday, the 21st of December" / "started on the 1st of December at ten hours..." / "Those whom the hurricane had just thrown on this coast"），warn 消除。event 比 character 更易犯此坑，Significance 每条 PN 必挂原文子句。
- **四节对标志性事件自然成立**：r1 五个情节枢纽（赌约/发射/搏斗/遇难/下降）四节无空节张力。虽 Significance / Participants & Setting 标 ○（选填），实践上 featured 档应写全四节。Participants & Setting 至少列主作品 + 核心 character/place 的 wikilink。
- **段落 ≤400 字**：`add_page.py`/`edit_page.py` 质量门对段落上限 400 字符（退出码 8），What Happens/Significance 叙事密集尤易超限，按论点/时间节点拆多段。
- **4-char VVV 渲染 Note**：引注含 4 字符作品码（TTLU/AWED/ACH…）时页首加 RFC-0003 待处理 Note，PN 数据有效但渲染为纯文本；≤3 字符作品码（FEM/MI/JCE）无需。
- **quality 字段省略 + edit_page 补跑**：建页省略 frontmatter 的 `quality`，交 `add_page.py` 自动回填。用 `edit_page.py` 修改内容后 quality 不回填，需补跑 `compute_quality.py` + `build_registry.py`（通用操作提示，适用所有类型）。
- **引文逐字核验 + sentence_index 兜底**：只采用对章节页原文核验过的引文；`corpus_search.py` 多关键词易零命中或热门作品淹没冷门，改用 1–2 关键词或直接读 `data/sentence_index/{VVV}-*.jsonl`（sid 内嵌 PPP）后以精确短语回定 PN。数值/日期类引文（"twenty-seven feet"、"1st of December ten hours forty-six minutes forty seconds"）以精确短语一次命中。
- **location 字段取值**：填事件主要发生地。取值可为 place 实体（Lincoln Island、Snæfellsjökull、Stone's Hill）或叙事场所/载具（Reform Club、Nautilus）；按「事件在原书中被反复标识的发生地」取值，优先能 wikilink 到既有 place/technology 实体者。无明确单一地点留空。

## 质量阈值

| 档位 | 最低要求 |
|------|---------|
| basic | Overview + What Happens，≥ 2 条 PN |
| standard | + Significance，≥ 4 条引注 |
| featured | 全部 4 节，≥ 6 条引注，Participants 完整 wikilink |

## 插图引用

不适用（无正文插图）。

## EVV6 定稿（converged，R32，2026-07-14）

**收敛判定：event 类型模板已收敛。** 依据三轮 EVV5 评估（R26 r1 / R28 r2 / R31 r3）：

- **结构追加量 7→0→0**：r1 追加 1 澄清（Participants wikilink 节 PN 豁免）+ 6 写作指引；r2 追加 0；r3 追加 0（仅 1 条工具经验细化，非新结构）。与 character（8→5→0）、place（5→3→0）、technology（3→2→0）收敛轨迹完全同构。
- **15 页零结构偏差**：三轮 15 页（r1 情节枢纽 / r2 新子领域 / r3 边缘复杂）H2 四节序、`book`/`location`/`pn_anchor` 三字段、引文规范零偏差，全 featured。
- **边缘批次零追加**：r3 最难批次（跨作品死亡、抽象无地点揭示、异地火山返回、极点火山climax、天外跨作品续篇）四节全吸收，收敛直接证据。

**定稿结论**：四节结构（Overview / What Happens / Significance / Participants & Setting）+ 三专属字段 + 引文规范 + 写作指引，全部冻结，后续 butler 建 event 页直接套用，不再迭代模板。

### EVV6 追加写作指引（2 条）

- **单字/专名引文需嵌更长 verbatim 上下文**（R31 固化）：当引文原文关键内容仅为单词或专有名词（如 "STROMBOLI"），overlap 校验因关键词重叠天然偏低而易触 warn。修法：引句嵌入更长 verbatim 上下文（"the little herdboy, slipping out of Hans' hands, replies 'STROMBOLI'"）。此为 r1「Significance PN 必挂 verbatim 子句」在单字专名场景的加强版。
- **跨作品事件 vs 跨作品实体计数区分**：event 的跨作品牵涉（nemo-death MI←TTLU、lunar-orbit-miss RM←FEM）属叙事引用——正文点名 + Significance 缝合，单值 `book` 字段即可，**不计入跨作品实体 ≥5 阈值**（该阈值仅统计跨作品实体：gun-cotton/the-moon/captain-nemo/robur，当前累计 4）。事件的跨作品不触发多值 book 字段的 RFC。
