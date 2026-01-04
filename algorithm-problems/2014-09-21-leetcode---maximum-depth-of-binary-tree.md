---
categories: Posts
date: 2014-09-21 00:00:00
title: LeetCode - Maximum Depth of Binary Tree
tags: []
layout: post
---

## 思路

左右结点的最大值。

## 代码


```c++
class Solution {
public:
    int DFS(int dep, TreeNode *cur)
    {
        int a = 0, b = 0;
        if (cur->left)
            a = DFS(dep + 1, cur->left);
        if (cur->right)
            b = DFS(dep + 1, cur->right);
        return max(a, max(b, dep));
    }
    int maxDepth(TreeNode *root) {
        if (!root) return 0;
        int a = 1, b = 1;
        if (root->left)
            a = DFS(2, root->left);
        if (root->right)
            b = DFS(2, root->right);
        return max(a, b);
    }
};
```