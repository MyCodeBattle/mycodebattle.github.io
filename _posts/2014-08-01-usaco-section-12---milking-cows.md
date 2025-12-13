---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.2 - Milking Cows
tags: []
layout: post
---

## 题意

奶农喂奶牛，求最长连续喂养时间和最长停断时间

## 思路

一开始我想了一个非常2的做法：开一个vis数组，把每次开始到结束的时间全标记上，然后来计算。。。做完了才发现这是多此一举（ ＴДＴ）只要记录下当前最长的结束时间和开始时间就行。

情况就两种

  1. 当前开始时间不在之前的区间里，这时候就结算以前的结果，重新开始。

  2. 在之前的区间里，更新结束的最大值。


因为最后一只奶牛情况没有结算，所以要另外算一次，不过USACO里没有这样的数据。

比如

2  
100 200  
300 1100

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| ```c++
/*ID: mycodeb1LANG: C++TASK: milk2*/ #include <bits/stdc++.h>using namespace std;const int MAXN = 1000000 + 10; struct COW{    int st, ed;    bool operator < (const COW &a) const    {        return st < a.st;    }}cow[5100]; int main(){    //freopen("input.txt", "r", stdin);    freopen("milk2.in", "r", stdin);    freopen("milk2.out", "w", stdout);    ios::sync_with_stdio(false);     int n, i, j, st, eat, noeat, ed;    scanf("%d", &n);    for (i = 0; i < n; i++)        scanf("%d%d", &cow[i].st, &cow[i].ed);    sort(cow, cow + n);    st = cow[0].st, ed = cow[0].ed, eat = ed - st, noeat = 0;    for (i = 1; i < n; i++)    {        if (cow[i].st <= ed)            ed = max(ed, cow[i].ed);        if (cow[i].st > ed)        {            eat = max(eat, ed - st);            noeat = max(noeat, cow[i].st - ed);            st = cow[i].st, ed = cow[i].ed;        }    }​    eat = max(eat, cow[i - 1].ed - st);    printf("%d %d\n", eat, noeat);    return 0;}
```  

2B代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152

| ```c++
/*ID: mycodeb1LANG: C++TASK: milk2*/ #include <bits/stdc++.h>using namespace std;const int MAXN = 1000000 + 10; struct COW{    int st, ed;    bool operator < (const COW &a) const    {        return st < a.st;    }}cow[5100]; int vis[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    freopen("milk2.in", "r", stdin);    freopen("milk2.out", "w", stdout);    ios::sync_with_stdio(false);     int n, i, j, st, eat, noeat, ed;    scanf("%d", &n);    for (i = 0; i < n; i++)        scanf("%d%d", &cow[i].st, &cow[i].ed);    sort(cow, cow + n);    st = cow[0].st, eat = cow[0].ed - cow[0].st, noeat = 0, ed = 0;    vis[st] = 1;    for (i = 0; i < n; i++)    {        if (!vis[cow[i].st])        {            eat = max(eat, ed - st);            noeat = max(noeat, cow[i].st - ed);            st = cow[i].st;            ed = 0;        }        for (j = cow[i].st; j <= cow[i].ed; j++)            vis[j] = 1;        ed = max(ed, cow[i].ed);    }    eat = max(eat, cow[i - 1].ed - st);    printf("%d %d\n", eat, noeat);        return 0;}
```