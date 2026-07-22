---
date: 2026-07-21
type: maintenance
scope: pn-citation rendering
severity: high
status: RESOLVED for this wiki via local shadow plugin (engine widening deferred by team — RFC #562 closed, out of current scope)
reporter: maintainer
---

# 调查+修复：PN 引注渲染为纯文本（约 81% 页面不成链）

> 摘要给维护者直接查阅。TL;DR：**不是今天引擎更新引起的**；是 2026-05-26 一个引擎提交把 PN 首段正则从「1–4 位」收窄成「恰好 3 位」，导致本 wiki 大量 2 位（MI/SC/OC…）与 4 位（TTLU/EHLA/DSCF/AWED/DOSE）卷号的引注不再成链。本地预览已修；生产需引擎打补丁（已提 RFC）。

## 现象

- `(VVV-NNN-PPP)` 行内引注在约半数页面渲染为**纯文本**、不可点击（captain-nemo 等）。
- captain-nemo 引 `TTLU`（4 位）与 `MI`（2 位）卷号——两者皆不成链。

## 根因（确诊）

引擎前端插件 `$MEMEX_ROOT/wiki/public/plugins/pn-citation/index.js` 硬编码首段为**恰好 3 位**：

```js
const _FIRST = '[A-Za-z0-9]{3}';                                  // line 23
const _CH_ID = '(?:[A-Za-z0-9]{3}-[A-Za-z0-9]{3,4}|[A-Za-z0-9]{3})'; // line 26
```

本 wiki 为多作品合集，卷号 VVV 为 **1–4 位**（LAW §三）。故仅 3 位卷号（ACH/JCE/FEM/FWB/ASC/SC2/WAI）成链；2 位与 4 位全部落为纯文本。

### 这是一次回归（非今日引擎更新所致）

`git -C ~/memex log` 于 `wiki/public/plugins/pn-citation/index.js`：

| commit | date | 说明 |
|--------|------|------|
| `07f8d34` | 2026-05-25 | 实现 RFC-buffett-0001：首段 `[A-Z][A-Z0-9]{0,3}`（**1–4 位**，匹配 TTLU/MI）|
| **`474c2c4`** | **2026-05-26** | **「PN 格式规范明确化」把首段收窄为 `[A-Z0-9]{3}`（恰好 3 位）——回归点** |
| `d8c8d6f` | 2026-05-28 | 首段加小写支持，**仍保留 {3}** |
| `1ef987d` | 2026-05-30 | NNN 放宽为字母，**仍保留 {3}** |

- 该文件自 2026-05-30 起未再改；**全仓库无 2026-07-21（今日）的提交**。故「今日更新引擎」既非诱因也未修复本 bug。
- captain-nemo「以前是对的」属实——**正确渲染止于 2026-05-26 之前**（`474c2c4` 之前），与您的记忆一致。

## 影响面（2026-07-21 实测）

- 词条页 **543 / 667（81.4%）** 至少含 1 条非 3 位卷号引注 → 纯文本。
- 全部行内引注宽度直方：宽 2 = 3449、宽 3 = 1532（唯一成链）、宽 4 = 1153 → **约 75% 引注不成链**。
- 无构建期预渲染可利用：成链纯客户端（`onAfterRender`），重跑 `publish.sh`/`build_registry.py` **无效**，须改插件 JS。

## 修复

### 唯一根治（本地+生产）：引擎两行补丁

`$MEMEX_ROOT/wiki/public/plugins/pn-citation/index.js`：

```diff
- const _FIRST = '[A-Za-z0-9]{3}';                                   // line 23
+ const _FIRST = '[A-Za-z0-9]{1,4}';
- const _CH_ID = '(?:[A-Za-z0-9]{3}-[A-Za-z0-9]{3,4}|[A-Za-z0-9]{3})';  // line 26
+ const _CH_ID = '(?:[A-Za-z0-9]{1,4}-[A-Za-z0-9]{3,4}|[A-Za-z0-9]{1,4})';
```

- 其余正则（`RE_PN_TAG`/`RE_CITATION_PLAIN`/`RE_CITATION_WIKILINK`）内插 `_CH_ID`，自动继承。
- Node 验证 1/2/3/4 位卷号（`A-001-002`/`MI-057-137`/`ACH-003-012`/`TTLU-010-057`/`EHLA-020-005`/`DOSE-002-008`）均正确捕获 `nnn=VVV-NNN`、`ppp=PPP`；`>4` 位不误匹配；`(20KL-001-007]` 仍拒（] 不在闭括号类）。超集变更，3 位旧码全兼容，低风险。
- 生产（Cloudflare Pages）经 CDN `baojie.github.io/memex/dist/plugins/` 加载，故引擎改后须**重建 dist**。
- 已提 **RFC-vernean-voyages-0003 → baojie/memex#562**（含 RFC-buffett-0001 回归证据）。姊妹 RFC-0001（`pn_structure_verify`）/RFC-0002（`build_sentence_index`）同根因，建议同批修。

### 已就地生效（仅 localhost 预览）：本地影子插件

- 新增 `docs/wiki/plugins/pn-citation/index.js`：引擎插件逐字副本 + 仅改上述两行（标 `LOCAL-FIX`）+ 头注。
- `serve.js` 先解析 `docs/wiki` 根、再回退引擎，故 localhost:1828 预览即用修正版；`curl localhost:1828/plugins/pn-citation/index.js` 已返回本地影子。**浏览器硬刷新**（清缓存）即见 captain-nemo 等 PN 成链。
- **不修生产**：非 localhost 主机 `index.html` 把 `@wiki/plugins/` 重映射到 CDN，绕过本地影子。
- **善后**：引擎修复 + CDN dist 重建后，请**删除** `docs/wiki/plugins/pn-citation/`（避免影子长期遮蔽引擎新版）。

## 验证清单

- [x] 根因定位到 `474c2c4`（git pickaxe/blame）
- [x] 确认非今日回归（仓库无 2026-07-21 提交）
- [x] 影响面量化（543/667 页；75% 引注）
- [x] 本地影子插件生效（curl 验证 + node 正则验证）
- [x] 引擎补丁 node 验证（1/2/3/4 位）
- [x] RFC-0003 更新并提交 issue #562
- [x] **团队裁决（2026-07-21）**：多卷（1–4 位 VVV）宽度不在当前引擎 scope，**推迟至后续引擎版本**；RFC #562 已 closed。
- [x] **本 wiki 结论**：本地影子插件即为**最终修复**，保留至引擎日后自行放宽正则（届时删影子）。localhost 预览已成链。
- [ ] （远期，待引擎版本）引擎放宽 `{3}→{1,4}` + CDN dist 重建 → 删除本地影子
