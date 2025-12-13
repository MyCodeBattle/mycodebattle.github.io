---
categories: Posts
date: 2014-10-01 00:00:00
title: HDU 3605 - Escape (多重匹配 | 最大流 & Dinic)
tags: []
layout: post
---

#  [HDU 3605 - Escape (多重匹配 | 最大流 & Dinic)](/2014/10/HDU-3605/ "HDU 3605 - Escape \(多重匹配 | 最大流 & Dinic\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 11 2014 20:36

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

折腾一天了这题。

10W的数据量，普通的网络流建图会TLE。

学习了缩点。就是把重复的点压缩，然后容量上增加。一共只有 (1 << 10)种状况。

后来用多重匹配写的时候竟然无限RE，现在还没找出原因。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1500 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cap, flow;}; struct DINIC{    int d[MAXN], cur[MAXN], vis[MAXN], st, ed;    vector<EDGE> edges;    vector<int> G[MAXN];    void add_edge(int from, int to, int cap)    {        EDGE a = {from, to, cap, 0};        EDGE b = {to, from, 0, 0};        edges.PB(a);        edges.PB(b);        int m = SZ(edges);        G[from].PB(m - 2); G[to].PB(m - 1);    }     void init(int st, int ed)    {        this->st = st, this->ed = ed;        edges.clear();        for(int i = 0; i <= ed; i++) G[i].clear();    }     int maxFlow()    {        int flow = 0;        while (BFS())        {            MS(cur, 0);            flow += DFS(st, INF);        }        return flow;    }     bool BFS()    {        MS(vis, 0);        queue<int> qu;        qu.push(st);        d[st] = 0; vis[st] = 1;        while (!qu.empty())        {            int x = qu.front(); qu.pop();            for (int i = 0; i < SZ(G[x]); i++)            {                EDGE &e = edges[G[x][i]];                if (!vis[e.to] && e.cap > e.flow)                {                    vis[e.to] = 1;                    d[e.to] = d[x] + 1;                    qu.push(e.to);                }            }        }        return vis[ed];    }     int DFS(int x, int a)    {        if (x == ed || a == 0) return a;        int flow = 0, f;        for (int &i = cur[x]; i < SZ(G[x]); i++)        {            EDGE &e = edges[G[x][i]];            if (d[x] + 1 == d[e.to] && (f = DFS(e.to, min(a, e.cap - e.flow))) > 0)            {                e.flow += f;                edges[G[x][i] ^ 1].flow -= f;                flow += f;                a -= f;                if (a == 0) break;            }        }        return flow;    }}maxFlow; int state[1500]; int main(){    //ROP;    int npeo, m, i, j;    while (~scanf("%d%d", &npeo, &m))    {        MS(state, 0);        int ed = (1 << m) + m, st = 0;        maxFlow.init(st, ed);        for (i = 1; i <= npeo; i++)        {            int sum = 0, tmp;            for (j = 0; j < m; j++)            {                scanf("%d", &tmp);                if (tmp) sum += (1 << j);            }            state[sum]++;        }        int tmp;        for (i = (1 << m); i < (1 << m) + m; i++)        {            scanf("%d", &tmp);            maxFlow.add_edge(i, ed, tmp);        }        for (i = 1; i < (1 << m); i++)        {            if (state[i])            {                maxFlow.add_edge(st, i, state[i]);                for (int j = 0; j < m; j++)                    if (i & (1 << j)) maxFlow.add_edge(i, (1 << m) + j, state[i]);            }        }        int flow = 0;        printf("%s\n", (maxFlow.maxFlow() == npeo ? "YES" : "NO"));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Graph - Bi graph Matching](/tags/Graph-Bi-graph-Matching/)[Foundation - SC](/tags/Foundation-SC/)
