---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10913 - Walking on a Grid
tags: []
layout: post
---

## 传送门

[UVa 10913 - Walking on a Grid](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1854&mosmsg=Submission+received+with+ID+13920500)

## 题意

从第一个格子走到最后一个，给出踩负数的最高次数，求最大权

## 思路

开一个四维数组，记录点，踩过的负数的次数，进入格子的方向。

如果从左边进来的，就不能再向左边走。以此类推

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MAXN = 75 + 5;
const int INF = 1061109567;
const int dir[3][2] = { {0, 1}, {0, -1}, {1, 0} };
 
int mp[MAXN][MAXN], vis[MAXN][MAXN][10][5], k, n;
LL dp[MAXN][MAXN][10][5], ans;
 
LL DFS(int x, int y, int kk, int way)
{
    LL &cur = dp[x][y][kk][way];
    if (vis[x][y][kk][way])
        return cur;
    vis[x][y][kk][way] = 1;
    if (mp[x][y] < 0)
        kk++;
    if (kk > k)
        return cur = -INF;
    if (x == n && y == n)
        return cur = mp[n][n];
    for (int i = 0; i < 3; i++)
    {
        int xx = x + dir[i][0], yy = y + dir[i][1];
        if (way != 1 && i == 0) //way = 1, 右方向进来
        {
            if (xx >= 1 && xx <= n && yy >= 1 && yy <= n)
            {
                if (DFS(xx, yy, kk, 0) != -INF)
                    cur = max(cur, DFS(xx, yy, kk, 0) + mp[x][y]);
            }
        }
        if (way != 0 && i == 1) //way = 0, 左方向进来
        {
            if (xx >= 1 && xx <= n && yy >= 1 && yy <= n)
            {
                if (DFS(xx, yy, kk, 1) != -INF)
                    cur = max(cur, DFS(xx, yy, kk, 1) + mp[x][y]);
            }
        }
        if (i == 2 && xx >= 1 && xx <= n && yy >= 1 && yy <= n)
        {
            if (DFS(xx, yy, kk, 2) != -INF)
                cur = max(cur, DFS(xx, yy, kk, 2) + mp[x][y]);
        }
    }
    return cur;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, cases = 0;
    while (scanf("%d%d", &n, &k), n + k)
    {
        ans = -INF;
        //memset(dp, 0xc0, sizeof dp);
        memset(vis, 0, sizeof vis);
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
            {
                scanf("%d", ∓[i][j]);
                for (int k = 0; k < 10; k++)
                    for (int l = 0; l < 5; l++)
                        dp[i][j][k][l] = -INF;
            }
        ans = DFS(1, 1, 0, 0);
        if (ans != -INF)
            printf("Case %d: %lld\n",++cases, ans);
        else
            printf("Case %d: impossible\n",++cases);
    }
    return 0;
}
```