---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 5187 - zhx's contest (思维 + 快速乘)
tags: []
layout: post
---

#  [HDU 5187 - zhx's contest (思维 + 快速乘)](/2015/03/HDU-5187/ "HDU 5187 - zhx's contest \(思维 + 快速乘\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 15 2015 10:24

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

一个序列是漂亮的序列，当1~i是递增或者递减，并且i~n是递增或者递减。

问有几种。

## 思路

关键点在于考虑最大的数n。

在n前面的肯定是递增的，n后面的肯定是递减的。  
同理，在1前面肯定是递减的。

所以 $ans = (C_n^0 + C_n_1 + ... + C_n^n) * 2 - 2 = 2^n-2$

特判一下`n=1`和`p=1`的情况。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738

| 
    
    
    LL Multi(LL a, LL b, LL n){    LL ret = 0;    while (b)    {        if (b & 1) ret = (ret + a) % n;        a = (a<<1) % n;        b >>= 1;    }    return ret;} LL pow_mod(LL a, LL m, LL n){    LL ret = 1;    while (m)    {        if (m & 1) ret = Multi(ret, a, n);        a = Multi(a, a, n);        m >>= 1;    }    return ret;} int main(){    //ROP;    LL n, p;    while (cin >> n >> p)    {        if (p == 1) { cout << "0" << endl; continue; }        if (n == 1) { cout << "1" << endl; continue; }        LL ans = pow_mod(2, n, p);        ans -= 2;        cout << (ans % p + p) % p << endl;    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)
