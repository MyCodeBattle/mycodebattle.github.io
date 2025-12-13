---
categories: Posts
date: 2014-09-01 00:00:00
title: CodeForces 471C - MUH and House of Cards
tags: []
layout: post
---

#  [CodeForces 471C - MUH and House of Cards](/2014/09/codeforces-471c/ "CodeForces 471C - MUH and House of Cards")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 27 2014 15:52

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出n个木棒，问能叠成多少种不同高度的房子。

## 思路

  1. 算出某个高度最少所需木棒。

  2. 如果这个高度所需木棒小于当前木棒，判断能否正好用完。

对于第一个，可知从上往下分别是1个屋顶，两个屋顶……k个屋顶。这时候是最省的。

这时候所用木棒为(1 + k) * k / 2 * 2（这是屋顶所用的） + k * (k - 1) / 2（连接屋顶的小横杠) = (1 + k) * k / 2 * 3 - k

如何判断能否正好用完？

在完成最低限度的建房子之后，如果要加木棒，只能3根3根加。所以判断n-k能不能整除3即可。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    LL n, i, j;    cin >> n;    LL ans = 0;    for (i = 1; ; i++)    {        LL temp = (((1 + i) * i) >> 1) * 3 - i;        if (temp > n) break;        if ((n - temp) % 3 == 0) ans++;    }    cout << ans << endl;    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Math - Others](/tags/Math-Others/)[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)
