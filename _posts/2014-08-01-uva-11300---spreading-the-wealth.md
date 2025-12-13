---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11300 - Spreading the Wealth
tags: []
layout: post
---

## 传送门

[UVa 11300 - Spreading the Wealth](http://vjudge.net/vjudge/problem/viewProblem.action?id=33899)

## 题意

有一些金币，只能给相邻的传送，问最少传送几个金币使得他们都一样

## 思路

大白上的题目，非常漂亮的分析。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int MAXN = 1e6 + 10;
const int INF = 0x3f3f3f3f;
 
int C[MAXN];
LL num[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, i, j, temp;
    while (~scanf("%d", &n))
    {
        LL sum = 0, ans = 0;
        C[0] = 0;
        for (i = 1; i <= n; i++)
        {
            scanf("%lld", #[i]);
            sum += num[i];
        }
        LL M = sum / n;
        for (i = 1; i < n; i++)
            C[i] = C[i - 1] + num[i] - M;
        sort(C, C + n);
        LL k = C[n / 2];
        for (i = 0; i < n; i++)
            ans += abs(k - C[i]);
        printf("%lld\n", ans);
    }
    return 0;
}
```