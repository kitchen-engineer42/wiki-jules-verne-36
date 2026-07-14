---
round: 19
date: 2026-07-14
phase: 9
gene: SCN27
type: character
pages: [axel, passepartout, fix, ned-land, michel-ardan]
result: pass
---

# R19 — SCN27 character r2（新子领域批次）

## 执行摘要

character 类型 pilot 第二轮（r2），选**非主角子领域**的 5 位角色，重点压 `role` 枚举——narrator（axel）、antagonist（fix）、supporting（passepartout/ned-land/michel-ardan）。r1 五页全为 protagonist，r2 覆盖其余三档。5 页用 r1 精化后的 character-schema（含 wikilink 节 PN 豁免、meta 避 warn 等指引）建成，全部 auto-backfill featured，零 overlap warn。

## 页面处理记录

| 页面 | book | role | first_appearance | 引注数 | 引注 PN | quality |
|------|------|------|------------------|--------|---------|---------|
| axel | Journey to the Center of the Earth | narrator | JCE-001 | 5 | JCE-001-002, JCE-002-004, JCE-019-025, JCE-003-040 | featured |
| passepartout | Around the World in Eighty Days | supporting | AWED-001 | 5 | AWED-001-018/019, AWED-002-004 | featured |
| fix | Around the World in Eighty Days | antagonist | AWED-006 | 6 | AWED-005-013/014, AWED-006-004/016, AWED-007-009 | featured |
| ned-land | Twenty Thousand Leagues Under the Seas | supporting | TTLU-004 | 4 | TTLU-004-007/008/009/011 | featured |
| michel-ardan | From the Earth to the Moon | supporting | FEM-018 | 4 | FEM-018-003/008/038/042 | featured |

## 本轮要点

- **role 枚举全覆盖**：r1（protagonist ×5）+ r2（narrator ×1、antagonist ×1、supporting ×3）= schema 四档 role 均有实例。narrator（axel 第一人称叙述者）、antagonist（fix 误判追捕，属「误判型反派」而非恶意）经建页验证枚举适配无摩擦。
- **affiliation 字段首次填值**：fix 填 `affiliation: Scotland Yard`（r1 五主角均空）。验证 affiliation 非空档——角色有明确组织归属时填写。
- **label 消歧**：fix 语料常以裸名 "Fix" 出现，label 定 "Detective Fix" 避免与普通词碰撞，aliases 收 "Fix"。
- **4-char VVV Note**：passepartout/fix（AWED）、ned-land（TTLU）加 RFC-0003 渲染 Note；axel（JCE）、michel-ardan（FEM）3-char 无需。
- **跨作品引用（正文提及，非跨作品实体）**：michel-ardan 主作品 FEM，Appearances 兼列 [[Round the Moon]]（航程续篇）。此为出场跨作品，非「同一实体分散两作」的跨作品实体，book 单值无争议。
- **wikilink 节 PN 豁免生效**：Relationships/Appearances 均为纯 wikilink，按 r1 精化的 §引文规范不强制 PN，5 页 auto-backfill featured 验证豁免正确。

## EXIT-GATE 检查

r2 建页轮，不做完整 E1–E5。即时核查：
- QUO7 `pn_format_lint.py --fix`：5 页无问题。
- `lint_bucket_structure.py --fix`：分桶正常。
- H2 五节序 5 页遵循 Overview → Role in the Story → Character & Traits → Relationships → Appearances。

## 遗留问题

1. **r3 边缘案例选取**：r3 应取边缘/复杂角色——跨作品角色深化、群像/集体角色、动物角色（如 Top 犬）、身份反转角色、极短出场角色，压 schema 盲点。
2. **featured 引注门表述**：ned-land/michel-ardan 仅 4 引注仍 featured（工具综合判定），schema「≥10」表述与工具判定的差异留 EVV6 裁定。
3. **跨作品实体累计仍 3 例**：本轮无新增跨作品实体。
