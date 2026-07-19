---
round: 275
date: 2026-07-18
type_round: 41
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R275 · SCN28-zombie · event — 僵尸勘探（零 event 池穷尽，转掘单事件作品之第二事件，播种建序 31-33）

## 执行摘要

Phase 2.1-B event 类型第 41 轮（type_round 41），queue(event)==0 触发 **SCN28-zombie** 勘探。
决策机 §3 首匹配 **§3(4)**（since_evv5=8<10；streak=0<3；since_discover=3<10、全局 queue≥10 → §3(3) 否；
**queue(event)==0 → §3(4) 触发**）。

**本轮无建页**，仅播种候选。前置已完成 DEDUP 更正（见 `R275-DEDUP-correction.md`：移除重复页
death-of-captain-nemo，event 45→44、total 1520→1519）。

**策略转向——零 event 作品池穷尽**：

| VVV | 作品 | 判定 |
|-----|------|------|
| SI | The Secret of the Island | =MI 第三部别译，已覆盖 → 不再掘 |
| VB | A Voyage in a Balloon | =DA 别译副本（17 处重合）→ 不再掘 |
| AMB | （反思随笔）| 非离散叙事事件 → 剔 |
| YEAR | （未来学随笔）| 非离散叙事事件 → 剔 |

零 event 作品已无可掘。改掘**单事件作品之第二事件**（RC/MW/MS 各现仅 1 event）。

## 播种候选（建序 31-33）

| 建序 | slug | anchor | 作品（现有 event）| 事件 | aliases | 链 |
|------|------|--------|------------------|------|---------|-----|
| 31 | wreck-of-the-albatross | RC-020 | Robur the Conqueror（albatross-abduction RC-005）| Prudent 炸药毁 Albatross、万尺坠海、Robur 众以桨翼逃生 | [Destruction of the Albatross, Fall of the Albatross] | [[Albatross]] |
| 32 | great-eyrie-investigation | MW-003 | Master of the World（terror-destruction MW-017）| Strock 勘探 Blue Ridge 不可攀之 Great Eyrie 火山口、诡焰怪声之谜 | [Ascent of the Great Eyrie, The Great Eyrie Mystery] | [[The Great Eyrie]] |
| 33 | assault-on-irkutsk | MS-033 | Michael Strogoff（strogoff-blinding MS-024）| Ogareff 内应叛谋、鞑靼夜袭 Irkutsk、Angara 火河 | [Defense of Irkutsk, The River of Fire] | [[Irkutsk]] |

**锚核充分性**：RC-020 章题「THE WRECK OF THE ALBATROSS」（194+126 sents，含窃药 RC-019-039/炸药如鱼雷 020-008/
万尺坠落 020-051/残骸没海 020-053）；MW-003 章题「THE GREAT EYRIE」（200 sents/77 paras）；
MS-033（215 sents/71 paras，Ogareff 叛谋+火河，邻章 032/034 可补）。三者 ≥8 distinct PN 均充裕可达。

**dup-check（filesystem，全 bucket + registry sweep）**：

- 三 exact-slug + 全变体（albatross-destruction/fall-of-the-albatross、great-eyrie-mystery/ascent/exploration、
  defense-of-irkutsk/siege-of-irkutsk/tartar-assault-on-irkutsk/irkutsk-river-of-fire）逐一 `ls docs/wiki/pages/*/` **全 ABSENT**。
- registry label/alias sweep：'albatross'→albatross-abduction(RC-005 event)+albatross(technology)；'eyrie'→great-eyrie(place)；
  'irkutsk'→irkutsk(place)+MS-ch31(chapter)。**三事件均无既有 event 覆盖**——place/technology 页非事件，本候选为对应事件页，链回之。
- 教训落实（R272 nemo-death 误判）：本轮每候选 slug+变体+alias 皆实际 filesystem 核，无凭空 ABSENT。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系 | stub%=0 | 否 |
| 7 | NEW1 | — | — |

new_candidates=3 ≥ type_close_new_candidate_min(3) → **productive**，discover_streak_low 保持 0。

## EXIT-GATE 检查

- **discover 充分性**：3 候选 ≥ min(3)，productive。✔
- **查重充分**：三 slug + 全变体 filesystem ABSENT；registry label/alias sweep 无 event 覆盖；教训落实逐一核。✔
- **锚核**：三 anchor 章题/密度确认 ≥8 distinct PN 可达；锚为线索非定论，建时逐句复核。✔
- **无建页**：本轮 discover-only，未用 add_page/Write/Edit 于 pages/**。✔
- **registry 一致**：total 1519 event 44 unknown 0（DEDUP 后）；仅 Robur PARK。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie discover，grow_state 存 R276 起始计数）

| 字段 | R275 起始 | R276 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 275 | 276 |
| type_round | 41 | 42 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | **0**（discover 重置）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 211 | 212 |
| last_updated_round | 275 | 276 |

## 遗留问题

1. **queue(event) 0→3**（建序 31-33 播种）。registry total 1519、event 44、unknown 0。
2. **下轮 R276 = NEW1（event）**：建 queue 建序 31 **wreck-of-the-albatross**（RC，RC-020）。
   since_evv5=9<10、streak=0、queue(event)=3>0 → §3(7) NEW1。RC 2-char 无需 Note。
   建时核窃药-引爆-坠毁-逃生单指、剔风暴过火山(RC-017/018)别线；链 [[Albatross]]。
   **注**：next EVV5 约 R277（since_evv5 至 R277 达 10）；R276 建页轮后 R277 触发 §3(1b) EVV5。
3. **消歧方法论**：queue 锚点视为线索非定论，建时逐句复核。四例修正（R256/R260/R261/R264/**R272 nemo-death dup**）
   + 七例核实无误（R265/R268/R269/R270/R272-建/R273/R274）。R272 dup 为**查重**失误（非锚点消歧），教训：变体/alias 逐一 filesystem 核。
4. **event 覆盖策略更新**：零 event 作品穷尽，转掘单事件作品第二事件。单事件作品富矿：RC/MW/MS/DSCF/FWB/FC 等。
5. **HK 待批（R275 DEDUP 遗留）**：（a）nemo-death 并 alias「Death of Prince Dakkar」；（b）destruction-of-lincoln-island book SI→MI 归一。
6. **event PN 回填债（R244/R255/R266 EVV5）**：13/44 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）再审。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=211→212（dead 变量）。
9. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
