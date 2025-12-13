---
categories: Posts
date: 2014-10-01 00:00:00
title: Codeforces 478C - Table Decorations (贪心)
tags: []
layout: post
---

#  [Codeforces 478C - Table Decorations (贪心)](/2014/10/codeforces-478c/ "Codeforces 478C - Table Decorations \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 18 2014 11:30

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

三个气球装饰桌子，一张桌子不能全是一种气球，求可以装饰桌子的个数。

## 思路

比赛的时候一直想着DP，但是一看这数据觉得一定会超时，又没什么好办法。

后来看题解竟然是贪心。

如果最多的气球大于其他两个之和的两倍，就可以一个配两个用掉，这时候的ans是min + mid。

如果不是，就要尽可能用完所有气球，$ans = (a + b + c) / 2$

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 150 + 10;const int MOD = 1e9 + 7;//const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; LL a[5]; int main(){    for (int i = 0; i < 3; i++) cin >> a[i];    sort(a, a + 3);    if (a[2] >= (a[0] + a[1]) << 1) cout << a[0] + a[1] << endl;    else cout << (a[1] + a[2] + a[0]) / 3 << endl;    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Greedy](/tags/Foundation-Greedy/)
