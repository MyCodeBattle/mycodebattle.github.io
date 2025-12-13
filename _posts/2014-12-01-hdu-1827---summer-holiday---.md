---
categories: Posts
date: 2014-12-01 00:00:00
title: HDU 1827 - Summer Holiday (强连通 + 缩点)
tags: []
layout: post
---

#  [HDU 1827 - Summer Holiday (强连通 + 缩点)](/2014/12/HDU-1827/ "HDU 1827 - Summer Holiday \(强连通 + 缩点\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Dec 7 2014 12:45

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

缩点之后有几个入度为0的就要通知几次，然后在那个强连通分量里找最便宜的打过去。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 1100 + 10;const int MOD = 1000007; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int fee[MAXN]; struct SCC{    int v, pre[MAXN], lowlink[MAXN], sccno[MAXN], scc_cnt, dfs_clock, in[MAXN], out[MAXN];    vector<int> G[MAXN], scc[MAXN];    stack<int> st;     void init(int v)    {        this->v = v;        for (int i = 1; i <= v; i++) G[i].clear(), scc[i].clear();        MS(sccno, 0); MS(pre, 0); MS(lowlink, 0); MS(in, 0);        scc_cnt = dfs_clock = 0;    }     void DFS(int u)    {        pre[u] = lowlink[u] = ++dfs_clock;        st.push(u);        for (int i = 0; i < SZ(G[u]); i++)        {            int v = G[u][i];            if (!pre[v])            {                DFS(v);                lowlink[u] = min(lowlink[u], lowlink[v]);            }            else if (!sccno[v]) lowlink[u] = min(lowlink[u], pre[v]);        }        if (pre[u] == lowlink[u])        {            ++scc_cnt;            while (1)            {                int x = st.top(); st.pop();                sccno[x] = scc_cnt;                if (x == u) break;            }        }    }     void solve()    {        for (int i = 1; i <= v; i++)        {            scc[sccno[i]].PB(i);            for (int j = 0; j < SZ(G[i]); j++)            {                int x = G[i][j];                if (sccno[i] != sccno[x])                {                    out[sccno[i]]++;                    in[sccno[x]]++;                }            }        }        int ans = 0, cnt = 0;        for (int i = 1; i <= scc_cnt; i++)        {            int tmp = INF;            if (in[i] == 0)            {                cnt++;                for (int j = 0; j < SZ(scc[i]); j++)                    tmp = min(tmp, fee[scc[i][j]]);                ans += tmp;            }        }        printf("%d %d\n", cnt, ans);    }     void find_scc()    {        for (int i = 1; i <= v; i++)            if (!pre[i]) DFS(i);    } }scc; int main(){    //ROP;    int v, e, i, j;    while (~scanf("%d%d", &v, &e))    {        scc.init(v);        for (i = 1; i <= v; i++) scanf("%d", &fee[i]);        for (i = 0; i < e; i++)        {            int a, b;            scanf("%d%d", &a, &b);            scc.G[a].PB(b);        }        scc.find_scc();        scc.solve();    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Graph - SCC](/tags/Graph-SCC/)
