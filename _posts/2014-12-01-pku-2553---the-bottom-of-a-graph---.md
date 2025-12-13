---
categories: Posts
date: 2014-12-01 00:00:00
title: PKU 2553 - The Bottom of a Graph (强连通 + 缩点)
tags: []
layout: post
---

## 题意

如果点A对于它所有能到达的点，都有那个点能到达点A，则成为A是sink。求所有的A。

## 思路

就是求出度为0的强连通分量。

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
#define ULL unsigned long long
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
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const double eps = 1e-6;
const int MAXN = 5000 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct SCC
{
    int v, e, dfs_clock, scc_cnt;
    int pre[MAXN], lowlink[MAXN], sccno[MAXN], out[MAXN];
    vector<int> G[MAXN], scc[MAXN], ans;
    stack<int> st;
 
    void init(int v)
    {
        this->v = v;
        for (int i = 0; i <= v; i++) G[i].clear(), scc[i].clear();
        ans.clear();
        dfs_clock = scc_cnt = 0;
        MS(pre, 0); MS(sccno, 0); MS(out, 0);
    }
 
    void DFS(int u)
    {
        pre[u] = lowlink[u] = ++dfs_clock;
        st.push(u);
        for (int i = 0; i < SZ(G[u]); i++)
        {
            int v = G[u][i];
            if (!pre[v])
            {
                DFS(v);
                lowlink[u] = min(lowlink[v], lowlink[u]);
            }
            else if (!sccno[v]) lowlink[u] = min(lowlink[u], pre[v]);
        }
        if (pre[u] == lowlink[u])
        {
            ++scc_cnt;
            while (true)
            {
                int x = st.top(); st.pop();
                sccno[x] = scc_cnt;
                if (x == u) break;
            }
        }
    }
 
    void Solve()
    {
        for (int i = 1; i <= v; i++)
            if (!pre[i]) DFS(i);
        for (int i = 1; i <= v; i++)
            scc[sccno[i]].PB(i);
        for (int i = 1; i <= v; i++)
            for (int j = 0; j < SZ(G[i]); j++)
            {
                int v = G[i][j];
                if (sccno[v] != sccno[i]) out[sccno[i]]++;
            }
        for (int i = 1; i <= scc_cnt; i++)
            if (out[i] == 0)
                for (int j = 0; j < SZ(scc[i]); j++) ans.PB(scc[i][j]);
        sort(ans.begin(), ans.end());
        if (ans.empty())
        {
            puts("");
            return;
        }
        printf("%d", ans[0]);
        for (viti it = ans.begin() + 1; it != ans.end(); it++)
            printf(" %d", *it);
        puts("");
        return;
    }
}scc;
 
int main()
{
    //ROP;
    int v, e, i, j;
    while (scanf("%d%d", &v, &e) == 2 && v != 0)
    {
        scc.init(v);
        for (i = 0; i < e; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            scc.G[a].PB(b);
        }
        scc.Solve();
    }
    return 0;
}
```