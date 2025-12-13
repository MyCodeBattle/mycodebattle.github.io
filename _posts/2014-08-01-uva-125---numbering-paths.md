---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 125 - Numbering Paths
tags: []
layout: post
---

## 传送门

[UVa 125 - Numbering Paths](http://vjudge.net/vjudge/problem/viewProblem.action?id=24951)

## 思路

如果用Floyd算过之后mp[i][i]不是0，说明存在环，这时候经过这个结点的路全部变成-1.

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int VMAXN = 30 + 5;const int INF = 0x3f3f3f3f; int mp[VMAXN][VMAXN], n; void Floyd(){    for (int k = 0; k <= n; k++)        for (int i = 0; i <= n; i++)            for (int j = 0; j <= n; j++)                mp[i][j] += mp[i][k] * mp[k][j];    for (int i = 0; i <= n; i++)        if (mp[i][i] != 0)            for (int j = 0; j <= n; j++)                for (int k = 0; k <= n; k++)                    if (mp[j][i] && mp[i][k])                        mp[j][k] = -1;} int main(){    //freopen("input.txt", "r", stdin);    int i, j, cases = 0, a, b, N;    while (~scanf("%d", &N))    {        memset(mp, 0, sizeof mp);        n = 0;        for (i = 0; i < N; i++)        {            scanf("%d%d", &a, &b);            mp[a][b] = 1;            n = max(n, max(a, b));        }        Floyd();        printf("matrix for city %d\n", cases++);        for (i = 0; i <= n; i++)        {            for (j = 0; j <= n; j++)                j == 0 ? printf("%d", mp[i][j]) : printf(" %d", mp[i][j]);            printf("\n");        }    }    return 0;}
```