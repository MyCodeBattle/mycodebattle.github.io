---
categories: Posts
date: 2014-09-01 00:00:00
title: USACO Section 1.5 - Number Triangles (简单DP)
tags: []
layout: post
---

#  [USACO Section 1.5 - Number Triangles (简单DP)](/2014/09/USACO-1_5-number-trangles/ "USACO Section 1.5 - Number Triangles \(简单DP\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 23 2014 18:57

**Contents**

  1. 1. 代码

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: numtri*/ #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1000 + 5; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int mp[MAXN][MAXN]; int main(){    //ROP;    freopen("numtri.in", "r", stdin);    freopen("numtri.out", "w", stdout);     int n, i, j;    scanf("%d", &n);    for (i = 1; i <= n; i++)        for (j = 1; j <= i; j++) scanf("%d", ∓[i][j]);    for (i = n - 1; i >= 1; i--)        for (j = 1; j <= i; j++)            mp[i][j] = max(mp[i + 1][j], mp[i + 1][j + 1]) + mp[i][j];    printf("%d\n", mp[1][1]);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - USACO](/tags/Online-Judge-USACO/)[DP - 递推](/tags/DP-递推/)
