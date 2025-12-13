---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 1420 - Priest John's Busiest Day (贪心)
tags: []
layout: post
---

#  [UVa 1420 - Priest John's Busiest Day (贪心)](/2014/11/UVa-1420/ "UVa 1420 - Priest John's Busiest Day \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 24 2014 23:54

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有N对人要举行婚礼，从S到T，牧师必须参加一半**以上** 的婚礼过程，问他能不能参加完全部的婚礼。

## 思路

可以想到如果牧师赶到某个婚礼的时候的时间超过了MID值，他就完不成了。所以只要求出所有婚礼的MID值，排序，然后贪心即可。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 1e5 + 10;const int MOD = 1000007;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct POINT{    int st, ed, mid;    bool operator < (const POINT &a) const    {        if (mid != a.mid) return mid < a.mid;        return st < a.st;    }}pit[MAXN]; int main(){    //ROP;    int n, i, j;    while (scanf("%d", &n), n)    {        for (i = 0; i < n; i++)        {            scanf("%d%d", &pit[i].st, &pit[i].ed);            pit[i].mid = pit[i].st + (pit[i].ed - pit[i].st) / 2 + 1;        }        sort(pit, pit + n);        int curTime = 0;        for (i = 0; i < n; i++)        {            if (curTime >= pit[i].mid) break;            curTime = max(curTime, pit[i].st);            curTime += pit[i].mid - pit[i].st;        }        printf("%s\n", i == n ? "YES" : "NO");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)
