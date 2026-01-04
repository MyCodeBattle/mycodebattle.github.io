---
categories: Posts
date: 2014-07-31 00:00:00
title: UVa 10759 - Dice Throwing
tags: []
layout: post
---

## 题意

有那个骰子，都扔到天上，求落下来的和>=m的概率。

## 思路

概率就是>=m的种类数 / 总共的种类数。

种类数可以用DP求。

转移方程$ dp[i][j] = dp[i - 1][j - k] , 1 <= k <= 6 $  
其中$dp[i][j]$表示前i个骰子总和为j的种类数。

## 代码


```c++
#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;
 
ull dp[25][151];
 
ull GCD(ull a, ull b)
{
    return !b ? a: GCD(b, a % b);
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, sum, i, j;
    for (i = 1; i <= 24; i++)
        for (j = 1; j <= 150; j++)
        {
            if (i == 1 && j <= 6)
                dp[i][j] = 1;
            for (int k = 1; k <= 6; k++)
            {
                if (j >= k)
                    dp[i][j] += dp[i - 1][j - k];
            }
        }
    while (~scanf("%d%d", &n, ∑), n + sum)
    {
        ull all = 0, cur = 0;
        for (i = n; i <= 6 * n; i++)
        {
            all += dp[n][i];
            if (i >= sum)
                cur += dp[n][i];
        }
        if (cur == all)
            printf("1\n");
        else if (cur == 0)
            printf("0\n");
        else
        {
            ull temp = GCD(all, cur);
            printf("%llu/%llu\n", cur / temp, all / temp);
        }
    }
    return 0;
}
```