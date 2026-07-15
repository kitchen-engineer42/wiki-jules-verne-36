---
round: 13
date: 2026-07-15
type_round: 4
phase: "2.1"
current_type: organization
gene: NEW1
pages: [cambridge-observatory, st-louis-fur-company, royal-society, royal-institution, east-india-company]
result: accept
---

# GROW 2.1-B · R13 · NEW1 · organization — 续建（5 页 standard，队列清空）

## 本轮公告

**R13 — Phase 2.1 — NEW1 — organization — 5 页**

R12 SCN28 红链发现将 queue_size 补至 16（≥10），重启建页轮。本轮取 queue P1 剩余 5 个
organization 候选建 standard 档，organization 语料候选就此穷尽（queue(organization)=0）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（rounds_since_last_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =1 | 否 |
| 3 | SCN28（queue_size < 10 或 rounds_since_discover ≥ 10）| queue_size=16, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（rounds_since_corpus ≥ 30）| =11 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| **6** | **默认 NEW1（5 页 standard）** | — | **触发** |

## 页面处理记录

| # | slug | 源作(VVV) | org_type | rev | size | 引注数 | 备注 |
|---|------|-----------|----------|-----|------|--------|------|
| 1 | cambridge-observatory | From the Earth to the Moon (FEM) | society | ASu7qU | 2140 | 8 | Gun Club 咨询的马萨诸塞天文台；著名 10/7 复函 |
| 2 | st-louis-fur-company | The Fur Country (FC) | company | 50clsV | 1914 | 4 | Hudson's Bay 唯一美国竞争对手；仅匿名 agents 出场 |
| 3 | royal-society | Five Weeks in a Balloon (FWB) | society | rD2Q1w | 1970 | 6 | 伦敦皇家学会（与 RGS 消歧）；Barnett 为其 laureate |
| 4 | royal-institution | The Underground City (UC) | society | BfKdch | 1740 | 5 | 爱丁堡皇家研究院；James Starr 为核心成员 |
| 5 | east-india-company | Around the World in Eighty Days (AWED) | company | r6u9hK | 2072 | 5 | 统治英属印度至 Sepoy 起义；1756 起 all-powerful |

> 全部 standard 档：Overview + Role in the Story + Members，每页 ≥4 引注，含成员/关联 wikilink。
> add_page.py 自动回填 quality=featured（虚高，DEFERRED-REGRADE，见 housekeeping）。
> 各段 ≤400 字（散文门手工核验：max 359/323/343/297/317）；行内引注用半角 `(VVV-NNN-PPP)`。

### 消歧处理

- **royal-society vs royal-geographical-society**：FWB 文本混用 "Royal Society"/"Royal Society of London"
  与地理学会。本页定为伦敦皇家学会（通科），frontmatter alias `Royal Society of London`，
  Overview 明示 "distinct from the exploration-funding [[Royal Geographical Society]]"。Barnett 的
  "laureate of the Royal Society"（FC-001-027/019-047）归入本页。
- **royal-institution 双址**：AWED-001-003 提 "Royal Institution or the London Institution"（伦敦），
  UC 系列则为爱丁堡皇家研究院（President Sir W. Elphiston 驻爱丁堡，UC-009-040）。本页取语料更丰的
  UC 爱丁堡版，book=The Underground City，不并入 AWED 提及以免混淆。
- **cambridge-observatory borderline place/org**：按其"作为咨询机构/学术团体"功能定 organization（R10 已议）。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 建页合规 | PASS | 5 页均经 add_page.py（无 Write/Edit 旁路）；type=organization 正确解析（非 unknown，pages.json 抽验）|
| G2 PN 有效性 | PASS | 全部 28 条引注 PN 经 sentence_index 校验存在（脚本比对）；半角括号；sid 前三段取 paragraph PN |
| G3 散文门 | PASS（手工）| 各页单段 max 297–359 ≤400；add_page.py 不强制散文门（PARK 债），本轮手工逐页核验 |
| G4 记录完整性 | PASS | 本日志 + queue.md 消费 5 候选并标注 queue(org)=0 + grow_state step-six→R14 |
| G5 链接密度 | PASS | 每页含 wikilink（[[Gun Club]]/[[Impey Barbicane]]/[[Hudson's Bay Company]]/[[Paulina Barnett]]/[[Dr. Ferguson]]/[[James Starr]]/[[Phileas Fogg]]）|

## state 更新

`current_round 13→14`，`type_round 3→4`，`rounds_since_last_evv5 3→4`，
`rounds_since_last_discover 0→1`，`rounds_since_last_corpus_discover 11→12`，
`discover_streak_low` 保持 1。`current_type` 仍 organization，`last_updated_round→14`。

## 遗留问题

1. **R14 = organization 强制 SCN28（zombie-guard）**：queue(organization)=0 → 决策矩阵
   `queue(current_type)==0` 触发 SCN28。organization 语料 R10 corpus discover 已判穷尽、R12 红链
   净新增=0，预期本轮 new_candidates<3 → discover_streak_low 1→2。
2. **organization 关闭在即**：R14 streak→2、R15 再 SCN28 streak→3 ≥ type_close_streak → CLOSE+SCN28
   关闭 organization（final_count=10），current_type 转 technology（type_queue 首位）。
3. **跨类型候选留队**：queue P2 的 11 条 character/place 候选待各自类型轮消费。
4. **Royal Society/RGS、Royal Institution 双址、Cambridge place/org** 三处消歧已就地处理，记录于本轮。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 漏判既有页 六项债务照旧 PARK/记录。
