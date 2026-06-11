/**
 * 活动网站模板系统 - 通用交互模块
 * 功能: 导航、滚动动画、灯箱、倒计时、留言
 */

(function() {
  'use strict';

  // ========== 导航菜单 ==========
  function initNav() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', function() {
      toggle.classList.toggle('active');
      menu.classList.toggle('open');
      document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
    });

    // 点击菜单项关闭
    menu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        toggle.classList.remove('active');
        menu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // ========== 滚动渐显动画 ==========
  function initScrollAnimations() {
    var elements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
    if (!elements.length) return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(function(el) {
      observer.observe(el);
    });
  }

  // ========== 照片灯箱 ==========
  function initLightbox() {
    var lightbox = document.getElementById('lightbox');
    if (!lightbox) return;

    var lbImg = lightbox.querySelector('img');
    var lbCaption = lightbox.querySelector('.lightbox-caption');
    var lbClose = lightbox.querySelector('.lightbox-close');

    // 绑定所有可点击的画廊图片
    document.querySelectorAll('.gallery-item').forEach(function(item) {
      item.addEventListener('click', function() {
        var img = item.querySelector('img');
        var caption = item.querySelector('.caption');
        if (img) {
          lbImg.src = img.src;
          lbImg.alt = img.alt || '';
          lbCaption.textContent = caption ? caption.textContent : '';
          lightbox.classList.add('open');
          document.body.style.overflow = 'hidden';
        }
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
      lbImg.src = '';
    }

    if (lbClose) lbClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && lightbox.classList.contains('open')) {
        closeLightbox();
      }
    });
  }

  // ========== 倒计时 ==========
  function initCountdown() {
    var container = document.getElementById('countdown');
    if (!container) return;

    var targetStr = container.dataset.target;
    if (!targetStr) return;

    var targetDate = new Date(targetStr).getTime();

    function update() {
      var now = Date.now();
      var diff = targetDate - now;

      if (diff <= 0) {
        container.innerHTML = '<div class="countdown-item"><div class="countdown-num">🎉</div><div class="countdown-label">活动已开始</div></div>';
        return;
      }

      var days = Math.floor(diff / 86400000);
      var hours = Math.floor((diff % 86400000) / 3600000);
      var mins = Math.floor((diff % 3600000) / 60000);
      var secs = Math.floor((diff % 60000) / 1000);

      container.innerHTML =
        '<div class="countdown-item"><div class="countdown-num">' + days + '</div><div class="countdown-label">天</div></div>' +
        '<div class="countdown-item"><div class="countdown-num">' + hours + '</div><div class="countdown-label">时</div></div>' +
        '<div class="countdown-item"><div class="countdown-num">' + mins + '</div><div class="countdown-label">分</div></div>' +
        '<div class="countdown-item"><div class="countdown-num">' + secs + '</div><div class="countdown-label">秒</div></div>';
    }

    update();
    setInterval(update, 1000);
  }

  // ========== 留言板（前端模拟） ==========
  function initGuestbook() {
    var form = document.getElementById('guestbook-form');
    var list = document.getElementById('messages-list');
    if (!form || !list) return;

    // 从 localStorage 加载已有留言
    var storageKey = 'guestbook_' + (document.title || 'default');
    var messages = [];
    try {
      messages = JSON.parse(localStorage.getItem(storageKey)) || [];
    } catch(e) {}

    function render() {
      list.innerHTML = '';
      if (messages.length === 0) {
        list.innerHTML = '<p style="text-align:center;color:var(--color-muted);padding:2rem 0;">还没有留言，写一条祝福吧！</p>';
        return;
      }
      messages.slice().reverse().forEach(function(msg) {
        var div = document.createElement('div');
        div.className = 'message-item';
        div.innerHTML =
          '<span class="message-author">' + escapeHtml(msg.name) + '</span>' +
          '<span class="message-time">' + msg.time + '</span>' +
          '<p class="message-text">' + escapeHtml(msg.text) + '</p>';
        list.appendChild(div);
      });
    }

    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var nameInput = form.querySelector('input[name="name"]');
      var textInput = form.querySelector('textarea[name="message"]');
      var name = (nameInput.value || '').trim() || '匿名';
      var text = (textInput.value || '').trim();
      if (!text) return;

      var now = new Date();
      var timeStr = now.getFullYear() + '-' +
        String(now.getMonth() + 1).padStart(2, '0') + '-' +
        String(now.getDate()).padStart(2, '0') + ' ' +
        String(now.getHours()).padStart(2, '0') + ':' +
        String(now.getMinutes()).padStart(2, '0');

      messages.push({ name: name, text: text, time: timeStr });

      try {
        localStorage.setItem(storageKey, JSON.stringify(messages));
      } catch(e) {}

      nameInput.value = '';
      textInput.value = '';
      render();
    });

    render();
  }

  // ========== 分享按钮 ==========
  function initShare() {
    var btn = document.querySelector('.btn-share');
    if (!btn) return;

    btn.addEventListener('click', function(e) {
      e.preventDefault();
      if (navigator.share) {
        navigator.share({
          title: document.title,
          url: window.location.href
        });
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href).then(function() {
          btn.textContent = '✓ 链接已复制';
          setTimeout(function() { btn.textContent = '分享'; }, 2000);
        });
      }
    });
  }

  // ========== 工具函数 ==========
  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ========== 平滑滚动（兼容旧浏览器） ==========
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(link) {
      link.addEventListener('click', function(e) {
        var target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          var top = target.getBoundingClientRect().top + window.pageYOffset - 60;
          window.scrollTo({ top: top, behavior: 'smooth' });
        }
      });
    });
  }

  // ========== 初始化 ==========
  document.addEventListener('DOMContentLoaded', function() {
    initNav();
    initScrollAnimations();
    initLightbox();
    initCountdown();
    initGuestbook();
    initShare();
    initSmoothScroll();
  });

})();
