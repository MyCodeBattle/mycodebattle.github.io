---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.1 - Your Ride Is Here
tags: []
layout: post
---

#  [USACO Section 1.1 - Your Ride Is Here](/2014/08/USACO-1_1-ride/ "USACO Section 1.1 - Your Ride Is Here")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 9 2014 22:56

**Contents**

  1. 1. 题意
  2. 2. 代码

## 题意

给两个字符串，看他们mod47的值相不相等

## 代码
    
    
    123456789101112131415161718192021222324252627

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: ride*/ ​#include <bits/stdc++.h>using namespace std; int main(){    freopen("ride.in", "r", stdin);    freopen("ride.out", "w", stdout);    string comet, we;    cin >> comet >> we;    int ncom = 1, nwe = 1;    for (int i = 0; i < comet.length(); i++)        ncom = ncom * ((comet[i] - 'A') + 1) % 47;    for (int i = 0; i < we.length(); i++)        nwe = nwe * ((we[i] - 'A') + 1) % 47;    if (ncom == nwe)        printf("GO\n");    else        printf("STAY\n");    return 0; }  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - USACO](/tags/Online-Judge-USACO/)
