---
categories: Posts
date: 2014-12-01 00:00:00
title: UVa 10396 - Vampire Numbers (暴力)
tags: []
layout: post
---

## 题意

计算n位的吸血鬼数有几个。

满足以下条件的成为吸血鬼数。

  1. v = xy, xy中的数合起来正好和v中的一样。
  2. xy不能同时有后缀0


## 思路

一开始打了个表，不过太大了，不让交。然后就直接暴力了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; bool Check(int a, int b){    int vis[11], vvis[11];    MS(vis, 0); MS(vvis, 0);    int num = a * b;    while (a)    {        int rem = a % 10;        a /= 10;        vis[rem]++;    }    while (b)    {        int rem = b % 10;        b /= 10;        vis[rem]++;    }    while (num)    {        int rem = num % 10;        num /= 10;        vvis[rem]++;    }    for (int i = 0; i < 10; i++)        if (vis[i] != vvis[i]) return false;    return true;} set<int> ans[10]; int main(){    const LL MAX = 1e10;    int i, j;    for (i = 10; i <= 99; i++)        for (j = i; j <= 99; j++)        {            int num = i * j;            if (num & 1) continue;            if (i % 10 == 0 && j % 10 == 0) continue;            if (Check(i, j)) ans[2].insert(num);        }    for (i = 100; i <= 999; i++)        for (j = 100; j <= 999; j++)        {            int num = i * j;            if (num > 100000000) continue;            if (num & 1) continue;            if (i % 10 == 0 && j % 10 == 0) continue;            if (Check(i, j)) ans[3].insert(num);        }    for (i = 1000; i <= 9999; i++)        for (j = i; j <= 9999; j++)        {            if (i % 10 == 0 && j % 10 == 0) continue;            LL num = (LL)i * j;            if (num > MAX) continue;            if (num & 1) continue;            if (Check(i, j)) ans[4].insert(num);        }    int n;    while (~scanf("%d", &n))    {        int pos = n / 2;        for (set<int>::iterator it = ans[pos].begin(); it != ans[pos].end(); it++)            printf("%d\n", *it);        puts("");    }    return 0;}
```