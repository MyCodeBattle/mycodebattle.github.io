---
categories: Posts
date: 2014-08-05 00:00:00
title: UVa 10910 - Marks Distribution
tags: []
layout: post
---

## 传送门

[UVa 10910 - Marks Distribution](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1851)

## 题意

有n门科目，总分sum，最低分k，求有多少种情况。

## 思路

$dp(i, j) += dp(i - 1, k)$

$dp(i, j)$表示前i个课程总分为j的情况有多少

还是记忆化搜索用得顺手╰（￣▽￣）╭

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int MAXN = 70;
 
LL dp[80][80];
int rem, n, sum, least;
 
LL DFS(int n, int curSum, int res)
{
    if (sum - res < least)
        return 0;
    if (n == 1)
        return 1;
    LL &cur = dp[n][curSum];
    if (cur != -1)
        return cur;
    cur = 0;
    for (int i = least; i <= least + rem; i++)
        if (curSum >= i)
            cur += DFS(n - 1, curSum - i, res + i);
    return cur;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, T;
    scanf("%d", &T);
    while (T--)
    {
        memset(dp, -1, sizeof dp);
        scanf("%d%d%d", &n, ∑, &least);
        rem = sum - n * least;
        printf("%lld\n", DFS(n, sum, 0));
    }
    return 0;
}
```