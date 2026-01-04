---
categories: Posts
date: 2014-08-03 00:00:00
title: UVa 10229 - Modular Fibonacci
tags: []
layout: post
---

## 传送门

[UVa 10229 - Modular Fibonacci](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1170)

## 思路

矩阵快速幂取模。上面那题用了别人的模板，早上又重新理了一遍快速幂、快速幂取模，做这题的时候理了一下矩阵快速幂。

理解了以后就发现上次的模板有问题。果然模板还是要自己写。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
 
struct MATRIX
{
    LL mat[2][2];
};
 
MATRIX ans, temp;
LL mod;
 
MATRIX Calc(MATRIX a, MATRIX b)
{
    MATRIX t;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            t.mat[i][j] = (a.mat[i][0] * b.mat[0][j] + a.mat[i][1] * b.mat[1][j]) % mod;
    return t;
}
 
void Init()
{
    temp.mat[0][0] = 1, temp.mat[0][1] = 1;
    temp.mat[1][0] = 1, temp.mat[1][1] = 0;
    ans.mat[0][0] = 1, ans.mat[1][1] = 1;
    ans.mat[0][1] = ans.mat[1][0] = 0;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, m[22];
    LL n;
    for (i = 0; i <= 21; i++)
        m[i] = (1 << i);
    while (~scanf("%lld%lld", &n, &mod))
    {
        mod = m[mod];
        Init();
        while (n)
        {
            if (n & 1)
                ans = Calc(temp, ans);
            temp = Calc(temp, temp);
            n >>= 1;
        }
        printf("%lld\n", (ans.mat[1][0]) % mod);
    }
    return 0;
}
```