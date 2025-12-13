---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 5171 - GTY's birthday gift (矩阵快速幂)
tags: []
layout: post
---

#  [HDU 5171 - GTY's birthday gift (矩阵快速幂)](/2015/02/HDU-5171/ "HDU 5171 - GTY's birthday gift \(矩阵快速幂\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 7 2015 23:51

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

中文题

## 思路

推一下。

前两个元素为a、b。

a+b, a+2b, 2a+3b, 3a+5b…

可以看出是一个Fibonacci数列类似。

那么可以构造出一个矩阵

$$ \begin{bmatrix} 1 & 1 & 1 \\\ 0 & 1 & 1 \\\ 0 & 1 & 0 \\\ \end{bmatrix} \begin{bmatrix} S_{n-1} \\\ F_{n-1} \\\ F_{n-2} \\\ \end{bmatrix} = \begin{bmatrix} S_n \\\ F_n \\\ F_{n-1} \\\ \end{bmatrix} $$

然后就矩阵快速幂了。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455

| 
    
    
    struct MATRIX{    int mat[3][3];}; MATRIX Pro(MATRIX &a, MATRIX &b){    MATRIX res;    MS(res.mat, 0);    for (int k = 0; k < 3; k++)        for (int i = 0; i < 3; i++)            for (int j = 0; j < 3; j++)                res.mat[i][j] = (res.mat[i][j] + (LL)a.mat[i][k] * b.mat[k][j]) % MOD;    return res;} int n, arr[MAXN]; void Init(MATRIX &a, MATRIX &b){    a.mat[0][0] = arr[n-1] + arr[n-2], a.mat[1][0] = arr[n-1], a.mat[2][0] = arr[n-2];    b.mat[0][0] = 1, b.mat[0][1] = 1, b.mat[0][2] = 1;    b.mat[1][0] = 0, b.mat[1][1] = 1, b.mat[1][2] = 1;    b.mat[2][0] = 0, b.mat[2][1] = 1, b.mat[2][2] = 0;} MATRIX MatrixQuickMod(int n){    MATRIX ans, tmp;    MS(ans.mat, 0); MS(tmp.mat, 0);    Init(ans, tmp);    while (n)    {        if (n & 1) ans = Pro(tmp, ans);        tmp = Pro(tmp, tmp);        n >>= 1;    }    return ans;} int main(){    //ROP;    int k;    while (~scanf("%d%d", &n, &k))    {        LL sum = 0;        for (int i = 0; i < n; i++) scanf("%d", &arr[i]), sum += arr[i];        sort(arr, arr + n);        sum -= arr[n-1] + arr[n-2];        MATRIX ans = MatrixQuickMod(k);        printf("%d\n", (sum + ans.mat[0][0]) % MOD);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Matrix](/tags/Math-Matrix/)
