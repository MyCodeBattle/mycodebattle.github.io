---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11991 - Easy Problem from Rujia Liu?
tags: []
layout: post
---

## 传送门

[UVa 11991 - Easy Problem from Rujia Liu?](http://vjudge.net/vjudge/problem/viewProblem.action?id=18696)

## 题意

给出一些序列，和几个询问，求第k个v的下标。

## 思路

用vector数组，记录下标

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e6 + 10;
const int INF = 0x3f3f3f3f;
 
vector<int> ve[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, m, i, j, a, b;
    while (~scanf("%d%d", &n, &m))
    {
        for (i = 0; i < MAXN; i++)
            ve[i].clear();
        for (i = 0; i < n; i++)
        {
            scanf("%d", &a);
            ve[a].push_back(i);
        }
        for (i = 0; i < m; i++)
        {
            scanf("%d%d", &a, &b);
            printf("%d\n", ve[b].size() >= a ? ve[b][a - 1] + 1 : 0);
        }
    }
    return 0;
}
```