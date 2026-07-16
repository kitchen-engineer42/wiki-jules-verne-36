---
round: 96
date: 2026-07-15
phase: "2.1-B"
gene: NEW1
pages: [china, russia, india, brazil, scotland]
result: success
---

## 执行摘要

R96 决策矩阵（读 R95 末计数器：queue=12≥10、since_evv5=1、since_discover=0、discover_streak_low=0、since_corpus=32）。矩阵字面：priority 3 不触发（queue≥10 且 since_discover=0），但 since_corpus=32≥30 → **priority 3.5 corpus-discover** 名义触发。然 R95 表层 discover 刚跑（since_discover=0）、且 queue 有 12 个已核可建候选积压——正属既定「消化可建积压优先于空转复扫」边缘情形（同 R90/R92 override）。**人工判定转 NEW1** 消化国级候选，corpus-discover 顺延至积压排空后再评。

本轮建 5 国级页，取 R95 surface 的最高 distinctPN + 主源最集中者：China（ASC:56 大铁路穿华）、Russia（MS:49 Michael Strogoff）、India（AWED:28 环游印度）、Brazil（EHLA:39 亚马逊之国）、Scotland（SC:19 Glenarvan 故乡）。各聚焦主作确指句避泛写。place 页数 225→230，registry 1293→1298，unknown 0。剩 5 国级候选（Peru/Sweden/Japan/Egypt/Ceylon）留 R97。

## 页面处理记录

| slug | rev | book(主作) | rof | 页内引注 distinctPN | over-400 修复 | 备注 |
|------|-----|------|-----|------|------|------|
| china | f5khzk | The Adventures of a Special Correspondent | real | 9 (ASC-001/002/003/004/005×2/006/008) | 无 | Grand Transasiatic 东终点/Bombarnac 目的地 Pekin |
| russia | sRNgL3 | Michael Strogoff | real | 9 (MS-003×3/004×2/005×3) | 无（Overview 段 435 拆 2） | Strogoff 信使穿越之帝国 |
| india | B8JInf | Around the World in Eighty Days | real | 9 (AWED-005/006/009/010×3/011×2) | 无（Overview 段 421 拆 2） | Fogg 三日横越之英属印度 |
| brazil | AkAABr | Eight Hundred Leagues on the Amazon | real | 10 (EHLA-001×3/002/003/004×2/005×2/007) | 无（Overview 段 456 拆 2） | Amazon 所润之国/Garral 家园 |
| scotland | oai6WN | In Search of the Castaways | real | 10 (SC-002/003/004×2/008/023/032×2/036/038) | 无（Geography 段 415 拆 2） | Glenarvan 高地故乡/Duncan 启航地 |

## EXIT-GATE 检查

- G4：5 页均经 `add_page.py --author grow` 建立，未直写 ✓
- place-schema：4 H2 顺序正确，frontmatter 8 字段齐全，5 页全 real ✓
- GROW-JUDGMENT-R50（页内 distinctPN ≥5）：9/9/9/10/10，全部达标 ✓
- 国级泛写规避：各页聚焦主作确指句——China ASC 大铁路穿华（Kara Koum/Gobi/Pekin 包裹案）；Russia MS 信使穿越（Czar 谕令/Ogareff 叛乱/Bokhara）；India AWED 三日横越（reversed triangle/Bombay-Calcutta 铁路）；Brazil EHLA 亚马逊之国（Capitaes do Mato/Solimaës/Guiana 边界）；Scotland SC Glenarvan 故乡（Dundee/Tweed/Malcolm Castle）✓
- 跨源 book 惯例：各取主源最集中之作定 book（ASC/MS/AWED/EHLA/SC 均单作 ≥19）✓
- ≤400 字门：建前 4 段 over-400（russia 435/india 421/brazil 456/scotland 415）已拆分，复验 0 超标 ✓
- 前向红链：0（China↔Russia 同批互链于 registry 重建后解析；Gobi/Tjon/Pekin/Siberia/Ural Mountains/Suez/Bombay/Calcutta/Amazon/Province of Amazones/Manaos/South America/Patagonia/Australia/New Zealand 均经 pages.json 核验存在）✓
- 交叉核既有页：5 slug/label 均无既有页碰撞（仅 Iceland 既建，5 国均无页）✓
- 排除清单：commit 前核 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` = clean

## 六步状态机（R96→R97，NEW1）

- current_round 96→97
- type_round 67→68
- rounds_since_last_evv5 1→2
- rounds_since_last_discover 0→1
- discover_streak_low 0（不变）
- rounds_since_last_corpus_discover 32→33
- last_updated_round 96→97

## 遗留问题

- **R97 预测 = NEW1（优先级 6）**：R96 末 queue=7<10（矩阵字面 priority 3 SCN28，since_discover=1 非 0）。但同 R90/R92 情形：queue 尚有 5 个可建国级候选（Peru/Sweden/Japan/Egypt/Ceylon）+ 2 hold；since_discover=1 刚经 R95 高产 surface。**建议 R97 续 NEW1** 消化剩余国级：Peru（EHLA:19/PL:13）、Sweden（WC:13）、Japan（AWED:11/TTLU:9）、Egypt（跨源 26，主源待复核）、Ceylon（TTLU:13 采珠场）。各聚焦主作确指句。
- **Egypt 主源复核**：DSCF:7/TTLU:6/OC:3 分散无单作 ≥10，建页时择确指句最集中之作定 book（倾向 TTLU 或 DSCF 沙漠穿越段）。
- **place 广度**：国级层已建 5，尚余 5 + England/France（待评城市页密集问题）+ Denmark/Turkey/Persia/Arabia 中候选。CLOSE 远未到。消化完国级后 corpus-discover（since_corpus 将 ≥33）可深扫查残余单作候选。
- **EVV5 下次约 R105**：since_evv5 R96 末=2。
- **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补交叉核，R97+ 附带（注：本 R96 已建 brazil，Lima=Peru 首府或与 lima 页相关，补核时一并核 Peru 建页后是否与 lima 城市页重复覆盖）。
