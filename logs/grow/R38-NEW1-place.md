---
round: 38
date: 2026-07-15
type_round: 10
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - cape-esquimaux
  - behring-strait
  - gourbi-island
  - spencer-island
  - red-sea
result: accept
---

# GROW 2.1-B · R38 · NEW1 · place — R36 复扫第二批 5 页（standard 档）

## 本轮公告

**R38 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 6 候选**

queue(place)=21，无高优先门抢先，落 NEW1 默认门。建 R36 复扫第二批 5 页：
**FC 漂流簇收尾**（Cape Esquimaux FC:23 / Behring Strait FC:22，漂流终点海峡）+
**孤岛簇**（Gourbi Island OC:41 彗星岛 / **Spencer Island** GM，并 Phina Island）+
**TTLU**（Red Sea TTLU:28，Nautilus 航线）。

> **EVV5 时序勘误（承 R37 遗留误记）**：R37 六步后 `rounds_since_last_evv5=9`（非 10）。EVV5 门
> 于**轮首**判 `since_evv5 ≥ 10`（R20 先例：R19 末达 10，R20 触发）。故 **R38 仍为 NEW1**，
> R37 日志「R38=EVV5」计数早了一轮。本轮六步后 since_evv5 达 10 → **R39 方触 EVV5**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =9（<10）| 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue_size=21, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =5 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=21 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| cape-esquimaux | The Fur Country (FC)| bOXBSk | 2152 | 23 | fictional / Arctic N. America | accept |
| behring-strait | The Fur Country (FC)| HoSRPw | 2109 | 22 | real / Asia–America passage | accept |
| gourbi-island | Off on a Comet (OC)| 2c7uBR | 1926 | 41 | fictional / Comet Gallia | accept |
| spencer-island | Godfrey Morgan (GM)| kUew0J | 2185 | 40+18 | fictional / Pacific Ocean | accept（合并）|
| red-sea | Twenty Thousand Leagues (TTLU)| RGgbET | 1947 | 28 | real / Africa–Arabia | accept |

> **合并裁定（Spencer Island = Phina Island）**：GM 中 Godfrey 漂流之岛真名 **Spencer Island**
> （Kolderup 拍下，旧金山西南 460 海里，32°15'N 145°18'W，GM-001-028/029），Godfrey 不知其名，
> 以未婚妻名唤作 **Phina Island**（GM-010-062）；结局揭晓「You should say Spencer Island!」
> （GM-022-017）。二名同岛，**并为一页**：slug=spencer-island（真名/含坐标），alias=「Phina Island」
> （叙事主用名，40 PN）。一页消费 queue 两候选（Phina + Spencer）。承 R37 铁律：建前查同一实体避免重页。

> **互链**：Cape Esquimaux ⇄ [[cape-bathurst]] / [[fort-hope]] / [[port-barnett]]（FC 漂流簇）；
> Behring Strait ⇄ [[cape-bathurst]] / [[victoria-island]] / [[fort-hope]]（漂流终点）；
> Red Sea → [[nautilus]]（Nemo 潜艇航线）；Gourbi Island / Spencer Island 源作暂无既有页可链，
> Connections 用纯文本（Gallia / Phina Island / Godfrey Morgan 均红链或非页，schema 允许）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{FC,OC,GM,TTLU}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页无超长段 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；spencer-island 加 alias |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 6 候选（含 Phina/Spencer 合并）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 38→39`；`type_round 9→10`；`rounds_since_last_evv5 9→10`（R39 将触 EVV5）；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 5→6`；`last_updated_round→39`。

## 遗留问题

1. **R39 = EVV5 到期**：since_evv5 本轮达 10 → R39 触 **EVV5 place schema 反思轮**（不建页、不消费队列，
   扫全 place 页评模板稳定性 + 反哺；EXIT-GATE 仅 G4）。样本 52 页，充足。
2. **queue(place) 余 15**：R36 补种 26 − R37 消费 5 − R38 消费 6（Phina/Spencer 并）= 15。
   下批优选：Lake Erie(MW:27) / Fort Providence(ACH:22) / Beechey Island(ACH:20) / Gulf Stream(TTLU:18) /
   Torres Strait(TTLU:15) / Polar Sea(FC:14) / Loch Malcolm(UC:13) / Lake Baikal(MS:12) / Gallian Sea(OC:12)。
3. **建前二次校准照旧**：余 15 候选主源 distinctPN 为 R36 grep 值，建页前逐页复核；同一实体先查合并（承 Spencer/Phina）。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
