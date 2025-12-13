---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1397 - Goldbach's Conjecture (筛素数)
tags: []
layout: post
---

#  [HDU 1397 - Goldbach's Conjecture (筛素数)](/2015/01/HDU-1397/ "HDU 1397 - Goldbach's Conjecture \(筛素数\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 27 2015 10:02

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出一个偶数能分解成几对素数和

## 思路

一遍扫描

## 代码
    
    
    1234567891011121314151617181920212223

| 
    
    
    void GetPrimeTable(){    int m = (int)sqrt(MAXN + 0.5);    for (int i = 2; i <= m; i++) if (!vis[i])        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;} int main(){    GetPrimeTable();    int n;    while (scanf("%d", &n), n)    {        int cnt = 0;        for (int i = 2; i <= (n>>1); i++)        {            if (vis[i] || vis[n-i]) continue;            cnt++;        }        printf("%d\n", cnt);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)
