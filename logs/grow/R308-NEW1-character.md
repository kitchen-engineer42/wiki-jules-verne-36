---
round: 308
date: 2026-07-19
type_round: 1
phase: "2.1"
current_type: character
gene: NEW1
pages: [aronnax]
result: success
---

# GROW 2.1-B · R308 · NEW1 · character — 建 Professor Aronnax（TTLU 第一人称叙述者、巴黎博物馆博物学者，登 Abraham Lincoln 追海怪、坠海获救成 Nautilus 阶下客）

## 执行摘要

Phase 2.1-B character 类型首建（type_round 1），消费 R307 discover 队列**建序 51**（首候选）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Professor Aronnax**（TTLU 第一人称叙述者）——*Twenty Thousand Leagues Under the Seas* 全书由其口吻叙述。
巴黎自然史博物馆助理教授（TTLU-002-002），报界论「海怪」时被点名「the honorable Pierre Aronnax, Professor at the Paris Museum」（TTLU-002-012）；受邀登 Abraham Lincoln 追猎，弃疲惫与藏品即刻应允（TTLU-003-003）；舰撞 Nautilus 坠海（TTLU-007-004），赖仆 Conseil 于水中执其臂得生（TTLU-007-012）；登潜艇为 Nemo 所识（TTLU-010-006）、告以「船上自由但附条件」而成永久之客（TTLU-010-025），Nemo 通篇以「Professor Aronnax」相称（TTLU-010-015）。性格：科学之人，蓄生物分类专家 Conseil（TTLU-003-008），受威胁犹守教授尊严（TTLU-002-025）。

**role=narrator**（第一人称叙述者，character schema role 枚举四档之一，对齐 axel 先例）。**affiliation=Paris Museum of Natural History**（叙事中反复标识之组织身份）。book=Twenty Thousand Leagues Under the Seas、first_appearance=TTLU-002。

**10 distinct solid PN**（TTLU-002/003/007/010）：002-002/002-012/002-025、003-003/003-007/003-008、007-004/007-012、010-006/010-015/010-025（11 引注、10 distinct pn_prefix-PPP）。

**查重**：exact-slug aronnax + 变体（professor-aronnax/pierre-aronnax）filesystem ABSENT；registry alias 无 character 页命中。剔 Nemo/Conseil/Ned Land（已有页）。

**TTLU 4-char VVV**：页首加 RFC-0003 待处理 Note（引注渲染为纯文本、PN 数据有效），对齐 captain-nemo 先例。

**wikilink**（5 链全存在，无悬挂）：[[twenty-thousand-leagues]]、[[nautilus]]、[[conseil]]、[[captain-nemo]]、[[ned-land]]。

prose-gate：初稿 Overview（512）+ Character & Traits（436）二段超门，各拆一次后 0 超段。add_page 一次成型（rev lsqKyJ，size 2888），quality 自动 featured。**pn_validator --mode strict ✓**（无 overlap warn）。

character 计数 15→16，registry total 1539→**1540**，unknown 恒 0。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(character)==0）| =6>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| aronnax | lsqKyJ | Twenty Thousand Leagues Under the Seas | narrator | TTLU-002 | 10 distinct | 叙述者博物学者，坠海-获救-成阶下客单指；剔 Nemo/Conseil/Ned Land 已有页；TTLU 4-char Note；链 5 页；strict ✓ |

- **aronnax**：10 distinct solid PN（TTLU-002/003/007/010）；aliases [Pierre Aronnax, Professor Pierre Aronnax]；character-schema 五 H2（Overview/Role in the Story/Character & Traits/Relationships/Appearances）。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Aronnax 身份-经历因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 2 段超门（512、436），各拆一次后 0 超段。✔
- **G3 ≥5 distinct PN**：10 solid（TTLU-002/003/007/010），逾门（target 8）。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role；TTLU 4-char Note。✔
- **registry 一致**：total 1540 character 16 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry alias 无 character 页冲突。✔
- **wikilink 完整性**：5 链全存在，无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R309 起始计数）

| 字段 | R308 起始 | R309 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 308 | 309 |
| type_round | 0 | 1 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 244 | 245 |
| last_updated_round | 308 | 309 |

## 遗留问题

1. **character 页数 16**：本轮 +1（aronnax）。queue(character) 6→**5**（建序 51 消费；余 52-56：ayrton/dick-sand/pencroft/herbert/paganel）。registry 全库 **1540**，unknown 0。
2. **下轮 R309 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；since_discover=1<10 且全局 queue≥10 → §3(3) 否；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 52（ayrton）。ayrton 跨 MI/SI/SC 三作品，建时 book 取主作品（MI 或 SC 源起）+ 正文点名其余作品并引 PN（对齐 captain-nemo/robur 跨作品 book 先例）；剔 event tabor-island-castaway 别线。
3. **character 候选池充沛**：type-survey 估 ~180-240，现 16 页。首批 6（建序 51-56）后仍大量二线角色（Nab、MI 其余殖民者、SC 群像、Michel Strogoff/Kaw-djer/Servadac 等主角）可续掘；queue(character) 降至 <10 或 since_discover≥10 时触发 §3(3) SCN28 补队列。
4. **EVV5 间隔重置**：R307 CLOSE §5.1 复位 since_evv5=0，character 类型从零起算；预计 R318 前后（since_evv5 达 10）首次触发 character EVV5。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias「Death of Prince Dakkar」；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（初稿 2 段超门已拆）。
8. **corpus-discover 顺延**：since_corpus=244→245（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（五类型皆 null）；character 建成即 Phase 2.1 迭代末触发。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
