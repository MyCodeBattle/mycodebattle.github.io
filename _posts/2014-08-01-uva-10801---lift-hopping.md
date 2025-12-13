---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10801 - Lift Hopping
tags: []
layout: post
---

## 传送门

[UVa 10801 - Lift Hopping](http://vjudge.net/problem/viewProblem.action?id=22172)

## 题意

有n部电梯，每部电梯可能到也可能到不了某个楼层。现在要去指定楼层，每次换乘电梯都要等60s。输出最短时间。

## 思路

如果这个不是图论专题真想不到这也可以转化为求最短路。

真是奇妙（๑•̀ㅂ•́)و✧

每部电梯可以到的地方可以连成图，所用时间就是权，这样就可以建图了。

然后就八仙过海各显神通啦，什么Dijkstra, Floyd, SPFA……尽管往上做。因为目前只会Floyd，先用这个写一下，下午熟悉一下Dijkstra。

换乘就是换边，这时候加上60s就行。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 100;const int INF = 0x3f3f3f3f; typedef pair<int, int> pii;priority_queue<pii, vector<pii>, greater<pii> >q;int mp[MAXN][MAXN], d[MAXN]; void Floyd(){    for (int k = 0; k < MAXN; k++)        for (int i = 0; i < MAXN; i++)            for (int j = 0; j < MAXN; j++)                mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j] + 60);} void Dijkstra(int start){    int i, j;    for (i = 0; i < MAXN; i++)        d[i] = INF;    d[start] = 0;    q.push(make_pair(d[start], start));    while (!q.empty())    {        pii t = q.top();        q.pop();        int u = t.second;        if (t.first != d[u])            continue;        for (int v = 0; v < MAXN; v++)            if (u == 0)            {                if (d[v] > d[u] + mp[u][v])                {                    d[v] = d[u] + mp[u][v];                    q.push(make_pair(d[v], v));                }            }            else                if (d[v] > d[u] + mp[u][v] + 60)                {                    d[v] = d[u] + mp[u][v] + 60;                    q.push(make_pair(d[v], v));                }    }} void SPFA(int start){    int vis[MAXN];    queue<int> q;    memset(vis, 0, sizeof vis);    for (int i = 0; i < MAXN; i++)        d[i] = INF;    d[start] = 0;    q.push(start);    while (!q.empty())    {        int u = q.front();        q.pop();        vis[u] = 0;        for (int i = 0; i < MAXN; i++)            if (u == 0)            {                if (d[i] > d[u] + mp[u][i])                {                    d[i] = d[u] + mp[u][i];                    if (!vis[i])                        vis[i] = 1, q.push(i);                }            }            else            {                if (d[i] > d[u] + mp[u][i] + 60)                {                    d[i] = d[u] + mp[u][i] + 60;                    if (!vis[i])                        vis[i] = 1, q.push(i);                }            }    }} int main(){    //freopen("input.txt", "r", stdin);    int nele, target, i, j;    int t[10], d[MAXN];    while (~scanf("%d%d%*c", &nele, ⌖))    {        memset(mp, 0, sizeof mp);        for (i = 0; i < nele; i++)            scanf("%d%*c", &t[i]);        for (i = 0; i < MAXN; i++)            for (j = 0; j < MAXN; j++)                mp[i][j] = (i == j ? 0 : INF);        char ch = 0;        for (i = 0; i < nele; i++)        {            for (j = 0; ch != '\n'; j++)                scanf("%d%c", &d[j], &ch);            for (int k = 0; k < j; k++)                for (int l = k + 1; l < j; l++)                {                    int &cur = mp[d[k]][d[l]];                    cur = min(cur, abs(d[k] - d[l]) * t[i]);                    mp[d[l]][d[k]] = cur;                }            ch = 0;        }        //Floyd();        //Dijkstra(0);        //SPFA(0);        mp[0][target] == INF ? printf("IMPOSSIBLE\n") : printf("%d\n", mp[0][target]);    }    return 0;}
```