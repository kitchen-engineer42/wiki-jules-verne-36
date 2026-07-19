---
round: 256
date: 2026-07-18
type_round: 22
phase: "2.1"
current_type: event
gene: NEW1
pages: [silfax-firedamp-attack]
result: success
---

# GROW 2.1-B · R256 · NEW1 · event — 建 Silfax's Firedamp Attack（Silfax 引 firedamp 毁 New Aberfoyle 未遂，UC）

## 执行摘要

Phase 2.1-B event 类型第 17 建（type_round 22），消费 R253 discover 队列**建序 17**（含重大消歧修正，见下）。
决策机 §3 首匹配 **NEW1**（R255 EVV5 reset since_evv5=0<10；streak=0<3；since_discover=2<10、全局 queue≥10；
queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

**★ 重大消歧修正（锚点 + 事件性质双改）**：R253 discover 将建序 17 记为「new-aberfoyle-explosion @ UC-005 firedamp 瓦斯爆炸」，
经逐句核查**该刻画有误**：
- UC-005-010/011/012 的「explosion」是**旧 Dochart 矿井中神秘炸柱的破坏悬疑**（Harry 闻远处爆响、发现一根矿柱被炸、
  "examined the place attacked by the explosion"、疑有人欲毁矿），属**隐身破坏者（后揭即 Silfax）设定线**，**非 firedamp 气爆**，
  且单指素材过薄（仅 010/011/012 三段核心，难达 ≥5 distinct）。
- 全书真正的 **firedamp 灾变**是 **UC-018 高潮**：Silfax 于 Nell 与 Harry 婚礼当日欲引积于穹顶的 firedamp 气毁灭 New Aberfoyle 全城，
  其驯枭衔燃芯升空点火，Nell 唤枭（Harfang）掷芯入水化解，Silfax 投湖自尽。素材丰、单指清晰。

故**改锚 UC-005→UC-018**，事件正名为 **Silfax's Firedamp Attack**（slug silfax-firedamp-attack），忠于「UC firedamp 事件」之本意而纠其误指。

gather("firedamp"/"fire-damp"/"explosion"/"Silfax"/"owl"/"dome" UC-018）。逐句核**单指该 firedamp 攻击事件**：
Silfax 引气爆矿之威胁、驯枭点火、gas 积于穹顶、千钧一发、Nell 唤枭化解、Silfax 自尽——单一（未遂）灾变事件。
**排除**：UC-005 神秘炸柱（别事件/设定线）、UC-016 Coal Town 淹没（别灾种，建序 18 另建）剔除。
exact-slug silfax-firedamp-attack ABSENT（变体 new-aberfoyle-explosion/firedamp-attack 亦 ABSENT）。**UC 2-char → 无需 page-top Note**。

**恰达门 9 distinct solid PN**（UC-018×9，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | UC-018-005 | James Starr 判「fire-maidens」实为 Silfax 可点之 firedamp 气（气源本质）|
| What Happens | UC-018-026 | Silfax 备行末次威胁、以毁全城阻婚（威胁）|
| What Happens | UC-018-027 | 白羽黑斑巨枭悬于其首、待命（凶器：驯枭）|
| What Happens | UC-018-030 | 见 Jack Ryan 泳来、Silfax 碎灯取燃芯挥舞（点火）|
| What Happens | UC-018-032 | gas 轻于空气积于穹顶、示意枭衔燃芯（firedamp 积聚）|
| Significance | UC-018-031 | James Starr 绝望中惊爆炸竟迟（千钧一发）|
| Significance | UC-018-033 | 「Another second and New Aberfoyle would be no more」（利害）|
| Significance | UC-018-035 | 枭辨 Nell 声、掷燃芯入水、落其足前（化解）|
| Significance | UC-018-037 | Silfax 复仇受挫、投湖自尽（结局）|

**VVV 处置**：UC 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过 0 超段。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 31→32，registry total 1506→**1507**，unknown 恒 0。add_page 一次成型（rev u5KVJR，size 2530，
quality 自动 featured）。
location=New Aberfoyle、pn_anchor=UC-018、book=The Underground City、aliases=[The Firedamp Attack on New Aberfoyle, The Threat to New Aberfoyle]。
链 *[[the-underground-city]]*、[[New Aberfoyle]]（Silfax、Nell、Harry Ford、James Starr、Jack Ryan 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R255 reset）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| silfax-firedamp-attack | u5KVJR | The Underground City | New Aberfoyle | UC-018 | 9 | 改锚 UC-005→UC-018（纠 R253 误指）；Silfax 引气爆矿未遂单指；剔 UC-005 炸柱、UC-016 淹没；UC 2-char 无 Note |

- **silfax-firedamp-attack**：9 distinct solid PN（UC-018，四节分配）；aliases 2 项；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Silfax firedamp 攻击；UC-005 炸柱、UC-016 淹没剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid（UC-018，9 distinct 段），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；UC 2-char 无需 Note。✔
- **registry 一致**：total 1507 event 32 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug silfax-firedamp-attack ABSENT；变体 ABSENT；非既有 31 event；无 alias 冲突。✔
- **单指核**：UC-018 逐句确认指同一 firedamp 攻击事件；UC-005/UC-016 别事件排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R257 起始计数）

| 字段 | R256 起始 | R257 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 256 | 257 |
| type_round | 22 | 23 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 192 | 193 |
| last_updated_round | 256 | 257 |

## 遗留问题

1. **event 页数 32**：本轮 +1（首个 UC event）。queue(event) 2→1（建序 18 待建）。registry 全库 **1507**，unknown 0。
2. **下轮 R257 = NEW1（event）**：since_evv5=1<10、streak=0、queue(event)=1>0 → §3(7) NEW1。
   建 queue 建序 18 **The Flooding of New Aberfoyle**（UC，UC-016）。UC 2-char，无需 Note。
   建时核 Coal Town 突遭地下水 inundation 淹没单指（UC-016-006/011/012），并核该淹没系人为预谋
   （UC-016-026「traces of explosion... premeditated by man」、UC-016-046「stanchions... partially sawn through」），与本轮 firedamp 攻击、UC-005 炸柱区分。
3. **消歧方法论沉淀**：event discover 播种时对「同名灾种」须核锚点章实际所指（UC 一书含 UC-005 炸柱悬疑 / UC-016 淹没 / UC-018 firedamp 三事件，切勿混指）。
4. **event PN 回填债（R244/R255 EVV5 记录）**：13/32 早期页 <5 PN，DEFERRED，下次 EVV5（R266 前后）或 EVV6 再审。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=192→193（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
