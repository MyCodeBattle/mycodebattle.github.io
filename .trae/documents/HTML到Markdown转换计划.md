# HTML到Jekyll Markdown转换计划

## 项目分析

1. **当前博客系统**：Jekyll
2. **目标**：将old_blog目录下的HTML文件转换为符合Jekyll规范的Markdown文件，并存放到_posts目录
3. **文件结构**：
   - old_blog/2014/[月份]/[文章目录]/index.html
   - old_blog/2015/[月份]/[文章目录]/index.html
4. **Jekyll文件格式要求**：
   - 文件名格式：YYYY-MM-DD-文章标题.md
   - 包含YAML前置元数据（categories, date, title, tags等）

## 转换步骤

### 1. 安装必要的转换工具
- 安装html2text库用于HTML到Markdown转换
- 确保BeautifulSoup4已安装用于HTML解析

### 2. 编写转换脚本
创建Python脚本 `convert_html_to_md.py`，实现以下功能：
- 遍历old_blog目录下所有HTML文件
- 从HTML文件中提取关键信息：
  - 标题（<h1>标签）
  - 日期（从目录结构推断：YYYY/MM/DD）
  - 分类和标签（从HTML内容或目录名推断）
- 将HTML内容转换为Markdown格式
- 生成符合Jekyll规范的YAML前置元数据
- 以正确的文件名保存到_posts目录

### 3. 执行转换
- 运行转换脚本
- 检查生成的Markdown文件格式是否正确
- 验证文件是否符合Jekyll规范

### 4. 测试和调整
- 运行Jekyll本地服务器测试转换后的文件
- 检查是否有格式问题或内容丢失
- 根据需要调整转换脚本

## 技术实现要点

1. **日期提取**：从目录结构YYYY/MM/DD提取日期信息
2. **标题提取**：从HTML的<h1>标签获取文章标题
3. **内容转换**：使用html2text库将HTML正文转换为Markdown
4. **YAML生成**：确保生成正确的YAML前置元数据
5. **文件名生成**：使用YYYY-MM-DD-文章标题.md格式

## 预期结果

- 所有HTML文件成功转换为Markdown格式
- 生成的文件符合Jekyll规范
- 文章内容完整保留
- 分类和标签信息正确提取
- 可以在Jekyll环境中正常展示
