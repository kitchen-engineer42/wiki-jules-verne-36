---
round: 16
date: 2026-07-15
type_round: 7
phase: "2.1"
current_type: organization
gene: NEW1
pages: [canadian-general-transportation-company, north-west-company]
result: accept
---

# GROW 2.1-B · R16 · NEW1 · organization — 建 R15 补捞的 2 候选

## 本轮公告

**R16 — Phase 2.1 — NEW1 — organization — 2 页**

R15 org-suffix 复扫补捞的 2 个候选（queue P1）本轮建 standard 档。建满后 queue(organization)=0，
organization 候选真正穷尽，进入关闭倒计时。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=14, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =14 | 否 |
| 3.9 | zombie-guard（queue(current_type)==0）| queue(org)=2 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| **6** | **默认 NEW1（≤5 页 standard）** | queue(org)=2 | **触发（建 2）** |

## 页面处理记录

| # | slug | 源作(VVV) | org_type | rev | size | 引注数 | 备注 |
|---|------|-----------|----------|-----|------|--------|------|
| 1 | canadian-general-transportation-company | The Waif of the Cynthia (WC) | company | quxY5d | 2218 | 6 | Cynthia 号船东公司；ex-director Joshua Churchill；Erik 寻亲主线机构 |
| 2 | north-west-company | The Fur Country (FC) | company | tFSbU7 | 2050 | 4 | 1784 蒙特利尔皮货公司；1821 被 Hudson's Bay 吸收 |

> 均 standard 档：Overview + Role in the Story + Members，每页 ≥4 引注，含关联 wikilink。
> add_page.py 自动回填 quality=featured（虚高，DEFERRED-REGRADE）。
> 各段 ≤400 字（散文门手工核验：cgtc max 350，nwc max 353）；行内引注半角 `(VVV-NNN-PPP)`。
> label 采用语料首现全名 "Canadian General Transportation Company"，alias 补简称。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 建页合规 | PASS | 2 页均经 add_page.py（无 Write/Edit 旁路）；type=organization 正确解析（pages.json 抽验）|
| G2 PN 有效性 | PASS | 全部 11 条引注 PN 经 sentence_index 校验存在；半角括号；sid 前三段取 paragraph PN |
| G3 散文门 | PASS（手工）| 各页单段 ≤400（cgtc 一段初稿 405 已拆分为 350）；add_page.py 不强制散文门（PARK 债）|
| G4 记录完整性 | PASS | 本日志 + queue.md 消费 2 候选 + grow_state step-six→R17 |
| G5 链接密度 | PASS | 含 [[The Waif of the Cynthia]] / [[Hudson's Bay Company]] / [[St Louis Fur Company]] / [[Paulina Barnett]] wikilink |

## state 更新

`current_round 16→17`，`type_round 6→7`，`rounds_since_last_evv5 6→7`，
`rounds_since_last_discover 0→1`，`rounds_since_last_corpus_discover 14→15`，
`discover_streak_low` 保持 2。`current_type` 仍 organization，`last_updated_round→17`。

## 遗留问题

1. **R17 = organization SCN28（zombie-guard）**：queue(org)=0，org-suffix 已复扫尽，红链无新增，
   预期 new_candidates=0 → discover_streak_low 2→3。
2. **R18 = CLOSE+SCN28 关闭 organization**：streak 达 3 → 关闭。organization final_count=14
   （GROW 建 12 + Pilot 既有 gun-club / weldon-institute 2），current_type 转 **technology**（type_queue 首位）。
3. **GROW-JUDGMENT-R15 复审项**：R15 判断性保持 streak=2（机械应 3）以先建后闭；本轮 2 页已建，
   该判断兑现为 2 个 grounded 页面而非遗弃。仍留用户批量复审。
4. **跨类型候选留队**：queue P2 现 12 条（character/place）待各自类型轮消费。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区（既有页 + 无链组织）六项债务照旧 PARK/记录。
