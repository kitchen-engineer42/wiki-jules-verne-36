---
round: 491
date: 2026-07-24
type_round: 183
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R491 · SCN28-zombie · character — 第三十六批 discover：密簇反派/证人缺员（sandgoist/martin-holt/patrick-odonoghan），queue 0→3

## 执行摘要

Phase 2.1-B character discover 轮（type_round 183）。§3 首匹配 **§3(4) SCN28-zombie**（since_evv5=9<10；SCN28 周期 since_discover=3<10；**queue(character)=0 → §3(4) 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第三十五批（建序 181-183）R488-R490 全数消费（dame-hansen/crockston/jack-ryan），queue 归 0，本轮触发 zombie discover。

**第三十六批 3 候选**（=3 → discover_streak_low 保持 0）——续「已引未建」高频反派/关键角，据 proper-noun 频次扫描取跨 TN/AM/WC 三密簇核心缺员：

| 建序 | slug | book | VVV | pn_anchor | role | mentions/PN | dup-check | 簇 |
|------|------|------|-----|-----------|------|-------------|-----------|-----|
| 184 | sandgoist | Ticket No. 9672 | TN | TN-004 | antagonist | 76/72 | ABSENT | TN 接 dame-hansen/hulda/joel/sylvius（→6）|
| 185 | martin-holt | An Antarctic Mystery | AM | AM-004 | supporting | 85/75 | ABSENT | AM 接 dirk-peters/jeorling/hurliguerly/jem-west（→7）|
| 186 | patrick-odonoghan | The Waif of the Cynthia | WC | WC-008 | supporting | 116/97 | ABSENT | WC 接 erik/schwaryencrona/bredejord/tudor-brown（→5）|

**候选说明**：
- **sandgoist**（TN，**antagonist**）——Drammen 高利贷者，逼 Dame Hansen 典当彩票、贪婪冷酷；76 mentions/72 distinctPN，首现 TN-004-071。前批 dame-hansen/sylvius-hogg/joel-hansen 页已以纯文本引其→回链，TN→6。
- **martin-holt**（AM）——Halbrane 号帆缆长（sailing-master）、为 Dirk Peters 所救、关联 Hunt 之谜；85 mentions/75 distinctPN，首现 AM-004-002。前批 hurliguerly/jem-west 已引→回链，AM→7。
- **patrick-odonoghan**（WC）——Cynthia 号幸存水手、握 Erik 身世之秘之关键证人、Noah Jones 欲灭口者；116 mentions/97 distinctPN，首现 WC-008-026。WC→5。

**dup-check 汇总**：3 候选 test -f + registry entity/label/alias 精确复验全 ABSENT。distinctPN 全 ≥72。**排除（registry-catch）**：TN 既建 hulda/ole-kamp/sylvius-hogg/joel-hansen/dame-hansen；AM 既建 len-guy/dirk-peters/william-guy/jeorling/hurliguerly/jem-west；WC 既建 erik/tudor-brown/schwaryencrona/mr-bredejord。**建页警示**：Patrick O'Donoghan 含撇号，label/aliases YAML 须双引号（鉴 butler R2 Stone's Hill 教训——单引号内撇号破 YAML→静默丢 frontmatter）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（≥10）| since_evv5=9 | 否 |
| 2 | CLOSE（streak_low≥3）| =0 | 否 |
| 3 | SCN28（since_discover≥10）| =3 | 否 |
| **4** | **SCN28-zombie（queue==0）** | **=0** | **触发** |
| 7 | NEW1 | — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 184-186）+ discover-note。

## EXIT-GATE 检查

- **G4**：discover 轮，仅更新 grow_state + queue.md + 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 dup-check ABSENT、无冲突。✔
- **grounding**：distinctPN 72/75/97，足支撑 ≥16 solid PN。✔
- **网络价值**：三者补密簇反派/证人、完足戏剧张力网；前批纯文本可回链。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R492 起始计数）

| 字段 | R491 起始 | R492 起始 |
|------|----------|----------|
| current_round | 491 | 492 |
| type_round | 183 | 184 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 427 | 428 |
| last_updated_round | 491 | 492 |

## 遗留问题

1. **character 148**：本轮无建页（discover 轮）。queue(character) 0→**3**（第三十六批建序 184-186）。registry **1672**，featured 35（5.0%），覆盖 32 部。
2. **下轮 R492 = EVV5（§3(1)）**：since_evv5 于 R492 起始达 **10** → 触发 §3(1) EVV5 质量评估轮（优先于 NEW1）。评估窗 = R482-R491 所建（含 R488/R489/R490 之 dame-hansen/crockston/jack-ryan + R479-R486 段）。EVV5 后 since_evv5 归 0。
3. **R493 起 = NEW1**：消费建序 184 **sandgoist**（TN 反派，antagonist，76 mentions；深耕 TN→6，回填三页纯文本）。
4. **CLOSE 观察**：高频缺员仍有余（Alvez/Craventy/Malarius/Mulrady/Donellan/Sir Francis Cromarty 等 ≥69 mentions 未建），character 广度未尽，暂不触发 §3(2) CLOSE。Phase 2.1-B 约 R490/500，近名义轮次上限，后续数批后或自然趋 CLOSE → Phase 3。
5. **目标**：grow 至 Phase 10。Phase 2.1-B 广度扩张持续，R491/~500。
6. **PN 渲染 / Martin Paz alias / HK / Pilot 债 / event PN 债 / 回链 / butler queue（3 P-task）**：DEFERRED。
7. **corpus-discover 顺延**：since_corpus=427→428。
