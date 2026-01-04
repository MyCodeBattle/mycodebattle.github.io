---
categories: Posts
date: 2014-10-05 00:00:00
title: UVa 11045 - My T-shirt suits me (最大流 & EK)
tags: []
layout: post
---

## 题意

一个人有两种合适的T恤，现在有K套，问能不能让所有人穿上合适的。

## 思路

乍一看感觉是二分图匹配的内容？可是我不会。

可以这么想：建一个源点，到每个衣服的容量显然可以算出。每个衣服到每个合适的人的容量为1，每个人最后都连上汇点，这条路容量为1（因为只能穿一件）。如果最后流量能达到人数，说明可以，否则不可以。

把最大流封装了一下。

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
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
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
const LL MAXN = 30 + 10;
const int MOD = 20071027;
  
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
  
int Convert(string str)
{
    if (str == "XXL") return 1;
    else if (str == "XL") return 2;
    else if (str == "L") return 3;
    else if (str == "M") return 4;
    else if (str == "S") return 5;
    else if (str == "XS") return 6;
}
  
​struct EDGE
{
    int from, to, cap, flow;
};
  
struct MAXFLOW
{
    int a[MAXN], p[MAXN], N;
    vector<EDGE> edge;
    vector<int> G[MAXN];
  
    void init(int n)
    {
        this->N = n;
        for (int i = 0; i <= n; i++) G[i].clear();
        edge.clear();
    }
  
    void add_edge(int from, int to, int cap)
    {
        edge.PB((EDGE){from, to, cap, 0});
        edge.PB((EDGE){to, from, 0, 0});
        int m = SZ(edge);
        G[from].PB(m - 2);
        G[to].PB(m - 1);
    }
  
    void EK(int st, int &flow)
    {
        queue<int> qu;
        while (true)
        {
            MS(a, 0);
            a[0] = INF;
            qu.push(0);
            while (!qu.empty())
            {
                int u = qu.front(); qu.pop();
                for (int i = 0; i < SZ(G[u]); i++)
                {
                    EDGE &e = edge[G[u][i]];
                    if (!a[e.to] && e.cap > e.flow)
                    {
                        qu.push(e.to);
                        p[e.to] = G[u][i];
                        a[e.to] = min(a[u], e.cap - e.flow);
                    }
                }
            }
            if (!a[N]) break;
            int u = N;
            while (u != st)
            {
                edge[p[u]].flow += a[N];
                edge[p[u] ^ 1].flow -= a[N];
                u = edge[p[u]].from;
            }
            flow += a[N];
        }
    }
}maxFlow;
  
int main()
{
    //ROP;
    ios::sync_with_stdio(0);
  
    int T, i, j, nmax, npeo;
    cin >> T;
    while (T--)
    {
        cin >> nmax >> npeo;
        maxFlow.init(npeo + 6 + 1);
        int f = nmax / 6;
        string s, ss;
        for (i = 1; i <= npeo; i++)
        {
            cin >> s;
            int tmp = Convert(s);
            maxFlow.add_edge(tmp, i + 6, 1);
            cin >> s;
            tmp = Convert(s);
            maxFlow.add_edge(tmp, i + 6, 1);
        }
        for (i = 1; i <= 6; i++) maxFlow.add_edge(0, i, f);
        for (i = 7; i <= npeo + 6; i++) maxFlow.add_edge(i, npeo + 6 + 1, 1);
        f = 0;
        maxFlow.EK(0, f);
        if (f == npeo) puts("YES");
        else puts("NO");
    }
    return 0;
}
```