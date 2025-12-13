---
categories: Posts
date: 2014-08-01 00:00:00
title: HDU 1856 - More is better
tags: []
layout: post
---

## 传送门

[HDU 1856 - More is better](http://www.bnuoj.com/v3/problem_show.php?pid=6005)

## 题意

一群人，有一些朋友，最后要留下朋友圈最大的，问最大的有多少人。

## 思路

一开始没想到在路径压缩的同时维护父结点的朋友圈数量，还想在全部弄完之后再扫描一遍。。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>#include <map>#define MP(a, b) make_pair(a, b)using namespace std;const int MAXN = 1e7 + 5;const int INF = 0x3f3f3f3f; int pa[MAXN], cnt[MAXN]; int Find(int x){    return pa[x] == x ? x : pa[x] = Find(pa[x]);} int main(){    //freopen("input.txt", "r", stdin);    int n, i, j, a, b;    while (~scanf("%d", &n))    {        if (n == 0)        {            printf("1\n");            continue;        }        int nmax = -1, nmin = INF;        for (i = 0; i < MAXN; i++)            pa[i] = i, cnt[i] = 1;        for (i = 0; i < n; i++)        {            scanf("%d%d", &a, &b);            nmax = max(max(a, b), nmax);            nmin = min(min(a, b), nmin);            int x = Find(a), y = Find(b);            if (x != y)            {                pa[x] = y;                cnt[y] += cnt[x];            }        }        int ans = 0;        for (i = nmin; i <= nmax; i++)            ans = max(ans, cnt[i]);        printf("%d\n", ans);    }    return 0;}
```