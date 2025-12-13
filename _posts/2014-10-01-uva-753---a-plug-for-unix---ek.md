---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 753 - A Plug for UNIX (最大流 | EK)
tags: []
layout: post
---

#  [UVa 753 - A Plug for UNIX (最大流 | EK)](/2014/10/UVa-753/ "UVa 753 - A Plug for UNIX \(最大流 | EK\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 6 2014 15:45

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

一个宾馆里有N种插座，现在有K个设备，每个设备有各自的插座类型。

还有一些转换器，提供插座类型之间的转换。

问最少剩下多少设备不能用。

## 思路

可以想到是最大流问题。

建一个源点，到每个插座的容量为1.

建一个汇点，到每个设备的容量为1.

插座到设备的容量为1.

转换器到插座的容量为INF。

然后跑一遍最大流吧。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 300 + 10;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; map<string, int> mp; struct EDGE{    int from, to, cap, flow;}; struct MAXFLOW{    int N;    int a[MAXN], p[MAXN];    vector<EDGE> edges;    vector<int> G[MAXN];     void init(int N)    {        for (int i = 0; i < N; i++) G[i].clear();        edges.clear();    }     void add_edge(int from, int to, int cap, int flow)    {        edges.PB((EDGE){from, to, cap, 0});        edges.PB((EDGE){to, from, 0, 0});        int m = SZ(edges);        G[from].PB(m - 2); G[to].PB(m - 1);    }     void EK(int st, int ed, int &flow)    {        queue<int> qu;        while (true)        {            MS(a, 0);            a[st] = INF;            qu.push(st);            while (!qu.empty())            {                int u = qu.front(); qu.pop();                for (int i = 0; i < SZ(G[u]); i++)                {                    EDGE &e = edges[G[u][i]];                    if (!a[e.to] && e.cap > e.flow)                    {                        a[e.to] = min(a[u], e.cap - e.flow);                        p[e.to] = G[u][i];                        qu.push(e.to);                    }                }            }            if (!a[ed]) break;            int u = ed;            while (u != st)            {                edges[p[u]].flow += a[ed];                edges[p[u] ^ 1].flow -= a[ed];                u = edges[p[u]].from;            }            flow += a[ed];        }    }}maxFlow; int main(){    //ROP;    ios::sync_with_stdio(0);         int T, i, j, n, m;    cin >> T;    while (T--)    {        int cnt = 2;        mp.clear();        maxFlow.init(MAXN);        cin >> n;        for (i = 0; i < n; i++)        {            string str;            cin >> str;            mp[str] = cnt++;            maxFlow.add_edge(0, mp[str], 1, 0);        }        cin >> m;        for (i = 1; i <= m; i++)        {            string thg, str;            cin >> thg >> str;            if (!mp.count(str))                mp[str] = cnt++;            mp[thg] = cnt++;            maxFlow.add_edge(mp[str], mp[thg], 1, 0);            maxFlow.add_edge(mp[thg], 1, 1, 0);        }        cin >> n;        for (i = 0; i < n; i++)        {            string a, b;            cin >> a >> b;            if (!mp.count(a)) mp[a] = cnt++;            if (!mp.count(b)) mp[b] = cnt++;            maxFlow.add_edge(mp[b], mp[a], INF, 0);        }        int flow = 0;        maxFlow.EK(0, 1, flow);        printf("%d\n", m - flow);        if (T) puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Graph - Flow Network](/tags/Graph-Flow-Network/)
