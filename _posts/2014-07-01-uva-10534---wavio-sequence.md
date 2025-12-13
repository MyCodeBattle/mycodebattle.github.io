---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10534 - Wavio Sequence
tags: []
layout: post
---

## 传送门

[UVa 10534 - Wavio Sequence](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1475&mosmsg=Submission+received+with+ID+13854295)

## 题意

从给定的序列中找出一个波浪序列，使前n + 1个数严格递增，后n + 1个数严格递减

## 思路

从两边分别找出以每个位置结束的最长递增序列，然后取他们两边的最小值。因为长度必须要相等，但是可以牺牲长的。  
一开始用$O(n^2)$的dp，TLE了。参考了**shuangde800** 的解题报告才了解还有一种$O(nlogn)$的方法。学习之。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748

| ```c++
#include <cstdio>#include <vector>#include <algorithm>using namespace std;const int MAXN = 10000 + 100; int num[MAXN], left[MAXN], right[MAXN];vector<int> ve; ​int main(){    //freopen("in.txt", "r", stdin);    int T, i, j, n;    while (~scanf("%d", &n))    {        for (i = 0; i < n; i++)            scanf("%d", #[i]);        ve.clear();        for (i = 0; i < n; i++)        {            if (ve.empty() || num[i] > ve.back())                ve.push_back(num[i]);            else            {                int t = lower_bound(ve.begin(), ve.end(), num[i]) - ve.begin();                ve[t] = num[i];            }            left[i] = ve.size();        }        ve.clear();        for (i = n - 1; i >= 0; i--)        {            if (ve.empty() || num[i] > ve.back())                ve.push_back(num[i]);            else            {                int t = lower_bound(ve.begin(), ve.end(), num[i]) - ve.begin();                ve[t] = num[i];            }            right[i] = ve.size();        }        int ans = 0;        for (i = 0; i < n; i++)            ans = max(ans, min(left[i], right[i]) * 2 - 1);        printf("%d\n", ans);    }    return 0;}
```