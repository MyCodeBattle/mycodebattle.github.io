---
categories: Posts
date: 2014-12-14 00:00:00
title: PKU 2186 - Popular Cows (强连通 + 缩点)
tags: []
layout: post
---

## 题意

找出所有牛都认为很NB的牛

## 思路

找出度为0的强连通分量，但是不能出现两个或两个以上，因为这样说明图不连通。

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
#include <iomanip>
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
const double eps = 1e-8;
const int MAXN = 10000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
 
struct SCC
{
    int dfs_clock, scc_cnt, v;
    int pre[MAXN], sccno[MAXN], lowlink[MAXN], scc[MAXN], out[MAXN];
    vector<int> G[MAXN];
    stack<int> st;
 
    void init(int n)
    {
        this->v = n;
        MS(pre, 0); MS(sccno, 0); MS(scc, 0); MS(out, 0);
        dfs_clock = scc_cnt = 0;
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
                lowlink[u] = min(lowlink[u], lowlink[v]);
            }
            else if (!sccno[v]) lowlink[u] = min(lowlink[u], pre[v]);
        }
        if (pre[u] == lowlink[u])
        {
            ++scc_cnt;
            while (1)
            {
                int x = st.top(); st.pop();
                sccno[x] = scc_cnt;
                if (x == u) break;
            }
        }
    }
 
    void solve()
    {
        for (int i = 1; i <= v; i++)
            if (!pre[i]) DFS(i);
        for (int i = 1; i <= v; i++) scc[sccno[i]]++;
        for (int i = 1; i <= v; i++)
            for (int j = 0; j < SZ(G[i]); j++)
            {
                int v = G[i][j];
                if (sccno[i] != sccno[v])  out[sccno[i]]++;
            }
        int ans = 0, cnt = 0;
        for (int i = 1; i <= scc_cnt; i++)
            if (out[i] == 0)
            {
                ans = i;
                cnt++;
            }
        printf("%d\n", cnt > 1 ? 0 : scc[ans]);
    }
}scc;
 
int main()
{
    //ROP;
    int v, e, i, j;
    scanf("%d%d", &v, &e);
    scc.init(v);
    for (i = 0; i < e; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        scc.G[a].PB(b);
    }
    scc.solve();
    return 0;
}
```