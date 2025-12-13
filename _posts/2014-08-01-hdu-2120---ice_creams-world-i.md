---
categories: Posts
date: 2014-08-01 00:00:00
title: HDU 2120 - Ice_cream's world I
tags: []
layout: post
---

#  [HDU 2120 - Ice_cream's world I](/2014/08/HDU-2120/ "HDU 2120 - Ice_cream's world I")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 25 2014 11:32

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[HDU 2120 - Ice_cream’s world I](http://www.bnuoj.com/v3/problem_show.php?pid=6264)

## 题意

有N个点，给出两点，意味着这是一堵墙，围起来的算一块地，求有几块地

就是求环的数量

## 思路

并查集。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>#include <map>#include <queue>#define MP(a, b) make_pair(a, b)using namespace std;const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f; int pa[MAXN]; int Find(int x){    return pa[x] == x ? x : pa[x] = Find(pa[x]);} int main(){    //freopen("input.txt", "r", stdin);    int nw, n, i, j, a, b;    while (~scanf("%d%d", &nw, &n))    {        int cnt = 0;        for (i = 0; i < nw; i++)            pa[i] = i;        for (i = 0; i < n; i++)        {            scanf("%d%d", &a, &b);            int x = Find(a), y = Find(b);            x == y ? cnt++ : pa[x] = y;        }        printf("%d\n", cnt);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Data Structure - Disjoint Set](/tags/Data-Structure-Disjoint-Set/)
