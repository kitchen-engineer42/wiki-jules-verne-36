---
round: 436
date: 2026-07-20
type_round: 128
phase: "2.1"
current_type: character
gene: NEW1
pages: [robert-curtis]
result: success
---

# GROW 2.1-B · R436 · NEW1 · character — 建 Robert Curtis（The Survivors of the Chancellor 之二副兼筏上真正领袖）；开 SC2 新簇，消费第二十三批建序 146，queue 2→1

## 执行摘要

Phase 2.1-B character 第 96 建（type_round 128），消费 R434 第二十三批 discover 队列**建序 146**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 147 van-tricasse）。开 SC2 新簇（首建页）。下轮 R437 since_evv5=10 → §3(1b) EVV5。**

**Robert Curtis**（*The Survivors of the Chancellor*）——Chancellor 号二副（大副 chief officer），第一人称叙述者 Kazallon 记其「this mate, whose name is Robert Curtis」（SC2-002-003），年约三十、体健有为（SC2-004-015）。船长 Huntly 神智渐失、棉货舱阴火暗燃之际，Curtis 挺身「From this time forward, I am captain of this vessel」（SC2-012-030），领众扑火（SC2-010-005）、周济饥众（SC2-016-010）、督造木筏（SC2-026-004）、筏上自居船长（SC2-031-002）；饥困逼近相食时挺身阻止「this butchery should not be permitted」（SC2-055-018），终以海水淡辨近 Amazon 河口获救之机（SC2-056-010）。性格：真水手之沉勇（SC2-004-016）、临危清声号令（SC2-020-012）、至死不弃望（SC2-014-009 / 051-005）。关系：叙述者 Kazallon 谢其救命（SC2-036-002）、越无能船长 Huntly（SC2-008-007）、洪流中救少年 André Letourneur（SC2-025-001）、徒手镇乱党 Owen（SC2-038-016）。

**role=protagonist**。book=The Survivors of the Chancellor、first_appearance=SC2-002、affiliation 空、**label=Robert Curtis，aliases=[]**。

**18 distinct solid PN**（SC2-002-003、004-015/016、008-007、010-005、012-030、014-009、016-010、020-012、025-001、026-004、029-013、031-002、036-002、038-016、051-005、055-018、056-010）：远逾 ≥5 门、逾 12-15 目标区。全 18 引文经程序化逐字子串复核（案例敏感）+ pn_validator strict 双通过。

**方法（ultracode workflow）**：mine→verify 双阶 workflow——10 miner 子代理分片扫 SC2 53 名现章 sentence_index 抽 PN-grounded 引文（明嘱勿混 Huntly/Walter/Kazallon），10 skeptic 子代理逐组复核。产 121 候选 / 118 validated / 116 distinct PN；本页自其中择 18 条铺陈其「二副—接掌—扑火—造筏—领筏—拒相食—获救」全弧。建页前另跑 Python 逐字子串校（句首大写引式改冒号导入后全 OK）。

**查重**：exact-slug robert-curtis filesystem test -f ABSENT（bucket ro）+ registry entity/label/alias 复验 ABSENT——无既建人物页，无冲突。

**wikilink**：本页为 SC2 首建页，Relationships 四位关系人（Kazallon/Captain Huntly/André Letourneur/Owen）**均未建**，依 character-schema「非既存指称以 PN-grounded 纯文本」原则列纯文本引注、不挂悬链；Appearances 挂 [[The Survivors of the Chancellor]]（work，存，SC2-029-013）。**SC2 簇由此开纵深**。

prose-gate：add_page 初稿 0 超段（正则复核 0 over-400）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 110→**111**，registry total 1634→**1635**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 146。消费后 queue=1。**下轮 R437 since_evv5=10 → §3(1b) EVV5 复评（不消费 queue，147 van-tricasse 顺延 R438）。**

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| robert-curtis | TEx5QU | The Survivors of the Chancellor | protagonist | SC2-002 | 18 distinct | 二副—船长失能接掌—领众扑火—周济—督造木筏—筏上船长—拒相食—海水辨 Amazon 获救；沉勇/清声号令/至死不弃四母题；label Robert Curtis / alias []；SC2 首建页（关系人纯文本无悬链）；workflow mine→verify + Python 逐字校；0 超段直建；strict 首验通过；Appearances 挂 [[The Survivors of the Chancellor]] |

- **robert-curtis**：18 distinct solid PN；aliases []；character-schema 五 H2。add_page rev TEx5QU（size 3933）。quality featured 回填。pn_validator --mode strict ✓。**SC2 簇开纵深；Robert Curtis 单指无消歧冲突（明嘱区分 Huntly/Walter/Kazallon）。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Curtis 之接掌—领导—救难因果；118 validated + Python 逐字子串复核；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（正则复核）。✔
- **G3 ≥5 distinct PN**：18 solid，远逾门（逾 12-15 目标）。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（description 单引号）；role=protagonist ∈ enum；aliases=[]。✔
- **registry 一致**：total 1635 character 111 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：SC2 首建页，关系人未建→纯文本无悬链；Appearances [[The Survivors of the Chancellor]] 存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R437 起始计数）

| 字段 | R436 起始 | R437 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 436 | 437 |
| type_round | 128 | 129 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 372 | 373 |
| last_updated_round | 436 | 437 |

## 遗留问题

1. **character 页数 111**：本轮 +1（robert-curtis）。queue(character) 2→**1**（建序 146 消费；余 147 van-tricasse）。registry 全库 **1635**，unknown 0。
2. **下轮 R437 = EVV5（§3(1b)）**：since_evv5 R437 起始=10 ≥ 10 → EVV5 复评轮（不建页、不消费 queue）。复评范围：Phase 2.1-B 近 10 轮建页质量 + EHLA/SC2 两新簇首页 + 累积 Pilot 种子债（7 页 PN<5、12 页 over-400、event 13/64 <5 PN）。EVV5 后 since_evv5 归 0。**147 van-tricasse 顺延 R438 NEW1。**
3. **第二十三批消费进度**：R435 NEW1（145 joam-garral ✓）→ R436 NEW1（146 robert-curtis ✓）→ **R437 EVV5**（复评）→ R438 NEW1（147 van-tricasse）→ queue 归 0 → R439 SCN28-zombie 补第二十四批。
4. **广度里程碑**：第二十三批已开 EHLA（joam-garral）/SC2（robert-curtis）两新簇；DOSE（van-tricasse）待 R438。character 覆盖作品数 ~20→22（本轮 +SC2），R438 后 →23。
5. **回链回填债**（DEFERRED，非阻塞）：**SC2 簇开纵深**（robert-curtis→kazallon/captain-huntly/andre-letourneur/miss-herbey 反向，待各建）；EHLA 簇（joam-garral→benito-garral/torres/manoel/minha/yaquita）；承前 OC/DSCF/ACH/SC/JCE/FC 各簇。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label；（f）同名异实体人物 label；（g）RFC-0003 4-char VVV 宽度（EHLA/DSCF/DOSE，parked）。
7. **event PN 回填债 + 散文门债 + character 内容债**：承前，DEFERRED，**R437 EVV5 复评**。
8. **corpus-discover 顺延**：since_corpus=372→373（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
