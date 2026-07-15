---
round: 52
date: 2026-07-15
type_round: 23
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - falkland-islands
  - sullivan-island
  - dream-bay
  - altamont-harbour
  - navy-island
result: accept
---

# GROW 2.1-B · R52 · NEW1 · place — R48 补种第三批 5 页（standard 档，续 R50 页内引注门）

## 本轮公告

**R52 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 3 候选 + 2 hold 升格**

R51 后 since_evv5=1、since_discover=3、queue(place)=15，决策矩阵高优先门全否，落 NEW1。
建 5 页：**南大西洋 1**（Falkland Islands，AM 主源 51）+ **Charleston 簇补 1**（Sullivan Island，BR）+
**GM 荒岛 1**（Dream Bay）+ **ACH 极北 1**（Altamont Harbour）+ **Niagara 簇补 1**（Navy Island，MW）。
Sullivan Island / Navy Island 自 R48 长尾 hold 列升格（严扫单源达门）。续执行 R50 页内引注门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=1 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=15, since_discover=3 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =19 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=15 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 段级 / 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|----------------------|---------------------------|------|
| falkland-islands | An Antarctic Mystery (AM)| RctcCf | 2146 | 段级 51 / 页内 8 | real / South Atlantic | accept |
| sullivan-island | The Blockade Runners (BR)| xUEngl | 2189 | 段级 7 / 页内 7 | real / United States (Charleston Harbor) | accept |
| dream-bay | Godfrey Morgan (GM)| Tm3Zut | 1851 | 段级 7 / 页内 6 | fictional / Pacific (Godfrey's island) | accept |
| altamont-harbour | The Adventures of Captain Hatteras (ACH)| 2Mh5fX | 1756 | 段级 6 / 页内 5 | fictional / Arctic (New America) | accept |
| navy-island | The Master of the World (MW)| woSiRJ | 1774 | 段级 6 / 页内 5 | real / United States (Niagara River) | accept |

> **续 R50 页内引注门**：五页建前逐页 grep sentence_index 校主源段级，成页后核页内 `(VVV-NNN-PPP)` 去重 ≥5——
> falkland 8、sullivan 7、dream-bay 6、altamont 5（贴门）、navy 5（贴门），全达门。falkland-islands 主源 AM:51 为本簇最强。

## 建前主源段级严扫 + hold

| 候选 | agg | 严扫实况 | 处置 |
|------|-----|---------|------|
| **Lake Ontario** | 7 | 主源 MW:4 <5；RC:2/PL:1（且「Ontario」含省名假匹配）| **hold**：真实大湖，跨源可凑但主源不达门，待净分 |
| **Black Sea** | 7 | 各源全 ≤2（ASC:2/RM/MS/SC/RC/TT 各 1），无叙事锚点 | **hold**：跨源过散，缺主叙事，暂不建 |

## 命名与互链

- **命名**：falkland-islands（alias Falkland Isles·The Falklands）/ sullivan-island / dream-bay / altamont-harbour / navy-island。
- **互链**：Falkland Islands ⇄ [[An Antarctic Mystery]] / [[Port Egmont]]（既有页，West Falkland 泊地）；
  Sullivan Island ⇄ [[The Blockade Runners]] / [[Morris Island]] / [[Fort Sumter]]（Charleston 三岛簇完整）；
  Dream Bay ⇄ [[Godfrey Morgan]] / [[Spencer Island]] / [[Flag Point]]（GM 荒岛簇）；
  Altamont Harbour ⇄ [[The Adventures of Captain Hatteras]] / [[Victoria Bay]]（New America 簇）；
  Navy Island ⇄ [[The Master of the World]] / [[Niagara River]] / [[Lake Erie]]（Niagara 簇）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{AM,BR,GM,ACH,MW}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN ≥5 逐页核：8/7/6/5/5 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 3 候选 + 2 hold 升格（15→12）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 52→53`；`type_round 23→24`；`rounds_since_last_evv5 1→2`；
`rounds_since_last_discover 3→4`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 19→20`；`last_updated_round→53`。

## 遗留问题

1. **place 页数 97→102**：本轮 +5，registry 全库 1165→1170。**place 破百**。
2. **queue(place) 12**：15 − R52 消费 3 = 12（Sullivan/Navy 自 hold 列升格，不占 bullet）。强候选渐少，
   余 Lake Ontario(cross)/Black Sea(散) hold；长尾 Detroit River/Goat Island/Niagara Falls/Platte River/North Sea 等 4–6 agg。
   下轮 R53 若 queue 仍 ≥10 且 since_discover<10 续 NEW1；预计数轮后 queue<10 触发 SCN28 补种或 since_corpus 达 30 触发深扫。
3. **两 hold 候选（本轮新增）**：Lake Ontario（主源 MW:4，跨源真实大湖，待净分升格）、Black Sea（跨源过散）。
4. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
5. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
