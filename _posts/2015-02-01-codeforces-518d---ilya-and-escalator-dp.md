---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 518D - Ilya and Escalator (概率DP)
tags: []
layout: post
---

## 题意

每个人要在他前面的人全部进了电梯之后才能进电梯。

一个人进电梯的概率是p。

现在问t秒后电梯里有几个人的期望。

## 思路

$dp[i][j] = dp[i-1][j] * (1-p) + dp[i-1][j-1] * p$

## 代码


```c++
double dp[MAXN][MAXN];
 
int main()
{
    int n, t;
    double p;
    scanf("%d%lf%d", &n, &p, &t);
    dp[0][0] = 1;
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dp[i+1][j+1] += dp[i][j]*p;
            dp[i+1][j] += dp[i][j]*(1-p);
        }
        dp[i+1][n] += dp[i][n];
    }
    double ans = 0;
    for (int i = 1; i <= n; i++) ans += dp[t][i] * i;
    printf("%.8f\n", ans);
    return 0;
}
```