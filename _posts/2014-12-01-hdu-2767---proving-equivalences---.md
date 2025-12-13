---
categories: Posts
date: 2014-12-01 00:00:00
title: HDU 2767 - Proving Equivalences (强连通 + 缩点)
tags: []
layout: post
---

#  [HDU 2767 - Proving Equivalences (强连通 + 缩点)](/2014/12/HDU-2767/ "HDU 2767 - Proving Equivalences \(强连通 + 缩点\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Dec 7 2014 0:46

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出还要加几条边才能构成一个强连通图

## 思路

求出强连通分量后缩点，求出每个强连通分量的入度和出度，答案就是入度为0数目好出度为0数目的最大值。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 2e4 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {-1, 0}, {0, -1}, {0, 1} }; int dfs_clock, scc_cnt, pre[MAXN], lowlink[MAXN], sccno[MAXN], in[MAXN], out[MAXN];vector<int> G[MAXN];stack<int> st; void DFS(int u){    pre[u] = lowlink[u] = ++dfs_clock;    st.push(u);    for (int i = 0; i < SZ(G[u]); i++)    {        int v = G[u][i];        if (!pre[v])        {            DFS(v);            lowlink[u] = min(lowlink[u], lowlink[v]);        }        else if (!sccno[v]) lowlink[u] = min(lowlink[u], pre[v]);    }    if (lowlink[u] == pre[u])    {        scc_cnt++;        while (1)        {            int x = st.top(); st.pop();            sccno[x] = scc_cnt;            if (x == u) break;        }    }} void FindSCC(int v){    MS(pre, 0); MS(lowlink, 0); MS(sccno, 0);    dfs_clock = scc_cnt = 0;    for (int i = 1; i <= v; i++)        if (!pre[i]) DFS(i);} int main(){   // ROP;    int T, i, j;    scanf("%d", &T);    while (T--)    {        MS(in, 0); MS(out, 0);        int v, e;        scanf("%d%d", &v, &e);        for (i = 0; i <= v; i++) G[i].clear();        for (i = 0; i < e; i++)        {            int a, b;            scanf("%d%d", &a, &b);            G[a].PB(b);        }        FindSCC(v);        if (scc_cnt == 1)        {            puts("0");            continue;        }        for (i = 1; i <= v; i++)        {            for (j = 0; j < SZ(G[i]); j++)            {                if (sccno[i] != sccno[G[i][j]])                {                    out[sccno[i]]++;                    in[sccno[G[i][j]]]++;                }            }        }        int inAns = 0, outAns = 0;        for (i = 1; i <= scc_cnt; i++)        {            if (in[i] == 0) inAns++;            if (out[i] == 0) outAns++;        }        printf("%d\n", max(inAns, outAns));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Graph - SCC](/tags/Graph-SCC/)
