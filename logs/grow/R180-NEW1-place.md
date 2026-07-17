---
round: 180
date: 2026-07-17
type_round: 151
phase: "2.1"
current_type: place
gene: NEW1
pages: [irtish]
result: success
---

# GROW 2.1-B · R180 · NEW1 · place — Sneffels 撞 DUPLICATE（既有 snaefellsjokull alias Sneffels）；改建 Irtish（MS 西伯利亚河，净 solid 5）

## 执行摘要

Phase 2.1-B place 广度扩张第 151 轮（type_round 151）。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10、since_discover=9<10、queue(place) nominal>0、stub%=0 → §3(7)）。

**承 R179 查重纪律，建前一律文件系统预检**（feedback_grow_dupcheck_filesystem）：
1. **Sneffels**（R179 预定优先，JCE 火山口）→ 文件系统查重命中 `snaefellsjokull EXISTS`。
   读 frontmatter 确认 `snaefellsjokull` **aliases: [Sneffels, Snæfell]**，正是同一冰川火山，
   且已用同一 PN JCE-005-050。**DUPLICATE**，未建。R179 遗留把 Sneffels 标 genuinely-NEW 系误判——
   当时只查了 sneffels/snaefell 变体，漏了真实地名拼写 snaefellsjokull（HK-discover-existing-type-blindspot 再现，
   但本轮查重纪律即时拦截，未走到 add_page）。
2. **Ishim**（MS×9，最强候选）→ 文件系统 `ichim EXISTS`；读页确认既有 `ichim`（Ichim，西伯利亚驿路 post-town）
   即 Ishim 同名异拼（MS 译名 Ichim/Ishim 互通）。Ishim 语料主指**驿路市镇**（MS-009-014/016/012-071~073 皆城镇），
   与 ichim 页重合。**DUPLICATE**，未建。
3. **Obi / Yenisei**（河）→ 文件系统 `obi EXISTS`、`yenisei EXISTS`，均已建。跳过。

**改建 Irtish（MS 单源，净 solid 5 达门）**：Irtish 为西伯利亚大河，语料稳定指向**河流**本体
（Omsk 立于其岸、鞑靼推进界线、入侵下行通道）。文件系统查重 irtish/irtysh 皆 NEW。5 distinct solid：
- **MS-004-038**：Omsk 立于 Irtish 岸；Michael 之母 Marfa 居此不肯离。
- **MS-002-022**：开战之初密报保证鞑靼尚未越过 Irtish 与 Obi（河作前线界）。
- **MS-005-040**：Caucasus 汽船上旅人虑「Kirghiz 若下 Irtish，则赴 Irkutsk 之路不安」。
- **MS-009-030**：Feofar-Khan 鞑靼过 Semipolatinsk，正下 Irtish（入侵通道）。
- **MS-012-075**：鞑靼连日强行军下 Irtish，席卷 Semipolatinsk 全省。
- 支撑 **MS-003-058**（中 Kirghiz 部落营地介于 Sara Sou / Irtish / Upper Ishim 诸河之间，河界泛指）。

place 计数 385→386，registry total 1453→1454，unknown 恒 0。
首版全段 ≤400（Overview 首版 414 超限 → 删「in the house of the Strogoffs,」降至 384；最长段 387）。
add_page 一次成型，pn_validator strict 建后即通过；build_registry 仅余既有 Robur alias 告警（PARK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=9<10、queue nominal≥10 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| nominal>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| irtish | YmUKOg | Michael Strogoff | real | Western Siberia | 5 | 西伯利亚河；Omsk 立岸；鞑靼下行入侵通道/前线界 |
| ~~sneffels~~ | — | — | — | — | — | **DUPLICATE**：既有 snaefellsjokull（alias Sneffels/Snæfell，同火山）|
| ~~ishim~~ | — | — | — | — | — | **DUPLICATE**：既有 ichim（同名异拼，驿路市镇）|
| ~~obi~~ | — | — | — | — | — | **既有**：obi 已建 |

- **irtish**：5 distinct solid PN（MS 单源）— 004-038（Omsk 岸/Marfa）/002-022（前线界 not beyond Irtish&Obi）/
  005-040（Kirghiz 下 Irtish 危 Irkutsk 路）/009-030（鞑靼过 Semipolatinsk 下 Irtish）/012-075（强行军下 Irtish 席卷）。
  003-058（Kirghiz 营地河界泛指）支撑。链 michael-strogoff。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：irtish 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：Overview 首版 414 → 删冗降至 384；最终最长 387。✔
- **G3 ≥5 distinct PN**：5 solid（MS 单源，达门）+ 1 支撑。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。DUPLICATE 3 例全在建前文件系统预检拦截，未产残页。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；book 无冒号免引号。✔
- **registry 一致**：total 1454 place 386 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 拼写变体 + registry alias + frontmatter alias 核对；Sneffels/Ishim/Obi 三例建前拦截。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → 见提交前核验。✔

## 六步状态机（NEW1，grow_state 存 R181 起始计数）

| 字段 | R180 起始 | R181 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 180 | 181 |
| type_round | 151 | 152 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 9 | 10 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 116 | 117 |
| last_updated_round | 180 | 181 |

## 遗留问题

1. **place 页数 386**：本轮 +1（Irtish）。registry 全库 1454，unknown 0。3 DUPLICATE 未增页（全建前拦截，无回滚）。
2. **下轮 R181 = SCN28 DISCOVER**：R181 起始 since_discover=10≥10 → §3(3) 触发 discover 勘探轮（非建页）。
   R179 遗留曾误记「R181 EVV5」——实为 since_evv5 R181=9<10，EVV5 顺延至 **R182**（since_evv5=10）。
   discover 优先于 EVV5，故 R181 走 discover：宽扫 place 未采 toponym（AM/JCE/FEM/OC 及 MS 剩余河/站），补 queue。
3. **查重纪律见效（本轮正例）**：R179 新立「文件系统预检」纪律本轮即拦下 3 DUPLICATE（Sneffels/Ishim/Obi），
   全部在 add_page 之前，无残页无回滚——对比 R179 Timbuktu 建后才由 alias 冲突暴露。纪律有效，续用。
   **补强**：查真实地名/原文拼写变体（Sneffels→snaefellsjokull、Ishim→ichim），不止英化 slug。
4. **未采待 R181+ probe**：Tobol（MS×1，净<5 DEFER）；AM/JCE/FEM/OC 未采 toponym；MS 剩余小站。
   discover 轮统一补录。
5. **stale-queue 清理债（承 R179 PARK）**：queue P3 发现块仍含已建/DUPLICATE 裸行；批量核销留 Phase 收尾。
6. **主矿脉建齐盘点（承 R179）**：DSCF 安哥拉、ASC 中亚、MS 西伯利亚主站均建齐；MS 河系补 Irtish（Obi/Yenisei 已在）。
   新矿续向 AM（Kerguelen✔）/JCE/FEM/OC 未采层。HK-premature-saturation-claim：未宣布饱和，续 exhaustive re-scan。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
9. **corpus-discover 顺延**：since_corpus=116→117（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana 净4、Missouri（passing）、Abyssinia 净3、
    Tioumen 净3、Carmen 净3、Mozambique 净0、Yeniseisk 净1、Kazan(2)、Tobol 净1、Baikal/Timbuktu/Tampa/Sneffels/Ishim DUPLICATE。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
