---
round: 208
date: 2026-07-17
type_round: 179
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 4
---

# GROW 2.1-B · R208 · SCN28 · place — 全库重扫补种（净新 4 buildable：Healthful House / Arctic Ocean / Upper Amazon / Celestial Empire）

## 执行摘要

Phase 2.1-B place 第 179 轮（type_round 179）。决策机 §3 首匹配 **SCN28-zombie**
（R201 队列 R207 建罄，queue(place)==0 → §3(4)）。**非建页轮**：全库 sentence_index
重扫补种。

**承 premature-saturation 纪律（memory rule）**：不凭 queue 空断言 place 饱和，
执行全库多词专名扫描（`/tmp/discover3.py`：≥2 词大写专名，单作品集中度 ≥6，剔已建
slug/label/alias + `the-` 前缀）。扫描确认 place **远未饱和**：既往聚焦 SC 巴塔哥尼亚/
FC 极地/EHLA 亚马逊 toponym，尚有大量单作品地点未掘。

**净新 4 buildable 候选**（均 ≥5 solid 单指，已抽样确认）：

| 建序 | 候选 | slug | 主作品×PN | referent | region | rof |
|------|------|------|----------|----------|--------|-----|
| 1 | Healthful House | healthful-house | FF×72 | Facing the Flag 私立疗养院（Thomas Roch 囚所）| （待定 FF 语境）| fictional |
| 2 | Arctic Ocean | arctic-ocean | FC×42（+ACH/WC/GM/OC/MS，共 55 distinct）| 真实北冰洋，单指跨作品 | Arctic | real |
| 3 | Upper Amazon | upper-amazon | EHLA×26 | 亚马逊上游河域（秘鲁森林出水）| Amazon Basin | real |
| 4 | Celestial Empire | celestial-empire | ASC×29（+AWED/GM/RC/TT/FC，共 42 distinct）| 中华帝国（China 别称）| Asia | real |

new_candidates=4 ≥ corpus_new_candidate_min(3) → discover_streak_low 保持 0。
本轮非建页，registry 不变（total 1473 place 405 unknown 0）。

## 决策矩阵（SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue==0 触发下条 | — |
| **4** | **SCN28-zombie（queue==0）** | **queue(place)==0** | **触发** |
| 5/6 | RCH2 系 | stub%=0 | 否 |
| 7 | NEW1 | — | — |

## 候选甄别记录（单指抽样）

- **Healthful House**（FF×72）：`FF-001-002` 疗养院 director 收 carte de visite；
  `FF-001-009` 私立机构，select personnel。→ Facing the Flag 具体场所，fictional，单指。
- **Arctic Ocean**（55 distinct）：`ACH-039-034` "It is called the Arctic Ocean"；
  `ACH-005-041` Johnson 老北冰洋水手。→ 真实北冰洋，跨作品单指（非异指）。
- **Upper Amazon**（EHLA×26）：`EHLA-001-008` 秘鲁森林出 Upper Amazon 之水；
  `EHLA-001-018` 自 Atlantic 岸至 Upper Amazon。→ 亚马逊上游河域，real，单指。
  与既有 `amazon`（place）为父/子域关系，非重复。
- **Celestial Empire**（ASC×29）：`ASC-001-007` Grand Transasiatic 至 Celestial
  Empire 首都；`ASC-001-044` 自 Caspian 至 Celestial Empire。→ 中华帝国（China 别称），
  real，region Asia。**注**：洲级 Asia HOLD 指大陆综述页，Celestial Empire=国家实体，
  可建；建时 region 填 Asia，须核 5 solid 单指（China 别称，非泛指）。

## EXIT-GATE 检查（SCN28 非建页）

- **非建页**：pages=[]，未调用 add_page/edit_page。✔
- **全库重扫**：`/tmp/discover3.py` 扫 968 sentence_index 文件，非凭 queue 推断。✔
- **候选 ≥5 solid**：4 候选主作品 PN 均 ≥26，抽样单指确认。✔
- **查重**：4 候选 slug/label/alias + `the-` 前缀双查皆 NEW。✔
- **registry 不变**：total 1473 place 405 unknown 0。✔

## 六步状态机（SCN28，grow_state 存 R209 起始计数）

| 字段 | R208 起始 | R209 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 208 | 209 |
| type_round | 179 | 180 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 6 | **0（RESET）** |
| discover_streak_low | 0 | 0（new_candidates=4≥3）|
| rounds_since_last_corpus_discover | 144 | 145 |
| last_updated_round | 208 | 209 |

## 遗留问题

1. **place 页数 405**：本轮非建页，registry 全库 1473，unknown 0。
2. **下轮 R209 = NEW1**：since_evv5=4<10、since_discover=0<10、queue(place)=4>0 → §3(7)。
   建 **Healthful House**（healthful-house，FF×72，Facing the Flag 疗养院/囚所），建前
   pages.json 子串 + `the-` 双查，抽样 ≥5 solid，核 FF region 与 rof=fictional。
3. **R209+ 建序**：Healthful House → Arctic Ocean → Upper Amazon → Celestial Empire
   （4 项），R212 建毕队列罄 → 再 SCN28。
4. **饱和证伪**：本轮重扫证 place 未饱和（4 净新）；FF/OC/ASC/UC/TN 等单作品地点脉未充分掘，
   后续 SCN28 可续掘（Facing the Flag / Off on a Comet / Claudius Bombarnac / Black
   Indies / Lighthouse 等）。
5. **Celestial Empire 建议**：为国家实体（China 别称），非大陆综述，可建；洲级 Asia 综述续 HOLD。
6. **HK-dupcheck-the-prefix-blindspot**：4 候选已应用 `the-` 前缀双查。PARK 记录。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=144→145（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/
    Turnagain/Fort Franklin/Cape Dundas/Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-dupcheck-the-prefix-blindspot、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
