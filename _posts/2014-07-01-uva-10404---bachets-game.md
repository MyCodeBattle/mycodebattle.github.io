---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10404 - Bachet's Game
tags: []
layout: post
---

## 传送门

[UVa 10404 - Bachet’s Game](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1345&mosmsg=Submission+received+with+ID+13848531)

## 题意

两个人取石头，轮流，谁取完就赢，问两个人都表现完美的情况下谁赢

## 思路

参考了[GoomMaple的解题报告](http://blog.csdn.net/goomaple/article/details/8882201)  
用0和1分别表示A必输和必赢的两种状态，然后开始递推。如果最后dp[n]是1，说明这种状态是必赢的，反之则必输。

## 代码


```c++
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 1000000 + 1000;

int dp[MAXN], stone[20];

int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, n, m;
    while (~scanf("%d%d", &n, &m))
    {
        memset(dp, 0, sizeof(dp));
        for (i = 0; i < m; i++)
            scanf("%d", &stone[i]);
        for (i = 1; i <= n; i++)
            for (j = 0; j < m; j++)
                if (i >= stone[j] && dp[i - stone[j]] == 0)
                {
                    dp[i] = 1;
                    break;
                }
        if (dp[n])
            printf("Stan wins\n");
        else
            printf("Ollie wins\n");
    }
    return 0;
}
```