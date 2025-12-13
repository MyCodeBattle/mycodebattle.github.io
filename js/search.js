// 搜索功能实现
class Search {
    constructor() {
        this.input = document.getElementById('search-input');
        this.resultsContainer = document.getElementById('search-results');
        this.currentIndex = -1;
        this.timer = null;
        this.isSearching = false;
        
        this.init();
    }
    
    // 初始化搜索功能
    init() {
        this.bindEvents();
    }
    
    // 绑定事件监听
    bindEvents() {
        // 输入事件，带防抖
        this.input.addEventListener('input', () => {
            this.debounceSearch();
        });
        
        // 点击搜索图标
        const searchIcon = document.getElementById('search-icon');
        searchIcon.addEventListener('click', () => {
            this.performSearch(this.input.value);
        });
        
        // 键盘事件
        this.input.addEventListener('keydown', (e) => {
            this.handleKeydown(e);
        });
        
        // 点击外部关闭搜索结果
        document.addEventListener('click', (e) => {
            if (!this.input.contains(e.target) && !this.resultsContainer.contains(e.target)) {
                this.hideResults();
            }
        });
    }
    
    // 防抖搜索
    debounceSearch() {
        if (this.timer) {
            clearTimeout(this.timer);
        }
        
        this.timer = setTimeout(() => {
            const query = this.input.value.trim();
            this.performSearch(query);
        }, 300);
    }
    
    // 执行搜索
    performSearch(query) {
        if (!query) {
            this.hideResults();
            return;
        }
        
        this.isSearching = true;
        this.showLoading();
        
        // 简单的字符包含匹配（不区分顺序）
        const results = this.searchPosts(query);
        
        this.isSearching = false;
        this.displayResults(results, query);
    }
    
    // 搜索文章
    searchPosts(query) {
        const lowerQuery = query.toLowerCase();
        
        return searchPosts.filter(post => {
            const lowerTitle = post.title.toLowerCase();
            
            // 检查标题是否包含所有查询字符（不区分顺序）
            for (let char of lowerQuery) {
                if (!lowerTitle.includes(char)) {
                    return false;
                }
            }
            
            return true;
        });
    }
    
    // 显示加载状态
    showLoading() {
        this.resultsContainer.innerHTML = '<div class="search-loading">搜索中...</div>';
        this.resultsContainer.style.display = 'block';
    }
    
    // 显示搜索结果
    displayResults(results, query) {
        this.resultsContainer.innerHTML = '';
        
        if (results.length === 0) {
            this.resultsContainer.innerHTML = '<div class="search-no-results">没有找到匹配的文章</div>';
        } else {
            const ul = document.createElement('ul');
            ul.className = 'search-results-list';
            
            results.forEach((result, index) => {
                const li = document.createElement('li');
                li.className = 'search-result-item';
                li.dataset.index = index;
                
                const title = this.highlightText(result.title, query);
                
                li.innerHTML = `
                    <a href="${result.url}" class="search-result-link">
                        <div class="search-result-title">${title}</div>
                        <div class="search-result-date">${result.date}</div>
                    </a>
                `;
                
                li.addEventListener('mouseenter', () => {
                    this.currentIndex = index;
                    this.highlightResult();
                });
                
                ul.appendChild(li);
            });
            
            this.resultsContainer.appendChild(ul);
        }
        
        this.resultsContainer.style.display = 'block';
        this.currentIndex = -1;
    }
    
    // 高亮匹配文本
    highlightText(text, query) {
        const lowerText = text.toLowerCase();
        const lowerQuery = query.toLowerCase();
        let result = '';
        let lastIndex = 0;
        
        // 简单的高亮实现，标记所有匹配的字符
        for (let i = 0; i < text.length; i++) {
            if (lowerQuery.includes(lowerText[i])) {
                if (lastIndex < i) {
                    result += text.substring(lastIndex, i);
                }
                result += `<span class="search-highlight">${text[i]}</span>`;
                lastIndex = i + 1;
            }
        }
        
        if (lastIndex < text.length) {
            result += text.substring(lastIndex);
        }
        
        return result;
    }
    
    // 处理键盘事件
    handleKeydown(e) {
        const items = this.resultsContainer.querySelectorAll('.search-result-item');
        
        if (items.length === 0) return;
        
        switch (e.key) {
            case 'ArrowDown':
                e.preventDefault();
                this.currentIndex = (this.currentIndex + 1) % items.length;
                this.highlightResult();
                break;
            case 'ArrowUp':
                e.preventDefault();
                this.currentIndex = (this.currentIndex - 1 + items.length) % items.length;
                this.highlightResult();
                break;
            case 'Enter':
                e.preventDefault();
                if (this.currentIndex >= 0 && this.currentIndex < items.length) {
                    const link = items[this.currentIndex].querySelector('a');
                    if (link) {
                        window.location.href = link.href;
                    }
                }
                break;
            case 'Escape':
                this.hideResults();
                break;
        }
    }
    
    // 高亮当前选中的结果
    highlightResult() {
        const items = this.resultsContainer.querySelectorAll('.search-result-item');
        
        items.forEach((item, index) => {
            if (index === this.currentIndex) {
                item.classList.add('search-result-active');
                item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                item.classList.remove('search-result-active');
            }
        });
    }
    
    // 隐藏搜索结果
    hideResults() {
        this.resultsContainer.style.display = 'none';
        this.resultsContainer.innerHTML = '';
        this.currentIndex = -1;
    }
}

// 页面加载完成后初始化搜索功能
document.addEventListener('DOMContentLoaded', () => {
    new Search();
});