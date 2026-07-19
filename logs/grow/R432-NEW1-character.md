---
round: 432
date: 2026-07-19
type_round: 124
phase: "2.1"
current_type: character
gene: NEW1
pages: [harris]
result: success
---

# GROW 2.1-B · R432 · NEW1 · character — 建 Harris（Dick Sand: A Captain at Fifteen 之 Alvez 奸细向导，伪作善意同乡诱骗 Dick Sand 一行深入安哥拉；开 DSCF 纵深，消费第二十二批建序 143，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 93 建（type_round 124），消费 R430 第二十二批 discover 队列**建序 143**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 144 isaac-hakkabut）。开 DSCF 纵深。**

**Harris**（*Dick Sand: A Captain at Fifteen*）——slave-trader Alvez 之美籍老代理，伪作善意同乡「my name is Harris and I was born in South Carolina」（DSCF-015-058），诡称家在智利边境（DSCF-015-060），献马为饵引一行赴 San Felice 农庄（DSCF-015-090）。武装居队首「Dick Sand and Harris, both armed... kept at the head of the little troop」（DSCF-016-004），以谎术障目：拨枪令 Dick 失的（DSCF-017-051），指长颈鹿为鸵鸟（DSCF-017-058），掩非洲之真相。诡计将破乃遁「Harris was no longer there, and his horse had disappeared with him」（DSCF-018-105），真相爆出「the Portuguese Negoro, and the American Harris, must be in collusion」（DSCF-018-112）。与 Negoro 同谋，夸口「it is even astonishing that I have succeeded in leading him a hundred miles at least from the coast」（DSCF-020-007）。Loanda 越狱之囚、Alvez 老代理（DSCF-020-076），终为 Dick Sand 所杀（DSCF-029-043），尸为土人舁去（DSCF-028-003）。

**role=antagonist**。book='Dick Sand: A Captain at Fifteen'、first_appearance=DSCF-015、affiliation 空、**label=Harris，aliases=[]**。

**13 distinct solid PN**（DSCF-015-058/060/090/117、016-004、017-051/058、018-105/112、020-007/076、028-003、029-043）：均 solid，逾门。「Harris」DSCF 内单指本奸细；无消歧冲突。

**查重**：exact-slug harris filesystem test -f ABSENT（bucket ha）+ registry entity/label/alias 复验（Python 精确）——「Harris / harris」无既建人物页，无冲突。

**DSCF 4-char VVV**：DSCF 为 4-char VVV → 依 RFC-0003 触发 4-char 顾虑，但本 wiki RFC-0003 parked（HK）；PN 校验 strict 通过，pn_prefix 无碰撞，非本轮阻塞。

**wikilink**：[[Dick Sand]]（dick-sand，既建，DSCF-029-043）、[[Negoro]]（negoro，既建，DSCF-020-007）、[[Hercules]]（hercules，既建，DSCF-015-117）、[[Dick Sand: A Captain at Fifteen]]（work，存，DSCF-020-076/028-003）——四链均无悬挂（labels 经 registry 复核）。**DSCF 簇开纵深**（harris 补 dick-sand/negoro/hercules）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 107→**108**，registry total 1631→**1632**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 143。消费后 queue=1 → R433 继续 NEW1（建序 144 isaac-hakkabut）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| harris | mhgTnv | Dick Sand: A Captain at Fifteen | antagonist | DSCF-015 | 13 distinct | 伪同乡诱骗-献马为饵-武装居队首-拨枪障目-指鹿为鸵-诡计破而遁-与 Negoro 同谋-Loanda 越狱囚-Alvez 老代理-终为 Dick 所杀；label Harris / alias []；DSCF 4-char RFC-0003 parked（非阻塞）；0 超段直建；strict 首验通过；四链 [[Dick Sand]]/[[Negoro]]/[[Hercules]]/[[Dick Sand: A Captain at Fifteen]] |

- **harris**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev mhgTnv（size 2896）。quality featured 回填。pn_validator --mode strict ✓。**DSCF 簇开纵深；Harris 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Harris 诱骗-同谋-伏诛因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=antagonist ∈ enum。✔
- **registry 一致**：total 1632 character 108 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Dick Sand + Negoro + Hercules + Dick Sand: A Captain at Fifteen 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R433 起始计数）

| 字段 | R432 起始 | R433 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 432 | 433 |
| type_round | 124 | 125 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 368 | 369 |
| last_updated_round | 432 | 433 |

## 遗留问题

1. **character 页数 108**：本轮 +1（harris）。queue(character) 2→**1**（建序 143 消费）。registry 全库 **1632**，unknown 0。
2. **下轮 R433 = NEW1（§3(7)）**：since_evv5=6<10；queue=1>0 且 since_discover=2<10 → NEW1，消费建序 144 **isaac-hakkabut**（OC Hansa 号吝啬犹太商贩，86 mentions，首现 OC-019；配对 [[Ben Zoof]]）。
3. **第二十二批消费进度**：R431 NEW1（142 bell ✓）→ R432 NEW1（143 harris ✓）→ R433 NEW1（144 isaac-hakkabut 待）→ queue 归 0 → R434 SCN28-zombie 补第二十三批。**EVV5 时点**：since_evv5 R433 起始=6，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**DSCF 簇开纵深**（harris→dick-sand/negoro/hercules 反向）、ACH 簇收束（bell/altamont/johnson 互链反向、Simpson/Pen/Wilson 待建）、OC 簇（isaac-hakkabut 待建→ben-zoof 反向）、SC 簇（olbinett/lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave/paganel 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs、Bell ACH vs SC/TTLU 一次性同名）；（g）RFC-0003 4-char VVV 宽度（DSCF 等 4-char VVV 触发，parked）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=368→369（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
