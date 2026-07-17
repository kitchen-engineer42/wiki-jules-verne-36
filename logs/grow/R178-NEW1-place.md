---
round: 178
date: 2026-07-17
type_round: 149
phase: "2.1"
current_type: place
gene: NEW1
pages: [coanza]
result: success
---

# GROW 2.1-B · R178 · NEW1 · place — Coanza 严剔改判 BUILD（河流地物 referent，Sierra Tandil 先例，净 solid 6+）；DSCF 安哥拉队列建齐收官

## 执行摘要

Phase 2.1-B place 广度扩张第 149 轮（type_round 149）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、streak=0<3、since_discover=7<10、queue(place)>0、stub%=0 → §3(7)）。
承 R175 probe DSCF 安哥拉队列末项 **Coanza**——建前严剔（R175/R176/R177 连续预警「疑河泛指多，大概率 DEFER」）。

**Coanza 严剔改判 BUILD（关键，Sierra Tandil / Lake Tanganyika 地物先例）**：23 distinctPN 全 DSCF。
初判假设候选为「Coanza 沿岸聚落」——若如此则全为 river/riverbank 泛指与「camp on the Coanza」奴营 locus，
净 settlement solid≈0 → 应 DEFER。**但严剔发现主 referent 本身即 Coanza 河（安哥拉一河，025-004 明确
"one of the rivers of Angola, flows into the Atlantic"）**，作为**河流地物 referent** 净 solid 充分：
025-004（安哥拉河/入海口/距沉船 cape 100mi）、025-003（tributaries 泛滥）、027-004（Kazounde 距河口 300mi）、
026-012（河东森林 20mi）、032-046（Livingstone 循右岸至 Lombe 汇流）、019-038（越河穿 devastated 省森林）
= 6 河流地物 solid，另 020-088（Ibn Hamis 奴营距岸 10mi）作 locus 支撑。**改建 coanza 河流 place 页**——
参 Sierra Tandil（山脉 referent 而非 village）、Lake Tanganyika 先例：取 well-attested 地物 referent 建页，
勿因「非聚落」技术性而 DEFER 良好 attested toponym。剔「camp on the Coanza」奴营 locus 泛指（026-014/025-033/027-055 等）。

place 计数 383→384，registry total 1451→1452，unknown 恒 0。
首版 para 2 建前压缩 400→376（"eight days after the departure...at the mercy of" → "eight days on...prey to"）；
全段 ≤400（289/376/378/366）。add_page 一次成型，pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=7<10、queue>0（轮初有 Coanza）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| coanza | xb6249 | Dick Sand: A Captain at Fifteen | real | West Africa | 6 | 安哥拉河流；Alvez 奴隶国腹地水系；Livingstone 循岸/Lombe 汇流；地物 referent 改判 BUILD |

- **coanza**：6 distinct solid 河流地物 PN（全 DSCF）— 025-004（安哥拉一河/入海/距沉船 cape 100mi）/025-003（tributaries 泛滥）/027-004（Kazounde 距河口 300mi）/026-012（河东森林 20mi）/032-046（Livingstone 循右岸至 Lombe 汇流）/019-038（越河穿森林）。020-088 奴营 locus 支撑。DSCF 单源。链 dick-sand-a-captain-at-fifteen。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：coanza 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（289/376/378/366）；para 2 建前压缩 400→376。✔
- **G3 ≥5 distinct PN**：6 河流地物 solid（DSCF 单源，超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；book 含冒号已单引号（LAW §8）。✔
- **registry 一致**：total 1452 place 384 unknown 0。✔
- **查重充分**：feature-aware 双测 coanza 皆 NEW。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R179 起始计数）

| 字段 | R178 起始 | R179 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 178 | 179 |
| type_round | 149 | 150 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 7 | 8 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 114 | 115 |
| last_updated_round | 178 | 179 |

## 遗留问题

1. **place 页数 384**：本轮 +1（Coanza）。registry 全库 1452，unknown 0。
2. **下轮 R179 gene 关口**：DSCF 安哥拉 probe 队列（Loanda/Cassange/Bihe/Coanza）**已建齐收官**，
   净 buildable place 候选=0。§3(3)：queue_size(place)<10 → **R179 大概率 SCN28 discover**（深层补种新矿脉）。
   若 SCN28 复扫产 ≥3 新候选则续 NEW1，否则评估 streak。轮初须实测 queue place 候选数确认 gene。
3. **地物 referent 纪律再证**（承 Sierra Tandil）：候选表面为「沿岸/山下聚落」但净 settlement solid 不足时，
   核主 referent——若地物本体（河/山/湖）well-attested 则改建地物页，勿轻 DEFER。Coanza=第 3 例（Tandil 山脉/Coanza 河）。
4. **DSCF 安哥拉富矿收官**：Loanda(8)/Cassange(6)/Bihe(5)/Coanza(6) 四页 + 既有 Kazounde——
   Dick Sand 安哥拉内陆奴隶贸易 toponym 层产出 4 新页后近饱。HK-premature-saturation-claim 第六度证伪闭环。
5. **建前压缩纪律见效**：R178 para 2 建前 400→376，无建后 edit。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=114→115（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3、Carmen 净3、Mozambique 净0。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
