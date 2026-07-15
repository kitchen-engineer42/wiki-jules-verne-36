---
round: 20
date: 2026-07-15
type_round: 11
phase: "2.1"
current_type: organization
gene: EVV5
new_candidates: null
pages: []
result: accept
---

# GROW 2.1-B · R20 · EVV5 · organization — schema 反思（周期检查，模板稳定）

## 本轮公告

**R20 — Phase 2.1 — EVV5 — organization — 0 页（schema 反思轮）**

`rounds_since_last_evv5` 于 R19 末达 10 = `evv5_interval`，EVV5（决策矩阵优先级 1b）先于
CLOSE+SCN28（优先级 2，streak=3）触发。本轮扫描 organization 全部 15 页，反思
`organization-schema` 模板是否需调整。EXIT-GATE 仅 G4。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| **1a** | **EVV5+SCN28（since_evv5≥10 且 since_discover≥10）** | since_evv5=10, since_discover=0 | 否（discover 未到期）|
| **1b** | **EVV5（since_evv5 ≥ 10）** | =10 | **触发 EVV5** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =3（本轮被 EVV5 抢占）| 否（优先级低）|

> EVV5 检查优先级高于 CLOSE（grow-state-machine.md L156），确保长期不做 EVV5 不被 CLOSE 抢占。
> streak=3 的关闭本轮让位于 EVV5，顺延至 R21。

## EVV5 — organization schema 反思

### 扫描范围：15 页（GROW 建 13 + Pilot gun-club / weldon-institute）

| 维度 | 观察 | 判定 |
|------|------|------|
| **H2 节结构** | 全 15 页均含 Overview + Role in the Story + Members；7 页加第 4 节 Activities（内容更丰）| **一致，模板稳定** |
| **PN grounding** | pn_count 4–28，standard 档均 ≥4（min=st-louis-fur-company 4）| **达标一致** |
| **散文体量** | prose_chars 1378–4076；standard 档 1378–2278，deep 档 3296–4076 | 分档合理 |
| **wikilink** | wl 1–10；均含关联 org/character 链 | 达标 |
| **org_type 填写** | 全 15 页 frontmatter 均正确填（club/company/society/committee/…）| frontmatter 一致 |

### 结论：模板稳定，无需更新

`organization-schema`（Overview / Role in the Story / Members / Activities，字段 book/org_type/
founded）在 15 页上表现一致：节结构统一、grounding 达标、分档清晰。**无结构性问题，模板不调整，
不 backfill，不写 schema RFC。**

### 发现（非结构性，记 housekeeping）

**HK-registry-typefield-not-propagated**（新记）：`build_registry.py` 生成的 pages.json 只透出
通用字段 + `book`，**未透出 `org_type`/`founded`**（15 页 frontmatter 均正确填写，但 registry
层不可见）。影响前端按 org_type 分面。属共享 memex 组件，依 RFC 停靠决策 **PARK**，本地
frontmatter 无需回填。已记入 housekeeping_queue.md P2。

**featured 虚高**（既有 HK-featured-inflation）：15 页全 featured，DEFERRED-REGRADE 照旧。

## EXIT-GATE 检查（EVV5 轮仅 G4）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；无页面新建/修改；housekeeping +1 条（registry typefield）；grow_state step-six→R21（type_round 10→11，since_evv5 10→0，since_discover 0→1，streak 保持 3，since_corpus 18→19）|

## state 更新

`current_round 20→21`，`type_round 10→11`，`rounds_since_last_evv5` **10→0**（EVV5 重置），
`rounds_since_last_discover 0→1`，`discover_streak_low` 保持 3，
`rounds_since_last_corpus_discover 18→19`。`current_type` 仍 organization，`last_updated_round→21`。

## 遗留问题

1. **R21 = CLOSE+SCN28 关闭 organization**：R20 EVV5 后 since_evv5 归零，streak=3 仍 ≥3 →
   R21 触 CLOSE+SCN28。organization final_count=15，写 closed_types（含 EVV6 质量分 evv6_score），
   type_queue 移除 organization，current_type 转 **technology**（首位），重置 type_round=0 /
   discover_streak_low=0 / rounds_since_last_evv5=0，随后为 technology 做首轮 discover。
2. **organization 模板冻结**：EVV5 判定模板稳定，technology 轮启动时以 organization 经验为参照
   建立 technology-schema Mini-Pilot（2.1-A：2–3 页 + 1 轮 EVV5）。
3. **Pacific Railroad**：暂定 place（queue P2），待 place 类型轮裁定。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
