---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 3692 - Kindergarten (最大团)
tags: []
layout: post
---

## 题意

幼儿园里女孩全部认识，男孩全部认识，一些女孩和一些男孩认识，要使他们都能认识才能组成一个圈子，求最大圈子人数。

## 思路

是求最大团，根据公式，就是V - 补图的最大匹配

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 200 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int mp[MAXN][MAXN], nb; struct EDGE{    int from, to;}; struct BIMATCHING{    int link[MAXN], head[MAXN], next[MAXN * MAXN];    bool vis[MAXN];    vector<EDGE> edges;     void init()    {        MS(link, -1); MS(head, -1);        edges.clear();    }    void add_edge(int from, int to)    {        edges.PB((EDGE){from, to});        int m = SZ(edges);        next[m - 1] = head[from];        head[from] = m - 1;    }     bool dfs(int u)    {        for (int v = 1; v <= nb; v++)        {            if (!vis[v] && mp[u][v])            {                vis[v] = 1;                if (link[v] == -1 || dfs(link[v]))                {                    link[v] = u;                    return true;                }            }        }        return false;    }     int solve(int n)  //n是待匹配的总数，这里默认从1开始    {        int res = 0;        for (int i = 1; i <= n; i++)        {            MS(vis, 0);            if (dfs(i)) res++;        }        return res;    }}hun; int main(){    //ROP;    int ng, n, i, j, cases = 0;    while (scanf("%d%d%d", &ng, &nb, &n), ng + nb + n)    {        MS(mp, -1);        hun.init();        while (n--)        {            int a, b;            scanf("%d%d", &a, &b);            mp[a][b] = 0;        }        printf("Case %d: %d\n", ++cases, ng + nb - hun.solve(ng));    }    return 0;}
```