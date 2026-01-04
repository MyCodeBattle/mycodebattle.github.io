# 文件整理执行计划

## 目标
将 `_posts` 目录下的题解类文章移动到 `algorithm-problems` 子文件夹，感想/笔记类文章保留在 `_posts` 目录。

## 分类规则

### 题解类文章（需要移动）
- 文件名包含平台关键词（不区分大小写）：`uva|hdu|codeforces|usaco|leetcode|pku|poj|zju|vijos|topcoder|codechef|light|cogs|luogu|scu|fzu|zstu|nyist|hihocoder|acdream|ural|sdut|nyoj`
- 文件名格式：`YYYY-MM-DD-平台-题号---题目名.md`

### 感想/笔记类文章（保留在 _posts）
- 文件名包含关键词：`memo|nothing|preface|about|杂记|good-bye|goodbye`
- 标题为中文描述性文字
- 技术笔记、生活感悟、博客功能记录等

## 执行步骤

### 步骤 1：创建新文件夹
```bash
mkdir -p /Users/zhuolx/Documents/mycodebattle.github.io/_posts/algorithm-problems
```

### 步骤 2：识别并移动题解文件
```bash
cd /Users/zhuolx/Documents/mycodebattle.github.io/_posts

# 使用 git mv 移动文件（保留 Git 历史）
for file in *.md; do
  if echo "$file" | grep -qiE "(uva|hdu|codeforces|usaco|leetcode|pku|poj|zju|vijos|topcoder|codechef|light|cogs|luogu|scu|fzu|zstu|nyist|hihocoder|acdream|ural|sdut|nyoj)"; then
    if ! echo "$file" | grep -qiE "(memo|nothing|preface|about|杂记|good-bye|goodbye)"; then
      echo "Moving: $file"
      git mv "$file" algorithm-problems/
    fi
  fi
done
```

### 步骤 3：验证移动结果
```bash
# 检查 _posts 目录下剩余的文件
ls -la /Users/zhuolx/Documents/mycodebattle.github.io/_posts/*.md

# 检查 algorithm-problems 目录下的文件
ls -la /Users/zhuolx/Documents/mycodebattle.github.io/_posts/algorithm-problems/

# 统计文件数量
echo "Posts in _posts: $(ls /Users/zhuolx/Documents/mycodebattle.github.io/_posts/*.md 2>/dev/null | wc -l)"
echo "Posts in algorithm-problems: $(ls /Users/zhuolx/Documents/mycodebattle.github.io/_posts/algorithm-problems/*.md 2>/dev/null | wc -l)"
```

### 步骤 4：测试 Jekyll 构建
```bash
cd /Users/zhuolx/Documents/mycodebattle.github.io
bundle exec jekyll serve
```

### 步骤 5：验证功能
- 访问 `http://localhost:4000`
- 检查所有文章是否能正常访问
- 测试搜索功能是否正常工作
- 检查文章列表、分类、标签等功能

### 步骤 6：提交更改
```bash
cd /Users/zhuolx/Documents/mycodebattle.github.io
git add .
git commit -m "Reorganize posts: move algorithm problems to algorithm-problems folder"
```

## 关键文件说明

### 不需要修改的文件
- `_config.yml` - Jekyll 会自动处理 `_posts` 子目录
- `_includes/search_data.html` - `site.posts` 会包含子目录中的文章
- `js/search.js` - 搜索逻辑不需要修改
- `_layouts/post.html` - 文章布局不需要修改

### 可选更新的文件
- `new.py` - 可以添加选项，让用户选择创建题解还是感想

## Jekyll 行为说明

1. **文件处理**：Jekyll 会自动处理 `_posts` 目录及其所有子目录中的 markdown 文件
2. **URL 生成**：文章 URL 基于 permalink 配置（`/:year/:month/:day/:title/`），移动文件不会影响 URL
3. **搜索索引**：`site.posts` 会包含所有子目录中的文章，搜索功能不受影响

## 风险和缓解措施

### 风险 1：文件分类错误
- **缓解**：使用精确的正则表达式匹配，移动前人工审核文件清单

### 风险 2：搜索功能失效
- **缓解**：Jekyll 的 `site.posts` 会包含子目录中的文章，搜索功能应该正常工作

### 风险 3：Git 历史丢失
- **缓解**：使用 `git mv` 命令移动文件，保留完整的 Git 历史

## 成功标准

1. 所有题解类文章成功移动到 `algorithm-problems` 文件夹
2. 所有感想/笔记类文章保留在 `_posts` 目录
3. Jekyll 本地服务器正常启动
4. 所有文章都能正常访问和显示
5. 搜索功能能够正确索引和检索所有文章
6. Git 历史完整保留

## 备份和回滚

在执行前，建议创建 Git 分支：
```bash
git checkout -b reorganize-posts
```

如果需要回滚：
```bash
git checkout main
git branch -D reorganize-posts
```
