---
round: 186
date: 2026-07-17
type_round: 157
phase: "2.1"
current_type: place
gene: NEW1
pages: [stapi]
result: success
---

# GROW 2.1-B · R186 · NEW1 · place — 建 Stapi（JCE Snæfell 脚下村，净 solid 9；R181 队列末项，耗尽）

## 执行摘要

Phase 2.1-B place 广度扩张第 157 轮（type_round 157）。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10、since_discover=4<10、queue(place)=2>0、stub%=0 → §3(7)）。
取 R181 discover 批次**末项** **Stapi**（JCE×10）。文件系统查重 stapi/-village/stapar 皆 NEW。

**Stapi（JCE 单源，净 solid 9 超门）**：Snæfell 半岛南麓、火山脚下的冰岛村落，下降入 Snæfell 火山口前的最后集结地。
sentence_index 命中 10 distinct PN，取 9 solid：
- **JCE-011-011**：Hans 受雇引路至 Snæfell 半岛南岸、火山脚下之 Stapi 村。
- **JCE-014-002**：约三十座熔岩石屋组成，居火山南麓。
- **JCE-013-035**：步行约四小时，马自停于 Stapi 神父宅门前。
- **JCE-011-014**：Hans 雇约不止于抵 Stapi，续役全程科研。
- **JCE-014-017**：抵 Stapi 次日即备启程。
- **JCE-014-045**：Hans 发令，众离村。
- **JCE-014-005**：叙事者于 Stapi 见海岸奇景之全美。
- **JCE-015-004**：越 Stapi 峡湾玄武岩壁，过古植被泥炭沼。
- **JCE-016-030**：遣散之冰岛人下 Snæfell 外坡返 Stapi。

place 计数 389→390，registry total 1457→1458，unknown 恒 0。
add_page 首建一段超 400（In the Narrative 438），写入前 awk 预检拦下，edit 两次修剪至 ≤400（最长 387），无残页。
pn_validator strict 建后即通过；build_registry 仅余既有 Robur alias 告警（PARK）。real_or_fictional=real、region=Snæfell Peninsula, Iceland。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=4<10；queue=2（discover 冷却末程）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=2<10 名义达 discover 条件，但为 R181 补种残项、冷却中，续 NEW1 消耗末项（承 R183–R185 判据）。
> **本轮建毕 R181 队列罄（5 项：Irtish✔/Tsalal✘DUP/Tristan✔/Bennet✔/Long's Peak✔/Stapi✔ — 计 5 buildable，Tsalal 除）。下轮 R187 必触 SCN28 discover 补种。**

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| stapi | MV5dPi | Journey to the Center of the Earth | real | Snæfell Peninsula, Iceland | 9 | Snæfell 脚下熔岩村；神父宅；下降前集结；峡湾玄武岩壁 |

- **stapi**：9 distinct solid PN（JCE 单源）；无 alias。链 journey-to-the-center-of-the-earth。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：stapi 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：add_page 首建一段 438，写入前 awk 预检 → edit 修至最长 387。✔
- **G3 ≥5 distinct PN**：9 solid（JCE 单源，超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1458 place 390 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 后缀变体（stapi/stapi-village/stapar）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R187 起始计数）

| 字段 | R186 起始 | R187 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 186 | 187 |
| type_round | 157 | 158 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 122 | 123 |
| last_updated_round | 186 | 187 |

## 遗留问题

1. **place 页数 390**：本轮 +1（Stapi）。registry 全库 1458，unknown 0。
2. **下轮 R187 = SCN28 discover（队列耗尽）**：R181 补种 5 项已建齐，queue(place)=0（本轮消费末项）→ §3(4) SCN28-zombie 亦触，§3(3) 亦触。
   须表层 toponym 复扫补种（AM/JCE/FEM/OC 剩余未采 + 其他作品长尾），入队时**查 slug + 后缀变体**（-island/-islet/-river/-city，承 Tsalal 教训）。目标净新 ≥3 buildable。
3. **discover 查重纪律**：入队即查 slug + 变体，避免 Tsalal 式漏检拖到 NEW1 建前。
4. **HK-addpage-prose-gate-bypass**：本轮 add_page 首建一段超 400，靠写入前 awk 预检 + edit 修剪，未污染库；add_page 散文门缺陷续 PARK。
5. **主矿脉盘点**：R181 批次 AM（Tristan/Bennet）/FEM（Long's Peak）/JCE（Stapi）已建齐。未宣布饱和——R187 discover 须先穷扫剩余 toponym 再评估。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=122→123（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
