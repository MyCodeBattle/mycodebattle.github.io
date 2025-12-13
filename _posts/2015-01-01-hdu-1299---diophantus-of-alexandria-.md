---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1299 - Diophantus of Alexandria (唯一分解定理)
tags: []
layout: post
---

## 题意

给定一个n，问有几组$\Large \frac {1}{x} + \frac {1}{y} = \frac {1}{n}$

## 思路

显然x > n && y > n。

设$x = n + a, y = n + b$，化简得$n^2 = ab$

所以问题就转化为求$n^2$的因子数。求出来之后$(ans + 1) / 2$就是答案。

如何求因子数？

根据唯一分解定理，一个数总可以被分解为有限个素数的乘积$N = P _{1}^{a_1}P_{2}^{a _2}…P_{n}^{a_n}$

因数个数为$k = (a_1 + 1) * (a_2 + 1) … * (a_n + 1)$

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546

| ```c++
vector<int> prime;int vis[MAXN]; void GetPrimeTable(){    int m = (int)sqrt(MAXN + 0.5);    for (int i = 2; i <= m; i++) if (!vis[i])        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;    for (int i = 2; i < MAXN; i++) if (!vis[i])        prime.PB(i);} int Solve(int n){    int ans = 1;    for (int i = 0; i < SZ(prime); i++)    {        int cnt = 0;        if (prime[i] > n) break;        while (n % prime[i] == 0)        {            cnt++;            n /= prime[i];        }        ans *= ((cnt<<1) + 1);    }    if (n != 1) ans *= 3;    return ans;} int main(){    GetPrimeTable();    int T;    scanf("%d", &T);    while (T--)    {        int n;        scanf("%d", &n);        int ans = Solve(n);        printf("Scenario #%d:\n", ++cases);        printf("%d\n", (ans+1) >> 1);        puts("");    }    return 0;}
```