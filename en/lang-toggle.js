/* ===== 找到啦 双语切换系统 v1.0 ===== */
(function(){
  var STORAGE_KEY='zhaodaola_lang';
  var isEN=location.pathname.indexOf('/en/')!==-1;
  var currentLang=isEN?'en':'zh';

  // 持久化语言选择
  try{localStorage.setItem(STORAGE_KEY,currentLang);}catch(e){}

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
        // EN → ZH: 回到上级目录
        var path=location.pathname;
        var idx=path.indexOf('/en/');
        target=path.substring(0,idx)+'/'+path.substring(idx+4);
        // 处理 index.html
        if(target.endsWith('/en')||target.endsWith('/en/'))target=target.replace(/\/en\/?$/,'/');
      }else{
        // ZH → EN: 进入 /en/ 子目录
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
      if(saved)return; // 已有选择，不自动跳转
      var browserLang=(navigator.language||navigator.userLanguage||'').toLowerCase();
      if(browserLang.indexOf('zh')===-1 && !isEN){
        // 非中文浏览器，自动跳转英文版
        var path=location.pathname;
        var file=path.split('/').pop()||'index.html';
        var dir=path.substring(0,path.lastIndexOf('/'));
        var target=dir+'/en/'+file;
        // 只对首页自动跳转
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
