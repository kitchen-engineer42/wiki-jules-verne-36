---
round: 69
date: 2026-07-15
type_round: 40
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - irkutsk
  - kazounde
  - iquitos
  - stockholm
  - zanzibar
result: accept
---

# GROW 2.1-B · R69 · NEW1 · place — 建 5 新页（standard 档）

## 本轮公告

**R69 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 24→19**

R68 后 since_evv5=7、since_discover=0、discover_streak_low=0、queue(place)=24、since_corpus=5。
决策矩阵：since_evv5=7<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=24≥10 且 since_discover=0<10 → SCN28 不触发；since_corpus=5<30 → SCN28-corpus 不触发；落 NEW1。
建 5 新页（消费 R68 补种的单作强候选）：**Irkutsk**（MS 东西伯利亚首府）+ **Kazounde**（DSCF 安哥拉奴市镇）+
**Iquitos**（EHLA 亚马逊上游农庄村）+ **Stockholm**（WC 瑞典首都）+ **Zanzibar**（FWB 东非气球启程岛）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=7 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =7 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=24≥10, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =5 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=24 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| irkutsk | Michael Strogoff (MS) | nUAZ3e | 7 | real / Eastern Siberia (Russia) | accept |
| kazounde | Dick Sand: A Captain at Fifteen (DSCF) | 6auVN9 | 9 | real / Angola (Central Africa) | accept |
| iquitos | Eight Hundred Leagues on the Amazon (EHLA) | MrMXVb | 8 | real / Upper Amazon (Peru) | accept |
| stockholm | The Waif of the Cynthia (WC) | U4TIGR | 8 | real / Sweden | accept |
| zanzibar | Five Weeks in a Balloon (FWB) | qNvNiE | 9 | real / East African coast | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——7/9/8/8/9 全达门。
> **Kazounde real 裁定**：Verne 依 real Angola 内陆奴隶贸易地理设定（Coanza 河、Bihe/Cassange 市），
> region Angola（Central Africa），real。book 值含冒号，YAML 单引号转义（LAW §8）。
> **book 冒号转义**：kazounde `book: 'Dick Sand: A Captain at Fifteen'` 单引号包裹，防 frontmatter 丢弃。
> **散文门复核**：stockholm/zanzibar 首建段初超 400（429/434），建前逐段裁剪至 373/397，全 ≤400。

## 命名与互链

- **命名**：irkutsk / kazounde / iquitos / stockholm / zanzibar（均 real，无 alias 冲突）。
- **互链**：Irkutsk ⇄ [[Michael Strogoff]]；Kazounde ⇄ [[Dick Sand: A Captain at Fifteen]]；
  Iquitos ⇄ [[Eight Hundred Leagues on the Amazon]]；Stockholm ⇄ [[The Waif of the Cynthia]]；
  Zanzibar ⇄ [[Five Weeks in a Balloon]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MS,DSCF,EHLA,WC,FWB}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（max 373–397）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：7/9/8/8/9 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段（stockholm/zanzibar 裁剪后 373/397），全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；kazounde book 冒号单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（24→19）；grow_state NEW1 six-step；无新 alias 冲突 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 69→70`；`type_round 40→41`；`rounds_since_last_evv5 7→8`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 5→6`；`last_updated_round→70`。

## 遗留问题

1. **place 页数 150→155**：本轮 +5，registry 全库 1218→1223，unknown 0。
2. **queue(place) 19≥10**：24 − R69 消费 5 = 19（含 2 holds Lake Ontario/Black Sea + Kara Sea 待精扫
   + 6 跨源候选 + R68 补种余 10：Omsk/Tomsk/Manaos/Pekin/San Francisco/London/Christiania/Bergen/Buffalo/Mounts Doerfel）。
3. **下轮 R70**：queue=19≥10、since_evv5=8<10、since_discover=1<10、since_corpus=6<30 → NEW1 建 5 页。
   优先消费 R68 单作强候选 Omsk/Tomsk/Pekin/London/San Francisco 或跨源 North Sea 等。
4. **R71 EVV5 临近**：since_evv5=8，R70 后为 9，R71 后 =10 → R71 起优先级 1b EVV5 抢占（质量抽检轮）。
5. **alias 待核（建页时定）**：Manaos↔Manaus、Pekin↔Peking/Beijing、Christiania↔Oslo（label 从 Verne 原文旧称）。
6. **Kara Sea 建前须精扫**：承 R63–R68，「kara」子串过配（58 命中含非地名）。
7. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）。
8. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
9. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
