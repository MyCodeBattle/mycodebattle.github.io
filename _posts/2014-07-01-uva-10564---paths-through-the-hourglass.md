---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10564 - Paths through the Hourglass
tags: []
layout: post
---

## 传送门

[UVa 10564 - Paths through the Hourglass](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1505&mosmsg=Submission+received+with+ID+13892959)

## 题意

看有没有一条路的和是sum，先输出路的总条数，如果有很多条，输出字典序最小的。

## 思路

状态转移方程$dp[i][j][s] = dp[i + 1][j][s - v] + dp[i + 1][j + 1][s - v]$，下面的方程。

$dp[i][j][s] = dp[i + 1][j][s - v] + dp[i + 1][j - 1][s - v]$，这是上面的方程，临界的时候要简单处理一下。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std;const int MAXN = 50; LL dp[MAXN][25][550];int n, mp[MAXN][25]; void PrintAns(int i, int j, int v){    if (i == 2 * n - 2)        return;    int k = mp[i][j];    if (i < n - 1)    {        if (j > 0 && dp[i + 1][j - 1][v - k])        {            printf("L");            PrintAns(i + 1, j - 1,v - k);            return;        }        printf("R");        PrintAns(i + 1, j, v - k);    }    else    {        if (dp[i + 1][j][v - k])        {            printf("L");            PrintAns(i + 1, j, v - k);            return;        }        printf("R");        PrintAns(i + 1, j + 1, v - k);    }} int main(){    //freopen("input.txt", "r", stdin);    int sum, i, j;    LL ans;    while (scanf("%d%d", &n, ∑), n + sum)    {        ans = 0;        memset(dp, 0, sizeof dp);        for (i = 0; i < n; i++)            for (j = 0; j < n - i; j++)                scanf("%d", ∓[i][j]);        for (i = n; i < 2 * n - 1; i++)            for (j = 0; j < i - n + 2; j++)                scanf("%d", ∓[i][j]);        for (i = 0; i < n; i++)            dp[2 * n - 2][i][mp[2 * n - 2][i]] = 1;        for (i = 2 * n - 3; i >= n - 1; i--)            for (j = 0; j < i - n + 2; j++)            {                int v = mp[i][j];                for (int s = v; s <= sum; s++)                    dp[i][j][s] = dp[i + 1][j][s - v] + dp[i + 1][j + 1][s - v];            }        for (i = n - 2; i >= 0; i--)        {            for (j = 0; j < n - i; j++)            {                int v = mp[i][j];                for (int s = v; s <= sum; s++)                {                    if (j == 0)                        dp[i][j][s] = dp[i + 1][j][s - v];                    else if (j == n - i - 1)                        dp[i][j][s] = dp[i + 1][j - 1][s - v];                    else                        dp[i][j][s] = dp[i + 1][j][s - v] + dp[i + 1][j - 1][s - v];                }                if (i == 0)                    ans += dp[0][j][sum];            }        }        printf("%lld\n", ans);        for (i = 0; i < n; i++)            if (dp[0][i][sum])            {                printf("%d ", i);                PrintAns(0, i, sum);                break;            }        printf("\n");    }    return 0;}
```