// hero.config.js — Vernean Voyages 首页英雄区背景
// 视觉隐喻：古董航海图上缓缓航行的光点（凡尔纳的"非凡旅行"航线），
// 配色呼应 paper-light 主题（米色底 + Hetzel 深红 #a02128 航线）。

export function buildHeroBackground() {
  return '<canvas id="hero-canvas" class="hero-cosmos"></canvas>';
}

export function startHeroAnimation(setStop) {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let raf = 0, w = 0, h = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);

  const CRIMSON = 'rgba(160, 33, 40, 0.55)';
  const INK = 'rgba(70, 55, 40, 0.18)';

  // 若干条正弦"航线"，光点沿线漂移
  const routes = Array.from({ length: 5 }, (_, i) => ({
    amp: 18 + i * 10,
    freq: 0.004 + i * 0.0011,
    phase: Math.random() * Math.PI * 2,
    y: 0.18 + i * 0.16,
    speed: 0.15 + Math.random() * 0.2,
    t: Math.random() * 1000,
  }));

  function resize() {
    const r = canvas.getBoundingClientRect();
    w = canvas.width = Math.max(1, r.width * dpr);
    h = canvas.height = Math.max(1, r.height * dpr);
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    for (const rt of routes) {
      rt.t += rt.speed;
      const baseY = rt.y * h;
      // 航线（虚线）
      ctx.beginPath();
      for (let x = 0; x <= w; x += 6 * dpr) {
        const y = baseY + Math.sin(x * rt.freq + rt.phase) * rt.amp * dpr;
        x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      }
      ctx.strokeStyle = INK;
      ctx.lineWidth = 1 * dpr;
      ctx.setLineDash([4 * dpr, 6 * dpr]);
      ctx.stroke();
      ctx.setLineDash([]);
      // 沿线漂移的光点
      const px = ((rt.t * dpr) % (w + 40 * dpr)) - 20 * dpr;
      const py = baseY + Math.sin(px * rt.freq + rt.phase) * rt.amp * dpr;
      ctx.beginPath();
      ctx.arc(px, py, 3.2 * dpr, 0, Math.PI * 2);
      ctx.fillStyle = CRIMSON;
      ctx.fill();
    }
    raf = requestAnimationFrame(draw);
  }

  resize();
  window.addEventListener('resize', resize);
  raf = requestAnimationFrame(draw);

  setStop(() => {
    cancelAnimationFrame(raf);
    window.removeEventListener('resize', resize);
  });
}
