---
categories: Posts
date: 2014-10-20 00:00:00
title: PKU 1157 - LITTLE SHOP OF FLOWERS (一般DP)
tags: []
layout: post
---

## 题意

每个花放在指定的花瓶里都有数值，现在要让所有的数值之和最大。

## 思路

dp[i][j]表示前i种花放到j种瓶子里的最大值。

$dp[i][j] = max(dp[i - 1][j - 1] + w[i][j], dp[i][j - 1])$

第i种花要么放到多出来的瓶子里，要么还是放在以前的里面。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
#define LL long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 100 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int dp[MAXN][MAXN], w[MAXN][MAXN];
 
int main()
{
    //ROP;
    int nvase, nflow, i, j;
    scanf("%d%d", &nflow, &nvase);
    for (i = 1; i <= nflow; i++)
        for (j = 1; j <= nvase; j++) scanf("%d", &w[i][j]);
    dp[1][1] = w[1][1];
    for (i = 2; i <= nvase; i++) dp[1][i] = max(dp[1][i - 1], w[1][i]);
    for (i = 2; i <= nflow; i++)
        for (j = i; j <= nvase; j++)
            dp[i][j] = max(dp[i - 1][j - 1] + w[i][j], dp[i][j - 1]);
    printf("%d\n", dp[nflow][nvase]);
    return 0;
}
```