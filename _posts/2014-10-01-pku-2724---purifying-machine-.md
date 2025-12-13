---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2724 - Purifying Machine (最小边覆盖)
tags: []
layout: post
---

#  [PKU 2724 - Purifying Machine (最小边覆盖)](/2014/10/PKU-2724/ "PKU 2724 - Purifying Machine \(最小边覆盖\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 12 2014 14:18

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有一些奶酪被污染了，现在要清洗一下。

有*的代表0 1都可以。

问最少要清洗几次。

## 思路

学习了判断两个二进制是不是只差一位。

对只差一位的序列建边，因为正反都建了一遍，所以最大匹配多了一倍。

最小边覆盖 = V - 最大匹配

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113

| 
    
    
    #include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct EDGE{    int from, to, cap;}; int match[MAXN], ele[MAXN];vector<int> G[MAXN]; struct HUNGARY{    int vis[MAXN];    int solve(int nrem)    {        int res = 0;        MS(match, 0);        for (int i = 0; i < nrem; i++)        {            MS(vis, 0);            res += DFS(i);        }        return res;    }     int DFS(int u)    {        for (int i = 0; i < SZ(G[u]); i++)        {            int v = G[u][i];            if (!vis[v])            {                vis[v] = 1;                if (!match[v] || DFS(match[v]))                {                    match[v] = u;                    return 1;                }            }        }        return 0;    }}hun; int main(){    //ROP;    int n, nope, i, j;    while (~scanf("%d%d", &n, &nope), n + nope)    {        int cur = 0;        char cmd[15];        while (nope--)        {            scanf("%s", cmd);            int sum = 0, pos = -1;            for (i = 0; i < n; i++)            {                if (cmd[i] == '*') pos = i;                else sum |= ((cmd[i] - '0') << i);            }            ele[cur++] = sum;            if (pos != -1) ele[cur++] = (sum | (1 << pos));        }        sort(ele, ele + cur);        int len = unique(ele, ele + cur) - ele;        for (i = 0; i <= len; i++) G[i].clear();        for (i = 0; i < len; i++)            for (j = i + 1; j < len; j++)            {                int tmp = ele[i] ^ ele[j];                if (tmp && ((tmp & (tmp - 1)) == 0))                {                    G[i].PB(j);                    G[j].PB(i);                }            }        printf("%d\n", len - hun.solve(len) / 2);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Graph - Bi graph Matching](/tags/Graph-Bi-graph-Matching/)
