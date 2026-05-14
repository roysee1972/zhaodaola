/**
 * 找到啦 · 分享结果卡片生成器
 * 
 * 功能：在诊断结果页生成一张可保存的分享卡片图片
 * 依赖：页面需有 #page-result, #resultList, #resultSummary, .result-sub
 *       以及全局变量 cardScores, cardPoints
 */

(function() {
  'use strict';

  /* ============================================================
     样式注入
     ============================================================ */
  const style = document.createElement('style');
  style.textContent = `
    /* 分享卡片按钮 */
    .share-card-btn {
      display: inline-block;
      padding: 10px 28px;
      background: transparent;
      border: 1px solid #c9a84c;
      color: #9a7a4a;
      font-family: 'Noto Serif SC', 'STSong', 'SimSun', serif;
      font-size: 14px;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      letter-spacing: 4px;
      transition: all 0.2s;
      margin-top: 12px;
    }
    .share-card-btn:hover {
      background: rgba(201,168,76,0.1);
      color: #5a3e1b;
    }

    /* 预览弹窗 */
    .share-card-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(30,20,10,0.75);
      z-index: 9999;
      justify-content: center;
      align-items: center;
      animation: scFadeIn 0.3s ease;
    }
    .share-card-overlay.show {
      display: flex;
    }
    @keyframes scFadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    .share-card-modal {
      background: #f5e6c8;
      border-radius: 12px;
      padding: 24px;
      max-width: 420px;
      width: 90%;
      text-align: center;
      box-shadow: 0 8px 40px rgba(0,0,0,0.3);
      animation: scSlideUp 0.3s ease;
    }
    @keyframes scSlideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .share-card-modal h3 {
      font-family: 'Noto Serif SC', serif;
      font-size: 18px;
      color: #5a3e1b;
      margin-bottom: 16px;
      letter-spacing: 4px;
    }

    .share-card-preview {
      width: 100%;
      border-radius: 8px;
      border: 1px solid rgba(139,90,43,0.2);
      margin-bottom: 20px;
    }

    .share-card-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
    }
    .share-card-actions button {
      padding: 10px 28px;
      border-radius: 8px;
      font-family: 'Noto Serif SC', serif;
      font-size: 14px;
      cursor: pointer;
      letter-spacing: 2px;
      transition: all 0.2s;
    }
    .sc-download-btn {
      background: linear-gradient(135deg, #c9a84c, #e8c870);
      border: none;
      color: #5a3e1b;
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(201,168,76,0.3);
    }
    .sc-download-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(201,168,76,0.4);
    }
    .sc-cancel-btn {
      background: transparent;
      border: 1px solid #c9a84c;
      color: #9a7a4a;
    }
    .sc-cancel-btn:hover {
      background: rgba(201,168,76,0.1);
    }

    .share-card-hint {
      font-size: 12px;
      color: #9a7a4a;
      margin-top: 12px;
      line-height: 1.6;
    }
  `;
  document.head.appendChild(style);

  /* ============================================================
     DOM：按钮 + 弹窗
     ============================================================ */
  function injectUI() {
    // 找到结果页的按钮区域，在"查看通关建议"按钮后面插入分享按钮
    const resultPage = document.getElementById('page-result');
    if (!resultPage) return;

    const navWrap = resultPage.querySelector('.nav-btn-wrap');
    if (!navWrap) return;

    // 创建分享按钮
    const shareBtn = document.createElement('button');
    shareBtn.className = 'share-card-btn';
    shareBtn.textContent = '生成分享卡片';
    shareBtn.onclick = generateShareCard;
    navWrap.appendChild(shareBtn);

    // 创建弹窗
    const overlay = document.createElement('div');
    overlay.className = 'share-card-overlay';
    overlay.id = 'shareCardOverlay';
    overlay.innerHTML = `
      <div class="share-card-modal">
        <h3>你的认知卡点画像</h3>
        <img class="share-card-preview" id="shareCardPreview" src="" alt="分享卡片">
        <div class="share-card-actions">
          <button class="sc-download-btn" onclick="downloadShareCard()">保存图片</button>
          <button class="sc-cancel-btn" onclick="closeShareCard()">取消</button>
        </div>
        <div class="share-card-hint">长按图片可分享给朋友<br>保存后发朋友圈，让更多人看见自己</div>
      </div>
    `;
    document.body.appendChild(overlay);
  }

  /* ============================================================
     Canvas 文本自动换行
     ============================================================ */
  function wrapText(ctx, text, maxWidth) {
    const chars = Array.from(text); // 正确处理中文
    const lines = [];
    let line = '';

    for (const ch of chars) {
      const test = line + ch;
      if (ctx.measureText(test).width > maxWidth && line) {
        lines.push(line);
        line = ch;
      } else {
        line = test;
      }
    }
    if (line) lines.push(line);
    return lines;
  }

  /* ============================================================
     绘制圆角矩形
     ============================================================ */
  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  /* ============================================================
     生成分享卡片
     ============================================================ */
  function generateShareCard() {
    // 获取数据
    const resultSub = document.querySelector('.result-sub');
    const levelName = resultSub ? resultSub.textContent.trim() : '未知关卡';

    // 计算排序后的卡点
    if (typeof computeScores === 'function') computeScores();
    const sorted = Object.entries(cardScores || {}).sort((a, b) => b[1] - a[1]);
    if (sorted.length === 0) {
      alert('还没有诊断结果，请先完成诊断。');
      return;
    }

    const topItems = sorted.slice(0, 3).map(([key, score]) => {
      const cp = cardPoints[key];
      return {
        name: cp ? cp.name : key,
        score: score,
        pct: Math.min(100, score * 40)
      };
    });

    // 获取摘要文字
    const summaryEl = document.getElementById('resultSummary');
    const summaryText = summaryEl ? summaryEl.textContent : '';

    /* ============================================================
       Canvas 绘制
       ============================================================ */
    const W = 750, H = 1060;
    const canvas = document.createElement('canvas');
    canvas.width = W;
    canvas.height = H;
    const ctx = canvas.getContext('2d');

    // --- 背景渐变（牛皮纸色） ---
    const grad = ctx.createLinearGradient(0, 0, W, H);
    grad.addColorStop(0, '#f7edd5');
    grad.addColorStop(0.35, '#eed9a4');
    grad.addColorStop(0.65, '#e8d090');
    grad.addColorStop(1, '#f0e2b8');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, W, H);

    // --- 纸张纹理（噪点模拟） ---
    for (let i = 0; i < 8000; i++) {
      const x = Math.random() * W;
      const y = Math.random() * H;
      const a = Math.random() * 0.03;
      ctx.fillStyle = `rgba(100,70,30,${a})`;
      ctx.fillRect(x, y, 1, 1);
    }

    // --- 顶部金色装饰条 ---
    ctx.fillStyle = '#c9a84c';
    ctx.fillRect(0, 0, W, 5);

    // --- 边框装饰 ---
    ctx.strokeStyle = 'rgba(139,90,43,0.25)';
    ctx.lineWidth = 1.5;
    roundRect(ctx, 20, 20, W - 40, H - 40, 8);
    ctx.stroke();

    // --- 内部细线装饰框 ---
    ctx.strokeStyle = 'rgba(139,90,43,0.12)';
    ctx.lineWidth = 0.5;
    roundRect(ctx, 30, 30, W - 60, H - 60, 6);
    ctx.stroke();

    let y = 80;

    // --- 网站名：找到啦 ---
    ctx.textAlign = 'center';
    ctx.fillStyle = '#5a3e1b';
    ctx.font = 'bold 48px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText('找到啦', W / 2, y);
    y += 36;

    // --- 副标题：生命游戏 ---
    ctx.fillStyle = '#9a7a4a';
    ctx.font = '16px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.letterSpacing = '6px';
    ctx.fillText('— 生 命 游 戏 —', W / 2, y);
    y += 36;

    // --- 分隔线 ---
    ctx.strokeStyle = 'rgba(201,168,76,0.5)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(200, y);
    ctx.lineTo(W - 200, y);
    ctx.stroke();
    y += 36;

    // --- 关卡名称 ---
    ctx.fillStyle = '#c9a84c';
    ctx.font = '14px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText(levelName, W / 2, y);
    y += 30;

    // --- 主标题：我的认知卡点画像 ---
    ctx.fillStyle = '#5a3e1b';
    ctx.font = 'bold 30px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText('我的认知卡点画像', W / 2, y);
    y += 48;

    // --- 摘要文字 ---
    if (summaryText) {
      ctx.fillStyle = '#9a7a4a';
      ctx.font = 'italic 15px "Noto Serif SC", "STSong", SimSun, serif';
      const sumLines = wrapText(ctx, summaryText, 580);
      sumLines.forEach(line => {
        ctx.fillText(line, W / 2, y);
        y += 24;
      });
      y += 20;
    }

    // --- 分隔线 ---
    ctx.strokeStyle = 'rgba(201,168,76,0.3)';
    ctx.beginPath();
    ctx.moveTo(80, y);
    ctx.lineTo(W - 80, y);
    ctx.stroke();
    y += 32;

    // --- TOP 3 卡点 ---
    ctx.textAlign = 'left';
    const barColors = ['#b85a3a', '#c9a84c', '#9a7a4a']; // 高/中/低

    topItems.forEach((item, i) => {
      const lx = 70;
      const bw = 480; // 进度条宽度

      // 序号圆圈
      ctx.fillStyle = i === 0 ? '#b85a3a' : i === 1 ? '#c9a84c' : '#9a7a4a';
      ctx.beginPath();
      ctx.arc(lx + 16, y + 4, 16, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#fff';
      ctx.font = 'bold 16px "Noto Serif SC", serif';
      ctx.textAlign = 'center';
      ctx.fillText(String(i + 1), lx + 16, y + 9);
      ctx.textAlign = 'left';

      // 卡点名称
      ctx.fillStyle = '#5a3e1b';
      ctx.font = 'bold 20px "Noto Serif SC", "STSong", SimSun, serif';
      ctx.fillText(item.name, lx + 44, y + 9);

      // 命中次数
      ctx.fillStyle = '#9a7a4a';
      ctx.font = '13px "Noto Serif SC", "STSong", SimSun, serif';
      ctx.textAlign = 'right';
      ctx.fillText(`命中 ${item.score} 次`, W - 70, y + 9);
      ctx.textAlign = 'left';
      y += 30;

      // 进度条背景
      const barY = y;
      const barH = 14;
      ctx.fillStyle = 'rgba(139,90,43,0.1)';
      roundRect(ctx, lx + 44, barY, bw, barH, 7);
      ctx.fill();

      // 进度条填充
      const fillW = Math.max(20, bw * item.pct / 100);
      const barGrad = ctx.createLinearGradient(lx + 44, 0, lx + 44 + fillW, 0);
      if (item.pct >= 60) {
        barGrad.addColorStop(0, '#b85a3a');
        barGrad.addColorStop(1, '#d46a4a');
      } else if (item.pct >= 30) {
        barGrad.addColorStop(0, '#c9a84c');
        barGrad.addColorStop(1, '#e8c870');
      } else {
        barGrad.addColorStop(0, '#9a7a4a');
        barGrad.addColorStop(1, '#b89a6a');
      }
      ctx.fillStyle = barGrad;
      roundRect(ctx, lx + 44, barY, fillW, barH, 7);
      ctx.fill();

      y += 42;
    });

    // --- 分隔线 ---
    y += 10;
    ctx.strokeStyle = 'rgba(201,168,76,0.3)';
    ctx.beginPath();
    ctx.moveTo(80, y);
    ctx.lineTo(W - 80, y);
    ctx.stroke();
    y += 36;

    // --- 底部引言 ---
    ctx.textAlign = 'center';
    ctx.fillStyle = '#9a7a4a';
    ctx.font = 'italic 16px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText('「 看见自己卡在哪，就是改变的第一步 」', W / 2, y);
    y += 40;

    // --- 网址 ---
    ctx.fillStyle = '#b89a6a';
    ctx.font = '13px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText('zhaodaola.top', W / 2, y);
    y += 22;

    // --- 底部标签 ---
    ctx.fillStyle = 'rgba(139,90,43,0.2)';
    ctx.font = '11px "Noto Serif SC", "STSong", SimSun, serif';
    ctx.fillText('— 找到啦 · 生命游戏的十二个关卡 —', W / 2, y);

    // --- 底部金色装饰条 ---
    ctx.fillStyle = '#c9a84c';
    ctx.fillRect(0, H - 5, W, 5);

    /* ============================================================
       显示预览弹窗
       ============================================================ */
    const dataUrl = canvas.toDataURL('image/png');
    document.getElementById('shareCardPreview').src = dataUrl;
    document.getElementById('shareCardOverlay').classList.add('show');

    // 存储 canvas 供下载用
    window._shareCardCanvas = canvas;
  }

  /* ============================================================
     下载卡片
     ============================================================ */
  window.downloadShareCard = function() {
    const canvas = window._shareCardCanvas;
    if (!canvas) return;

    const link = document.createElement('a');
    link.download = '找到啦-我的认知卡点.png';
    link.href = canvas.toDataURL('image/png');
    link.click();

    // 下载后关闭弹窗
    setTimeout(closeShareCard, 500);
  };

  /* ============================================================
     关闭弹窗
     ============================================================ */
  window.closeShareCard = function() {
    document.getElementById('shareCardOverlay').classList.remove('show');
  };

  // 点击遮罩关闭
  document.addEventListener('click', function(e) {
    if (e.target && e.target.id === 'shareCardOverlay') {
      closeShareCard();
    }
  });

  /* ============================================================
     初始化：页面加载后注入UI
     ============================================================ */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectUI);
  } else {
    injectUI();
  }

})();
