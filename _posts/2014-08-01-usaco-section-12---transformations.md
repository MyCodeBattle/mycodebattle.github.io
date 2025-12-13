---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.2 - Transformations
tags: []
layout: post
---

## 题意

给一个图，问经过哪一步骤可以得到结果图

## 思路

感觉做这些题目一点快感都没有（ ＴДＴ）

模拟，实际上只需要两个函数就行，一个是旋转90°的函数，另一个是对称的函数。

用image数组保存当前的状态，转一下判断一下。所以1~3步骤可以合并。之后也挺简单的，不多说了

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596

| ```c++
/*ID: mycodeb1LANG: C++TASK: transform*/ #include <bits/stdc++.h>using namespace std;const int MAXN = 10 + 2; int n;char mp[MAXN][MAXN], res[MAXN][MAXN], image[MAXN][MAXN]; void reNew(){    for (int i = 0; i < n; i++)        strcpy(image[i], mp[i]);} bool Check(){    for (int i = 0; i < n; i++)        for (int j = 0; j < n; j++)            if (res[i][j] != image[i][j])                return false;    return true;} void Rotate(){    char temp[MAXN][MAXN];    for (int i = 0; i < n; i++)        for (int j = 0; j < n; j++)            temp[j][n - 1 - i] = image[i][j];    for (int i = 0; i < n; i++)        strcpy(image[i], temp[i]);} void Reflection(){    char temp[MAXN][MAXN];    for (int i = 0; i < n; i++)        for (int j = 0; j < n; j++)            temp[i][n - 1 - j] = image[i][j];    for (int i = 0; i < n; i++)        strcpy(image[i], temp[i]);} int main(){    //freopen("input.txt", "r", stdin);    freopen("transform.in", "r", stdin);    freopen("transform.out", "w", stdout);    ios::sync_with_stdio(false);     int i, j;    scanf("%d%*c", &n);    for (i = 0; i < n; i++)        gets(mp[i]);    for (i = 0; i < n; i++)        gets(res[i]);    reNew();    for (i = 1; i <= 3; i++)    {        Rotate();        if (Check())        {            printf("%d\n", i);            return 0;        }    }    reNew();    Reflection();    if (Check())    {        printf("4\n");        return 0;    }    for (i = 0; i < 3; i++)    {        Rotate();        if (Check())        {            printf("5\n");            return 0;        }    }    reNew();    if (Check())    {        printf("6\n");        return 0;    }    printf("7\n");    return 0;}
```