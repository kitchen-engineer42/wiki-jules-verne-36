---
round: 198
date: 2026-07-17
type_round: 169
phase: "2.1"
current_type: place
gene: NEW1
pages: [corral]
result: success
---

# GROW 2.1-B · R198 · NEW1 · place — 建 The Corral（MI Lincoln Island Red Creek 畜栏/Ayrton 居所，净 solid 16 MI-referent；chimneys 判 DUPLICATE 剔除）

## 执行摘要

Phase 2.1-B place 广度扩张第 169 轮（type_round 169）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、since_discover=0<10、queue(place)=4>0、stub%=0 → §3(7)）。

**队首 chimneys 判 DUPLICATE 剔除**：R197 discover 入队 chimneys，本轮建页时 build_registry 报
`alias conflict: 'The Chimneys' → chimneys vs the-chimneys`——查 pages.json 得**既有页 the-chimneys**
（label "The Chimneys"，place，MI Lincoln Island，2026-07-15 建，旧 schema 含 H1 + bullet Connections）。
同指 Lincoln Island 河口花岗岩堆叠首居所，**确认完全重复**。即刻回滚：rm chimneys.md + chimneys.jsonl，
`git checkout` 还原 add_page 触改的 pages.json/pages.lite.json/recent.*/line_index（14 shard），registry 复归 1465。
**教训**：R197 discover 的文件系统查重漏测 `the-` 前缀变体（仅查 chimneys/后缀变体），承 memory
"GROW dup-check via filesystem"——须扩查 `the-<slug>`/`<slug>` 双向。记 housekeeping HK-dupcheck-the-prefix-blindspot，不另起 RFC。

**转建队列次项 The Corral（MI 单源密指，净 solid 16 MI-referent 远超门）**：Lincoln Island Red Creek 谷源、
Mount Franklin 麓之畜栏，圈 musmon/山羊，后建木屋为 Ayrton 隐居所、电报枢纽、叙事中枢。建前文件系统 + pages.json
双查（corral/the-corral/georgia/coppermine 皆 NEW），16 distinct solid MI PN：
- **MI-030-026**：Red Creek 源 / Mount Franklin 麓设栏，容 ruminants 免扰 Granite House。
- **MI-030-029**：engineer 划界，伐木立 palisade。
- **MI-030-030**：建期三周，palisade 外加 sheds 蔽兽。
- **MI-030-031**：栏成，raid 牧场逐 ruminants。
- **MI-030-034**：百 musmon 围，三十兽 + 十野羊经开门驱入。
- **MI-031-011**：栏内 musmon 增，lambs 卧 sheds。
- **MI-033-024**：储备充足，非日访，然每周须至。
- **MI-039-018**：距 Granite House 四五英里，圈驯养兽。
- **MI-040-036**：拉线量得五英里隔栏与 Granite House。
- **MI-042-076**：较 plateau 少露，Mount Franklin 半蔽，仅受飓风余威。
- **MI-038-077**：Harding 拟于此建 farm。
- **MI-039-026**：议为 Ayrton 于栏建木屋，尽舒适。
- **MI-040-025**：Ayrton 入所受居。
- **MI-040-028**：Harding 决使栏与 Granite House 即时通讯。
- **MI-040-045**：电报通，Harding 送电流询栏况，得 Ayrton 复。
- **MI-040-052**：栏路循 Mercy 左岸至 Falls River 口。

place 计数 397→398，registry total 1465→1466，unknown 恒 0。
add_page 一次成型，全段预检 ≤399（awk 打印所有 >399 段，本版 0 超段）。pn_validator strict 建后即通过；
build_registry 仅 Robur PARK 告警。real_or_fictional=fictional、region=Lincoln Island、aliases=[Corral]、label "The Corral"（避与 the-chimneys 式 `the-` slug 混淆，用大写 label + 唯一性）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10；queue=4（消费中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=4<10 名义达条件，但 discover=0 未逾期、队列消费中，续 NEW1。
> **队首 chimneys 剔为 DUPLICATE，实建次项 corral。剩余队列：New Georgia / Coppermine River（2 项）。**

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| corral | RHHSde | The Mysterious Island | fictional | Lincoln Island | 16 | Red Creek 谷畜栏；Ayrton 居所 + 电报枢纽；MI 单源密指 |
| ~~chimneys~~ | — | — | — | — | — | **DUPLICATE**（既有 the-chimneys），回滚未建 |

- **corral**：16 distinct solid MI PN（远超门）；alias [Corral]，label "The Corral"。链 the-mysterious-island。pn_validator --mode strict ✓ 全通过。
- **chimneys**：判重回滚，registry 复归 1465→再建 corral 至 1466。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：corral 全句源自 sentence_index 且 VVV=MI Lincoln Island referent；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，本版 0 超段。✔
- **G3 ≥5 distinct PN**：16 solid（MI referent，远超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号 + Ayrton''s 双撇（LAW §8）。✔
- **registry 一致**：total 1466 place 398 unknown 0；本轮无新 alias 告警（仅 Robur PARK）。✔
- **查重充分**：chimneys 判 DUPLICATE 回滚；corral 文件系统 + pages.json 双查（corral/the-corral/georgia/coppermine 皆 NEW）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R199 起始计数）

| 字段 | R198 起始 | R199 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 198 | 199 |
| type_round | 169 | 170 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 134 | 135 |
| last_updated_round | 198 | 199 |

## 遗留问题

1. **place 页数 398**：本轮 +1（The Corral）。chimneys 判 DUPLICATE 未建。registry 全库 1466，unknown 0。
2. **下轮 R199 = NEW1**：since_evv5=5<10、since_discover=1<10、queue(place)=2>0 → §3(7) NEW1。
   建 **New Georgia**（new-georgia，AM×11，亚南极岛，real，South Atlantic Ocean）。建前文件系统 + pages.json 双查 + `the-` 变体。
3. **R199+ 建序**：New Georgia → Coppermine River（2 项），R200 建毕队列罄 → R201 SCN28 discover。
4. **新增 housekeeping HK-dupcheck-the-prefix-blindspot**：discover/build 查重须双向覆盖 `the-<slug>` 与 `<slug>`；
   R197 chimneys 漏测 the-chimneys 致本轮回滚。PARK 记录，不另起 RFC（承 memory 停车规则）。
5. **MI 自然地理近饱和信号**：承 R197，MI 岬/湾/沼/河/林/湖主干已建齐，人居设施 chimneys 竟已存（the-chimneys）、
   corral 本轮建。后续 discover 宜向 FC/AM/AWED/ACH 极地-铁路长尾扩散。**未宣布饱和**。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页，含 the-chimneys），DEFER。
8. **corpus-discover 顺延**：since_corpus=134→135（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **featured re-grade DEFERRED**：17+ place 页 quality=none（R193 EVV5 登记），full-library re-grade 顺延至 RFC 批审。
11. **DEFER/DUPLICATE 累积**：本轮 +chimneys（DUPLICATE，既有 the-chimneys）；既有 Fort Enterprise（FC×4 DEFER）/
    North·South Mandible/Reptile Point DEFER，Medicine Bow/Grant Lake/Prospect Plateau DEFER，Salt Lake/Serpentine/Omaha/Cape Bathurst 等 DUPLICATE 照旧。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot（新）、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
