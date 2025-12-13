---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10048 - Audiophobia
tags: []
layout: post
---

## 传送门

[UVa 10048 - Audiophobia](http://vjudge.net/problem/viewProblem.action?id=22156)

## 题意

找出经过任意两点间的权的最大值

## 思路

改一下Floyd就行。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 100 + 10;const int INF = 0x3f3f3f3f; int dis[MAXN][MAXN], mp[MAXN][MAXN], n; void Floyd(){    for (int k = 1; k <= n; k++)        for (int i = 1; i <= n; i++)            for (int j = 1; j <= n; j++)                dis[i][j] = min(max(dis[i][k], dis[k][j]), dis[i][j]);} int main(){    //freopen("input.txt", "r", stdin);    int nc, nq, i, j, a, b, c, tt = 0, cases = 0;    while (scanf("%d%d%d", &n, &nc, &nq), n + nc + nq)    {        if (tt++)            printf("\n");        for (i = 0; i <= n; i++)            for (j = 0; j <= n; j++)                dis[i][j] = (i == j ? 0 : INF);        for (i = 0; i < nc; i++)        {            scanf("%d%d%d", &a, &b, &c);            dis[a][b] = dis[b][a] = c;        }        Floyd();        printf("Case #%d\n", ++cases);        for (i = 0; i < nq; i++)        {            scanf("%d%d", &a, &b);            if (dis[a][b] == INF)                printf("no path\n");            else                printf("%d\n", dis[a][b]);        }    }    return 0;}
```