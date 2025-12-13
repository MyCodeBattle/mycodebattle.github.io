---
categories: Posts
date: 2014-10-01 00:00:00
title: Codeforces 474D - Flowers (0 - 1背包)
tags: []
layout: post
---

## 题意

小明要吃花。

他只能吃k朵连着的白色花，不然就不吃，问花有a~b朵的时候有几种情况

## 思路

就是一个简单的背包

$dp[i] = dp[i - 1] + dp[i - k]$

有i朵花的时候，要么增加一朵红花，这时候是dp[i - 1]种情况，也可以增加k朵白花，dp[i - k]种情况。

比赛的时候我竟然写了排列组合，妥妥的TLE。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e5 + 10;const int MOD = 1e9 + 7;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;LL dp[MAXN];int main(){    //ROP;	ios::sync_with_stdio(0);	int n, k, i, j;	cin >> n >> k;	dp[0] = 1;	for (i = 1; i < MAXN; i++) dp[i] = (dp[i - 1] + (i >= k ? dp[i - k] : 0)) % MOD;	for (i = 2; i < MAXN; i++) dp[i] = (dp[i - 1] + dp[i]) % MOD;	dp[0] = 0;	while (n--)	{		int a, b;		cin >> a >> b;		cout << (dp[b] - dp[a - 1] + MOD) % MOD << endl;	}	return 0;}
```