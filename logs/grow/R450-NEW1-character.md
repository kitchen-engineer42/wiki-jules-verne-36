---
round: 450
date: 2026-07-22
type_round: 142
phase: "2.1"
current_type: character
gene: NEW1
pages: [jean-cornbutte]
result: success
---

# GROW 2.1-B · R450 · NEW1 · character — 建 Jean Cornbutte（A Winter Amid the Ice 之 Dunkirk 老船长/入北冰洋寻子）；开 WAI 新簇，消费第二十六批建序 155，queue 2→1

## 执行摘要

Phase 2.1-B character 第 105 建（type_round 142），消费建序 155。决策机 §3 首匹配 **NEW1**（since_evv5=1<10；since_discover=2<10 且 queue=2>0；stub%=0 → §3(7)）。**消费后 queue(character)=1（建序 156 james-playfair）。开 WAI 新簇（首建页）。character 破 120。**

**Jean Cornbutte**（*A Winter Amid the Ice*）——Dunkirk 老船长、自费建造 brig *Jeune-Hardie* 之船主（WAI-001-003/019）。爱子 Louis（Marie 之未婚夫）失踪北冰洋后，拒信其死、亲掌船率众入极地冰海搜寻（WAI-002-014/019、006-006、008-002）；性格：不弃望（WAI-002-016）、虔敬立誓（WAI-002-040）、决进极北（WAI-005-021）、以祷慰众（WAI-007-014）。终寻得子而己殁于坏血病、葬于极地海岸（WAI-016-006 / 014-004）——父代子死之悲弧。关系：子 Louis Cornbutte（WAI-011-050）、甥女 Marie（WAI-001-020）、忠仆 Penellan（WAI-002-022）、奸副 André Vasling（WAI-002-020）。

**role=protagonist**。book=A Winter Amid the Ice、first_appearance=WAI-001、affiliation 空、**label=Jean Cornbutte，aliases=[]**。

**16 distinct solid PN**（WAI-001-003/019/020、002-014/016/019/020/022/040、005-021、006-006、007-014、008-002、011-050、014-004、016-006）：逾门。全 16 引文程序化逐字子串复核 + strict 双通过（明嘱区分父 Jean 与子 Louis Cornbutte，同姓）。

**质量档（cap 持守）**：regrade → **standard**。featured 恒 34/674=5.1%。

**方法（workflow + 转录恢复）**：mine→verify（6+6 子代理）扫 WAI 16 章。output 迟落盘期间自 verify 转录恢复 58 valid / 54 distinct PN（后 workflow 完成复验一致）；择 16。

**查重**：exact-slug + registry label/alias ABSENT，无冲突。

**wikilink**：WAI 首建页，关系人（Louis/Marie/Penellan/Vasling）未建，PN-grounded 纯文本无悬链；Appearances 挂 [[A Winter Amid the Ice]]（work，存，WAI-014-004）。

prose-gate：0 超段。character 119→**120**，registry 1643→**1644**，覆盖作品 24→**25** 部。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| =1 | 否 |
| 3 | SCN28（since_discover≥10）| =2 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| **7** | **NEW1** | **—** | **触发** |

## 页面处理记录

- **jean-cornbutte**：rev d7pvKb（size 2874）；16 distinct solid PN；aliases []；五 H2；role=protagonist；quality standard（cap）。pn_validator --mode strict ✓。[[A Winter Amid the Ice]] 挂链；父/子消歧。**WAI 簇开纵深。**

## EXIT-GATE 检查

- **G1**：全句 sentence_index 单指 Jean（非子 Louis）；58 validated + Python 逐字校；strict ✓。✔
- **G2**：0 超段。✔　**G3**：16 distinct ≥5。✔　**G4**：add_page，未用 Write/Edit 于 pages/**。✔
- **schema**：五 H2；frontmatter 全字段（description 单引号）；role ∈ enum。✔
- **quality cap**：regrade 持守 5%；jean-cornbutte standard。✔　**registry**：total 1644 character 120 unknown 0 featured 34。✔
- **查重**：exact-slug + entity/label/alias ABSENT。✔　**wikilink**：[[A Winter Amid the Ice]] 无悬挂；关系人纯文本。✔
- **排除**：提交前 grep `butler.json|-schema.md|rfc-vernean` clean。✔

## 六步状态机（NEW1，grow_state 存 R451 起始计数）

| 字段 | R450 起始 | R451 起始 |
|------|----------|----------|
| current_round | 450 | 451 |
| type_round | 142 | 143 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 386 | 387 |
| last_updated_round | 450 | 451 |

## 遗留问题

1. **character 120**：queue(character) 2→**1**（余 156 james-playfair）。registry **1644**，featured 34（5.1%），覆盖 25 部。
2. **下轮 R451 = NEW1**：消费建序 156 **james-playfair**（BR Dolphin 号苏格兰船长/闯 Charleston 封锁线，protagonist，133 mentions，首现 BR-001；开 BR 新簇）。消费后 queue 归 0 → R452 SCN28-zombie 补第二十七批。覆盖 R451 后 →26 部。
3. **目标**：grow 至 Phase 10（GROW 终局）——Phase 2 广度扩张（R~50-500）持续中，R450/~500。
4. **PN 渲染 bug**（已定案）：本地影子为本 wiki 最终修复（RFC #562 closed）。
5. **HK / Pilot 债 / event PN 债**：DEFERRED（下次 EVV5 R458）。
6. **corpus-discover 顺延**：since_corpus=386→387。
