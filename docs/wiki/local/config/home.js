// WIKI_LANG = en
export const CORE_FEATURED = [];
export const PREFACE_IDS   = [];
export const APPENDIX_IDS  = [];
export const HOME_SECTIONS = [
  { label: 'Characters', tag: null, type: 'character', featuredOnly: false, limit: 8 },
  { label: 'Places',     tag: null, type: 'place',     featuredOnly: false, limit: 6 },
  { label: 'Technology', tag: null, type: 'technology', featuredOnly: false, limit: 6 },
];
export const SKIP_TYPES = new Set(['chapter', 'list', 'overview']);
// ⚠️ DISCLAIMER is no longer rendered by the engine (the <footer> already contains license info).
//    Kept as export only for compatibility; new projects may delete or leave empty.
