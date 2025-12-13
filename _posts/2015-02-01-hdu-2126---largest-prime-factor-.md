---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2126 - Largest prime factor (素数筛变种→因素筛)
tags: []
layout: post
---

#  [HDU 2126 - Largest prime factor (素数筛变种→因素筛)](/2015/02/HDU-2126/ "HDU 2126 - Largest prime factor \(素数筛变种→因素筛\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 7 2015 20:25

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出一个数的最大素因数的position

## 思路

和素数筛差不多的思路，在筛的时候直接筛出最大素因数

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e6 + 10;const int MOD = 29;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int vis[MAXN]; void Solve(){    int cnt = 1;    for (int i = 2; i < MAXN; i++) if (!vis[i])    {        vis[i] = cnt;        for (int j = (i<<1); j < MAXN; j += i) vis[j] = cnt;        cnt++;    }} int main(){    Solve();    int n;    while (~scanf("%d", &n))        printf("%d\n", vis[n]);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)
