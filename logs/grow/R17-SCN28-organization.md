---
round: 17
date: 2026-07-15
type_round: 8
phase: "2.1"
current_type: organization
gene: SCN28
new_candidates: 1
pages: []
result: accept
---

# GROW 2.1-B · R17 · SCN28 · organization — broadened 复扫（末轮：+1 org, +1 place）

## 本轮公告

**R17 — Phase 2.1 — SCN28 — organization — 0 页（discover 轮，末次 broadened 复扫）**

R16 后 queue(org)=0，zombie-guard 再触 SCN28。依 HK-corpus-discover-orgname-blindspot 建议，
关闭前跑一次 **broadened org-pattern 复扫**（后缀扩展至 committee/council/board/bank/railway/
railroad/trust… 等）作最终穷尽验证。**本轮为 organization 的末次 broadened 复扫**，此后不再扩展扫描。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =7 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=13, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =15 | 否 |
| **3.9** | **zombie-guard（queue(current_type)==0）** | queue(organization)=0 | **触发 SCN28** |

## SCN28 — broadened org-pattern 复扫

扩展后缀模式命中 count≥3 且无既有页的专名：

| count | 专名 | 判定 | 处置 |
|-------|------|------|------|
| 31 | Ice Bank | 误报（冰堤地物，非组织）| 弃 |
| **13** | **Inquiry Committee** | **真组织**（TT，distinctPN≈10）| **新候选 → queue P1（org）** |
| 10 | Pacific Railroad / Pacific Railway | borderline place/org（横贯铁路线路）| → queue P2（place，暂定）|
| 3 | American Union | 误报（指美国/合众国，非组织）| 弃 |
| 3 | Mana Bank | 误报（distinctPN=1，银行名单碎片）| 弃 |

**Inquiry Committee**（TT《Topsy-Turvy》，distinctPN≈10）：John Prestice 主持的正式调查委员会
（TT-010-009），审查计算家（[[J.T. Maston]]）为 Barbicane 北极方案所做的机密计算，日日催其
开口（TT-012-010）。有主席、有成员、有议事与公告职能，是明确的 organization，distinctPN 高于
多数已建 org。**建**。

**Pacific Railroad**（AWED/GM/RC，distinctPN≈10）：横贯美洲铁路，分 Central Pacific 与 Union
Pacific 两线（AWED-026-002），1867 年由总工程师 Dodge 通车（AWED-029-005）。语料以**线路/
基础设施**框架为主（"divided into two distinct lines"、"head of the Pacific Railway"），org 属性弱于
Grand Transasiatic Railway Company（后者明确为 "Railway Company" 法人）。**归 borderline place**，
入 queue P2 待 place 类型轮裁定，不作 org 建。

| 结果 | 数值 |
|------|------|
| broadened 命中（count≥3）| 6 |
| 误报弃 | 3（Ice Bank / American Union / Mana Bank）|
| **organization new_candidates** | **1（Inquiry Committee）** |
| place 候选入 P2 | 1（Pacific Railroad, borderline）|
| discover_streak_low | **保持 2（GROW-JUDGMENT-R17，见下）** |

### discover_streak_low 处置说明（GROW-JUDGMENT-R17，待用户复审）

机械规则：new_candidates(1) < 3 → streak 2→3 → R18 CLOSE 遗弃 Inquiry Committee（distinctPN≈10）。
本轮**保持 streak=2**，理由同 R15：discover 补捞出达门 grounded 候选 → 候选池未枯竭；遗弃 distinctPN≈10
的正式委员会违背广度全覆盖。

> **停止承诺**：本轮为 organization **末次 broadened 复扫**。R18 建 Inquiry Committee 后，R19 仅用
> **标准 discover 法**（红链 + 原始 org-suffix，不再扩展模式）确认穷尽 → new_candidates=0 → streak 2→3
> → R20 CLOSE 关闭 organization。此举防止无限扩展扫描 mining 长尾（committee/bank/railway 再 broaden 必有
> 更多边缘命中，须设停止点）。两次 judgment-hold（R15/R17）合计多建 3 个 distinctPN≥10 或达门 org 页。

## EXIT-GATE 检查（discover 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md P1 +Inquiry Committee，P2 +Pacific Railroad；grow_state step-six→R18（type_round 7→8，since_evv5 7→8，since_discover→0，streak 保持 2，since_corpus 15→16）|

## state 更新

`current_round 17→18`，`type_round 7→8`，`rounds_since_last_evv5 7→8`，
`rounds_since_last_discover→0`，`discover_streak_low` **保持 2**（GROW-JUDGMENT-R17），
`rounds_since_last_corpus_discover 15→16`。`current_type` 仍 organization，`last_updated_round→18`。

## 遗留问题

1. **R18 = organization NEW1 建 Inquiry Committee**（1 页 standard，TT）。
2. **R19 = organization SCN28（标准法，停止 broaden）** → 预期 new_candidates=0 → streak 2→3。
3. **R20 = CLOSE+SCN28 关闭 organization** → final_count=15，转 technology。
4. **Pacific Railroad place/org 归类**：暂定 place，待 place 类型轮或 2.1-Z PHQ 裁定；与 reform-club、
   Cambridge Observatory borderline 并列。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区 六项债务照旧 PARK/记录。
