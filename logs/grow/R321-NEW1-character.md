---
round: 321
date: 2026-07-19
type_round: 14
phase: "2.1"
current_type: character
gene: NEW1
pages: [michel-strogoff]
result: success
---

# GROW 2.1-B · R321 · NEW1 · character — 建 Michel Strogoff（沙皇信使、穿越西伯利亚送密令之主角）

## 执行摘要

Phase 2.1-B character 类型第 12 建（type_round 14），消费 R314 第二批 discover 队列**建序 62（末条）**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Michel Strogoff**（*Michael Strogoff* 主角）——沙皇信使团精锐上尉，负密信穿鞑靼叛乱之西伯利亚。召入御书房受命（MS-004-029/032）；Omsk 猎人 Peter Strogoff 之子、母 Marfa 尚居其地，众判其为唯一能自 Moscow 达 Irkutsk、越叛境冒诸险者（MS-004-035/033）。沙皇托信「deliver into the hands of the Grand Duke, and to no other but him」（MS-004-059），其上系全 Siberia 安危与大公之命（MS-004-074）；以「for God, for Russia, for my brother, and for myself」遣之（MS-004-081）。行程三千四百英里（MS-005-001），历俘囚灾厄终抵城下半 verst 而叹「At last!」（MS-030-062）。行动之人、不惑不疑（MS-004-030），不惧霜雪（MS-005-002），俘囚列中最忍最耐（MS-020-017）。其至难在自持：Omsk 街头为母所认，冷答「A resemblance deceives you」（MS-015-063）——认母即败使命；虽「would have given his life」拥母犹守其誓（MS-015-065）。伴 Nadia 越西伯利亚终携其脱险（MS-029-005）；受诫须避叛徒 Ivan Ogareff（MS-015-052）。

**role=protagonist**。book=Michael Strogoff、first_appearance=MS-004、affiliation=Corps of the Czar's Couriers。aliases=[Nicholas Korpanoff]（其化名 disguise；无冲突）。

**16 distinct solid PN**（MS-004×7/005×2/015×3/020/029/030）：004-029、004-030、004-032、004-033、004-035、004-059、004-074、004-081、005-001、005-002、015-052、015-063、015-065、020-017、029-005、030-062。

**查重**：exact-slug michel-strogoff filesystem + registry entity ABSENT（既存 michael-strogoff=work、strogoff-blinding=event，无 character）。

**MS 2-char VVV**：无需 RFC-0003 Note。

**label 冲突处置（关键）**：初建 label「Michel Strogoff」触发 build_registry 新 alias 冲突——**work michael-strogoff 既以「Michel Strogoff」为 alias**（另 alias「Michael Strogoff: The Courier of the Czar」）。为免破坏角色页自身 [[Michel Strogoff]] 解析（异于 Robur 型可 PARK 之 alias 冲突，此为**新页主 label** 冲突），就源解决：edit_page 于 **work 页释放 alias「Michel Strogoff」**（rev 1v2qbr，size 2688→2669，quality standard 保留），使角色独占该 label。语义正解：法文名「Michel Strogoff」指其人，英译书名「Michael Strogoff」指其书。复建 registry 仅余 Robur PARK。

**wikilink（同书簇）**：[[Michael Strogoff]]（work）、[[The Blinding of Michael Strogoff]]（event strogoff-blinding）、[[Irkutsk]]（place）——三链均存在无悬挂。Nadia/Marfa/Ivan Ogareff/Czar 纯文本（未建）。

prose-gate：add_page 初稿 0 超段。**pn_validator strict 首过 ✓**（无角色页 edit，quality featured 未被剥离）。

character 计数 26→**27**，registry total 1550→**1551**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1>0、since_discover=6 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=1>0，按既有实践走 NEW1 消费末条建序 62。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| michel-strogoff | ybCgc7 | Michael Strogoff | protagonist | MS-004 | 16 distinct | 信使-使命-自持-伴 Nadia 单指；MS 2-char 无 Note；strict 首过 ✓；label 冲突→释放 work alias；[[Michael Strogoff]]/[[The Blinding of Michael Strogoff]]/[[Irkutsk]] 互链 |
| michael-strogoff | 1v2qbr | —(work) | — | — | — | 释放 alias「Michel Strogoff」予角色页（解 label 冲突）；quality standard 保留；size 2688→2669 |

- **michel-strogoff**：16 distinct solid PN；aliases=[Nicholas Korpanoff]；character-schema 五 H2。add_page rev ybCgc7。pn_validator --mode strict ✓。
- **michael-strogoff（work）**：仅 frontmatter aliases 减一，正文未动。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Strogoff 信使-使命-自持因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门。✔
- **G3 ≥5 distinct PN**：16 solid，远逾门。✔
- **G4 脚本建页**：add_page（角色）+ edit_page（work 释 alias），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1551 character 27 unknown 0；仅 Robur PARK；新 label 冲突已就源消解。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Michael Strogoff/The Blinding of Michael Strogoff/Irkutsk 三链存在无悬挂；余纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R322 起始计数）

| 字段 | R321 起始 | R322 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 321 | 322 |
| type_round | 13 | 14 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 257 | 258 |
| last_updated_round | 321 | 322 |

## 遗留问题

1. **character 页数 27**：本轮 +1（michel-strogoff）。queue(character) 1→**0**（建序 62 末条消费）。registry 全库 **1551**，unknown 0。
2. **下轮 R322 = SCN28 第三批 discover（§3(3)/§3(4)）**：queue(character)=0 → §3(4) SCN28-zombie 触发（且 since_discover=7、§3(3) queue<10 亦成立）。须为 character 补给候选。深池仍充沛：**SC 群像**（Mary Grant/Robert Grant/John Mangles/McNabbs/Thalcave/Captain Grant）、**MS 余角**（Nadia/Ivan Ogareff/Marfa Strogoff/Feofar-Khan/Harry Blount/Alcide Jolivet）、**DSCF 余角**（Mrs. Weldon/Cousin Benedict/Tom/Bat/Acteon/Austin）、**单作品主角**（Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz/Nicholl/Hans）。
3. **MS 簇渐成**：michel-strogoff（character）+ michael-strogoff（work）+ strogoff-blinding/assault-on-irkutsk（event）+ Irkutsk 等 place 群。Nadia/Ogareff 若建可深化互链。
4. **EVV5 下次约 R328**（since_evv5 于 R318 复位，+10）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。**新增（e）**：character-vs-work 同名 label 张力——本轮以「释放 work alias」就源消解（michael/michel 分指书/人），后续同型（如未来 work/character 共名）沿此裁例或统一 RFC。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=257→258（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
