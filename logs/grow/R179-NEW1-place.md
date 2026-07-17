---
round: 179
date: 2026-07-17
type_round: 150
phase: "2.1"
current_type: place
gene: NEW1
pages: [kerguelen]
result: success
---

# GROW 2.1-B · R179 · NEW1 · place — stale-queue 连撞 3 DUPLICATE（Samarkand/Timbuktu/Tampa 皆既有）；同轮 probe 改建 Kerguelen（AM 荒岛群，净 solid 5）

## 执行摘要

Phase 2.1-B place 广度扩张第 150 轮（type_round 150）。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10、streak=0<3、since_discover=8<10、queue(place) nominal>0、stub%=0 → §3(7)）。
DSCF 安哥拉队列 R178 建齐收官后，本轮取 queue 最强候选 Samarkand——**连撞 3 DUPLICATE**，
同轮 probe 改建 **Kerguelen**（AM 单源，净 solid 5，避免空轮，参 Baikal→Tai-Youan / Mozambique→Loanda 同轮改建先例）。

**stale-queue 3 连撞 DUPLICATE（关键教训，HK-discover-existing-type-blindspot 再现）**：
1. **Samarkand**（queue line 74，31 distinctPN）→ 既有 `samarkand`（R158 建，rev L7zz7h）。queue 行后有 `<!-- ✔ R158 建 -->` 注但裸列表行未删除线，误读为未消费。
2. **Timbuktu**（queue line 150，RC×7）→ 既有 `timbuctoo`（R121 建，alias [Timbuktu]，FWB 主源）；**R154 已标 DUPLICATE**（line 151）。add_page 未拦（slug 不同），build_registry alias 冲突告警 'Timbuktu'→timbuctoo vs timbuktu 才暴露；已 rm 回滚（pages 1453→1452）。
3. **Tampa**（probe，FEM×34）→ 既有 `tampa-town`（Tampa Town，Columbiad 发射地）。文件系统查重即拦。

**根因**：queue 消费标记为「行后 `<!-- ✔ 建 -->` 注」而非统一删除线，裸 `- [place] X` 行易误判未消费；
且 discover 批次曾漏检既有页（HK-discover-existing-type-blindspot）。**纠正纪律：查重信号一律以文件系统
（`test -f docs/wiki/pages/<xx>/<slug>.md` + 拼写变体 + label/alias registry）为准，不信 queue 裸行**。本轮后续全改文件系统预检。

**同轮 probe 改建 Kerguelen（AM 单源，净 solid 5 达门）**：宽扫 AM/JCE/FEM 未采 toponym（MS 西伯利亚主站
omsk/tomsk/krasnoiarsk 等、ASC 中亚站、DSCF 安哥拉、FWB 非洲主 toponym 均已建齐）。命中 **Kerguelen**（AM×10+TT×2）：
001-003（49°45'S/69°6'E 坐标·命名）、001-004（有居民/欧美人口 nucleus/1839-08-02）、001-027（捕鲸船 put in/Green Cormorant）、
004-049（Pym 叙事 sealed letter 置于 Kerguelen 峰麓）、020-055（Halbrane 自 Kerguelen 起航 6.5 月后困冰山）= 5 solid，
+ 003-026/020-080/019-122 支撑。slug kerguelen，region Southern Indian Ocean。文件系统查重 kerguelen/-island/-islands/-s 皆 NEW。

place 计数 384→385，registry total 1452→1453，unknown 恒 0。
首版全段 ≤400（362/378/320/300）。add_page 一次成型，pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=7<10、queue nominal>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| nominal>0（但净 buildable 实低，stale 污染）| 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> 注：§3(4) 名义 queue>0 故不触 zombie，但本轮暴露 nominal queue 严重 stale（多为已建/DUPLICATE）——
> genuinely-buildable≈污染后极低（HK-queue-size-scope 加剧）。R180 起 NEW1 primary 须先文件系统预检整批 queue。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| kerguelen | 5PAktF | An Antarctic Mystery | real | Southern Indian Ocean | 5 | Halbrane 起航荒岛群；捕鲸港/Green Cormorant；Pym 峰麓 sealed letter |
| ~~samarkand~~ | — | — | — | — | — | **DUPLICATE**：既有 samarkand（R158）|
| ~~timbuktu~~ | — | — | — | — | — | **DUPLICATE**：既有 timbuctoo（R121，alias Timbuktu，R154 已标）；已 rm 回滚 |
| ~~tampa~~ | — | — | — | — | — | **DUPLICATE**：既有 tampa-town（Columbiad 发射地）|

- **kerguelen**：5 distinct solid PN（AM 单源）— 001-003（坐标/命名）/001-004（人口 nucleus）/001-027（捕鲸港 Green Cormorant）/004-049（Pym sealed letter 峰麓）/020-055（Halbrane 起航困冰山）。003-026/020-080/019-122 支撑。链 an-antarctic-mystery。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：kerguelen 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（362/378/320/300）。✔
- **G3 ≥5 distinct PN**：5 solid（AM 单源，达门）+ 3 支撑。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit；DUPLICATE 页 rm 回滚 + git checkout 生成物 + rebuild registry，未留残页。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；book 单引号（LAW §8）。✔
- **registry 一致**：total 1453 place 385 unknown 0（Timbuktu 回滚后 build_registry 无 timbuktu 冲突告警）。✔
- **查重充分**：文件系统 + 拼写变体 + registry alias 三重；DUPLICATE 3 例均在建前/建时拦截并处置。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R180 起始计数）

| 字段 | R179 起始 | R180 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 179 | 180 |
| type_round | 150 | 151 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 8 | 9 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 115 | 116 |
| last_updated_round | 179 | 180 |

## 遗留问题

1. **place 页数 385**：本轮 +1（Kerguelen）。registry 全库 1453，unknown 0。3 DUPLICATE 未增页（1 已 rm 回滚）。
2. **下轮 R180 = NEW1**：since_evv5=8<10、since_discover=9<10 → §3(7) NEW1。**建前须文件系统预检**：
   优先 **Sneffels**（JCE×7 净≥5：Saknussemm 密文火山口/Scartaris 影/several craters，genuinely-NEW，已文件系统确认 NEW）。
   备选 AM/JCE/FEM 未采 toponym。**R181 到期 EVV5**（since_evv5=8→R180 后=9→R181=10 触发）。
3. **查重纪律升级（本轮核心教训）**：queue 裸列表行不可信为「未消费」——消费标记散见行后 `<!-- ✔ 建 -->` 注。
   **NEW1 建前一律 `test -f` 文件系统预检（含拼写变体）+ registry alias 检查**，勿凭 queue nominal 判可建。
4. **stale-queue 清理债（新增记录，PARK）**：HK-discover-existing-type-blindspot 加剧——queue P3 发现块含大量已建/
   DUPLICATE 裸行（Samarkand/Timbuktu/多 ASC 中亚站/多 MS 西伯利亚站 等）。批量核销/加删除线宜留 Phase 收尾清理，本轮仅记录。
5. **主矿脉建齐盘点**：DSCF 安哥拉（Loanda/Cassange/Bihe/Coanza+Kazounde）、ASC 中亚（Samarkand/Kachgar/Tachkend/Douchak/
   Sou-Tcheou/Lan-Tcheou/Tai-Youan…）、MS 西伯利亚主站（Omsk/Tomsk/Krasnoiarsk/Tobolsk/Irkutsk/Nijni-Novgorod…）、
   FWB 非洲（Kazeh/Gondokoro/Timbuctoo）均已建齐。**新矿转向 AM（Kerguelen✔）/JCE（Sneffels 待）/FEM/OC 未采层**。
   HK-premature-saturation-claim：主脉近饱但仍有 AM/JCE/FEM/OC 支脉——**未宣布饱和，续 exhaustive re-scan**。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=115→116（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana 净4、Missouri（河 passing-mention）、
    Abyssinia 净3、Tioumen 净3、Carmen 净3、Mozambique 净0、Yeniseisk 净1、Kazan(2)、Baikal/Timbuktu/Tampa DUPLICATE。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot（本轮加剧）、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **富化机会（承 R154 记录）**：RC×7 Albatross 掠 Timbuktu 段可 Phase 3 RCH2 注入既有 timbuctoo；本轮 breadth 不做。
13. **洲级 America/Europe/Asia 续 HOLD**。
