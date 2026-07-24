---
round: 2
date: 2026-07-24
gene: LNK12-wikilink-integrity
pages: [lunar-projectile, twenty-thousand-leagues, j-t-maston, topsy-turvy, dick-kennedy, sea-monster-hunt, stony-hill, dick-sand-a-captain-at-fifteen, journey-to-the-center-of-the-earth]
result: pass
---

# Butler R2 · LNK12 wikilink-integrity · fix-links — 全库红链修复（12 target → 3，25/28 链解析）

## 执行摘要

`/butler --auto` 首个实质轮（round_counter 1→2；此前仅 R1 BOOT-readstate pilot 试跑）。empty_fallback → housekeeping：LNK12 全库 wikilink 完整性扫描。

**扫描**：1669 页，broken wikilink target **12**（~28 链），empty wikilink **0**（LNT14 clean）。

**根因**：全部为 **label-变体红链**——链接文本与规范页 label 不符（工作码/标点/前缀差异）。修复法本应 add-redirect（LNK10）或 add-alias（C3）；因变体串 slug 与规范页碰撞（`J.T. Maston`→`j-t-maston`、`Topsy Turvy`→`topsy-turvy` 等已占用），**一律 add-alias**（`edit_page.py --skip-prose-check`，仅改 frontmatter aliases，append-only，size 净增 +0~+42）。

**结果**：9 个 add-alias 目标全数修复，broken 12→**3**（仅余 deferred）。

## 页面处理记录

| 页面 | 操作 | 结果 | 备注 |
|------|------|------|------|
| lunar-projectile | +alias "Lunar Projectile" | pass | 解 11 红链（label「The Projectile」）|
| twenty-thousand-leagues | +alias "Twenty Thousand Leagues Under the Seas" | pass | 解 8 红链（label「…Sea」无 s）|
| j-t-maston | +alias "J.T. Maston" | pass | 解 3 红链（label 有空格）|
| topsy-turvy | +alias "Topsy Turvy" | pass | 解 1（连字符）|
| dick-kennedy | +alias "Kennedy" | pass | 解 1 |
| sea-monster-hunt | +alias "Sea Monster Hunt" | pass | 解 1（前缀 The）|
| stony-hill | +alias "Stone's Hill" | pass | 解 1；**撇号值初用单引号破 YAML→改双引号修正**（rev YznV7Q）|
| dick-sand-a-captain-at-fifteen | +alias "Dick Sand, A Captain at Fifteen" | pass | 解 1（冒号 vs 逗号 book-name 变体）|
| journey-to-the-center-of-the-earth | +alias "Journey to the Centre of the Earth" | pass | 解 1（Centre/Center + A）|

## 遗留问题（queue P2/P3，本轮未处理）

1. **[[Dr. Clawbonny]]（merge）**：`clawbonny`（label「Dr Clawbonny」）与 `doctor-clawbonny`（label「Doctor Clawbonny」）为**同一角色重复页** → 须 LNK15 dedup/merge（合并正文、保留 revision、加 alias「Dr. Clawbonny」），非单纯 add-alias。
2. **[[Sir Francis Cromarty]]（discover）**：AWED Fogg 惠斯特牌友/退役准将，未建页 → discover 候选。
3. **[[Russian America]]（discover）**：核 vs `alaska` 是否 alias；1 红链自 kamtchatka-current。

## 观察（供 W5）

- **add-alias YAML 陷阱**：含撇号的 alias 值（`Stone's Hill`）在单引号内破 YAML（LAW §八），必须双引号 `"Stone's Hill"`。build_registry 静默丢弃该页 frontmatter，连带其原 label 一并失效（本轮一度令 broken 反增 `Stony Hill`）——add-alias 类修改后应立即 rebuild + 复扫验证。
- **红链长尾成因 = label 变体**：工作码标点（冒号/逗号）、拼写（Centre/Center、Sea/Seas）、前缀「The」、空格（J.T./J. T.）。根治宜在建页时即为规范页补齐常见变体 alias，或引擎侧 wikilink 解析做标点/大小写归一化（可并入 memex-team RFC 讨论）。
- **queue 格式**：`logs/butler/queue.md` 主体为 GROW discover 注释（HTML comment），非 butler P-task 复选框；本轮已在 P1 头部注入 12 条标准 P-task，其余 GROW 注释保留。
