---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 1551 - Cable master (二分)
tags: []
layout: post
---

#  [HDU 1551 - Cable master (二分)](/2015/03/HDU-1551/ "HDU 1551 - Cable master \(二分\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 11 2015 19:55

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

求最大每段电缆长度。

## 思路

二分

## 代码
    
    
    123456789101112131415161718192021222324

| 
    
    
    bool Check(double num){    int cnt = 0;    for (int i = 0; i < n; i++) cnt += arr[i] / num;    return cnt >= k;} int main(){    //ROP;    while (scanf("%d%d", &n, &k), n)    {        for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);        double l = 0, r = INF, mid;        while (r-l > 1e-4)        {            mid = (l+r)/2;            if (Check(mid)) l = mid;            else r = mid;        }        printf("%.2f\n", l);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)
