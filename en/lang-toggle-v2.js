/* ===== 找到啦 双语切换系统 v3.0 ===== */
(function(){
  var STORAGE_KEY='zhaodaola_lang';
  var isEN=location.pathname.indexOf('/en/')!==-1;
  var currentLang=isEN?'en':'zh';

  // 中文文件名 → 英文文件名 映射
  var zhToEn={
    '建站缘起.html':'about.html',
    '联系我们.html':'contact.html',
    '临终故事十二则.html':'deathbed-stories.html',
    '第一关-原生家庭.html':'stage-01-family-of-origin.html',
    '第二关-求知求学.html':'stage-02-learning.html',
    '第三关-初入人海.html':'stage-03-entering-world.html',
    '第四关-独立谋生.html':'stage-04-independence.html',
    '第五关-婚恋家庭.html':'stage-05-love-marriage.html',
    '第六关-人到中年.html':'stage-06-midlife.html',
    '第七关-金钱关系.html':'stage-07-money.html',
    '第八关-人际迷宫.html':'stage-08-social-maze.html',
    '第九关-兴趣爱好.html':'stage-09-hobbies.html',
    '第十关-心灵信仰.html':'stage-10-spirituality.html',
    '第十一关-健康与衰老.html':'stage-11-health.html',
    '第十二关-终篇传承.html':'stage-12-legacy.html',
    'article-原生家庭-为你好.html':'article-for-your-own-good.html',
    'article-原生家庭-幸福观.html':'article-happiness.html'
  };
  // 反向映射：英文文件名 → 中文文件名
  var enToZh={};
  for(var k in zhToEn){if(zhToEn.hasOwnProperty(k)){enToZh[zhToEn[k]]=k;}}

  // 同名文件（中英文共用，不需要映射）
  var sameName=['index.html','updates.html','products.html','disclaimer.html','assessment-energy.html','assessment-influence.html','assessment-value.html','perimenopause.html'];

  // 持久化语言选择
  try{localStorage.setItem(STORAGE_KEY,currentLang);}catch(e){}

  // 注入样式
  var style=document.createElement('style');
  style.textContent='#langToggle{'
    +'position:fixed;top:20px;right:20px;z-index:9999;'
    +'display:inline-block;padding:8px 18px;'
    +'background:rgba(245,230,200,0.92);'
    +'border:1px solid rgba(139,90,43,0.25);'
    +'border-radius:20px;'
    +'font-family:"Noto Serif SC","STSong",serif;'
    +'font-size:13px;color:#5a3e1b;'
    +'letter-spacing:2px;cursor:pointer;'
    +'text-decoration:none;'
    +'box-shadow:0 2px 12px rgba(90,60,20,0.15);'
    +'backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);'
    +'transition:all 0.2s;'
    +'}'
    +'#langToggle:hover{'
    +'background:rgba(245,230,200,1);'
    +'border-color:#c9a84c;'
    +'box-shadow:0 4px 16px rgba(90,60,20,0.25);'
    +'}';
  document.head.appendChild(style);

  // 创建切换按钮
  function createToggle(){
    if(document.getElementById('langToggle'))return;
    var btn=document.createElement('a');
    btn.id='langToggle';
    btn.href='javascript:void(0)';
    btn.textContent=isEN?'中文':'English';
    btn.title=isEN?'Switch to Chinese':'Switch to English';
    btn.setAttribute('data-lang',currentLang);
    btn.onclick=function(){
      var path=location.pathname;
      var file=decodeURIComponent(path.split('/').pop())||'index.html';
      var target;
      if(isEN){
        // 从英文切到中文：去掉 /en/ 前缀，用中文文件名
        var idx=path.indexOf('/en/');
        var dir=path.substring(0,idx);
        var zhFile=enToZh[file]||file;
        target=dir+'/'+zhFile;
      }else{
        // 从中文切到英文：加 /en/ 前缀，用英文文件名
        var dir=path.substring(0,path.lastIndexOf('/'));
        var enFile=zhToEn[file]||file;
        target=dir+'/en/'+enFile;
      }
      try{localStorage.setItem(STORAGE_KEY,isEN?'zh':'en');}catch(e){}
      location.href=target;
    };
    document.body.appendChild(btn);
  }

  // 自动跳转（首次访问时根据浏览器语言）
  function autoRedirect(){
    try{
      var saved=localStorage.getItem(STORAGE_KEY);
      if(saved)return;
      var browserLang=(navigator.language||navigator.userLanguage||'').toLowerCase();
      if(browserLang.indexOf('zh')===-1 && !isEN){
        var path=location.pathname;
        var file=decodeURIComponent(path.split('/').pop())||'index.html';
        var dir=path.substring(0,path.lastIndexOf('/'));
        var enFile=zhToEn[file]||file;
        var target=dir+'/en/'+enFile;
        if(file==='index.html'||file===''||file==='/'){
          localStorage.setItem(STORAGE_KEY,'en');
          location.href=target;
        }
      }
    }catch(e){}
  }

  // DOM Ready
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){createToggle();autoRedirect();});
  }else{
    createToggle();autoRedirect();
  }
})();
