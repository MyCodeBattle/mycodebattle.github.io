---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2619 - Love you Ten thousand years (数论 + 原根)
tags: []
layout: post
---

#  [HDU 2619 - Love you Ten thousand years (数论 + 原根)](/2015/02/HDU-2619/ "HDU 2619 - Love you Ten thousand years \(数论 + 原根\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 22 2015 16:59

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

求出小于n的数的个数，满足$k^i \bmod n,1 \leq i \leq n是模n的完全剩余系 $

## 思路

请教了**SkyWalkerT** 巨巨。

其实是一个结论题。

> 对正整数(a,m)=1，如果 a 是模 m 的原根，那么 a 是整数模n乘法群（即加法群 Z/mZ 的可逆元，也就是所有与 m 互素的正整数构成的等价类构成的乘法群）Zn×的一个生成元。由于Zn×有 $\varphi (m)$个元素，而它的生成元的个数就是它的可逆元个数，即 $\varphi (\varphi (m))$个，因此当模m有原根时，它有$\varphi (\varphi (m))$个原根。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e7 + 2;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; LL get_phi(int n){    int m = (int)sqrt(n+0.5);    int ans = n;    for (int i = 2; i <= m; i++) if (n % i == 0)    {        ans = ans / i * (i-1);        while (n % i == 0) n /= i;    }    if (n > 1) ans = ans / n * (n-1);    return ans;} int main(){    int n;    while (~scanf("%d", &n))    {        printf("%d\n", get_phi(get_phi(n)));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)
