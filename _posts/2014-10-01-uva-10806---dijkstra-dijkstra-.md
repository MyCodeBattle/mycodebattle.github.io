---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 10806 - Dijkstra, Dijkstra. (费用流)
tags: []
layout: post
---

## 题意

求有权无向图中来回的最短路，第一次走过的路不可以再走。

想不通为什么不能求两次最短路。这题竟然是网络流的模型，涨姿势了。

把所有边的容量设为1，建一个源点，到点1的容量2，建一个汇点，到点n的容量2。然后跑最小费用最大流，当流量达到2的时候说明可以，输出cost。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146

| ```c++
​#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 110 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cap, flow, cost;}; struct MCMF{    int n, m, st, ed;    vector<EDGE> edges;    vector<int> G[MAXN];    int inq[MAXN];  //是否在队列中    int d[MAXN];    //bellman-Ford    int p[MAXN];    //上一条弧    int a[MAXN];    //可改进量     void init(int n)    {        this->n = n;        for (int i = 0; i < n; i++) G[i].clear();        edges.clear();    }     void add_edge(int from, int to, int cap, int cost)    {        edges.PB((EDGE){from, to, cap, 0, cost});        edges.PB((EDGE){to, from, 0, 0, -cost});        m = SZ(edges);        G[from].PB(m - 2);        G[to].PB(m - 1);    }     bool SPFA(int st, int ed, int &flow, int &cost)    {        fill(d, d + n + 1, INF);        MS(inq, 0);        d[st] = 0; inq[st] = 1; p[st] = -1; a[st] = INF;        queue<int> qu;        qu.push(st);        while (!qu.empty())        {            int u = qu.front(); qu.pop();            inq[u] = 0;            for (int i = 0; i < SZ(G[u]); i++)            {                EDGE &e = edges[G[u][i]];                if (e.cap > e.flow && d[e.to] > d[u] + e.cost)                {                    d[e.to] = d[u] + e.cost;                    p[e.to] = G[u][i];                    a[e.to] = min(a[u], e.cap - e.flow);                    if (!inq[e.to])                        qu.push(e.to), inq[e.to] = 1;                }            }        }        if (d[ed] == INF) return false;        flow += a[ed]; cost += d[ed] * a[ed];        int u = ed;        while (u != st)        {            edges[p[u]].flow += a[ed];            edges[p[u] ^ 1].flow -= a[ed];            u = edges[p[u]].from;        }        return true;    }     void min_cost(int st, int ed)    {        int flow = 0, cost = 0;        while (SPFA(st, ed, flow, cost))        {            if (flow == 2)            {                printf("%d\n", cost);                return;            }        }        puts("Back to jail");    }}MC; int main(){    //ROP;    int n, m;    while (scanf("%d", &n), n)    {        scanf("%d", &m);        MC.init(n + 5);        MC.add_edge(0, 1, 2, 0);        MC.add_edge(n, n + 1, 2, 0);        while (m--)        {            int a, b, c;            scanf("%d%d%d", &a, &b, &c);            MC.add_edge(a, b, 1, c);            MC.add_edge(b, a, 1, c);        }        MC.min_cost(0, n + 1);    }    return 0;}
```