---
categories: Posts
date: 2014-07-02 00:00:00
title: UVa 10066 - The Twin Towers
tags: []
layout: post
---

## 传送门

[UVa 10066 - The Twin Towers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1007&mosmsg=Submission+received+with+ID+13820387)

## 思路

最长公共子序列

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 100 + 10;

int dp[MAXN][MAXN];

int main()
{
    //freopen("input.txt", "r", stdin);
    int fnum[MAXN], snum[MAXN], fn, sn, i, j, cases = 1;
    while (scanf("%d%d", &fn, &sn), fn && sn)
    {
        memset(dp, 0, sizeof(dp));
        for (i = 0; i < fn; i++)
            scanf("%d", &fnum[i]);
        for (i = 0; i < sn; i++)
            scanf("%d", &snum[i]);
        for (i = 1; i <= fn; i++)
            for (j = 1; j <= sn; j++)
                if (fnum[i - 1] == snum[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        printf("Twin Towers #%d\n", cases++);
        printf("Number of Tiles : %d\n\n", dp[fn][sn]);
    }
    return 0;
}
```