---
round: 63
date: 2026-07-15
type_round: 35
phase: "2.1"
current_type: place
gene: SCN28-corpus
new_candidates: 18
pages: []
result: discover
---

# GROW 2.1-B · R63 · SCN28-corpus · place — 首次深层语料扫描（跨全 36 部聚合）

## 本轮公告

**R63 — Phase 2.1 — SCN28-corpus — place — 0 建页 / 跨源聚合深扫 / +18 候选 / queue 11→29 / since_corpus 归 0**

R62 后 since_evv5=1、since_discover=3、discover_streak_low=0、queue(place)=11、since_corpus=30。
决策矩阵：since_evv5=1<10 → EVV5 系不触发；queue=11≥10 且 since_discover=3<10 → SCN28（表层）不触发；
**since_corpus=30≥30 → 优先级 3.5 SCN28-corpus 触发**（自建 wiki 以来首次深层语料扫描）。

SCN28-corpus 为跨全 36 部语料的聚合深扫（非建页），专为捕获**单作 <5、跨作聚合 ≥5** 的地点——
即 R59 表层扫（单作视角）系统性遗漏的一类（cape-horn/rocky-mountains 先例）。产候选入 queue，since_corpus 归 0。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=1 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=11≥10, since_discover=3 | 否 |
| **3.5** | **SCN28-corpus（since_corpus ≥ 30）** | **=30** | **触发** |
| 3.9 | zombie-guard（queue(place)==0）| queue=11 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| NEW1（默认）| — | 被 3.5 抢占 | 否 |

## 扫描方法

全集 `data/sentence_index/*.jsonl`（36 部）正则抽取 toponym 构式，按 sid 前三段跨作聚合 distinctPN：

1. **后缀构式**：`(Cap ){1,3}(Ocean|Sea|Bay|Gulf|Island(s)|Isle(s)|River|Strait(s)|Cape|Lake|Mountains|Mount|Peak|Point|Land|Desert|Peninsula|Channel|Sound|Bank|Reef|Rock(s)|Falls|Cove|Harbour|Inlet|Firth|Archipelago)`
2. **「GEO of X」构式**：`(Suffix) of (Cap){1,3}`（Strait of Magellan、Bay of Bengal 类）
3. **「前缀 X」构式**：`(Cape|Mount|Lake|Fort|Port|Gulf) (Cap){1,2}`

排除已建（179 名含 alias）+ 已在 queue（11 名）。聚合 ≥5 且未收录者列为候选。

## 候选产出（18 新增）

### 单作达门（maxsingle ≥5，最稳）

| 候选 | 源作聚合 | agg | 单作 max | real/fictional | 备注 |
|------|---------|-----|---------|----------------|------|
| Strait of Magellan | SC:7/TTLU:4/AM:4/RC:3/+ | 23 | 7 | real | alias Straits of Magellan |
| Niagara Falls | MW:22/RC:5/+ | 38 | 22 | real | MW 决战场景 |
| Lake Tanganyika | DSCF:10/EHLA:1 | 11 | 10 | real | Dick Sand 非洲内陆 |
| Peak of Teneriffe | SC:6/RM:1/TTLU:1 | 8 | 6 | real | alias Teneriffe/Tenerife |
| Norfolk Island | SI:5/MI:4/SC:2 | 11 | 5 | real | — |
| Lake Barnett | FC:7 | 7 | 7 | 待核 | Fur Country 北极 |
| Lake Tinn | TN:6 | 6 | 6 | real | 挪威 |
| Fort Independence | SC:6 | 6 | 6 | real/settlement | In Search of Castaways |
| Mount Mendif | FWB:5 | 5 | 5 | 待核 | Five Weeks in a Balloon 非洲峰 |
| Cape Saknussemm | JCE:5 | 5 | 5 | fictional | Journey to Centre of Earth |
| Ice Bank | TTLU:30/WC:2 | 32 | 30 | 待核 | TTLU 南极冰障；feature/place 待裁 |

### 跨源达门（单作 <5，聚合 ≥5，须单一无歧义真实地点）

| 候选 | 源作聚合 | agg | 单作 max | 备注 |
|------|---------|-----|---------|------|
| North Sea | TTLU:2/RC:2/+7 作 | 9 | 2 | real；跨源建页 |
| Firth of Clyde | SC:4/UC:2 | 6 | 4 | real 苏格兰 |
| Long Island | TTLU:3/ASC:2/AWED:1 | 6 | 3 | real |
| Goat Island | MW:4/RC:2 | 6 | 4 | real 尼亚加拉 |
| Bay of Bengal | TTLU:3/RM:1/AWED:1 | 5 | 3 | real |
| Cape Bon | OC:3/RC:1/TTLU:1 | 5 | 3 | real 突尼斯 |

### 存疑（须建页前精核）

- **Kara Sea**：原「Sea of Kara」构式 agg 5（MS/WC）。但 `kara` 子串扫描过宽（含非地名命中，虚计 58）。
  记候选，建页前须以精确边界重扫。

## 排除与别名合并

- **人物误配**：Ned Land（"Land" 后缀误配 256 distinctPN）——人物非地点，排除。
- **截断/机构**：Lake City（Salt Lake City 截断）、Bank of England（金融机构/建筑）、Northern Ocean（Arctic 别名）——排除。
- **既有 hold 照旧**：Black Rock（待与 black-rock-creek 消歧）、Long's Peak（rocky-mountains 子地点）。
- **Cape Mandible**：MI:4（agg 5 含 SI:1 疑误配——虚构地点不应跨作）→ 单作 4<门，hold。
- **别名合并（非新建，留待 build 后页编辑）**：
  Behring's Straits/Strait → behring-strait alias；The Torres Strait → torres-strait alias；
  Lancaster Sound → lancaster-strait alias；Antarctic Ocean → antarctic-sea alias；
  Arctic Ocean → polar-sea alias（承 R59）；Blueridge Mountains → 既 Blue Ridge Mountains alias；
  Isle of Paques → 既 easter-island alias。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md +18 候选（11→29）；grow_state SCN28-corpus six-step |

> SCN28-corpus 为深扫轮（不建页），仅 G4 出口门。跨源聚合候选建页时须逐页复核页内引注 ≥5。

## 结论

**语料远未穷尽**。首次跨源深扫即产 18 新候选（new_candidates=18 ≥ corpus_new_candidate_min=3）→
corpus_discover_streak_low 保持 0，`corpus_exhausted` 保持 false。
深扫验证了 R59 结论方向（表层扫低估）：跨作聚合层另有一整类被系统遗漏的地点。
place 稳固 OPEN，广度扩张续行。

## state 更新（SCN28-corpus six-step）

`current_round 63→64`；`type_round 34→35`；`rounds_since_last_evv5 1→2`；
`rounds_since_last_discover 3→4`（表层 discover 机制独立，corpus 深扫不重置表层计数）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 30→0`（本轮归零）；`corpus_discover_streak_low` 保持 0（new_candidates≥3）；
`last_updated_round→64`。

## 遗留问题

1. **queue(place) 29**：11 + R63 深扫 18 = 29（27 真候选 + 2 holds）。含单作达门 11 + 跨源达门 6 + 存疑 1（Kara Sea）。
2. **下轮 R64：since_evv5=2、since_discover=4、queue=29≥10、since_corpus=0 → 优先级落 NEW1**（建 5 页，消费 queue 29→24）。
   优先建单作达门最稳者（Niagara Falls MW:22、Strait of Magellan SC:7、Lake Tanganyika DSCF:10、
   Peak of Teneriffe SC:6、Norfolk Island SI:5），暂缓跨源薄弱与存疑候选。
3. **别名合并债务**：7 组别名（Behring/Torres/Lancaster/Antarctic Ocean/Arctic Ocean/Blueridge/Isle of Paques）
   留待 build 后统一页编辑（edit_page.py 补 alias），非新建。
4. **Kara Sea 扫描过宽**：记 discover-pattern 精度债务（`kara` 子串误配）；建页前精核，入 housekeeping 佐证宽/窄式两难。
5. **Ice Bank feature/place 归类**：TTLU 南极冰障，agg 32 极强但属地理特征；建页时裁定 place vs 场景。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **discover 双盲区债务**（HK-surface-discover-pattern-undercount，R59 升格实质缺陷；R63 深扫再证跨作盲区）：build 后提 RFC。
8. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报（R63 实操印证）** 七项债务照旧 PARK/记录。
