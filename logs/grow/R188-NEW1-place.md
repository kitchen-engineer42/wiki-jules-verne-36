---
round: 188
date: 2026-07-17
type_round: 159
phase: "2.1"
current_type: place
gene: NEW1
pages: [reptile-end]
result: success
---

# GROW 2.1-B · R188 · NEW1 · place — 建 Reptile End（MI Lincoln Island 西南岬，净 solid 10）

## 执行摘要

Phase 2.1-B place 广度扩张第 159 轮（type_round 159）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10、since_discover=1<10、queue(place)=4>0、stub%=0 → §3(7)）。
取 R187 discover 批次首项 **Reptile End**（MI×16）。文件系统查重 reptile-end/reptile-point 皆 NEW。

**Reptile End（MI 单源，净 solid 10 远超门）**：Lincoln Island 西南端之岬，与东南 Claw Cape 对峙，定界殖民者勘探之南岸。
sentence_index 命中 16 distinctPN（含 SI-* 异版重复文本，按 MI 主码计），取 10 solid：
- **MI-023-052**：南岸自 Claw Cape（东南）至 Reptile End（西南）。
- **MI-034-082**：海岸全景一端，Claw Cape 至 Reptile End。
- **MI-026-035**：Falls River 至 Reptile End 之岸尽为林。
- **MI-026-038**：距 Falls River 约 12 英里。
- **MI-026-042**：约七时探险者抵 Reptile End。
- **MI-041-039**：Bonadventure 离 Port Balloon 抢风驶抵此岬。
- **MI-013-065**：目光半圆自岬扫至 Reptile End。
- **MI-035-024**：离岸约十英里，约一小时驶过。
- **MI-053-023**：勘探 Washington Bay 岸 Claw Cape 至 Reptile End。
- **MI-054-001**：2 月 18 日勘 Reptile End 至 Falls River 之林岸。
- **MI-038-099**：Herbert 于此岬遇美洲豹（前有一豹被杀于此）。

place 计数 390→391，registry total 1458→1459，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版最长 394，未触 HK-addpage-prose-gate-bypass）。pn_validator strict 建后即通过；
build_registry 仅余既有 Robur alias 告警（PARK）。real_or_fictional=fictional、region=Lincoln Island（与姊妹页 claw-cape/shark-gulf/flotsam-point 一致）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10；queue=4（新鲜补种冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=4<10 名义达 discover 条件，但 R187 刚补种、since_discover=1 冷却中，续 NEW1 消费新候选（承 R183–R186 判据）。
> 队列剩 3（Reptile End 后 Vanikoro/Tadorn Marsh/New America）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| reptile-end | 9fFU2T | The Mysterious Island | fictional | Lincoln Island | 10 | Lincoln Island 西南岬；Claw Cape 对峙；殖民者南岸勘探界 |

- **reptile-end**：10 distinct solid PN（MI 单源）；无 alias。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：reptile-end 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：一次成型，首版最长 394。✔
- **G3 ≥5 distinct PN**：10 solid（MI 单源，远超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1459 place 391 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 后缀变体（reptile-end/reptile-point）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R189 起始计数）

| 字段 | R188 起始 | R189 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 188 | 189 |
| type_round | 159 | 160 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 124 | 125 |
| last_updated_round | 188 | 189 |

## 遗留问题

1. **place 页数 391**：本轮 +1（Reptile End）。registry 全库 1459，unknown 0。
2. **下轮 R189 = NEW1**：since_evv5=7<10、since_discover=1<10、queue=3>0 → §3(7) NEW1。
   建 **Vanikoro**（TTLU/20KL×14，La Pérouse 沉没岛，Nautilus 访），建前文件系统查重（vanikoro/-island/-islands）+ 抽样 ≥5 solid。
3. **R189+ 建序（R187 批剩 3）**：Vanikoro → Tadorn Marsh → New America（3 项后队列罄，须再 SCN28 discover）。
4. **EVV5 临近**：since_evv5=7，R189–R191 建 3 项后约 R192 触 EVV5（since_evv5=10）。
5. **HK-addpage-prose-gate-bypass**：本轮一次成型未触；续常规 awk 段长复检。
6. **主矿脉盘点**：MI 密集地名网续掘（Reptile End 本轮，Tadorn Marsh 待）；20KL Vanikoro、ACH New America 待。未宣布饱和。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=124→125（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Cape Mandible（overlap mandible-cape）/Indian Peninsula/Balearic Isles DEFER；既有
    Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、
    Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
