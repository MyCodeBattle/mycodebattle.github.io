---
categories: Posts
date: 2015-01-01 00:00:00
title: Codeforces 505B - Mr. Kitayuta's Colorful Graph (DFS)
tags: []
layout: post
---

#  [Codeforces 505B - Mr. Kitayuta's Colorful Graph (DFS)](/2015/01/codeforces-505b/ "Codeforces 505B - Mr. Kitayuta's Colorful Graph \(DFS\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 19 2015 9:53

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一个图，每条边代表颜色，下面有几个询问，问从a到b有几条颜色完全一样的路

## 思路

建图。我用vector G[MAXN][MAXN]存图，然后从每个点到每个点，每种颜色都DFS一遍，最后输出。

比赛的时候也是写DFS，不过写的回溯，无限WA（ ＴДＴ）。后来不回溯了，直接暴力每种颜色。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 100 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; vector<int> G[MAXN][MAXN];int mp[MAXN][MAXN], x, y, vis[MAXN], v, e, cnt;int colvis[MAXN]; bool DFS(int cur, int target, int col){    if (cur == target) return true;    for (int i = 1; i <= v; i++)    {        if (SZ(G[cur][i]) == 0 || vis[i]) continue;        for (int j = 0; j < SZ(G[cur][i]); j++)        {            if (G[cur][i][j] != col) continue;            vis[i] = 1;            if (DFS(i, target, col)) return true;        }    }    return false;} int main(){    //ROP;    int i, j;    scanf("%d%d", &v, &e);    for (int i = 0; i < e; i++)    {        int a, b, c;        scanf("%d%d%d", &a, &b, &c);        G[a][b].PB(c); G[b][a].PB(c);    }    for (int i = 1; i <= v; i++)        for (int j = i + 1; j <= v; j++)        {            int ans = 0;            for (int k = 1; k <= e; k++)            {                MS(vis, 0);                if (DFS(i, j, k)) ans++;                mp[i][j] = mp[j][i] = ans;            }        }    int q;    scanf("%d", &q);    while (q--)    {        int a, b;        scanf("%d%d", &a, &b);        printf("%d\n", mp[a][b]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Search](/tags/Foundation-Search/)
