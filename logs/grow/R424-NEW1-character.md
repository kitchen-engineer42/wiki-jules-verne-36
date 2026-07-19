---
round: 424
date: 2026-07-19
type_round: 116
phase: "2.1"
current_type: character
gene: NEW1
pages: [lady-helena]
result: success
---

# GROW 2.1-B · R424 · NEW1 · character — 建 Lady Helena Glenarvan（In Search of the Castaways 之 Duncan 号女主人、力主搜救 Grant 船长遗孤而启航的 Glenarvan 贤妻；补 SC 簇，消费第二十批建序 138，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 88 建（type_round 116），消费 R421 第二十批 discover 队列**建序 138（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=2<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R425 SCN28-zombie 补第二十一批。补 SC 簇。**

**Lady Helena Glenarvan**（*In Search of the Castaways*）——Duncan 号之女主人、Lord Glenarvan 之贤妻、力主搜救 Grant 船长遗孤而启航之贤德淑女。偕夫登舟「Lord Edward Glenarvan was on board with his young wife, Lady Helena, and one of his cousins, Major McNabbs」（SC-001-002），苏格兰淑女而愈见珍重「a charming, high-souled, religious young woman」（SC-003-003）。共解沉船残笺「well, come, we have made out a good deal already」（SC-002-012），夫赞其为遗孤生望之所系「if those poor creatures ever see their native land again, it is you they will have to thank for it」（SC-002-080）。遗孤至城堡则温存以纳「drawing the young girl toward her, and taking both her hands and kissing the boy's rosy cheeks」（SC-003-021），然不以虚望相欺「Heaven forbid that I should answer you lightly such a question; I would not delude you with vain hopes」（SC-003-023）。义举启航「Lady Helena was a brave, generous woman, and what she had just done proved it indisputably」（SC-005-001），复携遗孤同行「Lady Helena could not refuse Mary's request to accompany her」（SC-005-007）。柔以待怯「with an encouraging smile」（SC-003-011），忘私以成夫职「too much concerned herself about them to grudge her husband's temporary absence」（SC-003-005），忧夜难寐候夫归「passed the night in great anxiety, and could not close her eyes」（SC-004-018），夫归则飞奔以迎「Lady Helena flew... the moment he alighted」（SC-004-020）。

**role=supporting**。book='In Search of the Castaways'、first_appearance=SC-001、affiliation 空、**label=Lady Helena Glenarvan，aliases=['Lady Helena', 'Helena']**。

**13 distinct solid PN**（SC-001-002、002-012/080、003-003/005/011/021/023、004-018/020、005-001/007）：均 solid，逾门。「Lady Helena」SC 内单指本人（Glenarvan 之妻）；无消歧冲突。

**查重**：exact-slug lady-helena filesystem test -f ABSENT（bucket la）+ registry entity/label/alias 复验——「Lady Helena Glenarvan / lady-helena」无既建人物页，无冲突。**registry-catch 排除**：glenarvan（既建 slug，label「Lord Glenarvan」）、mary-grant/mcnabbs（各既建）——正文以 wikilink 指既建页。

**SC 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Lord Glenarvan]]（glenarvan，既建，SC-004-020）、[[Mary Grant]]（mary-grant，既建，SC-004-027）、[[Major McNabbs]]（mcnabbs，既建，SC-001-002）、[[In Search of the Castaways]]（work，存，SC-005-001）——四链均无悬挂。**SC 簇再拓**（lady-helena 补 glenarvan/mary-grant/mcnabbs，Duncan 搜救簇）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400）。**引注**：strict 首验 SC-002-080 悬挂（[[Lord Glenarvan]] bullet 0.00% overlap）→ 改锚 SC-004-020 直引「Lady Helena flew... the moment he alighted」→ 复验通过。edit_page rev vs3qqh（Relationships bullet 间已插空行分段，0 exit-8）。quality featured 回填。

character 计数 102→**103**，registry total 1626→**1627**，unknown 恒 0。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 138。消费后 queue=0 → R425 SCN28-zombie 补第二十一批。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| lady-helena | 7Yq0fM→vs3qqh | In Search of the Castaways | supporting | SC-001 | 13 distinct | 偕夫登舟-苏格兰淑女-共解残笺-遗孤生望-温存以纳-不以虚望欺-义举启航-携遗孤行-柔以待怯-忘私成夫职-忧夜候归-飞奔迎夫；label Lady Helena Glenarvan / alias Lady Helena+Helena；SC 3-char 无 Note；0 超段；strict SC-002-080 悬挂→改锚 SC-004-020 通过；四链 [[Lord Glenarvan]]/[[Mary Grant]]/[[Major McNabbs]]/[[In Search of the Castaways]] |

- **lady-helena**：13 distinct solid PN；aliases ['Lady Helena', 'Helena']；character-schema 五 H2。add_page rev 7Yq0fM → edit_page rev vs3qqh（size 2763）。quality featured 回填。pn_validator --mode strict ✓。**SC 簇再拓；Lady Helena 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Lady Helena 登舟-解笺-纳孤-启航-候夫因果；strict ✓（SC-002-080 悬挂修正后）。✔
- **G2 段落 ≤400 字**：0 超门（awk 复核；edit_page Relationships bullet 分段 0 exit-8）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页 + edit_page 复用（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；SC 3-char 无 Note。✔
- **registry 一致**：total 1627 character 103 unknown 0。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；glenarvan/mary-grant/mcnabbs registry label EXISTS 已排除。✔
- **wikilink 完整性**：Lord Glenarvan + Mary Grant + Major McNabbs + In Search of the Castaways 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R425 起始计数）

| 字段 | R424 起始 | R425 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 424 | 425 |
| type_round | 116 | 117 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 360 | 361 |
| last_updated_round | 424 | 425 |

## 遗留问题

1. **character 页数 103**：本轮 +1（lady-helena）。queue(character) 1→**0**（建序 138 消费，第二十批全数消费完毕）。registry 全库 **1627**，unknown 0。
2. **下轮 R425 = SCN28-zombie（§3(4)）**：queue(character)==0 → SCN28-zombie 补第二十一批 discover 候选（≥3 grounded+dup-checked），since_discover 归零。since_evv5=9<10。
3. **第二十批消费完结**：R422 NEW1（136 clawbonny ✓）→ R423 NEW1（137 shandon ✓）→ R424 NEW1（138 lady-helena ✓）→ queue 归 0 → R425 SCN28-zombie 补第二十一批。**EVV5 时点**：since_evv5 R425 起始=9 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**SC 簇再拓**（lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave 反向待回填）、**ACH 簇**（shandon→captain-hatteras/clawbonny 反向、clawbonny→shandon 反向、Johnson/Altamont 待建）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=360→361（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
