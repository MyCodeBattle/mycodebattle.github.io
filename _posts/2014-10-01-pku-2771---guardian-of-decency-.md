---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2771 - Guardian of Decency (最大独立集)
tags: []
layout: post
---

## 题意

问符合条件的最大人数

## 思路

反一下。求能谈恋爱的最大匹配，用n - 最大匹配即可。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1100+ 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct PEO{    int age;    string sex, hb, mus;}peo[MAXN]; struct EDGE{    int from, to;}; struct BIMATCHING{    int link[MAXN], head[MAXN], next[MAXN * MAXN];    bool vis[MAXN];    vector<EDGE> edges;    void init()    {        MS(link, -1); MS(head, -1);        edges.clear();    }    void add_edge(int from, int to)    {        edges.PB((EDGE){from, to});        int m = SZ(edges);        next[m - 1] = head[from];        head[from] = m - 1;    }     bool dfs(int u)    {        for (int i = head[u]; i != -1; i = next[i])        {            EDGE &e = edges[i];            int v = e.to;            if (!vis[v])            {                vis[v] = 1;                if (link[v] == -1 || dfs(link[v]))                {                    link[v] = u;                    return true;                }            }        }        return false;    }     int hungary(int n)  //n是待匹配的总数，这里默认从1开始    {        int res = 0;        for (int i = 1; i <= n; i++)        {            MS(vis, 0);            if (dfs(i)) res++;        }        return res;    }}hun; bool Check(int i, int j){    if (abs(peo[i].age - peo[j].age) > 40 || peo[i].sex == peo[j].sex        || peo[i].hb == peo[j].hb || peo[i].mus != peo[j].mus) return false;    return true;}  int main(){    ios::sync_with_stdio(0);    //ROP;     int T, i, j;    cin >> T;    while (T--)    {        hun.init();        int n;        cin >> n;        for (i = 1; i <= n; i++)        {            cin >> peo[i].age >> peo[i].sex >> peo[i].mus >> peo[i].hb;            for (j = 1; j < i; j++)                if (Check(i, j))                {                    hun.add_edge(j, i);                    hun.add_edge(i, j);                }        }        cout << n - hun.hungary(n) / 2 << endl;    }    return 0;}
```