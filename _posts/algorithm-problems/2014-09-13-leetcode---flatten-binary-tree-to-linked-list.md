---
categories: Posts
date: 2014-09-13 00:00:00
title: LeetCode - Flatten Binary Tree to Linked List
tags: []
layout: post
---

## 题意

把一个链表弄成一条链

## 思路

先序遍历一下，记录上一结点，把上一结点的left变为0，right变为当前结点。

## 代码


```c++
class Solution {
    TreeNode *last;
public:
    void DFS(TreeNode *root)
    {
        if (root != 0)
        {
            TreeNode *l = root->left;
            TreeNode *r = root->right;  
            if (last == 0) last = root;
            else
            {
                last->left = 0;
                last->right = root;
                last = root;           
            }
            DFS(l);
            DFS(r);
        }
    }
    void flatten(TreeNode *root) {
        last = 0;
        DFS(root);
    }
};
```