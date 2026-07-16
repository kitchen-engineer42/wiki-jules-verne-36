---
round: 64
date: 2026-07-15
type_round: 35
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - niagara-falls
  - strait-of-magellan
  - peak-of-teneriffe
  - norfolk-island
result: accept
---

# GROW 2.1-B · R64 · NEW1 · place — 建 4 新页 + 修 2 type=unknown 破损页（standard 档）

## 本轮公告

**R64 — Phase 2.1 — NEW1 — place — 4 建页 + 2 修复 / standard 档 / 消费 5 候选 / queue 29→24**

R63 后 since_evv5=2、since_discover=4、discover_streak_low=0、queue(place)=29、since_corpus=0。
决策矩阵：since_evv5=2<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=29≥10 且 since_discover=4<10 → SCN28 不触发；since_corpus=0<30 → SCN28-corpus 不触发；落 NEW1。
消费 R63 深扫候选中单作达门最稳者，建 4 新页：**Niagara Falls**（MW Terror 尼亚加拉逃逸）+
**Strait of Magellan**（SC Duncan 麦哲伦海峡穿行）+ **Peak of Teneriffe**（SC 特内里费峰）+
**Norfolk Island**（SI 诺福克流放岛）。副产修复 2 页破损（见下）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=2 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=29≥10, since_discover=4 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =0 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=29 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| niagara-falls | The Master of the World (MW) | NE9f0z | 5 | real / United States (Great Lakes) | accept |
| strait-of-magellan | In Search of the Castaways (SC) | NMNXPh | 6 | real / South America | accept |
| peak-of-teneriffe | In Search of the Castaways (SC) | RhvWbP | 5 | real / Canary Islands (Atlantic) | accept |
| norfolk-island | The Mysterious Island (SI) | HwTN6f | 5 | real / South Pacific | accept |

> **续 R50 页内引注门**：四新页页内 `(VVV-NNN-PPP)` 去重 ≥5——5/6/5/5 全达门。

## 副产：LAW §8 破损页修复（type=unknown → place）

R64 建 lake-tanganyika 时 add_page.py 报 "already exists"——该页 R47 已建。核查发现其
`book: Dick Sand: A Captain at Fifteen` 裸值未加引号，第二个冒号破坏 YAML → 整块 frontmatter 丢弃
→ registry 记为 `type: unknown`。全库扫描发现同 bug 另一页 easter-island（R60 本对话早期我所建，
EXIT-GATE 当时给 description 加了引号却漏了 book 字段的冒号）。二者为全库仅有的 type=unknown 页。

| slug | 原建轮 | 修复 rev | distinctPN | 修复动作 |
|------|--------|----------|------------|---------|
| lake-tanganyika | R47 | Kym3I6 | 6 | book 字段单引号包裹 |
| easter-island | R60 | BNLbKc | 8 | book 单引号 + 拆分 3 处 >400 散文段（493/552/551→≤400）|

> **easter-island 散文门**：R60 经 add_page.py 建（散文门旁路），3 处正文段超 400 潜伏至 R64
> edit_page.py 触碰才暴露。按句边界拆分，8 处 PN（DSCF-012-083/012-093/012-086/012-096/013-047/
> 014-005/018-107/020-062）全保留。修复后全库 type=unknown 归 0。
> **discover 连带缺陷**：R63 深扫既有页快照按 `type=='place'` 过滤，type=unknown 页不可见 →
> lake-tanganyika 被误当新候选重列。已记 housekeeping HK-book-colon-yaml-break。

## 命名与互链

- **命名**：niagara-falls（alias Niagara River）/ strait-of-magellan（alias Straits of Magellan）/
  peak-of-teneriffe（alias Teneriffe, Tenerife）/ norfolk-island。
- **互链**：Niagara Falls ⇄ [[The Master of the World]] / [[The Terror]] / [[Lake Erie]]；
  Strait of Magellan ⇄ [[In Search of the Castaways]] / [[Duncan]] / [[Patagonia]]；
  Peak of Teneriffe ⇄ [[In Search of the Castaways]]；
  Norfolk Island ⇄ [[The Mysterious Island]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MW,SC,SI}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
四新页 add 前分段核验通过；二修复页经 edit_page.py 防缩减 + 散文门全 PASS。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：新页 5/6/5/5，修复页 6/8 |
| G2 散文门 ≤400 | PASS | 四新页 add 前分段；easter-island 修复时拆 3 超长段，全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含冒号 book 值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（29→24）；housekeeping 新增 HK-book-colon-yaml-break；grow_state NEW1 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 64→65`；`type_round 35→36`；`rounds_since_last_evv5 2→3`；
`rounds_since_last_discover 4→5`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 0→1`；`last_updated_round→65`。

## 遗留问题

1. **place 页数 129→135**：本轮 +4 新建 + 2 type 修复回归（lake-tanganyika/easter-island），registry 全库 1203。
2. **queue(place) 24**：29 − R64 消费 5 = 24。余含 R63 深扫候选（Lake Tinn、Fort Independence、
   Mount Mendif、Cape Saknussemm[虚构]、Firth of Clyde、Long Island、Goat Island、Bay of Bengal、
   Cape Bon、North Sea 等）+ 早期余候选（Indian/Pacific/Atlantic Ocean、Gulf of Mexico 等）。
3. **Kara Sea 建前须精扫**：R63 "kara" 子串过配（58 vs 真 ~5），建前须精确重扫 distinctPN。
4. **下轮 R65：since_evv5=3、since_discover=5、queue=24≥10、since_corpus=1 → 仍落 NEW1**（建 5 页，消费 queue 24→19）。
   择单作达门最稳者续建。
5. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break（本轮新增）、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
