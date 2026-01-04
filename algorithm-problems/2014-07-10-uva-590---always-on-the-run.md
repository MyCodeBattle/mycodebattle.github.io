---
categories: Posts
date: 2014-07-10 00:00:00
title: UVa 590 - Always on the run
tags: []
layout: post
---

## 传送门

[UVa 590 - Always on the run](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=531)

## 题意

小明要坐飞机度假，输入给出每个地方到其他地方的机票的价格，价格是循环的。要求求出第k天到目的地最少的钱。

## 思路

参考了[kedebug的解题报告](http://www.cnblogs.com/kedebug/archive/2012/11/19/2776892.html)  
引用一下他的说明

> 链式dp，dp[i][d]代表第d天到达i城市所需要的最小代价，于是dp[i][d] = min(dp[i][d], dp[j][d-1] + price[j][i][X])。  
> 意思是：第d天到达i城市所花费的代价是，第d-1天到达j城市 + j到i的价格 最小的一个。  
> 由于初识状态只有一个，即从城市1出发。所以初始值只有一个dp[1][0] = 0。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int INF = 0x3f3f3f3f
 
int dp[15][1100], price[15][15][35], day[15][15];
 
int main()
{
    //freopen("in.txt", "r", stdin);
    int n, k, i, j, ii, jj, cases = 1;
    while (scanf("%d%d", &n, &k) && n && k)
    {
        memset(price, 0, sizeof(price));
        memset(day, 0, sizeof(day));
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
            {
                if (i != j)
                {
                    scanf("%d", &day[i][j]);
                    for (int jj = 1; jj <= day[i][j]; jj++)
                        scanf("%d", &price[i][j][jj]);
                }
            }
        for (i = 0; i <= n; i++)
            for (j = 0; j <= k; j++)
                dp[i][j] = INF;
        dp[1][0] = 0;
        for (int d = 1; d <= k; d++)
            for (i = 1; i <= n; i++)
                for (j = 1; j <= n; j++)
                {
                    if (i != j)
                    {
                        int thatDay = (d - 1) % day[j][i] + 1;
                        if (price[j][i][thatDay] && dp[j][d - 1] != INF)
                            dp[i][d] = min(dp[i][d], dp[j][d - 1] + price[j][i][thatDay]);
                    }
                }
        printf("Scenario #%d\n", cases++);
        if (dp[n][k] != INF)
            printf("The best flight costs %d.\n\n", dp[n][k]);
        else
            printf("No flight possible.\n\n");
 
    }
    return 0;
}
```