---
categories: Posts
date: 2014-10-01 00:00:00
title: Codeforces 476C - Dreamoon and Sums (数学)
tags: []
layout: post
---

## 题意

给出a, b，算出有几个数，符合

  1. 商和余数相除等于k，k属于[1, a]。


## 思路

引用题解的思路。

> If we fix the value of k, and let d = div(x, b), m = mod(x, b), we have :  
> d = mk  
> x = db + m  
> So we have x = mkb + m = (kb + 1) * m.  
> And we know m would be in range [0, b - 1] because it’s a remainder, so the sum of x of that fixed k would be ![ ](http://espresso.codeforces.com/f8d0f051128fca158e10c5325846ff16f48107c8.png)  
> Next we should notice that if an integer x is nice it can only be nice for a single particular k because a given x uniquely defines div(x, b) and mod(x, b).  
> Thus the final answer would be sum up for all individual k: which can be calculated in O(a) and will pass the time limit of 1.5 seconds.  
> Also the formula above can be expanded to .

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    LL a, b;    cin >> a >> b;    LL tmp1 = ((1 + a) * a) >> 1;    tmp1 %= MOD;    tmp1 = tmp1 * b % MOD;    tmp1 += a;    LL tmp2 = (b * (b - 1)) >> 1;    tmp2 %= MOD;    LL ans = tmp1 * tmp2 % MOD;    cout << ans << endl;}
```