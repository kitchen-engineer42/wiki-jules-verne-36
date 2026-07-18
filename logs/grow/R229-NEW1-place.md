---
round: 229
date: 2026-07-18
type_round: 200
phase: "2.1"
current_type: place
gene: NEW1
pages: [baffins-bay]
result: success
---

# GROW 2.1-B · R229 · NEW1 · place — 建 Baffins Bay（格陵兰西侧北极海，捕鲸场，Forward 号北航必经；Hatteras 归欧之路）

## 执行摘要

Phase 2.1-B place 广度扩张第 200 轮（type_round 200）。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10、streak=2<3、since_discover=1<10、queue(place)=1>0 → §3(7)）。

取 R227 SCN28 队列**建序 2** **Baffin's Bay**（ACH 主）。建前 pages.json 子串（baffins-bay）+
连字符/撇号变体多查皆 NEW（exact-slug）。**单指**：ACH 全书主指格陵兰西侧真实北极海，无同名异指。
**净 9 distinct solid PN**（ACH×20 中择要，四节分配）：

- **ACH-010-030**：Baffin's Bay 冰解后近全通，成众捕鲸船渊薮。
- **ACH-009-073**：Forward 逾 72 度，海峡未开无从入湾。
- **ACH-058-004**：抵岸时湾半冻，三英里外浪拍冰缘——归欧之路。
- **ACH-057-020**：Doctor 计湾距不逾 600 英里，决取捷径抵之。
- **ACH-018-030**：McClintock Channel 尽处 Melville Bay，其外海峡通 Baffin's Bay。
- **ACH-006-020**：述及一长串海峡自湾通向外海。
- **ACH-051-041**：湾岸 Crimson Cliffs 红物，Doctor 装瓶待考。
- **ACH-047-011**：North-West Passage 未通——无船曾自 Behring Straits 达 Baffin's Bay。
- **ACH-014-030**：Inglefield 驾 Isabelle 溯湾至 Victoria Point（80 度）折返 Beechey Island。

place 计数 419→420，registry total 1487→1488，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 3 段 >399（426/433/411），拆分后 0 超段。pn_validator strict ✓。
real_or_fictional=real、region Arctic、book The Adventures of Captain Hatteras、aliases=[]。
Connections/正文含 [[North-West Passage]]/[[Behring Strait]]/[[Beechey Island]]/[[Melville Bay]]（四页均存）。

**label 去撇号修正（本轮教训）**：初以 `label: "Baffin's Bay"`（撇号）建页，build_registry
即报**新 alias 冲突**（`'Baffin's Bay' → baffin-bay vs baffins-bay`）——label slugify（撇号→丢）
得 `baffin-bay` 与 id `baffins-bay` 分歧。**非重复页**（baffin-bay 页不存在），但污染
「仅 Robur PARK」查重不变量。经 edit_page.py 改 `label: Baffins Bay`（去撇号，slugify=id）→
registry 复归仅 Robur PARK。记 **HK-place-apostrophe-label-slug-divergence**（撇号 toponym label
须去撇号或令 slugify 对齐 id，否则 registry 恒噪声）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =2 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=1<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| baffins-bay | kHM6CV | The Adventures of Captain Hatteras | real | Arctic | 9 | 格陵兰西侧北极海，捕鲸场；ACH 单指；label 去撇号避 slugify 分歧 |

- **baffins-bay**：9 distinct solid PN（ACH×9 中择，全书 ACH×20）；aliases []；label `Baffins Bay`（去撇号）。链 North-West Passage/Behring Strait/Beechey Island/Melville Bay。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Baffin's Bay；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，初 3 段（426/433/411）拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid（ACH）。✔
- **G4 脚本建页**：add_page.py 建 + edit_page.py 修 label，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（四 wikilink）；label 去撇号（LAW §8 + slugify 双安全）；description 无冒号/撇号。✔
- **registry 一致**：total 1488 place 420 unknown 0；仅 Robur PARK（Baffin 冲突经 label 修正消除）。✔
- **查重充分**：pages.json 子串（baffins-bay）+ 连字符/撇号变体多查皆 NEW（exact-slug）。✔
- **单指核**：ACH 逐句确认 Baffin's Bay 指一北极海。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R230 起始计数）

| 字段 | R229 起始 | R230 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 229 | 230 |
| type_round | 200 | 201 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 2 | 2 |
| rounds_since_last_corpus_discover | 165 | 166 |
| last_updated_round | 229 | 230 |

## 遗留问题

1. **place 页数 420**：本轮 +1（Baffins Bay）。registry 全库 1488，unknown 0。
2. **下轮 R230 = SCN28-zombie**：since_evv5=3<10、streak=2<3、since_discover=2<10、queue(place)==0 → §3(4)。
   第三次 place discover。试**撇号/连字符 toponym 专项正则**（补 HK-discover-possessive-hyphen-toponym-blindspot）
   + 河流/海角/湖泊等未建小特征细扫。
3. **discover_streak_low=2（关键分岔）**：R230 SCN28 若 new_candidates<3 → **streak 2→3** 触 §3(2)
   **CLOSE place → event 评估**（R231 起）。若 ≥3 则 streak reset=0 续 NEW1。
   前二 discover（R223/R227）皆 2 净新；撇号/连字符专项扫或再补数枚北极/河流特征。
4. **HK-place-apostrophe-label-slug-divergence**〔R229 新〕：撇号 toponym label 须去撇号令 slugify 对齐 id。
5. **HK-discover-possessive-hyphen-toponym-blindspot**〔R227〕：R230 专项扫重点。
6. **HK-dupcheck-bareterm-vs-slug**〔R223〕：本轮续遵。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=165→166（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；lancaster-sound〔R227 同指 lancaster-strait〕；
    tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建）；cape-mandible〔净 4〕/long-island〔NY 净 4〕/
    Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/
    Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot、HK-place-apostrophe-label-slug-divergence〔新〕、HK-dupcheck-the-prefix-blindspot、
    HK-dupcheck-semantic-synonym-blindspot、HK-dupcheck-bareterm-vs-slug、HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、
    RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
