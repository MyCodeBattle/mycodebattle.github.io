---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 11426 - GCD - Extreme (II) (数论)
tags: []
layout: post
---

## 题意

输出gcd(1, 2) + gcd(1, 3) + gcd(2, 3) +…+ gcd(n - 1, n)的和。

## 思路

大白例题。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 4e6 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int phi[MAXN]; void phi_table(int n){    phi[1] = 1;    for (int i = 2; i <= n; i++)        if (!phi[i])            for (int j = i; j <= n; j += i)            {                if (!phi[j]) phi[j] = j;                phi[j] = phi[j] / i * (i-1);            }} LL f[MAXN], ans[MAXN]; int main(){    int n;    phi_table(MAXN - 1);    for (int i = 1; i < MAXN; i++)        for (int j = i * 2; j < MAXN; j += i)            f[j] += (LL)i * phi[j / i];    ans[2] = f[2];    for (int i = 3; i < MAXN; i++) ans[i] = ans[i - 1] + f[i];    while (scanf("%d", &n), n)        printf("%lld\n", ans[n]);    return 0;}
```