---
round: 3
date: 2026-07-13
phase: 9
gene: SCN27
type: technology
pages: [albatross, victoria-balloon, the-forward, gun-cotton, ships-compass]
result: accept
---

# R3 — SCN27 technology r2（Phase 9-B 第二轮）

## 执行摘要

technology 类型第二轮。承 EVV5 r1 建议，本轮**换子领域**以验证 schema 对不同技术形态的适应性：r1 建的是大型火炮/弹舱 + 便携仪器，r2 转向**航空/航海载具**并首次引入 **`category=concept`** 抽象实体，覆盖 5 部新作品（RC/FWB/ACH/MI+FEM/DSCF），全部 corpus-grounded（每句有据）：

- **Albatross**（RC，Robur the Conqueror）— 74 具悬浮螺旋桨的重于空气飞行器（aeronef），与 r1 的 [[The Terror]] 呼应 Robur 双机
- **Victoria (balloon)**（FWB，Five Weeks in a Balloon）— Ferguson 的双层氢气球
- **The Forward**（ACH，The Adventures of Captain Hatteras）— 破冰钢艏极地布里格帆船
- **Gun-Cotton / pyroxyle**（FEM + MI）— 火棉/硝化纤维炸药，首个 `category=concept` 页，跨两部作品
- **Ship's Compass**（DSCF，Dick Sand）— 船罗盘及 Negoro 用铁块蓄意偏转磁针的情节核心仪器

每页均达 standard：4 节结构、类型专属 frontmatter 全填、quality=standard；Albatross/Victoria/Forward 引注数 12–13，达 featured 引注量级但档位仍记 standard（与批次一致，留待 EVV 提档）。

引注方法：`corpus_search.py` 定位候选 → 读章节页原文 grep 逐字核验 → 仅采用核验过的引文。

## 页面处理记录

| slug | type | category | 作品(VVV) | 引注数 | PN 来源示例 | quality | QUO7 |
|------|------|----------|-----------|--------|-------------|---------|------|
| albatross | technology | vehicle | RC | 12 | RC-007-007/022/025/026/027/030/031/032/034/035, RC-008-004 | standard | 无问题 |
| victoria-balloon | technology | vehicle | FWB | 13 | FWB-007-002/003/004/008/010/013/016/018/023/027, FWB-041-025/032/058 | standard | 无问题 |
| the-forward | technology | vehicle | ACH | 13 | ACH-001-002/004/008/012/046/047/048/049/052, ACH-016-036, ACH-034-021 | standard | 无问题 |
| gun-cotton | technology | concept | FEM+MI | 8 | MI-030-006/007/008/009/010, FEM-025-002/004/005 | standard | 无问题 |
| ships-compass | technology | instrument | DSCF | 9 | DSCF-010-065/067/068/070/072/089/090/092/094 | standard | 无问题 |

## EVV5 r1 模板应用检查

- **Science & Speculation 常态化**（EVV5 r1 建议）：5 页全部写此节，均以「真实器械/物理 vs 凡尔纳外推」收束（Albatross 纸质机身、气球氢浮力、Forward 极地造船史、火棉真实化学、罗盘磁偏原理），验证该指引在异质子领域仍适用。
- **`category=concept` 压力测试**：gun-cotton 作为抽象物质，Design & Operation 节改述「制法与理化性质」（MI-030-009/010 合成步骤 + MI-030-008 燃点/威力），未出现「无实体参数可引」的空节张力——schema 对 concept 亦可用。待 EVV5 r2 正式评估此适配。
- **段落 ≤400 字**：gun-cotton Role 节按 EVV5 指引拆为三段，避免退出码 8。

## EXIT-GATE 检查

- E（渲染/格式）：QUO7 全部「无问题」；`lint_bucket_structure --fix` 报「分桶结构正常，pages/ 与 history/ 根无散落 .md」。
- 继承 caveat：TTLU 4 字符 VVV 行内引注渲染问题（RFC-0003 parked）；本轮 5 页 VVV 均为 2–4 字符，其中 DSCF/FWB/ACH（3–4 字符）—— DSCF 4 字符与 TTLU 同受影响，数据合法待上游修复；RC/FEM/MI（2–3 字符）渲染正常。
- 完整 E1–E5 出口门在 technology 三轮结束后统一执行。

## 遗留问题

- 跨页 wikilink 目标（[[Robur]]、[[Captain Hatteras]]、[[Gun Club]] 等）多为 want-link，待 character/organization 轮次建页后由 9-C wikify 回填。已建成的交叉链接：Albatross↔The Terror、gun-cotton→Columbiad/Ruhmkorff Apparatus、Victoria→Albatross、the-forward→Captain Hatteras。
- gun-cotton `book` 字段取 FEM（主作品），但内容跨 FEM+MI；单值 book 字段对跨作品 concept 略显局促，记为 EVV6 元反思候选议题。
