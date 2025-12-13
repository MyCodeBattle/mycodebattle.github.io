---
categories: Posts
date: 2014-09-13 00:00:00
title: LeetCode - Pascal's Triangle
tags: []
layout: post
---

## 题意

输出杨辉三角

## 思路

照着输就行。

## 代码


```c++
class Solution {
    vector<vector<int> >vve;
public:
    vector<vector<int> > generate(int numRows) {
        for (int i = 1; i <= numRows; i++)
        {
            vector<int> cur;
            for (int j = 0; j < i; j++)
            {
                if (j == 0) cur.push_back(1);
                else
                {
                    if (j != i - 1)
                        cur.push_back(vve[i - 2][j] + vve[i - 2][j - 1]);
                    else
                        cur.push_back(1);
                }
            }
            vve.push_back(cur);
        }
        return vve;
    }
};
```