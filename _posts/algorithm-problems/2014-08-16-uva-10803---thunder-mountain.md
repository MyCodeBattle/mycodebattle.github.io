---
categories: Posts
date: 2014-08-16 00:00:00
title: UVa 10803 - Thunder Mountain
tags: []
layout: post
---

## 传送门

[UVa 10803 - Thunder Mountain](http://vjudge.net/vjudge/problem/viewProblem.action?id=24950)

## 题意

给一个图，两地之间的距离不能超过10KM，否则就算不连通。

如果图式强联通的，输出两点之间最长路径。

## 思路

Floyd

不过想不明白题目给的那个公式是怎么用的

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MAXN = 100 + 5;
const int INF = 0x3f3f3f3f;
 
struct POINT
{
    int x, y;
}pit[MAXN];
 
double dis[MAXN][MAXN];
int n;
 
void Floyd()
{
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, cases = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        double temp = 0;
        for (i = 0; i < n; i++)
        {
            scanf("%d%d", &pit[i].x, &pit[i].y);
            for (j = 0; j < i; j++)
            {
                temp = hypot(pit[i].x - pit[j].x, pit[i].y - pit[j].y);
                dis[i][j] = dis[j][i] = (temp > 10 ? INF : temp);
            }
        }
        Floyd();
        double ans = -1;
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                ans = max(ans, dis[i][j]);
        printf("Case #%d:\n", ++cases);
        ans == INF ? printf("Send Kurdy\n") : printf("%.4f\n", ans);
        printf("\n");
    }
    return 0;
}
```