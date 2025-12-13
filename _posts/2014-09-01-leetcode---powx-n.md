---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Pow(x, n)
tags: []
layout: post
---

## 思路

一开始直接交了一发pow(x, n)，RE了。

后来按正常的方法写了一发，TLE了。

只能用快速幂

注意处理n < 0的情况。

## 代码
    
    
    12345678910111213141516171819

| ```c++
class Solution {public:    double pow(double a, int m)    {        if (a == 1) return 1;        if (a == 0) return 0;        bool flag = m > 0 ? false : true;        if (flag) m = -m;        double ans = 1;        while (m > 0)        {            if (m & 1)                ans = ans * a;            a = a * a;            m >>= 1;        }        return flag ? 1 / ans : ans;    }};
```