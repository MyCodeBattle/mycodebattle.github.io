---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Merge Sorted Array
tags: []
layout: post
---

## 题意

把两个排好序的数组合并到第一个里。

## 思路

从后面开始合并，这样不用移动原来数组中的元素。

## 代码


```c++
class Solution {
public:
    void merge(int A[], int m, int B[], int n)
    {
        int i = m - 1, j = n - 1, pos = m + n - 1;
        while (1)
        {
            if (j < 0)
            {
                while (i >= 0) A[pos--] = A[i--];
                break;
            }
            if (i < 0)
            {
                while (j >= 0) A[pos--] = B[j--];
                break;
            }
            if (A[i] < B[j]) A[pos--] = B[j--];
            else A[pos--] = A[i--];
            if (pos < 0) break;
        }
    }
};
```