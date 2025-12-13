---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10006 - Carmichael Numbers
tags: []
layout: post
---

## 传送门

[UVa 10006 - Carmichael Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=947)

## 题意

给数字，判断是不是“Carmichael Numbers”。

## 思路

先筛出素数，再用快速幂取模判断是否满足条件。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 66000; int vis[MAXN]; LL PowMod(LL a, LL m, LL n){    if (m == 1)        return a % n;    LL x = PowMod(a, m >> 1, n);    LL ans = x * x % n;    if (m & 1)        ans = ans * a % n;    return ans;} int main(){    //freopen("input.txt", "r", stdin);    LL n, i;    for (i = 2; i <= MAXN; i++)        if (!vis[i])            for (LL j = i * i; j <= MAXN; j += i)                vis[j] = 1;    while (scanf("%lld", &n), n)    {        if (!vis[n])        {            printf("%lld is normal.\n", n);            continue;        }        for (i = 2; i < n; i++)            if (i != PowMod(i, n, n))            {                printf("%lld is normal.\n", n);                break;            }        if (i == n)            printf("The number %lld is a Carmichael number.\n", n);    }    return 0;}
```