---
round: 18
date: 2026-07-15
type_round: 9
phase: "2.1"
current_type: organization
gene: NEW1
pages: [inquiry-committee]
result: accept
---

# GROW 2.1-B · R18 · NEW1 · organization — 建 R17 broadened 复扫补捞的 Inquiry Committee

## 本轮公告

**R18 — Phase 2.1 — NEW1 — organization — 1 页**

R17 broadened 复扫补捞的 org 候选 Inquiry Committee（queue P1）本轮建 standard 档。
建后 queue(organization)=0，organization 候选真正穷尽，进入关闭倒计时（R19 标准法确认 → R20 CLOSE）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =2 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=13, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =16 | 否 |
| 3.9 | zombie-guard（queue(current_type)==0）| queue(org)=1 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| **6** | **默认 NEW1（≤5 页 standard）** | queue(org)=1 | **触发（建 1）** |

## 页面处理记录

| # | slug | 源作(VVV) | org_type | rev | size | 引注数 | 备注 |
|---|------|-----------|----------|-----|------|--------|------|
| 1 | inquiry-committee | Topsy-Turvy (TT) | committee | p3KLGL | 2711 | 6 | John Prestice 主持的官方调查委员会；审问 J.T. Maston 逼问北极大炮秘密；获政府全权、发公告警告各大洲 |

> standard 档：Overview + Role in the Story + Members，6 条半角引注（TT-010-009 / 010-011 / 011-005 /
> 011-011 / 012-010 / 012-011），全部经 sentence_index 校验存在。含关联 wikilink
> [[J.T. Maston]] / [[North Polar Practical Association]] / [[Gun Club]]。
> add_page.py 自动回填 quality=featured（虚高，DEFERRED-REGRADE）。
> 各段 ≤400 字（散文门手工核验：max 395，Overview 首段 388）；行内引注半角 `(VVV-NNN-PPP)`。
> label 采用语料首现全名 "Inquiry Committee"，alias 补 "Committee of Inquiry"（TT-010-009-s5 首现形）。

### PN 校验 warn 说明

add_page.py 报 TT-010-011 关键词重叠 1.9%（阈值 2%，mode=warn 未阻断）。该 PN 段确含
"Inquiry Committee"（s4）与 "Secretary of the Gun Club"（s16），引文（末段综合陈述委员会与
N.P.P.A./Gun Club 对立）factual grounded，仅关键词密度低于机械阈值。standard 档接受。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 建页合规 | PASS | 经 add_page.py（无 Write/Edit 旁路）；type=organization 正确解析（pages.json 抽验）|
| G2 PN 有效性 | PASS | 全部 6 条引注 PN 经 sentence_index 校验存在；半角括号；TT-010-011 warn（非阻断，见上）|
| G3 散文门 | PASS（手工）| 各段 ≤400（max 395）；add_page.py 不强制散文门（PARK 债）|
| G4 记录完整性 | PASS | 本日志 + queue.md 消费 1 候选 + grow_state step-six→R19 |
| G5 链接密度 | PASS | 含 [[J.T. Maston]] / [[North Polar Practical Association]] / [[Gun Club]] wikilink |

## state 更新

`current_round 18→19`，`type_round 8→9`，`rounds_since_last_evv5 8→9`，
`rounds_since_last_discover 0→1`，`rounds_since_last_corpus_discover 16→17`，
`discover_streak_low` 保持 2。`current_type` 仍 organization，`last_updated_round→19`。

## 遗留问题

1. **R19 = organization SCN28（标准法，停止 broaden）**：queue(org)=0，仅用红链 + 原始 org-suffix
   确认穷尽（不再扩展模式），预期 new_candidates=0 → discover_streak_low 2→3。
2. **R20 = CLOSE+SCN28 关闭 organization**：streak 达 3 → 关闭。organization final_count=15
   （GROW 建 13 + Pilot 既有 gun-club / weldon-institute 2），current_type 转 **technology**（type_queue 首位）。
3. **GROW-JUDGMENT-R17 兑现**：R17 判断性保持 streak=2（机械应 3）以先建后闭；本轮 Inquiry Committee
   已建（distinctPN≈10 正式委员会），该判断兑现为 1 个 grounded 页面而非遗弃。留用户批量复审。
4. **Pacific Railroad place/org 归类**：仍暂定 place（queue P2），待 place 类型轮或 2.1-Z PHQ 裁定。
5. **跨类型候选留队**：queue P2 现 13 条（character/place）待各自类型轮消费。
6. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区 六项债务照旧 PARK/记录。
