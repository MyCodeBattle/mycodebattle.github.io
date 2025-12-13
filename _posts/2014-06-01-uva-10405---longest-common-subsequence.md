---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 10405 - Longest Common Subsequence
tags: []
layout: post
---

#  [UVa 10405 - Longest Common Subsequence](/2014/06/UVa-10405/ "UVa 10405 - Longest Common Subsequence")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jun 29 2014 17:19

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10405 - Longest Common Subsequence](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1346&mosmsg=Submission+received+with+ID+13808165)

## 题意

求最长公共子序列

## 思路

题目简单粗暴地告诉我们求最长公共子序列。。。

## 代码
    
    
    123456789101112131415161718192021222324252627282930

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 1000 + 100;int dp[MAXN][MAXN];int main(){    //freopen("input.txt", "r", stdin);    int i, j, ans;    char astr[MAXN], bstr[MAXN];    while (gets(astr))    {        memset(dp, 0, sizeof(dp));        gets(bstr);        int len1 = strlen(astr), len2 = strlen(bstr);        for (i = 1; i <= strlen(astr); i++)            for (j = 1; j <= strlen(bstr); j++)            {                if (astr[i - 1] == bstr[j - 1])                    dp[i][j] = dp[i - 1][j - 1] + 1;                else                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);            }            printf("%d\n", dp[len1][len2]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Dynamic Programming](/tags/Dynamic-Programming/)
