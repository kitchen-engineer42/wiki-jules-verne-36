---
round: 199
date: 2026-07-17
type_round: 170
phase: "2.1"
current_type: place
gene: NEW1
pages: [new-georgia]
result: success
---

# GROW 2.1-B · R199 · NEW1 · place — 建 New Georgia（AM 亚南极岛/Isle de Saint Pierre，净 solid 8 AM-referent；剔 FC/TTLU 同名异指）

## 执行摘要

Phase 2.1-B place 广度扩张第 170 轮（type_round 170）。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10、since_discover=1<10、queue(place)=2>0、stub%=0 → §3(7)）。

取 R197 discover 队列**建序 3** **New Georgia**（AM）。建前 pages.json 子串双查（georgia/coppermine 皆无既有页），
`the-` 前缀亦无（承 R198 教训扩查）。

**同名异指剔除纪律（承 Far West R196）**：全库 "New Georgia" 11 hits 跨三指——
- **AM 亚南极岛**（本页 referent）：Isle de Saint Pierre / South Georgia / King George's Island，South Atlantic 环极岛。
- **FC 北美 New Georgia**（FC-030-008/FC-030-054/FC-032-023）："that part of North America which is called New Georgia"，
  太平洋西北岸区，猛犸牙采集地——**异指，剔除**。
- **TTLU-019-041**："coast of New Georgia" 沉船残骸，太平洋（Solomon）指向——**异指，剔除**。

本页仅采 AM 亚南极岛 referent，**净 8 distinct solid AM PN**（远超门）：
- **AM-010-020**：Isle de Saint Pierre，英名 South/New Georgia + King George's Island，环极。
- **AM-010-006**：距 Falklands 800 mi，Len Guy 以 Sandwich Isles 为南下起点前先访。
- **AM-009-043**：Polar Circle 渔场介 Sandwich Islands 与 New Georgia 间。
- **AM-020-215**：漂冰山，望遇 Orkneys–New Georgia 深水捕鲸船。
- **AM-025-014**：终弃望于 Sandwich/South Orkneys/South Georgia 水域寻捕鲸船。
- **AM-010-023**：距 Magellan Straits 500 leagues，属 Falklands administrative domain。
- **AM-010-024**：受 Antarctic polar current 直击，海兽频出。
- **AM-010-025**：岛无一树，鸟不需枝栖。

place 计数 398→399，registry total 1466→1467，unknown 恒 0。
add_page 一次成型，awk 全 >399 段预检 0 超段。pn_validator strict ✓；build_registry 仅 Robur PARK（无新 alias 冲突）。
real_or_fictional=real、region South Atlantic Ocean、aliases=[South Georgia, Isle de Saint Pierre, King George's Island]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；queue=2 消费中 | 否 |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 剩余队列：Coppermine River（建序 4，1 项）。R200 建毕队列罄 → R201 SCN28 discover。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| new-georgia | Kopvp7 | An Antarctic Mystery | real | South Atlantic Ocean | 8 | 亚南极岛 Isle de Saint Pierre；剔 FC 北美同名 + TTLU 太平洋同名 |

- **new-georgia**：8 distinct solid AM PN（剔 3 FC + 1 TTLU 同名异指）；aliases [South Georgia, Isle de Saint Pierre, King George's Island]。链 an-antarctic-mystery。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且 VVV=AM 亚南极岛 referent；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（AM referent，剔 FC/TTLU 同名异指）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1467 place 399 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串双查（georgia/coppermine）+ `the-` 前缀（承 R198 教训）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R200 起始计数）

| 字段 | R199 起始 | R200 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 199 | 200 |
| type_round | 170 | 171 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 135 | 136 |
| last_updated_round | 199 | 200 |

## 遗留问题

1. **place 页数 399**：本轮 +1（New Georgia）。registry 全库 1467，unknown 0。
2. **下轮 R200 = NEW1**：since_evv5=6<10、since_discover=2<10、queue(place)=1>0 → §3(7) NEW1。
   建 **Coppermine River**（coppermine-river，ACH+FC×10，北美极地大河，real，Arctic North America）。建前 pages.json 子串 + `the-`/coppermine/copper-mine 变体双查。
3. **R200 建毕队列罄 → R201 SCN28 discover**：R197 补种 4 项中 chimneys 判 DUPLICATE、corral/new-georgia 已建、
   Coppermine River 待建，R200 后队列归零 → §3(3)&§3(4) 触 discover。宜向 FC/AM/AWED/ACH 极地-铁路长尾扩散。
4. **HK-dupcheck-the-prefix-blindspot**：本轮已应用（子串双查 + the- 前缀），无复现。PARK 记录。
5. **同名异指剔除**：本轮 +New Georgia（剔 FC 北美 + TTLU 太平洋同名）；承 Far West（剔 generic American West）纪律。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=135→136（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：17+ place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Fort Enterprise/North·South Mandible/Reptile Point DEFER；
    Medicine Bow/Grant Lake/Prospect Plateau DEFER，Salt Lake/Serpentine/Omaha/Cape Bathurst 等 DUPLICATE 照旧。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
