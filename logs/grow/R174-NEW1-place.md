---
round: 174
date: 2026-07-16
type_round: 145
phase: "2.1"
current_type: place
gene: NEW1
pages: [sierra-tandil]
result: success
---

# GROW 2.1-B · R174 · NEW1 · place — Carmen 建前 DEFER（净 solid 3）；Tandil 消歧改建 sierra-tandil（山脉主体 referent，净 solid 8）

## 执行摘要

Phase 2.1-B place 广度扩张第 145 轮（type_round 145）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、streak=0<3、since_discover=3<10、queue(place)>0、stub%=0 → §3(7)）。
承 R170 SCN28 discover 建序，第 3 项预定 **Carmen**——建前复核未达门 DEFER，同轮消歧改建 **Sierra Tandil**。

**Carmen DEFER 裁定（承 Brindisi/Yeniseisk/Tioumen 纪律）**：7 distinctPN 全 SC。剔 009-019
（Magellan/Fuegian/Chilian/colonists of Carmen Tehuelches… 命名 enum，「colonists of Carmen」为 demonym 源非地确指）；
016-018「The Carmen route.」/016-027「going to Carmen?」/016-032「Carmen or Mendoza」皆同章 ch.16「Carmen route」
薄对话重复（同一「去 Carmen 还是 Mendoza」问答线）。仅 016-019（route from Carmen to Mendoza）、
016-041（Carmen route 跨经纬/两洋）、021-062（traders between Tandil and Carmen, at the mouth of the Rio Negro）
三处 solid。**净 3 < 5 门 → DEFER**（Carmen de Patagones 语料仅作路线东端/Rio Negro 口点，未足描述城本体）。

**Tandil 消歧改建 sierra-tandil（关键，参 Concepcion 城 vs 地物先例）**：8 distinctPN 全 SC。
消歧裁定——**village of Tandil** 仅 020-044（Glenarvan 决往 village of Tandil）、021-059（at Tandil 知情）两处，净 2<门；
但主体 referent 为 **Sierra Tandil**（山脉）：010-043（越 Sierra Tandil 赴 Point Medano）、020-041（Sierra Tandil 距 60mi）、
020-056（Sierra Tandil 首见 estancias）、021-001（Sierra Tandil 高出海平 1000 尺）、021-062（Sierra Tandil 与 Carmen 间无 Grant 踪）
五 solid + 026-012（Tandil/Tapalquem Sierras 稀树）。**建为 sierra-tandil place 页**（label「Sierra Tandil」，
巴塔哥尼亚潘帕斯山脉），净 solid 8 远超门。feature-aware 查重 tandil/sierra-tandil 两式皆 NEW。

place 计数 379→380，registry total 1447→1448，unknown 恒 0。
首版全段 ≤400（259/321/349/336/262），add_page 一次成型。pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10、queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| sierra-tandil | 5IPFBo | In Search of the Castaways | real | Patagonia | 8 | 潘帕斯山脉，高 1000 尺；越山赴 Point Medano；Tandil 消歧取 Sierra 主体 |
| ~~carmen~~ | — | — | — | — | — | **DEFER**：净 solid 3（剔 009-019 命名 enum + ch.16 薄对话重复）|
| ~~tandil(village)~~ | — | — | — | — | — | 净 solid 2；改建 sierra-tandil 山脉主体 |

- **sierra-tandil**：8 distinct solid PN（全 SC）— 021-001（高出海平 1000 尺）/010-043（越 Sierra Tandil 赴 Point Medano）/020-041（距 60mi）/020-044（往 village of Tandil）/020-056（首见 estancias）/021-062（Sierra Tandil 与 Carmen 间/Rio Negro 口 traders）/021-059（at Tandil 知情）/026-012（Tandil/Tapalquem Sierras 稀树）。SC 单源。链 in-search-of-the-castaways。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：sierra-tandil 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（259/321/349/336/262）。✔
- **G3 ≥5 distinct PN**：8（SC 单源，Sierra 主体 5 solid + village/enum 支撑 3）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry 一致**：total 1448 place 380 unknown 0。✔
- **查重充分**：feature-aware 双测 tandil/sierra-tandil 皆 NEW；Carmen 建前 re-vet 判 DEFER。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R175 起始计数）

| 字段 | R174 起始 | R175 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 174 | 175 |
| type_round | 145 | 146 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 110 | 111 |
| last_updated_round | 174 | 175 |

## 遗留问题

1. **place 页数 380**：本轮 +1（Sierra Tandil）。Carmen DEFER 未建。registry 全库 1448，unknown 0。
2. **下轮 R175 = NEW1**：since_evv5=3<10、since_discover=4<10、queue>0 → §3(7) NEW1。
   建 R170 discover 建序末项 **Mozambique**（11 distinctPN 多源；**建前严剔**：多为「Mozambique coast/channel」
   海岸海峡区域泛指，疑 <5 clean solid，大概率 DEFER）。若 DEFER 则 R170 批消尽、净 buildable=0 → R176 转 SCN28 深层补种。
3. **R170 discover 建序进度**：✔Kazeh → ✔Gondokoro → ✘Carmen(DEFER) → ✔Sierra Tandil；余 Mozambique(严剔待定)。
   5 候选 → 3 建 + 1 DEFER + 1 待定。
4. **消歧纪律见效**：Tandil village(净2) vs Sierra Tandil(净5+) 分离，取 well-grounded referent 建页——
   避免为技术性 village-only 而 DEFER 良好 attested toponym（参 Concepcion 城 vs 地物先例）。
5. **建前压缩纪律见效**：R174 首版即全段 ≤400，无建后 edit。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=110→111（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3、**Carmen 净3**；待定 Mozambique。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
