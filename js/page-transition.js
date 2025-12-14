// 页面过渡动画处理
(function() {
  // 为内容区域添加过渡动画类
  function addTransitionClass() {
    const mainContent = document.querySelector('.main');
    if (mainContent) {
      mainContent.classList.add('page-transition');
    }
  }

  // 页面进入动画
  function playEnterAnimation() {
    const mainContent = document.querySelector('.main');
    if (mainContent) {
      // 重置状态
      mainContent.classList.remove('page-exit', 'page-enter');
      
      // 触发重排
      mainContent.offsetHeight;
      
      // 添加进入动画
      mainContent.classList.add('page-enter');
      
      setTimeout(() => {
        mainContent.classList.remove('page-enter');
      }, 300);
    }
  }

  // 页面加载完成后初始化
  function initPage() {
    addTransitionClass();
    playEnterAnimation();
  }

  // 页面加载完成后添加进入动画
  document.addEventListener('DOMContentLoaded', initPage);

  // 监听页面显示事件（包括从缓存中加载）
  window.addEventListener('pageshow', function(e) {
    // 检查是否是从缓存中加载的页面
    if (e.persisted) {
      initPage();
    }
  });

  // 监听所有链接的点击事件
  document.addEventListener('click', function(e) {
    // 检查是否是文章链接
    const target = e.target.closest('a');
    
    // 只处理站内链接，不处理外部链接、锚点链接和下载链接
    if (target && 
        target.hostname === window.location.hostname && 
        !target.hasAttribute('download') && 
        target.getAttribute('href') && 
        target.getAttribute('href').substring(0, 1) !== '#') {
      
      e.preventDefault();
      const href = target.getAttribute('href');
      
      // 获取内容区域
      const mainContent = document.querySelector('.main');
      if (mainContent) {
        // 添加退出动画
        mainContent.classList.add('page-exit');
        
        // 动画结束后跳转页面
        setTimeout(() => {
          // 使用location.replace()避免在历史记录中添加重复条目
          window.location.href = href;
        }, 300);
      } else {
        // 如果没有找到内容区域，直接跳转
        window.location.href = href;
      }
    }
  });

  // 监听浏览器前进/后退按钮事件
  window.addEventListener('popstate', function() {
    // 延迟执行，确保页面内容已经更新
    setTimeout(() => {
      playEnterAnimation();
    }, 10);
  });
})();
