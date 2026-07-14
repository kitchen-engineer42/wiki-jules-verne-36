// WIKI_LANG = en
export const FIELD_LABELS = {
  label: 'Name', description: 'Description', born: 'Born', died: 'Died',
  nationality: 'Nationality', affiliation: 'Affiliation', field: 'Field',
  chapter: 'Chapter(s)', work: 'Work', role: 'Role',
  location: 'Location', vessel: 'Vessel', inventor: 'Inventor',
};
export const INFOBOX_SKIP = new Set(['id', 'type', 'quality', 'tags', 'coords', 'aliases']);
export const FIELD_GROUPS = [
  { label: 'Overview', fields: ['label', 'description', 'born', 'died', 'nationality'] },
  { label: 'In the Works', fields: ['work', 'role', 'chapter'] },
  { label: 'Details', fields: ['affiliation', 'field', 'location', 'vessel', 'inventor'] },
];
