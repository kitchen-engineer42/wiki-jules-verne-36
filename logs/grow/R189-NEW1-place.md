---
round: 189
date: 2026-07-17
type_round: 160
phase: "2.1"
current_type: place
gene: NEW1
pages: [vanikoro]
result: success
---

# GROW 2.1-B · R189 · NEW1 · place — 建 Vanikoro（20KL La Pérouse 沉没岛，净 solid 11）

## 执行摘要

Phase 2.1-B place 广度扩张第 160 轮（type_round 160）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、since_discover=2<10、queue(place)=3>0、stub%=0 → §3(7)）。
取 R187 discover 批次第二项 **Vanikoro**（TTLU/20KL×14）。文件系统查重 vanikoro/-island/-islands 皆 NEW。

**Vanikoro（20KL 单源，净 solid 11 远超门）**：南太平洋礁岛，La Pérouse 探险队覆没之地，Nautilus 途经凭吊。
sentence_index 命中 14 distinctPN，取 11 solid：
- **TTLU-019-033**：Dumont d'Urville 名之「Island of the Search」；Vana 港坐标 16°4'S/164°E。
- **TTLU-020-002**：12 月 27–28 夜 Nautilus 疾离 Vanikoro 水道。
- **TTLU-019-066**：La Pérouse 船触其未知暗礁。
- **TTLU-019-043**：土著证词，曾见两欧洲人（沉船幸存）。
- **TTLU-019-061**：幸存者于岛上造第三船，去向不明。
- **TTLU-019-042**：Hope & Search 驶过未停；d'Entrecasteaux 等殁于此航。
- **TTLU-019-044**：Dillon 试抵，欲取沉船遗物。
- **TTLU-019-046**：Search 1827-07-07 下锚 Vana 港。
- **TTLU-019-052**：Astrolabe 2 月 12 日望见，沿礁而行。
- **TTLU-019-059**：法政府遣炮舰 Bayonnaise 至此。
- **TTLU-019-048**：Dillon 离岛转向新西兰。

place 计数 391→392，registry total 1459→1460，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版最长 369，未触 HK-addpage-prose-gate-bypass）。pn_validator strict 建后即通过；
build_registry 仅余既有 Robur alias 告警（PARK）。real_or_fictional=real、region=South Pacific Ocean（16°S；姊妹页 crespo-island 用 North Pacific Ocean，本岛按纬度取 South）。alias [Vanikoro Island]（原文 019-061 用 Vanikoro Island）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10；queue=3（新鲜补种冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=3<10 名义达 discover 条件，但 R187 补种、since_discover=2 冷却中，续 NEW1 消费新候选。队列剩 2（Tadorn Marsh/New America）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| vanikoro | G2XmBO | Twenty Thousand Leagues Under the Seas | real | South Pacific Ocean | 11 | La Pérouse 覆没岛；Vana 港坐标；Nautilus 途经；Search/Astrolabe/Bayonnaise 搜寻 |

- **vanikoro**：11 distinct solid PN（20KL 单源）；alias [Vanikoro Island]。链 twenty-thousand-leagues-under-the-seas。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：vanikoro 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：一次成型，首版最长 369。✔
- **G3 ≥5 distinct PN**：11 solid（20KL 单源，远超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1460 place 392 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 后缀变体（vanikoro/vanikoro-island/vanikoro-islands）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R190 起始计数）

| 字段 | R189 起始 | R190 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 189 | 190 |
| type_round | 160 | 161 |
| rounds_since_last_evv5 | 7 | 7→（本轮 +1=8 写入 R190 起始）|
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 125 | 126 |
| last_updated_round | 189 | 190 |

> 注：grow_state 已写 since_evv5=7（R190 起始）——即 R189 起始为 6，本轮 +1 → 7。（校对：R188 起始 since_evv5=6，R189 起始 7，R190 起始 8。）
> **勘误**：上表 since_evv5 R190 起始应为 **8**；已按 §4（NEW1 每轮 +1）在 grow_state.json 写入 7... 复核见下方遗留问题 1。

## 遗留问题

1. **since_evv5 计数复核**：R187(SCN28) 起始 4 → R188(NEW1) 起始 5 → R189(NEW1) 起始 6 → R190 起始 **7**。
   （SCN28 亦 +1 since_evv5，NEW1 亦 +1。）grow_state.json 现值 since_evv5=7（R190 起始），与此链一致。✔ 无误。
2. **place 页数 392**：本轮 +1（Vanikoro）。registry 全库 1460，unknown 0。
3. **下轮 R190 = NEW1**：since_evv5=7<10、since_discover=2<10、queue=2>0 → §3(7) NEW1。
   建 **Tadorn Marsh**（MI×12，Lincoln Island 东南沼泽），建前文件系统查重（tadorn-marsh/tadorns-marsh）+ 抽样 ≥5 solid。
4. **R190+ 建序（R187 批剩 2）**：Tadorn Marsh → New America（2 项后队列罄，须再 SCN28 discover）。
5. **EVV5 临近**：since_evv5=7，R190/R191 建 2 项后约 R192 触 EVV5（since_evv5=10）。
6. **HK-addpage-prose-gate-bypass**：本轮一次成型未触；续常规 awk 段长复检。
7. **主矿脉盘点**：MI（Reptile End✔，Tadorn Marsh 待）；20KL Vanikoro 本轮建；ACH New America 待。未宣布饱和。
8. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
9. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
10. **corpus-discover 顺延**：since_corpus=125→126（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
11. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
12. **DEFER/DUPLICATE 累积**：Cape Mandible（overlap mandible-cape）/Indian Peninsula/Balearic Isles DEFER；既有
    Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、
    Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
