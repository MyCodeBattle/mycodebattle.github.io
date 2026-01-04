---
categories: Posts
date: 2015-03-23 00:00:00
title: HDU 3037 - Saving Beans (Lucas定理)
tags: []
layout: post
---

## 题意

有n个树。现在不能收获超过k个豆子，问有几种方法。

## 思路

问题等价于求出 $x_1 + x_2 ... + x_n = k$的非负整数解的个数。

思路有点神奇。

用隔板法，得出：  
当收获k个豆子时，答案为$C_{n+k-1}^{k}$  
所以最终的答案为$C_{n-1}^0 + C_n^1 + ... + C_{n+m-1}^m$

因为$C_n^k = C_{n-1}^k + C_{n-1}^{k-1}$。

然后合并，最后答案就是$C_{n+m-1}^m$

然后用一下Lucas定理。。

## 代码


```c++
LL Extend_GCD(LL a, LL b, LL &d, LL &x, LL &y)
{
    if (!b) { d = a, x = 1, y = 0; }
    else
    {
        Extend_GCD(b, a%b, d, y, x);
        y -= x * (a/b);
    }
}
 
LL inv(LL a, LL p)
{
    LL d, x, y;
    Extend_GCD(a, p, d, x, y);
    return (x+p) % p;
}
 
LL C(LL n, LL m, LL p)
{
    LL ret = 1, a = 1, b = 1;
    while (m)
    {
        a = a*n%p;
        b = b*m%p;
        n--, m--;
    }
    return a * inv(b, p) % p;
}
 
LL Lucas(LL n, LL m, LL p)
{
    if (m == 0) return 1;
    return C(n%p, m%p, p) * Lucas(n/p, m/p, p)%p;
}
 
int main()
{
    //ROP;
    int T;
    cin >> T;
    while (T--)
    {
        LL n, m, p;
        cin >> n >> m >> p;
        cout << Lucas(m+n, n, p) << endl;
    }
    return 0;
}
```