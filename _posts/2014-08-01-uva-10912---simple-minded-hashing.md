---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10912 - Simple Minded Hashing
tags: []
layout: post
---

#  [UVa 10912 - Simple Minded Hashing](/2014/08/UVa-10912/ "UVa 10912 - Simple Minded Hashing")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 8 2014 16:34

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10912 - Simple Minded Hashing](http://vjudge.net/problem/viewProblem.action?id=24899)

## 题意

给一个sum和length，问有几种严格递增的字符串符合。

## 思路

搞了很久的二维数组还是搞不出来，原来要开三维的（ ＴДＴ）图样

$$dp(i, j, k) = dp(i - 1, j - 1, k - i) + dp(i - 1, j, k)$$

$dp(i, j, k)表示前i个字母，j长度，sum为k的时候的情况，每个字母都有选和不选两种。

边界$dp(0, 0, 0) = 1$

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 400; int dp[30][30][MAXN], L, S; int main(){    int i, j, cases = 0;    dp[0][0][0] = 1;    for (i = 1; i <= 26; i++)        for (j = 0; j <= i; j++)            for (int k = 0; k <= 351; k++)            {                dp[i][j][k] = dp[i - 1][j][k];                if (j && k >= i)                    dp[i][j][k] += dp[i - 1][j - 1][k - i];            }    while (scanf("%d%d", &L, &S), L + S)    {        printf("Case %d: ", ++cases);        if (L > 26 || S > 351)        {            puts("0");            continue;        }        printf("%d\n", dp[26][L][S]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)
