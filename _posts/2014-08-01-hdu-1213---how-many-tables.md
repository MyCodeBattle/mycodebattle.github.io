---
categories: Posts
date: 2014-08-01 00:00:00
title: HDU 1213 - How Many Tables
tags: []
layout: post
---

#  [HDU 1213 - How Many Tables](/2014/08/HDU-1213/ "HDU 1213 - How Many Tables")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 23 2014 15:41

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[HDU 1213 - How Many Tables](http://www.bnuoj.com/v3/problem_show.php?pid=5413)

## 题意

给一些认识的人的名单，求要准备几张桌子

## 思路

并查集

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>#define MP(a, b) make_pair(a, b)using namespace std;const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f; int vis[MAXN], pa[MAXN]; int Find(int x){    return pa[x] == x ? x : pa[x] = Find(pa[x]);} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, n, npep, a, b;    scanf("%d", &T);    while (T--)    {        int cnt = 0;        memset(vis, 0, sizeof vis);        scanf("%d%d", &npep, &n);        for (i = 1; i <= npep; i++)            pa[i] = i;        for (i = 0; i < n; i++)        {            scanf("%d%d", &a, &b);            int x = Find(a), y = Find(b);            if (x != y)                pa[x] = y;        }        for (i = 1; i <= npep; i++)        {            int v = Find(i);            if (!vis[v])                cnt++, vis[v] = 1;        }        printf("%d\n", cnt);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Data Structure - Disjoint Set](/tags/Data-Structure-Disjoint-Set/)
