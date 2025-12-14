# Catsith's Home - Jekyll 博客项目

## 项目概述

这是一个基于 Jekyll 构建的个人技术博客，主要用于分享算法解题报告、技术笔记和生活感悟。博客托管在 GitHub Pages 上，使用了响应式设计，支持多设备访问。

- **项目名称**: Catsith's Home
- **作者**: Catsith (马壮)
- **主要技术**: Jekyll, GitHub Pages, Markdown
- **网站地址**: https://mycodebattle.github.io

## 项目结构

```
mycodebattle.github.io/
├── _config.yml          # Jekyll 配置文件
├── _includes/           # 可重用的 HTML 组件
│   ├── comments.html    # 评论组件
│   ├── footer.html      # 页脚
│   ├── header.html      # 页头
│   ├── navigation.html  # 导航栏
│   ├── pagination.html  # 分页组件
│   └── search_data.html # 搜索数据
├── _layouts/            # 页面布局模板
│   ├── default.html     # 默认布局
│   ├── page.html        # 页面布局
│   ├── post.html        # 文章布局
│   └── wiki.html        # Wiki 页面布局
├── _posts/              # 博客文章目录
├── _wiki/               # Wiki 页面目录
├── _site/               # Jekyll 生成的静态网站
├── assets/              # 静态资源
├── css/                 # 样式文件
├── js/                  # JavaScript 文件
├── images/              # 图片资源
├── page/                # 静态页面
├── vendor/              # 第三方资源
├── Gemfile              # Ruby 依赖管理
├── Gemfile.lock         # Ruby 依赖锁定文件
├── index.html           # 首页
├── favicon.ico          # 网站图标
└── new.py               # 创建新文章的 Python 脚本
```

## 构建和运行

### 本地运行

1. 安装 Jekyll 和相关依赖：
   ```bash
   bundle install
   ```

2. 启动本地服务器：
   ```bash
   bundle exec jekyll serve
   ```

3. 在浏览器中访问 `http://localhost:4000`

### 创建新文章

项目提供了一个 Python 脚本来快速创建新文章：

```bash
python new.py "文章标题"
```

这将在 `_posts` 目录下创建一个新的 Markdown 文件，文件名格式为 `YYYY-MM-DD-文章标题.md`。

### 部署到 GitHub Pages

项目配置为自动部署到 GitHub Pages。只需将更改推送到 GitHub 仓库，GitHub 会自动构建并部署网站。

## 开发约定

### 文章命名规范

- 文章文件名格式：`YYYY-MM-DD-文章标题.md`
- 日期必须与文章前置内容中的日期保持一致
- 文章标题使用连字符分隔，不包含空格

### 文章前置内容

每篇文章都需要以下前置内容：

```yaml
---
layout: post
date: YYYY-MM-DD HH:MM:SS
title: 文章标题
categories: 分类
tags: [标签1, 标签2]
---
```

### Wiki 页面

Wiki 页面存放在 `_wiki` 目录下，使用 `wiki` 布局，适合用于编写教程和文档。

### 评论系统

项目使用 Disqus 作为评论系统，配置在 `_config.yml` 中。

## 特殊功能

### 搜索功能

网站集成了搜索功能，搜索数据由 `_includes/search_data.html` 生成，搜索逻辑在 `js/search.js` 中实现。

### 响应式设计

网站支持响应式设计，在小屏幕设备上会自动应用 `css/small.css` 中的样式。

### 页面过渡

通过 `js/page-transition.js` 实现页面过渡效果。

## 自定义脚本

### new.py

用于快速创建新文章的 Python 脚本，自动生成符合 Jekyll 规范的 Markdown 文件，包含正确的前置内容。

### 清理脚本

- `clean_duplicate_posts.sh`: 清理重复文章
- `list_duplicate_titles.py`: 列出重复标题
- `find_duplicate_titles.py`: 查找重复标题
- `convert_html_to_md.py`: 将 HTML 转换为 Markdown

## 维护说明

### 定期任务

1. 定期运行清理脚本，清理重复内容
2. 更新依赖包：`bundle update`
3. 检查链接有效性

### 备份

建议定期备份 `_posts` 目录中的内容，以防意外丢失。

## 许可证

项目采用开源许可证，具体信息请参考 `LICENSE` 文件。