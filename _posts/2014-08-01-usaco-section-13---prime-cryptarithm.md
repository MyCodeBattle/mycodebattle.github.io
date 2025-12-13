---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.3 - Prime Cryptarithm
tags: []
layout: post
---

#  [USACO Section 1.3 - Prime Cryptarithm](/2014/08/USACO-1_3-crypt1/ "USACO Section 1.3 - Prime Cryptarithm")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 18 2014 21:58

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

计算出符合条件的数量

## 思路

暴力

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: crypt1*/ #include <cstdio>using namespace std;const int MAXN = 10; int num[MAXN]; bool Check(int n){    while (n)    {        if (!num[n % 10])            return false;        n /= 10;    }    return true;}int main(){    //freopen("input.txt", "r", stdin);    freopen("crypt1.in", "r", stdin);    freopen("crypt1.out", "w", stdout);     int n, i, j, a;    scanf("%d", &n);    for (i = 0; i < n; i++)    {        scanf("%d", &a);        num[a] = 1;    }    int cnt = 0;    for (i = 100; i <= 999; i++)    {        if (Check(i))            for (j = 10; j * i < 10000; j++)                if (Check(j))                {                    if (i * (j % 10) < 1000)                    {                        if (Check(i * (j % 10)))                        {                            int t = j / 10;                            if (i * t < 1000)                                if (Check(i * t) && Check(i * j))                                    cnt++;                        }                    }                }    }    printf("%d\n", cnt);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Foundation - Brute Force](/tags/Foundation-Brute-Force/)[Online Judge - USACO](/tags/Online-Judge-USACO/)
