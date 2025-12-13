---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11292 - Dragon of Loowater
tags: []
layout: post
---

#  [UVa 11292 - Dragon of Loowater](/2014/08/UVa-11292/ "UVa 11292 - Dragon of Loowater")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 19 2014 10:03

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11292 - Dragon of Loowater](http://vjudge.net/vjudge/problem/viewProblem.action?id=19048)

## 题意

一条龙有K个头，每个头都有直径。骑士有H能力值，只能砍直径H以下的头，收钱H，求最小花费干掉怪兽。

## 思路

排序一下，能干就干，不能干就算

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#define MP(a, b) make_pair(a, b)const int MAXN = 20000 + 10;const int INF = 0x3f3f3f3f; int dag[MAXN], knt[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, m, i, j;    while (scanf("%d%d", &n, &m), n + m)    {        for (i = 0; i < n; i++)            scanf("%d", &dag[i]);        for (i = 0; i < m; i++)            scanf("%d", &knt[i]);        sort(dag, dag + n);        sort(knt, knt + m);        int ans = 0;        i = 0;        for (j = 0; j < m; j++)            if (knt[j] >= dag[i])            {                ans += knt[j];                i++;                if (i == n)                    break;            }        i != n ? printf("Loowater is doomed!\n") : printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Others](/tags/Foundation-Others/)
