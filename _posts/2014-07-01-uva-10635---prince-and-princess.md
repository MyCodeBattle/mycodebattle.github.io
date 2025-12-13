---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10635 - Prince and Princess
tags: []
layout: post
---

## 传送门

[UVa 10635 - Prince and Princess](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1576)

## 思路

学习了LCS的$O(nlogn)$解法。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041

| ```c++
#include <bits/stdc++.h>using namespace std;const int INF = 0x3f3f3f3f;int Hash[70000];int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, an, bn, n, cases = 0;    scanf("%d", &T);    while (T--)    {        memset(Hash, 0, sizeof Hash);        vector<int> ve;        scanf("%d%d%d", &n, &an, &bn);        int temp = 1;        //ve.push_back(temp);        for (i = 1; i <= an + 1; i++)        {            scanf("%d", &temp);            Hash[temp] = i;        }        for (i = 0; i <= bn; i++)        {            scanf("%d", &temp);            if (temp == 0)                continue;            int v = Hash[temp];            if (ve.empty() || v > ve.back())                ve.push_back(v);            else            {                int t = lower_bound(ve.begin(), ve.end(), v) - ve.begin();                ve[t] = v;            }        }        printf("Case %d: %d\n", ++cases, ve.size());    }    return 0;}
```