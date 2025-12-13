---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10079 - Pizza Cutting
tags: []
layout: post
---

## 传送门

[UVa 10079 - Pizza Cutting](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1020)

## 题意

求n刀最多能切几块

## 思路

耍赖了，上OEIS查了一下。

$$f\left( n\right) =\dfrac {n * \left( n+1\right) } {2} + 1$$

## 代码
    
    
    1234567891011

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std; int main(){    LL ans, n;    while (~scanf("%lld", &n), n >= 0)        printf("%lld\n", n * (n + 1) / 2 + 1);    return 0;}
```