---
categories: Posts
date: 2014-08-01 00:00:00
title: Codeforces 459C - Pashmak and Buses
tags: []
layout: post
---

## 传送门

[Codeforces 459C - Pashmak and Buses](http://www.bnuoj.com/v3/problem_show.php?pid=39923)

## 题意

有N个人，K辆车，要去D天，输出没有两个人一直坐一辆车的方案。

## 思路

暴力就行。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int MAXN = 1000 + 5; int mp[MAXN][MAXN], n, k, d, cnt = 0, tmp[MAXN]; bool Judge(){    int temp = 1;    for (int i = 0; i < d; i++)    {        temp *= k;        if (temp >= n)            return true;    }    return false;} void DFS(int cur){    if (cnt == n)        return;    if (cur == d)    {        memcpy(mp[cnt++], tmp, sizeof tmp);        return;    }    int &t = tmp[cur];    for (t = 1; t <= k; t++)        DFS(cur + 1);} int main(){    //freopen("input.txt", "r", stdin);    int i, j;    scanf("%d%d%d", &n, &k, &d);    if (!Judge())    {        printf("-1\n");        return 0;    }    if (k > 1000) k = 1000;    DFS(0);    for (i = 0; i < d; i++)        for (j = 0; j < n; j++)            j == n - 1 ? printf("%d\n", mp[j][i]) : printf("%d ", mp[j][i]);    return 0;}
```