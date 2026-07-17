---
round: 183
date: 2026-07-17
type_round: 154
phase: "2.1"
current_type: place
gene: NEW1
pages: [tristan-da-cunha]
result: success
---

# GROW 2.1-B · R183 · NEW1 · place — Tsalal 撞 DUPLICATE（既有 tsalal-island）；改建 Tristan d'Acunha（AM+SC 南大西洋火山岛，净 solid 10）

## 执行摘要

Phase 2.1-B place 广度扩张第 154 轮（type_round 154）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10、since_discover=1<10、queue(place)=5>0、stub%=0 → §3(7)）。
R181 discover 补种 5 项，本轮取首项 Tsalal——**撞 DUPLICATE**，同轮改建 **Tristan d'Acunha**。

**Tsalal DUPLICATE（R181 discover 查重疏漏，本轮建前拦截）**：
- Tsalal（AM×90，R181 标最强）→ 文件系统查重 `tsalal new` 但 **`tsalal-island EXISTS`**。
  读 frontmatter 确认既有 `tsalal-island`（Tsalal Island，An Antarctic Mystery，fictional，Pym 叙事南极岛）即同一岛。**DUPLICATE**，未建。
- **根因**：R181 discover 仅查裸 slug `tsalal`，未查 `-island` 后缀变体（承 R180 教训「查拼写/后缀变体」，discover 环节仍漏）。
  **纠正**：discover 入队时即须查 slug + 常见后缀（-island/-islet/-river/-city）变体，不留到 NEW1 建前才发现。本轮已即时拦截，无残页。

**改建 Tristan d'Acunha（AM 主 + SC 双源，净 solid 10 远超门）**：文件系统查重 tristan-da-cunha/-dacunha/-d-acunha 皆 NEW。
南大西洋孤火山岛，Halbrane 南下入南极冰前最后有人居停靠地。10 distinct solid（多于门 5）：
- **AM-007-005**：位处规则西南风带之南。
- **AM-007-001**：Halbrane 抵此「非洲海之大锅炉」，进港补水。
- **AM-003-069**：Halbrane 直航 Tristan，Len Guy 探 Jane 幸存者消息。
- **AM-008-001**：Jeorling 见 Glass（自封 Governor-General，忆 11 年前 Jane 停靠）。
- **AM-001-039**：早前拟至此卸锡铜货。
- **AM-007-014**：无一港口。
- **AM-008-003**：火山高 8000 尺；Elephant Bay/Hardy Rock/West Point/Cotton Bay/Daly's Promontory。
- **SC-028-023**：坐标 37°8'S / 10°44'W。
- **SC-028-026**：首邑为湾心小村，急流灌之。
- **AM-004-073**：Jeorling 曾拟于此别 Halbrane。

place 计数 386→387，registry total 1454→1455，unknown 恒 0。
add_page 首建两段超 400（In the Narrative 413 / Geography 405，HK-addpage-prose-gate-bypass 再现——add_page 未拦），
即以 edit_page.py 修剪至 ≤400（最长 397）。pn_validator strict 修后通过；build_registry 仅余既有 Robur alias 告警（PARK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10、queue=5（<10?）| 否* |
| 4 | SCN28-zombie（queue(place)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *§3(3)：queue_size=5<10 名义达 discover 触发条件，但 R181 刚 discover（since_discover=1），队列为新鲜补种，
> 且 R181 已重置 since_discover=0 → 本轮 since_discover=1。此处按「discover 冷却」——刚补种不应立即再 discover，
> 走 NEW1 消耗新候选（承 R150→R151 先例：discover 次轮即转 NEW1 建 Nantucket）。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| tristan-da-cunha | 7WNjzk | An Antarctic Mystery | real | South Atlantic Ocean | 10 | 南大西洋孤火山岛；Halbrane 补水停靠；Governor Glass；SC 坐标/首邑村 |
| ~~tsalal~~ | — | — | — | — | — | **DUPLICATE**：既有 tsalal-island（AM，Pym 叙事南极岛）|

- **tristan-da-cunha**：10 distinct solid PN（AM 主 8 + SC 2 双源）；label 'Tristan d''Acunha'（Verne 拼写，YAML 单引双撇），alias [Tristan da Cunha]。链 an-antarctic-mystery。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：tristan 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：add_page 首建 413/405 超限 → edit_page 修剪至最长 397。✔（HK-addpage-prose-gate-bypass 再现，已 edit_page 修复）
- **G3 ≥5 distinct PN**：10 solid（AM 8 + SC 2，远超门）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 修，quality 自动回填 featured，未用 Write/Edit。Tsalal DUPLICATE 建前文件系统拦截，无残页。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；label/description 单引号（LAW §8）。✔
- **registry 一致**：total 1455 place 387 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 后缀变体（Tsalal→tsalal-island 拦截）+ registry alias。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R184 起始计数）

| 字段 | R183 起始 | R184 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 183 | 184 |
| type_round | 154 | 155 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 119 | 120 |
| last_updated_round | 183 | 184 |

## 遗留问题

1. **place 页数 387**：本轮 +1（Tristan d'Acunha）。registry 全库 1455，unknown 0。Tsalal DUPLICATE 未增页（建前拦截）。
2. **下轮 R184 = NEW1**：since_evv5=1<10、since_discover=2<10、queue=4>0 → §3(7) NEW1。
   建 R181 批次剩项 **Bennet Islet**（AM×13，以 Jane 船东合伙人命名之岛，赴 Tsalal 途中），建前文件系统查重（bennet-islet/bennet-island）+ 抽样 ≥5 solid。
3. **R184+ 建序（R181 批剩 4，Tsalal 已除）**：Bennet Islet → Long's Peak → Stapi。（3 项后队列罄，须再 SCN28 discover。）
4. **discover 查重纪律升级（本轮教训）**：SCN28 入队时须查 slug **+ 后缀变体**（-island/-islet/-river/-city），
   避免 R181 Tsalal（=tsalal-island）式漏检拖到 NEW1 建前。已在 R181 marker 后补记。
5. **HK-addpage-prose-gate-bypass 再现**：Tristan add_page 首建两段 413/405 未被 add_page 拦，靠人工 awk 复检 + edit_page 修至 ≤400。
   add_page 散文门缺陷续 PARK（RFC 全线 PARK）；建页后须常规 awk 段长复检。
6. **主矿脉盘点（承 R182）**：AM 未采层续掘（Tristan✔，剩 Bennet Islet）；JCE（Stapi 待）/FEM（Long's Peak 待）。未宣布饱和。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页修后 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=119→120（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
