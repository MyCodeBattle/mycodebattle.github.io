---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10943 - How do you add?
tags: []
layout: post
---

## 传送门

[UVa 10943 - How do you add?](http://vjudge.net/problem/viewProblem.action?id=24527)

## 思路

和前面有一题差不多。

$dp[i][j]$表示i个数字的时候和为j的情况数。

$$dp[i][j] = \sum _{k=0}^{k=i}dp\left( i-1,j-k\right) $$

## 代码
    
    
    12345678910111213141516171819202122232425262728

| ```c++
​#include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 100;const int MOD = 1e6; LL dp[110][110]; int main(){    int n, k, i, j;    for (i = 0; i <= MAXN; i++)        dp[1][i] = 1;    for (i = 2; i <= MAXN; i++)    {        dp[i][0] = 1;        for (j = 1; j <= MAXN; j++)            for (int k = 0; k <= j; k++)            {                dp[i][j] += dp[i - 1][j - k];                dp[i][j] %= MOD;            }    }    while (scanf("%d%d", &n, &k), n + k)        printf("%lld\n", dp[k][n]);    return 0;}
```