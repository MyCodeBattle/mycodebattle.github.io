#!/bin/bash

# 清理_posts目录中的重复垃圾文章
# 保留修改时间最新的版本，删除其余旧版本

POSTS_DIR="_posts"
BACKUP_DIR="backup_duplicates_$(date +%Y%m%d_%H%M%S)"

# 创建备份目录（如果需要）
# mkdir -p "$BACKUP_DIR"

echo "开始清理重复文章..."
echo "===================="

# 遍历所有md文件，按基础文件名分组
find "$POSTS_DIR" -type f -name "*.md" | 
while read -r file; do
    # 提取文件名（不含路径）
    filename=$(basename "$file")
    # 提取基础文件名（去除日期部分）
    base_name=$(echo "$filename" | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}-//')
    # 输出分组信息（基础文件名:完整路径）
    echo "$base_name:$file"
done | 
# 按基础文件名排序
sort | 
# 按基础文件名分组
awk -F: '{files[$1] = files[$1] " " $2} END {for (base in files) print base "=" files[base]}' | 
while IFS="=" read -r base_name files; do
    # 将文件列表转换为数组
    file_array=($files)
    # 如果只有一个文件，跳过
    if [ ${#file_array[@]} -le 1 ]; then
        continue
    fi
    
    echo "\n处理重复文章组: $base_name"
    echo "------------------------"
    
    # 按修改时间排序文件，最新的在前
    sorted_files=$(ls -t "${file_array[@]}")
    
    # 提取最新的文件（第一个）
    keep_file=$(echo "$sorted_files" | head -n 1)
    
    # 提取要删除的文件（剩余的）
    delete_files=$(echo "$sorted_files" | tail -n +2)
    
    echo "保留: $keep_file"
    echo "删除:"
    
    # 实际删除模式
    for del_file in $delete_files; do
        echo "  - $del_file"
        rm "$del_file"
    done
    
    # 测试模式（已禁用）
    # for del_file in $delete_files; do
    #     echo "  - $del_file (测试模式，未删除)"
    # done
done

echo "\n===================="
echo "清理完成！"
echo "已删除所有重复的旧版本文章，只保留了修改时间最新的版本。"
