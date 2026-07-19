---
round: 319
date: 2026-07-19
type_round: 12
phase: "2.1"
current_type: character
gene: NEW1
pages: [hercules]
result: success
---

# GROW 2.1-B · R319 · NEW1 · character — 建 Hercules（Pilgrim castaways 之巨力忠仆）

## 执行摘要

Phase 2.1-B character 类型第 10 建（type_round 12），消费 R314 第二批 discover 队列**建序 60**。决策机 §3 首匹配 **NEW1**
（R318 EVV5 后 since_evv5=0<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Hercules**（*Dick Sand: A Captain at Fifteen* 之获救黑人同伴）——力大无穷、殖民小队之守护者。其力之巨，对彼言「strong」一字或已冒失（DSCF-010-023）；然巨力偕温柔，举幼 Jack 如举软木婴孩、童为之欢呼（DSCF-005-008）。*Pilgrim* 船上为镇乱之手：奸厨 [[Negoro]] 胁少年船长，Hercules 但以重掌按其肩（DSCF-012-031）；执令如军人之精准不容迟（DSCF-016-105）。船破被俘后，其力转为脱逃与救援：纵身一跃落地、于弹雨中没入林下（DSCF-024-113）。其忠不倦：伪作术士单身潜入 Kazounde，先数日擒 Cousin Benedict 以探 Mrs. Weldon 囚所（DSCF-035-013）；不惜命救 [[Dick Sand]]（DSCF-035-029）——novice 半溺醒来，Hercules 跪其侧倾力照拂（DSCF-035-018）。机智兼力：夜巡河岸幸得漂舟、载众脱险（DSCF-035-042）。

**role=supporting**。book=Dick Sand, A Captain at Fifteen、first_appearance=DSCF-004。affiliation 空。aliases 空。

**9 distinct solid PN**（DSCF-005/010/012/016/024/035×4）：005-008、010-023、012-031、016-105、024-113、035-013、035-018、035-029、035-042。（≥5 逾门，落 target 8-10 内。）

**查重**：exact-slug hercules filesystem + registry entity ABSENT。

**DSCF 4-char VVV**：**须 RFC-0003 Note**（页顶已置）。

**wikilink（同书簇内互链）**：[[Dick Sand: A Captain at Fifteen]]（work）、[[Dick Sand]]（R 既建）、[[Negoro]]（R317 既建）——三链均存在无悬挂。Mrs. Weldon/Cousin Benedict/little Jack 纯文本（未建）。**DSCF 簇渐成**（dick-sand/negoro/hercules 三页互链）。

prose-gate：初稿 0 超段（Note blockquote 排除）。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

character 计数 24→**25**，registry total 1548→**1549**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R318 刚复位）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3>0、since_discover=4 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| hercules | jBpGS2 | Dick Sand, A Captain at Fifteen | supporting | DSCF-004 | 9 distinct | 巨力-温柔-镇乱-救主单指；DSCF 4-char **有 RFC-0003 Note**；strict 首过 ✓；[[Dick Sand]]/[[Negoro]]/work 互链 |

- **hercules**：9 distinct solid PN；aliases 空；character-schema 五 H2 + 页顶 RFC-0003 Note。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Hercules 巨力-救援因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门（Note blockquote 排除）。✔
- **G3 ≥5 distinct PN**：9 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；DSCF 4-char **有 RFC-0003 Note**。✔
- **registry 一致**：total 1549 character 25 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Dick Sand: A Captain at Fifteen/Dick Sand/Negoro 三链存在无悬挂；Weldon/Benedict/Jack 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R320 起始计数）

| 字段 | R319 起始 | R320 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 319 | 320 |
| type_round | 11 | 12 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 255 | 256 |
| last_updated_round | 319 | 320 |

## 遗留问题

1. **character 页数 25**：本轮 +1（hercules）。queue(character) 3→**2**（建序 60 消费；余 61-62：glenarvan/michel-strogoff）。registry 全库 **1549**，unknown 0。
2. **下轮 R320 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 61（glenarvan）。Lord Glenarvan（book In Search of the Castaways，pn_anchor SC-001，**role=protagonist**，SC 2-char 无 Note）——Duncan 号船主、寻 Grant 船长探险队领袖；与既建 paganel 同书可互链。
3. **DSCF 簇渐成**：dick-sand/negoro/hercules 三页互链。后续 DSCF 尚有 Mrs. Weldon/Cousin Benedict/Tom/Bat/Acteon/Austin 深池可建。
4. **queue 见底预警**：queue(character) 降至 2，R321 消费建序 62（michel-strogoff）后归 0 → R322 触发 §3(3)/§3(4) SCN28 第三批 discover 补给（深池仍充沛：SC 群像、DSCF 余角、单作品主角 Hector Servadac/Mathias Sandorf 等）。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=255→256（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
