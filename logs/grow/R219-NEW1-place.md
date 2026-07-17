---
round: 219
date: 2026-07-17
type_round: 190
phase: "2.1"
current_type: place
gene: NEW1
pages: [montgomery-street]
result: success
---

# GROW 2.1-B · R219 · NEW1 · place — 建 Montgomery Street（旧金山主街，跨 GM×13+AWED×3 单指 16 distinct，Kolderup 宅邸所在，环球赌途起讫地之一）

## 执行摘要

Phase 2.1-B place 广度扩张第 190 轮（type_round 190）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、since_discover=0<10、queue_size≥10〔全局，含 event/character 积压〕、
queue(place)=4>0、stub%=0 → §3(7)）。

取 R218 SCN28 队列**建序 1** **Montgomery Street**（GM 主）。建前 pages.json 子串（montgomery）+
`the-` 前缀双查皆 NEW。**跨作品单指**：GM×13 + AWED×3 = 16 distinctPN 全指旧金山那条主街，
无同名异指。**净 15 distinct solid PN**（远超门）：

- **AWED-025-006**：Montgomery Street 之于 SF 如 Regent Street 之于伦敦、Broadway 之于纽约；两侧壮丽商铺。
- **AWED-025-012**：节庆日人潮塞满人行道、车轨、店门、窗、屋顶。
- **AWED-025-017**：街上端一段石阶，可俯观人群而不被挤。
- **GM-003-002**：William W. Kolderup 归其 Montgomery Street 宅邸。
- **GM-012-002**：宅中主人安睡十小时无扰。
- **GM-002-083**：欢呼声随 Kolderup 至 Montgomery Street，美国人狂热。
- **GM-005-040**：启程日于 Montgomery Street 宅邸设盛大饯别早宴。
- **GM-005-034**：Stephenson 公司，Montgomery Street 摄影师。
- **GM-001-043**：Oakhurst，Montgomery Street 酒保。
- **GM-012-029**：街上三步内必遇递烟火之绅士。
- **GM-012-030**：「此处非旧金山，非 Montgomery Street」——Godfrey 荒岛告诫。
- **GM-020-037**：「回到 Montgomery Street 与 Kolderup 叔一处方算到家」。
- **GM-016-061**：Tartlet 叹此难不会发生于叔之 Montgomery Street 宅。
- **GM-009-013**：盼 Kolderup 汇款以返 Montgomery Street。
- **GM-021-015**：Tartlet 宁要 Montgomery Street 之地窖。

place 计数 412→413，registry total 1480→1481，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 3 段 >399，拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region United States、book Godfrey Morgan、aliases=[]。
Connections 散文含 [[San Francisco]]（页存）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| montgomery-street | GspUcw | Godfrey Morgan | real | United States | 15 | 旧金山主街；GM/AWED 跨作品单指；Kolderup 宅邸；比作 Regent St/Broadway |

- **montgomery-street**：15 distinct solid PN（跨 GM/AWED 单指）；aliases []。链 San Francisco/Kolderup/Godfrey 语境。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 SF Montgomery Street；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：15 solid（跨作品单指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（[[San Francisco]]）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1481 place 413 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（montgomery）+ `the-` 前缀双查皆 NEW。✔
- **跨作品单指核**：GM/AWED 逐句确认同指旧金山一条主街，采全。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R220 起始计数）

| 字段 | R219 起始 | R220 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 219 | 220 |
| type_round | 190 | 191 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 155 | 156 |
| last_updated_round | 219 | 220 |

## 遗留问题

1. **place 页数 413**：本轮 +1（Montgomery Street）。registry 全库 1481，unknown 0。
2. **下轮 R220 = NEW1**：since_evv5=4<10、since_discover=1<10、queue(place)=3>0、全局 queue_size≥10 → §3(7)。
   建 **North Carolina**（north-carolina，MW×11+FF×7+MI/TTLU×1=20 distinct，真实美州，含 Raleigh/Pamlico Sound，
   MW Great Eyrie 与 FF Healthful House 所在州），建前 pages.json 子串 + `the-` 双查，抽样 ≥5 solid，
   region United States，real；MW/FF 双书须逐句核同指一州。
3. **R220+ 建序**：North Carolina → Pleasant Garden → Kamtchatka Current（余 3 项）。
4. **多词池薄 + 单词盲区**：队列消费毕（约 R222 末），下一 SCN28 须转**单词地名扫**（改 discover3 正则容单词 toponym），
   否则多词池将过早报饱和（承 HK-premature-saturation-claim / HK-discover-existing-type-blindspot）。
   候选：Raleigh/Morganton/Wilmington/Pamlico/Behring 等。
5. **HK-dupcheck-the-prefix-blindspot**：本轮已应用，无复现。PARK 记录。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=155→156（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；Mackenzie〔river〕/Fort Good Hope/
    Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、HK-place-alias-suppression、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
