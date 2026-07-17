---
round: 176
date: 2026-07-16
type_round: 147
phase: "2.1"
current_type: place
gene: NEW1
pages: [cassange]
result: success
---

# GROW 2.1-B · R176 · NEW1 · place — 建 Cassange（DSCF 安哥拉 Benguela 内陆奴隶市场镇，Alvez 第三 factory，净 solid 6）

## 执行摘要

Phase 2.1-B place 广度扩张第 147 轮（type_round 147）。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10、streak=0<3、since_discover=5<10、queue(place)>0、stub%=0 → §3(7)）。
承 R175 probe 补种的 DSCF 安哥拉内陆·奴隶贸易 toponym 队列，本轮取 **Cassange**（净 solid 6 超门）。

**候选抽样对比（Bihe vs Cassange）**：R175 遗留 #2 预留 Bihe/Cassange 二选一。gather.py 复核——
Bihe 净 solid 5（DSCF；Alvez 第二 factory），Cassange 净 solid 6（DSCF；Alvez 第三 factory，
多 Livingstone 路线锚点）。**取较强者 Cassange 本轮建，Bihe 顺延 R177**。

**建 Cassange（DSCF 单源，净 solid 6 超门）**：7 distinctPN 全 DSCF。取 6 solid：
019-049（Benguela 内陆奴隶贸易市镇，与 Bihe/Kazounde 并列）、020-018（Alvez 一 agent 携奴队离 Cassange 失踪）、
027-006（Alvez 第三 factory 位 Benguela 之 Cassange）、032-025（region 破败时 Cassange factories 亦毁）、
032-045（Livingstone 经 Cassange 后抵 Saint Paul de Loanda）、032-046（Livingstone 归途 2/20 离 Cassange）。
033-015（Bihe/Kazounde/Cassange 三安哥拉奴市 enum）作支撑。slug cassange，label「Cassange」。
feature-aware 双测 cassange 皆 NEW。

place 计数 381→382，registry total 1449→1450，unknown 恒 0。
首版全段 ≤400（254/385/299/292）；para 2 建前压缩 407→385（"in charge of a caravan of slaves,
and was not heard of again" → "with a caravan of slaves, and vanished"）。add_page 一次成型，pn_validator strict 建后即通过。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=5<10、queue>0 | 否 |
| 4 | SCN28-zombie（queue(place)==0）| >0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| cassange | 3W67q1 | Dick Sand: A Captain at Fifteen | real | West Africa | 6 | Benguela 内陆奴隶市场镇；Alvez 第三 factory；Livingstone 路线锚点 |

- **cassange**：6 distinct solid PN（全 DSCF）— 019-049（Benguela 内陆奴市，与 Bihe/Kazounde 并列）/020-018（Alvez agent 携奴队离城失踪）/027-006（Alvez 第三 factory）/032-025（region 破败 factories 毁）/032-045（Livingstone 经城抵 Loanda）/032-046（Livingstone 归途 2/20 离城）。033-015 enum 支撑。DSCF 单源。链 dick-sand-a-captain-at-fifteen。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：cassange 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：首版全段 ≤400（254/385/299/292）；para 2 建前压缩 407→385。✔
- **G3 ≥5 distinct PN**：6（DSCF 单源，净 solid 6 超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；book 含冒号已单引号（LAW §8）。✔
- **registry 一致**：total 1450 place 382 unknown 0。✔
- **查重充分**：feature-aware 双测 cassange 皆 NEW。✔
- **排除检查**：`git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` → clean。✔

## 六步状态机（NEW1，grow_state 存 R177 起始计数）

| 字段 | R176 起始 | R177 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 176 | 177 |
| type_round | 147 | 148 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 112 | 113 |
| last_updated_round | 176 | 177 |

## 遗留问题

1. **place 页数 382**：本轮 +1（Cassange）。registry 全库 1450，unknown 0。
2. **下轮 R177 = NEW1**：since_evv5=5<10、since_discover=6<10、queue>0（Bihe/Coanza）→ §3(7) NEW1。
   建 **Bihe**（DSCF 安哥拉内陆商站/Alvez 第二 factory，净 solid 5，建前抽样确认）；Coanza 河 referent 需先严剔。
3. **R170 discover 建序收官后 R175 probe 队列进度**：Loanda ✔(R175) → Cassange ✔(R176) → 余 Bihe(R177) / Coanza(严剔待定)。
4. **DSCF 安哥拉富矿续采（place 未饱和第 6 次证实延续）**：Loanda(8)+Cassange(6)+queue Bihe/Coanza——
   Dick Sand 安哥拉内陆·奴隶贸易 toponym 层持续产出，HK-premature-saturation-claim 保持证伪。
5. **建前压缩纪律见效**：R176 para 2 建前 407→385，无建后 edit。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
7. **legacy H1 遗留（承 R171 EVV5）**：HK-legacy-h1-in-place-pages（150 页），DEFER 批处理。
8. **corpus-discover 顺延**：since_corpus=112→113（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：Brindisi 净4、Virginia 净4、Indiana 净0、Louisiana/Arkansas/Tennessee hold、
    Colorado/Michigan 河湖歧义、Baikal DUPLICATE、Yeniseisk 净1、Tioumen 净3、Carmen 净3、Mozambique 净0；Coanza 待判。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
