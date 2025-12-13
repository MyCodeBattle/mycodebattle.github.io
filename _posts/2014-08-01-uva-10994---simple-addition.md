---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10994 - Simple Addition
tags: []
layout: post
---

## 传送门

[UVa 10994 - Simple Addition](http://vjudge.net/problem/viewProblem.action?id=23306)

## 题意

按要求求和

## 思路

先打个表，发现随着n的增大，结果为

0 1 2 3 4 5 6 7 8 9  
1 1 2 3 4 5 6 7 8 9  
2 1 2 3 4 5 6 7 8 9

以此类推。所以可以计算出有几个10，再对个位求和。至于十位的那个数，将原数/10，就相当于计算这个数，可以写成迭代也可以递归。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
#pragma comment(linker, "/STACK:102400000,102400000")
 
LL Cal(LL n)
{
    LL ans = 0;
    while (n)
    {
        int t = n % 10;
        n /= 10;
        ans += (1 + t) * t / 2 + 45 * n;
    }
    return ans;
}
 
int main()
{
    LL p, q;
    int i, j;
    while (scanf("%lld%lld", &p, &q), p + q >= 0)
    {
        if (p == q)
            printf("%lld\n", Cal(q));
        else
            printf("%lld\n", Cal(q) - Cal(p - 1));
    }
    return 0;
}
```