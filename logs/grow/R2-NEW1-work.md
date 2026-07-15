---
round: 2
date: 2026-07-14
type_round: 1
phase: "2.1"
current_type: work
gene: NEW1
pages: [from-the-earth-to-the-moon, around-the-world-in-eighty-days, journey-to-the-center-of-the-earth, the-adventures-of-captain-hatteras, robur-the-conqueror]
result: accept
---

# GROW 2.1-B · R2 · NEW1 · work — 5 页

## 本轮公告

**R2 — Phase 2.1 — NEW1 — work — 5 页（standard 档）**

2.1-Showcase 完成后的首个类型扩张轮。`current_type=work`，串行建 5 页。

## 选页依据

按「existing entity pages 的 `book:` 字段引用频次」优先（关闭红链价值最高），
取尚未建页的 Top 5 作品：

| slug | 作品 | book 引用数 | VVV | 主要 PN 源 |
|------|------|-----------|-----|-----------|
| from-the-earth-to-the-moon | From the Earth to the Moon | 10 | FEM | FEM-001-002, FEM-004-009, FEM-001-003 |
| around-the-world-in-eighty-days | Around the World in Eighty Days | 9 | AWED | AWED-001-002, AWED-001-018 |
| journey-to-the-center-of-the-earth | A Journey to the Center of the Earth | 9 | JCE | JCE-001-002, JCE-005-050, JCE-006-002 |
| the-adventures-of-captain-hatteras | The Adventures of Captain Hatteras | 4 | ACH | ACH-001-002, ACH-004-012, ACH-012-041 |
| robur-the-conqueror | Robur the Conqueror | 3 | RC | RC-004-015, RC-007-032 |

> TTLU、MI 已在 2.1-Showcase 建为 featured，本轮不重复。

## 页面处理记录

| 页面 | 结果 | quality | 引文数 | 每句有据 | max 段长 |
|------|------|---------|-------|---------|---------|
| from-the-earth-to-the-moon | 新建 | standard | 4 | ✓ | 335 |
| around-the-world-in-eighty-days | 新建 | standard | 3 | ✓ | 323 |
| journey-to-the-center-of-the-earth | 新建 | standard | 3 | ✓ | 325 |
| the-adventures-of-captain-hatteras | 新建 | standard | 3 | ✓ | 363 |
| robur-the-conqueror | 新建 | standard | 2 | ✓ | 325 |

> 全部 5 页 work-schema 五节齐全（Overview / Plot Summary / Main Characters / Key Places & Technology / Themes），
> 每句断言均来自 corpus_search 命中段并标注 PN。已预控段落 ≤400 字（规避 add_page.py 散文门旁路缺陷，见 SHOWCASE-r1 EVV5）。

## EXIT-GATE 检查

- [x] G1 5 页全部成功新建（standard 档）
- [x] G2 每页 frontmatter 完整（type/vvv/chapter_count/genre）
- [x] G3 每句有据，PN 均经 sentence_index 核验
- [x] G4 记录完整性：本日志 + state 更新
- [x] G5 散文段全部 ≤400 字（预控，非事后修补）

## state 更新

`current_round 2→3`，`type_round 0→1`，`rounds_since_last_evv5/discover 0→1`。
`current_type` 仍为 `work`（候选未耗尽，剩余约 28 部作品）。

## 遗留问题

1. work 类型候选充足（35 部作品 − 已建 7 = 28 待建），无需 discover。
2. 下一轮延续 work NEW1（次高引用作品：Round the Moon、Master of the World、Five Weeks in a Balloon、In Search of the Castaways、Dick Sand 等）。
3. featured 虚高与 add_page.py 散文门旁路两项债务照旧 PARK（见 housekeeping_queue.md）。
