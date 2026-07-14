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
// BOOK_META：35 部作品逐卷条目（min/max 为 book_seq 范围，Phase 4 生成）。
export const BOOK_META = [
  { label: 'Twenty Thousand Leagues Under the Sea', subtitle: '47 chapters', min: 1, max: 47 },
  { label: 'A Journey to the Center of the Earth', subtitle: '45 chapters', min: 48, max: 92 },
  { label: 'Around the World in Eighty Days', subtitle: '37 chapters', min: 93, max: 129 },
  { label: 'The Mysterious Island', subtitle: '62 chapters', min: 130, max: 191 },
  { label: 'From the Earth to the Moon', subtitle: '28 chapters', min: 192, max: 219 },
  { label: 'Round the Moon', subtitle: '23 chapters', min: 220, max: 242 },
  { label: 'A Voyage in a Balloon', subtitle: 'short work', min: 243, max: 243 },
  { label: 'Doctor Ox\'s Experiment', subtitle: '17 chapters', min: 244, max: 260 },
  { label: 'Master Zacharius', subtitle: '5 chapters', min: 261, max: 265 },
  { label: 'A Drama in the Air', subtitle: 'short work', min: 266, max: 266 },
  { label: 'A Winter Amid the Ice', subtitle: '16 chapters', min: 267, max: 282 },
  { label: 'Ascent of Mont Blanc', subtitle: 'short work', min: 283, max: 283 },
  { label: 'An Antarctic Mystery', subtitle: '26 chapters', min: 284, max: 309 },
  { label: 'Dick Sand: A Captain at Fifteen', subtitle: '38 chapters', min: 310, max: 347 },
  { label: 'Eight Hundred Leagues on the Amazon', subtitle: '40 chapters', min: 348, max: 387 },
  { label: 'Facing the Flag', subtitle: '18 chapters', min: 388, max: 405 },
  { label: 'Five Weeks in a Balloon', subtitle: '44 chapters', min: 406, max: 449 },
  { label: 'Godfrey Morgan', subtitle: '22 chapters', min: 450, max: 471 },
  { label: 'The Adventures of Captain Hatteras', subtitle: '58 chapters', min: 472, max: 529 },
  { label: 'In Search of the Castaways', subtitle: '66 chapters', min: 530, max: 595 },
  { label: 'Michael Strogoff', subtitle: '34 chapters', min: 596, max: 629 },
  { label: 'Off on a Comet', subtitle: '45 chapters', min: 630, max: 674 },
  { label: 'Robur the Conqueror', subtitle: '23 chapters', min: 675, max: 697 },
  { label: 'The Adventures of a Special Correspondent', subtitle: '27 chapters', min: 698, max: 724 },
  { label: 'The Blockade Runners', subtitle: '10 chapters', min: 725, max: 734 },
  { label: 'The Fur Country', subtitle: '47 chapters', min: 735, max: 781 },
  { label: 'The Master of the World', subtitle: '18 chapters', min: 782, max: 799 },
  { label: 'The Pearl of Lima', subtitle: '9 chapters', min: 800, max: 808 },
  { label: 'The Secret of the Island', subtitle: '20 chapters', min: 809, max: 828 },
  { label: 'The Survivors of the Chancellor', subtitle: '57 chapters', min: 829, max: 885 },
  { label: 'The Underground City', subtitle: '19 chapters', min: 886, max: 904 },
  { label: 'The Waif of the Cynthia', subtitle: '22 chapters', min: 905, max: 926 },
  { label: 'Ticket No. 9672', subtitle: '20 chapters', min: 927, max: 946 },
  { label: 'Topsy Turvy', subtitle: '21 chapters', min: 947, max: 967 },
  { label: 'In the Year 2889', subtitle: 'short work', min: 968, max: 968 },
];
