---
categories: Posts
date: 2014-11-06 00:00:00
title: HDU 1028 - Ignatius and the Princess III (简单DP)
tags: []
layout: post
---

## 题意

找出一个数有几种不同的表达方式。

## 思路

可以递推求解。先求出每个数由1表示几种，再加上2，再加上3。。。。

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
const int MAXN = 200 + 10;
const int MOD = 1e9 + 7;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int dp[MAXN];
 
int main()
{
    int i, j, n;
    dp[0] = 1;
    for (i = 1; i < 121; i++)
        for (j = i; j < 121; j++) dp[j] += dp[j - i];
    while (~scanf("%d", &n)) printf("%d\n", dp[n]);
    return 0;
}
```