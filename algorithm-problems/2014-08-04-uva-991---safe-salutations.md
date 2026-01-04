---
categories: Posts
date: 2014-08-04 00:00:00
title: UVa 991 - Safe Salutations
tags: []
layout: post
---

## 传送门

传送门坏了。

## 题意

有n对人在圆圈上，问他们有几种不交叉握手的方案

## 思路

取一个人，连结其他人。显然，这条线的左边和右边的人必须是偶数才能握手。

假设现在有n对人，方案有左边0对，右边$n - 1$对，左边1对，右边$n - 2$对，以此类推。

$$f(n) = f(0) * f(n - 1) + f(1) * f(n - 2) + … + f(n - 1) * f(0)$$

是一个Catalan数列。

可耻地套一下公式

$$ f\left( n\right) =\dfrac {f\left( n-1\right) \cdot \left( 4n-2\right) } {n+1} $$

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
 
int main()
{
    bool first = true;
    LL C[20], i;
    int n;
    C[0] = 0, C[1] = 1;
    for (i = 2; i <= 10; i++)
        C[i] = C[i - 1] * (4 * i - 2) / (i + 1);
    while (~scanf("%d", &n))
    {
        if (!first)
            printf("\n");
        first = false;
        printf("%lld\n", C[n]);
    }
    return 0;
}
```