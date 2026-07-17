---
round: 154
date: 2026-07-15
type_round: 125
phase: "2.1"
current_type: place
gene: NEW1
pages: [maryland]
result: success
---

# GROW 2.1-B · R154 · NEW1 · place — 建 maryland（TT 主源，Gun Club/Baltimore/北极拍卖，6PN）；Timbuktu 判重跳过

## 执行摘要

Phase 2.1-B place 广度扩张第 125 轮（type_round 125）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、streak=0<3、since_discover=3<10、queue(place)>0、stub%=0 → §3(7)）。
承 R150 SCN28 补种建序，原定第 4 项 **Timbuktu 经查为重复**（既有 `timbuctoo.md` alias [Timbuktu] 已覆盖同城，
FWB 主源 7PN），**不建**——R150 SCN28 漏检既有页，属 HK-discover-existing-type-blindspot 再现。
遂建序内下一有效项 **Maryland**（R150 判 ~5 clean solid，多源 TT/FEM/BR）。

**Timbuktu 判重详情**：`gather.py` 显示 Timbuktu(RC×7) 与 Timbuctoo(FWB×22) 为同城两拼写。既有 timbuctoo 页
（rev featured，FWB 主源，alias 含 Timbuktu）已覆盖。RC×7 段（Albatross 掠 Timbuktu，Uncle Prudent/Phil Evans 囚，
"rather be in Timbuktu than on the Albatross"）为**富化机会**（Phase 3 RCH2 可 edit 注入 timbuctoo），本轮 breadth 不做。

**Maryland 消歧裁定**：美国州（含 Baltimore），Vernean 核心为 **Gun Club 本部 + Topsy-Turvy 北极拍卖**——
TT auction hall at Baltimore, Maryland（TT-001-040）、left the State of Maryland w/ Nicholl（TT-010-007）、that great city of Maryland（TT-018-003）；
FEM Gun Club established in Baltimore, Maryland（FEM-001-002）、population of Maryland 火炬游行（FEM-003-005）；
BR tobacco from Virginia and Maryland 格拉斯哥仓（BR-001-014）。净 solid = 6（TT×3+FEM×2+BR×1，全州/Baltimore-in-Maryland 确指）。

place 计数 365→366，registry total 1433→1434，unknown 恒 0。
散文首版 max para ≤400（首版即守门）；pn_validator strict 首版即全通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10、queue>10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| maryland | MjhCxx | Topsy-Turvy | real | United States | 6 | 美国州（Baltimore）；Gun Club 本部；TT 北极拍卖；FEM 建会；BR 烟草 |

- **maryland**：6 distinct PN — TT-001-040（Auction Hall at Baltimore, Maryland）/010-007（left the State of Maryland w/ Nicholl）/018-003（that great city of Maryland）、FEM-001-002（club established in Baltimore, Maryland）/003-005（population of Maryland 火炬游行）、BR-001-014（tobacco from Virginia and Maryland）。多源 TT(3)/FEM(2)/BR(1)。链 from-the-earth-to-the-moon/topsy-turvy/the-blockade-runners。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：maryland 全句源自 sentence_index，pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 max para ≤400（首版即守门）。✔
- **G3 ≥5 distinct PN**：6（三源；全 solid）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1434 place 366 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R155 起始计数）

| 字段 | R154 起始 | R155 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 154 | 155 |
| type_round | 125 | 126 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 90 | 91 |
| last_updated_round | 154 | 155 |

## 遗留问题

1. **place 页数 366**：本轮 +1。registry 全库 1434，unknown 0。
2. **⚠ R150 补种批已尽**：5 项处理完（✔Nantucket ✔Tunis ✔Tripoli ✘Timbuktu[重复] ✔Maryland），4 建 1 判重。
   **净 buildable 归零**——下轮起既有 queue 仅剩 sub-gate DEFER/hold 项（Virginia 净4、Louisiana 净3、Abyssinia 净3、
   Indiana 5 勉达、Arkansas/Tennessee <5、Colorado/Michigan 河湖歧义待剥离）。
3. **下轮 R155 = NEW1（名义）但净候选罄**：since_discover=4<10、queue_size 名义>10 → §3(7) NEW1，但净可建≈0。
   R155 须先**复议 DEFER 项能否凑 ≥5 solid**（Virginia 净4 距门 1、Indiana 5 勉达），或对 Colorado/Michigan 逐条剥离河湖，
   若均不成则本轮应触发**手动 SCN28 补种**（since_discover 未达 10，但净可建罄的实务判断——HK-queue-size-scope 情形）。
4. **HK-discover-existing-type-blindspot 再现（R154 Timbuktu）**：SCN28（R150）未比对既有页拼写变体（Timbuktu vs Timbuctoo）。
   教训：SCN28 补种须对每候选做既有页 + alias 双向查重（含拼写/音译变体）。已在 R154 建前捕获，未误建。记 housekeeping。
5. **timbuctoo RC 富化机会**：RC×7 Albatross 掠 Timbuktu 段可 Phase 3 RCH2 注入既有 timbuctoo 页（+囚禁情节）。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **EVV5 节奏**：since_evv5=4→约 R160 触发。
8. **corpus-discover 顺延临界**：since_corpus=90（HK-corpus-discover-not-in-statemachine PARK）；净表层近罄，转 corpus 深扫的实务临界渐近。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
