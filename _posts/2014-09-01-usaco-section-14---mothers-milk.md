---
categories: Posts
date: 2014-09-01 00:00:00
title: USACO Section 1.4 - Mother's Milk
tags: []
layout: post
---

#  [USACO Section 1.4 - Mother's Milk](/2014/09/USACO-1_4-milk3/ "USACO Section 1.4 - Mother's Milk")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 9 2014 19:09

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有三个桶，刚开始第三个是满的，问第一个是0的时候第三个桶的情况。

## 思路

无脑倒水，只要有水就倒。记录每一种状态是否达到过。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: milk3*/ #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 25 + 5;const int INF = 0x3f3f3f3f;using namespace std; int aFull, bFull, cFull, dp[MAXN][MAXN][MAXN];set<int> st; void DFS(int a, int b, int c){    if (dp[a][b][c]) return;    dp[a][b][c] = 1;    if (a == 0) st.insert(c);    if (a != 0)    {        if (b < bFull)            DFS(a - min(a, bFull - b), b + min(a, bFull - b), c);        if (c < bFull)            DFS(a - min(a, cFull - c), b, c + min(a, cFull - c));    }    if (b != 0)    {        if (a < aFull)            DFS(a + min(b, aFull - a), b - min(b, aFull - a), c);        if (c < cFull)            DFS(a, b - min(b, cFull - c), c + min(b, cFull - c));    }    if (c != 0)    {        if (a < aFull)            DFS(a + min(c, aFull - a), b, c - min(c, aFull - a));        if (b < bFull)            DFS(a, b + min(c, bFull - b), c - min(c, bFull - b));    }} int main(){    //freopen("input.txt", "r", stdin);    freopen("milk3.in", "r", stdin);    freopen("milk3.out", "w", stdout);     int a, b, c, i, j;    scanf("%d%d%d", &aFull, &bFull, &cFull);    DFS(0, 0, cFull);    for (set<int>::iterator it = st.begin(); it != st.end(); it++)    {        if (it == st.begin()) printf("%d", *it);        else printf(" %d", *it);    }    puts("");    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Foundation - Search](/tags/Foundation-Search/)[Online Judge - USACO](/tags/Online-Judge-USACO/)
