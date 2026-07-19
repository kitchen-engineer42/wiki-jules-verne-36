---
round: 314
date: 2026-07-19
type_round: 7
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R314 · SCN28 · character — queue 归零后第二批 discover，exhaustive re-scan 掘 6 候选建序 57-62

## 执行摘要

Phase 2.1-B character 类型 discover 轮（type_round 7）。R313 消费尽 R307 首批队列（建序 51-56），queue(character)==0。决策机 §3 首匹配 **SCN28**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0<discover_queue_threshold(10) → §3(3) SCN28 触发**；等价 §3(4) zombie，gene 皆 SCN28）。

**本轮为 discover 轮，不建页（pages: []）**。动作：exhaustive re-scan 语料补 character 候选 + append queue.md + 更新 grow_state + 写日志。registry 不变（total 1545、character 21、unknown 0）。

**exhaustive re-scan（遵 memory 规则「勿仅凭 queue 判饱和」）**：现 21 character 页覆盖各作品头部主角。逐作品扫 sentence_index，按语料 count + first-appearance 章明确性 + filesystem/registry 双查 ABSENT 三准则筛，掘第二批 **6 候选建序 57-62**：

| 建序 | slug | book | pn_anchor | role | 简述 | 语料 count |
|------|------|------|-----------|------|------|-----------|
| 57 | neb | The Mysterious Island | MI-002 | supporting | Cyrus Harding 之忠仆、Lincoln 岛第五殖民者 | MI 453 |
| 58 | gideon-spilett | The Mysterious Island | MI-002 | supporting | 战地记者、殖民者，冷静善射兼医护 | MI 452 |
| 59 | negoro | Dick Sand, A Captain at Fifteen | DSCF-002 | antagonist | 阴险葡籍船厨，篡改罗盘诱船入非洲 | DSCF 274 |
| 60 | hercules | Dick Sand, A Captain at Fifteen | DSCF-004 | supporting | 力大无穷之黑人获救者，忠勇护主 | DSCF 203 |
| 61 | glenarvan | In Search of the Castaways | SC-001 | protagonist | Duncan 号船主、寻 Grant 探险队领袖 | SC 1013 |
| 62 | michel-strogoff | Michel Strogoff | MS-004 | protagonist | 沙皇信使，穿越西伯利亚送密令 | MS 289 |

**dup-check（filesystem + registry 双查，遵 memory 规则）**：6 slug + 变体（neb/nab、gideon-spilett/spilett）全 **ABSENT**——registry type=character 命中 0；**注 cyrus-harding 已有页**（Lincoln 岛五殖民者已建 Harding，本批补 Neb/Spilett 二人，殖民者五缺 0）。

**低产判定**：new_candidates=6≥type_close_new_candidate_min(3) → **productive discover**，discover_streak_low 保持 0。**Phase 2.1 未近饱和**：character 池估 ~180-240，现 21 页 + 队列 6，远未竭；后续尚有 SC 群像（Mary Grant/Robert Grant/John Mangles/McNabbs/Thalcave/Captain Grant）、DSCF（Tom/Bat/Cousin Benedict/Mrs. Weldon）、单作品主角（Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz/Nicholl/Hans）等深池。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **queue(character)=0<10** | **触发** |
| 4 | SCN28-zombie（queue(character)==0）| ==0（等价命中，gene 同 SCN28）| — |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

> 本轮 queue==0，§3(3) 与 §3(4) 同时成立，gene 皆 SCN28（discover）。与前四轮（R310-313 queue>0 走 NEW1 消费）区别：queue 空必须 discover 补给。

## 页面处理记录

本轮为 discover 轮，无建页/编辑。动作：SCN28 character 第二批 discover（6 候选建序 57-62）+ 更新 grow_state + 写日志。

## EXIT-GATE 检查

- **discover 轮无建页**：G1-G4 页级门本轮不适用（pages: []）。✔
- **registry 一致**：total 1545 character 21 unknown 0，本轮未变。✔
- **查重充分**：6 候选 filesystem + registry 双查 ABSENT（含变体 neb/nab、gideon-spilett/spilett）。✔
- **exhaustive re-scan**：逐作品扫 sentence_index 择 count 高、首现章明确者，非仅凭 queue 判（遵 memory 规则）。✔
- **counter 语义**：SCN28 → since_discover 归 0；new_candidates=6≥3 → discover_streak_low 保持 0。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28 discover，grow_state 存 R315 起始计数）

| 字段 | R314 起始 | R315 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 314 | 315 |
| type_round | 6 | 7 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 6 | **0**（SCN28 复位）|
| discover_streak_low | 0 | 0（productive，new_candidates=6≥3）|
| rounds_since_last_corpus_discover | 250 | 251 |
| last_updated_round | 314 | 315 |

## 遗留问题

1. **character 队列补给**：R314 掘建序 57-62（6 候选），queue(character) 0→**6**。registry 全库 1545，character 21，unknown 0（本轮未建页）。
2. **下轮 R315 = NEW1（§3(7)）**：since_evv5=7<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 57（neb）。neb / Neb（book The Mysterious Island，pn_anchor MI-002，MI 2-char 无 Note）——Cyrus Harding 忠仆、Lincoln 岛第五殖民者，与既建 cyrus-harding/pencroft/herbert 同书，可 wikilink 互链。
3. **wikilink 回填契机**：本批含多同书角色（MI: neb/gideon-spilett 与既有 cyrus-harding/pencroft/herbert；SC: glenarvan 与既有 paganel），建成后可批量回填交叉 [[...]] 链，提升 MI/SC 簇内连通。
4. **EVV5 临近**：since_evv5=7，距阈值 10 尚 3 轮 → 约 R318 触发 §3(1) EVV5（模板演化评审轮）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理。
9. **corpus-discover 顺延**：since_corpus=250→251（dead 变量）。**EVV6 封存点**：Phase 2.1 关闭前回填 closed_types[].evv6_score（五类型皆 null）。featured re-grade DEFERRED。
10. **Phase 2.1 收尾判据**：character 池深（~180-240），距迭代收尾（type_queue 空 + character 候选竭）尚远；持续 NEW1 消费 + 周期 discover 补给。
