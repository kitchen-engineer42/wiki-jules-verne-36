---
round: 313
date: 2026-07-19
type_round: 6
phase: "2.1"
current_type: character
gene: NEW1
pages: [paganel]
result: success
---

# GROW 2.1-B · R313 · NEW1 · character — 建 Paganel（In Search of the Castaways 心不在焉之地理学家，R307 队列末位）

## 执行摘要

Phase 2.1-B character 类型第 6 建（type_round 6），消费 R307 discover 队列**末位建序 56**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；discover_streak_low=0<3；queue(character)=1>0 → §3(3) 走 NEW1 消费；§3(4) zombie 否；stub%=0 → §3(7) NEW1）。

**Jacques Paganel**（*In Search of the Castaways* 探险队地理学家）——Geographical Society of Paris 秘书、诸国学会通讯会员（SC-006-075），因心不在焉误登 *Duncan* 号（本欲赴印度却驶向南美，趁船员做礼拜时登错船，SC-007-007），却自称「too happy to have made a mistake which has turned out so agreeably」（SC-007-056）。投身寻找 Grant 船长、自列 Glenarvan 与少校之侧为探险要人（SC-010-049），maps 不离手、遇未标之溪则「all the fire of a geographer burned in his veins」（SC-011-011）。其博学既推动情节亦制造笑料——误学西班牙语代葡萄牙语（SC-015-055），后重读文书发现走错方向、读出文中所无（SC-024-002），此纠正重定全局搜索；彼达观曰「it is only human to make a mistake, while to persist in it, a man must be a fool」（SC-027-051）。自负而遭质疑地理学识则大怒（SC-017-036），然确属真才（Lady Helena 誉之，SC-035-027）；痴迷仪器、竟耗半夜擦拭望远镜之镜片（SC-034-051）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-006、**affiliation=Geographical Society of Paris**（其秘书身份，首个非空 affiliation 之 character 本批次）。aliases [Jacques Paganel]。

**11 distinct solid PN**（SC-006/007×2/010/011/015/017/024/027/034/035）：006-075、007-007、007-056、010-049、011-011、015-055、017-036、024-002、027-051、034-051、035-027。

**查重**：exact-slug paganel + 变体（jacques-paganel）filesystem ABSENT；registry 命中仅 3 chapter 页（SC-ch07/ch24/ch66，章题含 Paganel）——非 character 实体，剔除。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[In Search of the Castaways]]（work 页存在）。Glenarvan/McNabbs/Lady Helena/Captain Grant 纯文本（无独立页则不造死链）。

prose-gate：初稿 0 超段。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

character 计数 20→**21**，registry total 1544→**1545**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1>0 → NEW1 消费 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *§3(3) queue<10 成立（=1），按既有轮实践消费既有候选走 NEW1。**注**：本轮消费 R307 队列末位，queue(character)→0；**下轮 R314 触发 §3(4) SCN28-zombie re-scan** 补 character 候选。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| paganel | tWLpuI | In Search of the Castaways | supporting | SC-006 | 11 distinct | 心不在焉地理学家-误登船-纠错要角单指；affiliation=Geographical Society of Paris；SC 2-char 无 Note；strict 首过 ✓；链 work 页；剔 3 chapter 页；Glenarvan/McNabbs/Helena 纯文本 |

- **paganel**：11 distinct solid PN；aliases [Jacques Paganel]；character-schema 五 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Paganel 地理学-误船-纠错因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 含 book/affiliation/first_appearance/role/quality；SC 2-char 无 Note。✔
- **registry 一致**：total 1545 character 21 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + 变体 filesystem ABSENT；registry 仅命中 chapter 页（已剔）。✔
- **wikilink 完整性**：work 链存在，无悬挂；Glenarvan/McNabbs/Helena 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R314 起始计数）

| 字段 | R313 起始 | R314 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 313 | 314 |
| type_round | 5 | 6 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 249 | 250 |
| last_updated_round | 313 | 314 |

## 遗留问题

1. **character 页数 21**：本轮 +1（paganel）。queue(character) 1→**0**（R307 队列建序 51-56 全消费尽）。registry 全库 **1545**，unknown 0。
2. **下轮 R314 = SCN28-zombie re-scan（§3(4)）**：queue(character)==0 → §3(4) 触发 discover 补候选（非 NEW1 建页轮）。这是 R307 后首个 character discover 轮；须**穷尽扫描**语料补 character 候选（memory 规则：勿仅凭 queue 判饱和）。候选池充沛：MI 余殖民者 **Nab / Gideon Spilett / Cyrus Harding**（Lincoln 岛五殖民者尚余三）；SC 群像 **Glenarvan / Mary Grant / Robert Grant / Captain Grant / John Mangles / McNabbs**；单作品主角 **Michel Strogoff / Hector Servadac / Kaw-djer（The Survivors of the "Jonathan"）/ Mathias Sandorf / Kéraban / Wilhelm Storitz / Robur** 等。discover 轮 counter：since_discover 归 0、discover_streak_low 依 new_candidates 数更新。
3. **affiliation 字段首用（character）**：paganel affiliation=Geographical Society of Paris（本批 aronnax='Paris Museum of Natural History' 亦非空；ayrton/dick-sand/pencroft/herbert 空）。符合 character-schema（affiliation 为组织身份，主角/无组织者留空）。
4. **wikilink 回填候选（低优）**：herbert（R312）正文纯文本引 Pencroft（R311 已建页）；paganel 引 Glenarvan 等尚无页。俟相关 character 建成后可批量回填 [[...]] 链；本批保守未链，无死链。
5. **edit_page 剥离 quality 教训（已入 memory）**：R311-313 纯 add_page（除 R311 work 页 alias 修复），无新增涉及。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
9. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理。
10. **corpus-discover 顺延**：since_corpus=249→250（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
