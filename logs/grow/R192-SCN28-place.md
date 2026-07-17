---
round: 192
date: 2026-07-17
type_round: 163
phase: "2.1"
current_type: place
gene: SCN28
pages: []
result: discover
new_candidates: 3
---

# GROW 2.1-B · R192 · SCN28 · place — discover（R187 队列建罄，续掘 MI Lincoln Island 内陆水文/林区网，净新 3 buildable）

## 执行摘要

Phase 2.1-B place 广度扩张第 163 轮（type_round 163）。决策机 §3：since_evv5=9<10（未达 EVV5）、
queue(place)=0 → §3(3)（queue<10）&§3(4)（zombie）触 **SCN28 discover**（先于 EVV5，因 since_evv5 尚未达阈）。
R187 补种 4 项（Reptile End/Vanikoro/Tadorn Marsh/New America）R188–R191 建罄，队列归零，本轮复扫补种。

**矿脉选择**：Mysterious Island（Lincoln Island）为全库最密 toponym 网。前批已建外围（岬/湾/沼/高地：
Reptile End/Tadorn Marsh/Claw Cape/Shark Gulf/Port Balloon/Serpentine Peninsula/Flotsam Point/Union Bay/
Washington Bay/Prospect Heights/Mount Franklin/Granite House 等），本轮转掘**内陆水文/林区网**——
主河 The Mercy 及其左岸林 Jacamar Wood、Serpentine Peninsula 密林区 Forests of the Far West。

**净新 3 buildable（均文件系统 + 后缀变体查重，均 MI 单源 ≥5 solid distinctPN）**：

1. **The Mercy → mercy-river**（MI×168 distinctPN 极密）：Lincoln Island 主河，balloon 抛落处近旁，
   感 Providence 恩命名（MI-011-074）；Chimneys 由其 elbow 折返（MI-012-069/070）；穿 Prospect Heights
   达 Lake Grant（MI-013-028）；左岸即 Jacamar Wood（MI-013-033）；渡河为南探难点（MI-013-063）。
2. **Jacamar Wood → jacamar-wood**（MI×24）：Mercy 左岸林，猎 jacamar 鸟得名（MI-013-033）；
   斜穿东南→西北（MI-015-033）；无桥前仅此岸可猎（MI-019-024）；含于 Far West 林延展至目不能及（MI-025-028）；
   Granite House 窗以其枝伪装（MI-043-072）。
3. **Far West → far-west**（MI-referent 33 distinctPN）：Serpentine Peninsula 密林命名 Forests of the Far West
   （MI-011-075）；久未探（MI-019-024）；西距四英里首树（MI-021-017）；兽群栖此逼近 Prospect Heights
   （MI-022-035）；采野菜远征（MI-030-011）。**混指剔除**：generic American West（AM/ASC/AWED/EHLA 21 hits）非
   Lincoln Island 指，建页仅取 MI Lincoln Island 林区指。

new_candidates=3 ≥ type_close_new_candidate_min=3 → discover_streak_low 保持 0（未触低产）。
**未建页**：SCN28 为发现轮，仅入队 + 抽样验 solidity，since_discover 归 0。registry 恒 1462，place 恒 394。

## 决策矩阵（SCN28 discover）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=9<10 | 否 |
| 1b | EVV5（since_evv5≥10）| =9<10 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| **3** | **SCN28（queue<10 或 since_discover≥10）** | **queue=0<10** | **触发** |
| 4 | SCN28-zombie（queue(place)==0）| =0（同触）| （3 已触）|
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | （前置已触）|

> §3(3) 与 §3(4) 同时成立（queue=0 既 <10 又 ==zombie），SCN28 discover 触发。
> since_evv5=9<10 未达 EVV5 阈，故 SCN28 先行；**R193 起始 since_evv5=10 → §3(1b) R193 = EVV5**（全库 schema 反思，不建页）。

## 页面处理记录

本轮为 discover 轮，未建页。入队候选（建序）：

| 建序 | slug | label | book | rof | region | distinctPN | 状态 |
|------|------|-------|------|-----|--------|-----------|------|
| 1 | mercy-river | The Mercy | The Mysterious Island | fictional | Lincoln Island | MI×168 | 入队待建 R194 |
| 2 | jacamar-wood | Jacamar Wood | The Mysterious Island | fictional | Lincoln Island | MI×24 | 入队待建 |
| 3 | far-west | Far West | The Mysterious Island | fictional | Lincoln Island | MI×33(referent) | 入队待建 |

**排除**：serpentine-peninsula（既有页，MI-011-063 命名 Serpentine Peninsula/Reptile-end 同段，本体已建）；
great-salt-lake（Salt Lake 全为 Great Salt Lake AWED 同指）；Medicine Bow（AWED×5 单 80DA 铁路桥 borderline DEFER）；
Reptile Point（MI×3 净<5）、Grant Lake（2）、Prospect Plateau（0）DEFER。

## EXIT-GATE 检查（discover 轮）

- **G1 每句 PN grounding**：候选均抽样 solid full PN（见执行摘要），建页时逐句 grounding。✔（deferred to build）
- **查重充分**：mercy-river/jacamar-wood/far-west 均文件系统 test -f + 后缀变体（-river/-wood/-forests）+ 语义排除既有 serpentine-peninsula/great-salt-lake。✔
- **净新 ≥3**：3 buildable（Mercy/Jacamar Wood/Far West）达 min。✔
- **矿脉未宣布饱和**：MI 内陆网仍有余项（Lake Grant/Mount Bell/Falls River 待复扫）。✔
- **排除检查**：本轮仅改 queue.md/grow_state.json/log，见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（SCN28，grow_state 存 R193 起始计数）

| 字段 | R192 起始 | R193 起始（本轮末写入）| 变更 |
|------|----------|---------------------|------|
| current_round | 192 | 193 | +1 |
| type_round | 163 | 164 | +1 |
| rounds_since_last_evv5 | 9 | 10 | +1（**达阈，R193 触 EVV5**）|
| rounds_since_last_discover | 4 | 0 | **RESET**（discover）|
| discover_streak_low | 0 | 0 | 不变（new_cand=3≥3）|
| rounds_since_last_corpus_discover | 128 | 129 | +1 |
| last_updated_round | 192 | 193 | — |

## 遗留问题

1. **place 页数 394（不变）**：本轮 discover 未建页。registry 全库 1462，unknown 0。
2. **下轮 R193 = EVV5（§3(1b)）**：R193 起始 since_evv5=10≥10 → 触 EVV5 全库 schema 反思（**不建页**），
   评审 place-schema 一致性、既有页 grounding、debt 盘点，回填模板。EVV5 后 since_evv5 归 0。
3. **R194 起建序**：The Mercy（mercy-river）→ Jacamar Wood（jacamar-wood）→ Far West（far-west），
   3 项后队列罄，R197 须再 SCN28 discover。均 MI 单源 ≥5 solid 已抽样确认。
4. **Far West 混指剔除纪律**：建页时仅取 MI Lincoln Island 林区指（33 distinctPN），
   剔 generic American West（AM/ASC/AWED/EHLA 21 hits），避免 wrong-referent 稀释。
5. **MI 内陆网未采盘点（R197 discover 预备）**：Lake Grant（MI 密，湖本体待查 distinctPN 与 grant-lake dup）、
   Falls River（MI，Mercy 支流待查）、Mount Bell、Creek Glycerine、Grand View（待复扫 distinctPN 与 dup）。
6. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮 discover 未建页。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=128→129（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **DEFER/DUPLICATE 累积**：本轮 +Medicine Bow（borderline DEFER）/Reptile Point/Grant Lake/Prospect Plateau DEFER、
    Salt Lake(=great-salt-lake)/Serpentine(=serpentine-peninsula) DUPLICATE；既有 Cape Mandible/Indian Peninsula/
    Balearic Isles DEFER，Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen 等 DUPLICATE 照旧。
11. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
12. **洲级 America/Europe/Asia 续 HOLD**。
