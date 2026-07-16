---
round: 130
date: 2026-07-15
type_round: 101
phase: "2.1"
current_type: place
gene: NEW1
pages: [isthmus-of-panama]
result: success
---

# GROW 2.1-B · R130 · NEW1 · place — 建 isthmus-of-panama（消歧定主体=地峡/航路，7PN）

## 执行摘要

Phase 2.1-B place 广度扩张第 101 轮（type_round 101）。决策机 §3 首匹配裁定 **NEW1**（同 R129 口径，
queue_size 全类型≈17≥10、since_evv5=2<10、streak=1<3、since_discover=1<10、queue(place)>0、stub%=0 → §3(7)）。

消费长期悬置候选 **Panama**（R122 入队，11 distinctPN，「消歧未决」）。本轮作出消歧裁定：
**定主体为 Isthmus of Panama（地峡/大洋捷径）**，统合 isthmus 义（4 PN）+「way of Panama」航路义（3 PN）=7 干净引，
剔 city 义（TT-015-024 城市列举 / TTLU-026-019 wages，2<门）与 gulf 义（TTLU-026-011 单 PN<门）分列 hold。
place 计数 345→346，registry total 1413→1414，unknown 恒 0。

## 决策矩阵（同 R129，NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =1 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| queue_size≈17≥10, since_discover=1 | 否 |
| 4 | SCN28-zombie（queue(current_type)==0）| place>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> queue_size 口径续采全类型（spec 字面），承 R129 HK-queue-size-scope PARK。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| isthmus-of-panama | 8s2wIV | Dick Sand: A Captain at Fifteen | real | Central America | 7 | Atlantic-Pacific 陆桥捷径；统合 isthmus(4)+way-of-Panama 航路(3)；Cordilleras 横越；Nemo Gulf 珍珠场；与 Cape Horn/Good Hope 并列航路选项 |

- **isthmus-of-panama**：PN DSCF-001-016（Golden Age 线 Melbourne↔Isthmus of Panama）/038-004（steamer sailing for the Isthmus of Panama）、WC-015-013（"not thinking of Panama, nor of Cape Horn, nor of the Cape of Good Hope" 三航路并列）、GM-005-011（Panama, California and British Columbia Company）、FEM-024-020（Andes/Cordilleras crosses the Isthmus of Panama）、TTLU-026-011（Gulf of Panama 珍珠场）、ACH-006-020（driftwood towards Pacific by river of the Isthmus of Panama）。**消歧裁定**：Panama 11 PN 分散于 isthmus(4)/route(3)/gulf(1)/city(2)，无单义达 5；定主体为地峡+航路（同一实体，穿越地峡即 way of Panama），凑 7 干净引达门；city/gulf 义分列 hold。链 pacific-ocean/cape-horn/cape-of-good-hope/andes/from-the-earth-to-the-moon/dick-sand-a-captain-at-fifteen/the-waif-of-the-cynthia。pn_validator ✓ 0 issues。

## 过程事故与自纠（本轮唯一异常，已闭环）

**事故**：首建时 frontmatter `book: Dick Sand: A Captain at Fifteen` 值含冒号未加单引号（违 LAW.md §8），
YAML 解析失败 → type 落 `unknown`、quality None（registry 现 unknown=1）。
**误纠致二次污染**：为补 quality 先用 `edit_page.py` 修 book（type 恢复 place 但 quality 仍 None，因 edit_page 不回填），
继而误跑 `compute_quality.py`（无参=全库）—— 该脚本**重评全库 446 页并改写 27 无关页 frontmatter（standard→featured）**及
registry/line_index/recent 批量 churn，**违反 featured 全库重评延后令**（project_grow_featured_regrade：featured 视为无意义，
重评待 RFC 后用户批量评审）。
**闭环处置**：`git checkout` 回退 27 无关页 + pages.json/lite/backlinks/line_index/recent 至 HEAD，删 untracked isthmus 二产物，
以**修正后**（book 加单引号）/tmp 文件重跑 `add_page.py`（**add_page 自动回填 quality**，绕开 compute_quality）。
复验：pages.json 0 quality flips、仅 isthmus-of-panama.md 新增、type=place quality=featured book 正确解析。
**教训**：(1) 含冒号 frontmatter 值建前必加单引号（book/description/label）；(2) 单页补 quality 只用 add_page 回填，
**严禁 compute_quality 无参全库跑**（会触发延后中的全库重评）；(3) edit_page 后 quality 不回填是既知特性（place-schema EVV6 注）。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：isthmus-of-panama 全句源自 sentence_index，pn_validator ✓ 0 issues。✔
- **G2 段落 ≤400 字**：全部符合。✔
- **G3 ≥5 distinct PN**：7（DSCF×2/WC/GM/FEM/TTLU/ACH）。✔
- **G4 脚本建页**：经 add_page.py 建立（含一次 edit_page 修 YAML，均脚本路径，未用 Write/Edit 触碰页面）。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文。✔
- **registry/backlinks 重建**：total 1414 place 346 unknown 0；backlinks 覆盖 1240 页 3263 条。✔
- **排除检查**：commit 前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean（预置 dirty 项 butler.json/character|place|technology-schema.md/rfc-vernean-0003 均不 stage）。✔

## 六步状态机（NEW1，grow_state 存 R131 起始计数）

| 字段 | R130 起始 | R131 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 130 | 131 |
| type_round | 101 | 102 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 1 | 1（NEW1 不动 streak）|
| rounds_since_last_corpus_discover | 66 | 67 |
| last_updated_round | 130 | 131 |

## 遗留问题

1. **place 页数 346**：本轮 +1。registry 全库 1414，unknown 0。
2. **place 开放强候选归零**：R129 建 Mont Blanc/Bay of Bengal、R130 建 Isthmus of Panama 后，
   开放候选仅余洲级 Asia/Europe/America（HOLD，泛指风险须严筛确指句）+ Long Island（clean 4<门）+ 新增 hold（Panama City/Gulf of Panama 单义<门）。
3. **下轮 R131 预测**：queue_size 全类型口径仍≥10 → 续 NEW1；但 place 无干净可建强候选。选项：
   (a) 攻洲级 HOLD（America 须与 united-states 消歧、聚焦洲级确指句 vs 泛指）——高难度编辑判断；
   (b) 若判 place 实质无可建，宜复议 queue_size 口径转 discover/close 路径。倾向 R131 起评估 place CLOSE 时机。
4. **discover_streak_low=1**：R128 遗留；NEW1 不变。place 饱和迹象渐显，后续 discover 续低产将逼近 streak=3（CLOSE）。
5. **corpus-discover 顺延临界**：since_corpus=67，远过阈但非 §3 分支（PARK）。
6. **EVV5 节奏**：since_evv5=3，下次约 R138。
7. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
8. **散文门债**：32 页 >400（DEFERRED）；本轮页 over-400=0，无新增。
9. **PHQ 待决**：Rome/Petersburg/Athens/Amsterdam 荷城 + Long Island + Panama City/Gulf（<门 hold）；amsterdam-island R45 页不合规。
10. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass（32 页）、HK-corpus-discover-not-in-statemachine、HK-queue-size-scope、
    **HK-compute-quality-fullrun-regrade（本轮新记：compute_quality 无参会触发延后中的全库重评，禁用于单页补分）**、
    HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧；国级页价值待评。
