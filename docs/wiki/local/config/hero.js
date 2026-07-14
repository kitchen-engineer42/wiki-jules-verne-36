// WIKI_LANG = en
export const EYEBROW   = 'Jules Verne · Voyages Extraordinaires';
export const TITLE     = 'Vernean Voyages Wiki';
export const TAGLINE   = 'The people, places, and machines of Jules Verne\u2019s extraordinary journeys.';
export const DOC_TITLE = 'Vernean Voyages Wiki — A companion to the Collected Works of Jules Verne';
export const SEARCH_PLACEHOLDER     = 'Search entries…';
export const SEARCH_PLACEHOLDER_FTS = 'Full-text search…';
// BOOK_DISPLAY: 首页书籍卡片渲染风格
//   'card'  — 单卷 wiki，每本书显示为大卡片
//   'strip' — 多卷 wiki（书信集、全集），每本书显示为横条
// 36 部作品 → 多卷 → strip
export const BOOK_DISPLAY = 'strip';
// BOOK_META 在 Phase 3 确定作品清单后于 Phase 4/5 补全为逐卷条目。
export const BOOK_META = [
  { label: 'Collected Works', subtitle: '36 novels and short stories', min: 1, max: 999 },
];
