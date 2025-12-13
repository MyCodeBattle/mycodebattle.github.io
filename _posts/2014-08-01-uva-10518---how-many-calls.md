---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10518 - How Many Calls?
tags: []
layout: post
---

## 传送门

[UVa 10518 - How Many Calls?](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1459)

## 题意

求第n项Fibonacci数列的计算次数。

## 思路

可以通过打表发现次数为2 * F(n) - 1。所以就变成了计算F(n)。

可是n很大，$O(n)$也会超时，然后就学习了矩阵快速幂。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

| ```c++
#include <bits/stdc++.h>#define LL long longusing namespace std; struct MATRIX{    LL mat[2][2];}; MATRIX ans, temp;LL mod; MATRIX Calc(MATRIX a, MATRIX b){    MATRIX t;    for (int i = 0; i < 2; i++)        for (int j = 0; j < 2; j++)            t.mat[i][j] = (a.mat[i][0] * b.mat[0][j] + a.mat[i][1] * b.mat[1][j]) % mod;    return t;} void Init(){    temp.mat[0][0] = 1, temp.mat[0][1] = 1;    temp.mat[1][0] = 1, temp.mat[1][1] = 0;    ans.mat[0][0] = ans.mat[1][1] = 1;    ans.mat[0][1] = ans.mat[1][0] = 0;} int main(){    //freopen("input.txt", "r", stdin);    int i, j, cases = 0;    LL n;    while (scanf("%lld%lld", &n, &mod), n + mod)    {        printf("Case %d: %lld %lld ", ++cases, n, mod);        n++;        Init();        while (n)        {            if (n & 1)                ans = Calc(temp, ans);            temp = Calc(temp, temp);            n >>= 1;        }        printf("%lld\n", (ans.mat[1][0] * 2 - 1 + mod) % mod);    }    return 0;}
```