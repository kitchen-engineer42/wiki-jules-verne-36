---
round: 190
date: 2026-07-17
type_round: 161
phase: "2.1"
current_type: place
gene: NEW1
pages: [tadorn-marsh]
result: success
---

# GROW 2.1-B · R190 · NEW1 · place — 建 Tadorn Marsh（MI Lincoln Island 东南沼泽，净 solid 7）

## 执行摘要

Phase 2.1-B place 广度扩张第 161 轮（type_round 161）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、since_discover=3<10、queue(place)=2>0、stub%=0 → §3(7)）。
取 R187 discover 批次第三项 **Tadorn Marsh**（MI×12）。文件系统查重 tadorn-marsh/tadorns-marsh 皆 NEW。

**Tadorn Marsh（MI 单源，净 solid 7 超门）**：Lincoln Island 东南部广袤沼泽，水禽猎场，岛遭劫后野兽避难之所。
sentence_index 命中 12 distinctPN（含 SI-* 异版重复），取 7 solid：
- **MI-033-074**：8 月 3 日往岛东南 Tadorn Marsh 之远征。
- **MI-053-022**：东岸熟知之域，Claw Cape 至 Mandible Capes，广袤 Tadorn Marsh，近 Lake Grant。
- **MI-042-075**：冰期于广沼作狩猎游。
- **MI-054-004**：逃犯自 Flotsam Point 登陆，穿 Tadorn Marsh 入 Far West。
- **MI-061-060**：兽群逃至 Mercy 岸与 Tadorn Marsh，越 Port Balloon 路。
- **MI-061-078**：幸存兽仅 Tadorn Marsh 可避，少数栖 Prospect Heights。
- **MI-061-062**：岛劫后残林较 Tadorn Marsh 更荒。

place 计数 392→393，registry total 1460→1461，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版最长 361，未触 HK-addpage-prose-gate-bypass）。pn_validator strict 建后即通过；
build_registry 无 alias 告警（Robur 本轮未复现——registry 输出仅 [ok]）。real_or_fictional=fictional、region=Lincoln Island（与姊妹页 reptile-end/claw-cape 一致）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10；queue=2（新鲜补种冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=2<10 名义达 discover 条件，但 R187 补种、since_discover=3 冷却中，续 NEW1 消费末批。队列剩 1（New America）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tadorn-marsh | RK87bB | The Mysterious Island | fictional | Lincoln Island | 7 | Lincoln Island 东南沼泽；水禽猎场；岛劫野兽避难所 |

- **tadorn-marsh**：7 distinct solid PN（MI 单源）；无 alias。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tadorn-marsh 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：一次成型，首版最长 361。✔
- **G3 ≥5 distinct PN**：7 solid（MI 单源，超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1461 place 393 unknown 0；本轮无 alias 告警。✔
- **查重充分**：文件系统 + 后缀变体（tadorn-marsh/tadorns-marsh）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R191 起始计数）

| 字段 | R190 起始 | R191 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 190 | 191 |
| type_round | 161 | 162 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 126 | 127 |
| last_updated_round | 190 | 191 |

## 遗留问题

1. **place 页数 393**：本轮 +1（Tadorn Marsh）。registry 全库 1461，unknown 0。
2. **下轮 R191 = NEW1**：since_evv5=8<10、since_discover=3<10、queue=1>0 → §3(7) NEW1。
   建 **New America**（ACH×7，Altamont 命名极地大陆/岛），建前文件系统查重（new-america/new-america-continent）+ 抽样 ≥5 solid。
3. **R191 后队列罄**：R187 批 4 项（Reptile End/Vanikoro/Tadorn Marsh/New America）本轮建 3，剩 New America。R191 建毕须再 SCN28。
4. **EVV5 临近**：since_evv5=8，R191 NEW1 后 since_evv5=9；R192 起始将达 10 → **R192 触 EVV5**（除非 R192 先 SCN28）。
   注：R191 建 New America 后队列=0 → R192 §3 首匹配须复核：since_evv5=9<10 未达 EVV5，但 queue=0 → §3(3)/(4) SCN28 discover 先于 EVV5。R192 = SCN28。R193 起始 since_evv5=10 → R193 EVV5。
5. **HK-addpage-prose-gate-bypass**：本轮一次成型未触；续常规 awk 段长复检。
6. **主矿脉盘点**：MI（Reptile End✔/Tadorn Marsh✔）；20KL Vanikoro✔；ACH New America 待。MI 仍有中频未采层，R192 discover 续掘。未宣布饱和。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=126→127（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Cape Mandible（overlap mandible-cape）/Indian Peninsula/Balearic Isles DEFER；既有
    Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、
    Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
