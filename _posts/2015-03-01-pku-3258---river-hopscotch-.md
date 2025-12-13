---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 3258 - River Hopscotch (二分)
tags: []
layout: post
---

## 题意

消去M个石块，问石块间最短距离的最大值是多少。

## 思路

二分 + 检查。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142

| ```c++
int arr[MAXN];int vis[MAXN]; int L, N, M;bool Check(int num){    int cur = 0, cnt = 0;    for (int i = 1; i < N; i++)    {        if (arr[i] - arr[cur] < num)        {            cnt++;            if (cnt > M) return false;        }        else cur = i;    }    return true;} int main(){    //ROP;    scanf("%d%d%d", &L, &N, &M);    for (int i = 0; i < N; i++) scanf("%d", &arr[i]);    arr[N] = 0; arr[N+1] = L;    N += 2;    sort(arr, arr+N);    int l = 0, r = L, ans = L;    while (l <= r)    {        int mid = MID(l, r);        if (Check(mid))        {            ans = mid;            l = mid+1;        }        else r = mid-1;    }    printf("%d\n", ans);    return 0;}
```