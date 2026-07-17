---
round: 168
date: 2026-07-16
type_round: 139
phase: "2.1"
current_type: place
gene: NEW1
pages: [lan-tcheou]
result: success
---

# GROW 2.1-B · R168 · NEW1 · place — 建 lan-tcheou（ASC 单源 8PN，Grand Transasiatic 华属段重镇/皇帝宝藏电报站）

## 执行摘要

Phase 2.1-B place 广度扩张第 139 轮（type_round 139）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、streak=0<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。
承 R166 SCN28 discover 建序（Sou-Tcheou→**Lan-Tcheou**→Baikal→Tai-Youan），建第 2 项 Lan-Tcheou。

**消歧裁定**：Lan-Tcheou = Grand Transasiatic 华属段重镇（Sou-Tcheou 东 700km），Vernean 归属**全在《The
Adventures of a Special Correspondent》**——700km 外重镇（ASC-023-003）、26 May 7am 抵（023-036）、
governor 奉 Pekin 令电报皇帝宝藏抵站待送京或暂存 Lan-Tcheou（023-042）、narrator 决意访城（023-048）、
Caterna 于离站问妻所见（023-070）、长城「descending SE toward Lan-Tcheou」转 NE 之 bend（022-072）、
离城铁路穿沃野多曲（024-001）、自 Lan-Tcheou 发电报至京城次晨得复（027-062）。
净 solid = 8（全 ASC 单源，城主体确指；022-072 内省列举 Kian-Sou/Chan-si/Petchili 剔，仅取 Lan-Tcheou 长城 bend 确指）。

place 计数 375→376，registry total 1443→1444，unknown 恒 0。
**建前压缩**（承 R167 纪律）：首版 Overview 422、Geography 419 超 G2 门 → 建前即压缩 ≤400（末版 394/361/267/344/379），
add_page 一次成型，无建后 edit 往返。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、R166 补种 queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| lan-tcheou | y7G5Ej | The Adventures of a Special Correspondent | real | China | 8 | 华属段重镇；皇帝宝藏电报站；长城 bend |

- **lan-tcheou**：8 distinct solid PN — ASC-023-003（700km 重镇）/023-036（26 May 7am 抵）/023-042（governor 电报皇帝宝藏）/023-048（访城）/023-070（离站所见）/022-072（长城 bend）/024-001（离城铁路穿沃野）/027-062（自城发电报京城复）。ASC 单源。链 the-adventures-of-a-special-correspondent。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：lan-tcheou 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 Overview 422/Geography 419 超门 → 建前压缩；末版全段 ≤400（394/361/267/344/379）。✔
- **G3 ≥5 distinct PN**：8（ASC 单源，全 solid；022-072 剔内省列举仅取城 bend 确指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1444 place 376 unknown 0。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R169 起始计数）

| 字段 | R168 起始 | R169 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 168 | 169 |
| type_round | 139 | 140 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 104 | 105 |
| last_updated_round | 168 | 169 |

## 遗留问题

1. **place 页数 376**：本轮 +1（Lan-Tcheou）。registry 全库 1444，unknown 0。
2. **下轮 R169 = NEW1**：since_evv5=8<10、since_discover=2<10、queue>0 → §3(7) NEW1。
   建 **Baikal**（R166 discover 序第 3，MS Lake Baikal，17 distinctPN；**⚠ 建前严剔**：多处「Lake Baikal provinces」省区泛指/省列举须剔，确认净 ≥5 solid 湖体确指；湖非城，参 Michigan/Colorado 湖河消歧先例，若净 <5 clean solid 则 DEFER）。
3. **R166 discover 建序进度**：✔Sou-Tcheou → ✔Lan-Tcheou → **Baikal**(下轮 re-vet) → Tai-Youan(re-vet)；Yeniseisk/Tioumen 建前严剔。
4. **净 buildable**：R166 补 6 项，消 2（Sou-Tcheou/Lan-Tcheou），余 4（Baikal/Tai-Youan/Yeniseisk/Tioumen，均 re-vet）。
5. **建前压缩纪律见效**：R167 建后拆段 1 次 edit；R168 首版即压缩，一次成型。ASC 城页信息密度高，续用建前压缩。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页末版 over-400=0。
7. **EVV5 节奏**：since_evv5=7→8，约 R171 触发（since_evv5 达 10）。
8. **corpus-discover 顺延**：since_corpus=104→105（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、Colorado/Michigan 河湖歧义；R166 待定 Yeniseisk/Tioumen。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
