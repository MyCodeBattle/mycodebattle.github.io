---
categories: Posts
date: 2014-12-01 00:00:00
title: LeetCode - Binary Tree Level Order Traversal (DFSID)
tags: []
layout: post
---

## 题意

输出每一层结点的值。

## 思路

一星期没做题了。。哎。。

我用的DFSID。

## 代码


```c++
#include <cstdio>
#include <vector>
using namespace std;
 
class Solution {
    int depth;
    vector<vector<int> >ans;
    bool flag;
public:
    void DFSID(TreeNode *curNode, int curDep)
    {
        if (curDep > depth) return;
        if (curDep < depth)
        {
            if (curNode->left) DFSID(curNode->left, curDep + 1);
            if (curNode->right) DFSID(curNode->right, curDep + 1);
 
        }
        if (curDep == depth)
        {
            ans[depth].push_back(curNode->val);
            flag = true;
        }
    }
 
    vector<vector<int> > levelOrder(TreeNode *root) {
        if (root == 0) return ans;
        int i, j;
        depth = -1;
        flag = true;
        while (flag)
        {
            depth++;
            flag = false;
            vector<int> tmpVec;
            ans.push_back(tmpVec);
            DFSID(root, 0);
        }
        ans.pop_back();
        return ans;
    }
};
```