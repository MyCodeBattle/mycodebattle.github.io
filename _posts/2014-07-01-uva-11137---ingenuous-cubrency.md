---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 11137 - Ingenuous Cubrency
tags: []
layout: post
---

#  [UVa 11137 - Ingenuous Cubrency](/2014/07/UVa-11137/ "UVa 11137 - Ingenuous Cubrency")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 11 2014 21:22

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 代码
    1. 3.1. 递推
    2. 3.2. 记忆化搜索

## 传送门

[UVa 11137 - Ingenuous Cubrency](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=2078)

## 题意

和换硬币一样

## 代码

### 递推
    
    
    12345678910111213141516171819

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 10000 + 100; long long dp[MAXN]; int main(){    int i, j, n, money;    dp[0] = 1;    for (i = 1; i <= 21; i++)        for (j = i * i * i; j < 10000; j++)            dp[j] += dp[j - i * i * i];    while (~scanf("%d", &money))        printf("%lld\n", dp[money]);    return 0;}  
  
---|---  
  
### 记忆化搜索
    
    
    12345678910111213141516171819202122232425262728293031323334

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 10000 + 100;long long coin[22], dp[MAXN][22];long long DFS(int money, int k){    long long &ans = dp[money][k];    if (ans > 0)        return ans;    for (int i = k; i < 21; i++)        if (money - coin[i] >= 0)            ans += DFS(money - coin[i], i);    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int i, j, k, money;    for (i = 1; i <= 21; i++)        coin[i - 1] = i * i * i;    for (i = 0; i < 22; i++)        dp[0][i] = 1;    while (~scanf("%lld", &money))    {        long long ans = DFS(money, 0);        printf("%lld\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Dynamic Programming](/tags/Dynamic-Programming/)
