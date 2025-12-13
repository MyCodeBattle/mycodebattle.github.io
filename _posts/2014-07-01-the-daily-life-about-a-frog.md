---
categories: Posts
date: 2014-07-01 00:00:00
title: The daily life about a frog.
tags: []
layout: post
---

## 传送门

[UVa 357 - Let Me Count The Ways](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=293&mosmsg=Submission+received+with+ID+13826217)

## 思路

因为不想在一片绿色中空出一道白色才做的。

## 代码

[CODE_BLOCK_0]| ```c++
#include <cstdio>#include <cstring>#include <algorithm>#define LL long longusing namespace std;const int MAXN = 30000 + 100;const int mon[] = {1, 5, 10, 25, 50};LL d[MAXN][5];LL DP(int rim, int us){    LL &ans = d[rim][us];    if (ans != -1)        return ans;    ans = 0;    for (int i = us; i < 5; i++)        if (rim >= mon[i])            ans += DP(rim - mon[i], i);    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int temp;    LL i, j, ans, money;    memset(d, -1, sizeof(d));    for (i = 0; i < 5; i++)        d[0][i] = 1;    while (~scanf("%d", &temp))    {        ans = DP(temp, 0);        if (ans == 1)            printf("There is only 1 way to produce %d cents change.\n", temp);        else            printf("There are %lld ways to produce %d cents change.\n", ans, temp);    }    return 0;}
```  
---|---