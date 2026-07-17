---
round: 148
date: 2026-07-15
type_round: 119
phase: "2.1"
current_type: place
gene: NEW1
pages: [ohio]
result: success
---

# GROW 2.1-B · R148 · NEW1 · place — 建 ohio（MW Terror 追捕 Toledo/Lake Erie 岸，6PN；Missouri 州主体不可建 DEFER）

## 执行摘要

Phase 2.1-B place 广度扩张第 119 轮（type_round 119）。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10、streak=0<3、queue≈12≥10、since_discover=8<10、queue(place)>0、stub%=0 → §3(7)）。
承 R147 河/湖歧义州剥离建议，对比 Ohio 与 Missouri：**Missouri 州主体净 solid ≈0**（几乎全为 Missouri River 或州列举），DEFER；
**Ohio** 净 6 solid（州/城/湖岸指，无 Ohio River 混指），建之（The Master of the World 主源）。

**消歧裁定**：Vernean 核心为 **《The Master of the World》Terror 追捕线之 Ohio/Toledo/Lake Erie 南岸**——
MW 五处（Toledo is a city of that state 料捕于 Ohio、火车越 West Virginia and Ohio、roads of Ohio、
Lake Erie 界于 Ohio/Pennsylvania/New York、Toledo/Cleveland/Sandusky Ohio cities）+ JCE-039-008（marshes of Ohio 1801 猛犸骨）。
**剔州列举/铁路名**：MW-004-013（州列举 near Columbus）、MW-008-044（州道列举）、RC-009-008（产地州列举）、
RM-023-013（巡游州列举）、AWED-027-015（被逐州列举）、AWED-031-037（越州列举）、FEM-003-008（Ohio railroad 铁路名，非州）。
**无 Ohio River 混指**（样本无一为俄亥俄河主体，queue「疑河」顾虑经查不成立）。净 solid = 6（MW×5+JCE×1，二源）。

place 计数 361→362，registry total 1429→1430，unknown 恒 0。
散文首版 max para 343 ≤400（首版即守门）；pn_validator strict 首版即全通过。
**首版误置修正**：In the Narrative 首句原误挂占位 `(MW-004-013 wait)`（属被剔州列举），add_page 前已 edit 修正为正确的 MW-011-004（「Toledo is a city of that state」原句），并合并邻句控段长。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue≈12≥10、since_discover=8 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| ≫0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| ohio | 5p8Ll5 | The Master of the World | real | United States | 6 | 州/Lake Erie 南岸；MW Terror 追捕 Toledo + 湖岸城 + 火车/公路；JCE marshes of Ohio 猛犸骨 |

- **ohio**：6 distinct PN — MW-011-004（Toledo is a city of that state 料捕）/011-006（火车越 West Virginia and Ohio）/012-029（roads of Ohio）/011-021（Lake Erie 界于 Ohio/Pennsylvania/New York）/011-024（Toledo/Cleveland/Sandusky Ohio cities）、JCE-039-008（marshes of Ohio 1801 猛犸骨）。二源 MW(5)/JCE(1)。剔州列举/铁路名 7 项，无 Ohio River 混指。链 the-master-of-the-world/journey-to-the-centre-of-the-earth。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：ohio 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过（首版误置占位引已 add 前修正）。✔
- **G2 段落 ≤400 字**：首版 max para 343（首版即守门）。✔
- **G3 ≥5 distinct PN**：6（二源；剔州列举/铁路名 7 项）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1430 place 362 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R149 起始计数）

| 字段 | R148 起始 | R149 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 148 | 149 |
| type_round | 119 | 120 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 8 | 9 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 84 | 85 |
| last_updated_round | 148 | 149 |

## 遗留问题

1. **place 页数 362**：本轮 +1。registry 全库 1430，unknown 0。
2. **⚠ 下轮 R149 = EVV5（§3(1b) 触发）**：since_evv5 将达 **10 ≥ evv5_interval(10)** → **首匹配 §3(1a/1b)**，
   since_discover=9<10 故非 §3(1a)（EVV5+SCN28），而是 **§3(1b) 纯 EVV5**：质量反思，**不建页**，重置 since_evv5=0。
   R149 须执行 EVV5 gene（抽样近轮 place 页，评均分/PN 密度/散文门/消歧质量，写 EVV5 日志，更新模板/遗留），而非 NEW1。
3. **河/湖歧义州剥离结论**：Ohio 可建（州/城/湖岸，无河混指）；**Missouri 不可建**（净州 solid≈0，全河/列举）。
   待后续同法筛 Colorado（疑 Colorado River）、Michigan（MW×9 疑 lake-michigan）——大概率同 Missouri 命运，建前须逐条查。
4. **待筛/DEFER 项**：Missouri（州主体不可建，DEFER）、Virginia（净 4，DEFER）、Louisiana（净 3，DEFER）、Abyssinia（净 3，DEFER）、
   Colorado（疑河，待剥离）、Michigan（vs lake-michigan，待剥离）、Indiana（5，散引待筛）、Arkansas（Arkansas River）、Tennessee（ram 舰异指）、Oregon（<5 clean）。
   **净 buildable 持续收窄**：R145 起既有 queue 优质项渐罄，多轮后（EVV5 后）大概率须 §3(3) SCN28 复扫补种。
5. **引注对齐 + 占位自查教训**：R148 首版 In the Narrative 首句误留 `(MW-004-013 wait)` 占位（草稿残留），add_page 前人工复核捕获并改正为 MW-011-004。
   **教训**：草稿引注若一时不确定，勿留裸占位串入正文；建页前须逐句核对 PN 与源句。已在 add 前闭环，strict 亦会兜底（占位 PN 不存在会 fail）。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **EVV5 节奏**：since_evv5=9→R149 触发（见 #2）。
8. **corpus-discover 顺延临界**：since_corpus=85（HK-corpus-discover-not-in-statemachine PARK）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope（净 buildable≪nominal，本轮再证）、HK-premature-saturation-claim、
    HK-compute-quality-fullrun-regrade、HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、
    HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
