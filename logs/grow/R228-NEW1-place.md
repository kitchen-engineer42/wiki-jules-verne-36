---
round: 228
date: 2026-07-18
type_round: 199
phase: "2.1"
current_type: place
gene: NEW1
pages: [north-west-passage]
result: success
---

# GROW 2.1-B · R228 · NEW1 · place — 建 North-West Passage（北极海路，Atlantic↔Pacific，ACH 主线；McClure 发现，Hatteras 追寻）

## 执行摘要

Phase 2.1-B place 广度扩张第 199 轮（type_round 199）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、streak=2<3、since_discover=0<10、queue(place)=2>0 → §3(7)）。

取 R227 SCN28 队列**建序 1** **North-West Passage**（ACH 主）。建前 pages.json 子串（north-west-passage）+
连字符/`the-` 前缀多查皆 NEW（exact-slug；`no/north-west-passage.md` 不存在）。**单指**：ACH/FC 中
North-West Passage 全指连接大西洋与太平洋的北极海路，无同名异指。**净 9 distinct solid PN**
（剔除 FC-015-016-s2——gather 假阳，可见正文未含「North-West Passage」，仅述「vast sea stretching northwards」）：

- **ACH-042-052**：某记述题为「The North-West Passage, or the End of the Voyage」。
- **ACH-046-057**：极航之问——莫非为寻 North-West Passage？
- **ACH-047-011**：仍未发现——无船曾自 Behring Straits 通达 Baffin's Bay。
- **ACH-047-025**：Investigator 号入 Behring Straits，志在寻 Franklin 或 North-West Passage。
- **ACH-047-029**：McClure 拟经其所发现之 North-West Passage、由 Lancaster Sound 与 Baffin's Bay 返英。
- **ACH-049-041**：某长官近功成时言，不过欲打通 North-West Passage 而已。
- **FC-010-012**：那著名的 North-West Passage？
- **FC-010-020**：即大西洋与太平洋间的直达海路。
- **FC-025-024**：自 McClure 大胆发现以来即名 North-West Passage。

place 计数 418→419，registry total 1486→1487，unknown 恒 0。
add_page 一次成型；prose-gate awk 预检初 2 段 >399（465/462），拆分后 0 超段。pn_validator strict ✓；
build_registry 仅 Robur PARK（无新 alias 冲突 → 无重复建页）。
real_or_fictional=real、region Arctic、book The Adventures of Captain Hatteras、aliases=[]。
Connections/正文含 [[Behring Strait]]/[[Lancaster Strait]]/[[Arctic Ocean]]（三页均存）；
Baffin's Bay 暂散文提及（建序 2，R229 建后可回链）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =2 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=0<10；全局 queue_size≥10（HK-queue-size-scope）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| north-west-passage | y3cJIY | The Adventures of Captain Hatteras | real | Arctic | 9 | 北极海路 Atlantic↔Pacific；McClure 发现；ACH/FC 单指；剔 FC-015-016-s2 假阳 |

- **north-west-passage**：9 distinct solid PN（ACH×6+FC×3，剔 FC-015-016 假阳）；aliases []。链 Behring Strait/Lancaster Strait/Arctic Ocean。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指北极海路 North-West Passage；剔 FC-015-016-s2（假阳，未含术语）；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：awk 全 >399 段预检，初 2 段（465/462）拆分后本版 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid（ACH×6+FC×3）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文（三 wikilink）；description 无冒号/撇号（LAW §8 安全）。✔
- **registry 一致**：total 1487 place 419 unknown 0；仅 Robur PARK。✔
- **查重充分**：pages.json 子串（north-west-passage）+ 连字符/`the-` 前缀多查皆 NEW（exact-slug）。✔
- **单指核 + 假阳剔除**：ACH/FC 逐句确认 North-West Passage 指一海路；剔 FC-015-016-s2（gather 假阳）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R229 起始计数）

| 字段 | R228 起始 | R229 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 228 | 229 |
| type_round | 199 | 200 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 2 | 2 |
| rounds_since_last_corpus_discover | 164 | 165 |
| last_updated_round | 228 | 229 |

## 遗留问题

1. **place 页数 419**：本轮 +1（North-West Passage）。registry 全库 1487，unknown 0。
2. **下轮 R229 = NEW1**：since_evv5=2<10、streak=2<3、since_discover=1<10、queue(place)=1>0 → §3(7)。
   建 **Baffin's Bay**（baffins-bay，ACH×26 distinct，格陵兰西侧北极海，捕鲸场，Forward 号北航必经），
   建前 pages.json 子串 + 连字符/撇号变体双查，抽样 ≥5 solid，region Arctic，real。建后可回链 North-West Passage。
3. **R230 = SCN28-zombie**：Baffin's Bay 建毕 queue(place)==0 → §3(4)。第三次 place discover。
   若 new_candidates<3 → discover_streak_low 2→3 触 §3(2) CLOSE place→event 评估。
4. **discover_streak_low=2**：R230 SCN28 试撇号/连字符 toponym 专项正则（补 HK-discover-possessive-hyphen-toponym-blindspot）；确认饱和则 CLOSE place → event。
5. **HK-discover-possessive-hyphen-toponym-blindspot**〔R227〕：本轮 North-West Passage 即该类；下 SCN28 须专项扫。
6. **HK-dupcheck-bareterm-vs-slug**〔R223〕：本轮遵（north-west-passage 连字符/the- 多查）。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0（拆分达标）。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=164→165（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **featured re-grade DEFERRED**：18 place 页 quality=none，full-library re-grade 顺延至 RFC 批审。
12. **DEFER/DUPLICATE 累积**：chimneys（DUPLICATE R198）；celestial-empire（DUPLICATE R212）；lancaster-sound〔R227 同指 lancaster-strait〕；
    tsalal-island/serpentine-peninsula/beechey-island/lancaster-strait（R223 bare-term 净新但 slug 已建）；cape-mandible〔净 4〕/long-island〔NY 净 4〕/
    Wilmington/Catawba/Cape Hatteras/Cape Dundas/Mackenzie〔river〕/Fort Good Hope/Fort Resolution/Fort Enterprise/Turnagain/Fort Franklin/
    Bathurst Inlet/Mendoza/Neuquem/Araucania DEFER（净<5 或同指）。
13. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-discover-possessive-hyphen-toponym-blindspot、HK-dupcheck-the-prefix-blindspot、HK-dupcheck-semantic-synonym-blindspot、
    HK-dupcheck-bareterm-vs-slug、HK-place-alias-suppression、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
14. **洲级 America/Europe/Asia 续 HOLD**。
