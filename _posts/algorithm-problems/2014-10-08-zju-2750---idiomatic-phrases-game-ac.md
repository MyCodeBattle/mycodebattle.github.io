---
categories: Posts
date: 2014-10-08 00:00:00
title: ZJU 2750 - Idiomatic Phrases Game (最短路，吐血AC)
tags: []
layout: post
---

## 题意

成语接龙。

## 思路

最短路，建图，一个大大的水题我竟然做了一个晚上！！！！！！

究其原因竟然是数组版邻接表出了点问题！！！！！

后来把数组开大四倍就过了，这是什么原因？？？？

未解之谜。以后还要继续探究。

* * *

原因已找到，是next数组的问题，开太小了。以后看到边不多的题直接用STL大法了

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
#define LL long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 4000 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct EDGE
{
    int from, to, cost;
};
 
struct DIC
{
    string head, tail;
    int cost;
}dic[1100];
 
struct HEAPNODE
{
    int d, u;
    bool operator < (const HEAPNODE &a) const
    {
        return d > a.d;
    }
};
 
struct S_PATH
{
    int N, cnt, d[MAXN];
    int vis[MAXN], next[MAXN], head[MAXN], done[MAXN];
    vector<EDGE> edges;
 
    void add_edge(int from, int to, int cost)
    {
        edges.push_back((EDGE){from, to, cost});
        int m = SZ(edges);
        next[m - 1] = head[from];
        head[from] = m - 1;
    }
 
    void init()
    {
        MS(head, -1);
        edges.clear();
        MS(done, 0);
    }
 
    void dijkstra(int st)
    {
        priority_queue<HEAPNODE> pqu;
        MS(d, INF);
        d[st] = 0;
        pqu.push((HEAPNODE){d[st], st});
        while (!pqu.empty())
        {
            HEAPNODE x = pqu.top(); pqu.pop();
            int u = x.u;
            if (done[u]) continue;
            done[u] = 1;
            for (int i = head[u]; i != -1; i = next[i])
            {
                EDGE &e = edges[i];
                if (d[e.to] > d[u] + e.cost)
                {
                    d[e.to] = d[u] + e.cost;
                    pqu.push((HEAPNODE){d[e.to], e.to});
                }
            }
        }
    }
 
    void SPFA(int st)
    {
        MS(vis, 0);
        queue<int> qu;
        MS(d, INF);
        d[st] = 0;
        qu.push(st);
        while (!qu.empty())
        {
            int u = qu.front(); qu.pop();
            vis[u] = 0;
            for (int i = head[u]; i != -1; i = next[i])
            {
                EDGE &e = edges[i];
                if (d[e.to] > d[u] + e.cost)
                {
                    d[e.to] = d[u] + e.cost;
                    if (!vis[e.to])
                    {
                        vis[e.to] = 1;
                        qu.push(e.to);
                    }
                }
            }
        }
    }
}s;
 
int d[MAXN], n, mp[MAXN][MAXN];
 
priority_queue<pii, vector<pii>, greater<pii> >qu;
 
void Dijkstra(int st)
{
    memset(d, 0x3f, sizeof d);
    d[st] = 0;
    qu.push(make_pair(d[st], st));
    while (!qu.empty())
    {
        pii u = qu.top();
        qu.pop();
        int x = u.second;
        if (d[x] != u.first)
            continue;
        for (int v = 1; v <= n; v++)
            if (d[v] > d[x] + mp[x][v])
            {
                d[v] = d[x] + mp[x][v];
                qu.push(make_pair(d[v], v));
            }
    }
}
 
int main()
{
    //ROP;
    int i, j;
    while (scanf("%d", &n), n)
    {
        s.init();
        for (i = 1; i <= n; i++)
        {
            string str;
            cin >> dic[i].cost >> str;
            dic[i].head = str.substr(0, 4);
            dic[i].tail = str.substr(str.size() - 4, 4);
        }
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
            {
                if (i == j) continue;
                if (dic[i].tail == dic[j].head) s.add_edge(i, j, dic[i].cost);
            }
        s.dijkstra(1);
        printf("%d\n", s.d[n] == INF ? -1 : s.d[n]);
    }
    return 0;
}
```