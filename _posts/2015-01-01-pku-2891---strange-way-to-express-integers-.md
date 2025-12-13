---
categories: Posts
date: 2015-01-01 00:00:00
title: PKU 2891 - Strange Way to Express Integers (中国剩余定理不互质情况)
tags: []
layout: post
---

#  [PKU 2891 - Strange Way to Express Integers (中国剩余定理不互质情况)](/2015/01/PKU-2891/ "PKU 2891 - Strange Way to Express Integers \(中国剩余定理不互质情况\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 28 2015 20:55

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

上一题的降级版

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839

| 
    
    
    void Extend_GCD(LL a, LL b, LL &d, LL &x, LL &y){    if (!b) d = a, x = 1, y = 0;    else { Extend_GCD(b, a%b, d, y, x); y -= x * (a/b); }} int main(){    //ROP;    int n;    while (~scanf("%d", &n))    {        LL a1, r1;        scanf("%lld%lld", &a1, &r1);        bool flag = false;        if (n == 1) r1 = a1+r1;        for (int i = 0; i < n-1; i++)        {            LL a2, r2;            scanf("%lld%lld", &a2, &r2);            if (flag) continue;            LL x, y, A = a1, B = a2, C = r2 - r1, g;            Extend_GCD(A, B, g, x, y);            if (C % g)            {                flag = true;                continue;            }            x = C / g * x;            x = x - (x*g/B) * (B/g);            if (x < 0) x += B / g;            r1 = x*a1 + r1;            a1 = a1 / g * a2;        }        if (flag) puts("-1");        else printf("%lld\n", r1);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Math - Number Theory](/tags/Math-Number-Theory/)
