---
categories: Posts
date: 2014-07-30 00:00:00
title: UVa 10105 - Polynomial Coefficients
tags: []
layout: post
---

## 传送门

[UVa 10105 - Polynomial Coefficients](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1046&mosmsg=Submission+received+with+ID+13965168)

## 题意

求$ \left( a+b+\ldots +d\right) ^{n} $中 $ a^{n_1}b^{n_2}c^{n_3}\ldots d^{n_i} $的系数, $ n_{1}+n_{2}+\ldots +n_{i}=n $

## 思路

根据多项式公式  
$$ T_{r+1}=C_{n}^{r}\cdot a^{n-r}\cdot b^{r} $$

然后看成两项，就成了  
$$\dfrac {n!} {k_{0}\cdot \left({n-k_0}!\right)}\cdot \dfrac {\left( n-k_{0}\right) !} {k_{1}!\cdot \left( n-k_0 - k_1\right)! }$$

约分，以此类推，最后只剩$n!$除以每项的阶乘

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
 
int fac[20];
 
void Fac()
{
    fac[1] = fac[0] = 1;
    for (int i = 2; i <= 14; i++)
        fac[i] = fac[i - 1] * i;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    Fac();
    int n, k, i, j, temp;
    while (~scanf("%d%d", &n, &k))
    {
        int ans = fac[n];
        for (i = 0; i < k; i++)
        {
            scanf("%d", &temp);
            ans /= fac[temp];
        }
        printf("%d\n", ans);
    }
    return 0;
}
```