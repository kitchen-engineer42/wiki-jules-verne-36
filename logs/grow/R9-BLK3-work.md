---
round: 9
date: 2026-07-15
type_round: 8
phase: "2.1"
current_type: work
gene: BLK3
pages: []
result: accept
---

# GROW 2.1-B · R9 · BLK3 · work — 类型完成 Wikify + 关闭

## 本轮公告

**R9 — Phase 2.1 — BLK3 — work wikify pass + 类型关闭**

work 候选于 R8 耗尽（33/35 闭合），依 §2.1-E「候选耗尽后立即 wikify，不积压到最后」，
本轮执行 BLK3 全库 wikilink 注入，随后关闭 work 类型，`current_type` 转入 `organization`。

> BLK3 不走 2.1-B 决策矩阵（spec §2.1-B 第四步注），由类型耗尽事件触发。

## 执行步骤与结果

### 1. BLK3 wikilink 注入

```
python3 $MEMEX_ROOT/wiki/scripts/butler/bulk_wikilink.py
→ 218 个词条，处理 98 个实体页面
→ 74/98 页修改，新增 312 个链接
```

> **脚本无 `--type` 参数**：`bulk_wikilink.py` 仅支持 `--dry-run` / `--limit`，始终处理全部
> 非 chapter 实体页（spec §2.1-E 的 `--type work` 被静默忽略）。故本次 wikify 实际为**全库实体 pass**，
> 是 work-close wikify 的超集，一次性覆盖 work↔work 互链及既有 Pilot 期各类型页面。幂等，
> 后续类型关闭时重跑不产生重复链接。

### 2. 补录修订历史

`bulk_wikilink.py` 绕过 `record_revision.py`，逐页补录：

```
git diff --name-only HEAD -- docs/wiki/pages/**/*.md | record_revision.py <slug> --author grow
→ 74/74 页补录成功，0 失败
```

### 3. 断链扫描

`scan_wanted_pages.py` **不存在**于本机 memex（spec 已预期此情况）。work 为有限枚举语料，
red-link 勘探对其退化无意义（同 R7/R8 论证），故本轮跳过断链入队，不影响 work 关闭。
断链补全留待各开放类型（organization/place 等）建成后由 2.1-X 前统一处理。

### 4. 重建 registry + backlinks

```
build_registry.py docs/wiki/pages → 1066 pages（pages.json + pages.lite.json）
build_backlinks.py --stats → 覆盖 1034 被引用页，共 2345 条反向链接
```

> 链接密度显著提升（2.1-X 门槛：> 5 条/词条）。Top 被引：lincoln-island 72、granite-house 68、
> captain-nemo 62、nautilus 55。

## 类型关闭 bookkeeping

| 项 | 值 |
|----|-----|
| closed_type | work |
| closed_at_round | 9 |
| final_count（type==work）| 33 |
| evv6_score | null（待 2.1-Z-0 EVV6 全库评审填写）|
| current_type → | organization |
| type_queue → | [technology, place, event, character] |
| 计数器重置 | type_round=0, discover_streak_low=0, rounds_since_last_evv5=0 |

> `current_type` 与 `type_queue` 互斥（本项目 invariant：当前类型不在队列内），关闭时从队首弹出
> organization 作为新 current_type，而非 spec 快照的 `[t for t in queue if t!=closed]`（该式假设当前
> 类型在队列内，与本项目初始化不符）。结果等价：转入队首类型。

## EXIT-GATE 检查（BLK3 仅需 G4）

- [x] G4 记录完整性：本日志 + state 更新；wikify 经 bulk_wikilink + record_revision 补录（无 Write/Edit 旁路）；backlinks/registry 重建

## state 更新

`current_round 9→10`，`rounds_since_last_discover/corpus_discover 7→8`；关闭重置
`type_round→0`、`rounds_since_last_evv5→0`、`discover_streak_low→0`。`current_type work→organization`。
`closed_types` 追加 work 条目。`last_updated_round→10`。

## 遗留问题

1. **work 类型正式关闭**，`final_count=33`。全集 35 部：33 建页 + 2 语义重复弃建（SI=MI-3、VB=DA）。
   evv6_score 待 Phase 2.1 关闭前（2.1-Z-0）EVV6 全库评审回填。
2. **alias 冲突**：`build_registry` 报 `'Robur the Conqueror' → robur-the-conqueror vs robur`
   —— work 页 `robur-the-conqueror` 与 character 页 `robur` 的 label/alias 撞名（LAW §10）。
   Pilot 期既有数据问题，非本轮引入。记入 housekeeping_queue，待 organization/character 类型轮或
   2.1-Z PHQ 统一消歧（work 页 label 更具体，character 页保留 `Robur`）。
3. **scan_wanted_pages.py 缺失**：断链入队工具本机不存在。开放类型建成后需补断链扫描（手动 SCN28 或
   补装脚本），列入 2.1-X 前置。
4. **下一轮 R10 = organization 类型 type_round 0**：`rounds_since_last_discover=8`，未达 10；候选池空
   （organization 尚无候选），预计 priority-3 SCN28 触发首轮 organization 勘探播种候选池。
5. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度三项债务照旧 PARK。
