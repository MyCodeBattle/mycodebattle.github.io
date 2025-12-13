---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2184 - cow Exhibition (0-1背包)
tags: []
layout: post
---

## 题意

把第一个条件当成重量，第二个条件当成权值，就变成01背包了。

处理一下负数。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768

| ```c++
​#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 200000 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int dp[MAXN];pii arr[110]; int main(){    //ROP;    int n, k = 100000, kk = 200000;    scanf("%d", &n);    for (int i = 1; i <= n; i++)        scanf("%d%d", &arr[i].X, &arr[i].Y);    for (int i = 0; i <= kk; i++) dp[i] = -INF;    dp[k] = 0;    for (int i = 1; i <= n; i++)    {        if (arr[i].X > 0)            for (int j = kk; j >= arr[i].X; j--)                dp[j] = max(dp[j], dp[j-arr[i].X]+arr[i].Y);        else            for (int j = 0; j <= kk+arr[i].X; j++)                dp[j] = max(dp[j], dp[j-arr[i].X]+arr[i].Y);    }    int ans = 0;    for (int i = k; i <= kk; i++)        if (dp[i] > 0) ans = max(ans, dp[i]+i-k);    printf("%d\n", ans);    return 0;}
```