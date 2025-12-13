#!/usr/bin/env python3
import os
import re

def extract_title(file_path):
    """Extract the title from the YAML front matter of a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match the title field in YAML front matter
    match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def find_duplicate_titles(posts_dir):
    """Find duplicate titles in markdown files."""
    title_map = {}
    
    # Iterate through all markdown files in the posts directory
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            title = extract_title(file_path)
            if title:
                if title in title_map:
                    title_map[title].append(file_path)
                else:
                    title_map[title] = [file_path]
    
    # Filter for titles that appear more than once
    duplicates = {title: files for title, files in title_map.items() if len(files) > 1}
    
    return duplicates

def main():
    posts_dir = '_posts'
    duplicates = find_duplicate_titles(posts_dir)
    
    if duplicates:
        print("Found duplicate titles:")
        print("=" * 50)
        for title, files in duplicates.items():
            print(f"Title: '{title}'")
            print(f"Files: {len(files)}")
            for file in files:
                print(f"  - {file}")
            print("-" * 50)
    else:
        print("No duplicate titles found.")

if __name__ == "__main__":
    main()
