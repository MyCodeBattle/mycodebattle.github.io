---
categories: Posts
date: 2014-08-01 00:00:00
title: HDU 1548 - A strange lift
tags: []
layout: post
---

## 传送门

[HDU 1548 - A strange lift](http://vjudge.net/vjudge/problem/viewProblem.action?id=18359)

## 题意

有个电梯，每层只能上下固定的层数，求到达目的地最小的换乘次数

## 思路

建图就行。

不过Floyd死活过不去(°∀°)ﾉ

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758

| ```c++
#include <cstdio>#include <cstring>#include <queue>using namespace std;#define LL long longconst int MAXN = 200 + 5;const int INF = 0x3f3f3f3f; int mp[MAXN][MAXN], n, d[MAXN];typedef pair<int, int> pii;priority_queue<pii, vector<pii>, greater<pii> > qu; void Dijkstra(int st){    memset(d, 0x3f, sizeof d);    d[st] = 0;    qu.push(make_pair(d[st], st));    while (!qu.empty())    {        pii u = qu.top();        qu.pop();        int x = u.second;        if (d[x] != u.first)            continue;        for (int v = 1; v <= n; v++)            if (d[v] > d[x] + mp[x][v])            {                d[v] = d[x] + mp[x][v];                qu.push(make_pair(d[v], v));            }    }} int main(){    //freopen("input.txt", "r", stdin);    int st, ed, i, j;    while (scanf("%d", &n), n)    {        scanf("%d%d", &st, &ed);        int k = 0;        for (i = 1; i <= n; i++)            for (j = 1; j <= n; j++)                mp[i][j] = (i == j ? 0 : INF);        int t;        for (i = 1; i <= n; i++)        {            scanf("%d", &t);            if (i + t <= n)                mp[i][i + t] = 1;            if (i - t >= 1)                mp[i][i - t] = 1;        }        Dijkstra(st);        printf("%d\n", d[ed] == INF ? -1 : d[ed]);    }    return 0;}
```