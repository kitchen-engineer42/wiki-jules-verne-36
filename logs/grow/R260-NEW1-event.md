---
round: 260
date: 2026-07-18
type_round: 27
phase: "2.1"
current_type: event
gene: NEW1
pages: [kilimanjaro-cannon-shot]
result: success
---

# GROW 2.1-B · R260 · NEW1 · event — 建 The Firing of the Kilimanjaro Cannon（矿井巨炮发射欲移地轴，TT）｜含锚点修正

## 执行摘要

Phase 2.1-B event 类型第 20 建（type_round 27），消费 R258 discover 队列**建序 20**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

**⚠ 锚点修正（R256 型消歧）**：R258 discover 队列建序 20 原记 pn_anchor=**TT-004**「900 尺巨炮以 40 万磅火棉发射、欲改地轴」。
逐句核 TT-004 实为 *From the Earth to the Moon* 月射 **Columbiad**（900 尺、40 万磅火棉）之**回顾段**——是既往月球炮，非本书改地轴事件。
真正的「Kilimanjaro 改地轴巨炮」事件在 **TT-017/018/019**：Barbicane & Co. 在东非 Wamasai 的 Kilimanjaro 山体凿矿井炮（gallery/shaft，非金属炮），
装 2000 吨 melimelonite，欲以后坐力移地轴 23°28′。锚点改 **TT-018**（发射之章）。slug 保持 kilimanjaro-cannon-shot（本即指此事件）。

**单指核**：全 8 PN 单指 Kilimanjaro 矿井炮的发射及其结果（机械成功、天文失败、区域灾难）。
**排除**：TT-004 月射 Columbiad 回顾（别事件、别书情节）剔除；TT-017 中工厂/铸炮/工人调度等施工细节泛述剔除，仅取「炮之性质」「目的」两句立事件框架。
exact-slug kilimanjaro-cannon-shot ABSENT（变体 great-gun-firing/kilimanjaro-gun-shot/the-great-shot 亦 ABSENT）。**TT 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（TT-017×2 + TT-018×4 + TT-019×2，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | TT-017-008 | 非炮非臼、系凿于 Kilimanjaro 山体的矿井炮（gallery/shaft）——武器性质 |
| What Happens | TT-017-013 | Barbicane 答 Sultan：此工「将改变地球面貌」——目的 |
| What Happens | TT-018-002 | 9 月 22 日夜、午夜 Nicholl 点火巨炮——发射定时 |
| What Happens | TT-018-005 | 众人退至井口 3 km 外避空气冲击——布置 |
| What Happens | TT-018-011 | Barbicane 令「Fire」——号令 |
| What Happens | TT-018-012 | Nicholl 按钮、巨响震彻 Wamasai、2000 吨 melimelonite 爆燃——发射实况 |
| Significance | TT-019-035 | Zanzibar 电报：午夜整由 Kilimanjaro 南麓装置发射、数省毁于气浪、洋动至 Mozambique 海峡——结果与代价 |
| Significance | TT-019-021 | 日轮次晨如常西斜、其视运动无变——地轴未移（天文失败）|
| Significance | TT-019-040 | Barbicane & Co. 之试验彻底失败——定论 |

（表列 9 行含两 Significance 分述，distinct PN 计 8：TT-017-008/013、TT-018-002/005/011/012、TT-019-021/035/040 —— 实为 9 distinct，逾门。）

**VVV 处置**：TT 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 178/185/160 字，均 <400）。pn_validator --mode strict ✓。

event 计数 34→35，registry total 1509→**1510**，unknown 恒 0。add_page 一次成型（rev JA80Ho，size 3142，
quality 自动 featured）。
location=Kilimanjaro、pn_anchor=TT-018、book=Topsy-Turvy、aliases=[The Great Shot of Wamasai, The Axis-Shifting Shot]。
链 *[[topsy-turvy|Topsy-Turvy]]*、[[Kilimanjaro]]（Barbicane、Nicholl、J.T. Maston、Bali-Bali 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| kilimanjaro-cannon-shot | JA80Ho | Topsy-Turvy | Kilimanjaro | TT-018 | 9 distinct | 矿井炮发射欲移地轴单指；**锚点由 queue 误记 TT-004（月射 Columbiad 回顾）修正为 TT-018**；剔月射别事件与施工泛述；TT 2-char 无 Note |

- **kilimanjaro-cannon-shot**：9 distinct solid PN（TT-017×2 + TT-018×4 + TT-019×3，四节分配）；aliases [The Great Shot of Wamasai, The Axis-Shifting Shot]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Kilimanjaro 矿井炮发射；TT-004 月射 Columbiad 回顾剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：9 solid（TT-017/018/019），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；TT 2-char 无需 Note。✔
- **registry 一致**：total 1510 event 35 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug kilimanjaro-cannon-shot ABSENT；变体 ABSENT；非既有 34 event；无 alias 冲突。✔
- **单指核**：TT-018 发射逐句确认；TT-004 月射 Columbiad 回顾（别书别事件）排除；施工泛述排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R261 起始计数）

| 字段 | R260 起始 | R261 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 260 | 261 |
| type_round | 26 | 27 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 196 | 197 |
| last_updated_round | 260 | 261 |

## 遗留问题

1. **event 页数 35**：本轮 +1（TT 首 event）。queue(event) 2→**1**（建序 20 消费，余建序 21）。registry 全库 **1510**，unknown 0。
2. **下轮 R261 = NEW1（event）**：建 queue 建序 21 **charleston-blockade-run**（BR，BR-003）。
   since_evv5=5<10、streak=0、queue(event)=1>0 → §3(7) NEW1。BR 2-char 无需 Note。
   建时核 Dolphin 恃速强闯 Charleston 封锁线单指、剔立意/时局泛述。
   **note**：建序 21 消费后 queue(event)=0 → R262 = SCN28-zombie discover（须从未覆盖作品播 ≥3 net-new：ASC/WAI/DOSE/PL/TN/MZ 等）。
3. **消歧方法论沉淀（R256/R260）**：event discover 播种「同名巨炮/灾种」须核锚点章实指。TT 一书两炮事件：TT-004 月射 Columbiad 回顾（别书 From-Earth-to-Moon）勿与 TT-018 Kilimanjaro 改地轴炮混。queue 建序须视为线索非定论，建时逐句复核锚点。
4. **event 覆盖**：23/36 部作品含 event；本会话 +WC +TT。
5. **event PN 回填债（R244/R255 EVV5 记录）**：13/35 早期页 <5 PN，DEFERRED，下次 EVV5（约 R267）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=196→197（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
