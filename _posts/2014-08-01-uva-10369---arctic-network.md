---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10369 - Arctic Network
tags: []
layout: post
---

## 传送门

[UVa 10369 - Arctic Network](http://vjudge.net/problem/toListProblem.action)

## 题意

有几个前哨，要联网，现在有n颗卫星，一颗卫星可以给两个岛无视距离通信！剩下的只能用无线电了，求无线电最小的距离。

## 思路

构建一个MST，因为是从小到大加入边，把卫星给最长的那几条边，就是求第n-k条边的权。所以只要加到第n-k条就可以输出了。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long longconst int VMAXN = 500 + 10;const int DMAXN = VMAXN * VMAXN >> 1; struct POINT{    int x, y;}pit[VMAXN]; int u[DMAXN], v[DMAXN], n, p[VMAXN], r[DMAXN], nsate, noutp;double dis[DMAXN]; int cmp(const int i, const int j){    return dis[i] < dis[j];} int Find(const int x){    return p[x] == x ? x : (p[x] = Find(p[x]));} void Kruskal(){    int i, cnt = 0;    for (i = 1; i <= noutp; i++)        p[i] = i;    for (i = 0; i < n; i++)        r[i] = i;    sort(r, r + n, cmp);    for (i = 0; i < n; i++)    {        int e = r[i];        int x = Find(u[e]), y = Find(v[e]);        if (x != y)        {            cnt++, p[x] = y;            if (cnt == noutp - nsate)            {                printf("%.2f\n", dis[e]);                return;            }         }    }} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, a, b;    scanf("%d", &T);    while (T--)    {        n = 0;        scanf("%d%d", &nsate, &noutp);        for (i = 1; i <= noutp; i++)            scanf("%d%d", &pit[i].x, &pit[i].y);        for (i = 1; i <= noutp; i++)            for (j = i + 1; j <= noutp; j++)            {                u[n] = i, v[n] = j;                dis[n++] = hypot(pit[i].x - pit[j].x, pit[i].y - pit[j].y);            }        Kruskal();    }    return 0;}
```