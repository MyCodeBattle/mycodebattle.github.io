---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 562 - Dividing coins
tags: []
layout: post
---

## 传送门

[UVa 562 - Dividing coins](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=503&mosmsg=Submission+received+with+ID+13826496)

## 题意

给几个硬币，分成两份，求两份最小的差

## 思路

两份差最小，也就是使有一份尽量接近sum / 2，这样就是0-1背包了。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 100 + 10;

int coin[MAXN], dp[MAXN * 500];

int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, sum, temp;
    scanf("%d", &T);
    while (T--)
    {
        memset(dp, 0, sizeof(dp));
        temp = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf("%d", &coin[i]);
            temp += coin[i];
        }
        sum = temp / 2;
        for (i = 0; i < n; i++)
            for (j = sum; j >= coin[i]; j--)
                dp[j] = max(dp[j], dp[j - coin[i]] + coin[i]);
        printf("%d\n", temp - dp[sum] * 2);
    }
    return 0;
}
```