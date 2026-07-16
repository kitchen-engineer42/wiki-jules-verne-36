---
round: 129
date: 2026-07-15
type_round: 100
phase: "2.1"
current_type: place
gene: NEW1
pages: [mont-blanc, bay-of-bengal]
result: success
---

# GROW 2.1-B · R129 · NEW1 · place — 建 mont-blanc（欧洲最高峰，11PN）+ bay-of-bengal（Nemo 珍珠场，5PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 100 轮（type_round 100）。决策机 §3 首匹配裁定 **NEW1**：
since_evv5=1<10（非 1a/1b）、discover_streak_low=1<3（非 2）、
**queue_size≥discover_queue_threshold(10) 且 since_discover=0<10（priority 3 不触发）**、
queue(place)≠0（非僵尸 4）、stub%=0（非 5/6）→ 落 §3(7) NEW1 默认分支。

消费 R128 SCN28 补入的两强候选：**mont-blanc**（41 distinctPN，AMB 专篇）、
**bay-of-bengal**（5 distinctPN 恰达门，R128 由 hold 升格）。place 计数 343→345，registry total 1411→1413，unknown 恒 0。

### queue_size 口径说明（审计透明）

§3 priority 3 的 `queue_size` 按 grow-state-machine.md §3 注「`logs/butler/queue.md` 中有效候选行数（去除已处理条目）」
取**全类型有效候选行数**（place 开放 + 预置 character 红链候选 11 等），当前 ≈18≥10 → priority 3 不触发。
> ⚠ **口径存疑（记 HK-queue-size-scope PARK）**：R127/R128 日志曾以 `queue(place)` 单类型口径（≈6<10）触发 SCN28，
> 与本轮全类型口径不一致。二读并存：全类型口径下活跃类型近饱和时靠预置跨类型候选维持 queue≥10、由 priority 4
> (`queue(current_type)==0`) 兜底转 discover；单类型口径下 place<10 即 discover。本轮采**全类型（spec 字面）**口径建页
> ——既忠于 spec 字面、又消费强候选 mont-blanc（勿使 41PN 强候选滞留至 CLOSE 而未建）。口径歧义待用户末期评审统一。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=1 | 否 |
| 1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue_size≈18≥10, since_discover=0 | 否 |
| 4 | SCN28-zombie（queue(current_type)==0）| place≈6≠0 | 否 |
| 5 | RCH2（stub%≥20）| =0 | 否 |
| 6 | NEW1+RCH2（stub%∈[15,20)）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| mont-blanc | 9tnHNq | The Ascent of Mont Blanc | real | France | 11 | 欧洲最高峰；AMB 专篇 Chamonix 登顶；Balmat+Paccard 首登；1866 冰崩罹难；14,439ft 高度基准（FEM/RM/SC）；**与 alps 山链页判然不同（本页具体峰体）** |
| bay-of-bengal | zjp3jz | Twenty Thousand Leagues Under the Sea | real | Indian Ocean | 5 | Nemo 珍珠场/黑潮源/恒河浮尸/Andaman 群岛；⚠ RM-010-016「从月看地」偏 oblique，AWED+TTLU 4 确指为主干，恰达 5 门 |

- **mont-blanc**：PN AMB-001-002/040/062/081/100/104/111/146、FEM-024-021、RM-007-005、SC-013-014。AMB《The Ascent of Mont Blanc》专篇为主体（Chamonix 1871-08-18 出发登顶、summit 窄脊 200 步长一码宽、Goûter/Mont Maudit 雪链、Balmat 与 Paccard 首登、1866 英客四人冰崩罹难、「painful ascent」），跨源 FEM/RM/SC 以 14,439ft 欧洲最高作高度基准。与既有 alps（rev vR6O4P，山链）严分：本页为链中具体最高峰。链 the-ascent-of-mont-blanc/alps/from-the-earth-to-the-moon/round-the-moon/in-search-of-the-castaways。pn_validator ✓ 0 issues。
- **bay-of-bengal**：PN TTLU-014-028/025-040/026-011、AWED-016-005、RM-010-016。TTLU 三引为叙事主干（Nemo「pearl fisheries in the Bay of Bengal」、Kuroshio 黑潮源、湾口恒河浮尸），AWED-016-005 Andaman 群岛所在湾，RM-010-016 从月辨识真湾（偏 oblique，辅证）。distinctPN=5 恰达 GROW-JUDGMENT-R50 门。链 indian-ocean/nautilus/captain-nemo/twenty-thousand-leagues/around-the-world-in-eighty-days/round-the-moon。pn_validator ✓ 0 issues。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：两页全句源自 sentence_index，逐页 pn_validator ✓ 0 issues（段落存在 + 关键词重叠达标）。✔
- **G2 段落 ≤400 字**：全部符合（Bengal Overview 拆两段以避门）。✔
- **G3 ≥5 distinct PN**：mont-blanc 11、bay-of-bengal 5（恰门）。✔
- **G4 脚本建页**：两页均经 add_page.py 建立，未用 Write/Edit 触碰 docs/wiki/pages。✔
- **schema 一致**：place-schema 四 H2（Overview/In the Narrative/Geography & Features/Connections），无 H1，Connections 为散文。✔
- **registry/backlinks 重建**：total 1413 place 345 unknown 0；backlinks 覆盖 1238 页 3255 条。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R130 起始计数）

| 字段 | R129 起始 | R130 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 129 | 130 |
| type_round | 100 | 101 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 1 | 1（NEW1 不动 streak）|
| rounds_since_last_corpus_discover | 65 | 66 |
| last_updated_round | 129 | 130 |

## 遗留问题

1. **place 页数 345**：本轮 +2。registry 全库 1413，unknown 0。
2. **queue_size 口径歧义（HK-queue-size-scope，新增 PARK）**：见上「口径说明」。R127/R128 单类型口径 vs 本轮全类型口径。
   末期评审须统一，并回判 R128 SCN28 是否应为 NEW1。建议：活跃类型 discover 触发宜用 `queue(current_type)`
   （否则预置跨类型候选会永久压制活跃类型 discover），但字面 spec 为全类型——待 RFC 澄清。
3. **下轮 R130 预测**：全类型口径下 queue_size 仍≥10、since_evv5=2<10、streak=1<3、queue(place)>0、stub%=0 → 续 NEW1。
   place 剩可建候选：Panama（待消歧 City/Isthmus/canal）；洲级 Asia/Europe/America（HOLD，须聚焦确指句）。
   强候选已罄，下轮 NEW1 或消费 Panama（先决消歧）或转洲级 HOLD 复议；若判无可建则 priority 4 兜底 discover。
4. **discover_streak_low=1**：R128 低产遗留；NEW1 轮不变。若后续 discover 续低产则向 3（CLOSE）逼近。
5. **corpus-discover 顺延临界**：since_corpus=66，远过阈但非 §3 分支（PARK）；待表层复扫 0 新时议 corpus 深扫。
6. **EVV5 节奏**：since_evv5=2，下次约 R138。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **散文门债**：32 页 >400（既有债 DEFERRED，RFC 后 edit_page 复拆）；本轮两页 over-400=0，无新增。
9. **PHQ 待决**：Panama 消歧；Rome/Petersburg/Athens/Amsterdam 荷城（<门 hold）；Long Island（clean 4<门续 hold）；
   amsterdam-island R45 页不合规（H1+bullet Connections+aliases list）。
10. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass（32 页）、HK-corpus-discover-not-in-statemachine、
    HK-queue-size-scope（新）、HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧；国级页价值待评。
