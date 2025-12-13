---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11520 - Fill the Square
tags: []
layout: post
---

#  [UVa 11520 - Fill the Square](/2014/09/UVa-11520/ "UVa 11520 - Fill the Square")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 1 2014 19:11

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11520 - Fill the Square](http://www.bnuoj.com/v3/problem_show.php?pid=19938)

## 题意

给一个图填上英文，要求上下左右不能有相同的，字典序从左到右从上到下最小。

## 思路

暴力。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 10 + 5;const int INF = 0x3f3f3f3f;using namespace std; char mp[MAXN][MAXN]; int main(){    //freopen("input.txt", "r", stdin);    bool flag;    int T, i, j, n, cases = 0;    scanf("%d", &T);    while (T--)    {        scanf("%d%*c", &n);        for (i = 0; i < n; i++)            gets(mp[i]);        for (i = 0; i < n; i++)            for (j = 0; j < n; j++)            {                if (mp[i][j] == '.')                {                    for (char k = 'A'; k <= 'Z'; k++)                    {                        flag = true;                        if (i > 0 && k == mp[i - 1][j]) flag = false;                        if (i < n - 1 && k == mp[i + 1][j]) flag = false;                        if (j > 0 && k == mp[i][j - 1]) flag = false;                        if (j < n - 1 && k == mp[i][j + 1]) flag = false;                        if (flag)                        {                            mp[i][j] = k;                            break;                        }                    }                }            }        printf("Case %d:\n", ++cases);        for (i = 0; i < n; i++)            puts(mp[i]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)
