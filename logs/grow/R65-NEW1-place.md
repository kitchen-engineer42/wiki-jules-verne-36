---
round: 65
date: 2026-07-15
type_round: 36
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - lake-tinn
  - fort-independence
  - mount-mendif
  - lake-barnett
  - cape-saknussemm
result: accept
---

# GROW 2.1-B · R65 · NEW1 · place — 建 5 新页（standard 档）+ 修 niagara-falls alias 撞名

## 本轮公告

**R65 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 24→19**

R64 后 since_evv5=3、since_discover=5、discover_streak_low=0、queue(place)=24、since_corpus=1。
决策矩阵：since_evv5=3<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=24≥10 且 since_discover=5<10 → SCN28 不触发；since_corpus=1<30 → SCN28-corpus 不触发；落 NEW1。
消费 R63 深扫候选中单作达门最稳者，建 5 新页：**Lake Tinn**（TN Telemark 湖）+
**Fort Independence**（SC 阿根廷边堡）+ **Mount Mendif**（FWB Adamova 双锥峰）+
**Lake Barnett**（FC Victoria Island 命名湖）+ **Cape Saknussemm**（JCE 地心海岬）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=3 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=24≥10, since_discover=5 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =1 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=24 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| lake-tinn | Ticket No. 9672 (TN) | kqkdah | 8 | real / Norway (Telemark) | accept |
| fort-independence | In Search of the Castaways (SC) | znFNFg | 6 | real / Argentina (the Pampas) | accept |
| mount-mendif | Five Weeks in a Balloon (FWB) | BY4Oe1 | 5 | real / Africa (Kingdom of Adamova) | accept |
| lake-barnett | The Fur Country (FC) | upWZnL | 7 | fictional / Arctic (Victoria Island) | accept |
| cape-saknussemm | A Journey to the Center of the Earth (JCE) | slEuhw | 5 | fictional / The Central Sea (subterranean) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——8/6/5/7/5 全达门。
> **子串过配复核（承 R63/R64 教训）**：queue 候选 Lake Barnett（`Barnett` 单串 438 命中 = Mrs Barnett 人名）、
> Cape Saknussemm（`Saknussemm` 单串 41 命中 = 炼金术士人名）建前均以精确短语 `Lake Barnett`/`Cape Saknussemm`
> 重扫，得 7/5 distinctPN，确认达门。二者均为叙事内命名之地物，定 `real_or_fictional: fictional`。

## 副产：niagara-falls alias 撞名修复

R65 build_registry 报 alias 冲突：R64 建的 niagara-falls 携 alias「Niagara River」，与既有独立页
niagara-river（label「Niagara River」）撞名。Niagara Falls（瀑布）与 Niagara River（河）本为不同地物，
该 alias 系 R64 误加。经 edit_page.py 改 alias 为「Falls of Niagara」（真别名、不撞名），并顺带修
Overview 段 404→≤400（R64 add_page 散文门旁路遗留）。rev Pb3Z4f。修复后 registry 仅余既有 Robur alias
撞名（PARK 债），无新冲突。

## 命名与互链

- **命名**：lake-tinn（alias Tinn）/ fort-independence / mount-mendif / lake-barnett / cape-saknussemm。
- **互链**：Lake Tinn ⇄ [[Ticket No. 9672]]；Fort Independence ⇄ [[In Search of the Castaways]]；
  Mount Mendif ⇄ [[Five Weeks in a Balloon]]；Lake Barnett ⇄ [[The Fur Country]]；
  Cape Saknussemm ⇄ [[A Journey to the Center of the Earth]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{TN,SC,FWB,FC,JCE}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：8/6/5/7/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段；niagara-falls 修复段 404→≤400，全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含冒号/撇号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（24→19）+ niagara 撞名注；grow_state NEW1 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 65→66`；`type_round 36→37`；`rounds_since_last_evv5 3→4`；
`rounds_since_last_discover 5→6`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 1→2`；`last_updated_round→66`。

## 遗留问题

1. **place 页数 135→140**：本轮 +5，registry 全库 1203→1208。
2. **queue(place) 19**：24 − R65 消费 5 = 19（含 2 holds Lake Ontario/Black Sea + Kara Sea 待精扫）。
   余真候选含 Indian/Pacific/Atlantic Ocean、Gulf of Mexico、Coronation Gulf、Platte River、Caribbean Sea、
   Blue Ridge Mountains、Shannon Island、Ice Bank 及跨源候选 North Sea/Firth of Clyde/Long Island/Goat Island/
   Bay of Bengal/Cape Bon。
3. **Kara Sea 建前须精扫**：承 R63/R64，「kara」子串过配（58 vs 真 ~5），建前须精确重扫。
4. **下轮 R66：since_evv5=4、since_discover=6、queue=19≥10、since_corpus=2 → 仍落 NEW1**（建 5 页，消费 19→14）。
5. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break（R64 新增）、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路（R65 niagara 修复再证）、RFC-0003 VVV 宽度、Robur alias、
   build_wanted 空格滤、registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
