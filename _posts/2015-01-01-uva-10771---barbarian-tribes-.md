---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 10771 - Barbarian tribes (思维)
tags: []
layout: post
---

#  [UVa 10771 - Barbarian tribes (思维)](/2015/01/UVa-10771/ "UVa 10771 - Barbarian tribes \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 9 2015 16:23

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

在失落之岛上有两个部落，每个部落各选出m、n人，然后从第1个开始，k个杀第一个，再数k个杀第二个，按规则补上一个。  
问最后剩下哪个部落的。

## 思路

看了下数据量也不大，直接用链表模拟了。果断T。

后来看了帆神的题解。。。。

因为K部落只能两个两个减，所以当他是奇数的时候一定是剩下的。

单单判断一个奇数也跑了18ms。。。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    int n, m, k, i, j;    while (scanf("%d%d%d", &n, &m, &k), n + m + k)        printf("%s\n", m % 2 ? "Keka" : "Gared");    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)
