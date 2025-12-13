---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10236 - The Fibonacci Primes
tags: []
layout: post
---

## 传送门

[UVa 10236 - The Fibonacci Primes](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1177)

## 题意

求第n个Fibonacci素数。

## 思路

参考了他人的题解。有这么一个公式

$$Fibonacci\\_prime[k] = Fibonacci[prime[k]]$$

先写一个程序，可以看出第22000个Fibonacci素数大概要到240000这么多项数。一开始我是用JAVA直接推出来，然后输出。可是BigInteger的数组开不到这么大（ ＴДＴ）。

原来稍微处理一下就可以了。

因为只要前九位，所以只要大于$1e9$的时候除以10就行，然后前一项也要相应地对位。最后输出整数部分。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748

| ```c++
#include <bits/stdc++.h>using namespace std;const int MAXN = 250000;const int MAX = 1e9; double fibo[MAXN];int prime[MAXN], vis[MAXN]; void Init(){    int k = 1;    for (int i = 2; i < 500; i++)        if (!vis[i])        {            for (int j = i * i; j < MAXN; j += i)                vis[j] = 1;        }    for (int i = 2; i < MAXN; i++)        if (!vis[i])            prime[k++] = i;    fibo[1] = fibo[2] = 1;    int flag = 0;    for (int i = 3; i < MAXN; i++)    {        fibo[i] = fibo[i - 1];        if (flag)            fibo[i] += fibo[i - 2] / 10;        else            fibo[i] += fibo[i - 2];        flag = 0;        while (fibo[i] >= MAX)        {            flag = 1;            fibo[i] /= 10;        }    }    prime[1] = 3, prime[2] = 4;} int main(){    //freopen("input.txt", "r", stdin);    Init();    int n;    while (~scanf("%d", &n))        printf("%d\n", (int)fibo[prime[n]]);    return 0;}
```