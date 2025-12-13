---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10277 - Boastin' Red Socks
tags: []
layout: post
---

## 传送门

[UVa 10277 - Boastin’ Red Socks](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1218&mosmsg=Submission+received+with+ID+13975007)

## 题意

有红袜子和黑袜子，取出一双红袜子的概率是p / q，求红袜子和黑袜子各有多少个。

## 思路

设红袜子有m个。

$$ \dfrac {m} {n}\cdot \dfrac {m-1} {n-1}=\dfrac {np} {nq} $$

所以只要枚举m或者n就行。这里枚举n。

$t=\sqrt {np}, 如果t(t + 1) = np成立，t + 1 = m$

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std;const int MAXN = 50000; LL GCD(LL a, LL b){    return !b ? a : GCD(b, a % b);} int main(){    //freopen("input.txt", "r", stdin);    LL p, q, m, t, i, j;    while (scanf("%lld%lld", &p, &q), p + q)    {        if (p == q)        {            printf("2 0\n");            continue;        }        if (p == 0)        {            printf("0 2\n");            continue;        }        LL k = GCD(p, q);        p /= k, q /= k;        for (i = 2; i <= MAXN; i++)            if (i * (i - 1) % q == 0)            {                LL n = i * (i - 1) / q;                m = n * p;                t = (LL)sqrt(m + 0.5);                if (t * (t + 1) == m && t >= 1)                    break;            }        if (i > MAXN)            printf("impossible\n");        else            printf("%lld %lld\n", t + 1, i - t - 1);    }    return 0;}
```