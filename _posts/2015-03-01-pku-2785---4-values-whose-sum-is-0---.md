---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2785 - 4 Values whose Sum is 0 (二分 + 思维)
tags: []
layout: post
---

## 题意

找出四元组a+b+c+d=0的个数。

## 思路

枚举a+b，找c+d。

用map竟然TLE了，明明和手动二分一样的复杂度。

## 代码
    
    
    12345678910111213141516171819202122232425262728

| ```c++
vector<int> s1, s2;int a[MAXN], b[MAXN], c[MAXN], d[MAXN];int main(){    //ROP;    int n;    while (~scanf("%d", &n))    {        s1.clear(); s2.clear();        for (int i = 0; i < n; i++) scanf("%d%d%d%d", &a[i], &b[i], &c[i], &d[i]);        for (int i = 0; i < n; i++)            for (int j = 0; j < n; j++)            {                s1.PB(a[i]+b[j]);                s2.PB(-c[i]-d[j]);            }        int cnt = 0;        sort(s2.begin(), s2.end());        for (int i = 0; i < SZ(s1); i++)        {            int x = lower_bound(s2.begin(), s2.end(), s1[i]) - s2.begin();            int y = upper_bound(s2.begin(), s2.end(), s1[i]) - s2.begin();            cnt += y-x;        }        printf("%d\n", cnt);    }    return 0;}
```