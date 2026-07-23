---
round: 465
date: 2026-07-23
type_round: 157
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R465 · SCN28-zombie · character — 第三十批 discover：转深耕高频缺员（manoel-valdez/sylvius-hogg/procope），queue 0→3

## 执行摘要

Phase 2.1-B character discover 轮（type_round 157）。决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=5<10；SCN28 周期 since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十九批（建序 163-165）R462-R464 全数消费（john-strock/mr-ward/fritz-napoleon-smith，MW/YEAR 两新作皆开），queue 归 0，本轮触发 zombie discover。

**簇策转向**：flagship work 广度趋饱和（31/33 work 页已覆盖；余 A Drama in the Air / Round the Moon / The Ascent of Mont Blanc 皆薄 cast 或核心角既建）。本批据**全库 sentence_index proper-noun 频次扫描**（honorific+Name + 中句大写重复词，减 registry labels/aliases）取三部**已建簇之高频缺员**深耕：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 166 | manoel-valdez | Eight Hundred Leagues on the Amazon | EHLA | EHLA-002 | supporting | 343/15 | ABSENT | EHLA 深耕 接 joam/benito/torres |
| 167 | sylvius-hogg | Ticket No. 9672 | TN | TN-009 | supporting | 149/50 | ABSENT | TN 深耕 接 hulda/ole-kamp |
| 168 | procope | Off on a Comet | OC | OC-011 | supporting | 79/45 | ABSENT | OC 深耕 接 isaac-hakkabut |

**候选说明**：
- **manoel-valdez**（EHLA）——巴西军队助理军医、Minha（Joam Garral 之女）之未婚夫，随 jangada 顺 Amazon 而下；343 mentions（Manoel）/15（Manoel Valdez），首现 EHLA-002-074「My friend, Manoel, assistant surgeon, Brazilian army」。接 joam-garral/benito-garral/torres。
- **sylvius-hogg**（TN）——挪威 Storthing 议员/教授、Hulda 一家之恩人，力查彩票 9672 之下落与 Ole 生死；149 mentions（Sylvius Hogg）/50（Sylvius），首现 TN-009-001。接 hulda/ole-kamp。
- **procope**（OC）——Dobryna 号指挥官、Count Timascheff 所倚之航海家，测绘彗星掠地后之新海岸；79 mentions（Lieutenant Procope）/45（Procope），首现 OC-011-001。接 isaac-hakkabut（Servadac/Timascheff 待后批）。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT。mentions 全 ≥79，distinct-PN 充裕支撑 ≥16 solid PN。**排除（registry-catch，扫描既建高频）**：fix/joe/dick-kennedy/hans/nadia/ivan-ogareff/harry-blount/alcide-jolivet/thomas-black 皆既建（flagship 次要角已覆盖）；Dolphin/Ebba（船）、Dingo（犬）、Chinese/Russian/Siberian（族称）等非人名剔除。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| since_evv5=5 | 否 |
| 2 | CLOSE（streak_low≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 166-168）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：discover 轮，仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、无冲突。✔
- **grounding**：mentions 343/149/79，distinct-PN 充裕支撑 ≥16 solid PN。✔
- **数据驱动**：全库 proper-noun 频次扫描定候选，非人名（船/犬/族称）已剔除，既建高频角已排除。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R466 起始计数）

| 字段 | R465 起始 | R466 起始 |
|------|----------|----------|
| current_round | 465 | 466 |
| type_round | 157 | 158 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 401 | 402 |
| last_updated_round | 465 | 466 |

## 遗留问题

1. **character 130**：本轮无建页（discover 轮）。queue(character) 0→**3**（第三十批建序 166-168）。registry **1654**，featured 35（5.1%），覆盖 31 部。
2. **下轮 R466 = NEW1（§3(7)）**：queue=3>0 且 since_discover=0<10 → NEW1，消费建序 166 **manoel-valdez**（EHLA Minha 未婚夫/军医，supporting，343 mentions；深耕 EHLA 接 joam/benito/torres）。
3. **深耕计划**：R466（166 manoel-valdez）→ R467（167 sylvius-hogg）→ R468（168 procope）→ queue 归 0 → **R469 = EVV5**（since_evv5 于 R469 起始达 10）→ R470 SCN28-zombie 补第三十一批。
4. **广度趋饱和信号**：flagship 次要角多已覆盖，后续 discover 将更依赖二/三线缺员深耕；若连续 discover 产出 <3（discover_streak_low 累加至 3）→ 触发 §3(2) CLOSE → character 类型收口 → 迈向 Phase 3。本批仍足 3，未触发。
5. **目标**：grow 至 Phase 10。Phase 2.1-B 广度扩张持续，R465/~500。
6. **PN 渲染 / Martin Paz alias / HK / Pilot 债 / event PN 债 / 回链**：DEFERRED。
7. **corpus-discover 顺延**：since_corpus=401→402。
