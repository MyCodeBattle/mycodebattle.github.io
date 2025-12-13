#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from bs4 import BeautifulSoup
import html2text
import datetime

# 配置
OLD_BLOG_DIR = './old_blog'
POSTS_DIR = './_posts'

# 确保输出目录存在
os.makedirs(POSTS_DIR, exist_ok=True)

# 初始化html2text转换器
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.ignore_images = False
converter.body_width = 0  # 不自动换行
converter.use_automatic_links = True


def extract_date_from_path(file_path):
    """从文件路径中提取日期"""
    # 匹配路径中的 YYYY/MM 格式，没有DD则使用01
    match = re.search(r'old_blog/(\d{4})/(\d{2})', file_path)
    if match:
        year, month = match.groups()
        # 尝试从目录名中提取可能的日期信息
        # 例如：old_blog/2014/06/UVa-10003/index.html -> 2014-06-01
        return f"{year}-{month}-01"
    return None


def extract_title(soup, file_path):
    """从HTML中提取标题，如果失败则使用目录名"""
    # 尝试从h1标签中提取
    h1_tags = soup.find_all('h1')
    for h1 in h1_tags:
        text = h1.get_text(strip=True)
        if text and text != 'PureFrog\'s Home':  # 排除网站标题
            return text
    
    # 尝试从h2标签中提取
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        text = h2.get_text(strip=True)
        if text and text != 'PureFrog\'s Home':
            return text
    
    # 尝试从meta标签中提取
    meta_title = soup.find('meta', property='og:title') or soup.find('meta', name='title')
    if meta_title and meta_title.get('content'):
        title = meta_title['content']
        if title != 'PureFrog\'s Home':
            return title
    
    # 尝试从title标签中提取
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text(strip=True)
        # 通常title格式为 "文章标题 - 网站名称"，尝试提取文章标题部分
        if ' - ' in title:
            title = title.split(' - ')[0]
        if title != 'PureFrog\'s Home':
            return title
    
    # 如果都失败，使用目录名作为标题
    # 例如：old_blog/2014/06/UVa-10003/index.html -> UVa-10003
    dir_name = os.path.basename(os.path.dirname(file_path))
    return dir_name


def extract_content(soup):
    """从HTML中提取正文内容"""
    # 尝试多种可能的正文位置
    content_selectors = [
        'article',
        '.article-content',
        '.post-content',
        '#content',
        '.content',
        'div[class*="content"]',
        '.main-content',
        '.entry-content'
    ]
    
    for selector in content_selectors:
        content = soup.select_one(selector)
        if content:
            return content
    
    # 如果找不到特定的内容容器，返回body，但移除不需要的元素
    body = soup.find('body')
    if body:
        # 移除一些不需要的元素
        elements_to_remove = [
            'header', 'footer', 'nav', '.sidebar', '#disqus_thread', 
            'script', 'style', '.toc', '#toc', '.categorieslist', 
            '.tagslist', '.linkslist', '.rsspart', '.share', 
            '#asidepart', '.openaside', '#totop'
        ]
        for elem in body.select(','.join(elements_to_remove)):
            elem.decompose()
        return body
    
    return soup


def get_unique_filename(date, title, counter):
    """生成唯一的文件名"""
    # 清理标题，用于文件名
    slug = re.sub(r'[^a-zA-Z0-9\s\-_]', '', title)
    slug = slug.lower().replace(' ', '-')
    # 如果标题太短，添加counter确保唯一性
    if len(slug) < 5:
        slug += f"-{counter}"
    filename = f"{date}-{slug}.md"
    return filename


def convert_html_to_md(html_file, counter):
    """将单个HTML文件转换为Markdown"""
    print(f"Processing: {html_file}")
    
    # 提取日期
    date = extract_date_from_path(html_file)
    if not date:
        # 如果从路径中提取不到日期，使用当前日期
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(f"  Warning: Could not extract date from path, using current date: {date}")
    
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取标题
    title = extract_title(soup, html_file)
    print(f"  Title: {title}")
    
    # 提取正文
    content_element = extract_content(soup)
    html_content = str(content_element)
    
    # 转换为Markdown
    md_content = converter.handle(html_content)
    
    # 清理Markdown内容
    md_content = re.sub(r'^#+\s*$', '', md_content, flags=re.MULTILINE)  # 移除空标题行
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)  # 最多保留两个连续换行
    # 移除可能的重复标题
    md_content = re.sub(r'^#\s+PureFrog\'s Home\s*\n+', '', md_content)
    
    # 生成YAML前置元数据
    yaml_frontmatter = f"""---
categories: Posts
date: {date} 00:00:00
title: {title}
tags: []
layout: post
---

"""
    
    # 生成唯一的文件名
    filename = get_unique_filename(date, title, counter)
    file_path = os.path.join(POSTS_DIR, filename)
    
    # 保存Markdown文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(yaml_frontmatter)
        f.write(md_content)
    
    print(f"  Saved to: {file_path}")
    print()


def main():
    """主函数，遍历所有HTML文件并转换"""
    print("Starting HTML to Markdown conversion...")
    print(f"Scanning directory: {OLD_BLOG_DIR}")
    print()
    
    # 遍历所有HTML文件
    counter = 0
    for root, dirs, files in os.walk(OLD_BLOG_DIR):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                try:
                    convert_html_to_md(html_file, counter)
                    counter += 1
                except Exception as e:
                    print(f"Error processing {html_file}: {e}")
                    print()
    
    print(f"Conversion completed! Processed {counter} files.")
    

if __name__ == "__main__":
    main()
