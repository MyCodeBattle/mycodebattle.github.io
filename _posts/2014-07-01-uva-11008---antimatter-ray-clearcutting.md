---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 11008 - Antimatter Ray Clearcutting
tags: []
layout: post
---

#  [UVa 11008 - Antimatter Ray Clearcutting](/2014/07/UVa-11008/ "UVa 11008 - Antimatter Ray Clearcutting")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 22 2014 16:06

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11008 - Antimatter Ray Clearcutting](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1949&mosmsg=Submission+received+with+ID+13924213)

## 题意

用一把激光枪，一枪可以打死同一直线上的树，求最少几枪可以干掉n - m颗树。

## 思路

状态压缩DP，但是不会做。  
参考了[Titanium的解题报告](http://www.cnblogs.com/scau20110726/archive/2012/09/28/2707866.html)

用$dp[i]$表示在i这个状态的时候还要几枪才能达到目的，然后记忆化搜索。  
还要好好体会。。。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 16 + 1;const int INF = 0x3f3f3f3f; struct TREE{    int x, y;}tree[MAXN]; int slope[MAXN][MAXN], dp[(1 << 18)], n, m, remain; int DFS(int sta){    int i, sum = 0, j;    int &cur = dp[sta];    if (cur != -1)        return cur;    for (i = 0; i < n; i++)        if ((1 << i) & sta)            sum++;    if (sum <= remain)        return cur = 0;    if (sum == 1)        return cur = 1;    cur = INF;    for (i = 0; i < n; i++)        if ((1 << i) & sta)            for (j = i + 1; j < n; j++)                if ((1 << j) & sta)                    cur = min(cur, DFS(sta & (~slope[i][j])) + 1);    return cur;} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, cases = 0;    scanf("%d", &T);    while (T--)    {        memset(dp, -1, sizeof dp);        scanf("%d%d", &n, &m);        remain = n - m;        for (i = 0; i < n; i++)            scanf("%d%d", &tree[i].x, &tree[i].y);        for (i = 0; i < n; i++)            for (j = 0; j < n; j++)            {                if (i == j)                    continue;                for (int k = n - 1; k >= 0; k--)                {                    slope[i][j] <<= 1;                    if ((tree[k].y - tree[i].y) * (tree[j].x - tree[i].x) == (tree[j].y - tree[i].y) * (tree[k].x - tree[i].x))                        slope[i][j]++;                }            }        int ans = DFS((1 << n) - 1);        printf("Case #%d:\n%d\n", ++cases, ans);        if (T)            printf("\n");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)[Must Be Done Again](/tags/Must-Be-Done-Again/)
