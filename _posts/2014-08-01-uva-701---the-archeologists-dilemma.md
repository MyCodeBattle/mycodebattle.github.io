---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 701 - The Archeologists' Dilemma
tags: []
layout: post
---

#  [UVa 701 - The Archeologists' Dilemma](/2014/08/UVa-701/ "UVa 701 - The Archeologists' Dilemma")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 9 2014 14:54

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 701 - The Archeologists’ Dilemma](http://vjudge.net/problem/viewProblem.action?id=20528)

## 题意

给出一个数n，这个数是$2^e$的前部分，现在求出最小的e。

## 思路

想不到可以枚举位数。参考了Staginner。

$$n * 10^x <= 2^e$$

$$(n + 1) * 10^x > 2^e$$

然后解出e。

## 代码
    
    
    12345678910111213141516171819202122232425

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000") int main(){    int i, j, e, a;    char str[100];    while (~scanf("%d", &a))    {        sprintf(str, "%d", a);        for (i = strlen(str) + 1; ; i++)        {            int x = (int)(log2(a) + i * log2(10));            int y = (int)(log2(a + 1) + i * log2(10));            if (x != y)            {                printf("%d\n", y);                break;            }        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Foundation - Brute Force](/tags/Foundation-Brute-Force/)[Online Judge - UVa](/tags/Online-Judge-UVa/)
