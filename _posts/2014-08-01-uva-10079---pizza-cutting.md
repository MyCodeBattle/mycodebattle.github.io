---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10079 - Pizza Cutting
tags: []
layout: post
---

#  [UVa 10079 - Pizza Cutting](/2014/08/UVa-10079/ "UVa 10079 - Pizza Cutting")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 4 2014 21:22

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10079 - Pizza Cutting](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1020)

## 题意

求n刀最多能切几块

## 思路

耍赖了，上OEIS查了一下。

$$f\left( n\right) =\dfrac {n * \left( n+1\right) } {2} + 1$$

## 代码
    
    
    1234567891011

| 
    
    
    #include <bits/stdc++.h>#define LL long longusing namespace std; int main(){    LL ans, n;    while (~scanf("%lld", &n), n >= 0)        printf("%lld\n", n * (n + 1) / 2 + 1);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Math - Number Theory](/tags/Math-Number-Theory/)
