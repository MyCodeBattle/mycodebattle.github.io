---
categories: Posts
date: 2014-10-10 00:00:00
title: PKU 2536 - Gopher II (最大流 & ISAP & Dinic | 最大匹配)
tags: []
layout: post
---

## 题意

跑的进洞的老鼠不会被抓到。求被抓到的最少的老鼠。

## 思路

一开始想到最小费用最大流，后来搞不出来。后来用最大流，发现有人用最大流能跑到30+ms，找了一下原来是ISAP，早上回来之后又调ISAP，一直调到刚才，跑出来还一样！！！肯定是我写挫了。晚上再调

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
const int MAXN = 1000 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    double x, y;
}mou[MAXN], hole[MAXN];
 
struct EDGE
{
    int from, to, cap, flow;
};
 
struct MAXFLOW
{
    int source;         // 源点
    int sink;           // 汇点
    int p[MAXN];   // 可增广路上的上一条弧的编号
    int num[MAXN]; // 和 t 的最短距离等于 i 的节点数量
    int cur[MAXN]; // 当前弧下标
    int d[MAXN];   // 残量网络中节点 i 到汇点 t 的最短距离
    int N;
    bool visited[MAXN];
    vector<EDGE> edges;
    vector<int> G[MAXN];
 
    void init(int st, int ed)
    {
        this->sink = ed, this->source = st;
        this->N = ed;
        edges.clear();
        for (int i = 0; i <= N; i++) G[i].clear();
    }
 
    void add_edge(int from, int to, int cap)
    {
        edges.PB((EDGE){from, to, cap, 0});
        edges.PB((EDGE){to, from, 0, 0});
        int m = SZ(edges);
        G[from].PB(m - 2); G[to].PB(m - 1);
    }
 
    // 预处理, 反向 BFS 构造 d 数组
        bool bfs()
        {
            memset(visited, 0, sizeof(visited));
            queue<int> Q;
            Q.push(sink);
            visited[sink] = 1;
            d[sink] = 0;
            while (!Q.empty()) {
                int u = Q.front();
                Q.pop();
                for (int i = 0; i < SZ(G[u]); ++i) {
                    EDGE &e = edges[G[u][i]];
                    if (!visited[e.to]) {
                        visited[e.to] = true;
                        d[e.to] = d[u] + 1;
                        Q.push(e.to);
                    }
                }
            }
            return visited[source];
        }
 
    // 增广
    int augment()
    {
        int u = sink, df = INF;
        // 从汇点到源点通过 p 追踪增广路径, df 为一路上最小的残量
        while (u != source) {
            EDGE &e = edges[p[u]];
            df = min(df, e.cap - e.flow);
            u = edges[p[u]].from;
        }
        u = sink;
        // 从汇点到源点更新流量
        while (u != source) {
            edges[p[u]].flow += df;
            edges[p[u]^1].flow -= df;
            u = edges[p[u]].from;
        }
        return df;
    }
 
    int max_flow()
    {
        int flow = 0;
        bfs();
        memset(num, 0, sizeof(num));
        for (int i = 0; i < N; i++) num[d[i]]++;
        int u = source;
        memset(cur, 0, sizeof(cur));
        while (d[source] < N) {
            if (u == sink) {
                flow += augment();
                u = source;
            }
            bool advanced = false;
            for (int i = cur[u]; i < G[u].size(); i++) {
                EDGE& e = edges[G[u][i]];
                if (e.cap > e.flow && d[u] == d[e.to] + 1) {
                    advanced = true;
                    p[e.to] = G[u][i];
                    cur[u] = i;
                    u = e.to;
                    break;
                }
            }
            if (!advanced) { // retreat
                int m = N - 1;
                for (int i = 0; i < SZ(G[u]); ++i)
                    if (edges[G[u][i]].cap > edges[G[u][i]].flow)
                        m = min(m, d[edges[G[u][i]].to]);
                if (--num[d[u]] == 0) break; // gap 优化
                num[d[u] = m+1]++;
                cur[u] = 0;
                if (u != source)
                    u = edges[p[u]].from;
            }
        }
        return flow;
    }
}maxFlow;
 
int main()
{
    //ROP;
    int nmouse, nhole, sec, vel, i, j;
    while (~scanf("%d%d%d%d", &nmouse, &nhole, &sec, &vel))
    {
        int st = 0, ed;
        double run = sec * vel;
        ed = nmouse + nhole + 1;
        maxFlow.init(st, ed);
        for (i = 1; i <= nmouse; i++) scanf("%lf%lf", &mou[i].x, &mou[i].y);
        for (i = 1; i <= nhole; i++)
        {
            scanf("%lf%lf", &hole[i].x, &hole[i].y);
            maxFlow.add_edge(i + nmouse, ed, 1);
        }
        for (i = 1; i <= nmouse; i++)
        {
            maxFlow.add_edge(0, i, 1);
            for (j = 1; j <= nhole; j++)
            {
                //当前点编号i + nhole
                double dis = hypot(mou[i].x - hole[j].x, mou[i].y - hole[j].y);
                if (dis <= run) maxFlow.add_edge(i, j + nmouse, 1);
            }
        }
        int flow = 0;
        flow = maxFlow.max_flow();
        printf("%d\n", nmouse - flow);
    }
    return 0;
}
```
 
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
const int MAXN = 1000 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    double x, y;
}mou[MAXN], hole[MAXN];
 
struct EDGE
{
    int from, to, cap, flow;
};
 
struct DINIC
{
    int d[MAXN], cur[MAXN], vis[MAXN], st, ed;
    vector<EDGE> edges;
    vector<int> G[MAXN];
    void add_edge(int from, int to, int cap)
    {
        edges.PB((EDGE){from, to, cap, 0});
        edges.PB((EDGE){to, from, 0, 0});
        int m = SZ(edges);
        G[from].PB(m - 2); G[to].PB(m - 1);
    }
 
    void init(int st, int ed)
    {
        this->st = st, this->ed = ed;
        edges.clear();
        for(int i = 0; i <= ed; i++) G[i].clear();
    }
 
    int maxFlow()
    {
        int flow = 0;
        while (BFS())
        {
            MS(cur, 0);
            flow += DFS(st, INF);
        }
        return flow;
    }
 
    bool BFS()
    {
        MS(vis, 0);
        queue<int> qu;
        qu.push(st);
        d[st] = 0; vis[st] = 1;
        while (!qu.empty())
        {
            int x = qu.front(); qu.pop();
            for (int i = 0; i < SZ(G[x]); i++)
            {
                EDGE &e = edges[G[x][i]];
                if (!vis[e.to] && e.cap > e.flow)
                {
                    vis[e.to] = 1;
                    d[e.to] = d[x] + 1;
                    qu.push(e.to);
                }
            }
        }
        return vis[ed];
    }
 
    int DFS(int x, int a)
    {
        if (x == ed || a == 0) return a;
        int flow = 0, f;
        for (int &i = cur[x]; i < SZ(G[x]); i++)
        {
            EDGE &e = edges[G[x][i]];
            if (d[x] + 1 == d[e.to] && (f = DFS(e.to, min(a, e.cap - e.flow))) > 0)
            {
                e.flow += f;
                edges[G[x][i] ^ 1].flow -= f;
                flow += f;
                a -= f;
                if (a == 0) break;
            }
        }
        return flow;
    }
}maxFlow;
 
 
int main()
{
    //ROP;
    int nmouse, nhole, sec, vel, i, j;
    while (~scanf("%d%d%d%d", &nmouse, &nhole, &sec, &vel))
    {
        int st = 0, ed;
        double run = sec * vel;
        ed = nmouse + nhole + 1;
        maxFlow.init(st, ed);
        for (i = 1; i <= nmouse; i++) scanf("%lf%lf", &mou[i].x, &mou[i].y);
        for (i = 1; i <= nhole; i++)
        {
            scanf("%lf%lf", &hole[i].x, &hole[i].y);
            maxFlow.add_edge(i + nmouse, ed, 1);
        }
        for (i = 1; i <= nmouse; i++)
        {
            maxFlow.add_edge(0, i, 1);
            for (j = 1; j <= nhole; j++)
            {
                //当前点编号i + nhole
                double dis = hypot(mou[i].x - hole[j].x, mou[i].y - hole[j].y);
                if (dis <= run) maxFlow.add_edge(i, j + nmouse, 1);
            }
        }
        int flow = 0;
        flow = maxFlow.maxFlow();
        printf("%d\n", nmouse - flow);
    }
    return 0;
}
```