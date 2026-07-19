---
round: 271
date: 2026-07-18
type_round: 38
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R271 · SCN28-zombie · event — 僵尸勘探：queue(event)==0 触发，掘 3 候选（SI 二 + DA 一）

## 执行摘要

Phase 2.1-B event 类型第 3 次 discover（R267 后），本轮为 **SCN28-zombie**（§3(4)：queue(event)==0 触发）。
决策机 §3 逐门：(1a/1b) since_evv5=4<10 否；(2) streak=0<3 否；(3) since_discover=3<10、全局 queue≥10 否；
**(4) queue(event)==0 → SCN28-zombie 触发**。R267 三候选（建序 25-27）R268/R269/R270 全建毕，event 队列归零。

**零 event 覆盖作品重扫**（memory：claiming saturation 前须穷举重扫）：以 event 页 frontmatter `pn_anchor` 反查 VVV 覆盖，
30/35 VVV 已覆盖，**零 event 作品 = 35−30 = {AMB, DA, SI, VB, YEAR}**（5 部）。逐部核可建性：

| VVV | 作品 | 章数 | 可建性 |
|-----|------|------|--------|
| SI | The Secret of the Island（神秘岛第三部）| 20 | ★ 富矿：Nemo 之死、荒岛毁灭、Duncan 救援等多事件 |
| DA | A Drama in the Air | 1（202 段）| ★ 气球疯客掀祸-脱险单指climax |
| VB | A Voyage in a Balloon | 1（162 段）| 备选（气球升空，与 DA 题材近，暂缓）|
| AMB | The Ascent of Mont Blanc | 1（144 段）| ✗ 反思性随笔、事件弥散、难达 8 单指 PN |
| YEAR | In the Year 2889 | 1 | ✗ 未来学随笔、无离散叙事事件 |

**本轮掘 3 候选**（new_candidates=3 ≥ type_close_new_candidate_min(3) → **productive**，discover_streak_low 保持 0）：

### 建序 28 — death-of-captain-nemo（SI，SI-017）
Nemo 于 Nautilus 沉舟前弥留、口诵「God and my country!」溘然长逝，殖民者闭舱开阀令 Nautilus 沉海为其墓。
book=The Secret of the Island、location=Lincoln Island、pn_anchor=**SI-017**。
9 distinct PN 可达：SI-017-003（愿殁于 Nautilus）/012（此地就死-遗请）/021（许诺遗愿）/076（渐沉神态安详）/078（叠臂待终）/079（「God and my country」溘逝）/080（Harding 阖 Prince Dakkar 之目）/089（开阀 Nautilus 渐沉）/090（Nautilus 今为 Nemo 之墓）。
剔 Nemo 身世自述（SI-016）、殖民者后续别线。SI 无 work 页 → 建时链 [[Captain Nemo]] character 或 [[The Mysterious Island]]。

### 建序 29 — destruction-of-lincoln-island（SI，SI-019）
Franklin 火山复苏、熔岩毁殖民地、Dakkar Grotto 壁溃、气爆百里可闻、Lincoln 岛没入太平洋、仅余一孤岩。
book=The Secret of the Island、location=Lincoln Island、pn_anchor=**SI-019**。
8 distinct PN 可达：SI-018-028（喷发伴地震-岛危）/044（连爆如排炮）+ SI-019-077（熔岩毁磨坊屋舍-最后一击）/078（退守末垒）/080（Dakkar Grotto 溃-气爆百里-洋覆全岛）+ SI-020-002（孤岩三十尺-所余唯此）/003（四周皆没深渊-仅存窄岩）/007（孤岩九日-必死之势）。
剔后续 Duncan 救援（另一事件）、Nemo 之死（建序 28）别线。

### 建序 30 — the-madman-in-the-balloon（DA，DA-001）
叙事者气球升空、疯客藏身、狂列历代飞行家之死、割断吊篮索、叙事者攀网自救、暴风驱向海、锚索钩地得生。
book=A Drama in the Air、location=over Holland（Zeeland/La Gueldre）、pn_anchor=**DA-001**。
8 distinct PN 可达：DA-001-159（识破疯客）/200（疯客起立）/201（「时辰已到，我等必死」）/203（「割断这些索！」）/204（缠斗-疯客割吊篮索）/210（篮坠-攀入网眼）/214（球疾旋倾覆）/215（锚索钩隙-坠落生还）/217（醒于 Harderwick 农舍）。
剔球升技术描写、历代飞行家掌故（背景）别线。DA 有 work 页 → 链 [[A Drama in the Air]]。

**查重**：三候选 exact-slug 全 ABSENT（death-of-captain-nemo / destruction-of-lincoln-island / the-madman-in-the-balloon；
变体 nemo-death / lincoln-island-explosion / balloon-drama-over-holland 等亦 ABSENT）；无 label/alias 冲突。
**无页面新建/编辑**：registry 恒 **1517**，event 恒 42，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **==0** | **触发** |
| 5/6 | RCH2 系 | — | — |
| 7 | NEW1 | — | — |

## 页面处理记录

（discover 轮，无页面新建/编辑。产出为 queue.md 追加 3 候选建序 28-30。）

## EXIT-GATE 检查

- **G 勘探产出**：new_candidates=3 ≥ 3 → productive；三候选均逐章核 ≥8 distinct PN 可达、单指事件。✔
- **零 event 穷举重扫**：pn_anchor 反查 30/35 覆盖，零 event = {AMB,DA,SI,VB,YEAR}；SI/DA 取材，VB 备选，AMB/YEAR 判非叙事事件剔除。✔
- **查重充分**：三候选 exact-slug + 变体 ABSENT；无 alias 冲突。✔
- **registry 一致**：无建页，total 1517 event 42 unknown 0。✔
- **无越权写页**：本轮仅写 queue.md + 日志 + grow_state。✔

## 六步状态机（SCN28-zombie，grow_state 存 R272 起始计数）

| 字段 | R271 起始 | R272 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 271 | 272 |
| type_round | 37 | 38 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 0（SCN28 重置）|
| discover_streak_low | 0 | 0（productive）|
| rounds_since_last_corpus_discover | 207 | 208 |
| last_updated_round | 271 | 272 |

## 遗留问题

1. **queue(event) 0→3**（建序 28-30 播种）。registry 全库 **1517**，event 42，unknown 0。
2. **下轮 R272 = NEW1（event）**：建 queue 建序 28 **death-of-captain-nemo**（SI，SI-017）。
   since_evv5=5<10、streak=0、queue(event)=3>0 → §3(7) NEW1。**SI 3-char 无需 Note**。
   建时核 Nemo 弥留-长逝-沉舟单指、剔身世自述别线；SI 无 work 页 → 链 [[Captain Nemo]] 或 [[The Mysterious Island]]。
3. **R273 = 建序 29 destruction-of-lincoln-island；R274 = 建序 30 the-madman-in-the-balloon**。三建毕后 queue(event) 再归 0 → R275 = SCN28-zombie（余 VB 及跨作品可续掘；AMB/YEAR 判非事件）。
4. **消歧方法论四例沉淀（R256/R260/R261/R264）**：queue 锚点视为线索非定论，建时逐句复核。已积四例修正 + 四例核实无误（R265/R268/R269/R270）。
5. **event 覆盖 30/36**：建序 28-30 建毕后 SI+DA 入册 → 32/36。
6. **event PN 回填债（R244/R255/R266 EVV5）**：13/42 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）再审。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=207→208（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **零 event 作品剩余记录**：VB（备选，气球题材与 DA 近）、AMB（反思随笔）、YEAR（未来学随笔）—— 后二判非离散叙事事件，暂不入 queue。
11. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
