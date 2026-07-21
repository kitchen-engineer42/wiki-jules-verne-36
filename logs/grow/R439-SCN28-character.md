---
round: 439
date: 2026-07-21
type_round: 131
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R439 · SCN28-zombie · character — 第二十四批 discover：深耕 EHLA/SC2/DOSE 三新簇（torres/doctor-ox/miss-herbey），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 131）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；since_discover=4<10 → §3(3) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十三批（建序 145-147）R435-R438 全数消费（3 建：joam-garral/robert-curtis/van-tricasse，其中 R437 为 EVV5 复评轮不消费），queue 归 0，本轮触发 zombie discover。

**第二十四批 3 候选**（=3 → discover_streak_low 保持 0）——**深耕**上批新开之 EHLA/SC2/DOSE 三簇（各仅 1 页），各补第二簇员以脱离孤簇、起簇内网络与反向链：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 148 | torres | Eight Hundred Leagues on the Amazon | EHLA | EHLA-001 | antagonist | 331 | ABSENT | EHLA 深耕 补 joam-garral/benito-garral |
| 149 | doctor-ox | Doctor Ox's Experiment | DOSE | DOSE-003 | antagonist | 71 | ABSENT | DOSE 深耕 补 van-tricasse/niklausse |
| 150 | miss-herbey | The Survivors of the Chancellor | SC2 | SC2-002 | supporting | 77 | ABSENT | SC2 深耕 补 robert-curtis/monsieur-letourneur |

**候选说明**：
- **torres**（EHLA）——探破 Joam Garral 隐名 Dacosta 之无赖前森林警卫，持能证其清白之密码文书行敲诈之反派；331 mentions，首现 EHLA-001（EHLA-001-007）。joam-garral 页已多处引其为敌（EHLA-020-053/037-012），建页即起反向链。
- **doctor-ox**（DOSE）——题名神秘科学家，以供氧照明为幌、暗注氧气激荡 Quiquendone 全镇之反派；71 mentions（名指 52 + 「the doctor」），首现 DOSE-003（DOSE-003-035）。van-tricasse 页已述其氧激（DOSE-008-003 等），建页起反向链。
- **miss-herbey**（SC2）——Chancellor 号年轻英国女乘客，筏上众生还者间以镇定尊严为道德中心者；77 mentions，首现 SC2-002（SC2-002-006）。

**dup-check 汇总**：3 候选 exact-slug test -f 全 ABSENT + registry entity/label/alias（含 Torres/Doctor Ox/Miss Herbey）Python 精确复验 ABSENT，无冲突。全 mentions ≥71 grounded（331/77/71），足支撑 ≥12 distinct solid PN。**排除（registry-catch）**：joam-garral/robert-curtis/van-tricasse（上批 R435-R438 既建，label EXISTS）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| since_discover=4 | 否 |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 148-150）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥71（torres 331、miss-herbey 77、doctor-ox 71），均足支撑 ≥12 distinct solid PN。✔
- **registry-catch 排除**：joam-garral/robert-curtis/van-tricasse 经 registry label EXISTS 命中既建，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R440 起始计数）

| 字段 | R439 起始 | R440 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 439 | 440 |
| type_round | 131 | 132 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 375 | 376 |
| last_updated_round | 439 | 440 |

## 遗留问题

1. **character 页数 112**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十四批建序 148-150）。registry 全库 **1636**，unknown 0。
2. **下轮 R440 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 148 **torres**（EHLA 敲诈 Joam 之无赖反派，antagonist，331 mentions，首现 EHLA-001；深耕 EHLA 簇 + 起 joam-garral 反向链）。
3. **深耕转向**：第二十四批将 EHLA/SC2/DOSE 三新簇各补第二员（torres/doctor-ox/miss-herbey），令其成 ≥2 页簇、可起簇内反向链（torres↔joam-garral、doctor-ox↔van-tricasse）。
4. **质量 cap 提示**：自本批建页起，每 NEW1 轮末须追加 `local/scripts/regrade_quality.py --apply` + `build_registry.py` 以持守 featured ≤5% cap（引擎 add_page 仍回填 featured，见 `logs/maint/2026-07-21-quality-regrade.md`）。
5. **回链回填债 / HK / Pilot 债 / event PN 债**：承前，DEFERRED。
6. **corpus-discover 顺延**：since_corpus=375→376（dead 变量）。
