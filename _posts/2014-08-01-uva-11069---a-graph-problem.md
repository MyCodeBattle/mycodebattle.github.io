---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11069 - A Graph Problem
tags: []
layout: post
---

#  [UVa 11069 - A Graph Problem](/2014/08/UVa-11069/ "UVa 11069 - A Graph Problem")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 5 2014 17:40

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11069 - A Graph Problem](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2010)

## 题意

有n数，选出集合满足以下条件：

  1. 相差2或者3
  2. 尽可能长

## 思路

只要加上相差两位和三位的情况即可

$dp[i] = dp[i - 2] + dp[i - 3]$

## 代码
    
    
    1234567891011121314151617

| 
    
    
    #include <bits/stdc++.h>#define LL long longusing namespace std; LL dp[100]; int main(){    int n;    dp[0] = 1, dp[1] = 1, dp[2] = 2;    for (int i = 3; i <= 76; i ++)        dp[i] = dp[i - 2] + dp[i - 3];    while (~scanf("%d", &n))        printf("%lld\n", dp[n]);    return 0; }  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)
