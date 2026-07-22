# RFC-vernean-voyages-0003: Widen VVV segment regex to `{1,4}` in pn-citation (and sibling components)

- **Status**: CLOSED / deferred (2026-07-21) — team decision: multi-volume (1–4 char VVV) widening is
  out of current engine scope, deferred to a later engine version. **Resolution for this wiki: the local
  shadow plugin (`docs/wiki/plugins/pn-citation/index.js`) is the accepted fix and stays until the engine
  eventually widens the regex.** Kept here as the record of the root-cause analysis.
- **Date**: 2026-07-13 (filed + closed 2026-07-21)
- **Issue**: baojie/memex#562 (closed)
- **Source wiki**: vernean-voyages
- **Wiki repo**: https://github.com/kitchen-engineer42/wiki-jules-verne-36
- **Target**: `wiki/public/plugins/pn-citation/index.js` (+ sibling fixes in `pn_structure_verify`, `build_sentence_index`)
- **Regression of**: RFC-buffett-0001 (`07f8d34`, VVV 1–4 char support) — collapsed by `474c2c4` (2026-05-26)

---

## Problem

The Vernean Voyages Wiki is a 35-work anthology. Per `LAW.md §三`, its PN scheme uses a
three-segment volume format `VVV-NNN-PPP`, where **VVV is a work code of 1–4 chars**
(regex `[A-Za-z0-9]{1,4}`). Real codes in use include `TTLU` (4 chars, *Twenty Thousand
Leagues Under the Sea*), `MI` (2), `WC` (2), `ACH` (3).

The shared `pn-citation` wiki-jules-verne-36 plugin hardcodes a **3-char** first segment:

```js
const _FIRST = '[A-Za-z0-9]{3}';
const _CH_ID = '(?:[A-Za-z0-9]{3}-[A-Za-z0-9]{3,4}|[A-Za-z0-9]{3})';
const RE_CITATION_PLAIN = new RegExp(`([（(])(${_CH_ID})-([A-Za-z0-9]{3,4})([）)])`, 'g');
```

As a result, an inline citation such as `(TTLU-013-004)` **fails to match** and renders as
plain text. Only 3-char codes (e.g. `ACH`, `JCE`, `FEM`) link correctly.

**Live impact (measured 2026-07-21):** **543 / 667 entity pages (81.4%)** contain ≥1 citation
whose VVV is not exactly 3 chars. Of all inline citations: width-2 = 3449, width-3 = 1532
(the only ones that render), width-4 = 1153 — i.e. **~75% of citations render as plain text**.
`captain-nemo` (cites `TTLU` and `MI`) is a representative case reported by the maintainer.

## Root cause

`_FIRST` / `_CH_ID` assume exactly 3 chars for the volume code. **This is a regression, not a
new gap.** Git history of `pn-citation/index.js`:

- `07f8d34` (2026-05-25, *implement RFC-buffett-0001: VVV 卷号前缀 PN 格式扩展*) introduced a
  **flexible** first segment `[A-Z][A-Z0-9]{0,3}` (1–4 chars) that matched `TTLU` (4) and `MI` (2).
- `474c2c4` (2026-05-26, *feat(pn): PN 格式规范明确化*) **collapsed** it to `[A-Z0-9]{3}`
  (exactly 3), silently dropping 1/2/4-char VVV support.
- `d8c8d6f` (2026-05-28) added lowercase, `1ef987d` (2026-05-30) widened NNN — both **kept `{3}`**.
- No commit since 2026-05-30 touches these lines; the repo has **zero commits dated 2026-07-21**,
  so today's engine update neither caused nor fixed this. Correct rendering last existed **before
  2026-05-26** — consistent with the maintainer's recollection that Captain Nemo "used to be correct".

This is one of **three** engine components hardcoding a 3-char VVV, all sharing the root cause:

| Instance | Component | Layer | Impact |
|----------|-----------|-------|--------|
| RFC-0001 | `pn_structure_verify` | verification (report only) | false negatives for non-3-char VVV |
| RFC-0002 | `build_sentence_index` | data index | corrupts sentence/search index for non-3-char VVV |
| **RFC-0003** | `pn-citation` plugin | wiki-jules-verne-36 render | non-3-char citations render as plain text |

The `VVV-NNN-PPP` spec (`ref/spec/data-pn.md`) permits variable-width VVV; the
implementations do not honor it.

## Proposed change

Replace the hardcoded `{3}` on the **VVV segment only** with `{1,4}` across all three
components. Concretely, in `pn-citation/index.js`:

```js
const _FIRST = '[A-Za-z0-9]{1,4}';
const _CH_ID = '(?:[A-Za-z0-9]{1,4}-[A-Za-z0-9]{3,4}|[A-Za-z0-9]{1,4})';
```

NNN and PPP remain `{3,4}` / `{3}` as today. Apply the equivalent widening in
`pn_structure_verify` and `build_sentence_index`. Add a regression fixture with a 4-char
VVV (`TTLU-013-004`) so this class of defect is caught in CI.

## Compatibility

The change is a superset: every currently-matching 3-char code still matches. No existing
single-book wiki (3-char or numeric VVV) is affected. Low risk.

## Local stopgap (already applied in the sub-wiki, localhost only)

To restore the **localhost preview** immediately, the sub-wiki ships a local shadow of the
plugin at `docs/wiki/plugins/pn-citation/index.js` (a verbatim copy of the engine plugin with
only the two `{3}→{1,4}` lines changed). `serve.js` resolves the `docs/wiki` root **before** the
engine fallback, so the local preview renders every VVV width correctly. **This does NOT fix
production**: for non-localhost hosts `index.html` remaps `@wiki/plugins/` to the CDN
(`baojie.github.io/memex/dist/plugins/`), which still serves the buggy engine build. The shadow
should be **deleted** once the engine fix lands and the CDN `dist` is rebuilt.

## Notes

- No build-time fix exists: linkification is purely client-side (`onAfterRender`); re-running
  `publish.sh` / `build_registry.py` cannot fix it — the plugin JS must change.
- Sibling RFC-0001 / RFC-0002 cover the same root cause in the verification and index
  layers; they should be fixed together in one upstream change.
