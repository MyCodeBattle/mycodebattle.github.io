---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 563 - Crimewave (拆点 + 最大流 & EK)
tags: []
layout: post
---

## 题意

抢劫完N个银行后要逃跑，问能不能不碰头跑出去

## 思路

重点在于不能碰头，也就是不能走到同一点。

这个要怎么控制呢？

答：把一个点拆成两个点，一个入，一个出，入到出的流量为1.

这样一来只要有人走过，下一个人就走不了了。

这就是要拆点的原因。

至于详细的拆法，Titanium已经讲得很好了（<http://www.cnblogs.com/scau20110726/archive/2012/12/20/2827177.html）>

网上的版本都是数组版邻接表？我就来(tou)一(xia)个(lan)vector版吧

引用一下他的解释。

> 算法思路：对于给定的网格，行为S列为A，我们按行优先给所有点标号，从1到S _A。然后对每个点拆点，拆点后一个点变为两个点(那么总点数为2_ S _A)，在这里我把拆点后的两个点叫做“前点”和“后点”，对于坐标为(i,j)的点，拆点后“前点”的编号为u=(i-1)_ A+j , “后点”的编号好v=u+S*A;
> 
> 我们还要额外设置一个源点s，编号为0，一个汇点，编号为2 _S_ A+1。从源点s建有向边指向所有的银行，从所有网格边沿的点建有向边指向汇点t，另外网格内一个点要和它上下左右四个点建立无向边（也就是两条有向边）。数据很大，要用邻接表保存
> 
> 问题就是，我们已经事先拆点了，原来的两个点(i,j)和(i,j+1)有连线那么拆点后怎么链接呢？
> 
> 第一部分（一个点和它上下左右的四个点建边）：从这个点的“后点”和四周的点的“前点”建有向边（因为用邻接表建图，所以所有的有向边都有反边，注意反边的容量为0）。
> 
> 第二部分（源点和所有银行建边）：源点s和所有银行的“前点”建有向边（还有反边）
> 
> 第三部分（所有网格边沿的点和汇点建边）：所有网格边沿的点的“后点”和汇点建有向边（还有反边）
> 
> 因此
> 
> 第一部分：两个点a，b之间会有四边有向边，一条是a点的“后点”指向b点的“前点”，一条是b点的“后点”指向a点的“前点”。这两条还附带两条反边所以一共四条
> 
> 第二部分：源点和银行的“前点”有边，再附带一个反边
> 
> 第三部分：网格边沿点的“后点”和汇点有边，再附带一个反边
> 
> 所有边的容量都1（这样就起到了每个点只能用一次的效果），附带的反边容量当然是为0
> 
> 建图后，直接EK，算最大流，最大流等于银行个数那么可以逃脱，不等（小于）就不可以

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 5100 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;  struct EDGE{    int from, to, cap, flow;}; struct MAXFLOW{    int a[MAXN], p[MAXN];    vector<EDGE> edges;    vector<int> G[MAXN];     void init()    {        for (int i = 0; i < MAXN; i++) G[i].clear();        edges.clear();    }     void add_edge(int from, int to, int cap)    {        edges.PB((EDGE){from, to, cap, 0});        edges.PB((EDGE){to, from, 0, 0});        int m = SZ(edges);        G[from].PB(m - 2); G[to].PB(m - 1);    }     void EK(int st, int ed, int &flow)    {        queue<int> qu;        while (true)        {            MS(a, 0);            a[st] = INF;            qu.push(st);            while (!qu.empty())            {                int u = qu.front(); qu.pop();                for (int i = 0; i < SZ(G[u]); i++)                {                    EDGE &e = edges[G[u][i]];                    if (!a[e.to] && e.cap > e.flow)                    {                        a[e.to] = min(a[u], e.cap - e.flow);                        qu.push(e.to);                        p[e.to] = G[u][i];                    }                }            }            if (!a[ed]) break;            int u = ed;            while (u != st)            {                edges[p[u]].flow += a[ed];                edges[p[u] ^ 1].flow -= a[ed];                u = edges[p[u]].from;            }            flow += a[ed];        }    }}maxFlow; int main(){    //ROP;    int T, i, j, n, m, nbank;    scanf("%d", &T);    while (T--)    {        maxFlow.init();        scanf("%d%d%d", &n, &m, &nbank);        int st = 0, ed = m * n * 2 + 1;        for (i = 1; i <= n; i++)            for (j = 1; j <= m; j++)            {                int u = (i - 1) * m + j;    //入点                int v = u + m * n;      //出点                maxFlow.add_edge(u, v, 1);                for (int k = 0; k < 4; k++)                {                    int ii = i + dir[k][0], jj = j + dir[k][1];                    if (ii >= 1 && ii <= n && jj >= 1 && jj <= m)                    {                        int uu = (ii - 1) * m + jj;                        maxFlow.add_edge(v, uu, 1);                    }                    else maxFlow.add_edge(v, ed, 1);                }            }        for (i = 0; i < nbank; i++)        {            int a, b;            scanf("%d%d", &a, &b);            int u = (a - 1) * m + b;            maxFlow.add_edge(st, u, 1);        }        int flow = 0;        maxFlow.EK(st, ed, flow);        printf("%s\n", (flow == nbank ? "possible" : "not possible"));    }    return 0;}
```