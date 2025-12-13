---
categories: Posts
date: 2014-11-07 00:00:00
title: UVa 11401 - Triangle Counting (容斥原理)
tags: []
layout: post
---

## 题意

输出最长边小于等于n的边长不同的三角形的个数。

## 思路

这个变形有点神奇。大白例题

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
const int MAXN = 1000000 + 10;
const int MOD = 1e9 + 7;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
LL dp[MAXN];
 
int main()
{
    dp[3] = 0;
    for (LL i = 4; i <= 1000000; i++)
        dp[i] = dp[i - 1] + ((i - 1) * (i - 2) / 2 - (i - 1) / 2) / 2;
    int n;
    while (cin >> n, n >= 3)
        cout << dp[n] << endl;
    return 0;
}
```