---
round: 87
date: 2026-07-15
phase: "2.1-B"
gene: SCN28
pages: []
result: success
---

## 执行摘要

R87 决策矩阵（读 R86 末计数器：since_evv5=3<10、queue=5<10、since_discover=2<10、since_corpus=23<30）→ 优先级 3 **SCN28 表层复扫**（queue<10 触发 discover）。本轮不建页，仅向候选队列补种。

采用「地名关键词邻接扫描」：捕获紧邻 river/town/city/port/island/cape/sea/lake/mountain/gulf/bay/village/province/strait/desert/steppe/valley/coast 等地理词的大写专名，经人名/demonym stoplist 过滤，再逐一 `\bName\b` 词边界核 distinctPN。此法揭示前几轮裸词扫描被 demonym（American/Chinese/Norwegian…）掩盖的一批强真地名，**否证了 R86 提出的 place 饱和假设**。

新增 7 个候选（均 distinctPN ≥8）：Greenland、Patagonia、Gobi、Vesfjorddal、Tjon、Klock-Klock、Amazones。new_candidates=7 ≥3 → discover_streak_low 维持 0（未向 CLOSE 累加）。queue 5→12。

## 页面处理记录

（discover 轮，无建页）

| 候选 | distinctPN | 主源 | rof | 备注 |
|------|-----------|------|-----|------|
| Greenland | 68 | ACH:30/WC:11/TN:8/TT:8/FC:5/WAI:4 | real | 跨作多现，主源 ACH 极地探险，可跨源建 |
| Patagonia | 34 | SC:26 (+MI/RC/RM/AM/DSCF/TT/TTLU) | real | SC 沿 37°线搜索区 |
| Gobi | 16 | ASC:15/TT:1 | real | ASC 大铁路穿越之中亚瀚海 |
| Vesfjorddal | 12 | TN:12 | real | 挪威 Telemark 山谷/TN 主场景 |
| Tjon | 10 | ASC:10 | real | ASC 在建高架桥所跨之谷/脱轨险地 |
| Klock-Klock | 19 | AM:19 | fictional | Tsalal 岛土著村（slug klock-klock）|
| Amazones | 8 | EHLA:8 | real | 巴西亚马逊省；⚠ 与 amazon（河）label 近，须专用 slug 避碰 |

## EXIT-GATE 检查

- G4（页面操作合规）：本轮无建页，无 add_page/edit_page 调用 ✓
- 词边界核验：7 候选均以 `\bName\b`（Klock-Klock 用连字符全名）全库扫描确认 distinctPN，非子串污染 ✓
- 交叉核既有页：7 候选 label/slug 均不在 pages.json（Amazones 与 amazon 河页近似，已加避碰 slug 提示）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R87→R88，SCN28 discover）

- current_round 87→88
- type_round 58→59
- rounds_since_last_evv5 3→4
- rounds_since_last_discover 重置为 0
- discover_streak_low 0（new_candidates=7≥3，不累加）
- rounds_since_last_corpus_discover 23→24
- last_updated_round 87→88

## 遗留问题

- **R88 预测 = NEW1（优先级 6）**：R87 末 queue=12≥10、since_evv5=4<10、since_discover=0<10、since_corpus=24<30、stub%=0 → 优先级 6 NEW1 建 5 页。优先消费本轮高 distinctPN 强候选：Greenland（跨源 68，book 取主作 The Adventures of Captain Hatteras）、Patagonia（SC:26）、Gobi（ASC:15）、Vesfjorddal（TN:12）、Klock-Klock（AM:19）。Amazones 须先定 slug（amazonas-province）再建，避 amazon 河页 label 碰撞。
- **方法论修正**：裸词扫描（R76/R84）会被 demonym 掩盖真地名；本轮「地理关键词邻接 + demonym stoplist」显著提升召回。后续 discover 应沿用此法。记入 housekeeping：HK-surface-discover-pattern-undercount 可结此案（demonym 过滤补丁）。
- **EVV5 下次约 R94**：since_evv5 从 R83=0 累加，约每 11 轮触发。
- **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补交叉核，R88+ 附带。
- 前几轮 held 跨源候选（North Sea/Long Island/Bay of Bengal/Cape Bon/Kara Sea）续 hold，待 R89+ 若强候选耗尽再精核建页或剔除。
