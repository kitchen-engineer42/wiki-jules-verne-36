---
round: 220
date: 2026-07-17
type_round: 191
phase: "2.1"
current_type: place
gene: NEW1
pages: [north-carolina]
result: success
---

# GROW 2.1-B · R220 · NEW1 · place — 建 North Carolina（真实美州，跨 MW×11+FF×7+MI/TTLU 各1=20 distinct 单指一州；首府 Raleigh，Great Eyrie〔MW〕与 Healthful House〔FF〕所在州）

## 执行摘要

Phase 2.1-B place 广度扩张第 191 轮（type_round 191）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、since_discover=1<10、queue(place)=3>0、全局 queue_size≥10〔HK-queue-size-scope〕、stub%=0 → §3(7)）。

取 R218 SCN28 队列**建序 2** **North Carolina**（MW 主）。建前 pages.json 子串（north-carolina）+
`the-` 前缀双查皆 NEW。**跨作品单指**：MW×11 + FF×7 + MI×1 + TTLU×1 = 20 distinctPN 全指真实美国
北卡罗来纳州（一实体，非同名异指）。**净 15 distinct solid PN**（远超门）：

- **FF-001-006**：北卡首府 Raleigh，四十四州之一，内陆 150 英里。
- **MW-001-004**：异象始于北卡西部。
- **FF-007-020**：北卡为北纬 35 度线所贯，东延至摩洛哥。
- **MW-001-014**：飞行器降于 Raleigh 附近。
- **MW-002-002**：巡视员抵 Raleigh，北卡首府。
- **MW-005-002**：北卡报章详载 Great Eyrie 之攀登。
- **FF-004-071**：北卡州长获报 Healthful House 遭闯、两人被劫。
- **FF-004-025**：北卡各县全道路车站严查，家宅遍搜。
- **FF-002-009**：Pamlico Sound；港 Wilmington〔北卡〕/ Charleston〔南卡〕。
- **TTLU-043-017**：航近北卡，复过 Cape Hatteras。
- **MW-002-023**：Alleghany 恐有火山如 Mont Pelee 之祸威胁北卡。
- **MW-002-046**：Morganton，北卡——向市长陈使命。
- **MI-009-070**：东北向西南轨迹贯北卡、南卡、佐治亚。
- **MW-015-044**：飞船夜行覆 Lake Erie 至北卡之距。
- **FF-013-022**（备）：Healthful House 近 New-Berne，北卡（Roch/Gaydon 被劫）。

place 计数 413→414，registry total 1481→1482，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 1 段 >399，拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region United States、book Master of the World、aliases=[]。
Connections/正文含 [[Great Eyrie]]/[[Healthful House]]/[[Morganton]]/[[Pamlico Sound]]（四页均存）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| north-carolina | t1j8Ua | Master of the World | real | United States | 15 | 真实美州；MW/FF/MI/TTLU 跨作品单指一州；Raleigh 首府；Great Eyrie/Healthful House 所在 |

- **north-carolina**：15 distinct solid PN（跨四作品单指一州）；aliases []。链 Great Eyrie/Healthful House/Morganton/Pamlico Sound。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指真实北卡州；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：15 solid（跨作品单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（四 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1482 place 414 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（north-carolina）+ `the-` 前缀双查皆 NEW。✔
- **跨作品单指核**：MW/FF/MI/TTLU 逐句确认同指真实一州（首府 Raleigh），采全；非同名异指。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R221 起始计数）

| 字段 | R220 起始 | R221 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 220 | 221 |
| type_round | 191 | 192 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 156 | 157 |
| last_updated_round | 220 | 221 |

## 遗留问题

1. **place 页数 414**：本轮 +1（North Carolina）。registry 全库 1482，unknown 0。
2. **下轮 R221 = NEW1**：since_evv5=5<10、since_discover=2<10、queue(place)=2>0、全局 queue_size≥10 → §3(7)。
   建 **Pleasant Garden**（pleasant-garden，MW×16 单指；北卡 Morganton 近村，Great Eyrie 山脚，火山灰飘落地），
   建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，region United States，real。
3. **R221+ 建序**：Pleasant Garden → Kamtchatka Current（余 2 项）。
4. **多词池薄 + 单词盲区**：队列消费毕（约 R222 末），下一 SCN28 须转**单词地名扫**（改 discover3 正则容单词 toponym），
   否则多词池将过早报饱和（承 HK-premature-saturation-claim / HK-discover-existing-type-blindspot）。
   候选：Raleigh/Wilmington/Pamlico/Behring/Hatteras 等。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=156→157（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/
    Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
