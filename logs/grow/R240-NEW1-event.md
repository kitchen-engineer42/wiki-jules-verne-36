---
round: 240
date: 2026-07-18
type_round: 6
phase: "2.1"
current_type: event
gene: NEW1
pages: [andes-earthquake]
result: success
---

# GROW 2.1-B · R240 · NEW1 · event — 建 The Andes Earthquake（Cordillera 夜震掀落搜寻队、掠走 Robert Grant，SC）

## 执行摘要

Phase 2.1-B event 类型第 6 建（type_round 6），消费 R238 discover 队列**建序 6**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub=0 → §3(7)）。

**The Andes Earthquake**（SC 主）。事件锚定 pn_anchor=**SC-013**（Cordillera 夜震之章）。
gather（"earthquake" SC 多 PN + SC-012 region overturned / SC-013 shock）。逐句核**单指该事件**
（Glenarvan 搜寻队夜越安第斯，地震掀落全队、Robert Grant momentary 失踪）。
exact-slug andes-earthquake ABSENT。SC 2-char，PN 正常渲染，无需 RFC-0003 Note。

**恰达门 7 distinct solid PN**（SC×7，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SC-013-073 | Paganel 惊呼「An earthquake!」（夜震起）|
| Overview | SC-013-075 | tremendous shock 掀落全队至山脚 |
| What Happens | SC-012-024 | 向导警告 last earthquake 毁道 |
| What Happens | SC-012-038 | region overturned by recent shocks 逼队上行 |
| What Happens | SC-013-076 | 幸存者站起 stunned but firm |
| Significance | SC-014-007 | 「Heaven grant Robert may be still alive!」失踪之痛 |
| Significance | SC-014-003 | shocks always occurring 安第斯永劫震荡 |

**VVV 处置**：SC 2-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓。

event 计数 20→21，registry total 1495→1496，unknown 恒 0。

**建页波折记录**（方法论债）：add_page.py 一次成型（rev AIkToj，quality 自动 featured），但 pn_validator strict 报
`SC-013-073 关键词重叠度 1.56% < 2%`——Overview 原句仅系短引 `"An earthquake!"`，keywords 与源句重叠不足。
改以 verbatim 长句 `"An earthquake!" exclaimed Paganel, and he was not mistaken` 挂 PN 后 strict ✓。
惟修正走 edit_page.py（强制 400 门），触退出码 8（第 3 段 428 字），拆 Overview 两段后 edit_page.py 成型（rev Itt9Qm，size 2377）。
**edit_page.py 不回填 quality**——页面 quality 被剥离、registry quality: None。经 add_page.py `_backfill_quality` 纯函数单页回填
（非 compute_quality.py 全库 CLI，遵 deferred re-grade）→ quality featured 复原。build_registry 仅 Robur PARK。
location=Andes、pn_anchor=SC-013、book=In Search of the Castaways、aliases=[The Cordillera Convulsion]。
链 [[Andes]]/*[[in-search-of-the-castaways]]*（Glenarvan/Paganel/Robert Grant 散文提及，未建 character）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| andes-earthquake | Itt9Qm | In Search of the Castaways | Andes | SC-013 | 7 | Cordillera 夜震掀队；Robert Grant momentary 失踪；SC 2-char 无需 RFC-0003 Note；quality 经单页纯函数回填 |

- **andes-earthquake**：7 distinct solid PN（SC 全用，四节分配）；aliases [The Cordillera Convulsion]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（安第斯地震）；strict 重叠度门修正后 ✓。✔
- **G2 段落 ≤400 字**：edit_page.py 400 门通过（第 3 段拆分后）。✔
- **G3 ≥5 distinct PN**：7 solid（SC），逾门。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 改 + add_page._backfill_quality 回填，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（含撇号）。✔
- **registry 一致**：total 1496 event 21 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug andes-earthquake ABSENT；非既有 20 event。✔
- **单指核**：SC ch12/13/14 逐句确认指同一地震事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R241 起始计数）

| 字段 | R240 起始 | R241 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 240 | 241 |
| type_round | 6 | 7 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 176 | 177 |
| last_updated_round | 240 | 241 |

## 遗留问题

1. **event 页数 21**：本轮 +1（The Andes Earthquake）。队列余 2（建序 7-8）。registry 全库 1496，unknown 0。
2. **下轮 R241 = NEW1（event）**：建 queue 建序 7 **The Condor Abduction**（SC，SC-014）。
   since_evv5=7<10、streak=0、queue(event)=2>0 → §3(7) NEW1。SC 2-char，无需 RFC-0003 Note。
   **须核单指**：SC condor 有泛指飞掠句，建时剔除，只保留「秃鹰掠走 Robert Grant」单指句。
3. **注意 R244 EVV5 逼近**：since_evv5=7，将于 R244（=10）触发 §3(1b) EVV5 全库评审轮（非建页）。
4. **edit_page.py quality 剥离债（方法论）**：edit_page.py 不回填 quality，改页后须以 add_page._backfill_quality 单页回填
   （禁 compute_quality.py 无参全库跑，违 deferred re-grade）。event 建页宜 add_page.py 一次成型、避免 edit 回炉。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=176→177（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
