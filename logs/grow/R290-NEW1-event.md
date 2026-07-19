---
round: 290
date: 2026-07-18
type_round: 56
phase: "2.1"
current_type: event
gene: NEW1
pages: [recovery-of-the-projectile]
result: success
---

# GROW 2.1-B · R290 · NEW1 · event — 建 The Recovery of the Projectile（Columbiad 炮弹返地溅落太平洋、Susquehanna 号打捞得三人生还，RM 第二 event）

## 执行摘要

Phase 2.1-B event 类型第 54 建（type_round 56），消费 R289 discover 队列**建序 40**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；streak=0<3；since_discover=0<10、全局 queue≥10 → §3(3) 否；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Recovery of the Projectile**（RM 第二 event，作品原仅 lunar-orbit-miss 掠月未着）——*Round the Moon* 之终局。
Columbiad 巨炮所射铝弹环月后返坠地球，于 12 月 12 日 1.17 a.m. 呼啸坠入太平洋、擦断正测深之 Susquehanna 号艏斜桅几乎沉之；
舰识为 Gun Club 炮弹，投浮标标定落点、驰 San Francisco 电告 Gun Club；携 Murchison 所制抓钩、潜水衣、压气室返，连日搜海底皆徒劳、28 日绝望；
返航之际忽见浮标现于下风舷、上悬美利坚国旗——J.T. Maston 顿悟铝弹排水二十八吨故浮于海面；划艇趋近、开破损舷窗，Barbicane/Nicholl/Michel Ardan 三人正安然弈骨牌，Ardan 高呼「Double blank！」，历环月与返坠而无恙。

**锚核（逐句复核，锚无误、framing 准确）**：R289 队列记 pn_anchor=**RM-022**（打捞高潮章），framing 为「Susquehanna 打捞浮弹得三人生还」。
逐句核 RM-020~022：坠海擦桅（RM-020-045/048/049）在测深章末；识别+标定+电告（RM-021-008/013/027）在「J.T. MASTON CALLED IN」；
搜寻徒劳→浮弹→开舱得生还弈骨牌 climax（RM-022-042/046/052/061/064/066/067）确在 **RM-022**。故 pn_anchor 保留 **RM-022**，framing 与文本相符，无需改锚、无需改 slug。跨 RM-020/021/022 取 PN。

**单指核**：全 19 distinct PN 单指炮弹返地这一连续因果（测深设定→坠海擦桅→识别「他们回来了」→议决打捞→投浮标→电告→携具返搜→搜底徒劳→见浮标国旗→顿悟其浮→开舱→三人弈骨牌生还）。
**排除**：lunar-orbit-miss（掠月未着陆，首 event 已建独立页）；测深为海底电缆之设定支线仅取定位不展开；Long's Peak 望远镜通讯之戏谑议论（RM-020-034~038）剔除；返地后 Baltimore 凯旋/巡展（RM-023）结局细节剔除。
exact-slug recovery-of-the-projectile ABSENT（变体 projectile-recovery/pacific-splashdown/susquehanna-rescue/the-floating-projectile 亦 ABSENT）。aliases [The Susquehanna Rescue, Splashdown in the Pacific, Recovery from the Ocean Bed]（避「The Projectile」——technology 页 label，无冲突）。

**VVV 2-char 核**：RM 为 2-char VVV，pn_validator --mode strict ✓，**无需 RFC-0003 Note**。

**工作页处置**：RM 有 work 页 **[[Round the Moon]]**；链回之 + [[Gun Club]]（organization 页存在）。Susquehanna/Blomsberry/Bronsfield/Maston/Barbicane/Nicholl/Ardan 无对应页，纯文本叙述（不造死链）；San Francisco 无页纯文本。
book='Round the Moon'、location='The Pacific Ocean, about a hundred leagues off the American coast'。

**逾达门 19 distinct solid PN**（跨 RM-020/021/022）：RM-020-017/022（设定）+ RM-020-045/048/049/053（坠海擦桅+识别）+ RM-021-008/013/027（议决+标定+电告）+ RM-022-006/017/024/042（携具返搜+徒劳）+ RM-022-046/052/061/064/066/067（浮标国旗+悟浮+开舱+骨牌生还）。

prose-gate：add_page 一次成型（rev gLcoKB，size 3598），Participants bullet 预置空行分隔，无合并误报；全段 ≤400；无需 edit_page 拆段。pn_validator --mode strict ✓。

event 计数 53→54，registry total 1528→**1529**，unknown 恒 0。quality 自动 featured。build_registry 仅 Robur PARK（既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| recovery-of-the-projectile | gLcoKB | Round the Moon | The Pacific Ocean, about a hundred leagues off the American coast | RM-022 | 19 distinct | 坠海-识别-标定-电告-返搜-浮弹-骨牌生还单指（跨 RM-020/021/022）；锚 RM-022 逐句核实无误、framing 准确；剔 lunar-orbit-miss(掠月 已覆盖)/海底电缆设定/望远镜通讯戏谑/Baltimore 凯旋别线；RM 2-char 无需 Note；链 [[Round the Moon]]+[[Gun Club]] |

- **recovery-of-the-projectile**：19 distinct solid PN（跨 RM-020/021/022，返地打捞）；aliases [The Susquehanna Rescue, Splashdown in the Pacific, Recovery from the Ocean Bed]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指返地打捞；lunar-orbit-miss/海底电缆/望远镜通讯/凯旋结局剔除；strict ✓。✔
- **G2 段落 ≤400 字**：add_page 一次成型，0 超段；bullet 预置空行无合并误报。✔
- **G3 ≥5 distinct PN**：19 solid（跨 RM-020/021/022），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；RM 2-char PN 渲染正常无需 Note。✔
- **registry 一致**：total 1529 event 54 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug recovery-of-the-projectile ABSENT；变体 ABSENT；aliases 无 label 冲突（避「The Projectile」technology label）。✔
- **单指核**：RM-020~022 返地因果逐句确认；打捞 climax RM-022 核实；framing 与文本相符。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R291 起始计数）

| 字段 | R290 起始 | R291 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 290 | 291 |
| type_round | 56 | 57 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 226 | 227 |
| last_updated_round | 290 | 291 |

## 遗留问题

1. **event 页数 54**：本轮 +1（RM 第二 event）。queue(event) 3→**2**（建序 40 消费；余建序 41 rescue-of-joam-dacosta / 42 the-ice-sphinx）。registry 全库 **1529**，unknown 0。
2. **下轮 R291 = NEW1（§3(7)）**：since_evv5=2<10；streak=0<3；since_discover=1<10 且全局 queue≥10；queue(event)=2>0；stub%=0 → §3(7) NEW1。建 queue 最小建序 = **建序 41 rescue-of-joam-dacosta（EHLA）**。**EHLA 4-char，建时须核 PN 渲染（RFC-0003）**；且与既有 amazon-cryptogram 分工明确（解谜 vs 临刑营救），逐句核 EHLA-038/039 临刑赦免序列。
3. **消歧方法论·framing 核实**：queue 锚点与 framing 均视为线索非定论。本轮 RM-022 锚 + framing 逐句核实均准确，无需改。教训延续（R283 改锚 / R286 改锚+改 slug）：discover framing 须建时以文本复核。
4. **event 覆盖策略**：20 单事件作品为第二事件矿脉；已建 RC/MW/MS/FF/SC2/DSCF/FC/FWB/OC/**RM** 十部。余 EHLA/AM（queue 待建）+ 其他单事件作品留后续 zombie 续掘。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一。
6. **event PN 回填债**：13/53 早期页 <5 PN，DEFERRED，R288 EVV5 记录、零消解；本轮页 19 PN 不入债。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=226→227（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；event EVV6 时须一并处理 13 页 PN 回填债。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
