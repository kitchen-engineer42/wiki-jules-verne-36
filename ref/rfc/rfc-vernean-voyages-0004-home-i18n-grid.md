# RFC-vernean-voyages-0004: home plugin expand/collapse button hardcodes Chinese + expanded-grid blank cell (RFC-memex-0048 regression)

- **Status**: proposed (filed)
- **Date**: 2026-07-21
- **Issue**: baojie/memex#555
- **Source wiki**: vernean-voyages (Vernean Voyages Wiki — `WIKI_LANG=en`)
- **Wiki repo**: https://github.com/kitchen-engineer42/wiki-jules-verne-36
- **Target**: `wiki/public/plugins/home/index.js`, `wiki/public/plugins/i18n/strings.js`, `wiki/public/css/home.css`
- **Related (conclusions this regresses)**:
  - RFC-memex-0048 — home section expand/collapse feature (the code that introduced both defects)
  - RFC-memex-0073 (#423, CLOSED) — engine HTML templates must not hardcode Chinese; wire into i18n
  - RFC-memex-0077 (#367, CLOSED) — homepage expand-grid fix + DOM/CSS regression tests
  - RFC-sudongpo-0013 (#390, CLOSED) — i18n missing-key backfill + `t()` fallback

---

## Problem

On an English wiki (`WIKI_LANG=en`, `defaultLang='en'`), the home page's per-type "expand/collapse" control has two defects:

**(a) i18n — button label is hardcoded Chinese.** The control renders `展开剩余 N 个` (expand) and `收起` (collapse) regardless of `WIKI_LANG`. It should render English (e.g. `Show N more` / `Show less`).

**(b) Layout — a blank cell appears in the expanded grid.** When a section is expanded, an empty card slot shows in the middle of the grid (the empty tracks in the first grid's last row). Example: Events has `limit=8`; at 5 columns the first grid's last row holds 3 cards + 2 empty tracks, and because the remaining cards render in a *separate* grid below, those tracks stay visibly blank.

Both were introduced by the RFC-memex-0048 expand/collapse feature and regress the already-closed conclusions of #0073 (no hardcoded Chinese) and #0077 (single continuous expand-grid).

## Root cause

`wiki/public/plugins/home/index.js`:

1. **Three hardcoded Chinese literals** bypass the i18n `t()` that is otherwise threaded through `buildHomeBodyHtml`:
   - initial render: `` `...>展开剩余 ${restCount} 个</button>` ``
   - click handler `_onExpandCollapse`: `btn.textContent = '收起'` and `` btn.textContent = `展开剩余 ${btn.dataset.restCount} 个` ``
   - `strings.js` has `collapse`/`expand` but **no count-placeholder key** for "Show N more".
   - `_onExpandCollapse` is a module-level handler with no `core`/`t` in scope.

2. **Two separate sibling grids.** The template emits `<div class="featured-grid">{first N cards}</div>` and, as a *sibling*, `<div class="home-more-cards" hidden>{rest cards}</div>` — each its own `display:grid; auto-fill`. The first grid's partial last row leaves empty tracks that show as the blank cell; the rest cards start a fresh grid instead of flowing into those tracks.

## Proposed change

### 1. `wiki/public/plugins/i18n/strings.js` — add count-placeholder keys (near existing `collapse`/`expand`)

```diff
   collapse:             { zh: '折叠',            en: 'Collapse',      ja: '折りたたむ' },
   expand:               { zh: '展开',            en: 'Expand',        ja: '展開する' },
+  home_show_more:       { zh: '展开剩余 %s 个',  en: 'Show %s more',  ja: '他 %s 件を表示' },
+  home_show_less:       { zh: '收起',            en: 'Show less',     ja: '折りたたむ' },
```

### 2. `wiki/public/plugins/home/index.js` — use `t()`, and render one grid

```diff
+// captured in init() so the document-level click handler can translate labels
+let _core = null;
 function init(core) {
+  _core = core;
   ...
 }

 function _onExpandCollapse(e) {
   ...
-  const grid = header.nextElementSibling;                 // .featured-grid
-  const moreCards = grid?.nextElementSibling;             // .home-more-cards
+  const grid = header.nextElementSibling;                 // .featured-grid
+  const moreCards = grid?.querySelector(':scope > .home-more-cards');
   if (!moreCards || !moreCards.classList.contains('home-more-cards')) return;
   const expanded = btn.getAttribute('aria-expanded') === 'true';
+  const t = k => _core?.t?.(k) ?? k;
   if (!expanded) {
     moreCards.removeAttribute('hidden');
     btn.setAttribute('aria-expanded', 'true');
-    btn.textContent = '收起';
+    btn.textContent = t('home_show_less');
   } else {
     moreCards.setAttribute('hidden', '');
     btn.setAttribute('aria-expanded', 'false');
-    btn.textContent = `展开剩余 ${btn.dataset.restCount} 个`;
+    btn.textContent = t('home_show_more').replace('%s', btn.dataset.restCount);
     ...
   }
 }

 function buildHomeBodyHtml(bookCardsHtml, sections, totalPages, t = k => k) {
   ...
-    const moreBtn = restCount
-      ? `<button type="button" class="home-more-btn" aria-expanded="false" data-rest-count="${restCount}">展开剩余 ${restCount} 个</button>`
-      : '';
-    const moreSection = restCount
-      ? `<div class="home-more-cards" hidden>${restHtml}</div>`
-      : '';
+    const moreBtn = restCount
+      ? `<button type="button" class="home-more-btn" aria-expanded="false" data-rest-count="${restCount}">${escapeHtml(t('home_show_more').replace('%s', restCount))}</button>`
+      : '';
     return `<div class="home-section-header"> ${titleHtml} ${subHtml} ${moreBtn} </div>
-      <div class="featured-grid">${cardsHtml}</div>
-      ${moreSection}`;
+      <div class="featured-grid">${cardsHtml}${restCount ? `<span class="home-more-cards" hidden>${restHtml}</span>` : ''}</div>`;
   }).join('');
```

### 3. `wiki/public/css/home.css` — make the "rest" wrapper transparent to the grid

```diff
-.home-more-cards {
-  display: grid;
-  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
-  gap: 1em;
-  margin: -0.8em 0 1.8em;
-}
-.home-more-cards[hidden] { display: none; }
+.home-more-cards { display: contents; }
+.home-more-cards[hidden] { display: none; }
```

With `display:contents`, the rest cards become direct children of the single `.featured-grid`; featured + rest fill one continuous grid, so the last row reflows and no blank track remains. `%s` substitution follows the codebase's existing pattern.

## Test (per #0077)

DOM/CSS regression: for a section with `limit` not a multiple of the column count, assert the expanded grid has no empty track between the last "featured" card and the first "rest" card, and that the button label equals `t('home_show_more'|'home_show_less')` for `lang ∈ {en, zh, ja}`.

## Scope / non-goals

- Home plugin only. Does not touch grading, data, or other plugins.
- Keeps `collapse`/`expand` keys as-is (used elsewhere); adds two count-aware keys rather than overloading them.
