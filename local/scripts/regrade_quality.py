#!/usr/bin/env python3
"""Distribution-aware quality re-grade — enforces the GROW.spec quality cap.

Conclusion source (closed RFCs, baojie/memex):
  - RFC-munger-0008 (#266): quality distribution cap = premium 5% / featured 5% (<=10% combined).
  - RFC-hitchhiker-0009 (#481): add_page.py auto-backfill bypasses that cap in the engine's
    write path, inflating featured to ~90%+. Fix = a one-time (and periodic) per-wiki
    '--regrade-to-distribution' DATA operation: rank entity pages by quality_score, keep only
    the top slice as featured, everyone else standard (structural basic/stub preserved).

This local script implements that at the wiki-data layer (the engine grader is read-only).
Because add_page re-backfills 'featured' on every new page, RE-RUN THIS after each GROW build
round (add_page -> build_registry -> this script -> build_registry) to hold the cap.

premium stays image-gated (0 here, no entity page has images), so the whole 10% budget is
spent on featured's own 5% line -> top 5% by score.

Usage:
  python3 local/scripts/regrade_quality.py            # dry-run (prints target distribution)
  python3 local/scripts/regrade_quality.py --apply    # write frontmatter quality
Then: python3 "$MEMEX_ROOT/wiki/scripts/build_registry.py" docs/wiki/pages
"""
import sys, json, math
from pathlib import Path

MEMEX = Path.home() / 'memex'
sys.path.insert(0, str(MEMEX / 'wiki' / 'scripts'))
import compute_quality as cq  # engine grader (read-only import)

APPLY = '--apply' in sys.argv
FEATURED_PCT = 0.05                       # munger-0008 featured cap
ENTITY_EXCLUDE = {'chapter', 'overview', 'list'}
FM_RE = cq.FRONTMATTER_RE

reg = json.load(open('docs/wiki/pages.json'))['pages']
PATHMAP = {p.stem: p for p in Path('docs/wiki/pages').rglob('*.md')}  # buckets strip hyphens
rows = []
for slug, v in reg.items():
    if v.get('type') in ENTITY_EXCLUDE:
        continue
    p = PATHMAP.get(slug)
    if p is None or not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    m = FM_RE.match(text)
    if not m:
        continue
    import yaml
    front = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    rows.append({'slug': slug, 'path': p, 'text': text,
                 'struct': cq.compute_level(front, body),
                 'score': cq.compute_quality_score(front, body),
                 'cur': v.get('quality')})

N = len(rows)
n_featured = math.ceil(N * FEATURED_PCT)
rows.sort(key=lambda r: (-r['score'], r['slug']))
featured_slugs = {r['slug'] for r in rows[:n_featured]}

from collections import Counter
final = {}
for r in rows:
    if r['slug'] in featured_slugs and r['struct'] in ('featured', 'premium', 'standard'):
        final[r['slug']] = 'featured'
    elif r['struct'] in ('featured', 'premium'):
        final[r['slug']] = 'standard'      # below cutoff -> cap to standard
    else:
        final[r['slug']] = r['struct']     # keep structural standard/basic/stub

print(f'entity pages: {N} | featured target (top {FEATURED_PCT:.0%}): {n_featured}')
print('BEFORE:', dict(Counter(r['cur'] for r in rows)))
print('AFTER :', dict(Counter(final.values())))
print(f'featured score band: {rows[n_featured-1]["score"]}..{rows[0]["score"]}')
print(f'pages changing grade: {sum(1 for r in rows if r["cur"] != final[r["slug"]])}')

if APPLY:
    wrote = 0
    for r in rows:
        new_text, ch = cq.update_frontmatter(r['text'], final[r['slug']])
        if ch:
            r['path'].write_text(new_text, encoding='utf-8'); wrote += 1
    print(f'APPLIED: wrote {wrote} files (now run build_registry.py)')
else:
    print('DRY-RUN (pass --apply to write)')
