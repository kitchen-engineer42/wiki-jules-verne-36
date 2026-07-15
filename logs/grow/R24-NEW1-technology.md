---
round: 24
date: 2026-07-15
type_round: 2
phase: "2.1"
current_type: technology
gene: NEW1
pages: [fulgurator, the-sword, oxyhydric-gas]
result: accept
---

# GROW 2.1-B · R24 · NEW1 · technology — 建 R23 复扫补种的 3 候选（FF×2 + DOSE×1）

## 本轮公告

**R24 — Phase 2.1 — NEW1 — technology — 3 页（standard 批）**

R23 SCN28 broadened 复扫命中 R21 窄扫盲区的 3 真发明，本轮 NEW1 一并建为 standard 档：
**fulgurator**（武器）+ **the-sword**（载具）同源 *Facing the Flag*，**oxyhydric-gas**（概念）源
*Doctor Ox's Experiment*。建后 queue(technology)=0。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=14, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =22 | 否 |
| 3.9 | zombie-guard（queue(current_type)==0）| queue(technology)=3 | 否 |
| 4/5 | RCH2 / NEW1+RCH2（stub% ≥ 15%）| stub%=0 | 否 |
| **6** | **默认 NEW1（≤5 页 standard）** | queue(technology)=3 | **触发（建 3）** |

## 页面处理记录

| # | slug | 源作(VVV) | category | inventor | rev | size | 引注数 | 备注 |
|---|------|-----------|----------|----------|-----|------|--------|------|
| 1 | fulgurator | Facing the Flag (FF) | weapon | Thomas Roch | Hx8lvo | 4205 | 20 | 自推进超级爆炸武器；全书核心 McGuffin；Roch 认出三色旗后拒射，炸毁 Back Cup 与自身 |
| 2 | the-sword | Facing the Flag (FF) | vehicle | British Royal Navy | 5Zb9lc | 3011 | 15 | 12 吨英军潜水艇，三水密舱；Davon 中尉潜入 Back Cup 营救 Roch，被海盗拖船撞沉 |
| 3 | oxyhydric-gas | Doctor Ox's Experiment (DOSE) | concept | Doctor Ox | LZIpnV | 3216 | 15 | 电解酸化水制氧氢气；名为照明，实为向全城灌纯氧的生理实验；爆炸终结 |

> 三页均 standard 档，technology-schema 四节全备（Overview + Design & Operation + Role in the Story
> + Science & Speculation）。全部半角引注经 sentence_index 校验：FF-001~018 章（fulgurator/the-sword）、
> DOSE-003~017 章（oxyhydric-gas）。数值/机械参数用引号短句，无超 3 行 blockquote。
> 各段 ≤400 字手工核验（fulgurator max 394；the-sword max 366；oxyhydric-gas max 358）。
> add_page.py 自动回填 quality=featured（虚高，DEFERRED-REGRADE）。
> wikilink：fulgurator→[[Thomas Roch]]/[[Ker Karraje]]；the-sword→[[Thomas Roch]]/[[Ker Karraje]]/[[Nautilus]]；
> oxyhydric-gas→[[Doctor Ox]]。姊妹 tech 与红链人物均已埋链（backlinks 覆盖 1040 页 / 2363 条）。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 建页合规 | PASS | 三页均经 add_page.py（无 Write/Edit 旁路）；type=technology 正确解析 |
| G2 PN 有效性 | PASS | 全部引注 PN 经 sentence_index 校验存在（FF/DOSE 章）；半角括号；无 warn |
| G3 散文门 | PASS（手工）| 各段 ≤400（max 394）；add_page.py 不强制散文门（PARK 债）|
| G4 记录完整性 | PASS | 本日志；queue.md 消费 3 候选（P1 technology 清空）；grow_state step-six→R25 |
| G5 链接密度 | PASS | 三页共含 [[Thomas Roch]]×2 / [[Ker Karraje]]×2 / [[Nautilus]] / [[Doctor Ox]] wikilink |

## state 更新

`current_round 24→25`，`type_round 2→3`，`rounds_since_last_evv5 2→3`，
`rounds_since_last_discover 0→1`，`rounds_since_last_corpus_discover 22→23`，
`discover_streak_low` 保持 0。`current_type` 仍 technology，`last_updated_round→25`。

## 遗留问题

1. **R25 = technology SCN28（zombie-guard，queue(technology)=0）**：R23 已 broadened 复扫一轮，本轮
   建完 3 候选后再确认是否还有第三类漏判（如 Steam House / Standard Island / Terror 之外的特制机器）。
   预期 new_candidates 稀少 → streak 累积 → technology 收尾倒计时。
2. **technology 覆盖盘点**：Pilot 16 + Go-Ahead + 本轮 3 = 20 页。核心机器（Nautilus/Albatross/Terror/
   Forward/Columbiad/…）+ 武器（Fulgurator）+ 潜艇（the Sword）+ 化学概念（oxyhydric gas）均已覆盖。
3. **Thomas Roch / Ker Karraje / Doctor Ox 红链**：本轮埋入 4 条人物红链，待 character 类型轮消费；
   Davon 中尉（the-sword）distinctPN 待 character 轮评估。
4. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传 七项债务照旧 PARK/记录。
