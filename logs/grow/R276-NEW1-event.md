---
round: 276
date: 2026-07-18
type_round: 42
phase: "2.1"
current_type: event
gene: NEW1
pages: [wreck-of-the-albatross]
result: success
---

# GROW 2.1-B · R276 · NEW1 · event — 建 The Wreck of the Albatross（Prudent 窃炸药、午夜引信、爆炸毁 Albatross、万尺坠海、Robur 逆桨救生，RC）

## 执行摘要

Phase 2.1-B event 类型第 31 建（type_round 42），消费 R275 discover 队列**建序 31**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Wreck of the Albatross**（RC 第二 event，作品原仅 albatross-abduction RC-005）。被囚之 Uncle Prudent 自弹药库窃取
两磅炸药筒、藏于舱内滑柜、以慢引信定时午夜点燃；三人沿锚索逃回 Pitt Island；Albatross 修螺旋桨后返航途中
引信燃尽、爆炸撕裂船体、悬浮螺旋桨尽毁、万尺坠落；Robur 攀破舱、逆转船首桨作伞减速，然爆后八十秒残骸没入太平洋。

**锚核（本轮无精修）**：R275 队列记 pn_anchor=**RC-020**（章题「THE WRECK OF THE ALBATROSS」），逐句核 RC-019/020 两章
确为窃药-引爆-坠毁全程所在（窃药 019-034 → 地狱机器两磅 019-040 → 慢引信定时 019-043 → 午夜点燃入柜 019-055 →
引信过三分之一火星逼近 020-022 → 骇爆撕船 020-048 → 末桨停坠深渊 020-050 → 万尺坠落 020-051 → Robur 逆桨 020-052 →
八十秒残骸没入海 020-053），锚 **RC-020** 确认无误、保持。

**单指核**：全 9 distinct PN 单指 Albatross 之毁灭这一连续事件（窃药→定时→点燃→火星逼近→爆裂→失升→坠落→逆桨→没海）。
**排除**：RC-017/018 风暴过火山（另一别险）、RC-019 沿锚索逃生细节（属逃生子线，仅取与毁灭直接相关句）、Robur 追捕计划别线剔除。
exact-slug wreck-of-the-albatross ABSENT（变体 destruction-of-the-albatross/fall-of-the-albatross/albatross-destruction 亦 ABSENT）。**RC 2-char → 无需 page-top Note**。

**工作页处置**：RC 有 work 页 **[[Robur the Conqueror]]**；链回之 + [[Albatross]]（technology）+ [[Robur]]（character）+ [[Chatham Islands]]（place）。book=Robur the Conqueror、location=Pacific Ocean, near the Chatham Islands。

**恰达门 9 distinct solid PN**（跨 RC-019/020，窃药-毁灭全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | RC-019-040 | 地狱机器两磅炸药、足以碎船为齑粉、否则于坠落中毁之（机器）|
| What Happens | RC-019-034 | 前夜潜入弹药库窃得炸药筒（窃药）|
| What Happens | RC-019-043 | 取火药制慢引信、午夜点燃使爆于三四点（定时）|
| What Happens | RC-019-055 | 近午夜置炸药慢引信于榻下滑柜、点燃推回（点燃）|
| What Happens | RC-020-022 | 引信逾三分之一燃尽、火星向炸药爬行（逼近）|
| Significance | RC-020-048 | 骇人爆炸撼船、舱室成木屑、灯灭电断、悬浮桨多毁（爆裂）|
| Significance | RC-020-050 | 末悬浮桨停转、Albatross 坠入深渊（失升）|
| Significance | RC-020-051 | 八人攀残骸坠万尺、船首桨垂直仍转坠更急（坠落）|
| Significance | RC-020-052 | Robur 攀破舱逆转船首桨作伞减速（逆桨）|
| Significance | RC-020-053 | 爆后八十秒残骸尽没入太平洋波涛（没海）|

**VVV 处置**：RC 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 239/182/201 字，均 <400）。pn_validator --mode strict ✓。

event 计数 44→45，registry total 1519→**1520**，unknown 恒 0。add_page 一次成型（rev 8aZVK6，size 3235，
quality 自动 featured）。
location=Pacific Ocean, near the Chatham Islands、pn_anchor=RC-020、book=Robur the Conqueror、aliases=[Destruction of the Albatross, Fall of the Albatross]。
链 [[Robur the Conqueror]]+[[Albatross]]+[[Robur]]+[[Chatham Islands]]。
build_registry 仅 Robur PARK（alias conflict robur-the-conqueror vs robur，既有债）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| wreck-of-the-albatross | 8aZVK6 | Robur the Conqueror | Pacific Ocean, near the Chatham Islands | RC-020 | 9 distinct | 窃药-引爆-坠毁单指（炸药筒 → 慢引信 → 爆裂 → 万尺坠海）；锚 RC-020 核实无误保持；剔 RC-017/018 风暴过火山/逃生子线/追捕别线；RC 2-char 无 Note；链 [[Robur the Conqueror]]+[[Albatross]]+[[Robur]]+[[Chatham Islands]] |

- **wreck-of-the-albatross**：9 distinct solid PN（跨 RC-019/020，Albatross 毁灭全程）；aliases [Destruction of the Albatross, Fall of the Albatross]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Albatross 毁灭；风暴过火山/逃生子线/追捕别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（239/182/201，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：9 solid（跨 RC-019/020），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；RC 2-char 无需 Note。✔
- **registry 一致**：total 1520 event 45 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug wreck-of-the-albatross ABSENT；变体 ABSENT；registry label/alias sweep 无 event 覆盖（albatross-abduction 为另一事件）；无 alias 冲突。✔
- **单指核**：RC-019/020 窃药-毁灭全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R277 起始计数）

| 字段 | R276 起始 | R277 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 276 | 277 |
| type_round | 42 | 43 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 212 | 213 |
| last_updated_round | 276 | 277 |

## 遗留问题

1. **event 页数 45**：本轮 +1（RC 第二 event）。queue(event) 3→**2**（建序 31 消费，余 32/33）。registry 全库 **1520**，unknown 0。
2. **下轮 R277 = EVV5（§3(1b)）**：since_evv5=10≥10 触发质量评审。since_discover=1<10 → 非 §3(1a)，为纯 §3(1b) EVV5。
   EVV5 审 event 全类型质量，回填 PN 债（13/45 早期页 <5 PN，R244/R255/R266 累积），评 featured 合理性。
   EVV5 后 since_evv5 重置 0；若 EVV5 不建页则 R278 续 NEW1 建序 32 great-eyrie-investigation。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。四例修正（R256/R260/R261/R264）+ R272 nemo-death dup（查重失误）
   + 八例核实无误（R265/R268/R269/R270/R273/R274/**R276**）。
4. **event 覆盖策略**：零 event 作品穷尽，转掘单事件作品第二事件。queue 余建序 32（MW great-eyrie）/33（MS assault-on-irkutsk）。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债**：13/45 早期页 <5 PN，DEFERRED，R277 EVV5 审。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
8. **corpus-discover 顺延**：since_corpus=212→213（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
