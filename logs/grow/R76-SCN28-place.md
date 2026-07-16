---
round: 76
date: 2026-07-15
type_round: 47
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 12
pages: []
result: discover
---

# GROW 2.1-B · R76 · SCN28 · place — 表层复扫补种（12 候选，非建页）

## 本轮公告

**R76 — Phase 2.1 — SCN28 — place — 0 建页 / 表层复扫 discover / 补种 12 候选 / queue 7→19**

R75（NEW1 建 5）后 since_evv5=3、since_discover=2、discover_streak_low=0、queue(place)=7、since_corpus=12。
决策矩阵：since_evv5=3<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
**queue=7<10 → 优先级 3 SCN28 触发**（抢占 NEW1），since_corpus=12<30 → 非 corpus 型。
本轮为表层复扫 discover：补种 place 候选入 queue，不建任何页；since_discover 归 0。

R73 补种 8 已 R74–R75 全数消费。本轮改用**裸词城市扫描**（人名 stoplist 滤除）——
此前几轮偏重地理后缀 toponym（Sea/Cape/Island/Firth 等），已近枯竭（本轮后缀扫描仅回 4 个既有页别名）；
但裸词城市扫描揭示大批未建**主要城市**仍在库中：补种 12 强候选（各精核词边界 distinctPN ≥8）：
Nijni-Novgorod / Bombay / Melbourne / Lima / Gibraltar / Morganton / Tijuco / Kilimanjaro /
Tsalal / Calcutta / Allahabad / Benares。**place 远未枯竭**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=3 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=7<10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =12 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=7 | 否 |
| RCH2（stub% ≥ 20%）| —（未评估，SCN28 先占）| 否 |
| NEW1（默认）| —（被优先级 3 抢占）| 否 |

## 复扫方法与候选核验

本轮双路复扫 `data/sentence_index/*.jsonl`：
1. **地理后缀 toponym 扫描**（Sea/Cape/Island/Firth/Bay/Gulf/Strait…）——仅回 4 个既有页别名
   （Arctic Ocean→polar-sea、Isle of Paques→easter-island、Cape of Good Hope→built、Torres Strait→built），
   **后缀型近枯竭**。
2. **裸词城市/地名扫描 + 人名 stoplist 滤**——回 321 raw 候选（单作 distinctPN ≥6），去噪后
   逐候选精核**词边界**（`\bName\b`）distinctPN（段级 PN = sid 前三段 `VVV-NNN-PPP`），
   比对 pages.json label/alias/id 排除既有页，逐句抽样确认为地名非人物。保留 12 强候选：

| 候选 | 单作 distinctPN（top） | region / real | 排除污染核验 |
|------|----------------------|---------------|--------------|
| Nijni-Novgorod | MS:47 / ASC:1 | 俄罗斯下诺夫哥罗德 / real | 专名；「the Tsiganes of Nijni-Novgorod」Michael 启程集市城 |
| Bombay | AWED:50 / SC:2 / DSCF:1 | 印度孟买 / real | 词边界；「not unlike Bombay, Calcutta, and Singapore」Fogg 印度登陆港 |
| Melbourne | SC:51 / DSCF:5 / MI:4 | 澳大利亚墨尔本 / real | 专名；「get it repaired nearer than Melbourne」SC 澳洲段主港 |
| Lima | PL:36 / DSCF:2 / GM:1 | 秘鲁利马 / real | 专名；「its death-blow at Lima」PL 舞台城 |
| Gibraltar | OC:38 / TTLU:9 / WC:7 | 直布罗陀 / real | 专名；OC 彗星掠地距测基点 |
| Morganton | MW:36 | 美国北卡罗来纳 / real | 专名；「the letter I had received from Morganton」Great Eyrie 山脚镇 |
| Tijuco | EHLA:39 | 巴西蒂茹科 / real | 专名；EHLA Joam Garral 早年城 |
| Kilimanjaro | TT:34 | 东非乞力马扎罗 / real | 专名；TT（Five Weeks）气球飞越东非高峰 |
| Tsalal | AM:90 | 南极察拉尔岛 / **fictional** | 专名；「before we should have reached Tsalal Island」AM（Poe 续篇）虚构岛 |
| Calcutta | AWED:28 / TTLU:5 / SC:4 | 印度加尔各答 / real | 词边界；Fogg 印度铁路东终点，与 Bombay 并列 |
| Allahabad | AWED:14 | 印度阿拉哈巴德 / real | 专名；「between Rothal and Allahabad」铁路中断处 |
| Benares | AWED:8 / FEM:1 | 印度贝拿勒斯 / real | 专名；Fogg 恒河圣城铁路站 |

> **既有页去重**：12 候选逐一比对 pages.json label/alias/id，**均 new**（无 HK-discover-existing-type-blindspot 命中）。
> **place 未枯竭结论**：R75 遗留问题曾预警「单作强候选渐稀」——本轮裸词扫描**证伪**：主要城市
> （Bombay/Melbourne/Lima/Gibraltar/Nijni-Novgorod 等 distinctPN 36–51）大量未建，后续 NEW1 建页
> runway 充足。此前偏重地理后缀 toponym 造成的枯竭错觉，实为扫描模式盲区（HK-surface-discover-pattern-undercount）。
> **Tsalal 为 fictional**：AM（An Antarctic Mystery，Poe《Pym》续篇）虚构南极岛；建页时 real_or_fictional=fictional。
> **noise/碎片剔除**（不入 queue）：Nagasaki（AWED:4<门）、人名假匹配（stoplist 已滤）、孤词。

## PN 接地核验

本轮不建页，无正文 PN 落地。候选 distinctPN 仅为 queue 强度参考，来自 `data/sentence_index/`
词边界精核；建页轮（R77+）消费时须再逐句复核页内引注 ≥5。

## EXIT-GATE 检查（discover 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；queue.md 补种 12 候选（7→19）；grow_state SCN28 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（SCN28 discover six-step）

`current_round 76→77`；`type_round 47→48`；`rounds_since_last_evv5 3→4`；
`rounds_since_last_discover 2→0`（discover 轮，RESET）；
`discover_streak_low` 保持 0（new_candidates=12≥3，不自增）；
`rounds_since_last_corpus_discover 12→13`；`last_updated_round→77`。

## 遗留问题

1. **queue(place) 7→19**：补种 12 强候选后 discover 门解除；R77 起 since_discover=0，
   优先级 3 不再触发，回落 NEW1 建页。
2. **下轮 R77 = NEW1**：queue=19≥10、since_evv5=4<10、since_discover=0<10、since_corpus=13<30
   → 优先级 6 NEW1 建 5 页（standard 档），消费 queue 头部候选（优先单作强 Nijni-Novgorod/
   Bombay/Melbourne/Lima/Gibraltar）。
3. **place 未枯竭（R75 预警证伪）**：主要城市 distinctPN 36–51 大批未建；后续多轮 NEW1 runway 充足。
   剩余待扫：印度次城（AWED）、俄/西伯利亚镇（MS）、南美城（EHLA/DSCF）、澳洲镇（SC）。
4. **EVV5 将于 R82 触发**（since_evv5 每轮 +1，R76 后=4，R82 达 10）。
5. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount（本轮再度验证：
   后缀盲区致枯竭错觉）、featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、
   build_wanted 空格滤、registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
