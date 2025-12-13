---
categories: Posts
date: 2015-01-01 00:00:00
title: PKU 2262 - Goldbach's Conjecture (数论)
tags: []
layout: post
---

## 题意

把一个大于二的偶数分解成两个素数和

## 思路

先筛出素数

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e6 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int vis[MAXN], n; void get_prime(){    int limit = (int)sqrt(MAXN + 0.5);    for (int i = 2; i <= limit; i++) if (!vis[i])        for (int j = i*i; j <= MAXN; j += i) vis[j] = 1;} int main(){    get_prime();    while (scanf("%d", &n), n)    {        for (int i = 2; i <= (n>>1); i++)            if (!vis[i] && !vis[n-i])            {                printf("%d = %d + %d\n", n, i, n-i);                break;            }             }    return 0;}
```