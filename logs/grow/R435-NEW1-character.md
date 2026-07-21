---
round: 435
date: 2026-07-20
type_round: 127
phase: "2.1"
current_type: character
gene: NEW1
pages: [joam-garral]
result: success
---

# GROW 2.1-B · R435 · NEW1 · character — 建 Joam Garral（Eight Hundred Leagues on the Amazon 之 Amazon 庄主 / 蒙冤化名 Joam Dacosta）；开 EHLA 新簇，消费第二十三批建序 145，queue 3→2

## 执行摘要

Phase 2.1-B character 第 95 建（type_round 127），消费 R434 第二十三批 discover 队列**建序 145**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 146 robert-curtis、147 van-tricasse）。开 EHLA 新簇（首建页）。**

**Joam Garral**（*Eight Hundred Leagues on the Amazon*）——Upper Amazon 上 Iquitos 之富庶 fazenda 庄主兼家族族长，其农庄「had become one of the richest establishments on the Upper Amazon」（EHLA-003-018）；来时「without family or fortune」（EHLA-003-013），隐一重身世：实为二十余年前因 Tijuco 钻石劫案蒙冤定死、越狱化名之 **Joam Dacosta**（EHLA-020-005 / 036-019）。为洗雪旧案、不将重负遗于女儿女婿，率家乘 jangada 顺流而下自首（EHLA-020-101 / 024-044）；奸人 Torres 以能证其清白之密码文书相要挟（EHLA-022-034），终为警所捕（EHLA-020-108），受审将刑，末刻文书破译「proclaimed so absolutely the innocence of the fazender of Iquitos」而获昭雪（EHLA-039-013 / 040-001）。性格：正直坦荡（EHLA-003-035）、临刑不挠（EHLA-020-020）、宁死不逃「Joam Dacosta, innocent, will not fly!」（EHLA-037-039）、信念与虔敬支撑（EHLA-037-002）。关系：妻 Yaquita（EHLA-026-003）、子 Benito 女 Minha（EHLA-003-029）、女婿 Manoel Valdez（EHLA-004-014）、奸人 Torres（EHLA-020-053 / 037-012）。

**role=protagonist**。book=Eight Hundred Leagues on the Amazon、first_appearance=EHLA-002、affiliation 空、**label=Joam Garral，aliases=[Joam Dacosta]**（其真名，全书交替使用；registry 复验 alias 唯一无冲突）。

**19 distinct solid PN**（EHLA-003-013/018/029/035、004-014、020-005/020/053/101/108、022-034、024-044、026-003、036-019、037-002/012/039、039-013、040-001）：远逾 ≥5 门、逾 12-15 目标区。全 19 引文经程序化逐字子串复核（案例敏感）+ pn_validator strict 双通过。

**方法（ultracode workflow）**：mine→verify 双阶 workflow——10 miner 子代理分片扫 EHLA 38 名现章 sentence_index 抽 PN-grounded 引文，10 skeptic 子代理逐组复核。产 124 候选 / 122 validated / 116 distinct PN；本页自其中择 19 条最强跨五节铺陈其「隐名庄主—蒙冤—自首—受审—昭雪」全弧。建页前另跑 Python 逐字子串校（初查 3 处因句首大写失配，改用原文大写引式后全 OK）。

**查重**：exact-slug joam-garral filesystem test -f ABSENT（bucket jo）+ registry entity/label/alias（含变体 Joam Dacosta）复验 ABSENT——无既建人物页，无冲突。

**wikilink**：本页为 EHLA 首建页，Relationships 四位关系人（Yaquita/Benito/Minha/Manoel/Torres）**均未建**，依 character-schema「非既存指称以 PN-grounded 纯文本」原则列纯文本引注、不挂悬链；Appearances 挂 [[Eight Hundred Leagues on the Amazon]]（work，存，EHLA-040-001）。**EHLA 簇由此开纵深**（后续 benito-garral/torres/manoel/minha 建后回填反向链）。

prose-gate：add_page 初稿 0 超段（正则复核 0 over-400；Relationships 四 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 109→**110**，registry total 1633→**1634**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 145。消费后 queue=2 → R436 继续 NEW1（建序 146 robert-curtis）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| joam-garral | k2jV0Z | Eight Hundred Leagues on the Amazon | protagonist | EHLA-002 | 19 distinct | 隐名庄主—Tijuco 蒙冤 Dacosta—为洗冤自首—Torres 密码要挟—被捕受审—末刻文书昭雪；正直/不挠/宁死不逃/虔敬四母题；label Joam Garral / alias [Joam Dacosta]；EHLA 首建页（关系人纯文本无悬链）；workflow mine→verify + Python 逐字校；0 超段直建；strict 首验通过；Appearances 挂 [[Eight Hundred Leagues on the Amazon]] |

- **joam-garral**：19 distinct solid PN；aliases [Joam Dacosta]；character-schema 五 H2。add_page rev k2jV0Z（size 3967）。quality featured 回填。pn_validator --mode strict ✓。**EHLA 簇开纵深；Joam Garral/Dacosta 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Joam（Garral/Dacosta）之隐名—蒙冤—自首—昭雪因果；122 validated + Python 逐字子串复核；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（正则复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：19 solid，远逾门（逾 12-15 目标）。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（description 单引号）；role=protagonist ∈ enum；aliases=[Joam Dacosta]。✔
- **registry 一致**：total 1634 character 110 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias（含 Joam Dacosta）ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：EHLA 首建页，关系人未建→纯文本无悬链；Appearances [[Eight Hundred Leagues on the Amazon]] 存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R436 起始计数）

| 字段 | R435 起始 | R436 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 435 | 436 |
| type_round | 127 | 128 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 371 | 372 |
| last_updated_round | 435 | 436 |

## 遗留问题

1. **character 页数 110**：本轮 +1（joam-garral）。queue(character) 3→**2**（建序 145 消费；余 146 robert-curtis、147 van-tricasse）。registry 全库 **1634**，unknown 0。
2. **下轮 R436 = NEW1（§3(7)）**：since_evv5=9<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 146 **robert-curtis**（SC2 Chancellor 号二副兼真正领袖，protagonist，223 mentions，首现 SC2-002；开 SC2 新簇）。
3. **第二十三批消费进度**：R435 NEW1（145 joam-garral ✓）→ R436 NEW1（146 robert-curtis 待）→ **R437 = §3(1b) EVV5**（since_evv5 R437 起始=10，复评不消费）→ R438 NEW1（147 van-tricasse）→ queue 归 0 → R439 SCN28-zombie 补第二十四批。
4. **回链回填债**（DEFERRED，非阻塞）：**EHLA 簇开纵深**（joam-garral→benito-garral/torres/manoel/minha/yaquita 反向，待各建）；承 R434 清单（OC/DSCF/ACH/SC/JCE/FC 各簇 + SC2/DOSE 新簇待首建后起链）。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label；（f）同名异实体人物 label；（g）RFC-0003 4-char VVV 宽度（EHLA/DSCF/DOSE 等 4-char VVV，parked）。
6. **event PN 回填债 + 散文门债 + character 内容债**：承前，DEFERRED，下次 EVV5 **R437** 复评（本簇 EVV5 将复评 EHLA/SC2 新簇首页质量 + 累积 Pilot 种子债）。
7. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=371→372（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
