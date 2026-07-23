---
round: 479
date: 2026-07-23
type_round: 171
phase: "2.1"
current_type: character
gene: NEW1
pages: [mr-bredejord]
result: success
---

# GROW 2.1-B · R479 · NEW1 · character — 建序 175 mr-bredejord（WC Schwaryencrona 挚友/论辩律师），WC 簇达 4 页，queue 3→2

## 执行摘要

Phase 2.1-B character 建页轮（type_round 171）。§3 首匹配 **§3(7) NEW1**（since_evv5=8；streak_low=0；since_discover=0；queue=3>0）。消费建序 **175 mr-bredejord**（第三十三批首员），深耕 The Waif of the Cynthia（WC）簇，queue 3→2。

**新建 mr-bredejord**（WC，supporting，label「Mr. Bredejord」/alias「Bredejord」，首现 WC-004）：Stockholm 名律师、Schwaryencrona 之毕生挚友兼论辩对手；以怀疑论与 Pliny/Quintilian 之赌局激将考据、以盘诘之能助查、终以法律为 Erik 争得 Vandalia 矿之产权。**16 distinct PN**（WC-004…022，94 名指句精选），逐句 verbatim。

**链接**：`[[Doctor Schwaryencrona]]`/`[[Erik]]`/`[[Tudor Brown]]`（三者既建，**WC 簇达 4 页密网**）、`[[The Waif of the Cynthia]]`（work）。**schwaryencrona↔mr-bredejord 双向互链成立**（回填前批纯文本）。Professor Hochstedt（未建）→ 纯文本。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5 | since_evv5=8 | 否 |
| 2 | CLOSE | streak_low=0 | 否 |
| 3 | SCN28 | since_discover=0 | 否 |
| 4 | SCN28-zombie | queue=3 | 否 |
| **7** | **NEW1（queue>0）** | **queue=3** | **触发** |

## 页面处理记录

| 建序 | slug | book | VVV | role | distinct PN | quality | PN 校验 |
|------|------|------|-----|------|-------------|---------|---------|
| 175 | mr-bredejord | The Waif of the Cynthia | WC | supporting | 16 | featured→standard | ✓ strict |

**5 段式**：Overview（Stockholm 名律师 WC-004-043、盘诘之能 WC-009-013）→ Role（身世赌局 WC-006-023、纽约查案 WC-009-026、influence 促成远征 WC-011-057、为 Erik 争矿权 WC-022-041）→ Traits（讽辞伤人 WC-008-007、鼻烟盒之习 WC-004-055、输赌暗恼 WC-006-054）→ Relationships（[[Doctor Schwaryencrona]] 论辩挚友 WC-004-060/Pliny 赌 WC-006-060、[[Erik]] 喜其致富 WC-022-028、[[Tudor Brown]] 独疑伪图 WC-014-034）→ Appearances（[[The Waif of the Cynthia]] 晕船 WC-013-040/叹 Erik 功 WC-016-035、whist 尾声 WC-022-045）。

## EXIT-GATE 检查

- **G4**：`add_page.py mr-bredejord`（author=grow），未用 Write/Edit 于 pages/**。✔
- **verbatim**：16 quoted-PN pairs 全 substring 命中；无跨句/内引号拼接（WC-014-034 止于 rascal 前）。✔
- **over-400**：初稿 Role 一段 409 字 → 拆为二段，复检无超长。✔
- **5-H2 收敛**：完整。✔
- **PN grounding**：16 distinct PN ≥5。strict「✓」。✔
- **链接**：`[[Doctor Schwaryencrona]]`/`[[Erik]]`/`[[Tudor Brown]]`/`[[The Waif of the Cynthia]]` 全 EXISTS，无 dangling；**WC 簇 4 页密网、schwaryencrona↔mr-bredejord 双向**；Hochstedt 未建 → 纯文本。✔
- **质量帽**：regrade 后 featured **35/694（5.1%）**，mr-bredejord 落 standard。✔
- **queue 消费**：175 建毕，queue 3→2 → 下轮 R480 = NEW1（176 yaquita）。✔

## 六步状态机（NEW1，grow_state 存 R480 起始计数）

| 字段 | R479 起始 | R480 起始 |
|------|----------|----------|
| current_round | 479 | 480 |
| type_round | 171 | 172 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 415 | 416 |
| last_updated_round | 479 | 480 |

## 遗留问题

1. **character 140**：本轮 +1（mr-bredejord）。registry **1664**，featured 35（5.1%），覆盖 32 部（WC 簇 4 页：schwaryencrona/erik/tudor-brown/mr-bredejord）。
2. **下轮 R480 = NEW1**：queue=2>0 → 消费建序 176 **yaquita**（EHLA Joam 之妻/Minha 之母，supporting，109 mentions；深耕 EHLA 至 7 页，回填 minha 页 Yaquita）。
3. **深耕计划**：R480（176 yaquita）→ R481（177 hurliguerly）→ queue 归 0 → **R481 起始 since_evv5=10 → R481 = EVV5**？校验：R480 起始=9 → R480 NEW1 非 EVV5 → R481 起始=10 → **R481 = EVV5**。故 177 hurliguerly 顺延至 R482（EVV5 后），或 R481 先建再 EVV5——按 §3 首匹配，R481 起始 since_evv5=10 触发 §3(1) EVV5 优先，177 hurliguerly 顺延 R482。
4. **目标**：grow 至 Phase 10。Phase 2.1-B 广度扩张持续，R479/~500。
5. **PN 渲染 / Martin Paz alias / HK / Pilot 债 / event PN 债**：DEFERRED。
6. **corpus-discover 顺延**：since_corpus=415→416。
