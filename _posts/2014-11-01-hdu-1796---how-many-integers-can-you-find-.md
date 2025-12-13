---
categories: Posts
date: 2014-11-01 00:00:00
title: HDU 1796 - How many integers can you find (容斥原理)
tags: []
layout: post
---

#  [HDU 1796 - How many integers can you find (容斥原理)](/2014/11/HDU-1796/ "HDU 1796 - How many integers can you find \(容斥原理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 14 2014 13:03

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出小于N的，能整除一个集合里的数的个数。

## 思路

最基本的容斥原理。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-8;const int MAXN = 60;const int MOD = 1000007; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int ans, n, pivot;vector<int> num; int LCM(int a, int b){    return a / __gcd(a, b) * b;} int DFS(int curPos, int curPro, int curCnt){    for (int i = curPos; i < SZ(num); i++)    {        int tmp = (pivot - 1) / LCM(curPro, num[i]);        if (curCnt & 1) ans += tmp;        else ans -= tmp;        DFS(i + 1, LCM(curPro, num[i]), curCnt + 1);    }} int main(){    //ROP;    int i, j;    while (cin >> pivot >> n)    {        num.clear();        ans = 0;        for (i = 0; i < n; i++)        {            int tmp;            scanf("%d", &tmp);            if (tmp) num.PB(tmp);        }        DFS(0, 1, 1);        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Combinatorics](/tags/Math-Combinatorics/)
