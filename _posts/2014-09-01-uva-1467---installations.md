---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1467 - Installations
tags: []
layout: post
---

#  [UVa 1467 - Installations](/2014/09/UVa-1467/ "UVa 1467 - Installations")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 13 2014 10:51

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 1467 - Installations](http://www.bnuoj.com/v3/problem_show.php?pid=37084)

## 题意

安装东西，给出安装时间和最后期限，罚时按超过最后期限X天计算。求最大罚时和次大罚时最小是多少。

## 思路

一开始想二分的，后来发现没用。

参考了他人的思路。

首先按照最后期限排序，这样可以得出最大罚时最小的解，记录位置。

因为可能前面的有些任务可能罚时不够第二大罚时，把它移到第一第二罚时后面以后还可能不够，但是这样一移第一第二罚时就减少了。

（虽然这样说得通，但是还是不太明白。日后再想想）

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384

| 
    
    
    ​#include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 500 + 5;const int INF = 0x3f3f3f3f;using namespace std; struct POINT{    int last, dead, pani;    POINT() : pani(0) {}    bool operator < (const POINT &a) const    {        if (dead != a.dead) return dead < a.dead;        else return last < a.last;    }}pit[MAXN]; int pos; void Update(const int pani, int &firMax, int &secMax){    if (pani > firMax)    {        secMax = firMax;        firMax = pani;    }    else if (pani > secMax) secMax = pani;} int Check(int ele){    int firMax = 0, secMax = 0;    int pas = 0;    for (int i = 0; i <= pos; i++)    {        if (i == ele) continue;        pas += pit[i].last;        int pani = max(0, pas - pit[i].dead);        Update(pani, firMax, secMax);    }    pas += pit[ele].last;    int pani = max(0, pas - pit[ele].dead);    Update(pani, firMax, secMax);    return firMax + secMax;} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, n;    scanf("%d", &T);    while (T--)    {        int sum = 0, firMax = 0, secMax = 0;        scanf("%d", &n);        for (i = 0; i < n; i++)            scanf("%d%d", &pit[i].last, &pit[i].dead);        sort(pit, pit + n);        int pas = 0;        for (i = 0; i < n; i++)        {            pas += pit[i].last;            int t = max(pas - pit[i].dead, 0);            if (t > firMax)            {                pos = i;                secMax = firMax;                firMax = t;            }            else if (t > secMax)            {                pos = i;                secMax = t;            }        }        int ans = firMax + secMax;        for (i = 0; i < pos; i++)            ans = min(ans, Check(i));        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)
