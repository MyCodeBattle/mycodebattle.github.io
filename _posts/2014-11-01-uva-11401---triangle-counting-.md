---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 11401 - Triangle Counting (容斥原理)
tags: []
layout: post
---

#  [UVa 11401 - Triangle Counting (容斥原理)](/2014/11/UVa-11401/ "UVa 11401 - Triangle Counting \(容斥原理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 7 2014 11:15

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出最长边小于等于n的边长不同的三角形的个数。

## 思路

这个变形有点神奇。大白例题

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1000000 + 10;const int MOD = 1e9 + 7; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; LL dp[MAXN]; int main(){    dp[3] = 0;    for (LL i = 4; i <= 1000000; i++)        dp[i] = dp[i - 1] + ((i - 1) * (i - 2) / 2 - (i - 1) / 2) / 2;    int n;    while (cin >> n, n >= 3)        cout << dp[n] << endl;    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Math - Combinatorics](/tags/Math-Combinatorics/)
