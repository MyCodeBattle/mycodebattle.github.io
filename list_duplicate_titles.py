import os
import re

posts_dir = '/Users/zhuolx/Documents/mycodebattle.github.io/_posts'

print("找到的重复标题文章列表：")
print("=" * 80)
print(f"{'文件名':<60} {'标题':<20}")
print("=" * 80)

for filename in os.listdir(posts_dir):
    if filename.endswith('.md'):
        file_path = os.path.join(posts_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 检查是否包含front matter中的title
        front_matter_title_match = re.search(r'^title:(.+)$', content, re.MULTILINE)
        # 检查是否包含内容中的# 标题格式
        content_title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        
        if front_matter_title_match and content_title_match:
            front_matter_title = front_matter_title_match.group(1).strip()
            content_title = content_title_match.group(1).strip()
            print(f"{filename:<60} {front_matter_title:<20}")