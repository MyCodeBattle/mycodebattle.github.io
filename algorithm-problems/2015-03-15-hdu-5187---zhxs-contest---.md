---
categories: Posts
date: 2015-03-15 00:00:00
title: HDU 5187 - zhx's contest (思维 + 快速乘)
tags: []
layout: post
---

## 题意

一个序列是漂亮的序列，当1~i是递增或者递减，并且i~n是递增或者递减。

问有几种。

## 思路

关键点在于考虑最大的数n。

在n前面的肯定是递增的，n后面的肯定是递减的。  
同理，在1前面肯定是递减的。

所以 $ans = (C_n^0 + C_n_1 + ... + C_n^n) * 2 - 2 = 2^n-2$

特判一下
```c++
n=1
```
和
```c++
p=1
```
的情况。

## 代码


```c++
LL Multi(LL a, LL b, LL n)
{
    LL ret = 0;
    while (b)
    {
        if (b & 1) ret = (ret + a) % n;
        a = (a<<1) % n;
        b >>= 1;
    }
    return ret;
}
 
LL pow_mod(LL a, LL m, LL n)
{
    LL ret = 1;
    while (m)
    {
        if (m & 1) ret = Multi(ret, a, n);
        a = Multi(a, a, n);
        m >>= 1;
    }
    return ret;
}
 
int main()
{
    //ROP;
    LL n, p;
    while (cin >> n >> p)
    {
        if (p == 1) { cout << "0" << endl; continue; }
        if (n == 1) { cout << "1" << endl; continue; }
        LL ans = pow_mod(2, n, p);
        ans -= 2;
        cout << (ans % p + p) % p << endl;
    }
    return 0;
}
```