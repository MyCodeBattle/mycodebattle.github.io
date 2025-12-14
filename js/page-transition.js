// 页面过渡动画处理 - 彻底解决动画播放两次问题
(function() {
  // 生成唯一页面ID，确保每个页面实例只播放一次动画
  const PAGE_INSTANCE_ID = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
  
  // 标记当前页面是否已经播放过进入动画
  let hasPlayedEnterAnimation = false;
  
  // 动画状态管理
  let isPlayingExitAnimation = false;
  let navigationTimeout = null;
  let animationEndListener = null;
  
  // 获取主内容元素
  const getMainContent = () => document.querySelector('.main');
  
  // 清除所有超时和事件监听
  const cleanupAnimation = () => {
    if (navigationTimeout) {
      clearTimeout(navigationTimeout);
      navigationTimeout = null;
    }
    
    const mainContent = getMainContent();
    if (mainContent && animationEndListener) {
      mainContent.removeEventListener('animationend', animationEndListener);
      animationEndListener = null;
    }
  };
  
  // 页面进入动画 - 确保每个页面实例只播放一次
  const playEnterAnimation = () => {
    // 如果动画已经播放过，直接返回
    if (hasPlayedEnterAnimation) {
      return;
    }
    
    const mainContent = getMainContent();
    if (!mainContent) {
      return;
    }
    
    // 标记动画开始播放
    hasPlayedEnterAnimation = true;
    
    // 重置所有动画类
    mainContent.classList.remove('page-enter', 'page-exit');
    
    // 触发重排，确保动画能正确开始
    mainContent.offsetHeight;
    
    // 添加进入动画类
    mainContent.classList.add('page-enter');
    
    // 监听动画结束事件
    animationEndListener = (e) => {
      if (e.animationName === 'fadeIn') {
        mainContent.classList.remove('page-enter');
        animationEndListener = null;
      }
    };
    
    mainContent.addEventListener('animationend', animationEndListener);
    
    // 添加超时保护，防止动画结束事件不触发
    navigationTimeout = setTimeout(() => {
      mainContent.classList.remove('page-enter');
      if (animationEndListener) {
        mainContent.removeEventListener('animationend', animationEndListener);
        animationEndListener = null;
      }
    }, 1200); // 比动画时长多200ms的安全缓冲
  };
  
  // 初始化进入动画
  const initEnterAnimation = () => {
    // 使用requestAnimationFrame确保DOM已经完全渲染
    requestAnimationFrame(() => {
      playEnterAnimation();
    });
  };
  
  // 页面退出动画
  const handleLinkClick = (e) => {
    const target = e.target.closest('a');
    
    // 只处理站内链接，不处理外部链接、锚点链接和下载链接
    if (target && 
        target.hostname === window.location.hostname && 
        !target.hasAttribute('download') && 
        target.getAttribute('href') && 
        target.getAttribute('href').substring(0, 1) !== '#') {
      
      e.preventDefault();
      const href = target.getAttribute('href');
      
      const mainContent = getMainContent();
      if (!mainContent || isPlayingExitAnimation) {
        // 如果没有主内容或正在播放退出动画，直接跳转
        window.location.href = href;
        return;
      }
      
      // 标记正在播放退出动画
      isPlayingExitAnimation = true;
      
      // 添加退出动画类
      mainContent.classList.add('page-exit');
      
      // 监听退出动画结束事件
      animationEndListener = (e) => {
        if (e.animationName === 'fadeOut') {
          cleanupAnimation();
          window.location.href = href;
        }
      };
      
      mainContent.addEventListener('animationend', animationEndListener);
      
      // 添加超时保护，确保导航能正常进行
      navigationTimeout = setTimeout(() => {
        cleanupAnimation();
        window.location.href = href;
      }, 500); // 比退出动画时长多200ms
    }
  };
  
  // 页面加载完成后初始化进入动画
  document.addEventListener('DOMContentLoaded', () => {
    // 只在首次加载时初始化动画
    if (!hasPlayedEnterAnimation) {
      initEnterAnimation();
    }
  });
  
  // 监听页面显示事件（包括从缓存加载）
  window.addEventListener('pageshow', (e) => {
    // 从缓存加载的页面需要重新播放动画
    if (e.persisted) {
      // 重置动画标记，允许重新播放
      hasPlayedEnterAnimation = false;
      initEnterAnimation();
    }
  });
  
  // 监听所有链接的点击事件
  document.addEventListener('click', handleLinkClick);
  
  // 监听浏览器前进/后退按钮事件
  window.addEventListener('popstate', () => {
    // 清理任何待处理的导航
    cleanupAnimation();
    isPlayingExitAnimation = false;
    
    // 延迟执行，确保页面内容已经更新
    setTimeout(() => {
      // 重置动画标记，允许重新播放
      hasPlayedEnterAnimation = false;
      initEnterAnimation();
    }, 50);
  });
  
  // 监听页面卸载事件，确保清理资源
  window.addEventListener('beforeunload', cleanupAnimation);
})();
