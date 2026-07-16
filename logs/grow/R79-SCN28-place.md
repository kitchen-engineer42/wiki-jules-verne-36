---
round: 79
date: 2026-07-15
type_round: 50
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 15
pages: []
result: discover
---

# GROW 2.1-B · R79 · SCN28 · place — 表层复扫补种（15 候选，非建页）

## 本轮公告

**R79 — Phase 2.1 — SCN28 — place — 0 建页 / 表层复扫 discover / 补种 15 候选 / queue 9→24**

R78（NEW1 建 5）后 since_evv5=6、since_discover=2、discover_streak_low=0、queue(place)=9、since_corpus=15。
决策矩阵：since_evv5=6<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
**queue=9<10 → 优先级 3 SCN28 触发**（抢占 NEW1），since_corpus=15<30 → 非 corpus 型。
本轮为表层复扫 discover：补种 place 候选入 queue，不建任何页；since_discover 归 0。

R76 补种 12 已 R77–R78 全数消费（余 Allahabad/Benares 二未建）。本轮续裸词城市扫描
并纳入**河/湖名精核**，补种 15 强候选（各词边界 distinctPN ≥8，均非既有页/人物）：
Amazon / Krasnoiarsk / Perm / Obi / Ekaterenburg / Yenisei / Volga / Omaha / Liverpool /
Suez / Auckland / Shanghai / Singapore / Ega / Zabediero。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=6 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =15 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=9 | 否 |
| RCH2（stub% ≥ 20%）| —（未评估，SCN28 先占）| 否 |
| NEW1（默认）| —（被优先级 3 抢占）| 否 |

## 复扫方法与候选核验

复扫 `data/sentence_index/*.jsonl`：裸词专名扫描（人名/代词 stoplist 滤）+ 河/湖名定向精核，
逐候选精核**词边界**（`\bName\b`）distinctPN（段级 PN = sid 前三段），比对 pages.json
label/alias/id 排除既有页，逐句抽样确认为地名非人物。保留单作 distinctPN ≥8 的真地点。

| 候选 | 单作 distinctPN（top） | region / real | 排除污染核验 |
|------|----------------------|---------------|--------------|
| Amazon | EHLA:179 | 南美亚马逊河 / real | 河名；「near the Amazon; no other river」EHLA 主航道 |
| Krasnoiarsk | MS:38 | 东西伯利亚 / real | 专名；「mine only as far as Krasnoiarsk」Blount 电报终点 |
| Perm | MS:28 | 乌拉尔（俄）/ real | 专名；Tsar 电报站清单「Nijni-Novgorod, Perm, Ekaterenburg」 |
| Obi | MS:24 | 西伯利亚鄂毕河 / real | 河名；MS 渡河点（词边界，非 Obi 人名） |
| Ekaterenburg | MS:22 | 乌拉尔 / real | 专名；电报站清单/Ural 东坡城 |
| Yenisei | MS:21 | 东西伯利亚叶尼塞河 / real | 河名；Krasnoiarsk 城下渡河 |
| Volga | MS:21 | 俄伏尔加河 / real | 河名；「junction of the Volga and the Oka」Nijni 河汊 |
| Omaha | AWED:20 | 美内布拉斯加 / real | 专名；「On leaving Omaha... Platte River」太平洋铁路东端 |
| Liverpool | AWED:25 | 英格兰 / real | 专名；Fogg 大西洋归国登陆港 |
| Suez | AWED:22 | 埃及 / real | 专名；Mongolia「between Brindisi and Bombay via the Suez Canal」/Fix 候船 |
| Auckland | SC:31 | 新西兰 / real | 专名；「follow the coast to Auckland」北岛目标港 |
| Shanghai | AWED:11 | 中国 / real | 专名；「pilot-boat came in sight of Shanghai」 |
| Singapore | AWED:10 | 新加坡 / real | 专名；「Bombay, Calcutta, and Singapore」中转港 |
| Ega | EHLA:14 | 巴西亚马逊镇 / real | 专名；「desire to visit Ega」jangada 停靠 |
| Zabediero | MS:11 | 西伯利亚村 / real | 专名；「little village of Zabediero」8/15 convoy 抵达 |

> **既有页去重**：15 候选逐一比对 pages.json label/alias/id，**均 new**。
> **剔除项**：**Baikal**（`lake-baikal` 已建 → 剔）；**Coimbra**（DSCF「son of Major Coimbra of Bihe」实为奴商
> 人名，非葡萄牙城 → 剔）；**Zealand**（「New Zealand」子串伪匹配 → 剔）；Adelaide/Sydney（SC<8）、Madras/Aden（AWED<8）、
> Sacramento/Ogden（<8）、Aral（ASC:3）均 <门剔除。
> **河/湖名首度纳入**：本轮起 place 扫描扩及大河（Amazon/Volga/Obi/Yenisei）——Verne 地理骨架的自然地物，
> distinctPN 高且接地稳固，补 place 类型广度盲区。

## PN 接地核验

本轮不建页，无正文 PN 落地。候选 distinctPN 仅为 queue 强度参考，来自 `data/sentence_index/`
词边界精核；建页轮（R80+）消费时须再逐句复核页内引注 ≥5。

## EXIT-GATE 检查（discover 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 补种 15 候选（9→24）；grow_state SCN28 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 discover six-step）

`current_round 79→80`；`type_round 50→51`；`rounds_since_last_evv5 6→7`；
`rounds_since_last_discover 2→0`（discover 轮，RESET）；
`discover_streak_low` 保持 0（new_candidates=15≥3，不自增）；
`rounds_since_last_corpus_discover 15→16`；`last_updated_round→80`。

## 遗留问题

1. **queue(place) 9→24**：补种 15 强候选后 discover 门解除；R80 起 since_discover=0，
   优先级 3 不再触发，回落 NEW1 建页。
2. **下轮 R80 = NEW1**：queue=24≥10、since_evv5=7<10、since_discover=0<10、since_corpus=16<30
   → 优先级 6 NEW1 建 5 页。优先消费头部 MS 河/城群（Krasnoiarsk/Perm/Obi/Ekaterenburg/Yenisei）
   或大河（Amazon/Volga）。
3. **EVV5 将于 R82 触发**（since_evv5 R79 后=7，R82 达 10）。届时 since_discover 或已 <10
   → 优先级 1b 单 EVV5（非 EVV5+SCN28）。
4. **place runway 充足**：河/湖名纳入后候选池再度扩容；后续尚有印度次城（Allahabad/Benares 在队）、
   美西铁路镇（Ogden/Sacramento 待复核）、南美港（Callao/Valparaiso 待精核）。
5. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
