---
round: 194
date: 2026-07-17
type_round: 165
phase: "2.1"
current_type: place
gene: NEW1
pages: [mercy-river]
result: success
---

# GROW 2.1-B · R194 · NEW1 · place — 建 The Mercy（MI Lincoln Island 主河，净 solid 14 极充；R192 队列首项）

## 执行摘要

Phase 2.1-B place 广度扩张第 165 轮（type_round 165）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10、since_discover=1<10、queue(place)=3>0、stub%=0 → §3(7)）。
取 R192 discover 批次**首项** **The Mercy**（MI×168 distinctPN）。文件系统查重 mercy-river/the-mercy/mercy 皆 NEW，alias_index 无占用。

**The Mercy（MI 单源，净 solid 14 远超门）**：Lincoln Island 主河，感 Providence 恩命名，贯穿岛之内陆水文网。
sentence_index 命中 168 distinctPN，取 14 solid：
- **MI-011-074**：命名——感 Providence 恩取名 the Mercy，供饮水、近 balloon 抛落处。
- **MI-019-011**：河口位于 Chimneys 突岩与崖之间。
- **MI-012-069**：Chimneys 由河之首折 elbow 折返。
- **MI-012-070**：左岸抵 Chimneys。
- **MI-013-028**：循岸穿 Prospect Heights 达 Lake Grant 近旁林隙。
- **MI-023-033**：造平底独木舟航河、探源。
- **MI-025-008**：晨六时独木舟启碇赴河口。
- **MI-023-055**：源隐于山，course/source 不可考。
- **MI-025-056**：午后四时水路为水生植物/礁石所阻，航行艰。
- **MI-021-003**：冬季河口积冰，Lake Grant 全冻。
- **MI-020-027**：河口成牡蛎床。
- **MI-013-033**：左岸即 Jacamar Wood。
- **MI-012-013**：循河穿 Far West 林 / Lake Grant 路达 Prospect Heights 与 Union Bay。
- **MI-016-012**：Granite House 居 Mercy 与 Lake Grant 之间，地利。

place 计数 394→395，registry total 1462→1463，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版 3 段 >400：526/436/413，awk 预检拦截；blank-line 拆段 + trim 后最长 378，未触 HK-addpage-prose-gate-bypass）。
pn_validator strict 建后即通过；build_registry 仅 Robur PARK 告警。real_or_fictional=fictional、region=Lincoln Island（与姊妹页 reptile-end/tadorn-marsh 一致）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10；queue=3（R192 新鲜补种冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=3<10 名义达 discover 条件，但 R192 补种、since_discover=1 冷却中，续 NEW1 消费。队列剩 2（Jacamar Wood/Far West）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| mercy-river | flRplu | The Mysterious Island | fictional | Lincoln Island | 14 | Lincoln Island 主河；Providence 恩命名；左岸 Jacamar Wood；口成牡蛎床/冬冻 |

- **mercy-river**：14 distinct solid PN（MI 单源）；无 alias。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。label "The Mercy"。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：mercy-river 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版 3 段超（526/436/413），awk 预检拦截，拆段 + trim 后最长 378。✔
- **G3 ≥5 distinct PN**：14 solid（MI 单源，远超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1463 place 395 unknown 0；本轮无新 alias 告警（仅 Robur PARK）。✔
- **查重充分**：文件系统 + 后缀变体（mercy-river/the-mercy/mercy）+ alias_index。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R195 起始计数）

| 字段 | R194 起始 | R195 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 194 | 195 |
| type_round | 165 | 166 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 130 | 131 |
| last_updated_round | 194 | 195 |

## 遗留问题

1. **place 页数 395**：本轮 +1（The Mercy）。registry 全库 1463，unknown 0。
2. **下轮 R195 = NEW1**：since_evv5=1<10、since_discover=2<10、queue=2>0 → §3(7) NEW1。
   建 **Jacamar Wood**（jacamar-wood，MI×24，Mercy 左岸林），建前文件系统查重（jacamar-wood/jacamar-woods）+ 抽样 ≥5 solid。
3. **R195–R196 建序**：Jacamar Wood → Far West（R192 队列剩 2），R196 建毕队列罄 → R197 须再 SCN28 discover。
4. **Far West 混指剔除纪律**：建页仅取 MI Lincoln Island 林区指（33 distinctPN），剔 generic American West 21 hits。
5. **HK-addpage-prose-gate-bypass**：本轮首版 3 段超 400，awk 预检拦截修正；续常规 awk 段长复检。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=130→131（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：17 place 页 quality=none（R193 EVV5 登记），full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：Medicine Bow/Reptile Point/Grant Lake/Prospect Plateau DEFER、Salt Lake(=great-salt-lake)/
    Serpentine(=serpentine-peninsula) DUPLICATE；既有 Cape Mandible/Indian Peninsula/Balearic Isles DEFER，
    Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen 等 DUPLICATE 照旧。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
