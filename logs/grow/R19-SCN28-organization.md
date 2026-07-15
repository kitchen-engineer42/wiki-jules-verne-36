---
round: 19
date: 2026-07-15
type_round: 10
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 0
pages: []
result: accept
---

# GROW 2.1-B · R19 · SCN28 · organization — 标准法穷尽确认（停止 broaden）

## 本轮公告

**R19 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮，标准法确认穷尽）**

R18 建 Inquiry Committee 后 queue(org)=0，zombie-guard 触 SCN28。依 R17 停止承诺，本轮
**仅用标准 discover 法**（红链 + 原始 org-suffix：Company/Club/Society/Association/Institute/
Institution/Bank，**不再扩展** committee/council/board/railway/railroad/trust 等 broadened 模式），
确认候选池穷尽。**预期 new_candidates=0 → discover_streak_low 2→3 → R20+ 关闭倒计时。**

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=13, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =17 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(organization)=0 | **触发 SCN28** |

## SCN28 — 标准法 org-suffix 复扫（原始后缀，不 broaden）

原始后缀模式命中 distinctPN≥3 的专名，逐一判定：

| distinctPN | 专名 | 判定 | 处置 |
|-----|------|------|------|
| 31 | Bay Company | 既有页碎片（"Hudson's Bay Company" 去撇号后残段，= hudsons-bay-company）| 弃 |
| 28 | Ice Bank | 误报（冰堤地物，非组织；R17 已判）| 弃 |
| 23 | Reform Club | 既有页（reform-club，Pilot 期建为 place；place/org 归类待定，见 HK）| 弃（不重建）|
| 23 | Geographical Society | 既有页碎片（"Royal Geographical Society" 去 Royal 残段，= royal-geographical-society）| 弃 |
| 3 | American Company | 误报（跨 3 书语义不一致：TT 泛指敌方；RC 实为 "Russo-American Company"；FC 泛指对手代理。非单一专名，"Russo-American Company" 单独 distinctPN=1 不达门）| 弃 |

**红链复扫**：label-aware 未解析 wikilink 扫描无新增 org 红链（R14/R17 已消费）。

| 结果 | 数值 |
|------|------|
| 标准法命中（distinctPN≥3）| 5 |
| 既有页碎片弃 | 3（Bay Company / Reform Club / Geographical Society）|
| 误报弃 | 2（Ice Bank / American Company）|
| **organization new_candidates** | **0** |
| discover_streak_low | **2→3（机械规则；候选池确已穷尽，无 judgment-hold）** |

> **穷尽确认**：标准法与 R15/R17 broadened 复扫已交叉覆盖全部 org-suffix 命中，剩余全为
> 既有页碎片或误报。organization 候选真正穷尽，streak 依机械规则 2→3，无 judgment-hold
> （与 R15/R17 不同：本轮无新达门 grounded 候选，遗弃论据不成立）。**关闭条件成立。**

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 无消费（0 候选）；grow_state step-six→R20（type_round 9→10，since_evv5 9→10，since_discover→0，streak 2→3，since_corpus 17→18）|

## state 更新

`current_round 19→20`，`type_round 9→10`，`rounds_since_last_evv5 9→10`，
`rounds_since_last_discover→0`，`discover_streak_low` **2→3**（机械规则，候选穷尽），
`rounds_since_last_corpus_discover 17→18`。`current_type` 仍 organization，`last_updated_round→20`。

## 遗留问题（R20 决策矩阵修正）

1. **R20 = EVV5（非 CLOSE）**：R18 日志曾projected R20=CLOSE，但 `rounds_since_last_evv5` 于本轮
   末达 **10 = evv5_interval**，EVV5（优先级 1）先于 CLOSE+SCN28（优先级 2）触发。R20 为
   **organization 类型 EVV5 质量抽评轮**（非 discover-due，故 plain EVV5 非 EVV5+SCN28），评后
   `since_evv5→0`，`streak` 保持 3。
2. **R21 = CLOSE+SCN28 关闭 organization**：R20 EVV5 后 since_evv5 归零，streak=3 仍 ≥3 →
   R21 触 CLOSE+SCN28。organization final_count=15（GROW 建 13 + Pilot gun-club/weldon-institute 2），
   写 closed_types（evv6_score 于 CLOSE 轮 EVV6 赋值），current_type 转 **technology**。
3. **GROW-JUDGMENT-R15/R17 兑现完毕**：两次 judgment-hold 合计多建 3 个达门 org（north-west /
   canadian-general-transportation / inquiry-committee）。本轮无 hold（候选确已穷尽）。留用户批量复审。
4. **Pacific Railroad place/org 归类**：暂定 place（queue P2），待 place 类型轮或 2.1-Z PHQ 裁定。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区 六项债务照旧 PARK/记录。
