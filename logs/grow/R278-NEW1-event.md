---
round: 278
date: 2026-07-18
type_round: 44
phase: "2.1"
current_type: event
gene: NEW1
pages: [great-eyrie-investigation]
result: success
---

# GROW 2.1-B · R278 · NEW1 · event — 建 The Investigation of the Great Eyrie（Strock 与 Elias Smith 勘探绝壁失利，MW 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 32 建（type_round 44），消费 R275 discover 队列**建序 32**。决策机 §3 首匹配 **NEW1**
（EVV5 后 since_evv5=0<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Investigation of the Great Eyrie**（MW 第二 event，作品原仅 terror-destruction MW-017）。police inspector Strock 奉命勘探
Blue Ridge 山中传闻不可攀之 Great Eyrie 火山口——诡焰怪声惊扰乡里。与 Morganton 市长 Elias Smith 及向导 Harry Horn、
James Bruck 自 Morganton 出发，沿 Catawba 河至 Pleasant Garden；陡坡难行、峡谷不可攀、攀枝匍匐；循落石所辟裂罅上至
"slide" 顶；然百尺石壁环峰、绕行无缺无隙、终不得入；Strock 无奈弃勘、返 Washington 待续追。**首勘失利、谜团未破**。

**锚核（本轮无精修）**：R275 队列记 pn_anchor=**MW-003**（章题「THE GREAT EYRIE」，200 sents/77 paras），逐句核 MW-003
确为勘探全程所在（出发 002 → Strock 受命夺秘 028 → 峡谷不可攀攀枝匍匐 036 → 落石裂罅 054 → 至 slide 顶半十一时 057 →
百尺石壁最终峰垒 058 → 绕壁无隙可攀 064 → 弃勘无从裂地越壁 072 → 千五百尺环垣荒绝 069 → Eyrie 高五千尺传不可攀 024），锚
**MW-003** 确认无误、保持。原 queue 候选 PN（004/008/009/017/020/022/023/024）多为章首铺垫，实建时改采勘探动作序列句（036/054/057/058/064/072），单指更强。

**单指核**：全 10 distinct PN 单指 Great Eyrie 首次勘探这一连续事件（出发→受命→攀难→循罅→抵壁→绕行→弃勘）。
**排除**：MW-017 terror-destruction（Eyrie 之毁灭，已建独立页）；Robur/Terror 追猎主线剔除；后续 Washington 复命（077）属尾声，仅取与勘探直接相关句。
exact-slug great-eyrie-investigation ABSENT（变体 great-eyrie-ascent/great-eyrie-expedition/ascent-of-the-great-eyrie/great-eyrie-mystery/investigation-of-the-great-eyrie 亦 ABSENT）。**MW 2-char → 无需 page-top Note**。

**工作页处置**：MW 有 work 页 **[[The Master of the World]]**；链回之 + [[The Great Eyrie]]（place）+ [[Morganton]]（place）+ [[Pleasant Garden]]（place）+ [[Blue Ridge Mountains]]（place）。book=The Master of the World、location=The Great Eyrie, Blue Ridge Mountains, North Carolina。

**逾达门 10 distinct solid PN**（皆 MW-003，勘探全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | MW-003-024 | Eyrie 高五千尺、传闻全然不可攀、未证之说即攀登动因（缘起）|
| What Happens | MW-003-002 | 拂晓自 Morganton 出发、沿 Catawba 河、向导 Horn 与 Bruck 随行（出发）|
| What Happens | MW-003-036 | 一时后坡陡峡谷不可攀、无立足处、攀枝匍匐而进（攀难）|
| What Happens | MW-003-054 | 上至巨罅、根断石碎如雪崩扫过山侧（循罅）|
| What Happens | MW-003-057 | 循落石所辟坚土裂罅、半十一时抵 slide 上缘（登顶）|
| What Happens | MW-003-058 | 百尺外百尺高石壁矗立、最终峰垒最后屏障（抵壁）|
| Significance | MW-003-064 | 绕壁一时半、无一处缺口、无一隙可攀（绕行）|
| Significance | MW-003-072 | 无从裂地越壁、掷最后不甘一瞥而随众下山（弃勘）|
| Participants | MW-003-028 | Strock 受命自 Eyrie 之魔夺秘、以好奇之魔驱使追之（人物）|
| Setting | MW-003-069 | 环垣周千二至千五百尺、荒绝之巅唯猛禽翱翔（背景）|

**VVV 处置**：MW 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 203/221/214 字，均 <400）。pn_validator --mode strict ✓。

event 计数 45→46，registry total 1520→**1521**，unknown 恒 0。add_page 一次成型（rev uSAdPk，size 3273，
quality 自动 featured）。
location=The Great Eyrie, Blue Ridge Mountains, North Carolina、pn_anchor=MW-003、book=The Master of the World、aliases=[Ascent of the Great Eyrie, The Great Eyrie Mystery]。
链 [[The Master of the World]]+[[The Great Eyrie]]+[[Morganton]]+[[Pleasant Garden]]+[[Blue Ridge Mountains]]。
build_registry 仅 Robur PARK（alias conflict robur-the-conqueror vs robur，既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R277 reset）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| great-eyrie-investigation | uSAdPk | The Master of the World | The Great Eyrie, Blue Ridge Mountains, North Carolina | MW-003 | 10 distinct | 勘探-攀难-绝壁-弃勘单指（出发 → 攀枝匍匐 → 循罅登顶 → 绕壁无隙 → 弃勘下山）；锚 MW-003 核实无误保持；剔 MW-017 terror-destruction/Robur 追猎主线/Washington 复命尾声；MW 2-char 无 Note；链 [[The Master of the World]]+[[The Great Eyrie]]+[[Morganton]]+[[Pleasant Garden]]+[[Blue Ridge Mountains]] |

- **great-eyrie-investigation**：10 distinct solid PN（皆 MW-003，Great Eyrie 首勘全程）；aliases [Ascent of the Great Eyrie, The Great Eyrie Mystery]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Great Eyrie 首勘；terror-destruction/Robur 主线/复命尾声剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（203/221/214，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：10 solid（皆 MW-003），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；MW 2-char 无需 Note。✔
- **registry 一致**：total 1521 event 46 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug great-eyrie-investigation ABSENT；变体 5 式 ABSENT；registry sweep 'eyrie' 仅 great-eyrie(place)，无 event 覆盖；无 alias 冲突。✔
- **单指核**：MW-003 首勘全程逐句确认；锚核实无误无需精修；queue 候选 PN 多章首铺垫，改采勘探动作序列句。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R279 起始计数）

| 字段 | R278 起始 | R279 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 278 | 279 |
| type_round | 44 | 45 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 214 | 215 |
| last_updated_round | 278 | 279 |

## 遗留问题

1. **event 页数 46**：本轮 +1（MW 第二 event）。queue(event) 2→**1**（建序 32 消费，余 33）。registry 全库 **1521**，unknown 0。
2. **下轮 R279 = NEW1（§3(7)）**：since_evv5=1<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → NEW1。
   建建序 33 **assault-on-irkutsk**（MS，MS-033）。MS 2-char 无需 Note；建时核 Ogareff 叛卖 + 鞑靼夜袭 Irkutsk + Angara 火河单指、
   剔 strogoff-blinding(MS-024 已覆盖)别线；**MS-033 锚须逐句复核**（主线=叛卖/夜袭；river-of-fire PN 归属须审慎）；链 [[Irkutsk]]。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。四例修正（R256/R260/R261/R264）+ R272 nemo-death dup（查重失误）
   + 九例核实无误（R265/R268/R269/R270/R273/R274/R276/**R278**）。R278 队列候选 PN 多章首铺垫、改采动作序列句，锚 MW-003 本身无误。
4. **event 覆盖策略**：零 event 作品穷尽，转掘单事件作品第二事件。queue 余建序 33（MS assault-on-irkutsk）。建序 33 后 queue(event)=0 → 触 SCN28-zombie 再掘。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」（并可借机补 PN 至 ≥5，消一债页）；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债**：13/46 早期页 <5 PN，DEFERRED，R277 EVV5 记录、零消解；R278 新建页 10 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=214→215（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
