---
round: 91
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R91 决策矩阵（读 R90 末计数器：queue=3<10、since_evv5=7<10、since_discover=1、discover_streak_low=1、since_corpus=27<30）→ 优先级 3 **SCN28 表层复扫**（queue<10 触发 discover；此为正当触发——R90 消化积压后 queue 真实降至 3，since_discover=1 非零）。不建页。

沿用 demonym-stoplist geo 邻接法续扫。**否证 R89/R90「place 趋饱和」判断**：本轮 surface 一批**大区域/国家级**真地名——Norway（跨源 101 distinctPN）、New Zealand（127）、Angola（DSCF:32）、Africa（洲级 245）、South America（洲级 53）。均以 `\bName\b` 全库核，distinctPN ≫5，粒度与既建 Australia/Siberia/Patagonia（区域级）一致。**new_candidates=5 ≥ 3 → discover_streak_low 1→0**（place 关闭倒计时撤销）。queue 3→8。

## 页面处理记录

（discover 轮，无建页）

### 新增候选

| 候选 | distinctPN | 主源 | rof | 备注 |
|------|-----------|------|-----|------|
| Norway | 101 | TN:32 / WC:25 | real | 挪威/Telemark/峡湾国度 |
| New Zealand | 127 | SC:72 | real | SC 毛利篇主舞台/37°线终点 |
| Angola | 32 | DSCF:32 | real | 内陆奴隶贸易之地/Kazounde 所在 |
| Africa | 245 | DSCF:91 / FWB:70 | real | 洲级；FWB 气球横越之陆 ⚠ 聚焦确指句 |
| South America | 53 | DSCF:17 / EHLA:11 / SC:8 | real | 洲级；DSCF/EHLA/SC 舞台 ⚠ 聚焦确指句 |

### 剔除/噪声（未入队）

| 候选 | distinctPN | 裁定 |
|------|------|------|
| Victoria | 22 | 多实体污染（Queen Victoria/Victoria Island[已建]/Victoria Bay[已建]/Victoria balloon[tech]）→ 非单一地点，剔 |
| America | 9 | 泛指（North/South America/USA）多义，剔 |
| Klock | 7 | 「Klock-Klock」（已建 klock-klock R88）子串，剔 |
| Niagara | 5 | niagara-falls/niagara-river/goat-island 已建，裸名污染，剔 |
| No / Floridian / Algerian | 12/5/5 | 假匹配 / demonym，剔 |

## EXIT-GATE 检查

- G4：本轮无建页，无 add_page/edit_page 调用 ✓
- 词边界核验：5 新候选均以 `\bName\b` 全库扫描核 distinctPN（Norway 101/New Zealand 127/Angola 32/Africa 245/South America 53）✓
- 接地诚信：demonym stoplist（american/chinese/norwegian/floridian/algerian 等）滤除国民称谓假匹配；Victoria/Niagara/Klock 多义或既建变体剔除 ✓
- 交叉核既有页：5 新候选 label/slug 均不在 pages.json（Australia/Siberia 已建但 Norway/NZ/Angola/Africa/South America 未建）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R91→R92，SCN28 discover）

- current_round 91→92
- type_round 62→63
- rounds_since_last_evv5 7→8
- rounds_since_last_discover 重置为 0
- discover_streak_low 1→0（new_candidates=5≥3，高产重置，撤销关闭倒计时）
- rounds_since_last_corpus_discover 27→28
- last_updated_round 91→92

## 遗留问题

- **R92 预测 = NEW1（优先级 6）**：R91 末 queue=8<10 → 矩阵字面仍触发 priority 3 SCN28。但同 R90 情形：since_discover 刚重置为 0，紧接再扫必空转；队列现有 6 个可建候选（Norway/New Zealand/Angola/Africa/South America + Amazones）。**建议 R92 直接 NEW1** 消化：先建 5 个国家/区域级（Norway/New Zealand/Angola/South America/Amazones[定 slug amazonas-province]），Africa 洲级留后单独精建（须聚焦 FWB 气球横越确指句，避免泛写）。R92 起点按实际计数器裁定。
- **饱和判断修正**：R89/R90 曾疑 place 趋饱和，R91 以区域/洲级粒度 surface 5 大候选否证之——**place 广度仍有区域层未穷尽**。后续 discover 可续挖国家级（Egypt/India/China/Sweden/Denmark 等 Verne 频繁设定国），但须逐一词边界核并判断是否值得洲/国级页（避免与既有城市/地点页重复覆盖）。
- **EVV5 下次约 R94**：since_evv5 R91 末=8，约每 11 轮（R83→R94）。
- **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补交叉核，R92+ 附带。
- Amazones 建页前定 slug（amazonas-province）避 amazon 河页碰撞；Africa book 定 Five Weeks in a Balloon 待建页时复核主源。
