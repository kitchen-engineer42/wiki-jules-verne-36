---
round: 418
date: 2026-07-19
type_round: 110
phase: "2.1"
current_type: character
gene: NEW1
pages: [joliffe]
result: success
---

# GROW 2.1-B · R418 · NEW1 · character — 建 Corporal Joliffe（The Fur Country 之 Fort Hope 下士司务、忙碌好脾气而怕内的军曹，救活半冻僵的天文学家；消费第十九批建序 133，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 83 建（type_round 110），消费 R417 第十九批 discover 队列**建序 133（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2（建序 134-135 rae/martha）。**

**Corporal Joliffe**（*The Fur Country*）——Fort Hope 之下士司务、忙碌好脾气而怕内的军曹。司务改屋「the large room on the ground-floor was completely transformed」（FC-001-003），人见人爱「asked Joliffe, who had a gracious word for every body」（FC-001-022）。救活半冻僵的天文学家「Corporal Joliffe could think of no better means to restore the lost vital heat than to give him a bath in the bowl of hot punch」（FC-003-028），复以美酒暖其内腑（FC-003-036）。官长离堡则代守「the command of the fort fell to Corporal Joliffe, or rather to his little wife」（FC-026-010），归时其声相迎「the shouts of Corporal Joliffe welcomed their return to the factory」（FC-027-054）。终日忙碌以娱众（FC-030-002），甚且充婴儿之乳保姆「a kind of foster-father or nurse to the baby」（FC-034-030）。怕内而不认「Corporal Joliffe obeyed his wife without owning it」（FC-001-026），嗜猎鹿「with the greatest satisfaction that there were plenty of these ruminants on this coast」（FC-011-017），驯鹿乃其所偏爱之猎物（FC-011-015）。忧薪「the Company promised us double pay」（FC-024-014），复自剖「it isn't that we think much about money, but that the money sticks to us」（FC-024-017）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-001、affiliation 空、**label=Corporal Joliffe，aliases=['Joliffe']**。

**15 distinct solid PN**（FC-001-003/022/026、003-007/028/036、011-015/017、024-010/014/017、026-010、027-054、030-002、034-030）：均 solid，逾门。「Joliffe」FC 内区分 Corporal Joliffe（本人）与 Mrs Joliffe（其妻）——正文引注均取 Corporal 语境，Mrs Joliffe 以行内文字（FC-024-010）呈现，无消歧冲突。

**查重**：exact-slug joliffe filesystem test -f ABSENT（bucket jo）+ registry entity/label/alias 复验——「Corporal Joliffe / joliffe」无既建人物页，无冲突。

**FC 2-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Jaspar Hobson]]（lieutenant-hobson，既建，FC-003-007）、[[Thomas Black]]（thomas-black，既建，FC-003-028）、[[The Fur Country]]（work，存，FC-027-054）——三链均无悬挂。**Mrs Joliffe 页未建**：正文以 PN-grounded 行内文字呈现（FC-024-010），未设悬挂链。**FC 簇再拓**（joliffe 补入 lieutenant-hobson/mac-nab/sabine/marbre，FC 簇继续收束）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 97→**98**，registry total 1621→**1622**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 133。消费后 queue=2 → R419 继续 NEW1（建序 134 rae）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| joliffe | 84o8mG | The Fur Country | supporting | FC-001 | 15 distinct | 司务改屋-人见人爱-救活天文学家-代守孤堡-归声相迎-终日忙碌-充婴保姆-怕内不认-嗜猎驯鹿-忧薪自剖；label Corporal Joliffe / alias Joliffe；FC 2-char 无 Note；0 超段直建；strict 首验通过；三链 [[Jaspar Hobson]]/[[Thomas Black]]/[[The Fur Country]]；Mrs Joliffe 行内文字（FC-024-010）|

- **joliffe**：15 distinct solid PN；aliases ['Joliffe']；character-schema 五 H2。add_page rev 84o8mG（size 2577）。quality featured 回填。pn_validator --mode strict ✓。**FC 簇再拓；Corporal/Mrs Joliffe 语境区分无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Corporal Joliffe 司务-救人-代守-怕内-嗜猎因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：15 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1622 character 98 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Jaspar Hobson + Thomas Black + The Fur Country 三链存在无悬挂；Mrs Joliffe 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R419 起始计数）

| 字段 | R418 起始 | R419 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 418 | 419 |
| type_round | 110 | 111 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 354 | 355 |
| last_updated_round | 418 | 419 |

## 遗留问题

1. **character 页数 98**：本轮 +1（joliffe）。queue(character) 3→**2**（建序 133 消费）。registry 全库 **1622**，unknown 0。
2. **下轮 R419 = NEW1（§3(7)）**：since_evv5=3<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 134 **rae**（FC 铁匠/营建匠人，30 mentions，首现 FC-001；FC-035-005 与 mac-nab 并列受 marbre 告知浮岛之危）。
3. **第十九批消费进度**：R418 NEW1（133 joliffe ✓）→ R419 NEW1（134 rae 待）→ R420 NEW1（135 martha 待）→ queue 归 0 → R421 SCN28-zombie 补第二十批。**EVV5 时点**：since_evv5 R419 起始=3 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**FC 簇本轮再拓**（joliffe→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe 待建）；rae 待建、martha 待建、JCE 簇（martha→professor-lidenbrock/axel/grauben 反向、grauben/saknussemm/fridrikssen 反向链）、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=354→355（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
