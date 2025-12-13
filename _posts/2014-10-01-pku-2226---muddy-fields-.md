---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2226 - Muddy Fields (最小点覆盖)
tags: []
layout: post
---

#  [PKU 2226 - Muddy Fields (最小点覆盖)](/2014/10/PKU-2226/ "PKU 2226 - Muddy Fields \(最小点覆盖\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 12 2014 0:59

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

用最少的木板覆盖。

## 思路

很有意思的建图。横着标号，然后竖着标号，建边，求最小点覆盖。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cap;}; struct HUNGARY{    int vis[MAXN], link[MAXN], head[MAXN], next[MAXN * MAXN];    vector<EDGE> edges;     void init()    {        edges.clear();        MS(head, -1); MS(link, -1);    }     int solve(int nrem)    {        int res = 0;        for (int i = 1; i <= nrem; i++)        {            MS(vis, 0);            res += DFS(i);        }        return res;    }     void add_edge(int from, int to)    {        EDGE a = {from, to};        edges.PB(a);        int m = SZ(edges);        next[m - 1] = head[from];        head[from] = m - 1;    }     int DFS(int u)    {        for (int i = head[u]; i != -1; i = next[i])        {            int v = edges[i].to;            if (!vis[v])            {                vis[v] = 1;                if (link[v] == -1 || DFS(link[v]))                {                    link[v] = u;                    return 1;                }            }        }        return 0;    }}hun; char mp[MAXN][MAXN];int num[MAXN][MAXN]; int main(){    //ROP;    int row, col, i, j;    while (~scanf("%d%d", &row, &col))    {        hun.init();        for (i = 1; i <= row; i++) scanf("%s", mp[i] + 1);        int cnt = 0;        for (i = 1; i <= row; i++)        {            for (j = 1; j<= col; j++)                if (mp[i][j] == '*') num[i][j] = (mp[i][j] == mp[i][j - 1] ? cnt : ++cnt);        }        cnt = 0;        for (i = 1; i <= col; i++)        {            for (j = 1; j <= row; j++)            {                if (mp[j][i] == '*')                {                    if (mp[j][i] != mp[j - 1][i]) cnt++;                    hun.add_edge(cnt, num[j][i]);                }            }        }        printf("%d\n", hun.solve(cnt));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Graph - Bi graph Matching](/tags/Graph-Bi-graph-Matching/)
