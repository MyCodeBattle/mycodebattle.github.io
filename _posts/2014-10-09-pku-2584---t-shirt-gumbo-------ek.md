---
categories: Posts
date: 2014-10-09 00:00:00
title: PKU 2584 - T-Shirt Gumbo (二分图最大匹配 & 匈牙利算法 | 最大流 & EK)
tags: []
layout: post
---

## 题意

给出一个人能穿的型号和每个型号衣服的多少，求能不能每个人恰好分配到一件。

## 思路

第一次先用最大流写了一下，然后就试试最大匹配。

最大匹配就是把n件相同的衣服拆成一件一件，分别编号，再把人和它们相连，然后就匈牙利算法了。  
感觉用最大匹配写繁琐一点。

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
const int MAXN = 100 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
string str = "0SMLXT";
 
struct EDGES
{
    int from, to;
};
 
struct EDGE
{
    int from, to, cap, flow;
};
 
int start[6], cnt[6], L[MAXN], R[MAXN];
int link[MAXN], vis[MAXN], head[MAXN], next[MAXN * MAXN];
 
struct BIMATCHING
{
 
    vector<EDGES> edges;
 
    void init()
    {
        MS(link, -1); MS(head, -1);
        edges.clear();
    }
 
    void add_edge(int from, int to)
    {
        edges.PB((EDGES){from, to});
        int m = SZ(edges);
        next[m - 1] = head[from];
        head[from] = m - 1;
    }
 
    bool dfs(int u)
    {
        for (int i = head[u]; i != -1; i = next[i])
        {
            EDGES &e = edges[i];
            int v = e.to;
            if (!vis[v])
            {
                vis[v] = 1;
                if (link[v] == -1 || dfs(link[v]))
                {
                    link[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
 
    int hungary(int n)
    {
        int res = 0;
        for (int i = 6; i < 6 + n; i++)
        {
            MS(vis, 0);
            if (dfs(i)) res++;
        }
        return res;
    }
}hun;
 
/*
 
struct MAXFLOW
{
    int head[MAXN], next[MAXN * MAXN], N, a[MAXN], p[MAXN];
    vector<EDGE> edges;
 
    void init(int N)
    {
        this->N = N;
        MS(head, -1);
        edges.clear();
    }
 
    void add_edge(int from, int to, int cap)
    {
        edges.PB((EDGE){from, to, cap, 0});
        edges.PB((EDGE){to, from, 0, 0});
        int m = SZ(edges);
        next[m - 2] = head[from];
        head[from] = m - 2;
        next[m - 1] = head[to];
        head[to] = m - 1;
    }
 
    void EK(int st, int &flow)
    {
        queue<int> qu;
        while (true)
        {
            MS(a, 0);
            a[0] = INF;
            qu.push(st);
            while (!qu.empty())
            {
                int u = qu.front(); qu.pop();
                for (int i = head[u]; i != -1; i = next[i])
                {
                    EDGE &e = edges[i];
                    if (!a[e.to] && e.cap > e.flow)
                    {
                        a[e.to] = min(a[u], e.cap - e.flow);
                        qu.push(e.to);
                        p[e.to] = i;
                    }
                }
            }
            if (!a[N]) break;
            int u = N;
            while (u != st)
            {
                edges[p[u]].flow += a[N];
                edges[p[u] ^ 1].flow -= a[N];
                u = edges[p[u]].from;
            }
            flow += a[N];
        }
    }
}maxFlow;
 
*/
 
int main()
{
    //ROP;
    string cmd;
    int i, j;
    while (cin >> cmd && cmd != "ENDOFINPUT")
    {
        int n;
        cin >> n;
        //int N = n + 5 + 1;
        //maxFlow.init(N);
        hun.init();
        string sz;
        for (i = 6; i <= n + 5; i++)
        {
            cin >> sz;
            int l = str.find(sz[0]);
            int r = str.find(sz[1]);
            L[i] = l, R[i] = r;
            /*
            for (j = l; j <= r; j++) maxFlow.add_edge(j, i, 1);
            maxFlow.add_edge(i, N, 1);
            */
        }
        int sum = 0;
        for (i = 1; i <= 5; i++)
        {
            int num;
            cin >> num;
            start[i] = sum + 1;
            cnt[i] = num;
            sum += cnt[i];
            //maxFlow.add_edge(0, i, num);
        }
        for (i = 6; i < 6 + n; i++)
            for (j = start[L[i]]; j < start[R[i]] + cnt[R[i]]; j++) hun.add_edge(i, j);
        cin >> cmd;
        int flow = hun.hungary(n);
        //maxFlow.EK(0, flow);
        printf("%s\n", (flow == n ? "T-shirts rock!" : "I'd rather not wear a shirt anyway..."));
    }
    return 0;
}
```