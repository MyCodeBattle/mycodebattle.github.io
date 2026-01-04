---
categories: Posts
date: 2014-07-20 00:00:00
title: UVa 10604 - Chemical Reaction
tags: []
layout: post
---

## 传送门

[UVa 10604 - Chemical Reaction](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=&problem=1545&mosmsg=Submission+received+with+ID+13913073)

## 题意

有N种化学剂，它们两两混合可以产生新的成分和热量，现在给出N个瓶子，要求计算它们混合产生的最少热量。

## 思路

用$dp[1][2][3][4][5][6]$表示六种试剂各有k瓶时能产生的最小热量。  
状态转移方程$dp[xxxxxx] = min(d[xxxxxx], dp[x - 1][y - 1][z + 1][xxx] + xy.heat)$，其中x、y是反应的两个试剂。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAXN = 40 + 5;
 
int dp[MAXN][MAXN][MAXN][MAXN], mp[MAXN][4], vis[25], layer[5], n;
 
int DFS(int cnt)
{
    int &cur = dp[layer[0]][layer[1]][layer[2]][layer[3]];
    if (cnt == 5)
        return cur = 0;
    if (cur != -1)
        return cur;
    cur = 0;
    for (int i = 0; i < 4; i++)
    {
        if (layer[i] == n)
            continue;
        int temp = mp[layer[i]++][i];
        if (vis[temp])
        {
            vis[temp] = 0;
            cur = max(cur, DFS(cnt - 1) + 1);
            vis[temp] = 1;
        }
        else
        {
            vis[temp] = 1;
            cur = max(cur, DFS(cnt + 1));
            vis[temp] = 0;
        }
        layer[i]--;
    }
    return cur;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j;
    while (scanf("%d", &n), n)
    {
        memset(dp, -1, sizeof dp);
        memset(vis, 0, sizeof vis);
        memset(layer, 0, sizeof layer);
        for (i = 0; i < n; i++)
            for (j = 0; j < 4; j++)
                scanf("%d", ∓[i][j]);
        printf("%d\n", DFS(0));
    }
    return 0;
}
```