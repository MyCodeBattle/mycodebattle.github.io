---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 10730 - Antiarithmetic? (等差数列)
tags: []
layout: post
---

#  [UVa 10730 - Antiarithmetic? (等差数列)](/2015/01/UVa-10730/ "UVa 10730 - Antiarithmetic? \(等差数列\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 31 2015 23:55

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

判断一个数列中会不会出现3个的等差数

## 思路

记录每个数的位置

直接枚举公差，复杂度$O(nlogn)$

## 代码
    
    
    1234567891011121314151617181920212223242526272829

| 
    
    
    int pos[MAXN]; int main(){    //ROP;    int n;    while (scanf("%d:", &n), n)    {        for (int i = 0; i < n; i++)        {            int tmp;            scanf("%d", &tmp);            pos[tmp] = i;        }        bool flag = false;        for (int i = 0; i < n; i++)        {            if (flag) break;            for (int j = 1; i + 2*j < n; j++)            {                if (pos[i] < pos[i+j] && pos[i+j] < pos[i+2*j]) flag = true;                if (pos[i] > pos[i+j] && pos[i+j] > pos[i+2*j]) flag = true;                if (flag) break;            }        }        printf("%s\n", flag ? "no": "yes");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Math - Others](/tags/Math-Others/)
