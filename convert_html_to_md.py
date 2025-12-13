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


def extract_date_from_path(file_path):
    """从文件路径中提取日期"""
    match = re.search(r'old_blog/(\d{4})/(\d{2})', file_path)
    if match:
        year, month = match.groups()
        return f"{year}-{month}-01"
    return datetime.datetime.now().strftime('%Y-%m-%d')


def extract_title(soup, html_file):
    """从HTML中提取标题，如果失败则使用目录名"""
    # 1. 尝试从文章内容中的h1/h2标签提取
    content_selectors = [
        'article',
        '.article-content',
        '.post-content',
        '#content',
        '.content',
        'div[class*="content"]'
    ]
    
    for selector in content_selectors:
        content = soup.select_one(selector)
        if content:
            # 在内容区域内查找标题
            h1 = content.find('h1')
            if h1:
                text = h1.get_text(strip=True)
                if text and text != 'PureFrog\'s Home':
                    return text
            
            h2 = content.find('h2')
            if h2:
                text = h2.get_text(strip=True)
                if text and text != 'PureFrog\'s Home':
                    return text
    
    # 2. 尝试从整个页面的h1/h2标签提取
    h1_tags = soup.find_all('h1')
    for h1 in h1_tags:
        text = h1.get_text(strip=True)
        if text and text != 'PureFrog\'s Home':
            return text
    
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        text = h2.get_text(strip=True)
        if text and text != 'PureFrog\'s Home':
            return text
    
    # 3. 尝试从title标签提取
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text(strip=True)
        # 通常title格式为 "文章标题 - 网站名称"，尝试提取文章标题部分
        if ' - ' in title:
            title = title.split(' - ')[0]
        if title and title != 'PureFrog\'s Home' and len(title) > 5:
            return title
    
    # 4. 使用目录名作为标题（最后手段）
    dir_name = os.path.basename(os.path.dirname(html_file))
    return dir_name


def extract_code_blocks(html_content):
    """提取HTML中的代码块，返回清理后的HTML和代码块列表"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 移除不需要的元素
    elements_to_remove = [
        'header', 'footer', 'nav', '.sidebar', '#disqus_thread', 
        'script', 'style', '.toc', '#toc', '.categorieslist', 
        '.tagslist', '.linkslist', '.rsspart', '.share', 
        '#asidepart', '.openaside', '#totop', '.article-info',
        '.article-meta', '.post-meta', '.meta', '.entry-meta'
    ]
    for elem in soup.select(','.join(elements_to_remove)):
        elem.decompose()
    
    # 提取代码块
    code_blocks = []
    code_counter = 0
    
    # 处理figure.highlight表格结构的代码块
    for figure in soup.find_all('figure', class_='highlight'):
        table = figure.find('table')
        if table:
            # 找到代码列（td.code）
            code_td = table.select_one('td.code')
            if code_td:
                # 提取代码内容
                code_lines = []
                for line in code_td.find_all('div', class_='line'):
                    code_lines.append(line.get_text())
                code = '\n'.join(code_lines)
                code = code.strip()
                
                if code:
                    # 替换整个figure为标记
                    placeholder = f"__CODE_BLOCK_{code_counter}__"
                    figure.replace_with(placeholder)
                    code_blocks.append(code)
                    code_counter += 1
    
    # 处理普通<pre>标签中的代码
    for pre in soup.find_all('pre'):
        code = pre.get_text()
        # 清理代码，移除行号和特殊字符
        # 移除连续的数字行号
        code = re.sub(r'^\s*\d{3,}\s*$', '', code, flags=re.MULTILINE)
        # 移除单个数字行号
        code = re.sub(r'^\s*\d+\s*', '', code, flags=re.MULTILINE)
        # 移除表格分隔符
        code = re.sub(r'^\s*\|\s*$', '', code, flags=re.MULTILINE)
        code = re.sub(r'^\s*---\|---\s*$', '', code, flags=re.MULTILINE)
        # 移除多余的空行
        code = re.sub(r'\n{3,}', '\n\n', code)
        code = code.strip()
        if code:
            # 替换代码块为标记
            placeholder = f"__CODE_BLOCK_{code_counter}__"
            pre.replace_with(placeholder)
            code_blocks.append(code)
            code_counter += 1
    
    # 处理<code>标签中的代码（如果有的话）
    for code_tag in soup.find_all('code'):
        code = code_tag.get_text()
        code = code.strip()
        if code:
            placeholder = f"__CODE_BLOCK_{code_counter}__"
            code_tag.replace_with(placeholder)
            code_blocks.append(code)
            code_counter += 1
    
    return str(soup), code_blocks


def convert_html_to_md(html_file):
    """将单个HTML文件转换为Markdown"""
    print(f"Processing: {html_file}")
    
    # 提取日期
    date = extract_date_from_path(html_file)
    
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取标题
    title = extract_title(soup, html_file)
    print(f"  Title: {title}")
    
    # 提取代码块
    processed_html, code_blocks = extract_code_blocks(html_content)
    
    # 转换为Markdown
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0
    converter.use_automatic_links = True
    md_content = converter.handle(processed_html)
    
    # 恢复代码块
    for i, code in enumerate(code_blocks):
        placeholder = f"__CODE_BLOCK_{i}__"
        if code:
            # 确保代码块正确换行
            code_lines = code.split('\n')
            formatted_code = '\n'.join(code_lines)
            md_content = md_content.replace(placeholder, f'\n```c++\n{formatted_code}\n```\n')
    
    # 清理Markdown内容
    # 移除网站标题
    md_content = re.sub(r'#\s*PureFrog\'s Home\s*\n+', '', md_content)
    # 移除作者和发布信息
    md_content = re.sub(r'By.*?Published.*?\n+', '', md_content, flags=re.DOTALL)
    # 移除分类和标签链接
    md_content = re.sub(r'\[Solving Reports\](/categories/Solving-Reports/)', '', md_content)
    md_content = re.sub(r'\[Online Judge.*?\](/tags/.*?)', '', md_content)
    md_content = re.sub(r'\[Math.*?\](/tags/.*?)', '', md_content)
    # 移除残留的行号和表格符号
    md_content = re.sub(r'^\s*\d{3,}\s*$', '', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\s*\|\s*$', '', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\s*---\|---\s*$', '', md_content, flags=re.MULTILINE)
    # 清理多余的空行
    md_content = re.sub(r'\n{4,}', '\n\n\n', md_content)
    # 清理文件开头和结尾的空行
    md_content = md_content.strip()
    
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
    slug = re.sub(r'[^a-zA-Z0-9\s\-_]', '', title)
    slug = slug.lower().replace(' ', '-')
    if len(slug) < 5:
        slug = f"{slug}-{os.path.basename(os.path.dirname(html_file))}"
    filename = f"{date}-{slug}.md"
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
                    convert_html_to_md(html_file)
                    counter += 1
                except Exception as e:
                    print(f"Error processing {html_file}: {e}")
                    print()
    
    print(f"Conversion completed! Processed {counter} files.")
    

if __name__ == "__main__":
    main()
