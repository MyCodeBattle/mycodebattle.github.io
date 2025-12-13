---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 3496 - Watch The Movie (二维背包)
tags: []
layout: post
---

## 题意

小明看电影有限制，最多选m部，看l分钟长。问在此前提下他能获得的最大满意值。

## 思路

二维背包。要滚一下。

## 代码
    
    
    123456789101112131415161718192021222324

| ```c++
int dp[110][1100];pii arr[MAXN]; int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        int n, m, l;        scanf("%d%d%d", &n, &m, &l);        for (int i = 0; i <= m; i++)            for (int j = 0; j <= l; j++)                dp[i][j] = (i == 0 ? 0 : -INF);        for (int i = 1; i <= n; i++) scanf("%d%d", &arr[i].X, &arr[i].Y);        for (int i = 1; i <= n; i++)            for (int j = m; j >= 1; j--)                for (int k = l; k >= arr[i].X; k--)                    dp[j][k] = max(dp[j][k], dp[j-1][k-arr[i].X] + arr[i].Y);        printf("%d\n", max(0, dp[m][l]));    }    return 0;}
```