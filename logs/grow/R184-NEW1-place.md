---
round: 184
date: 2026-07-17
type_round: 155
phase: "2.1"
current_type: place
gene: NEW1
pages: [bennet-islet]
result: success
---

# GROW 2.1-B · R184 · NEW1 · place — 建 Bennet Islet（AM 南极小岛，净 solid 8；一次成型全段 ≤400）

## 执行摘要

Phase 2.1-B place 广度扩张第 155 轮（type_round 155）。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10、since_discover=2<10、queue(place)=4>0、stub%=0 → §3(7)）。
取 R181 discover 批次剩项 **Bennet Islet**（AM×13）。文件系统查重 bennet-islet/-island/bennet 皆 NEW。

**Bennet Islet（AM 单源，净 solid 8 超门）**：An Antarctic Mystery 中远南海域一荒岛，Halbrane 循 Jane 航迹南下的登陆点之一。
8 distinct solid：
- **AM-005-054**：周约一 league，以 Jane 船东合伙人 Bennet 命名。
- **AM-019-005**：荒芜，南下时最先向水手报出之陆地。
- **AM-014-006**：Len Guy 宣告拟往 Bennet Islet。
- **AM-014-011**：拟停 24 小时，较 Tsalal 近 50 英里。
- **AM-015-035**：12 月 23 晨 Halbrane 自此启碇，携走 Tsalal 惨案新证。
- **AM-015-002**：无人居——岸无棚屋、无炊烟。
- **AM-011-013**：Len Guy 计划中冰墙外首个登陆点，先于 Tsalal。
- **AM-015-018**：Jane 昔日下锚处遗木板尚存，可断自 Jane 后无他船登岛。

place 计数 387→388，registry total 1455→1456，unknown 恒 0。
add_page 一次成型，全段 ≤400（首版最长 356，未触 HK-addpage-prose-gate-bypass）。pn_validator strict 建后即通过；
build_registry 仅余既有 Robur alias 告警（PARK）。real_or_fictional=fictional、region=Antarctic（与姊妹页 tsalal-island 一致）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| since_discover=2<10；queue=4（discover 冷却中）| 否 |
| 4 | SCN28-zombie（queue(place)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> §3(3)：queue=4<10 名义达 discover 条件，但 R181 刚补种、since_discover=2 仍在冷却，续 NEW1 消耗新候选（承 R183 判据）。
> 队列剩 3（Bennet 后 Long's Peak/Stapi），耗尽后再 SCN28。

## 页面处理记录

| slug | rev | book | rof | region | 页内引注 | 消歧/要点 |
|------|-----|------|-----|--------|---------|----------|
| bennet-islet | uMf97j | An Antarctic Mystery | fictional | Antarctic | 8 | 远南荒岛；以 Jane 船东合伙人命名；Halbrane 停 24h；Jane 下锚遗木板 |

- **bennet-islet**：8 distinct solid PN（AM 单源）；alias [Bennet Island]（原文两拼互用）。链 an-antarctic-mystery。pn_validator --mode strict ✓ 全通过。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：bennet-islet 全句源自 sentence_index；pn_validator --mode strict ✓ 全通过。✔
- **G2 段落 ≤400 字**：一次成型，首版最长 356。✔
- **G3 ≥5 distinct PN**：8 solid（AM 单源，超门）。✔
- **G4 脚本建页**：add_page.py 建，quality 自动回填 featured，未用 Write/Edit。✔
- **schema 一致**：place-schema 四 H2，无 H1，Connections 散文；description 单引号（LAW §8）。✔
- **registry 一致**：total 1456 place 388 unknown 0；仅既有 Robur alias 告警（PARK）。✔
- **查重充分**：文件系统 + 后缀变体（bennet-islet/-island/bennet）。✔
- **排除检查**：见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 六步状态机（NEW1，grow_state 存 R185 起始计数）

| 字段 | R184 起始 | R185 起始（本轮末写入）|
|------|----------|---------------------|
| current_round | 184 | 185 |
| type_round | 155 | 156 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 120 | 121 |
| last_updated_round | 184 | 185 |

## 遗留问题

1. **place 页数 388**：本轮 +1（Bennet Islet）。registry 全库 1456，unknown 0。
2. **下轮 R185 = NEW1**：since_evv5=2<10、since_discover=3<10、queue=3>0 → §3(7) NEW1。
   建 **Long's Peak**（FEM×8+RM×7，Rocky Mtns 巨镜观测台），建前文件系统查重（longs-peak/long-peak/-observatory）+ 抽样 ≥5 solid。
3. **R185+ 建序（R181 批剩 3）**：Long's Peak → Stapi。（2 项后队列罄，须再 SCN28 discover。）
4. **discover 冷却续行**：since_discover=3，queue 名义 3<10 但为新鲜补种，NEW1 消耗中；耗尽（R186 后）触 §3(3) 或 §3(4) 再 discover。
5. **HK-addpage-prose-gate-bypass**：本轮一次成型未触；R183 曾触（Tristan），续常规 awk 段长复检。
6. **主矿脉盘点**：AM 未采层 Tristan/Bennet Islet 本批建齐（剩 FEM Long's Peak/JCE Stapi）。未宣布饱和。
7. **散文门债**：37 页 >400（既有 DEFERRED，HK-addpage-prose-gate-bypass）；本轮页 over-400=0。
8. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
9. **corpus-discover 顺延**：since_corpus=120→121（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
10. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
11. **DEFER/DUPLICATE 累积**：Brindisi/Virginia/Indiana/Louisiana/Missouri/Abyssinia/Tioumen/Carmen/Mozambique/Yeniseisk/Kazan/Tobol、Baikal/Timbuktu/Tampa/Sneffels/Ishim/Tsalal DUPLICATE、Cape Portland/Altona DEFER。
12. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
13. **洲级 America/Europe/Asia 续 HOLD**。
