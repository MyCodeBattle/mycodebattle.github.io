---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 1511 - Invitation Cards (最短路 & Dijkstra)
tags: []
layout: post
---

#  [PKU 1511 - Invitation Cards (最短路 & Dijkstra)](/2014/10/PKU-1511/ "PKU 1511 - Invitation Cards \(最短路 & Dijkstra\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 8 2014 15:11

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

求起点到每个点的最小费用，来回。

## 思路

一开始在回来的时候每个点调用了一次Dijkstra，果断TLE。

其实把边反一下就行。

不过我用vector版邻接表跑了5S！难道是大量clear的原因？

邻接表跑了2s，vector的效率简直不忍直视。以后要投奔数组版了

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e6 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cost;}; struct HEAPNODE{    int d, u;    bool operator < (const HEAPNODE &a) const    {        return d > a.d;    }}; struct S_PATH{    int N, d[MAXN];    vector<int> G[MAXN];    vector<EDGE> edges;     void add_edge(int from, int to, int cost)    {        edges.PB((EDGE){from, to, cost});        G[from].PB(SZ(edges) - 1);    }     void init(int N)    {        this->N = N;        for (int i = 0; i <= N; i++) G[i].clear();        edges.clear();    }     void dijkstra(int st, int ed)    {        priority_queue<HEAPNODE> pqu;        fill(d, d + N + 1, INF);        d[st] = 0;        pqu.push((HEAPNODE){d[st], st});        while (!pqu.empty())        {            HEAPNODE x = pqu.top(); pqu.pop();            int u = x.u;            if (x.d != d[u]) continue;            for (int i = 0; i < SZ(G[u]); i++)            {                EDGE &e = edges[G[u][i]];                if (d[e.to] > d[u] + e.cost)                {                    d[e.to] = d[u] + e.cost;                    pqu.push((HEAPNODE){d[e.to], e.to});                }            }        }    }}s; int u[MAXN], v[MAXN], c[MAXN]; int main(){    //ROP;    int T, i, j;    scanf("%d", &T);    while (T--)    {        int nstop, n;        scanf("%d%d", &nstop, &n);        s.init(nstop + 1);        for (i = 0; i < n; i++)        {            int from, to, cost;            scanf("%d%d%d", &u[i], &v[i], &c[i]);            s.add_edge(u[i], v[i], c[i]);        }        LL fee = 0;        s.dijkstra(1, nstop);        for (i = 2; i <= nstop; i++) fee += s.d[i];        s.init(nstop);        for (i = 0; i < n; i++) s.add_edge(v[i], u[i], c[i]);        s.dijkstra(1, nstop);        for (i = 2; i <= nstop; i++) fee += (LL)s.d[i];        printf("%lld\n", fee);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Algorithm - Shortest Path](/tags/Algorithm-Shortest-Path/)
