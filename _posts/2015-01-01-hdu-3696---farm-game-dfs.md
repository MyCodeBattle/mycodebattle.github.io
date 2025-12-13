---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 3696 - Farm Game (DFS)
tags: []
layout: post
---

#  [HDU 3696 - Farm Game (DFS)](/2015/01/HDU-3696/ "HDU 3696 - Farm Game \(DFS\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 19 2015 10:16

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出几种物品的转化关系，问最多能赚到多少钱

## 思路

对每个东西DFS，求出一单位的这个东西最多能换到多少钱，之后加起来。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; vector<pair<int, double> > G[MAXN];pair<double, double> arr[MAXN];int n;double maxValue[MAXN]; void Input(){    for (int i = 1; i <= n; i++) scanf("%lf%lf", &arr[i].Y, &arr[i].X);    int nn, T;    scanf("%d", &T);    double rate;    for (int i = 0; i < T; i++)    {        int pre, next;        scanf("%d%d", &nn, ⪯);        for (int j = 0; j < (nn<<1) - 2; j++)        {            if (!(j&1)) scanf("%lf", &rate);            else            {                scanf("%d", &next);                G[pre].PB({next, rate});                pre = next;            }        }    }} double DFS(int cur){    if (maxValue[cur]) return maxValue[cur];    double ret = arr[cur].Y;    for (int i = 0; i < SZ(G[cur]); i++) ret = max(ret, G[cur][i].Y * DFS(G[cur][i].X));    return maxValue[cur] = ret;} void Init(){    MS(maxValue, 0);    for (int i = 1; i <= n; i++) G[i].clear();} int main(){    //ROP;    int i, j;    while (scanf("%d", &n), n)    {        Init();        Input();        for (i = 1; i <= n; i++) DFS(i);        double ans = 0;        for (i = 1; i <= n; i++) ans += arr[i].X * maxValue[i];        printf("%.2f\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Search](/tags/Foundation-Search/)
