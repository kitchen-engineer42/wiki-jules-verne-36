---
round: 11
date: 2026-07-15
type_round: 1
phase: "2.1"
current_type: organization
gene: NEW1
pages: [hudsons-bay-company, royal-geographical-society, north-polar-practical-association, grand-transasiatic-railway-company, peninsular-and-oriental-company]
result: accept
---

# GROW 2.1-B · R11 · NEW1 · organization — 首批建页（5 页 standard）

## 本轮公告

**R11 — Phase 2.1 — NEW1 — organization — 5 页**

organization 类型首个建页轮。R10 SCN28 corpus discover 播种 11 候选（queue P1），
本轮从 P1 取 5 条建 standard 档 organization 页，每句 PN-grounded（源作 sentence_index）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（可建候选 < 10 或 rounds_since_discover ≥ 10）| 候选=11 ≥ 10 且 since_discover=0 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =9 | 否 |
| 4/5 | RCH2 / NEW1+RCH2 | stub%=0 | 否 |
| **6** | **默认 NEW1（5 页 standard）** | — | **触发** |

## 页面处理记录

| # | slug | 源作(VVV) | org_type | rev | size | 备注 |
|---|------|-----------|----------|-----|------|------|
| 1 | hudsons-bay-company | The Fur Country (FC) | company | RoQRXT | 4622 | 1670 特许皮货公司；Hobson 远征母体 |
| 2 | royal-geographical-society | Five Weeks in a Balloon (FWB) + Captain Hatteras (ACH) | society | fzCU0a | 4586 | 资助/表彰 Ferguson 气球与 Hatteras 极地远征 |
| 3 | north-polar-practical-association | Topsy-Turvy (TT) | company | fcPiY6 | 4124 | Gun Club 化名 Barbicane & Co. 购北极 |
| 4 | grand-transasiatic-railway-company | Adventures of a Special Correspondent (ASC) | company | SDCiAJ | 4314 | 里海—北京直达铁路公司（开通六周）|
| 5 | peninsular-and-oriental-company | Around the World in Eighty Days (AWED) | company | fANYPb | 3956 | P&O 轮船（Mongolia/Rangoon）|

> 全部 standard 档：Overview + Role in the Story + Members（含 member wikilink）+ Activities（≥4 引文）。
> add_page.py 自动回填 quality=featured（虚高，DEFERRED-REGRADE，见 housekeeping）。
> 每段 ≤400 字（散文门手工核验通过：各页 max 356–400）；实体页行内引注用半角 `(VVV-NNN-PPP)`。

### 计划变更：Reform Club 发现漏判 → P&O 顶替

R10 discover 将 **Reform Club** 列为 organization 候选（distinctPN≈23，AWED），
但建页时 add_page.py 报 `页面已存在`——`reform-club` 已作为 **`type: place`** 页存在
（Pilot 期建，featured，region=London，real_or_fictional=real）。属 R10 红链/corpus 扫描的
**发现漏判**：扫描未核对既有 place 页 label，误判为新候选。

**处置**：不重建（LAW §10 label 唯一性禁重名），不自动改类型（place↔org 归类为判断性变更，
blast-radius 涉及 place 类型未来 final_count，留待用户/PHQ 裁定，与 Cambridge Observatory 同列 borderline）。
为保持 NEW1=5 新建页，从 queue P1 顺位取 **Peninsular and Oriental Company**（AWED，distinctPN≈4，
清晰的轮船公司实体，语料充分：Mongolia/Rangoon 两船 + Peninsular Company 代理人 + 公司条例）顶替。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 建页合规 | PASS | 5 页均经 add_page.py（无 Write/Edit 旁路）；type=organization 正确解析（非 unknown）|
| G2 PN 有效性 | PASS | 每句引 sentence_index 真实 PN（sid 前三段）；半角括号；抽验 FC/FWB/ASC/AWED/TT 段号均存在 |
| G3 散文门 | PASS（手工）| 各页单段 ≤400（max 400）；add_page.py 不强制散文门（PARK 债），本轮手工逐页核验 |
| G4 记录完整性 | PASS | 本日志 + queue.md 消费 5 候选 + grow_state step-six→R12 |
| G5 链接密度 | PASS | 每页含 member wikilink（[[Phileas Fogg]]/[[Impey Barbicane]]/[[Claudius Bombarnac]] 等）|

## state 更新

`current_round 11→12`，`type_round 1→2`，`rounds_since_last_evv5 1→2`，
`rounds_since_last_discover 0→1`，`rounds_since_last_corpus_discover 9→10`，
`discover_streak_low` 保持 0。`current_type` 仍 organization，`last_updated_round→12`。

## 遗留问题

1. **R12 = organization NEW1 续建**：queue P1 剩 5 候选（Cambridge Observatory / St Louis Fur Company /
   Royal Society / Royal Institution / East India Company）。取 ≤5 建页；注意 Royal Society 与本轮
   royal-geographical-society 语料重叠（FWB 文本混用 "Royal Society"），建页时消歧内容与 label。
2. **Reform Club place/org 归类**：`reform-club` 现为 place 页。它是绅士俱乐部（组织性强），
   但作为 Pall Mall 建筑亦可视 place。与 Cambridge Observatory 并列 borderline，
   待 character 轮后或 2.1-Z PHQ 统一裁定；若改 org 需 edit_page.py 改 type 并调 place final_count。
   已记 queue 注释 + 本条。
3. **member wikilink 红链**：新页含 [[Jaspar Hobson]]/[[Paulina Barnett]]/[[Dr. Ferguson]]/[[Kennedy]]/
   [[Dr. Clawbonny]]/[[J.T. Maston]]/[[Major Noltitz]]/[[Sir Francis Cromarty]]/[[Fix]] 等，
   多数 character 页未建（character 为 type_queue 末位）。红链留待 character 类型扩张 + BLK3 wikify 解析。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias 撞名、scan_wanted_pages.py 缺失
   五项债务照旧 PARK/记录。
