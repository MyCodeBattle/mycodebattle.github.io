---
categories: Posts
date: 2014-08-01 00:00:00
title: HDU 1158 - Employment Planning
tags: []
layout: post
---

## 传送门

[HDU 1158 - Employment Planning](http://vjudge.net/vjudge/problem/viewProblem.action?id=30427)

## 题意

给出雇佣，解雇，每个月所要的花费，再给出每个月最少要有的人，求总的费用最小。

## 思路

$dp[i][j] = min(dp[i][j], dp[i][k] + (j - k) * hire + salary * j)$

k表示上个月的雇佣人数，如果k>j，说明有人被解雇了，就要换成解雇的费用，枚举k即可。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MP(a, b) make_pair(a, b)
using namespace std;
const int MAXN = 10000;
const int INF = 0x3f3f3f3f;
 
int dp[13][MAXN], pp[13];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, i, j, hire, salary, fire, nmax;
    while (scanf("%d", &n), n)
    {
        memset(dp, INF, sizeof dp);
        nmax = -1;
        scanf("%d%d%d", &hire, &salary, &fire);
        for (i = 1; i <= n; i++)
        {
            scanf("%d", &pp[i]);
            nmax = max(nmax, pp[i]);
        }
        for (i = pp[1]; i <= nmax; i++)
            dp[1][i] = i * (hire + salary);
        for (i = 2; i <= n; i++)
        {
            for (j = pp[i]; j <= nmax; j++)
                for (int k = pp[i - 1]; k <= nmax; k++)
                {
                    if (j > k)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + (j - k) * hire + j * salary);
                    else
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + (k - j) * fire + j * salary);
                }
        }
        int ans = INF;
        for (i = pp[n]; i <= nmax; i++)
            ans = min(ans, dp[n][i]);
        printf("%d\n", ans);
    }
    return 0;
}
```