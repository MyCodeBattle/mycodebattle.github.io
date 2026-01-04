---
categories: Posts
date: 2014-07-30 00:00:00
title: UVa 10375 - Choose and divide
tags: []
layout: post
---

## 传送门

[UVa 10375 - Choose and divide](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1316&mosmsg=Submission+received+with+ID+13967067)

## 题意

求两个组合数的商

## 思路

根据

$$C_{n}^{k}=\dfrac {n-k+1} {k}\cdot C_{n}^{k-1}$$

一乘一除就不会溢出。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int p, q, r, s, i, j;
    while (~scanf("%d%d%d%d", &p, &q, &r, &s))
    {
        double ans = 1;
        q = min(p - q, q);
        s = min(r - s, s);
        for (i = 1; i <= max(q, s); i++)
        {
            if (i <= q)
                ans = ans * (p - i + 1) / i;
            if (i <= s)
                ans = ans / (r - i + 1) * i;
        }
        printf("%.05f\n", ans);
    }
    return 0;
}
```