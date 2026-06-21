/* ===== 找到啦 双语切换系统 v2.0 ===== */
(function(){
  var STORAGE_KEY='zhaodaola_lang';
  var isEN=location.pathname.indexOf('/en/')!==-1;
  var currentLang=isEN?'en':'zh';

  // 持久化语言选择
  try{localStorage.setItem(STORAGE_KEY,currentLang);}catch(e){}

  // 注入样式
  var style=document.createElement('style');
  style.textContent='#langToggle{'
    +'position:fixed;bottom:20px;right:20px;z-index:9999;'
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
      var target;
      if(isEN){
        var path=location.pathname;
        var idx=path.indexOf('/en/');
        target=path.substring(0,idx)+'/'+path.substring(idx+4);
        if(target.endsWith('/en')||target.endsWith('/en/'))target=target.replace(/\/en\/?$/,'/');
      }else{
        var path=location.pathname;
        var file=path.split('/').pop()||'index.html';
        var dir=path.substring(0,path.lastIndexOf('/'));
        target=dir+'/en/'+file;
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
        var file=path.split('/').pop()||'index.html';
        var dir=path.substring(0,path.lastIndexOf('/'));
        var target=dir+'/en/'+file;
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
