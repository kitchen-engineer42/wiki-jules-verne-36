---
round: 56
date: 2026-07-15
type_round: 28
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - hudsons-bay
  - port-grauben
  - island-of-ljakow
  - island-of-sein
  - icy-cape
result: accept
---

# GROW 2.1-B · R56 · NEW1 · place — R54 新候选次批 + Hudson's Bay 消费 5 页（standard 档）

## 本轮公告

**R56 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R55 后 since_evv5=5、since_discover=1、queue(place)=11，决策矩阵高优先门全否，落 NEW1。
建 5 页：**Hudson's Bay**（FC/ACH 哈得孙湾，严扫排除 Company org）+ **Port Gräuben**（JCE 地心海滩）+
**Island of Ljakow**（WC New Siberian 岛）+ **Island of Sein**（WC 布列塔尼礁岛）+ **Icy Cape**（FC 阿拉斯加岬）。
Hudson's Bay 为 R48 老候选、余四枚自 R54 新候选。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=5 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=11, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =23 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=11 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 段级 / 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|----------------------|---------------------------|------|
| hudsons-bay | The Fur Country (FC) + ACH | VYT7sP | 2047 | 段级 12（排 Company）/ 页内 5 | real / Canada (Hudson's Bay) | accept |
| port-grauben | Journey to the Centre of the Earth (JCE)| YtBU6U | 1988 | 段级 8 / 页内 6 | fictional / Underground (Liedenbrock Sea) | accept |
| island-of-ljakow | The Waif of the Cynthia (WC)| gf0o4S | 1725 | 段级 8 / 页内 6 | real / Arctic (New Siberian Is.) | accept |
| island-of-sein | The Waif of the Cynthia (WC)| fZelm8 | 1612 | 段级 5 / 页内 5 | real / France (Brittany) | accept |
| icy-cape | The Fur Country (FC)| QTfZa7 | 1755 | 段级 5 / 页内 5 | real / United States (Alaska) | accept |

> **续 R50 页内引注门**：五页成页后核页内 `(VVV-NNN-PPP)` 去重 ≥5——
> hudsons-bay 5（贴门）、port-grauben 6、island-of-ljakow 6、island-of-sein 5（贴门）、icy-cape 5（贴门），全达门。
> **Hudson's Bay 消歧**：严扫排除含「Compan」句，仅计水体义 12；页首明标 ≠ [[Hudson's Bay Company]] org 页。

## 命名与互链

- **命名**：hudsons-bay / port-grauben（label Port Gräuben / alias Port Grauben）/
  island-of-ljakow（alias Ljakow Island）/ island-of-sein（alias Île de Sein）/ icy-cape。
- **互链**：Hudson's Bay ⇄ [[The Fur Country]] / [[The Adventures of Captain Hatteras]] / [[Fort Reliance]] / [[Hudson's Bay Company]]（明标异体）；
  Port Gräuben ⇄ [[Journey to the Centre of the Earth]] / [[Liedenbrock Sea]]；
  Island of Ljakow ⇄ [[The Waif of the Cynthia]]（WC 簇渐成）；
  Island of Sein ⇄ [[The Waif of the Cynthia]]；
  Icy Cape ⇄ [[The Fur Country]] / [[Victoria Island]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{FC,ACH,JCE,WC}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN ≥5 逐页核：5/6/6/5/5 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（11→6）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 56→57`；`type_round 27→28`；`rounds_since_last_evv5 5→6`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 23→24`；`last_updated_round→57`。

## 遗留问题

1. **place 页数 111→116**：本轮 +5，registry 全库 1180→1185。
2. **queue(place) 6**：11 − R56 消费 5 = 6，再破 SCN28 阈值（<10）。余 4 真候选
   （Polar Sea FC:14 / Melville Island ACH:9 borderline / Rocky Mountains RM:9 / Cape Washington ACH:5 贴门）+ 2 hold（Lake Ontario/Black Sea）。
   **下轮 R57：queue=6<10 → 优先级 3 SCN28 复扫**。注意：R54 复扫已收割多数强候选，
   R57 若 new_candidates<3 则 discover_streak_low+1，启动 place 关闭倒计时（streak≥3 触发 CLOSE）。
3. **Ham Rock/Ljakow/Sein 孤链**：SC2/WC 作品页簇尚薄，后续 character/event 轮补链。
4. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
5. **SCN28-corpus 深扫倒计时**：since_corpus=24，距阈值 30 尚 6 轮（~R62）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
7. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
