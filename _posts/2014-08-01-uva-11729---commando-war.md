---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11729 - Commando War
tags: []
layout: post
---

## 传送门

[UVa 11729 - Commando War](http://vjudge.net/vjudge/problem/viewProblem.action?id=28436)

## 题意

有N个士兵，每个人交代任务要B分钟，执行任务要J分钟，要求输出最少完成任务用时

## 思路

贪心，按执行时间从大到小排

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#define MP(a, b) make_pair(a, b)const int MAXN = 1000 + 10;const int INF = 0x3f3f3f3f; struct P{    int b, j;    bool operator < (const P &a) const    {        return j > a.j;    }}pp[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, i, j, cases = 0;    while (scanf("%d", &n), n)    {        for (i = 0; i < n; i++)            scanf("%d%d", &pp[i].b, &pp[i].j);        sort(pp, pp + n);        int ans = 0, vt = 0;        for (i = 0; i < n; i++)        {            vt += pp[i].b;            ans = max(ans, vt + pp[i].j);        }        printf("Case %d: %d\n", ++cases, ans);    }    return 0;}
```