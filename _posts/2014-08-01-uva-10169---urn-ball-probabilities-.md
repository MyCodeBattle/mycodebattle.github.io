---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10169 - Urn-ball Probabilities !
tags: []
layout: post
---

## 传送门

[UVa 10169 - Urn-ball Probabilities !](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1110&mosmsg=Submission+received+with+ID+13975621)

## 题意

有两个盒子，刚开始的时候第一个里面只有一个红球，第二个里有两个球，一红一白。

每轮从每个盒子里各拿出一个球，之后各放入一个白球，放回红球。

给出玩的次数，求在这么多次当中至少有一次拿到两个红球的概率和全部拿到两个红球的概率p小数点后连续的0的个数。

## 思路

在某次的时候，拿到两个红球的概率$P=\dfrac {1} {i\left( i+1\right) }$，其它情况是$1 - p$

那么，直到某次的时候，至少拿到一次两个红球的概率是

$$q *= (1 - P)$$  
$$P_{ans} = 1 - q * (1 - P)$$

q是直到目前为止没有拿过一次两个红球的概率。

至于统计0的个数，设$P = 10^a$为全是两个红球的概率。

设i和d分别为p的整数部分和小数部分。i部分只改变位数，所以要的就是i的值。

$$\log \left( P^{i+d}\right) = i + d$$

## 代码
    
    
    12345678910111213141516171819202122232425

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std;const int MAXN = 1e6; double dp[MAXN];    //at least one pick are two red ballsint ans[MAXN]; int main(){    int n;    LL i, j;    double p = 1, q = 1, t = 0;    for (i = 1; i <= MAXN; i++)    {        p = 1.0 / i / (i + 1);        q *= (1 - p);        dp[i] =  1 - q;        t += log10(1.0 * i * (i + 1));        ans[i] = (int)(t - fmod(t, 1));    }    while (~scanf("%d", &n))       printf("%.6f %d\n", dp[n], ans[n]);    return 0;}
```