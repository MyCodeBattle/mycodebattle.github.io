---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10673 - Play with Floor and Ceil
tags: []
layout: post
---

## 传送门

[UVa 10673 - Play with Floor and Ceil](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=115&page=show_problem&problem=1614)

## 题意

解方程

## 思路

继续学习。可耻地套了模板。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 1e6 + 100;const int INF = 0x3f3f3f3f; void GCDExt(LL a, LL b, LL &d, LL &x, LL &y){    if (!b)        d = a, x = 1, y = 0;    else    {        GCDExt(b, a % b, d, y, x);        y -= x * (a / b);    }} int main(){    //freopen("input.txt", "r", stdin);    LL x, y, d, a, b, k, i, j, T, c;    scanf("%lld", &T);    while (T--)    {        scanf("%lld%lld", &c, &k);        LL a = (LL)floor(c * 1.0 / k);        LL b = (LL)ceil(c * 1.0 / k);        GCDExt(a, b, d, x, y);        x *= (c / d);        y *= (c / d);        printf("%lld %lld\n", x, y);    }    return 0;}
```