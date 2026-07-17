---
round: 175
date: 2026-07-16
type_round: 146
phase: "2.1"
current_type: place
gene: NEW1
pages: [saint-paul-de-loanda]
result: success
---

# GROW 2.1-B · R175 · NEW1 · place — Mozambique 建前 DEFER（净 solid 0，全海峡/海岸/省泛指）；同轮 probe 补建 Saint Paul de Loanda（DSCF 安哥拉首府，净 solid 8），DSCF 安哥拉富矿开新

## 执行摘要

Phase 2.1-B place 广度扩张第 146 轮（type_round 146）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、streak=0<3、since_discover=4<10、queue(place)>0、stub%=0 → §3(7)）。
承 R170 SCN28 discover 建序末项 **Mozambique**——建前严剔净 0 DEFER；R170 批消尽、净 buildable=0，
同轮 probe 补矿并建 **Saint Paul de Loanda**（避免空轮，参 Baikal→Tai-Youan / Carmen→Sierra Tandil 同轮改建先例）。

**Mozambique DEFER 裁定（如 R170 预判）**：11 distinctPN 多源（DSCF/FWB/MI/TT/TTLU）。全数为
「Mozambique Channel/canal」（海峡地物：FWB-009-003/011-002、TT-015-020/019-035、TTLU-028-012）、
「Mozambique coast」（海岸泛指：DSCF-004-002/020-073/032-050）、「province of Mozambique」（区域泛指：TT-017-003）、
奴隶贸易方向 enum（DSCF-019-019）、疑误配（MI-030-040 本句无 Mozambique）。**无城本体确指，净 solid 0 → DEFER**。

**同轮 probe 补矿（R170 批尽 → 净 buildable=0，HK-queue-size-scope；不空轮，补建 1）**：
宽扫 FWB/DSCF/SC 未采 toponym。feature-aware 双测命中既有页规避 3：Kilimanjaro/Kazounde/Lake Tanganyika(Tanganyika)。
弃：Tete（24 distinctPN 但净 1——多为「Kara-Tete」毛利酋长人名误配，仅 DSCF-032-051 城确指）、
Msene(1)/Nyangwe(1)/Emboma(3)/Seymour(3)/Tapalquem(3) below-gate。**命中 DSCF 安哥拉内陆·奴隶贸易 toponym 新矿**：
Loanda(15)/Coanza(23)/Bihe(7)/Cassange(7)。

**建 Saint Paul de Loanda（DSCF 单源，净 solid 8 超门）**：15 distinctPN 全 DSCF。取 8 solid：
019-032（葡属殖民地首府）、019-054（Loanda→Zaïre 经 San Salvador 路线）、020-033（penitentiary of Loanda）、
020-076（Alvez 逃犯出 Loanda penitentiary）、025-036（距内陆城 400mi、离 Coanza 营 250mi）、
032-037（跨非斜穿至 Loanda 为目标）、032-046（Livingstone 9/24 离城）、037-030（押解至 Loanda 终老 penitentiary）。
slug saint-paul-de-loanda，label「Saint Paul de Loanda」，alias Loanda。feature-aware 双测 loanda/saint-paul-de-loanda 皆 NEW。

place 计数 380→381，registry total 1448→1449，unknown 恒 0。
首版全段 ≤400（269/364/318/344），add_page 一次成型。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=4<10、queue>0（轮初）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 注：轮初 queue 有 Mozambique（nominal>0）故 §3(7) NEW1；轮中 Mozambique DEFER 致净 buildable=0，
> 同轮 probe 补矿建 1（不转 SCN28，保持 NEW1 productive round），新候选入队待后续。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| saint-paul-de-loanda | X7MihS | Dick Sand: A Captain at Fifteen | real | West Africa | 8 | 葡属安哥拉首府/港；Livingstone 跨非终点；penitentiary |
| ~~mozambique~~ | — | — | — | — | — | **DEFER**：净 solid 0（全 Channel/coast/province 泛指）|

- **saint-paul-de-loanda**：8 distinct solid PN（全 DSCF）— 019-032（葡属殖民地首府）/019-054（→Zaïre 经 San Salvador）/020-033（penitentiary of Loanda）/020-076（Alvez 逃犯出 penitentiary）/025-036（距内陆 400mi/离 Coanza 营 250mi）/032-037（跨非目标）/032-046（Livingstone 9/24 离城）/037-030（押解终老 penitentiary）。DSCF 单源。链 dick-sand-a-captain-at-fifteen。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：saint-paul-de-loanda 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（269/364/318/344）。✔
- **G3 ≥5 distinct PN**：8（DSCF 单源，净 solid 8 超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；book 含冒号已单引号（LAW §8）。✔
- **registry 一致**：total 1449 place 381 unknown 0。✔
- **查重充分**：feature-aware 双测 loanda/saint-paul-de-loanda 皆 NEW；probe 命中既有 3 页规避。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R176 起始计数）

| 字段 | R175 起始 | R176 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 175 | 176 |
| type_round | 146 | 147 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 111 | 112 |
| last_updated_round | 175 | 176 |

## 遗留问题

1. **place 页数 381**：本轮 +1（Saint Paul de Loanda）。Mozambique DEFER 未建。registry 全库 1449，unknown 0。
2. **下轮 R176 = NEW1**：since_evv5=4<10、since_discover=5<10、queue>0（R175 补种 Coanza/Bihe/Cassange）→ §3(7) NEW1。
   建 **Bihe** 或 **Cassange**（DSCF 安哥拉内陆商站，各 7 distinctPN，建前抽样 ≥5 solid）；Coanza 河 referent 需先严剔。
3. **R170 discover 建序收官**：✔Kazeh → ✔Gondokoro → ✘Carmen(DEFER) → ✔Sierra Tandil → ✘Mozambique(DEFER)。
   5 候选 → 3 建 + 2 DEFER。R175 同轮 probe 补矿 Loanda + 入队 3。
4. **DSCF 安哥拉富矿开新（place 未饱和第 6 次证实）**：Loanda(8)+queue Coanza/Bihe/Cassange——
   Dick Sand 安哥拉内陆·奴隶贸易 toponym 层为继 FWB 尼罗河后又一新富矿。HK-premature-saturation-claim 第六度证伪。
5. **误配纪律（承 Tandil/lake-baikal）**：Tete 24 distinctPN 表面高，实为「Kara-Tete」毛利酋长人名误配（\bTete\b 命中连字符名），
   净城 solid 仅 1——distinctPN 高不等于地确指高，word-boundary 命中须核 referent（人名/地名混淆）。
6. **建前压缩纪律见效**：R175 首版即全段 ≤400，无建后 edit。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
8. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
9. **corpus-discover 顺延**：since_corpus=111→112（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3、Carmen 净3、**Mozambique 净0**；Coanza 待判。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
