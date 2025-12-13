---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 696 - How Many Knights
tags: []
layout: post
---

## 传送门

[UVa 696 - How Many Knights](http://vjudge.net/problem/viewProblem.action?id=23153)

## 题意

一个nXm的棋盘上能放几只马

## 思路

一开始以为能DP，YY了好久也没出来。可耻地看了别人的结论。

如果row >= 2的话，隔一个放一个是最多的。row = 2 和row = 1讨论一下即可。

## 代码
    
    
    123456789101112131415161718192021222324

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000") int main(){    int row, col, i, j, a, b, ans;    while (scanf("%d%d", &a, &b), a + b)    {        row = min(a, b);        col = max(a, b);        if (row == 1)            printf("%d knights may be placed on a %d row %d column board.\n", a * b, a, b);        else if (row == 2)        {            ans = 4 * (col / 4) + 2 * (col % 4 <= 2 ? col % 4 : 2);            printf("%d knights may be placed on a %d row %d column board.\n", ans,  a, b);        }        else            printf("%d knights may be placed on a %d row %d column board.\n", (a * b + 1) >> 1, a, b);    }    return 0;}
```