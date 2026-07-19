---
round: 337
date: 2026-07-19
type_round: 30
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R337 · SCN28 · character — 第五批 discover：6 候选补给（queue 归零后勘探）

## 执行摘要

Phase 2.1-B character 第 5 次 discover（`SCN28-zombie`）。决策机 §3 首匹配 **SCN28**
（since_evv5=7<10 → 非 §3(1)；discover_streak_low=0<3 → 非 §3(2)；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。

**本轮为勘探补给轮，不建页（pages: []）**。动作：向 character 候选队列补 **6** 个 grounded + dup-checked 候选（建序 75-80），更新 grow_state（since_discover→0）+ 写日志。registry 不变（total 1563、character 39、unknown 0）。

**6 候选 ≥ type_close_new_candidate_min(3)** → discover_streak_low 保持 **0**（无 type-close 压力，character 类型远未饱和）。

## 候选清单（建序 75-80，均 filesystem dup-check ABSENT）

| 建序 | slug | label | book | pn_anchor | role | mentions | 簇/要点 |
|------|------|-------|------|-----------|------|----------|---------|
| 75 | sangarre | Sangarre | Michael Strogoff | MS-006 | antagonist | 45 | Ogareff 之吉普赛女党羽、密探，助识破 Michael；MS 簇完形（ivan-ogareff/feofar-khan/michel-strogoff）|
| 76 | hector-servadac | Hector Servadac | Off on a Comet | OC-002 | protagonist | 522 | 法国上尉、彗星撞击后随 Gallia 遨游太空之主角；OC 新簇种子 |
| 77 | ben-zoof | Ben Zoof | Off on a Comet | OC-002 | supporting | 310 | Servadac 之忠仆勤务兵、蒙马特之子；OC 簇配对 |
| 78 | lieutenant-hobson | Lieutenant Hobson | The Fur Country | FC-001 | protagonist | 589 | 哈德逊湾公司中尉、率队建极地毛皮堡；FC 新簇种子 |
| 79 | thomas-roch | Thomas Roch | Facing the Flag | FF-001 | supporting | 204 | 疯狂发明家、Fulgurator 超级武器创造者；FF 新簇种子 |
| 80 | len-guy | Len Guy | An Antarctic Mystery | AM-001 | protagonist | 222 | Halbrane 号船长、寻兄 William Guy 之南极远征领队；AM 新簇种子 |

> **dup-check**：6 slug filesystem `docs/wiki/pages/*/<slug>.md` 全 ABSENT。
> **簇效应**：MS 簇经 sangarre 完形（Ogareff 之党羽）；OC 以 hector-servadac/ben-zoof 配对种子起簇；FC/FF/AM 各下一单作品主角种子，为 Phase 2.1 广度扩张开四部新作品之门。
> **深池说明**：初拟 Mathias Sandorf/Kaw-djer/Wilhelm Storitz/Kéraban 经查**不在本 36 部合集**（无对应 VVV），故改选合集内实有作品之主角/要角。余续存候选：claudius-bombarnac(ASC)/erik(WC)/james-starr(UC)/nell(UC)/paulina-barnett(FC)/palmyrin-rosette(OC)/dirk-peters(AM)/len-guy 兄 William Guy 等，留第六批。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=0 | — |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6/7 | RCH2/NEW1 | — | 未达 |

> queue(character)==0（R336 末位消费后归零），§3(4) 触发勘探。补 6 候选后 queue(character)=6。

## EXIT-GATE 检查（SCN28 勘探轮，仅 G4）

- **G4 记录完整性**：本轮 pages: []，无建页；6 候选清单、dup-check、pn_anchor、role、簇归属完整入日志 + queue.md。✔
- **G1/G2/G3/G5 跳过**：SCN28 勘探轮无建页/改页，按规程跳过。✔
- **registry 一致**：total 1563 character 39 unknown 0，本轮未变。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R338 起始计数）

| 字段 | R337 起始 | R338 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 337 | 338 |
| type_round | 29 | 30 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 6 | **0**（SCN28 复位）|
| discover_streak_low | 0 | 0（new_candidates=6≥3）|
| rounds_since_last_corpus_discover | 273 | 274 |
| last_updated_round | 337 | 338 |

## 遗留问题

1. **character 页数 39**：本轮 discover 未建页。queue(character) 0→**6**（建序 75-80）。registry 全库 **1563**，unknown 0。
2. **下轮 R338 = NEW1（§3(7)）**：since_evv5=8<10；since_discover=0；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 75（sangarre）。Sangarre（book Michael Strogoff，pn_anchor MS-006，role antagonist，MS 2-char 无 Note）——Ogareff 之吉普赛女党羽、密探；与 ivan-ogareff/feofar-khan/michel-strogoff 可互链，MS 簇完形。
3. **第五批消费预判**：R338-343 依次建 sangarre/hector-servadac/ben-zoof/lieutenant-hobson/thomas-roch/len-guy；**惟 R339 遇 EVV5（since_evv5 于 R339 达 10）优先插入**——即 R338 建 sangarre 后，R339 触发 §3(1b) EVV5 schema 反射轮（pages:[]），第五批余 5 候选顺延至 R340-344 建成，R345 queue 再归 0 → 第六批 discover。
4. **captain-grant→Robert 回链回填**：DEFERRED（R336 记录）。
5. **EVV5 下次 = R339**（since_evv5 于 R329 复位，R339 达 10）。R338 NEW1（sangarre）→ R339 EVV5 反射 → R340 起续建第五批。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=273→274（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
