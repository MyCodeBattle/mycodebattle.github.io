---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 11258 - String Partition
tags: []
layout: post
---

## 传送门

[UVa 11258 - String Partition](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=2225&mosmsg=Submission+received+with+ID+13925995)

## 题意

给一个数字字符串，可以任意分割，求它们最大的和。

## 思路

可以对字符串预处理，求出每个区间的大小。

$dp[i]$表示前i个数字的最大和。  
状态转移方程$dp[i] = dp[j] + dp[j + 1][i]，(0 <= j < i)$

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MAXN = 200 + 10;
const int INF = 2147483647;
 
LL sum[MAXN][MAXN], dp[MAXN];
char str[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int len, i, j, T;
    scanf("%d%*c", &T);
    while (T--)
    {
        memset(dp, 0, sizeof dp);
        memset(sum, 0, sizeof sum);
        gets(str + 1);
        len = strlen(str + 1);
        for (i = 1; i <= len; i++)
        {
            LL temp = 0;
            for (j = i; j <= len; j++)
            {
                temp = temp * 10 + str[j] - '0';
                if (temp > INF)
                    break;
                sum[i][j] = temp;
            }
        }
        for (i = 1; i <= len; i++)
            for (j = 0; j < i; j++)
                dp[i] = max(dp[i], dp[j] + sum[j + 1][i]);
        printf("%lld\n", dp[len]);
    }
    return 0;
}
```