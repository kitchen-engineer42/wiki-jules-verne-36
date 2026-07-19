---
round: 327
date: 2026-07-19
type_round: 20
phase: "2.1"
current_type: character
gene: NEW1
pages: [nadia]
result: success
---

# GROW 2.1-B · R327 · NEW1 · character — 建 Nadia（伴 Strogoff 越西伯利亚之流放者之女）

## 执行摘要

Phase 2.1-B character 第 17 建（type_round 20），消费 R322 第三批 discover 队列**建序 67**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Nadia**（*Michael Strogoff*）——年少 Livonia 女子，「from Riga; she was Livonian, consequently Russian」（MS-007-010），穿战乱之西伯利亚往 Irkutsk 寻其流放之父。初以一握报名：「'Nadia,' said she, holding out her hand」（MS-008-019）。为共越鞑靼防线，Michael 纳其入伪名之下——「'Come, Nadia,' answered Michael, 'and make what use you like of your brother Nicholas Korpanoff'」（MS-008-020）。虽被告诫「there are physical fatigues a woman may be unable to endure」（MS-010-012），仍力行，得其赞「'You are a brave girl, Nadia'... 'God Himself would have led you'」（MS-010-045）。被掳至 Omsk 与 Michael 之母同陷，「rendered to the mother those attentions which she had herself received from the son」（MS-021-075），其向 Marfa 之近乃「an instinctive sympathy」所「first drew Nadia towards」（MS-021-083），谓其「'Brother, sister, mother--he has been all to me!'」（MS-021-094）。Michael 目盲后二人易位，其为其目——「Michael could now only see with Nadia's eyes」（MS-028-001），步履赖「that trembling little hand which guided him」（MS-025-006）。忍苦为其标记：赴 Irkutsk 苦道上「Nadia never complained」（MS-025-036），匮乏中予 Michael「the lion's share of this scanty meal」（MS-025-033）；且认 Marfa 为母，「'I am Marfa's daughter'」（MS-014-038）。

**role=supporting**。book=Michael Strogoff、first_appearance=MS-008、affiliation 空、aliases 空。

**13 distinct solid PN**（MS-007-010、008-019/020、010-012/045、014-038、021-075/083/094、025-006/033/036、028-001）：均 solid，逾门。

**查重**：exact-slug nadia filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Michel Strogoff]]（R321 character）、[[Michael Strogoff]]（work）——二链均存在无悬挂。Marfa Strogoff 纯文本（未建）。MS 簇（michel-strogoff/michael-strogoff/nadia + events strogoff-blinding/assault-on-irkutsk）。

prose-gate：add_page 初稿 2 超段（413/404），拆段后 0 超门。**引注修正**：strict 首验 MS-028-001 重叠 1.75%<2%（Relationships bullet 关系散文与源句字面重叠低），改引 MS-025-006（源句含 companion/guided/hand，重叠达标），edit_page rev cSO0fD 后 strict ✓；quality featured 未剥离（/tmp 保 quality 字段）。

character 计数 31→**32**，registry total 1555→**1556**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2>0、since_discover=4 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费建序 67。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| nadia | cSO0fD | Michael Strogoff | supporting | MS-008 | 13 distinct | Livonia 女-伪妹-越西伯利亚-盲导-忍苦单指；MS 2-char 无 Note；拆 2 超段；引注 MS-028-001→MS-025-006 修正后 strict ✓；[[Michel Strogoff]]/[[Michael Strogoff]] 互链 |

- **nadia**：13 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev dsbG5x→edit_page rev cSO0fD。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Nadia 越西伯利亚-盲导-忍苦因果；引注修正后 strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建页改页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1556 character 32 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Michel Strogoff/Michael Strogoff 二链存在无悬挂；Marfa Strogoff 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R328 起始计数）

| 字段 | R327 起始 | R328 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 327 | 328 |
| type_round | 19 | 20 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 263 | 264 |
| last_updated_round | 327 | 328 |

## 遗留问题

1. **character 页数 32**：本轮 +1（nadia）。queue(character) 2→**1**（建序 67 消费；余 68：ivan-ogareff）。registry 全库 **1556**，unknown 0。
2. **下轮 R328 = NEW1（§3(7)）**：since_evv5=9<10；queue(character)=1>0 → §3(7) NEW1，消费建序 68（ivan-ogareff）——**队列将空**。Ivan Ogareff（book Michael Strogoff，pn_anchor MS-002，role antagonist）——叛徒军官、通鞑靼、Strogoff 之私敌；与既建 michel-strogoff/michael-strogoff/assault-on-irkutsk 可互链。消歧须避 MS-015-052（Ogareff 与 Strogoff 同段）。
3. **EVV5 下次约 R329**（since_evv5 于 R318 复位，+10）：R328 起 since_evv5=9，R329 达 10——**EVV5 反射轮预计落 R329**（消费建序 68、队列空之后）。届时 §3(1b) EVV5 优先（character schema 反射）。R329 后 queue==0 → 若非 EVV5 则 §3(4) SCN28-zombie 第四批 discover。
4. **MS 簇壮大**：michel-strogoff/michael-strogoff/nadia + events；建序 68（ivan-ogareff）建成后 MS 达四实体页。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=263→264（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
