---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10375 - Choose and divide
tags: []
layout: post
---

#  [UVa 10375 - Choose and divide](/2014/07/UVa-10375/ "UVa 10375 - Choose and divide")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 30 2014 19:36

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10375 - Choose and divide](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1316&mosmsg=Submission+received+with+ID+13967067)

## 题意

求两个组合数的商

## 思路

根据

$$C_{n}^{k}=\dfrac {n-k+1} {k}\cdot C_{n}^{k-1}$$

一乘一除就不会溢出。

## 代码
    
    
    123456789101112131415161718192021222324

| 
    
    
    #include <bits/stdc++.h>#define LL long longusing namespace std; int main(){    //freopen("input.txt", "r", stdin);    int p, q, r, s, i, j;    while (~scanf("%d%d%d%d", &p, &q, &r, &s))    {        double ans = 1;        q = min(p - q, q);        s = min(r - s, s);        for (i = 1; i <= max(q, s); i++)        {            if (i <= q)                ans = ans * (p - i + 1) / i;            if (i <= s)                ans = ans / (r - i + 1) * i;        }        printf("%.05f\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Math - Number Theory](/tags/Math-Number-Theory/)[Online Judge - UVa](/tags/Online-Judge-UVa/)
