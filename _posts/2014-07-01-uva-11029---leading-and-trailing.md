---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 11029 - Leading and Trailing
tags: []
layout: post
---

## 传送门

[UVa 11029 - Leading and Trailing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1970&mosmsg=Submission+received+with+ID+13962427)

## 题意

求$a^b$的前三位和后三位。

## 思路

后三位用快速幂取模求，可耻地套了模板。

前三位参考了**kedebug** 的log大法。。

设$ a=lg\left( n\right) $，$i$和$k$为a的整数和小数部分。

则$ 10^{a}=n\Rightarrow 10^{i} * 10^{j}=n $

$10^i$无关，所以只和$10^j$有关。

## 代码
    
    
    12345678910111213141516171819202122232425262728

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std; LL PowMod(int a, int m, int n){    if (m == 1)        return a % n;    LL x = PowMod(a, m >> 1, n);    LL ans = x * x % n;    if (m & 1)        ans = ans * a % n;    return ans;} int main(){    int T, a, b;    scanf("%d", &T);    while (T--)    {        scanf("%d%d", &a, &b);        LL lans = PowMod(a, b, 1000);        int ans = (int)pow(10 * 1.0, 2 + fmod(b * log10(a), 1));        printf("%d...%03lld\n", ans, lans);    }    return 0;}
```