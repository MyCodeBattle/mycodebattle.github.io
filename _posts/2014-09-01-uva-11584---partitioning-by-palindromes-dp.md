---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11584 - Partitioning by Palindromes (简单DP)
tags: []
layout: post
---

#  [UVa 11584 - Partitioning by Palindromes (简单DP)](/2014/09/UVa-11584/ "UVa 11584 - Partitioning by Palindromes \(简单DP\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 24 2014 15:04

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

求一个字符串能最少分成几个回文串。

## 思路

$dp[i] = min(dp[i], dp[j - 1] + 1), [j, i]是回文串, 1 <= j < i$

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1000 + 5; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int dp[MAXN];char str[MAXN]; bool Check(int l, int r){    while (l < r)    {        if (str[l] != str[r]) return false;        l++; r--;    }    return true;} int main(){    //ROP;    int T, i, j;    scanf("%d", &T);    while (T--)    {        scanf("%s", str + 1);        int len = strlen(str + 1);        for (i = 1; i <= len; i++)        {            dp[i] = dp[i - 1] + 1;            for (j = 1; j < i; j++)                if (Check(j, i)) dp[i] = min(dp[j - 1] + 1, dp[i]);        }        printf("%d\n", dp[len]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[DP - 递推](/tags/DP-递推/)
