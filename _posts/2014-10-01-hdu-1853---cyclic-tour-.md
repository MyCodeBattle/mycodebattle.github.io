---
categories: Posts
date: 2014-10-01 00:00:00
title: HDU 1853 - Cyclic Tour (最小费用最大流)
tags: []
layout: post
---

#  [HDU 1853 - Cyclic Tour (最小费用最大流)](/2014/10/HDU-1853/ "HDU 1853 - Cyclic Tour \(最小费用最大流\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 16 2014 19:12

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

求把每个点都属于一个环，环的最小权和。

## 思路

学习了最小费用最大流求环的最小权的方法。

把一个点拆成两个，控制入度和出度，如果最后的流量等于一开始的流量，就可以。

不过奇怪的是在另外一题完全一样的题里我的模板竟然TLE了。。。再多做几题看看

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 300 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cap, flow, cost;}; struct MCMF{    int m, st, ed;    vector<EDGE> edges;    int head[MAXN], next[MAXN * MAXN];    int inq[MAXN];  //是否在队列中    int d[MAXN];    //bellman-Ford    int p[MAXN];    //上一条弧    int a[MAXN];    //可改进量     void init(int n)    {        this->ed = n;        MS(head, -1);        edges.clear();    }     void add_edge(int from, int to, int cap, int cost)    {        edges.PB((EDGE){from, to, cap, 0, cost});        edges.PB((EDGE){to, from, 0, 0, -cost});        m = SZ(edges);        next[m - 2] = head[from]; head[from] = m - 2;        next[m - 1] = head[to]; head[to] = m - 1;    }     bool SPFA(int st, int ed, int &flow, int &cost)    {        fill(d, d + ed + 1, INF);        MS(inq, 0);        d[st] = 0; inq[st] = 1; p[st] = -1; a[st] = INF;        queue<int> qu;        qu.push(st);        while (!qu.empty())        {            int u = qu.front(); qu.pop();            inq[u] = 0;            for (int i = head[u]; i != -1; i = next[i])            {                EDGE &e = edges[i];                if (e.cap > e.flow && d[e.to] > d[u] + e.cost)                {                    d[e.to] = d[u] + e.cost;                    p[e.to] = i;                    a[e.to] = min(a[u], e.cap - e.flow);                    if (!inq[e.to])                        qu.push(e.to), inq[e.to] = 1;                }            }        }        if (d[ed] == INF) return false;        flow += a[ed]; cost += d[ed] * a[ed];        int u = ed;        while (u != st)        {            edges[p[u]].flow += a[ed];            edges[p[u] ^ 1].flow -= a[ed];            u = edges[p[u]].from;        }        return true;    } }MFMC; int main(){    //ROP;    int T, i, j, ncity, nway;    while (~scanf("%d%d", &ncity, &nway))    {        int st = 0, ed = 2 * ncity + 1;        MFMC.init(ed);        while (nway--)        {            int a, b, c;            scanf("%d%d%d", &a, &b, &c);            MFMC.add_edge(a, b + ncity, 1, c);        }        for (i = 1; i <= ncity; i++)        {            MFMC.add_edge(st, i, 1, 0);            MFMC.add_edge(i + ncity, ed, 1, 0);            //MFMC.add_edge(i, i + ncity, 1, 0);        }        int cost = 0, flow = 0;        while (MFMC.SPFA(st, ed, flow, cost));        if (flow == ncity) printf("%d\n", cost);        else printf("-1\n");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Graph - Flow Network](/tags/Graph-Flow-Network/)
