---
categories: Posts
date: 2015-01-30 00:00:00
title: HDU 1905 -  Pseudoprime numbers (快速幂)
tags: []
layout: post
---

## 题意

判断一个数是不是伪素数

## 思路

先判断素数，再快速幂一下。

## 代码


```c++
LL Quick_Mod(LL a, LL m, LL n)
{
    LL ans = 1;
    while (m)
    {
        if (m & 1) ans = ans * a % n;
        a = a * a % n;
        m >>= 1;
    }
    return ans;
}
 
bool Check(LL p)
{
    int m = sqrt(p + 0.5);
    for (int i = 2; i <= m; i++)
        if (p % i == 0) return false;
    return true;
}
 
int main()
{
    //ROP;
    LL p, a;
    while (cin >> p >> a, p + a)
    {
        if (Check(p)) { cout << "no" << endl; continue; }
        LL tmp = Quick_Mod(a, p, p);
        if (tmp == a % p) cout << "yes" << endl;
        else cout << "no" << endl;
    }
    return 0;
}
```