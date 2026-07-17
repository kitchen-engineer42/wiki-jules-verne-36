---
round: 221
date: 2026-07-17
type_round: 192
phase: "2.1"
current_type: place
gene: NEW1
pages: [pleasant-garden]
result: success
---

# GROW 2.1-B · R221 · NEW1 · place — 建 Pleasant Garden（北卡 Great Eyrie 山脚村，MW×16 单指；Catawba 河畔近 Morganton，火山灰飘落地）

## 执行摘要

Phase 2.1-B place 广度扩张第 192 轮（type_round 192）。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10、since_discover=2<10、queue(place)=2>0、全局 queue_size≥10〔HK-queue-size-scope〕、stub%=0 → §3(7)）。

取 R218 SCN28 队列**建序 3** **Pleasant Garden**（MW 主）。建前 pages.json 子串（pleasant-garden）+
`the-` 前缀双查皆 NEW。**单作品单指**：MW×16 = 16 distinctPN 全指北卡 Morganton 近之 Great Eyrie 山脚村庄，
无同名异指。**净 14 distinct solid PN**（远超门）：

- **MW-001-004**：Great Eyrie 圆顶自 Morganton（Catawba 河畔）可见，经 Pleasant Garden 近山更清。
- **MW-003-002**：自 Morganton 沿 Catawba 左岸之路通 Pleasant Garden 村。
- **MW-003-007**：抵 Pleasant Garden，宿于市长家。
- **MW-001-009**：烟云东吹向 Pleasant Garden，飘落灰烬。
- **MW-001-010**：Morganton 与 Pleasant Garden 及近山农户受威胁。
- **MW-001-017**：四月四日夜，Pleasant Garden 众人被喧声惊醒。
- **MW-002-039**：若 Great Eyrie 为火山，Pleasant Garden 与 Morganton 数千人危。
- **MW-003-010**：自 Pleasant Garden 可见全山脊。
- **MW-003-076**：马车停 Pleasant Garden 市长宅前过夜。
- **MW-003-070**：须早行方能当夜返 Pleasant Garden。
- **MW-011-060**：柏木香忆及 Morganton 与 Pleasant Garden 林气。
- **MW-005-017**：Pleasant Garden 市长可靠，Morganton 市长之友。
- **MW-015-041**：Great Eyrie 异象、噪声惊 Pleasant Garden 与 Morganton。
- **MW-017-029**：山再动则 Morganton 与 Pleasant Garden 疑火山口重开。

place 计数 414→415，registry total 1482→1483，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 1 段 >399，拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region United States、book Master of the World、aliases=[]。
Connections/正文含 [[Great Eyrie]]/[[Morganton]]（二页均存）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| pleasant-garden | KYgkzb | Master of the World | real | United States | 14 | 北卡 Great Eyrie 山脚村；Catawba 河畔近 Morganton；MW 单指 |

- **pleasant-garden**：14 distinct solid PN（MW 单指）；aliases []。链 Great Eyrie/Morganton。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指北卡 Pleasant Garden 村；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：14 solid（MW 单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（二 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1483 place 415 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（pleasant-garden）+ `the-` 前缀双查皆 NEW。✔
- **单作品单指核**：MW 逐句确认同指一村，采全。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R222 起始计数）

| 字段 | R221 起始 | R222 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 221 | 222 |
| type_round | 192 | 193 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 157 | 158 |
| last_updated_round | 221 | 222 |

## 遗留问题

1. **place 页数 415**：本轮 +1（Pleasant Garden）。registry 全库 1483，unknown 0。
2. **下轮 R222 = NEW1**：since_evv5=6<10、since_discover=3<10、queue(place)=1>0、全局 queue_size≥10 → §3(7)。
   建 **Kamtchatka Current**（kamtchatka-current，FC×15 单指；白令海域洋流，与 Behring Current 交汇，牵动浮岛漂向），
   建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region North Pacific，real。**建毕队列罄 → R223 = SCN28 zombie**。
3. **R223 SCN28 须转单词地名扫**：多词≥7-PN 净新池已薄；改 discover3 正则容单词 toponym，
   否则过早报饱和（承 HK-premature-saturation-claim / HK-discover-existing-type-blindspot）。
   候选：Raleigh/Wilmington/Pamlico/Behring/Hatteras/Catawba 等。
4. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
6. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
7. **corpus-discover 顺延**：since_corpus=157→158（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
10. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/
    Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
