---
round: 275
date: 2026-07-18
phase: "2.1"
gene: DEDUP-correction
pages: [death-of-captain-nemo]
result: success
---

# GROW 2.1-B · R275 · DEDUP 更正 — 移除重复 event 页 death-of-captain-nemo（SI-017 与既有 MI nemo-death 同一事件）

## 执行摘要

R275 zombie discover 前置校验发现 R272 所建 **death-of-captain-nemo**（SI-017）为 **重复页**，予以移除。

**根因**：**The Secret of the Island**（VVV=SI）实为 **The Mysterious Island**（VVV=MI）第三部之别译；
语料 sentence_index 将同一部小说以两个 VVV 码各编码一次（MI 全本 + SI 第三部）。
因此 SI-017（Nemo 于 Nautilus 弥留长逝、殖民者开阀沉舟为墓）与既有 MI event **nemo-death**
（MI-059，label「The Death of Captain Nemo」，aliases [Nemo's Last Hours]）为**同一事件**。

**R271 discover 误判**：R271 zombie discover 日志称「变体 nemo-death … ABSENT」，
但从未实际 `ls` 核 `nemo-death.md`（该页 R-早期已存在）。此为「dup-check 须逐变体/alias 做 filesystem 核」
铁律的违反——凭空断言 ABSENT。

## 处置

| 动作 | 细节 |
|------|------|
| git rm 页 | `docs/wiki/pages/de/death-of-captain-nemo.md` |
| git rm history | `docs/wiki/history/de/death-of-captain-nemo.jsonl` |
| rebuild registry | `build_registry.py docs/wiki/pages` → event **45→44**，total **1520→1519**，unknown 0 |
| queue.md 更正 | 建序 28 标 ✘ 移除（DUPLICATE）；R271 discover 行加「更正」注，删「变体 nemo-death ABSENT」误述 |
| 入链核查 | 无页面链向该 dup；`the-mysterious-island` 之 `[[The Death of Captain Nemo]]` 解析至 nemo-death（label 精确匹配），未破链 |

**alias 损失（可接受）**：dup 页 aliases [The Last Moments of Captain Nemo, Death of Prince Dakkar] 未并入 nemo-death；
「Death of Prince Dakkar」为角色本名，具检索价值，记为 HK 待批（不擅改既有良页）。

## 连带判定

- **destruction-of-lincoln-island（SI-019，R273）保留**：Lincoln 岛火山毁灭为**独立且未覆盖**事件，
  MI 现有三 event（lincoln-island-landing MI-001 / tabor-island-castaway MI-036 / nemo-death MI-059）
  皆不含岛之毁灭。虽源自 SI 副本编码，事件真实且唯一，**非重复**。book 字段「The Secret of the Island」
  与 wiki 惯用「The Mysterious Island」不一致，记 HK 待批（PN 为 SI-* 编码，暂不改）。
- **the-madman-in-the-balloon（DA-001，R274）保留**：DA「A Drama in the Air」为独立短篇，
  VB「A Voyage in a Balloon」为同一故事之别译副本（17 处重合已核）；仅建 DA 一页，无重复。

## 零 event 池穷尽结论

| VVV | 作品 | 判定 |
|-----|------|------|
| SI | The Secret of the Island | =MI 第三部别译，已覆盖 → **不再掘** |
| VB | A Voyage in a Balloon | =DA 别译副本 → **不再掘** |
| AMB | （反思随笔）| 非离散叙事事件 → 剔 |
| YEAR | （未来学随笔）| 非离散叙事事件 → 剔 |

**结论**：零 event 作品池实已穷尽。后续 SCN28-zombie 须转向**单事件作品之第二事件**掘矿，
不得再掘 SI/VB。dup-check 对每候选 slug + 全变体 + 全 alias 逐一 filesystem 核（本次教训）。

## 状态机

**不消耗建轮**：本次为纠错移除，非 gene-express 建轮，grow_state 计数器不变（维持 R275-start）。
R275 zombie discover 于本更正后照常执行并推进至 R276-start。

## 遗留问题（更新）

1. **event 页数回正 44**、registry total **1519**、unknown 0。
2. **HK 待批**：（a）nemo-death 并入 alias「Death of Prince Dakkar」「The Last Moments of Captain Nemo」；
   （b）destruction-of-lincoln-island book 字段 SI→MI 归一。二者均不擅动既有页，批量评审时处置。
3. **dup-check 铁律强化**：discover 播种候选时，每 slug + 变体 + alias 必 filesystem 核，禁止凭空 ABSENT。
