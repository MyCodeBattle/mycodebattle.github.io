---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 106 - Fermat vs. Pythagoras
tags: []
layout: post
---

#  [UVa 106 - Fermat vs. Pythagoras](/2014/07/UVa-106/ "UVa 106 - Fermat vs. Pythagoras")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 26 2014 17:31

**Contents**

  1. 1. 传送门
  2. 2. 思路
  3. 3. 代码

## 传送门

[UVa 106 - Fermat vs. Pythagoras](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=115&page=show_problem&problem=42)

## 思路

继续学习。

参考了[程序控的题解](http://www.cnblogs.com/devymex/archive/2010/08/07/1799713.html)

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 1e6 + 100;const int INF = 0x3f3f3f3f; int vis[MAXN]; int GCD(int a, int b){    return b == 0 ? a : GCD(b, a % b);} int main(){    //freopen("input.txt", "r", stdin);    int fcnt, scnt, i, j, n, x, y, z;    while (~scanf("%d", &n))    {        memset(vis, 0, sizeof vis);        fcnt = scnt = 0;        int imax = (int)sqrt((double)n + 0.5);        for (i = 1; i <= imax; i++)        {            for (j = i + 1; j <= imax; j += 2)            {                if (GCD(i, j) != 1)                    continue;                z = i * i + j * j;                if (z > n)                    break;                x = 2 * i * j;                y = j * j - i * i;                fcnt++;                for (int k = 1; z * k <= n; k++)                    vis[k * x] = vis[k * y] = vis[k * z] = 1;            }        }        for (i = 1; i <= n; i++)            if (!vis[i])                scnt++;        printf("%d %d\n", fcnt, scnt);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Math - Number Theory](/tags/Math-Number-Theory/)
