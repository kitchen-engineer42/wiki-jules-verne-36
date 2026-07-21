---
round: 433
date: 2026-07-20
type_round: 125
phase: "2.1"
current_type: character
gene: NEW1
pages: [isaac-hakkabut]
result: success
---

# GROW 2.1-B · R433 · NEW1 · character — 建 Isaac Hakkabut（Off on a Comet 之 Hansa 号吝啬商贩，彗星 Gallia 上唯利是图的守财者；消费第二十二批建序 144，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 94 建（type_round 125），消费 R430 第二十二批 discover 队列**建序 144**（末位）。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=2<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R434 = §3(4) SCN28-zombie 补第二十三批。**

**Isaac Hakkabut**（*Off on a Comet*）——Cologne 出身的地中海旧货商，自名并常住其 tartan 小船 *Hansa*（OC-019-051）；彗星 Gallia 掳走一片地球后，其满载货舱成殖民地存续命脉（OC-020-024），而他本人为货舱蜷居的守财misanthrope（OC-031-029）。灾变中仍逼讨西班牙人过船费（OC-020-038），谋尽揽 Gallia 全部钱币（OC-030-010），借 steelyard 放高利（OC-032-038）私喜「eighteen hundred per cent. interest」（OC-032-078）。诡秤行骗终被 Rosette 咖啡称重之局揭穿「The old reprobate, the rascal has cheated us!」（OC-040-083 / OC-041-001）。性格母题：贪欲不可拔除（OC-030-009）、亲吻金币（OC-040-068）、逃生气球上终以命重于财、解下暗藏钱带（OC-043-071）。叙事以其时代的 antisemitic「usurer」漫画式刻画定位（OC-020-018），本页以编辑者中性口吻标注此点、以引文承其守财-放贷-诡秤三母题，不复述最露骨的种族修辞。

**role=supporting**。book=Off on a Comet、first_appearance=OC-019、affiliation 空、**label=Isaac Hakkabut，aliases=[]**。

**18 distinct solid PN**（OC-019-051、020-018/024/038、030-009/010、031-029、032-038/078、035-007、040-025/068/078/083、041-001/004、043-071、045-021）：远逾 ≥5 门、逾 12-15 目标区。「Hakkabut / Isaac」OC 内单指本商贩；无消歧冲突。

**方法记录（ultracode workflow）**：本轮以 mine→verify 双阶 workflow 佐研——8 miner 子代理分片扫 19 章 sentence_index 抽 PN-grounded 引文，8 skeptic 子代理逐组复核（引文逐字兑现 + 指称单指 Hakkabut）。产 97 候选 / 96 validated / 70 distinct PN；本页自其中择 18 条最强跨五节铺陈。全引文经 skeptic 逐字回验 + pn_validator strict 复核。

**查重**：exact-slug isaac-hakkabut filesystem test -f ABSENT（bucket is）+ registry entity/label/alias 复验（Python 精确）——「Isaac Hakkabut / Hakkabut / isaac-hakkabut」无既建人物页，无冲突。

**wikilink**：[[Hector Servadac]]（hector-servadac，既建，OC-035-007）、[[Ben Zoof]]（ben-zoof，既建，OC-041-004）、[[Palmyrin Rosette]]（palmyrin-rosette，既建，OC-040-025/078）、[[Off on a Comet]]（work，存，OC-045-021）——四链均无悬挂（labels 经 registry 复核）。**OC 簇开纵深**（isaac-hakkabut 补 ben-zoof/palmyrin-rosette/hector-servadac）。

prose-gate：add_page 初稿 0 超段（正则复核 0 over-400；Relationships 三 bullet 间已插空行分段）。**引注**：strict 首验即通过。quality featured 回填。

character 计数 108→**109**，registry total 1632→**1633**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 144（末位）。消费后 queue=0 → R434 = §3(4) SCN28-zombie 补第二十三批。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| isaac-hakkabut | wWOlPV | Off on a Comet | supporting | OC-019 | 18 distinct | Hansa 号吝啬旧货商-货舱为殖民地命脉-逼讨过船费-谋揽 Gallia 全币-steelyard 放高利 1800%-诡秤诈骗被 Rosette 揭穿-亲吻金币-气球暗藏钱带终以命重于财-叙事 antisemitic usurer 漫画（中性标注）；label Isaac Hakkabut / alias []；workflow mine→verify 佐研；0 超段直建；strict 首验通过；四链 [[Hector Servadac]]/[[Ben Zoof]]/[[Palmyrin Rosette]]/[[Off on a Comet]] |

- **isaac-hakkabut**：18 distinct solid PN；aliases []；character-schema 五 H2。add_page rev wWOlPV（size 3726）。quality featured 回填。pn_validator --mode strict ✓。**OC 簇开纵深；Hakkabut 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Hakkabut 守财-放贷-诡秤-伏诛因果；96 validated 引文经 skeptic 逐字回验；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（正则复核；Relationships bullet 分段）。✔
- **G3 ≥5 distinct PN**：18 solid，远逾门（逾 12-15 目标）。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（description 单引号）；role=supporting ∈ enum。✔
- **registry 一致**：total 1633 character 109 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突（3 alias warn 均既有 parked HK：Claudius Bombarnac / Hector Servadac / Robur the Conqueror，非本页引入）。✔
- **wikilink 完整性**：Hector Servadac + Ben Zoof + Palmyrin Rosette + Off on a Comet 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R434 起始计数）

| 字段 | R433 起始 | R434 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 433 | 434 |
| type_round | 125 | 126 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 369 | 370 |
| last_updated_round | 433 | 434 |

## 遗留问题

1. **character 页数 109**：本轮 +1（isaac-hakkabut）。queue(character) 1→**0**（第二十二批建序 144 末位消费，全批 bell/harris/isaac-hakkabut 3 建告罄）。registry 全库 **1633**，unknown 0。
2. **下轮 R434 = SCN28-zombie（§3(4)）**：queue(character)=0 → zombie discover 补第二十三批候选（3 候选，跨作品避集中；since_discover 归零）。**EVV5 时点**：since_evv5 R434 起始=7，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**。
3. **回链回填债**（DEFERRED，非阻塞）：**OC 簇开纵深**（isaac-hakkabut→ben-zoof/palmyrin-rosette/hector-servadac 反向）、DSCF 簇（harris→dick-sand/negoro/hercules 反向）、ACH 簇收束（bell/altamont/johnson 互链反向、Simpson/Pen/Wilson 待建）、SC 簇（olbinett/lady-helena→glenarvan/mary-grant/mcnabbs 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向）、其余承 R432 遗留清单。
4. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs、Bell ACH vs SC/TTLU 一次性同名）；（g）RFC-0003 4-char VVV 宽度。
5. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
6. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
7. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=369→370（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
