---
round: 434
date: 2026-07-20
type_round: 126
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R434 · SCN28-zombie · character — 第二十三批 discover：一举开 EHLA/SC2/DOSE 三部零覆盖大作之新簇（joam-garral/robert-curtis/van-tricasse），queue 0→3，since_discover 归零；广度转向

## 执行摘要

Phase 2.1-B character discover 轮（type_round 126）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十二批（建序 142-144）R431-R433 全数消费（3 建：bell/harris/isaac-hakkabut），queue 归 0，本轮触发 zombie discover。

**第二十三批 3 候选**（=3 → discover_streak_low 保持 0）——**广度转向**：前批深耕 ACH/DSCF/OC，本批一举开三部**零建页大作**之新簇，跨三作品避集中：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 145 | joam-garral | Eight Hundred Leagues on the Amazon | EHLA | EHLA-002 | protagonist | 407 | ABSENT | EHLA 开新簇 补 benito-garral/manoel/minha/fragoso/torres |
| 146 | robert-curtis | The Survivors of the Chancellor | SC2 | SC2-002 | protagonist | 223 | ABSENT | SC2 开新簇 补 monsieur-letourneur/miss-herbey/kazallon |
| 147 | van-tricasse | Doctor Ox's Experiment | DOSE | DOSE-002 | protagonist | 97 | ABSENT | DOSE 开新簇 补 doctor-ox/niklausse |

**候选说明**：
- **joam-garral**（EHLA，42 章，0 建页）——Amazon 农庄庄主兼家族族长，实为二十余年前蒙冤定罪、化名 Joam Garral 之无辜者 Joam Dacosta，为洗雪旧案率家顺 Amazon 而下，贯穿全书。407 mentions（含 Joam/Garral/Dacosta 变体）。首现 EHLA-002（sample EHLA-002-079「My father, Joam Garral, has his farm about three miles from here.」）。
- **robert-curtis**（SC2，57 章，0 建页）——Chancellor 号二副，船焚船沉、船长无能之际挺身成筏上众生还者之真正领袖。223 mentions（corpus 拼作 Curtis）。首现 SC2-002（sample SC2-002-003「...this mate, whose name is Robert Curtis...」）。
- **van-tricasse**（DOSE，17 章，0 建页）——Quiquendone 镇冷静迟缓之镇长，以冰川般优柔体现全镇昏沉，为 Doctor Ox 供氧实验所激荡者。97 mentions。首现 DOSE-002（sample DOSE-002-008「"Our predecessor," said Van Tricasse gravely...」）。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT + registry entity/label/alias（含变体 Joam Dacosta / Curtis）均 ABSENT（Python 精确复验），无冲突。全 mentions ≥97 grounded（407/223/97），足支撑 ≥12 distinct solid PN。**排除（registry-catch）**：MS 全簇八页既建（ivan-ogareff/nadia/harry-blount/alcide-jolivet/michel-strogoff/marfa-strogoff/feofar-khan/sangarre），故 MS 高频名不取；WC 之 erik/tudor-brown 既建。

**方法（ultracode workflow）**：本轮 discover 以 prospect workflow 佐研——3 子代理逐作品（EHLA/SC2/DOSE）扫全书 sentence_index 计名频、剔除 built-labels、定锚最强未建角色，并逐字兑现首现 PN 与 sample 引文。三 sample PN（EHLA-002-079 / SC2-002-003 / DOSE-002-008）均经 grep 回验逐字命中。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 145-147）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 精确复验（含变体）无冲突。✔
- **grounding**：全 3 mentions ≥97（joam-garral 407、robert-curtis 223、van-tricasse 97），均足支撑 ≥12 distinct solid PN；sample PN 逐字回验。✔
- **registry-catch 排除**：MS 全簇八页 + WC erik/tudor-brown 经 registry label EXISTS 命中既建，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R435 起始计数）

| 字段 | R434 起始 | R435 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 434 | 435 |
| type_round | 126 | 127 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 370 | 371 |
| last_updated_round | 434 | 435 |

## 遗留问题

1. **character 页数 109**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十三批建序 145-147）。registry 全库 **1633**，unknown 0。
2. **下轮 R435 = NEW1（§3(7)）**：since_evv5=8<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 145 **joam-garral**（EHLA Amazon 庄主/蒙冤 Dacosta，protagonist，407 mentions，首现 EHLA-002；开 EHLA 新簇）。**EVV5 时点**：since_evv5 R435 起始=8，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**（第二十三批 R435/R436 消费两建后，R437 EVV5，余建序 147 顺延 R438）。
3. **第二十三批消费计划**：R435 NEW1（145 joam-garral）→ R436 NEW1（146 robert-curtis）→ R437 EVV5（复评，不消费）→ R438 NEW1（147 van-tricasse）→ queue 归 0 → R439 SCN28-zombie 补第二十四批。
4. **广度里程碑**：本批一举开 EHLA（42 章）/SC2（57 章）/DOSE（17 章）三部零覆盖大作，character 覆盖作品数 ~20→23。后续可续深各新簇（EHLA torres/benito、SC2 letourneur/herbey、DOSE doctor-ox/niklausse）。
5. **回链回填债**（DEFERRED，非阻塞）：承 R433 清单（OC/DSCF/ACH/SC/JCE/FC 各簇反向链），新增 EHLA/SC2/DOSE 三新簇待首建后起链。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label；（f）同名异实体人物 label；（g）RFC-0003 4-char VVV 宽度（EHLA/DSCF 等 4-char VVV，parked）。
7. **event PN 回填债 + 散文门债 + character 内容债**：承前，DEFERRED，下次 EVV5 R437 复评。
8. **corpus-discover 顺延**：since_corpus=370→371（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
