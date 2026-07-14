// LocalSettings.js — wiki 本地配置
// 模板位于 $MEMEX_ROOT/docs/dist/LocalSettings.js，复制到 docs/wiki/local/ 后修改。

export const wgSiteName = 'Vernean Voyages Wiki';

// core 插件（plugins.json 中 core: true）始终加载，无需在此列出。
// 非 core 插件需加入此列表才会启用。
export const wgEnabledPlugins = [
  'autolink',
  'pn-citation',
  'footnote',
  'backlinks',
  'sealso',
  'want-button',
  'math',
  'math-array',
  'page-marker',
  'export',
  'semantic-block',
  'semantic-query',
  // 地图插件需专项地理数据，暂不启用：
  // 'place-map', 'route-map', 'geomap',
];
