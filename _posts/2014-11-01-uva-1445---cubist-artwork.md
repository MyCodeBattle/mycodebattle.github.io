---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 1445 - Cubist Artwork
tags: []
layout: post
---

#  [UVa 1445 - Cubist Artwork](/2014/11/UVa-1445/ "UVa 1445 - Cubist Artwork")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 26 2014 23:33

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出正视图和侧视图（右），求最少有几个方块。

## 思路

贪心，如果正视图的个数和侧视图相同，就可以把它们看成是同一个东西。

$ans += i * max(f[i], r[i])$

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 1e5 + 10;const int MOD = 1000007;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int f[50], r[50]; int main(){    //ROP;    int a, b, i, j;    while (scanf("%d%d", &a, &b), a + b)    {        MS(f, 0); MS(r, 0);        for (int i = 0; i < a; i++)        {            int tmp;            scanf("%d", &tmp);            f[tmp]++;        }        for (int i = 0; i < b; i++)        {            int tmp;            scanf("%d", &tmp);            r[tmp]++;        }        int ans = 0;        for (int i = 1; i <= 20; i++)            ans = ans + i * max(f[i], r[i]);        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)
