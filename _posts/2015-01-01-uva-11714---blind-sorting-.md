---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 11714 - Blind Sorting (机智)
tags: []
layout: post
---

#  [UVa 11714 - Blind Sorting (机智)](/2015/01/UVa-11714/ "UVa 11714 - Blind Sorting \(机智\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 12 2015 20:29

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

随意指定两个数，告诉大小，问要几次能得出最大的和第二大的。

## 思路

按照类似比赛的那种晋级法，最后得出冠军肯定要n - 1次，然后用亚军和冠军路上的对手都比一次。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    int n, i, j;    while (~scanf("%d", &n))    {        int ans = n - 1;        int cnt = 0;        while (n != 2)        {            n = (n + 1)>>1;            cnt++;        }        printf("%d\n", ans + cnt);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)
