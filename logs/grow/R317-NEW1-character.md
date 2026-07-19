---
round: 317
date: 2026-07-19
type_round: 10
phase: "2.1"
current_type: character
gene: NEW1
pages: [negoro]
result: success
---

# GROW 2.1-B · R317 · NEW1 · character — 建 Negoro（Pilgrim 之葡籍船厨、篡改罗盘之反派奴隶贩子）

## 执行摘要

Phase 2.1-B character 类型第 9 建（type_round 10），消费 R314 第二批 discover 队列**建序 59**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Negoro**（*Dick Sand: A Captain at Fifteen* 之反派）——生为葡人、英语流利，任 *Pilgrim* 号船厨（DSCF-002-008）；年约四十（DSCF-002-011），孤僻离群，遇沉船残骸时独不离厨舱、全船唯一无动于衷者（DSCF-003-004）。其叛卖蓄谋而隐秘：以罪手篡乱罗盘、令船一路偏向（DSCF-011-007）；船身猛摇将其掷向罗经柜，起身犹握方自柜下取之铁片、抢在 [[Dick Sand]] 察觉前藏之（DSCF-012-013）。船破后审视沙滩与崖如追忆旧迹之人（DSCF-014-022）——盖彼熟此 Angola 海岸、与美人 Harris 通谋（DSCF-018-112）。其行皆出残忍与宿怨：自言与少年船长有账待算（DSCF-020-010）、面露实之残酷（DSCF-020-016）；终显为奴贩 Alvez 之爪牙，冷谋将俘众分二——可鬻为奴者与其余（DSCF-020-078）。彼乃不满于虐、更享其苦之恶徒（DSCF-030-012）；囚 Mrs. Weldon，谋以自称「escaped faithful servant」之伪信诱其夫入彀（DSCF-031-066）。

**role=antagonist**（本批首个反派角色）。book=Dick Sand, A Captain at Fifteen、first_appearance=DSCF-002。affiliation 空。aliases 空。

**12 distinct solid PN**（DSCF-002×2/003/011/012/014/018/020×3/030/031）：002-008、002-011、003-004、011-007、012-013、014-022、018-112、020-010、020-016、020-078、030-012、031-066。

**查重**：exact-slug negoro filesystem ABSENT；registry type=character 无命中（pages.json entity 检查 ABSENT）。

**DSCF 4-char VVV**：**须 RFC-0003 Note**（页顶已置 `> **Note:** ... 4-character work code (\`DSCF\`) ...`）。

**wikilink**：[[Dick Sand: A Captain at Fifteen]]（work，label 校验为「Dick Sand: A Captain at Fifteen」）、[[Dick Sand]]（character，R 既建）——二链均存在无悬挂。Harris/Mrs. Weldon/Alvez 纯文本（未建）。

prose-gate：初稿 0 超段（含 Note blockquote 排除）。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未被剥离）。

character 计数 23→**24**，registry total 1547→**1548**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4>0、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| negoro | De8eLj | Dick Sand, A Captain at Fifteen | antagonist | DSCF-002 | 12 distinct | 船厨-罗盘破坏-奴贩-反派单指；DSCF 4-char **有 RFC-0003 Note**；strict 首过 ✓；[[Dick Sand]]/[[Dick Sand: A Captain at Fifteen]] 互链 |

- **negoro**：12 distinct solid PN；aliases 空；character-schema 五 H2 + 页顶 RFC-0003 Note。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Negoro 船厨-破坏-奴贩因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：散文段 0 超门（Note blockquote 排除）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；DSCF 4-char **有 RFC-0003 Note**。✔
- **registry 一致**：total 1548 character 24 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Dick Sand: A Captain at Fifteen/Dick Sand 二链存在无悬挂；Harris/Weldon/Alvez 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R318 起始计数）

| 字段 | R317 起始 | R318 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 317 | 318 |
| type_round | 9 | 10 |
| rounds_since_last_evv5 | 9 | **10**（达阈值）|
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 253 | 254 |
| last_updated_round | 317 | 318 |

## 遗留问题

1. **character 页数 24**：本轮 +1（negoro）。queue(character) 4→**3**（建序 59 消费；余 60-62：hercules/glenarvan/michel-strogoff）。registry 全库 **1548**，unknown 0。
2. **下轮 R318 = EVV5（§3(1)/§3(1b)）**：**since_evv5=10≥evv5_interval(10) → 触发 EVV5**（模板演化评审轮，非 NEW1 建页）。EVV5 为 character-schema 模板评审：抽样近建页（pencroft/herbert/paganel/neb/gideon-spilett/negoro）复核五 H2 结构、frontmatter 字段完整性、PN 密度、wikilink 簇连通，产出模板演化建议（若有），复位 since_evv5=0。**Phase 2.1 EVV6 封存点仍 DEFERRED**（Phase 2.1 关闭前统一回填 closed_types[].evv6_score）。
3. **建序 60-62 顺延至 R319+**：EVV5 后 R319 = NEW1 消费建序 60（hercules，book Dick Sand, A Captain at Fifteen，pn_anchor DSCF-004，DSCF 4-char **须 Note**，role supporting：力大无穷之获救黑人，忠勇护主；与 negoro/dick-sand 同书可互链）。
4. **MI 五殖民者簇完整**（上轮 R316 达成）：cyrus-harding 早期页交叉链回填 DEFERRED。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC（5 例阈值）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）；本轮 over-400=0。
8. **entity quality none 22 例**：既有债，Phase 2.1 EVV6 全库评审统一处理。
9. **corpus-discover 顺延**：since_corpus=253→254（dead 变量）。featured re-grade DEFERRED。
