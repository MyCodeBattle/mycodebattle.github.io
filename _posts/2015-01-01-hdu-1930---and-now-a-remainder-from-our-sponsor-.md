---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1930 - And Now, a Remainder from Our Sponsor (不互素的中国剩余定理)
tags: []
layout: post
---

#  [HDU 1930 - And Now, a Remainder from Our Sponsor (不互素的中国剩余定理)](/2015/01/HDU-1930/ "HDU 1930 - And Now, a Remainder from Our Sponsor \(不互素的中国剩余定理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 30 2015 18:04

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

先把字符按顺序01 02 03，三个一组组成一个序列，然后用这个序列模四个数，得到四个余数。

现在给出余数，让还原字符

## 思路

中国剩余定理的不互素情况。

用扩展欧几里得逐条合并。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061

| 
    
    
    int n;LL a[MAXN], r[MAXN]; void Extend_Gcd(LL a, LL b, LL &g, LL &x, LL &y){    if (!b) g = a, x = 1, y = 0;    else { Extend_Gcd(b, a%b, g, y, x); y -= x * (a/b); }} int num[10]; void Extend_Chinese_Remainder(LL &a1, LL &r1)   //计算K mod ai = ri, ri不互素情况{    LL a2, r2, x, y, g;    for (int i = 1; i < 4; i++)    {        a2 = a[i]; r2 = r[i];        Extend_Gcd(a1, a2, g, x, y);        LL C = r2 - r1, tmp = a2 / g;        x = C / g * x;        x = (x%tmp + tmp) % tmp;        r1 = a1*x + r1;        a1 = a1 / g * a2;        r1 = (r1%a1 + a1) % a1;    }} vector<int> ans; int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        ans.clear();        scanf("%d", &n);        for (int i = 0; i < 4; i++) scanf("%lld", &a[i]);        for (int i = 0; i < n; i++)        {            int tmp;            scanf("%d", &tmp);            for (int j = 0; j < 4; j++)                r[3-j] = tmp % 100, tmp /= 100;            LL a1 = a[0], r1 = r[0];            Extend_Chinese_Remainder(a1, r1);            for (int i = 0; i < 3; i++)                r[2-i] = r1 % 100, r1 /= 100;            for (int i = 0; i < 3; i++) ans.PB(r[i]);        }        int j;        for (j = SZ(ans)-1; j >= 0; j--)            if (ans[j] != 27) break;        for (int i = 0; i <= j; i++)            if (ans[i] == 27) printf(" ");            else printf("%c", ans[i] + 'A' - 1);        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)
