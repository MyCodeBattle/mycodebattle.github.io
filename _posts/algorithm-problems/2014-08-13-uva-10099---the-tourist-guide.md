---
categories: Posts
date: 2014-08-13 00:00:00
title: UVa 10099 - The Tourist Guide
tags: []
layout: post
---

## 传送门

[UVa 10099 - The Tourist Guide](http://vjudge.net/problem/viewProblem.action?id=21242)

## 题意

要从A到B，每条路上都有人数限制，求最少要走几趟

## 思路

只要找出路的最小值最大就行。用Floyd

一开始样例都看不懂，怎么算都是四趟。原来导游也算一人（ ＴДＴ）

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MAXN = 100 + 10;
const int INF = 0x3f3f3f3f;
 
int mp[MAXN][MAXN], n;
 
void Floyd()
{
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                mp[i][j] = max(min(mp[i][k], mp[k][j]), mp[i][j]);
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int nedge, i, j, a, b, c, st, ed, npeo, cases = 0;
    while (scanf("%d%d", &n, &nedge), n + nedge)
    {
        memset(mp, 0, sizeof mp);
        for (i = 0; i < nedge; i++)
        {
            scanf("%d%d%d", &a, &b, &c);
            mp[a][b] = mp[b][a] = c;
        }
        Floyd();
        scanf("%d%d%d", &st, &ed, &npeo);
        printf("Scenario #%d\n", ++cases);
        printf("Minimum Number of Trips = %.f\n\n", ceil(npeo * 1.0 / (mp[st][ed] - 1)));
    }
    return 0;
}
```