---
round: 17
date: 2026-07-14
phase: 9
gene: SCN27
type: character
pages: [captain-nemo, phileas-fogg, professor-lidenbrock, cyrus-harding, captain-hatteras]
result: pass
---

# R17 — SCN27 character r1（最强实体批次）

## 执行摘要

character 类型 pilot 第一轮（r1），选凡尔纳最具标志性的 5 位主角建 featured 页，验证 `character-schema.md` 五节结构（Overview / Role in the Story / Character & Traits / Relationships / Appearances）。5 页全部经语料逐字核验引注、`add_page.py` 自动回填 featured。r1 取「最强实体」——每部代表作的核心主角，schema 五节自然成立，无空节。

## 页面处理记录

| 页面 | book | role | first_appearance | 引注数 | 引注 PN | quality |
|------|------|------|------------------|--------|---------|---------|
| captain-nemo | Twenty Thousand Leagues Under the Seas | protagonist | TTLU-010 | 7 | TTLU-010-057/021/022/076, TTLU-008-001, MI-057-137, MI-058-005 | featured |
| phileas-fogg | Around the World in Eighty Days | protagonist | AWED-001 | 7 | AWED-001-002/004/010, AWED-002-004, AWED-003-027/057/063 | featured |
| professor-lidenbrock | Journey to the Center of the Earth | protagonist | JCE-001 | 6 | JCE-001-002/025/027, JCE-002-036, JCE-005-003, JCE-006-002 | featured |
| cyrus-harding | The Mysterious Island | protagonist | MI-002 | 6 | MI-002-004/029/050, MI-013-063, MI-017-044, MI-018-056 | featured |
| captain-hatteras | The Adventures of Captain Hatteras | protagonist | ACH-012 | 6 | ACH-012-041/044/047/048/056, ACH-056-004 | featured |

## 本轮要点

- **跨作品角色 captain-nemo**：Nemo 主作品为 TTLU，死亡场景在 MI。沿用 place the-moon 处置——单值 `book`=TTLU（信息最丰富），正文点名 MI 并引 PN（MI-057-137/MI-058-005）。跨作品实体累计升至 3 例（technology gun-cotton + place the-moon + character captain-nemo），仍 <5 阈值，暂不提多值 book RFC。
- **4-char VVV 渲染 Note**：captain-nemo（TTLU）、phileas-fogg（AWED）引注含 4 字符作品码，渲染为纯文本，页首加 RFC-0003 待处理 Note，PN 数据有效。
- **Lidenbrock/Liedenbrock 拼写决策**：语料原文作 "Liedenbrock"，既有 place 页 wikilink 作 [[Professor Lidenbrock]]。label 定为 "Professor Lidenbrock"（与既有 wikilink 一致），aliases 收录语料拼写 "Professor Liedenbrock"/"Liedenbrock"，两轨可解析。
- **overlap warn 修正（edit_page）**：professor-lidenbrock 初建时 JCE-002-036 挂在元叙述句（"a man of restless motion and formidable learning"）上，overlap 1.72% <2% 告警。用 `edit_page.py` 改为逐字子句 "He was acknowledged to be quite a polyglot (JCE-002-036)"，warn 消除。此为 place EVV5 r2「meta 表述避 warn」指引在 character 的复用。
- **edit_page 后补跑 compute_quality**：因 professor-lidenbrock 经 edit_page 修改（不回填 quality），补跑 `compute_quality.py` + `build_registry.py`，5 页统一 featured（沿用 place EVV6 定稿流程提示）。
- **段落 ≤400 字门控**：edit_page 触发退出码 8（Role 段 477 字、Character & Traits 段 516 字），按论点各拆为两段后通过。

## EXIT-GATE 检查

r1 建页轮，不做完整 E1–E5（留 QUO23/EVV6 后统一）。即时核查：
- QUO7 `pn_format_lint.py --fix`：5 页无问题。
- `lint_bucket_structure.py --fix`：pages/ 与 history/ 根目录无散落 .md，分桶正常。
- H2 五节序 5 页遵循 Overview → Role in the Story → Character & Traits → Relationships → Appearances。

## 遗留问题

1. **wikilink-only 节 PN 豁免**：character-schema §引文规范现称「每个 H2 节至少 1 条 PN」，但 Relationships / Appearances 为 wikilink 交叉引用节，与 place Connections 同性质。EVV5/EVV6 轮需比照 place 澄清：交叉引用节以链接完整性为质量准则，不强制 PN。
2. **跨作品实体累计 3 例**：captain-nemo 使累计达 3（<5 阈值），维持单值 book + 正文补偿。
3. **4-char VVV 渲染**：TTLU/AWED 引注渲染问题仍待 RFC-0003 建站后统一处理。
