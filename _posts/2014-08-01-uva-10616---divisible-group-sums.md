---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10616 - Divisible Group Sums
tags: []
layout: post
---

#  [UVa 10616 - Divisible Group Sums](/2014/08/UVa-10616/ "UVa 10616 - Divisible Group Sums")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 8 2014 19:25

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10616 - Divisible Group Sums](http://vjudge.net/problem/viewProblem.action?id=27250)

## 题意

从给出的数字当中选出M个，它们的和能被D整除，求个数。

## 思路

和上一题差不多。  
$dp(i, j, k)$表示前i个选j个余数是k的情况。

$$dp(i, j, k) = dp(i - 1, j, k) + dp(i - 1, j - 1, kk)$$

$kk = (D + k - num[i] \% D) \% D)$。这步想不出来TAT

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 205; LL dp[MAXN][15][21]; int num[MAXN], N, Q, M, D; void Solve(){    dp[0][0][0] = 1;    for (int i = 1; i <= N; i++)        for (int j = 0; j <= M; j++)            for (int k = 0; k < D; k++)            {                dp[i][j][k] = dp[i - 1][j][k];                if (j)                {                    int temp = (D + k - num[i] % D) % D;                    dp[i][j][k] += dp[i - 1][j - 1][temp];                }            }} int main(){    //freopen("input.txt", "r", stdin);    int i, j, bCases = 0;    while (scanf("%d%d", &N, &Q), N + Q)    {        printf("SET %d:\n", ++bCases);        int cases = 0;        for (i = 1; i <= N; i++)            scanf("%d", #[i]);        for (i = 0; i < Q; i++)        {            printf("QUERY %d: ", ++cases);            memset(dp, 0, sizeof dp);            scanf("%d%d", &D, &M);            Solve();            printf("%lld\n", dp[N][M][0]);        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)
