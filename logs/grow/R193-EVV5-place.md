---
round: 193
date: 2026-07-17
type_round: 164
phase: "2.1"
current_type: place
gene: EVV5
pages: []
result: reflect
---

# GROW 2.1-B · R193 · EVV5 · place — schema 反思（place-schema 复盘：converged 确认，模板零改动）

## 执行摘要

Phase 2.1-B place 广度扩张第 164 轮（type_round 164）。决策机 §3：R193 起始 since_evv5=10≥10 →
§3(1b) 触 **EVV5**（schema 反思，**不建页**）。since_discover=0（R192 SCN28 刚 RESET）<10，故非 EVV5+SCN28 合并轮，纯 EVV5。

**复盘对象**：`local/template/place-schema.md`（MTD3 定稿 + EVV5 r1/r2 追加 + EVV6 converged）。
**复盘输入**：place 类型全库 394 页；本 EVV5 周期（R183–R192）新建 8 页
（tristan-da-cunha/bennet-islet/longs-peak/stapi/reptile-end/vanikoro/tadorn-marsh/new-america）。

## 复盘输入

| 指标 | 值 | 来源 |
|------|-----|------|
| place 全库页数 | 394 | pages.json |
| 本 EVV5 周期新建 | 8（R183–R192，含 2 SCN28 discover 轮不建页）| logs/grow |
| 近 6 页 pn_validator strict | 6/6 ✓ 全通过 | longs-peak/stapi/reptile-end/vanikoro/tadorn-marsh/new-america |
| registry alias 告警 | 1（Robur PARK，与 place 无关）| build_registry |
| schema 结构偏差 | 0 | 全 8 页四 H2 无 H1，Connections 散文 |
| 段落 >400 触门 | 0（本周期建页；R185/R186 建前 awk 拦截修正）| awk 预检 |

## 发现

- **模板零改动**。place-schema 自 EVV6 converged（2026-07-13）后历经 tech surface toponym 层
  （AM/JCE/FEM/OC）+ 本周期 MI/20KL/ACH 强矿脉共 8 页，四节结构（Overview / In the Narrative /
  Geography & Features / Connections）+ `book`/`real_or_fictional`/`region` 专属字段全程自然成立，无新增缺陷。
- **real/fictional 双档持续适配**：本周期真实地点（longs-peak/stapi/vanikoro/tristan-da-cunha）以
  Geography & Features 述真实地理，虚构地点（reptile-end/tadorn-marsh/new-america/bennet-islet）述作者构造地形，
  与 EVV5 r1 结论一致，无空节张力。
- **MI 单源页达标不困难**：Lincoln Island toponym 网极密，reptile-end(10)/tadorn-marsh(7)/vanikoro(11) 均
  MI/单源 ≥7 solid，印证 EVV5 r1「单书角色难达 standard」在 place 类型不成立——地理实体单书内引注密度足够。
- **段长门为建页操作层约束，非 schema 缺陷**：R185/R186 首版 >400（441/438），awk 预检拦截后 trim 达标。
  HK-addpage-prose-gate-bypass（add_page 不强制 400 门）为已记 debt，续以 awk 预检兜底，非模板问题。

## 全库质量分布观察（re-grade DEFERRED，仅记录不动作）

- place 394 页：featured 377 / none 17。17 'none' 页为未回填 quality 的历史/早期页
  （aberfoyle/astrakhan/bolivia/cape-tchelynskin/connecticut/dublin/easter-island/guinea/hudsons-bay/
  kentucky/lake-tanganyika/massachusetts/niagara-falls/pennsylvania/sou-tcheou/tristan-da-cunha/victoria-island）。
- 注：tristan-da-cunha（R183 add_page 建）本应自动回填 featured 却为 none——add_page 回填在少数页未生效，
  归入 **featured 虚高/full-library re-grade DEFERRED** 债（standing directive：featured 视为无意义，
  全库 re-grade 顺延至 RFC 批审后）。本轮不动作，仅登记。

## 判定

- **place-schema.md 确认 converged，EVV6 定稿后零改动**，与 technology（追加量 3→2→0）收敛轨迹同构。
- schema 稳定，无阻塞 Phase 2.1 推进的模板债。EVV5 周期正常收敛。
- 进入 R194 继续 NEW1 建页，消费 R192 discover 队列（The Mercy → Jacamar Wood → Far West）。

## 六步状态机（EVV5，grow_state 存 R194 起始计数）

| 字段 | R193 起始 | R194 起始（本轮末写入）| 变更 |
|------|----------|---------------------|------|
| current_round | 193 | 194 | +1 |
| type_round | 164 | 165 | +1 |
| rounds_since_last_evv5 | 10 | 0 | **RESET**（EVV5 执行）|
| rounds_since_last_discover | 0 | 1 | +1（非 SCN28）|
| discover_streak_low | 0 | 0 | 不变 |
| rounds_since_last_corpus_discover | 129 | 130 | +1 |
| last_updated_round | 193 | 194 | — |

## EXIT-GATE 检查（EVV5 反思轮）

- **未建页**：EVV5 为 schema 反思轮，pages=[]，registry 恒 1462 place 394 unknown 0。✔
- **schema 复盘完成**：place-schema converged 确认，模板零改动。✔
- **grounding 抽检**：近 6 页 pn_validator strict 6/6 ✓。✔
- **debt 登记**：featured re-grade DEFERRED（17 none 页含 tristan-da-cunha 回填缺失）已记，不动作。✔
- **排除检查**：本轮仅改 grow_state.json/log，见提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'`。✔

## 遗留问题

1. **place 页数 394（不变）**：EVV5 未建页。registry 全库 1462，unknown 0。
2. **下轮 R194 = NEW1**：since_evv5=0<10、since_discover=1<10、queue(place)=3>0 → §3(7) NEW1。
   建 **The Mercy**（mercy-river，MI×168，Lincoln Island 主河），建前文件系统查重（mercy-river/the-mercy/mercy）+ 抽样 ≥5 solid。
3. **R194+ 建序**：The Mercy → Jacamar Wood → Far West（R192 discover 队列 3 项），3 项后 R197 须再 SCN28。
4. **Far West 混指剔除纪律**：建页仅取 MI Lincoln Island 林区指（33 distinctPN），剔 generic American West 21 hits。
5. **featured re-grade DEFERRED**：17 place 页 quality=none（含 add_page 回填缺失的 tristan-da-cunha）；
   full-library re-grade 顺延至 RFC 批审，本 EVV5 仅登记不动作。
6. **散文门债**：37 页 >400（HK-addpage-prose-gate-bypass），DEFERRED；EVV5 未建页。
7. **legacy H1 遗留**：HK-legacy-h1-in-place-pages（150 页），DEFER。
8. **corpus-discover 顺延**：since_corpus=129→130（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
9. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
10. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
    HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
    HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
11. **洲级 America/Europe/Asia 续 HOLD**。
