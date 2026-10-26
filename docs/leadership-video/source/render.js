// Usage: node render.js stills 1.2 4.5 ...   |   node render.js video out.mp4
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

const FPS = 30, DUR = 25;
const mode = process.argv[2];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'video.html'));
  await page.evaluate(() => window.setup());

  if (mode === 'stills') {
    for (const t of process.argv.slice(3)) {
      await page.evaluate(t => window.render(t), +t);
      await page.screenshot({ path: path.join(__dirname, 'stills', `t${(+t).toFixed(2)}.png`) });
    }
  } else {
    const out = process.argv[3];
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-preset', 'slow', '-crf', '15', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = FPS * DUR;
    const cdp = await page.context().newCDPSession(page);
    for (let f = 0; f < n; f++) {
      await page.evaluate(t => window.render(t), f / FPS);
      const { data } = await cdp.send('Page.captureScreenshot', { format: 'png', optimizeForSpeed: true });
      const buf = Buffer.from(data, 'base64');
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 75 === 0) console.log('frame', f, '/', n);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
