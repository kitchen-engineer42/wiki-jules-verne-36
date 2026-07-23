---
round: 447
date: 2026-07-22
type_round: 139
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R447 · SCN28-zombie · character — 第二十六批 discover：广度转向，一举开 TN/WAI/BR 三部零覆盖新作之簇（hulda/jean-cornbutte/james-playfair），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 139）。决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=9<10；discover_streak_low=0；since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十五批（建序 151-153）R444-R446 全数消费（3 建：benito-garral/andre-letourneur/niklausse，三簇各成 3 页闭环），queue 归 0，本轮触发 zombie discover。

**第二十六批 3 候选**（=3 → discover_streak_low 保持 0）——**广度转向**：EHLA/SC2/DOSE 三簇皆成 3 页三角后，本批一举开三部**零建页新作**：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 154 | hulda | Ticket No. 9672 | TN | TN-001 | protagonist | 321 | ABSENT | TN 开新簇 补 joel/sylvius-hog/ole-kamp |
| 155 | jean-cornbutte | A Winter Amid the Ice | WAI | WAI-001 | protagonist | 151 | ABSENT | WAI 开新簇 补 penellan/louis/marie/vasling |
| 156 | james-playfair | The Blockade Runners | BR | BR-001 | protagonist | 133 | ABSENT | BR 开新簇 补 crockston/jenny-halliburtt |

**候选说明**：
- **hulda**（TN，20 章，0 建页）——Dal 客栈之贤淑挪威少女，痴候航海未婚夫 Ole Kamp 归来、持其漂流瓶所遗中彩票据者；321 mentions，首现 TN-001。label「Hulda Hansen」（消歧裸名 Hulda）。
- **jean-cornbutte**（WAI，16 章，0 建页）——Dunkirk 老船长，率 Jeune-Hardie 号众入北冰洋寻失踪爱子 Louis 者；151 mentions，首现 WAI-001。
- **james-playfair**（BR，10 章，0 建页）——Dolphin 号年轻苏格兰船长，美国南北战争中冒险闯 Charleston 封锁线者；133 mentions，首现 BR-001。

**dup-check 汇总**：3 候选 exact-slug test -f 全 ABSENT + registry entity/label/alias（含 Hulda Hansen / Cornbutte / Playfair）精确复验 ABSENT，无冲突。全 mentions ≥133（321/151/133），足支撑 ≥12 distinct solid PN。三部 work 页均存，建页 Appearances 可挂链。**排除（registry-catch）**：SI（The Secret of the Island）高频名 Harding/Pencroft/Ayrton/Cyrus/Herbert/Spilett 皆既建于 MI，故 SI 不取；MZ（Master Zacharius）题名角色与 work 同名（HK(e)），暂避（后批可取其女 Gérande）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 154-156）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：discover 轮，无建页无编辑；仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、registry 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥133（321/151/133），足支撑 ≥12 distinct solid PN。✔
- **registry-catch 排除**：SI 全簇既建于 MI；MZ 题名同 work（HK(e)）——均排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R448 起始计数）

| 字段 | R447 起始 | R448 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 447 | 448 |
| type_round | 139 | 140 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 383 | 384 |
| last_updated_round | 447 | 448 |

## 遗留问题

1. **character 页数 118**：本轮无建页（discover 轮）。queue(character) 0→**3**（第二十六批建序 154-156）。registry 全库 **1642**，featured 34（5.1%）。
2. **下轮 R448 = EVV5（§3(1b)）**：since_evv5 R448 起始=10 ≥ 10 → EVV5 复评轮（不建页、不消费 queue；since_discover=0<10 故非 EVV5+SCN28，纯 EVV5）。复评窗口 **R438–R447**（含 EHLA/SC2/DOSE 三簇 9 新页 + quality cap 落地 + workflow 转录恢复）。EVV5 后 since_evv5 归 0。**154 hulda 顺延 R449 NEW1。**
3. **广度里程碑**：第二十六批开 TN/WAI/BR 三部零覆盖新作，character 覆盖作品 23→**26** 部（建后）。
4. **消费计划**：R448 EVV5（复评）→ R449 NEW1（154 hulda）→ R450 NEW1（155 jean-cornbutte）→ R451 NEW1（156 james-playfair）→ queue 归 0 → R452 SCN28-zombie 补第二十七批。
5. **PN 渲染 bug**（已定案）：本地影子为本 wiki 最终修复；引擎多卷宽度团队推迟（RFC #562 closed）。
6. **HK / Pilot 债 / event PN 债**：承前，DEFERRED，**R448 EVV5 复评**。
7. **corpus-discover 顺延**：since_corpus=383→384。
