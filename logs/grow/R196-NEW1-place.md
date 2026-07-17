---
round: 196
date: 2026-07-17
type_round: 167
phase: "2.1"
current_type: place
gene: NEW1
pages: [far-west]
result: success
---

# GROW 2.1-B · R196 · NEW1 · place — 建 Far West（MI Lincoln Island 西部密林区，净 solid 14 MI-referent；R192 队列末项，建罄）

## 执行摘要

Phase 2.1-B place 广度扩张第 167 轮（type_round 167）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、since_discover=3<10、queue(place)=1>0、stub%=0 → §3(7)）。
取 R192 discover 批次**末项** **Far West**（MI-referent×33 distinctPN）。文件系统查重 far-west/far-west-forests/forests-of-the-far-west 皆 NEW，alias_index 无占用。

**Far West（MI 单源，净 solid 14 MI-referent 远超门）**：Lincoln Island 西部覆 Serpentine Peninsula 之大密林，
殖民地最后勘探之域。**混指剔除纪律**：全库 Far West 54 distinctPN 中 21 为 generic American West
（AM/ASC/AWED/EHLA），本页逐句核 VVV=MI 且指 Lincoln Island 林区，仅采 33 MI-referent 中 14 solid：
- **MI-011-075**：命名——覆 Serpentine Peninsula 之密林名 forests of the Far West。
- **MI-019-024**：immense woods 久未探。
- **MI-023-055**：初探一无所见。
- **MI-025-023**：首枪惊林中回声（kingfisher 状鸟）。
- **MI-031-028**：Harding/Herbert 入林，Mercy 左岸。
- **MI-031-038**：勘 cycas 生长处，返 Granite House 报。
- **MI-029-055**：辟直道穿 Far West 林。
- **MI-021-017**：西距四英里首树起。
- **MI-025-028**：含 Jacamar Wood 延展至目不能及。
- **MI-026-043**：末树间见 bamboo 丛。
- **MI-026-028**：河转恐复入 Far West，engineer 频察罗盘。
- **MI-012-013**：循 Mercy 穿 Far West 达 Prospect Heights 与 Union Bay。
- **MI-022-035**：兽多栖此，饥则逼近 Prospect Heights。
- **MI-027-022**：Spilett 议造桥便入 Far West。

place 计数 396→397，registry total 1464→1465，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版 Connections 段 476，awk **全 >399 段**预检拦截——承 R195 教训，本轮打印所有超段，拆段后最长 363，未触 HK-addpage-prose-gate-bypass）。
pn_validator strict 建后即通过；build_registry 仅 Robur PARK 告警。real_or_fictional=fictional、region=Lincoln Island、aliases=[Forests of the Far West]。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=3<10；queue=1（末项冷却）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=1<10 名义达条件，但为 R192 补种末项、冷却中，续 NEW1 消费。
> **本轮建毕 R192 队列罄（3 项 The Mercy/Jacamar Wood/Far West 全建）。下轮 R197 queue=0 → §3(3)&§3(4) 触 SCN28 discover。**

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| far-west | hD9Kfg | The Mysterious Island | fictional | Lincoln Island | 14 | 覆 Serpentine Peninsula 西部大密林；末勘探域；混指剔 generic American West |

- **far-west**：14 distinct solid PN（MI 单源 referent，剔 21 generic American West）；alias [Forests of the Far West]。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：far-west 全句源自 sentence_index 且 VVV=MI Lincoln Island referent；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检拦截首版 476 段，拆段后最长 363。✔
- **G3 ≥5 distinct PN**：14 solid（MI referent，远超门；已剔 21 generic American West wrong-referent）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1465 place 397 unknown 0；本轮无新 alias 告警（仅 Robur PARK）。✔
- **查重充分**：文件系统 + 后缀变体（far-west/far-west-forests/forests-of-the-far-west）+ alias_index。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R197 起始计数）

| 字段 | R196 起始 | R197 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 196 | 197 |
| type_round | 167 | 168 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 132 | 133 |
| last_updated_round | 196 | 197 |

## 遗留问题

1. **place 页数 397**：本轮 +1（Far West）。registry 全库 1465，unknown 0。
2. **下轮 R197 = SCN28 discover（队列耗尽）**：R192 补种 3 项（The Mercy/Jacamar Wood/Far West）本轮建齐，
   queue(place)=0 → §3(3)（queue<10）&§3(4)（zombie）触发。须表层 toponym 复扫补种，目标净新 ≥3。
3. **R197 discover 预备——MI 内陆网未采盘点**：Lake Grant（MI 密，湖本体待查 distinctPN 与 grant-lake dup）、
   Red Creek（MI，Mercy 支流/泉源）、Falls River（MI，Mercy 支流）、Creek Glycerine、Grand View、Mount Bell 待复扫
   distinctPN 与 dup；MI 外围如 20KL/ACH/AWED 剩余 toponym 长尾亦可掘。
4. **HK-addpage-prose-gate-bypass**：本轮 awk 预检改打印**所有** >399 段（承 R195 教训），首版 476 段一次拦截，未复现漏判。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
7. **corpus-discover 顺延**：since_corpus=132→133（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
9. **featured re-grade DEFERRED**：17 place 页 quality=none（R193 EVV5 登记），full-library re-grade 顺延至 RFC 批审。
10. **DEFER/DUPLICATE 累积**：Medicine Bow/Reptile Point/Grant Lake/Prospect Plateau DEFER、Salt Lake/Serpentine DUPLICATE；
    既有 Cape Mandible/Indian Peninsula/Balearic Isles DEFER，Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen 等 DUPLICATE 照旧。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
