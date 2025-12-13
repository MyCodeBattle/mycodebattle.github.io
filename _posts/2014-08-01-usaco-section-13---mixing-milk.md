---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.3 - Mixing Milk
tags: []
layout: post
---

#  [USACO Section 1.3 - Mixing Milk](/2014/08/USACO-1_3-milk/ "USACO Section 1.3 - Mixing Milk")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 15 2014 21:08

**Contents**

  1. 1. 题意
  2. 2. 代码

## 题意

求最便宜的买牛奶方法。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: milk*/ #include <bits/stdc++.h>using namespace std;const int MAXN = 5000 + 100; struct PRICE{    int per, amount;    bool operator < (const PRICE &a) const    {        return per < a.per;    }}far[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    freopen("milk.in", "r", stdin);    freopen("milk.out", "w", stdout);     int need, i, j, n, ans;    scanf("%d%d", &need, &n);    for (i = 0; i < n; i++)        scanf("%d%d", &far[i].per, &far[i].amount);    sort(far, far + n);    ans = 0;    for (i = 0; i < n; i++)    {        if (need >= far[i].amount)        {            need -= far[i].amount;            ans += far[i].per * far[i].amount;        }        else        {            ans += far[i].per * need;            break;        }    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - USACO](/tags/Online-Judge-USACO/)[Foundation - Greedy](/tags/Foundation-Greedy/)
