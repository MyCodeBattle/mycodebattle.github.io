---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2181 - Jumping Cows (DP)
tags: []
layout: post
---

## 题意

跳奇数步加上能量，偶数步减去，问最大能量。

## 思路

背包。如果某个阶梯不跳的话就直接继承上一个相同特性的阶梯值。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758

| ```c++
#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 150000 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int dp[MAXN][2], arr[MAXN]; int main(){    //ROP;    //odd increase    int n;    scanf("%d", &n);    for (int i = 1; i <= n; i++) scanf("%d", &arr[i]);    for (int i = 1; i <= n; i++)    {        dp[i][0] = max(dp[i-1][0], dp[i-1][1] - arr[i]);        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + arr[i]);    }    printf("%d\n", max(dp[n][0], dp[n][1]));    return 0;}
```