---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10163 - Storage Keepers
tags: []
layout: post
---

#  [UVa 10163 - Storage Keepers](/2014/07/UVa-10163/ "UVa 10163 - Storage Keepers")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 24 2014 15:28

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10163 - Storage Keepers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1104&mosmsg=Submission+received+with+ID+13936584)

## 题意

有N个柜子，M个人，一个柜子只能有一个人来打扫，一个人可以打扫多个柜子，求最大安全系数和这种情况下最少的钱。

## 思路

$dp[i][j]$表示前i个人打扫j个柜子。  
状态转移方程$dp[i][j] = max(dp[i][j], min(dp[i - 1][j - k], value[i] / k))$，不过之前得先让$dp[i][j] = dp[i - 1][j]$，意思是当前这个人不打扫柜子时的情况。

之后根据求出来的值去求最小花费

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 100 + 10;const int INF = 0x3f3f3f3f; int safe[MAXN], dp[MAXN][MAXN], fee[MAXN][MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int sto, n, i, j;    while (scanf("%d%d", &sto, &n), sto + n)    {        memset(dp, 0, sizeof dp);        memset(fee, 0x3f, sizeof fee);        for (i = 1; i <= n; i++)            scanf("%d", &safe[i]);        for (i = 1; i <= n; i++)        {            dp[i - 1][0] = INF;            for (j = 1; j <= sto; j++)            {                dp[i][j] = dp[i - 1][j];                for (int k = 1; k <= j; k++)                    dp[i][j] = max(dp[i][j], min(dp[i - 1][j - k], safe[i] / k));            }        }        //printf("%d\n", dp[n][sto]);        for (i = 1; i <= n; i++)        {            fee[i - 1][0] = 0;            for (j = 1; j <= sto; j++)            {                fee[i][j] = fee[i - 1][j];                for (int k = 1; k <= j; k++)                    if (safe[i] / k >= dp[n][sto])                        fee[i][j] = min(fee[i][j], fee[i - 1][j - k] + safe[i]);            }        }        if (dp[n][sto] == 0)            printf("0 0\n");        else            printf("%d %d\n", dp[n][sto], fee[n][sto]);    }    return 0; }  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)
