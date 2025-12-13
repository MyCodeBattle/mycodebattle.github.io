---
categories: Posts
date: 2014-07-19 00:00:00
title: UVa 607 - Scheduling Lectures
tags: []
layout: post
---

## 传送门

[UVa 607 - Scheduling Lectures](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=548)

## 题意

有N个话题，要求所用讲座数最少，并输出最小DI。

## 思路

可以用贪心的思想得出所要用的讲座数。  
$dp[i][j] = dp[i - 1][k - 1] + GetValue(total - sum[k])$，$dp[i][j]$表示前i场讲座讲j个话题所用最少DI。

## 代码


```c++
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAXN = 1100;

int dp[MAXN][MAXN], vis[MAXN][MAXN], lect[MAXN], C, total;

int GetValue(int t)
{
    if (!t)
        return 0;
    else if (t >= 1 && t <= 10)
        return -C;
    else
        return (t - 10) * (t - 10);
}

int DFS(int x, int y)
{
    int &cur = dp[x][y];
    if (vis[x][y])
        return cur;
    if (x == 0)
        if (y)
            return INF;
        else
            return 0;
    int sum = 0;
    cur = INF;
    for (int i = y; i > 0; i--)
    {
        sum += lect[i];
        if (sum > total)
            break;
        cur = min(cur, DFS(x - 1, i - 1) + GetValue(total - sum));
    }
    vis[x][y] = 1;
    return cur;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int n, i, j, cnt, cases = 0;
    while (scanf("%d", &n), n)
    {
        //memset(dp, 0x3f, sizeof dp);
        memset(vis, 0, sizeof vis);
        vis[0][0] = 1, dp[0][0] = 0;
        cnt = 1;
        scanf("%d%d", &total, &C);
        for (i = 1; i <= n; i++)
            scanf("%d", &lect[i]);
        int temp = 0;
        for (i = 1; i <= n; i++)
        {
            temp += lect[i];
            if (temp > total)
            {
                temp = lect[i];
                cnt++;
            }
        }
        if (cases)
            printf("\n");
        printf("Case %d:\n\n", ++cases);
        printf("Minimum number of lectures: %d\n", cnt);
        printf("Total dissatisfaction index: %d\n", DFS(cnt, n));
    }
    return 0;
}
```