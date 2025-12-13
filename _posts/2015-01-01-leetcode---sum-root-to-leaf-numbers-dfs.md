---
categories: Posts
date: 2015-01-01 00:00:00
title: LeetCode - Sum Root to Leaf Numbers (DFS)
tags: []
layout: post
---

## 题意

输出所有经过路径组成的数字的和。

## 代码


```c++
class Solution {
public:
    int ans;
    void DFS(TreeNode *cur, int curAdd)
    {
        int curAns = curAdd + cur->val;
        if (cur->left != NULL) DFS(cur->left, curAns * 10);
        if (cur->right != NULL) DFS(cur->right, curAns * 10);
        if (cur->left == 0 && cur->right == 0) ans += curAns;
    }
    
    int sumNumbers(TreeNode *root) {
        if (root == 0) return 0;
        ans = 0;
        DFS(root, 0);
        return ans;
    }
};
```