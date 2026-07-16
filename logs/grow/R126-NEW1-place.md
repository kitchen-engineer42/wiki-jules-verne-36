---
round: 126
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [salt-lake-city, charleston, richmond, washington]
result: success
---

## 执行摘要

Phase 2.1-B place 广度扩张第 97 轮（type_round 97）。决策机 §3 首匹配裁定 **NEW1**：
queue=11≥10（非 discover 触发）、since_evv5=9<10（未达 EVV5）、discover_streak_low=0（无关闭倒计时）、
since_discover=3<10、queue(place)≠0（非僵尸）、stub%=0（非 RCH2）→ 落 §3(7) NEW1 默认分支。

本轮从 place 候选池取 5 名建页，**实建 4 页**：候选 Amsterdam 经建前消歧证实为陷阱
（岛义 amsterdam-island 已于 R45 建成，荷兰城真城确指 <5 门），故未建，仅建其余 4 名。
place 计数 339 → 343，registry total 1407 → 1411，unknown 恒 0。

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| salt-lake-city | Nxol1r | Around the World in Eighty Days | real | Utah | 5 | AWED 摩门首府/Ogden 支线两小时游；RC Albatross 俯瞰；恰达 5 门 |
| charleston | RlfU3G | The Blockade Runners | real | South Carolina | 12 | 内战首炮之港/被封锁棉城；确指 SC 城，无 Charlestown MA 混入 |
| richmond | aSjsb5 | The Mysterious Island | real | Virginia | 8 | Grant 围困邦联首府/气球脱逃起点；确指 VA，无伦敦 Richmond upon Thames 混入 |
| washington | ynguY0 | From the Earth to the Moon | real | United States | 8 | 美国首都/美式子午线原点/Lincoln 遇刺城；严筛剔 Cape Washington/Washington Bay/人喻/Irving |

## 页面处理记录

- **salt-lake-city**：PN AWED-027-020/027-022/026-006、RC-010-026/010-032。摩门篇犹他城，Fogg 于 Ogden 停留六小时期间以支线往游两小时；Passepartout 街头见闻；Albatross 空中辨认摩门首府。链 omaha/platte-river/great-salt-lake/albatross/around-the-world-in-eighty-days/robur-the-conqueror。pn_validator 0 issues。
- **charleston**：PN BR-001-052/001-053/003-067/004-032/006-014/006-031/006-034/007-002/007-014、FF-002-009/010-067、SC2-001-003。《The Blockade Runners》核心港，内战首炮 Fort Sumter 之地/棉花壅塞/Dolphin 闯锁抵港。链 fort-sumter/the-blockade-runners/new-orleans。pn_validator 0 issues。
- **richmond**：PN MI-002-002/002-004/002-009/002-010/002-018/030-042、BR-008-067、AM-005-001。《神秘岛》castaways 出逃起点，Grant 围城/俘虏城/气球升空脱逃/Richmond cabinet。链 the-mysterious-island/cyrus-harding/lincoln-island/the-blockade-runners。pn_validator 0 issues。
- **washington**：PN FEM-003-009/003-008/013-047/015-003、BR-008-011、FF-001-017、MI-011-086/014-068。美国首都/铁路枢纽 Baltimore→New York/美式子午线原点/Lincoln 遇刺预言。**多实体严筛剔除**：Cape Washington（ACH×6 北极岬=既有 cape-washington 页）、Washington Bay（MI 虚构 Lincoln 岛湾=既有 washington-bay 页）、FEM-003-013「a Washington of science」（人喻）、FC-016-033 Washington Irving（人名）。链 baltimore/gun-club/new-york/from-the-earth-to-the-moon/the-mysterious-island/richmond。pn_validator 0 issues。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：4 页全句源自 sentence_index，逐页 pn_validator 0 issues（段落存在 + 关键词重叠 ≥2%）。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：salt-lake-city 5（恰达门）、charleston 12、richmond 8、washington 8。✔
- **G4 脚本建页**：4 页均经 add_page.py 建立，未用 Write/Edit 触碰 docs/wiki/pages。✔
- **schema 一致**：place-schema 四 H2（Overview/In the Narrative/Geography & Features/Connections），无 H1，Connections 为散文。✔
- **registry/backlinks 重建**：total 1411 place 343 unknown 0；backlinks 覆盖 1235 页 3244 条。✔
- **排除检查**：预期 commit 前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 输出 clean。

## 六步状态机（NEW1，grow_state 存 R127 起始计数）

| 字段 | R126 起始 | R127 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 126 | 127 |
| type_round | 97 | 98 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 62 | 63 |
| last_updated_round | 126 | 127 |

## 遗留问题

- **R127 = EVV5 预测**：since_evv5 达 10 ≥ evv5_interval → R127 首匹配 §3(1) 触发 EVV5。since_discover 届时为 4<10，故非 EVV5+SCN28 合并，预期纯 EVV5 评估轮。注：queue 消费后约 7<10，但 §3 首匹配将 EVV5 置于 SCN28 之前，故仍先走 EVV5。执行前须读 grow-state-machine.md EVV5 分支规范。
- **Amsterdam 候选消解**：岛义 amsterdam-island 既建 R45（rev HzFcAz），荷兰城真城确指 <5，双落空，declined/defer（同 Rome/Petersburg/Athens 城市 hold 处置）。教训：建前须核候选自身 slug 是否既存，而非仅核链接目标。
- **PHQ 累积（build 末 RFC 批审）**：amsterdam-island R45 页不合规（H1 + bullet Connections + aliases list）；洲级 Asia/Europe/America HOLD（America 须与 united-states 消歧）；Long Island/Bay of Bengal 4<门续 hold；Panama 消歧未决（isthmus/gulf/city/route）。
- **queue 存量**：本轮消费 4，Amsterdam declined，place 候选池开放候选降至约 6（Asia/Europe/America 洲级 HOLD + Long Island/Bay of Bengal <门 hold + Panama 消歧）。R127 EVV5 后若 R128 落 SCN28（queue<10）将补种。
