---
round: 195
date: 2026-07-17
type_round: 166
phase: "2.1"
current_type: place
gene: NEW1
pages: [jacamar-wood]
result: success
---

# GROW 2.1-B · R195 · NEW1 · place — 建 Jacamar Wood（MI Lincoln Island Mercy 左岸林，净 solid 13；R192 队列第二项）

## 执行摘要

Phase 2.1-B place 广度扩张第 166 轮（type_round 166）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、since_discover=2<10、queue(place)=2>0、stub%=0 → §3(7)）。
取 R192 discover 批次**第二项** **Jacamar Wood**（MI×24 distinctPN）。文件系统查重 jacamar-wood/jacamar-woods/jacamar 皆 NEW，alias_index 无占用。

**Jacamar Wood（MI 单源，净 solid 13 远超门）**：Lincoln Island Mercy 左岸密林，猎 jacamar 鸟得名，殖民地早期唯一猎场。
sentence_index 命中 24 distinctPN，取 13 solid：
- **MI-013-033**：命名——remembrance of jacamar 鸟，Mercy 左岸林。
- **MI-053-022**：位于 road to corral 与 Mercy 之间，近 Lake Grant。
- **MI-019-024**：无桥/舟前，仅此左岸猎场。
- **MI-015-033**：道穿林，斜行东南→西北，最密处。
- **MI-030-011**：远征采野菜（菠菜/水芹/萝卜）。
- **MI-043-072**：取林缘枝蔓伪装 Granite House 窗。
- **MI-025-028**：含于 Far West 林延展至目不能及。
- **MI-055-062**：Mercy 受林下泉源补给。
- **MI-061-035**：Mount Franklin 东坡；虽密林亦恐火山急流达 Prospect Heights。
- **MI-022-026**：风暴中闻林中怒号。
- **MI-051-084**：Mercy 与湖间之林段道荒。
- **MI-061-030**：Red Creek 与林之泉遭岩浆威胁。
- **MI-051-001**：Herbert 负伤，穿林通行艰。

place 计数 395→396，registry total 1463→1464，unknown 恒 0。
add_page 建后首版 Connections 段 439>400，edit_page 拆段修正（rev ahorWV→xixArG，最长 379）；HK-addpage-prose-gate-bypass 记债（add_page 不强制 400 门，awk 预检漏判该段——修正见遗留 5）。
pn_validator strict 修后即通过；build_registry 仅 Robur PARK 告警。real_or_fictional=fictional、region=Lincoln Island。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10；queue=2（R192 补种冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=2<10 名义达 discover 条件，但 R192 补种、since_discover=2 冷却中，续 NEW1 消费。队列剩 1（Far West）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| jacamar-wood | xixArG | The Mysterious Island | fictional | Lincoln Island | 13 | Mercy 左岸密林；jacamar 鸟命名；早期唯一猎场；泉源补 Mercy |

- **jacamar-wood**：13 distinct solid PN（MI 单源）；无 alias。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：jacamar-wood 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 Connections 段 439 超门，edit_page 拆段后最长 379。✔（修正达标）
- **G3 ≥5 distinct PN**：13 solid（MI 单源，远超门）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 修，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1464 place 396 unknown 0；本轮无新 alias 告警（仅 Robur PARK）。✔
- **查重充分**：文件系统 + 后缀变体（jacamar-wood/jacamar-woods/jacamar）+ alias_index。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R196 起始计数）

| 字段 | R195 起始 | R196 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 195 | 196 |
| type_round | 166 | 167 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 131 | 132 |
| last_updated_round | 195 | 196 |

## 遗留问题

1. **place 页数 396**：本轮 +1（Jacamar Wood）。registry 全库 1464，unknown 0。
2. **下轮 R196 = NEW1**：since_evv5=2<10、since_discover=3<10、queue=1>0 → §3(7) NEW1。
   建 **Far West**（far-west，MI-referent×33，Serpentine Peninsula 密林区），建前文件系统查重（far-west/far-west-forests）+ **仅取 MI Lincoln Island 林区指**，剔 generic American West 21 hits。
3. **R196 后队列罄**：R192 批 3 项（The Mercy/Jacamar Wood/Far West）R194–R196 建齐，R196 建毕 queue=0 → R197 须再 SCN28 discover。
4. **Far West 混指剔除纪律（R196 建页重点）**：54 distinctPN 中仅 33 为 MI Lincoln Island 林区指，
   21 为 generic American West（AM/ASC/AWED/EHLA），建页逐句核 VVV=MI 且指 Lincoln Island 林区，避免 wrong-referent。
5. **HK-addpage-prose-gate-bypass 再现**：本轮 add_page 首版 Connections 段 439 未被拦截（add_page 无 400 门），
   awk 预检当轮遗漏该段（拆段后仍 439，系 Edit 定位错段——已 edit_page 补正）。教训：awk 预检须打印**所有** >399 段并逐一核，勿只看 top-N 首行。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页修正后 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=131→132（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：17 place 页 quality=none（R193 EVV5 登记），full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：Medicine Bow/Reptile Point/Grant Lake/Prospect Plateau DEFER、Salt Lake/Serpentine DUPLICATE；
    既有 Cape Mandible/Indian Peninsula/Balearic Isles DEFER，Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen 等 DUPLICATE 照旧。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
