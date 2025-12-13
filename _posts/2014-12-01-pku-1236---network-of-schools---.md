---
categories: Posts
date: 2014-12-01 00:00:00
title: PKU 1236 - Network of Schools (强连通 + 缩点)
tags: []
layout: post
---

## 题意

每个学校都能送东西到其他学校，现在问

  1. 最少指定几个学校可以送完全部。
  2. 加上几个学校可以随意送达。


第一个就是求入度为0的数量，第二个求加几条边可以变成强连通图。

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
const double eps = 1e-6;
const int MAXN = 110 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct SCC
{
    int v, pre[MAXN], lowlink[MAXN], sccno[MAXN], scc_cnt, dfs_clock, in[MAXN], out[MAXN];
    vector<int> G[MAXN], scc[MAXN];
    stack<int> st;
 
    void init(int v)
    {
        this->v = v;
        for (int i = 1; i <= v; i++) G[i].clear(), scc[i].clear();
        MS(sccno, 0); MS(pre, 0); MS(lowlink, 0); MS(in, 0);
        scc_cnt = dfs_clock = 0;
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
        if (scc_cnt == 1)
        {
            puts("1");
            puts("0");
            return;
        }
        for (int i = 1; i <= v; i++)
        {
            for (int j = 0; j < SZ(G[i]); j++)
            {
                int x = G[i][j];
                if (sccno[i] != sccno[x])
                {
                    in[sccno[x]]++;
                    out[sccno[i]]++;
                }
            }
        }
        int inAns = 0, outAns = 0;
        for (int i = 1; i <= scc_cnt; i++)
        {
            if (in[i] == 0) inAns++;
            if (out[i] == 0) outAns++;
        }
        printf("%d\n", inAns);
        printf("%d\n", max(inAns, outAns));
    }
 
    void find_scc()
    {
        for (int i = 1; i <= v; i++)
            if (!pre[i]) DFS(i);
    }
 
}scc;
 
int main()
{
    //ROP;
    int v, e, i, j;
    while (~scanf("%d", &v))
    {
        scc.init(v);
        for (int i = 1; i <= v; i++)
        {
            int tmp;
            while (scanf("%d", &tmp), tmp)
                scc.G[i].PB(tmp);
        }
        scc.find_scc();
        scc.solve();
    }
    return 0;
}
```