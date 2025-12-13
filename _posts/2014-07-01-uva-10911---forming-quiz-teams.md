---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10911 - Forming Quiz Teams
tags: []
layout: post
---

#  [UVa 10911 - Forming Quiz Teams](/2014/07/UVa-10911/ "UVa 10911 - Forming Quiz Teams")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 15 2014 0:46

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10911 - Forming Quiz Teams](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1852&mosmsg=Submission+received+with+ID+13885097)

## 题意

给出n * 2个点，要求配出n组点，使每组点的距离之和最短。

## 思路

小白上的例题，不过因为涉及到位运算，脑子有点转不过来，只能勉强理解。

把每种状态压缩，然后DP。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142

| 
    
    
    #include <bits/stdc++.h>using namespace std;const int INF = 0x3f3f3f3f; struct POINT{    int x, y;}point[20]; double dp[(1 << 20)]; double Dis(int i, int j){    return hypot(point[i].x - point[j].x, point[i].y - point[j].y);} int main(){    //freopen("input.txt", "r", stdin);    int i, j, n, cases = 0;    char str[200];    while (scanf("%d", &n), n)    {        n = n * 2;        for (i = 0; i < n; i++)            scanf("%s%d%d", str, &point[i].x, &point[i].y);        dp[0] = 0;        for (int s = 1; s < (1 << n); s++)        {            dp[s] = INF;            for (i = 0; i < n; i++)                if (s & (1 << i))                    break;            for (j = i + 1; j < n; j++)                if (s & (1 << j))                    dp[s] = min(dp[s], Dis(i, j) + dp[s ^ (1 << i) ^ (1 << j)]);        }        printf("Case %d: %.2lf\n",++cases, dp[(1 << n) - 1]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)[Must Be Done Again](/tags/Must-Be-Done-Again/)
