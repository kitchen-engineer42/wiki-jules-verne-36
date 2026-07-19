---
round: 336
date: 2026-07-19
type_round: 29
phase: "2.1"
current_type: character
gene: NEW1
pages: [robert-grant]
result: success
---

# GROW 2.1-B · R336 · NEW1 · character — 建 Robert Grant（勇毅随队寻父之幼子；第四批队列末位）

## 执行摘要

Phase 2.1-B character 第 24 建（type_round 29），消费 R330 第四批 discover 队列**建序 74（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0，R337 将触发第五批 SCN28-zombie discover。**

**Robert Grant**（*In Search of the Castaways*）——Grant 船长之幼子，「Mary and Robert were the captain's only children」（SC-004-003），首现 SC-003-026。Glenarvan 越潘帕草原「delighted not to leave Robert behind」（SC-018-013），骑术之佳令 Thalcave「often turned his head to look at Robert」（SC-018-026），而少年笑答「He wants me to be a sailor」（SC-018-032），念父「how he will thank you for saving his life」（SC-018-034）。最险为秃鹰掠空「It was a human body the condor had in his claws ... it was Robert Grant」（SC-014-055），一枪毙鹰「the bird was dead, and the body of Robert was quite concealed beneath his mighty wings」（SC-014-061）。其勇获 Thalcave 赞「pointed to Robert, and said, 'A brave!'」（SC-019-110），求其勿弃「'friend Thalcave, don't leave us!'」（SC-019-080）。终为父之子——誓「never cease searching for my father, who would never have given us up」（SC-064-039）、信「a man like my father doesn't die till he has finished his work」（SC-064-043）、誉 Glenarvan「He is a brother that will never forsake us, never!」（SC-064-046）、寻父复呼「My father!」（SC-064-074）。

**role=supporting**。book=In Search of the Castaways、first_appearance=SC-003、affiliation 空、aliases 空。

**13 distinct solid PN**（SC-004-003、014-055/061、018-013/026/032/034、019-080/110、064-039/043/046/074）：均 solid，逾门。

**查重**：exact-slug robert-grant filesystem + registry entity ABSENT。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Captain Grant]]（R335，本轮回链达成）、[[Mary Grant]]（存）、[[Thalcave]]（存）、[[In Search of the Castaways]]（work，存）——四链均存在无悬挂。R335 遗留的 captain-grant→Robert 纯文本回链可择轮 edit_page 回填（非阻塞，记录于遗留）。

prose-gate：add_page 初稿 2 超段（Role 481、Character 543），各拆一刀后 0 超门再建。**引注**：strict 首验即通过，无需修正。quality featured 未剥离。

character 计数 38→**39**，registry total 1562→**1563**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1>0、since_discover=5 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=1>0，按既有实践走 NEW1 消费建序 74（末位）。消费后 queue=0，R337 转 §3(4)。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| robert-grant | zT1o00 | In Search of the Castaways | supporting | SC-003 | 13 distinct | Grant 幼子-秃鹰掠空-Thalcave 敬勇-寻父誓言；SC 2-char 无 Note；拆 2 超段；strict 首验通过；Captain Grant 回链达成；[[Captain Grant]]/[[Mary Grant]]/[[Thalcave]]/work 互链 |

- **robert-grant**：13 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev zT1o00。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Robert 随队-遇险-寻父因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；SC 2-char 无 Note。✔
- **registry 一致**：total 1563 character 39 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Captain Grant/Mary Grant/Thalcave/In Search of the Castaways 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R337 起始计数）

| 字段 | R336 起始 | R337 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 336 | 337 |
| type_round | 28 | 29 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 272 | 273 |
| last_updated_round | 336 | 337 |

## 遗留问题

1. **character 页数 39**：本轮 +1（robert-grant）。queue(character) 1→**0**（建序 74 末位消费）。registry 全库 **1563**，unknown 0。
2. **下轮 R337 = SCN28-zombie（§3(4)）**：since_evv5=7<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；**queue(character)=0 → §3(4) SCN28-zombie 触发**，勘探补给第五批候选（≥3 grounded + dup-checked）。深池预选：Sangarre（MS 女间谍，Ogareff 之党）、单作品主角 Hector Servadac / Mathias Sandorf / Kaw-djer / Kéraban / Wilhelm Storitz、以及 20KL 簇 Nicholl、MI 簇 Herbert Brown / Gideon Spilett 等。R337 为勘探轮，pages: []，仅 G4。
3. **captain-grant→Robert 回链回填**：R335 captain-grant 页 Robert Grant 为纯文本（当时未建），本轮 robert-grant 已建，可择轮 edit_page 将其回填为 [[Robert Grant]]（非阻塞，DEFERRED）。
4. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。R337 discover + R338 NEW1（消费第五批建序 75）+ R339 EVV5。
5. **SC 簇达九实体**：glenarvan/paganel/ayrton/mary-grant/john-mangles/mcnabbs/thalcave/captain-grant/robert-grant 互链成群。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=272→273（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
