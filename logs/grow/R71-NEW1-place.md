---
round: 71
date: 2026-07-15
type_round: 42
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - manaos
  - christiania
  - bergen
  - buffalo
  - mounts-doerfel
result: accept
---

# GROW 2.1-B · R71 · NEW1 · place — 建 5 新页（standard 档）

## 本轮公告

**R71 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 14→9**

R70 后 since_evv5=9、since_discover=2、discover_streak_low=0、queue(place)=14、since_corpus=7。
决策矩阵：since_evv5=9<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=14≥10 且 since_discover=2<10 → SCN28 不触发；since_corpus=7<30 → SCN28-corpus 不触发；落 NEW1。
建 5 新页（消费 R68 补种末批候选）：**Manaos**（EHLA 内格罗河口城）+ **Christiania**（TN 挪威首都/今 Oslo）+
**Bergen**（TN 挪威西岸港）+ **Buffalo**（MW Erie 湖东端港城）+ **Mounts Doerfel**（RM 月面南极山脉）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=9 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=14≥10, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =7 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=14 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| manaos | Eight Hundred Leagues on the Amazon (EHLA) | ShRCPC | 7 | real / Amazonas (Brazil) | accept |
| christiania | Ticket No. 9672 (TN) | KahVzO | 7 | real / Norway | accept |
| bergen | Ticket No. 9672 (TN) | PsXVlj | 7 | real / Norway | accept |
| buffalo | The Master of the World (MW) | 2T0fVM | 7 | real / New York (United States) | accept |
| mounts-doerfel | Round the Moon (RM) | Nk6OHb | 5 | real / Southern Moon (circumpolar) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——7/7/7/7/5 全达门。
> **Mounts Doerfel 恰达门**：RM 全语料仅 5 段命名 Doerfel（RM-012-058/016-022/016-030/017-007/017-013），
> 五段全引，distinctPN=5=门；月面 real 地物（南极附近实名山脉），region Southern Moon。
> **alias**：manaos→Manaus（现代名）、christiania→Oslo（现代名）；Verne label 从原文旧称。
> **Buffalo 反污染承 R68**：MW `\bBuffalo\b` 已核为 Erie 湖港城（MW-011/013/014 段），非 bison。
> **同书双页**：christiania 与 bergen 同出 TN，distinctPN 各自独立核。散文门五页全 ≤400（max 361）。

## 命名与互链

- **命名**：manaos（alias Manaus）/ christiania（alias Oslo）/ bergen / buffalo / mounts-doerfel（均 real）。
- **互链**：Manaos ⇄ [[Eight Hundred Leagues on the Amazon]]；Christiania ⇄ [[Ticket No. 9672]]；
  Bergen ⇄ [[Ticket No. 9672]]；Buffalo ⇄ [[The Master of the World]]；Mounts Doerfel ⇄ [[Round the Moon]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{EHLA,TN,MW,RM}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（max 361）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：7/7/7/7/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS（max 361）|
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；manaos/christiania 各有 alias |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（14→9）；grow_state NEW1 six-step；无新 alias 冲突 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 71→72`；`type_round 42→43`；`rounds_since_last_evv5 9→10`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 7→8`；`last_updated_round→72`。

## 遗留问题

1. **place 页数 160→165**：本轮 +5，registry 全库 1228→1233，unknown 0。
2. **queue(place) 9<10**：14 − R71 消费 5 = 9（含 2 holds Lake Ontario/Black Sea + Kara Sea 待精扫
   + 6 跨源候选 North Sea/Firth of Clyde/Long Island/Goat Island/Bay of Bengal/Cape Bon）。
   R68 补种 15 强候选已全数消费（R69×3 + R70×2 + R71×5... 实为 R69 消费 Irkutsk/Kazounde/Iquitos/
   Stockholm/Zanzibar，R70 消费 Omsk/Tomsk/Pekin/London/San Francisco，R71 消费 Manaos/Christiania/
   Bergen/Buffalo/Mounts Doerfel = 15 全清）。
3. **下轮 R72 = EVV5（优先级 1b）**：since_evv5 六步后=10≥10 → **R72 触发 EVV5 质量抽检轮**（非建页）。
   注：queue=9<10 本会触发优先级 3 SCN28，但 EVV5（1b）优先级更高抢占。EVV5 抽检既有 place 页样本，
   评分记录，since_evv5 归 0；不新增/编辑页面（除非抽检发现须修）。
4. **R73 预判**：EVV5 后 since_evv5=0；queue=9<10、since_discover=3（EVV5 非 discover，since_discover+1→4？
   按 EVV5 six-step 确认）→ 优先级 3 SCN28 表层复扫补种 place 候选。EVV5 与 SCN28 具体 six-step 建页前查 spec。
5. **alias 待核已定**：Manaos↔Manaus、Christiania↔Oslo（本轮已写入 aliases）。
6. **Kara Sea 建前须精扫**：承 R63–R68，「kara」子串过配。
7. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）。
8. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
9. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
