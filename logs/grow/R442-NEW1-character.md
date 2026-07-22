---
round: 442
date: 2026-07-21
type_round: 134
phase: "2.1"
current_type: character
gene: NEW1
pages: [miss-herbey]
result: success
---

# GROW 2.1-B · R442 · NEW1 · character — 建 Miss Herbey（The Survivors of the Chancellor 之筏上镇定女乘客）；深耕 SC2 簇 + 起 miss-herbey↔robert-curtis 反向链，消费第二十四批建序 150（末位），queue 1→0

## 执行摘要

Phase 2.1-B character 第 100 建（type_round 134），消费 R439 第二十四批 discover 队列**建序 150（末位）**。决策机 §3 首匹配 **NEW1**（since_evv5=4<10；discover_streak_low=0；since_discover=2<10 且 queue=1>0；stub%=0 → §3(7)）。**消费后 queue(character)=0（第二十四批 torres/doctor-ox/miss-herbey 3 建告罄）→ R443 = §3(4) SCN28-zombie 补第二十五批。深耕 SC2 簇（第 2 页）。**

**Miss Herbey**（*The Survivors of the Chancellor*）——年约二十之英国少女、势利善抱怨之 Mrs. Kear 的受雇女伴（SC2-002-006 / 004-018）；Chancellor 号焚沉、众登筏后成筏上道德中心：默然守职、火中救主母（SC2-013-017）、殚力侍疾（SC2-012-015）、自省口粮予人（SC2-033-008）、助葬首位罹难者（SC2-028-008）。性格：卑役不怨（SC2-004-019）、临危具「calm Christian fortitude」（SC2-028-005）、惧唯为他人（SC2-027-013）、抽死签闻名不惊（SC2-053-008）。关系：受制于 Mrs. Kear（SC2-005-019）；筏上领袖 [[Robert Curtis]] 与众从其恤命之请（SC2-054-006）；Mrs. Kear 殁后孑然（SC2-032-011），终为 Letourneur 父子收为家人（SC2-057-016）；获救时引众谢天（SC2-057-002）；末志退隐侍病苦（SC2-057-014）。

**role=supporting**。book=The Survivors of the Chancellor、first_appearance=SC2-002、affiliation 空、**label=Miss Herbey，aliases=[]**。

**16 distinct solid PN**（SC2-002-006、004-018/019、005-019、012-015、013-017、027-013、028-005/008、032-011、033-008、053-008、054-006、057-002/014/016）：逾门。全 16 引文经程序化逐字子串复核 + pn_validator strict 双通过。

**质量档（cap 持守）**：add_page 回填 featured，regrade_quality --apply 复定档——miss-herbey 未入前 34，落 **standard**。featured 恒 34/669=5.1%。

**方法（ultracode workflow）**：mine→verify 双阶——7 miner + 7 skeptic 子代理扫 SC2 40 现章（Herbey 分布稀疏）。产 58 候选 / 58 validated / 57 distinct PN；择 16 铺陈「受雇女伴—侍疾—筏上镇定虔敬—自省予人—恤命—获救志隐」全弧。

**查重**：exact-slug miss-herbey test -f ABSENT（bucket mi）+ registry entity/label/alias 复验 ABSENT——无冲突。

**wikilink**：[[Robert Curtis]]（既建 R436，SC2-054-006，**起簇内反向链**）+ [[The Survivors of the Chancellor]]（work，存，SC2-057-002）；Mrs. Kear / Letourneur 父子 未建，PN-grounded 纯文本。**SC2 簇由单页扩为 2 页，miss-herbey↔robert-curtis 互链成型。**

prose-gate：0 超段。**引注**：strict 首验即通过。

character 计数 114→**115**（**character 建页破百**：type_round 134，实 100 建），registry total 1638→**1639**，featured 恒 34，unknown 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =2 | 否 |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2（stub%≥15）| =0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 150（末位）。消费后 queue=0 → **R443 = §3(4) SCN28-zombie 补第二十五批**。

## 页面处理记录

| slug | rev | book | role | first_app | 引注 | quality | 要点 |
|------|-----|------|------|-----------|------|---------|------|
| miss-herbey | yDpOvL | The Survivors of the Chancellor | supporting | SC2-002 | 16 distinct | standard | 受雇女伴—火中救主母—侍疾—自省予人—恤命—获救志隐；[[Robert Curtis]] 反向链；Mrs. Kear/Letourneur 纯文本；workflow mine→verify + Python 逐字校；regrade 落 standard（cap）；strict 通过 |

- **miss-herbey**：16 distinct solid PN；aliases []；五 H2。add_page rev yDpOvL（size 3279）。regrade → standard（top-5% cap）。pn_validator --mode strict ✓。**SC2 簇深耕；miss-herbey↔robert-curtis 互链。**

## EXIT-GATE 检查

- **G1 PN grounding**：全句源自 sentence_index 单指 Miss Herbey；58 validated + Python 逐字校；strict ✓。✔
- **G2 段落 ≤400 字**：0 超门。✔
- **G3 ≥5 distinct PN**：16 solid，逾门。✔
- **G4 脚本建页**：add_page；未用 Write/Edit 于 pages/**。✔
- **schema 一致**：五 H2；frontmatter 全字段（description 单引号转义撇号）；role=supporting ∈ enum。✔
- **quality cap**：regrade 持守 5% cap；miss-herbey 落 standard。✔
- **registry 一致**：total 1639 character 115 unknown 0 featured 34。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT。✔
- **wikilink 完整性**：[[Robert Curtis]] + [[The Survivors of the Chancellor]] 存在无悬挂；Mrs. Kear/Letourneur 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R443 起始计数）

| 字段 | R442 起始 | R443 起始 |
|------|----------|----------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 442 | 443 |
| type_round | 134 | 135 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 378 | 379 |
| last_updated_round | 442 | 443 |

## 遗留问题

1. **character 页数 115**：本轮 +1（miss-herbey，standard）。queue(character) 1→**0**（第二十四批 148-150 三建告罄）。registry 全库 **1639**，featured 34（5.1%）。
2. **下轮 R443 = SCN28-zombie（§3(4)）**：queue(character)=0 → zombie discover 补第二十五批（3 候选；since_discover 归零）。
3. **簇成型里程碑**：第二十四批已令 EHLA/SC2/DOSE 三新簇各成 **2 页**并互链（torres↔joam-garral、miss-herbey↔robert-curtis、doctor-ox↔van-tricasse）。
4. **PN 渲染 bug**（已处理）：本地影子修 localhost；引擎 RFC-0003 → baojie/memex#562；详见 `logs/maint/2026-07-21-pn-render-bug.md`。
5. **回链回填债 / HK / Pilot 债 / event PN 债**：承前，DEFERRED EVV6。
6. **corpus-discover 顺延**：since_corpus=378→379。
