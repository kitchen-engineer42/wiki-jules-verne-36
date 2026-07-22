---
round: 441
date: 2026-07-21
type_round: 133
phase: "2.1"
current_type: character
gene: NEW1
pages: [doctor-ox]
result: success
---

# GROW 2.1-B · R441 · NEW1 · character — 建 Doctor Ox（Doctor Ox's Experiment 题名神秘科学家/反派）；深耕 DOSE 簇 + 起 doctor-ox↔van-tricasse 反向链，消费第二十四批建序 149，queue 2→1

## 执行摘要

Phase 2.1-B character 第 99 建（type_round 133），消费 R439 第二十四批 discover 队列**建序 149**。决策机 §3 首匹配 **NEW1**（since_evv5=3<10；discover_streak_low=0；since_discover=1<10 且 queue=2>0；stub%=0 → §3(7)）。**消费后 queue(character)=1（建序 150 miss-herbey）。深耕 DOSE 簇（第 2 页）。**

**Doctor Ox**（*Doctor Ox's Experiment*）——题名神秘科学家：Europe 知名之 physiologist（DOSE-004-003），居镇外 Oudenarde 门旁实验室（DOSE-005-009）。以「自费为镇供 oxyhydric gas 照明」为幌（DOSE-003-039 / 004-009），实则借此行 physiological experiment（DOSE-004-007）——铺气管以纯氧饱和 Quiquendone 公私建筑与街衢（DOSE-017-002），激荡昏沉镇民为狂躁好战。性格：能化学兼精生理（DOSE-004-010）、冷酷超然「So much the worse for them!」（DOSE-004-019）、野心欲「reform the world」（DOSE-004-031）、暗喜实验见效（DOSE-005-050）。其助手 Gédéon Ygène（DOSE-004-006）；于镇长 [[Van Tricasse]] 之镇施术并暗察其变（DOSE-005-030）。终气厂爆炸止其实验（DOSE-015-006 / 017-006），叙述者斥其理论（DOSE-017-008）。

**role=antagonist**。book=Doctor Ox's Experiment、first_appearance=DOSE-003、affiliation 空、**label=Doctor Ox，aliases=[]**。

**16 distinct solid PN**（DOSE-003-039、004-002/003/006/007/009/010/019/031、005-009/030/050、015-006、017-002/006/008）：逾门。全 16 引文经程序化逐字子串复核 + pn_validator strict 双通过。

**质量档（cap 持守）**：add_page 回填 featured，regrade_quality --apply 按全局 top-5% 复定档——doctor-ox 未入前 34，落 **standard**。featured 恒 34/668=5.1%。

**方法（ultracode workflow）**：mine→verify 双阶——5 miner + 5 skeptic 子代理扫 DOSE 12 现章。产 46 候选 / 44 validated / 42 distinct PN；择 16 铺陈「神秘生理学家—照明为幌—纯氧实验—激荡全镇—气厂爆炸止术」全弧。

**查重**：exact-slug doctor-ox test -f ABSENT（bucket do）+ registry entity/label/alias 复验 ABSENT——无冲突。

**wikilink**：[[Van Tricasse]]（既建 R438，DOSE-005-030，**起簇内反向链**）+ [[Doctor Ox's Experiment]]（work，存，DOSE-017-008）；Ygène 未建，PN-grounded 纯文本。**DOSE 簇由单页扩为 2 页，doctor-ox↔van-tricasse 互链成型。**

prose-gate：0 超段。**引注**：strict 首验即通过。

character 计数 113→**114**，registry total 1637→**1638**，featured 恒 34，unknown 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =1 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | role | first_app | 引注 | quality | 要点 |
|------|-----|------|------|-----------|------|---------|------|
| doctor-ox | MYcz20 | Doctor Ox's Experiment | antagonist | DOSE-003 | 16 distinct | standard | 神秘生理学家—oxyhydric 照明为幌—纯氧实验激荡全镇—气厂爆炸；助手 Ygène；[[Van Tricasse]] 反向链；workflow mine→verify + Python 逐字校；regrade 落 standard（cap）；strict 通过 |

- **doctor-ox**：16 distinct solid PN；aliases []；五 H2。add_page rev MYcz20（size 3007）。regrade → standard（top-5% cap）。pn_validator --mode strict ✓。**DOSE 簇深耕；doctor-ox↔van-tricasse 互链。**

## EXIT-GATE 检查

- **G1 PN grounding**：全句源自 sentence_index 单指 Doctor Ox 之照明幌—纯氧实验—伏止因果；44 validated + Python 逐字校；strict ✓。✔
- **G2 段落 ≤400 字**：0 超门。✔
- **G3 ≥5 distinct PN**：16 solid，逾门。✔
- **G4 脚本建页**：add_page；未用 Write/Edit 于 pages/**。✔
- **schema 一致**：五 H2；frontmatter 全字段（book/description 单引号转义撇号）；role=antagonist ∈ enum。✔
- **quality cap**：regrade 持守 5% cap；doctor-ox 落 standard。✔
- **registry 一致**：total 1638 character 114 unknown 0 featured 34。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT。✔
- **wikilink 完整性**：[[Van Tricasse]] + [[Doctor Ox's Experiment]] 存在无悬挂；Ygène 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R442 起始计数）

| 字段 | R441 起始 | R442 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 441 | 442 |
| type_round | 133 | 134 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 377 | 378 |
| last_updated_round | 441 | 442 |

## 遗留问题

1. **character 页数 114**：本轮 +1（doctor-ox，standard）。queue(character) 2→**1**（余 150 miss-herbey）。registry 全库 **1638**，featured 34（5.1%）。
2. **下轮 R442 = NEW1（§3(7)）**：queue=1>0 且 since_discover=2<10 → NEW1，消费建序 150 **miss-herbey**（SC2 筏上镇定女乘客，supporting，77 mentions，首现 SC2-002；深耕 SC2 簇 + 起 miss-herbey↔robert-curtis 反向链）。消费后 queue 归 0 → R443 SCN28-zombie 补第二十五批。
3. **PN 渲染 bug**（用户 R440 提出，已处理）：本地影子插件修 localhost 预览；引擎 RFC-0003 → baojie/memex#562；详见 `logs/maint/2026-07-21-pn-render-bug.md`。
4. **回链回填债**（DEFERRED）：DOSE 簇 doctor-ox↔van-tricasse 已成、余 niklausse/ygène 待建；EHLA 簇 torres↔joam-garral 已成；SC2/OC/DSCF/ACH 各簇承前。
5. **HK / Pilot 债 / event PN 债**：承前，DEFERRED EVV6。
6. **corpus-discover 顺延**：since_corpus=377→378。
