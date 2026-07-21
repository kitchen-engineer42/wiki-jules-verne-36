---
date: 2026-07-21
type: maintenance
scope: quality-distribution
trigger: user bug report (quality bloat >90% featured)
---

# 维护：质量分布 re-grade（featured 失控 → 5% cap）

## 背景

用户报告：除 stub 外，全库 >90% 词条页标为 `quality: featured`，明显注水。

## 结论依据（baojie/memex 已闭环 RFC）

- **RFC-munger-0008（#266, CLOSED）**：GROW.spec 质量分布上限 = premium 5% / featured 5%（合计 ≤10%）。featured 应表「搜索热度前 5–10%」的甄别档。
- **RFC-hitchhiker-0009（#481, CLOSED）**：`add_page.py._backfill_quality` 在**建页写入路径**绕过该 cap——`compute_level` 的 featured 判据是纯结构门（h2≥3 且 PN≥3 且散文≥200），几乎所有模板页轻松达标 → 全库 featured 单调累积至 90%+。修复含一次性 `--regrade-to-distribution`：按 `quality_score` 排序，仅前 5%/5% 置 premium/featured，其余落 standard/basic（存量修复属**各 wiki 数据操作**）。

引擎（`$MEMEX_ROOT/wiki/scripts/compute_quality.py`）为只读，尚未实装该 cap；故在**数据层**执行 re-grade。

## 操作

`local/scripts/regrade_quality.py`（复用引擎 `compute_quality.compute_quality_score` / `compute_level` / `update_frontmatter`，只读 import）：
- 分母：词条页（type ∉ {chapter, overview, list}），666 页。
- 按 `quality_score` 降序，前 5%（ceil(0.05×666)=34）置 **featured**；premium 仍 image-gated → 0（无词条页带图）；其余结构档封顶 standard（featured/premium→standard，保留结构 basic/stub）。

## 结果

| | featured | standard | 备注 |
|--|----------|----------|------|
| BEFORE | 618（+25 无档 +20 standard）| — | ~93% featured |
| **AFTER** | **34（5.1%）** | 632 | 逾 cap 修复 |

- 变更 614 页（仅改 frontmatter `quality:` 行；25 张原无档页顺带补 `quality` 并去 body 首空行，纯 cosmetic）。
- featured score band 61–66。per-type featured（全局 top-5%，非按类均摊）：technology 7/20、character 16/112、event 6/64、work 3/33、organization 3/15、place 2/422——最富引注页（多为 mine→verify 高 PN 页）胜出，符合「搜索热度前 5%」语义。
- `build_registry.py` 重建 pages.json 复核 5.1%。

## 后续（防复膨）

引擎 add_page 每建新页仍会回填 featured（#481 缺口未在引擎实装）。**GROW 每建页轮末追加**：`add_page → build_registry → local/scripts/regrade_quality.py --apply → build_registry`，以持守 cap。新页若 quality_score 进全局 top-34 则自然保留 featured，否则落 standard。

## 未决（引擎侧，需 RFC / 用户）

- 引擎 `add_page._backfill_quality` 接入分布门（#481 提案第 1 条）为根治；本地 re-grade 仅数据层兜底。
- `compute_level` premium 判据要求 has_image，词条页无图 → premium 永 0；若欲启用 premium 档需另议（#527 tier 一致性）。
