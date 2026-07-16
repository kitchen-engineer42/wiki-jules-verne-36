---
round: 55
date: 2026-07-15
type_round: 27
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - vigo-bay
  - ham-rock
  - gueboroa-island
  - sea-of-clouds
  - sea-of-rains
result: accept
---

# GROW 2.1-B · R55 · NEW1 · place — R54 新候选首批消费 5 页（standard 档，续页内引注门）

## 本轮公告

**R55 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R54 discover 后 since_evv5=4、since_discover=0、queue(place)=16，决策矩阵高优先门全否，落 NEW1。
建 5 页，全取 R54 SCN28 新候选之最强五枚：
**Vigo Bay**（TTLU 维哥湾，Nautilus 打捞沉船金）+ **Ham Rock**（SC2 Chancellor 搁浅礁岛）+
**Gueboroa Island**（TTLU Torres 海峡 Papua 岛）+ **Sea of Clouds**（RM 月海 Mare Nubium）+
**Sea of Rains**（RM 月海 Mare Imbrium）。后两页成 lunar 月海簇，接既有 lunar-projectile。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=4 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=16, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =22 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=16 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 段级 / 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|----------------------|---------------------------|------|
| vigo-bay | Twenty Thousand Leagues (TTLU)| t2prpG | 1961 | 段级 11 / 页内 6 | real / Spain (Galicia) | accept |
| ham-rock | The Survivors of the Chancellor (SC2)| gpt7CA | 1803 | 段级 9 / 页内 5 | fictional / Atlantic Ocean | accept |
| gueboroa-island | Twenty Thousand Leagues (TTLU)| CZ5Cek | 2035 | 段级 8 / 页内 5 | real / Torres Strait (Papua) | accept |
| sea-of-clouds | Round the Moon (RM)| Kp3yW9 | 1907 | 段级 8 / 页内 6 | real / Moon (near side) | accept |
| sea-of-rains | Round the Moon (RM)| eqyMu2 | 1827 | 段级 7 / 页内 6 | real / Moon (near side) | accept |

> **续 R50 页内引注门**：五页成页后核页内 `(VVV-NNN-PPP)` 去重 ≥5——
> vigo-bay 6、ham-rock 5（贴门）、gueboroa-island 5（贴门）、sea-of-clouds 6、sea-of-rains 6，全达门。

## 命名与互链

- **命名**：vigo-bay（label Vigo Bay / alias Bay of Vigo）/ ham-rock / gueboroa-island /
  sea-of-clouds（alias Mare Nubium）/ sea-of-rains（alias Mare Imbrium）。
- **互链**：Vigo Bay ⇄ [[Twenty Thousand Leagues Under the Sea]] / [[Nautilus]]；
  Ham Rock ⇄ [[The Survivors of the Chancellor]]（新作首页，孤链待簇）；
  Gueboroa Island ⇄ [[Twenty Thousand Leagues Under the Sea]] / [[Torres Strait]] / [[Nautilus]]；
  Sea of Clouds ⇄ [[Round the Moon]] / [[Sea of Rains]] / [[Lunar Projectile]]；
  Sea of Rains ⇄ [[Round the Moon]] / [[Sea of Clouds]] / [[Lunar Projectile]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{TTLU,SC2,RM}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN ≥5 逐页核：6/5/5/6/6 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（16→11）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 55→56`；`type_round 26→27`；`rounds_since_last_evv5 4→5`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 22→23`；`last_updated_round→56`。

## 遗留问题

1. **place 页数 106→111**：本轮 +5，registry 全库 1175→1180。**首建 SC2（Chancellor）与 RM（Round the Moon）地点**。
2. **queue(place) 11**：16 − R55 消费 5 = 11。余 4 R54 新候选（Port Gräuben JCE:7 / Island of Ljakow WC:6 / Island of Sein WC:5 / Icy Cape FC:5）
   + R36/R41 老块 5（Polar Sea/Melville Island/Rocky Mountains/Cape Washington/Hudson's Bay）+ 2 hold（Lake Ontario/Black Sea）。
   下轮 R56：queue=11≥10 且 since_discover=1<10 → 高优先门全否 → NEW1，续消费。
3. **Ham Rock 孤链**：SC2（Chancellor）首页，暂无同作互链页；后续 character/event 轮或补 Chancellor 簇再链。
4. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
5. **SCN28-corpus 深扫倒计时**：since_corpus=23，距阈值 30 尚 7 轮（~R62）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
7. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
