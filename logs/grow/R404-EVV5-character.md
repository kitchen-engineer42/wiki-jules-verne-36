---
round: 404
date: 2026-07-19
type_round: 96
phase: "2.1"
current_type: character
gene: EVV5
pages: []
result: success
---

# GROW 2.1-B · R404 · EVV5 · character — 全 88 页 schema 反射：结构三指标全通过（5 H2 精确 / role∈enum / book 非空），内容债恒定 7 PN<5 + 12 over-400（Pilot 种子 DEFERRED），since_evv5 归零

## 执行摘要

Phase 2.1-B character EVV5 schema 反射轮（type_round 96）。决策机 §3 首匹配 **§3(1b) EVV5**
（since_evv5=10≥10 → §3(1b) 触发；since_discover=0<10 → 非 §3(1a) EVV5+SCN28 合并轮）。**pages:[]，仅 G4，不消费队列**，since_evv5 归 0。

EVV5 为周期性（interval=10）schema 反射轮：扫全 character（**88 页**）3 结构指标 + 2 内容债指标，不建页不编辑。自上次 EVV5（R393，78 页）以来新建 10 页（R394-R402：phina-hollaney/madge/thomas-black/taskinar/dick-kennedy 等 + 既有），本轮复评全库结构合规性。

## 扫描结果（88 页）

### 结构三指标（硬门，须全通过）

| 指标 | 判定 | 违规数 |
|------|------|--------|
| 5 H2 精确匹配（Overview / Role in the Story / Character & Traits / Relationships / Appearances）| ✔ | **0** |
| role ∈ enum {protagonist, antagonist, supporting, narrator} | ✔ | **0** |
| book 非空 | ✔ | **0** |

**role 分布**：supporting 58、protagonist 14、antagonist 12、narrator 4（合计 88）。

> **扫描教训（本轮捕获）**：首扫读 pages.json 顶层 `v.get('role')` → 全空（role 存于 .md frontmatter 而非 registry 顶层），误报 bad_role=88。改解析各页 `^role:` frontmatter 行 → bad_role=0。**role 位于 frontmatter，registry 顶层无此字段**，EVV5 扫描须解析页文件本体。

### 内容债二指标（软门，DEFERRED backfill）

| 指标 | 违规数 | 明细 |
|------|--------|------|
| ≥5 distinct solid PN | **7** | aouda(3)、barbicane(3)、passepartout(3)、axel(4)、conseil(4)、ned-land(4)、top(4) |
| prose ≤400 字 | **12** | aouda、axel、barbicane、captain-hatteras、captain-nemo、cyrus-harding、fix、ned-land、passepartout、phileas-fogg、professor-lidenbrock、top |

**内容债恒定**：7 PN<5 + 12 over-400 与 R393 EVV5 完全一致，**均 Pilot 种子页**，无新增。自 R393 以来新建 10 页（含 R394-R402 各建）**全数 12-14 distinct PN、0 over-400**，未贡献任何新债。DEFERRED backfill（Phase 2.1 EVV6 或专项回填轮统一处理）。

## 决策矩阵（EVV5）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10、since_discover=0 | 否（since_discover<10）|
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | （被 §3(1b) 先匹配）|
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

EVV5 为 schema 反射轮，无建页、无编辑（仅 G4）。产出全库扫描报告，不改动任何页面文件，不消费 queue（第十六批建序 124-126 保留）。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为反射轮，无建页无编辑；仅更新 grow_state + 写日志，未用 Write/Edit 于 pages/**。✔
- **结构合规**：88 页 5 H2 精确 / role∈enum / book 非空 三指标全通过（违规 0/0/0）。✔
- **内容债追踪**：7 PN<5 + 12 over-400，与 R393 恒定，均 Pilot 种子，DEFERRED。自 R393 新建 10 页无新债。✔
- **role 分布**：supporting 58 / protagonist 14 / antagonist 12 / narrator 4 = 88，全 ∈ enum。✔
- **不消费队列**：第十六批建序 124-126 保留，R405 起消费。✔
- **since_evv5 归零**：10→0。✔

## 六步状态机（EVV5，grow_state 存 R405 起始计数）

| 字段 | R404 起始 | R405 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 404 | 405 |
| type_round | 96 | 97 |
| rounds_since_last_evv5 | 10 | 0（EVV5 归零）|
| rounds_since_last_discover | 0 | 1（EVV5 非 SCN28/CLOSE，+1）|
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 340 | 341 |
| last_updated_round | 404 | 405 |

## 遗留问题

1. **character 页数 88（本轮无建）**：queue(character)=3（第十六批建序 124-126 未消费）。registry 全库 **1612**，unknown 0。
2. **下轮 R405 = NEW1（§3(7)）**：since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1，消费建序 124 **samuel-fergusson**（FWB 主角，role=protagonist，可回链 [[Dick Kennedy]]/[[Five Weeks in a Balloon]]）。
3. **第十六批消费自 R405 起**：R405 NEW1（124 samuel-fergusson）→ R406 NEW1（125 mac-nab）→ R407 NEW1（126 hans-bjelke）→ queue 归 0 → R408 SCN28-zombie 补第十七批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + dick-kennedy↔samuel-fergusson（待建，双向）、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。JCE 新建 hans-bjelke 可回链 professor-lidenbrock/axel。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT 即此类）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（本轮 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5（R414）复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=340→341（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
