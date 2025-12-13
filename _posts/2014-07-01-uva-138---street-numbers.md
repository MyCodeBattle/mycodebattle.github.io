---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 138 - Street Numbers
tags: []
layout: post
---

## 传送门

[UVa 138 - Street Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=115&page=show_problem&problem=74)

## 题意

某个人出门，向左走的和和向右走的和一样，求它的门牌号，输出10个。

## 思路

列出方程，化简可得$2k^2 = n^2 + n$, 进一步化简得$(2n+1)^2-2(2k^2)=1$，这也是佩尔方程的基本形式。

设$x = 2n+1, y = 2k$，得$x^2 - 2y^2 = 1$

$$x_{i+1} = x_1x_i + ny_1y_i$$

$$y_{i+1} = x_1y_i + y_1x_i$$

只要用一个变量保存x即可。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
 
int main()
{
    int i, j, x, y, X0 = 3, Y0 = 2;
    x = X0, y = Y0;
    for (i = 0; i < 10; i++)
    {
        int t = x;
        x = 3 * t + 2 * 2 * y;
        y = 3 * y + 2 * t;
        printf("%10d%10d\n", y >> 1, (x - 1) >> 1);
    }
    return 0;
}
```